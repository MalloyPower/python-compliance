#!/usr/bin/python

import os
import sys
import subprocess
import shutil

import re
import linecache
import tempfile

import qualitas

# This is where the Makefile lives:
FRONTEND_DIR = os.path.join(os.getcwd(), 'pycomply')

# This is what the Makefile builds:
FRONTEND_EXE = os.path.join(FRONTEND_DIR, 'run')

# I need to record errors for each processed file:
ERROR_LOG = os.path.join(os.getcwd(), 'error.log')

# The versions of Python we have front-ends for:
SERIES2 = ['2.0', '2.2', '2.3', '2.4', '2.4.3', '2.5', '2.6', '2.7', '2.7.2']
SERIES3 = ['3.0', '3.1', '3.2', '3.3.0', '3.5.0', '3.6.0']

# The versions we're using for the ESEM paper:
FOR_ESEM = ['2.5', '2.6', '2.7', '3.0', '3.1', '3.2', '3.3.0', '3.5.0']


# What are you analysing?
TEST_ROOT = qualitas.get_root_dir()


# Need to fix 'print' to be version-agnostic, even for early 2.x
def safe_print(msg, pfile=sys.stdout, pflush=False, pend='\n'):
    pfile.write(msg+pend)
    if pflush:
        pfile.flush()


def print_perc(perc):
    ''' How do you want your percentages to be printed? '''
    #return '%4.1f' % perc  # 1 decimal place
    return '\\shade{%d}' % round(perc)

class TestHarness:

    def __init__(self, version, verbose=False):
        self.noPassed = 0
        self.noFailed = 0
        self.verbose = verbose
        self.make_executable(version)

    @staticmethod
    def copy_file(srcFolder, srcFile, dstFile):
        srcPath = os.path.join(FRONTEND_DIR, srcFolder, srcFile)
        assert os.path.isfile(srcPath), 'File %s not found' % srcPath
        dstPath = os.path.join(FRONTEND_DIR, dstFile)
        shutil.copyfile(srcPath, dstPath)

    @staticmethod
    def shell_run(cmd):
        return subprocess.call(cmd, cwd=FRONTEND_DIR, shell=True)
    
    def make_executable(self, ver, forceMake=False):
        self.ver_front_end = os.path.join(FRONTEND_DIR, 'pycomply-%s' % ver)
        if forceMake or not os.path.isfile(self.ver_front_end):
            safe_print('--- Building front-end for v%s' % ver, sys.stderr)
            TestHarness.copy_file('scanners', ver+'.l', 'scan.l')
            TestHarness.copy_file('parsers', ver+'.y', 'parse.y')
            retcode = TestHarness.shell_run('make')
            assert retcode == 0, '\t*** FAILED to make the parser'
            os.rename(FRONTEND_EXE, self.ver_front_end)

    def init_counters(self):
        self.noPassed = 0
        self.noFailed = 0

    def set_verbose(self):
        self.verbose = True

    @staticmethod
    def count_tests(testpath):
        assert os.path.isdir(testpath), testpath + 'must be a directory'
        count = 0
        for _, _, files in os.walk(testpath):
            pyFiles = [filename for filename in files
                       if filename.endswith('.py')]
            count += len(pyFiles)
        return count

    def print_context(self, filename, line_no):
        for d in [line_no-1, line_no, line_no+1]:
            safe_print('%d:%s' % (d, linecache.getline(filename, d)),
                       sys.stderr, True, '')
        safe_print('')

    def check_return_code(self, retcode, testcase):
        if retcode > 0:
            if self.verbose:
                safe_print('\n* ' + testcase+ ' failed.', sys.stderr)
                try:
                    with open(ERROR_LOG, 'r') as tmp_fh:
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
                 % (testcase, self.ver_front_end, ERROR_LOG)
        retcode = TestHarness.shell_run(toExec)
        self.check_return_code(retcode, testcase)

    def test_directory(self, testpath, reinit=False):
        assert os.path.isdir(testpath), testpath + 'must be a directory'
        if reinit:
            self.init_counters()
        for root, dirs, files in os.walk(testpath):
            for filename in files:
                if filename.endswith('.py'):
                    self.test_one_file(root, filename)

    def get_total(self):
        return (self.noPassed + self.noFailed)

    def percent_passed(self):
        if self.get_total() == 0:
            return 0
        return self.noPassed * 100.0 / self.get_total()

    def __str__(self):
        return '%d Passed, %d Failed (%5.2f%% passed)' \
                % (self.noPassed, self.noFailed, self.percentPassed())


def latex_table_row(data, effect=None, want_hline=False):
    lstr = lambda s: ('\\text%s{%s}' % (effect,s)) if effect else str(s)
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
        row_data[i].append('%5d' % TestHarness.count_tests(testpath))
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
    # We assemble the data column-by-column (one column per Python version)
    percs =  [[] for t in qualapps]  # one row per testcase
    for runver in pyVersions:
        harness = build_harness(runver)
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
    if versions == []: # None specified, so use *all* the Python front-ends
        versions = FOR_ESEM 
    if qualapps == []: # None specified, so test "all" the applications
        qualapps = full_suite
    return (versions, qualapps)


if __name__ == '__main__':
    versions, qualapps = get_pyvers_qualapps(sys.argv[1:])
    percs = test_all(versions, qualapps, TEST_ROOT, mk_harness)
    print_latex_table(versions, qualapps, TEST_ROOT, percs)
