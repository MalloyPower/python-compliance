#!/usr/bin/python3

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
import codecs

import qualitas


# The versions of Python we have front-ends for:
SERIES2 = ['2.0', '2.2', '2.3', '2.4', '2.4.3', '2.5', '2.6', '2.7', '2.7.2']
SERIES3 = ['3.0', '3.1', '3.2', '3.3.0', '3.5.0', '3.6.0']

# The versions we're using for the ESEM paper:
FOR_ESEM = ['2.0', '2.2', '2.4', '2.5', '2.6', '2.7',
            '3.0', '3.1', '3.2', '3.3.0', '3.5.0', '3.6.0']

def root_for(suite):
    if suite == 'qualitas':
        return qualitas.corpus_for_year('2017')
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
    FRONTEND_DIR = os.path.join(os.path.dirname(__file__), 'multi-front-end')
    # This is the exe that the Makefile builds:
    FRONTEND_EXE = os.path.join(FRONTEND_DIR, 'pycomply')
    # I need to (record errors for each processed file:
    ERROR_LOG = os.path.join(os.getcwd(), 'error.log')

    def __init__(self, version, verbose=False):
        self.init_counters()
        self.verbose = verbose # If true, print syntax error messages
        self.ver_front_end = '%s-%s' % (TestHarness.FRONTEND_EXE, version)
        self.make_executable(version)

    def make_command(self, version):
        return 'make PYVER=%s' % version

    @staticmethod
    def copy_file(srcFolder, srcFile, dstFile):
        srcPath = os.path.join(TestHarness.FRONTEND_DIR, srcFolder, srcFile)
        assert os.path.isfile(srcPath), 'File %s not found' % srcPath
        dstPath = os.path.join(TestHarness.FRONTEND_DIR, dstFile)
        shutil.copyfile(srcPath, dstPath)

    @staticmethod
    def shell_run(cmd, mycwd):
        return subprocess.call(cmd, cwd=mycwd, shell=True)
    
    def make_executable(self, version, forceMake=False):
        ''' Makes the executable front-end if it's not already there '''
        if forceMake or not os.path.isfile(self.ver_front_end):
            print("Making front-end for version %s..." % version, flush=True)
            retcode = TestHarness.shell_run(self.make_command(version), TestHarness.FRONTEND_DIR)
            assert retcode == 0, '\tFAILED to make the parser'

    def init_counters(self):
        self.num_passed = 0
        self.num_failed = 0

    def set_verbose(self, see_errors=True):
        self.verbose = see_errors

    def print_context(self, filename, line_no):
        ''' Print a line from a file, and line(s) before and after it '''
        ctxt = 1  # No. of lines before and after
        for d in range(line_no-ctxt, line_no+ctxt+1):
            try :
                print('%d:%s' % (d, linecache.getline(filename, d)),
                      file=sys.stderr, flush=True, end='')
            except (SyntaxError) as err:
                msg = str(err).replace(filename, os.path.basename(filename))
                print('%d:%s' % (d, msg))

    def check_return_code(self, retcode, filename, filepath):
        ''' Increment pass/fail counter; print error details if desired '''
        if retcode > 0:
            if self.verbose:
                print('\n*', filepath, 'failed.', file=sys.stderr)
                try:
                    #with open(TestHarness.ERROR_LOG, 'r') as tmp_fh:
                    with codecs.open(TestHarness.ERROR_LOG, 'r',
                                     encoding='utf-8', errors='ignore') as tmp_fh:
                        error_msg = tmp_fh.read()
                        print(error_msg, file=sys.stderr, flush=True, end='')
                        match = re.match('^(\d+)', error_msg)
                        if match:
                            line_no = int(match.group(1))
                            self.print_context(filepath, line_no)
                except (UnicodeDecodeError) as err:
                    print('Exception %s' % err, file=sys.stderr)
            self.num_failed += 1
        else:
            # print(testcase, 'passed')
            self.num_passed += 1

    def test_one_file(self, root, filename):
        filepath = os.path.join(root, filename)
        # sed hack adds an extra '\n' at end of file:
        toExec = 'sed -e \'$a\\\' "%s" | %s > %s 2>&1' \
                 % (filepath, self.ver_front_end, TestHarness.ERROR_LOG)
        this_path = os.path.dirname(os.path.realpath(__file__))         
        retcode = TestHarness.shell_run(toExec, this_path)
        self.check_return_code(retcode, filename, filepath)

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
        return (self.num_passed + self.num_failed)

    def percent_passed(self):
        ''' Return the percentage pass rate (or 0 no files processed)'''
        if self.get_total() == 0:
            return 0
        return self.num_passed * 100.0 / self.get_total()

    def __str__(self):
        return '%d Passed, %d Failed (%5.2f%% passed)' \
                % (self.num_passed, self.num_failed, self.percentPassed())

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


def test_all(pyVersions, qualapps,
             testroot=qualitas.get_root_dir()):
    ''' For each given Python version, test each given directory.
        Optionally can specify the root (for non-Qualitas),
        and a different harness (instead of TestHarness).
    '''
    # We assemble the data column-by-column (one column per Python version)
    percs =  [[] for t in qualapps]  # one row per application
    for runver in pyVersions:
        # Print the syntax errors if we're testing 1 version with 1 app:
        want_verbose = len(pyVersions)==1 and len(qualapps)==1
        # New harness for each version:
        harness = TestHarness(runver, want_verbose)  
        safe_print("Running front-end for v%s on %d apps:"
              % (runver, len(qualapps)),
              sys.stderr, True, '')
        tot_failed = 0
        for i,testdir in enumerate(qualapps):
            safe_print(" %s," % testdir, sys.stderr, True, '')
            harness.test_directory(os.path.join(testroot,testdir), True)
            percs[i].append(harness.percent_passed())
            tot_failed += harness.num_failed
        safe_print(' done (%d cases failed).' % tot_failed, sys.stderr)
    return percs


def get_pyvers_appnames(given_args, test_dir=qualitas.get_root_dir()):
    ''' Use the (command-line) args to specify front-end(s) or app(s) '''
    full_suite = qualitas.get_dirnames(test_dir)
    qualapps = [ ]
    versions = [ ]
    for arg in given_args:
        if arg in SERIES2+SERIES3:
            versions.append(arg)
        elif arg in full_suite:
            qualapps.append(arg)
        else:
            safe_print('Unkown argument: "%s"' % arg, sys.stderr)
            sys.exit(1)
    if versions == []: # None specified, so use "all" the Python front-ends
        versions = FOR_ESEM 
    if qualapps == []: # None specified, so test "all" the applications
        qualapps = full_suite
    return (versions, qualapps)


# On the command line you can specify the Python versions to use,
# or list the Quaitas apps you want to process (or a mixture of both)
# Default is to use all (ESEM) versions to process all Qualitas apps.
if __name__ == '__main__':
    versions, qualapps = get_pyvers_appnames(sys.argv[1:])
    percs = test_all(versions, qualapps, TEST_ROOT)
    print_latex_table(versions, qualapps, TEST_ROOT, percs)
