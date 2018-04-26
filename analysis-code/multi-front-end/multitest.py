#!/usr/bin/python3
'''
    Test harness to build and run a front-end on a Python test-suite.
    Default is to measure all fornt-ends against all libraries.
    Prints a table of pass rates (no of files passed / total no of files)
'''

import os
import sys
import subprocess
import shutil

import re
import linecache
import codecs

# Where the (Python library) test cases live:
TESTROOT = os.path.join(os.path.dirname(__file__), '..' , 'testsuite-python-lib')

# The Python version numbers that we might want to test:
SERIES2 = ['2.0', '2.2', '2.4', '2.4.3', '2.5', '2.6', '2.7']
SERIES3 = ['3.0', '3.1', '3.2', '3.3.0', '3.5.0', '3.6.0']


class TestHarness:
    ''' Instantiate with a Python version, run over a dir of Python files.
        Records no. of pass/fail, prints nice output for syntax errors.
    '''

    def __init__(self, version, wantVerbose=False):
        self.init_counters()
        self.set_verbose(wantVerbose)
        self.ver_front_end = '%s-%s' % (TestHarness.FRONTEND_EXE, version)
        self.make_executable(version)

    # This is the directory where the Makefile lives:
    FRONTEND_DIR = os.path.dirname(__file__)

    # This is the exe that the Makefile builds (I'll rename this):
    FRONTEND_EXE = os.path.join(FRONTEND_DIR, 'run')
    # I need somewhere to record errors for each processed file:
    ERROR_LOG = os.path.join(os.getcwd(), 'error.log')

    @classmethod
    def copy_file(self, srcFolder, srcFile, dstFile):
        srcPath = os.path.join(TestHarness.FRONTEND_DIR, srcFolder, srcFile)
        assert os.path.isfile(srcPath), 'File %s not found' % srcPath
        dstPath = os.path.join(TestHarness.FRONTEND_DIR, dstFile)
        shutil.copyfile(srcPath, dstPath)

    @staticmethod
    def shell_run(cmd):
        return subprocess.call(cmd, cwd=TestHarness.FRONTEND_DIR, shell=True)

    def make_command(self, version):
        return 'make PYVER=%s' % version

    def make_executable(self, version, forceMake=False):
        ''' Makes the executable front-end if it's not already there '''
        if forceMake or not os.path.isfile(self.ver_front_end):
            print("Making front-end for version %s..." % version,
                  flush=True)
            retcode = TestHarness.shell_run(self.make_command(version))
            assert retcode == 0, '\tFAILED to make the parser'

    @classmethod
    def count_tests(self, version):
        ''' Count all the .py files in a directory and its sub-dirs '''
        testDir = os.path.join(TESTROOT, 'Python-%s' % version)
        assert os.path.isdir(testDir), testDir + 'must be a directory'
        count = 0
        for _, _, files in os.walk(testDir):
            pyFiles = [filename for filename in files
                       if filename.endswith('.py')]
            count += len(pyFiles)
        return count

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
        retcode = TestHarness.shell_run(toExec)
        self.check_return_code(retcode, filename, filepath)

    def test_directory(self, testpath, reinit_counters=False):
        ''' Tests all .py files in this directory and its subdirectories. '''
        assert os.path.isdir(testpath), testpath + 'must be a directory'
        if reinit_counters:
            self.init_counters()
        for root, dirs, files in os.walk(testpath):
            for filename in files:
                if filename.endswith('.py'):
                    self.test_one_file(root, filename)

    def test_on_library(self, libver, reinit_counters=False):
        ''' Test the front-end on the given Python library version '''
        test_path = os.path.join(TESTROOT, 'Python-%s' % libver)
        self.test_directory(test_path, reinit_counters)

    def get_num_failed(self):
        ''' Return the number of files that failed'''
        return self.num_failed

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
                % (self.num_passed, self.num_failed, self.percent_passed())


def print_latex_table(versions, rows, totals):
    ENDL = '\\\\'
    # Table header:
    print('$\\begin{array}{cl|*{%d}{c}}' % len(versions))
    print('&& \\multicolumn{%d}{c}{\\emph{Test suites from the Python library}}'
          % len(versions), ENDL)
    print('&    Ver & ',
               ' & '.join(map(lambda v:'%5s' % v, versions)), ENDL)
    print('\\hline\\hline')
    print('\\multirow{%d}{*}{\\rotatebox{90}{\\emph{Python front-end}}}'
          % len(versions))
    # The actual data:
    for ver, a_row in zip(versions, rows):
        print('& %7s & ' % ver, ' & '.join(a_row), ENDL)
    # Table totals and footer:
    print('\\hline')
    print('&Totals: & ', ' & '.join(totals), ENDL)
    print('\\end{array}$')

def test_all(versions):
    perc_rows, fail_rows = [], []
    for runver in versions:
        print("Running %s on %d test suites:" % (runver, len(versions)))
        harness = TestHarness(runver)
        this_perc, this_fail = [], []
        for testver in versions:
            print("\ton", testver)
            harness.init_counters()
            harness.test_on_library(testver)
            shading = ('\\cShade ' if runver == testver else '')
            this_perc.append('%s%4.1f ' % (shading, harness.percent_passed()))
            this_fail.append('%s%4d ' % (shading, harness.get_num_failed()))
        perc_rows.append(this_perc)
        fail_rows.append(this_fail)
    totals = ['%5d' % TestHarness.count_tests(v) for v in versions]
    print_latex_table(versions, perc_rows, totals)
    print_latex_table(versions, fail_rows, totals)

def test_ver_with(runver, testcases):
    ''' Test the version against the libraries of the versions in testcases 
        Report syntax errors as they occur.
    '''
    harness = TestHarness(runver, True)
    for testver in testcases:
        harness.init_counters()
        harness.test_on_library(testver)
        print('  Running %s parser over %s tests: %s'
              % (runver, testver, harness))
        

if __name__ == '__main__':
    if len(sys.argv) == 1:  # No args, test all
        test_all(SERIES2)
        test_all(SERIES3)
    elif len(sys.argv) == 2:  # One arg, test with its own suite
        test_ver_with(sys.argv[1], [sys.argv[1]])
    else:  # Just test given versions
        test_all(sys.argv[1:])
