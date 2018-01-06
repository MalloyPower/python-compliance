#!/usr/bin/python

'''
    Main test harness: process a directory with a specified front-end.
    Record the pass/fail counts and print a latex table with the pass rate.
    Example use:
    (1) Specify the Pythohn front-ends and the apps to process:
        qualitas_test.py 2.7 3.5 gramps astropy    # Two versions, two apps
    (2) Process all the Qualitas apps with a particular front end:
        qualitas_test.py 2.6 2.7     # Two versions, all apps
    (3) Process a given apps with all front ends:
        qualitas_test.py gramps astropy    # All versions, two apps
    This is how we get Table 1 for the ESEM 2017 paper.
'''


import os
import sys
import subprocess
import shutil

import re
import linecache

import qualitas


# The versions of Python we have front-ends for:
SERIES2 = ['2.0', '2.2', '2.3', '2.4', '2.4.3', '2.5', '2.6', '2.7', '2.7.2']
SERIES3 = ['3.0', '3.1', '3.2', '3.3.0', '3.5.0', '3.6.0']

# The versions we're using for the ESEM paper:
FOR_ESEM = ['2.5', '2.6', '2.7', '3.0', '3.1', '3.2', '3.3.0', '3.5.0']

def root_for(suite):
    if suite == 'qualitas':
        return qualitas.get_root_dir()
    # This is where I put stuff:
    JAMES_ROOT = '/media/passport/bigApps/corpus-python'
    if suite in ['getpython3', 'top20-github', 'linchen', 'destefanis']:
        return os.path.join(JAMES_ROOT, suite)
    elif suite == 'anaconda3': # Go down a layer to get SciPy sub-packages
        return os.path.join(JAMES_ROOT, suite, 'pkgs')
    assert False, 'Unknown Python test suite: '+suite

# What are you analysing?
TEST_ROOT = root_for('qualitas')

# Need to fix 'print' to be version-agnostic, even for early 2.x
def safe_print(msg, pfile=sys.stdout, pflush=False, pend='\n'):
    pfile.write(msg+pend)
    if pflush:
        pfile.flush()

class TestHarness:
    ''' Instantiate with a Python version, run over a dir of Python files.
        Records no. of pass/fail, prints nice output for syntax errors.
    '''
    
    # This is the directory where the Makefile lives:
    FRONTEND_DIR = os.path.join(os.getcwd(), 'multi-front-end')
    # This is the exe that the Makefile builds (I'll rename this):
    FRONTEND_EXE = os.path.join(FRONTEND_DIR, 'run')
    # I need to (record errors for each processed file:
    ERROR_LOG = os.path.join(os.getcwd(), 'error.log')

    def __init__(self, version, verbose=False):
        self.init_counters()
        self.verbose = verbose # If true, print syntax error messages
        self.ver_front_end = '%s-%s' % (TestHarness.FRONTEND_EXE, version)
        self.make_executable(version)

    @staticmethod
    def copy_file(srcFolder, srcFile, dstFile):
        srcPath = os.path.join(TestHarness.FRONTEND_DIR, srcFolder, srcFile)
        assert os.path.isfile(srcPath), 'File %s not found' % srcPath
        dstPath = os.path.join(TestHarness.FRONTEND_DIR, dstFile)
        shutil.copyfile(srcPath, dstPath)

    @staticmethod
    def shell_run(cmd):
        return subprocess.call(cmd, cwd=TestHarness.FRONTEND_DIR, shell=True)
    
    def make_executable(self, ver, makeCmd='make'):
        ''' Makes the executable front-end if it's not already there '''
        if not os.path.isfile(self.ver_front_end):
            safe_print('--- Building front-end for v%s' % ver, sys.stderr)
            TestHarness.copy_file('scanners', ver+'.l', 'scan.l')
            TestHarness.copy_file('parsers', ver+'.y', 'parse.y')
            retcode = TestHarness.shell_run(makeCmd)
            assert retcode == 0, '\t*** FAILED to make the parser'
            os.rename(TestHarness.FRONTEND_EXE, self.ver_front_end)

    def init_counters(self):
        self.noPassed = 0
        self.noFailed = 0

    def set_verbose(self, see_errors=True):
        self.verbose = see_errors

    def print_context(self, filename, line_no):
        ''' Print the line, and the line before and after it '''
        for d in [line_no-1, line_no, line_no+1]:
            safe_print('%d:%s' % (d, linecache.getline(filename, d)),
                       sys.stderr, True, '')
        safe_print('')

    def check_return_code(self, retcode, testcase):
        ''' Increment pass/fail counter; print error details if desired '''
        if retcode > 0:
            if self.verbose:
                safe_print('\n* ' + testcase+ ' failed.', sys.stderr)
                try:
                    with open(TestHarness.ERROR_LOG, 'r') as tmp_fh:
                        error_msg = tmp_fh.read()
                        safe_print(error_msg, sys.stderr, True, '')
                        match = re.match('^(\d+)', error_msg)
                        if match:
                            line_no = int(match.group(1))
                            self.print_context(testcase, line_no)
                except (UnicodeDecodeError) as err:
                    safe_print('Exception %s' % err, sys.stderr)
            self.noFailed += 1
        else:
            # safe_print(testcase + ' passed')
            self.noPassed += 1

    def test_one_file(self, root, filename):
        testcase = os.path.join(root, filename)
        toExec = 'sed -e \'$a\\\' "%s" | %s > %s 2>&1' \
                 % (testcase, self.ver_front_end, TestHarness.ERROR_LOG)
        retcode = TestHarness.shell_run(toExec)
        self.check_return_code(retcode, testcase)

    def test_directory(self, testpath, reinit_counters=False):
        ''' Tests all files in this directory and its subdirectories. '''
        assert os.path.isdir(testpath), testpath + 'must be a directory'
        if reinit_counters:
            self.init_counters()
        for root, dirs, files in os.walk(testpath):
            for filename in files:
                if filename.endswith('.py'):
                    self.test_one_file(root, filename)

    def get_total(self):
        ''' Return the total number of files processed (so far)'''
        return (self.noPassed + self.noFailed)

    def percent_passed(self):
        ''' Return the percentage pass rate (or 0 no files processed)'''
        if self.get_total() == 0:
            return 0
        return self.noPassed * 100.0 / self.get_total()

    def __str__(self):
        return '%d Passed, %d Failed (%5.2f%% passed)' \
                % (self.noPassed, self.noFailed, self.percentPassed())

def print_perc(perc):
    ''' How do you want your percentages to be printed? '''
    #return '%4.1f' % perc  # 1 decimal place
    return '\\shade{%d}' % round(perc)

def latex_table_row(data, effect=None, want_hline=False):
    ''' Print a single row of a latex table (to stdout) '''
    lstr = lambda s: ('\\text%s{%s}' % (effect,s)) if effect else ('%12s' % s)
    row_str = ' & '.join([lstr(d) for d in data]) + '\\\\'
    if want_hline:
        row_str += '\n\\hline'
    return row_str

def print_latex_table(pyVersions, qualapps, testroot, percs, labels=None):
    # First column of table should be the application names:
    if not labels: # Can optionally specify labels for rows
        labels = qualapps
    row_data =  [[t] for t in labels]
    # Data columns are the percentages for each version:
    for i, plist in enumerate(percs):
        row_data[i].extend([print_perc(p) for p in plist])
    # Last column should be totals for each application:
    for i,testdir in enumerate(qualapps):
        testpath = os.path.join(testroot,testdir)
        row_data[i].append('%5d' % qualitas.count_python_files(testpath))
    # Now print the table, row-by-row:
    safe_print('\\begin{tabular}{l*{%d}{c}c}' % len(pyVersions))
    safe_print(latex_table_row(['Application'] + 
                          [p for p in pyVersions] + ['Files'], 'bf', True))
    for row in row_data:
        safe_print(latex_table_row(row))
    safe_print('\\hline')
    safe_print('\\end{tabular}')

def mk_harness(runver):
    ''' Making this a function allows us to parameterise test_all '''
    return TestHarness(runver, False)

def test_all(pyVersions, qualapps,
             testroot=qualitas.get_root_dir(), build_harness=mk_harness):
    ''' For each given Python version, test each given directory.
        Optionally can specify the root (for non-Qualitas),
        and a different harness (instead of TestHarness).
    '''
    # We assemble the data column-by-column (one column per Python version)
    percs =  [[] for t in qualapps]  # one row per application
    for runver in pyVersions:
        harness = build_harness(runver)  # New harness for each version
        safe_print("Running front-end for v%s on %d apps:"
              % (runver, len(qualapps)),
              sys.stderr, True, '')
        for i,testdir in enumerate(qualapps):
            safe_print(" %s," % testdir, sys.stderr, True, '')
            harness.test_directory(os.path.join(testroot,testdir), True)
            percs[i].append(harness.percent_passed())
        safe_print(' done.', sys.stderr)
    return percs


def get_pyvers_qualapps(args, test_dir=qualitas.get_root_dir()):
    ''' Use the (command-line) args to specify front-end(s) or app(s) '''
    full_suite = qualitas.get_dirnames(test_dir)
    qualapps = [ ]
    versions = [ ]
    for arg in sys.argv[1:]:
        if arg in SERIES2+SERIES3:
            versions.append(arg)
        elif arg in full_suite:
            qualapps.append(arg)
        else:
            safe_print('Unkown argument: "%s"' % arg, sys.stderr)
            sys.exit(1)
    if versions == []: # None specified, so use "all" the Python front-ends
        versions = SERIES2+SERIES3 # FOR_ESEM 
    if qualapps == []: # None specified, so test "all" the applications
        qualapps = full_suite
    return (versions, qualapps)


# On the command line you can specify the Python versions to use,
# or list the Quaitas apps you want to process (or a mixture of both)
# Default is to use all (ESEM) versions to process all Qualitas apps.
if __name__ == '__main__':
    versions, qualapps = get_pyvers_qualapps(sys.argv[1:])
    percs = test_all(versions, qualapps, TEST_ROOT, mk_harness)
    print_latex_table(versions, qualapps, TEST_ROOT, percs)
