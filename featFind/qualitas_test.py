#!/usr/bin/python

''' Run the front-end in this directory over the Qualitas suite.
    Assume the front-end is a feature-counter, so it returns totals
    per file; we accumulate these and print totals per application.
    This is a clone of the file used in multitest.
'''
from __future__ import print_function

import os
import sys
import subprocess
import shutil

import re
import linecache

import qualitas

# This is where the Makefile lives:
FRONTEND_DIR = os.path.join(os.getcwd())

# This is the front-end that the Makefile builds:
FRONTEND_EXE = os.path.join(FRONTEND_DIR, 'run')

# I need to record errors and metrics for each processed file:
ERROR_LOG = os.path.join(os.getcwd(), 'error.log')
METRICS_LOG = os.path.join(os.getcwd(), 'metrics.log')

# sed trick to add a newline to the end of a file:
ADD_NEWLINE = 'sed -e \'$a\\\' '


class TestHarness:

    def __init__(self, version, verbose=False):
        self.verbose = verbose
        self.init_counters()
        self.make_executable(version)

    @staticmethod
    def delete_logs():
        if os.path.isfile(ERROR_LOG): os.remove(ERROR_LOG)
        if os.path.isfile(METRICS_LOG): os.remove(METRICS_LOG)

    @staticmethod
    def shell_run(cmd):
        return subprocess.call(cmd, cwd=FRONTEND_DIR, shell=True)
    
    def make_executable(self, ver, forceMake=False):
        self.ver_front_end = '%s-%s' % (FRONTEND_EXE, ver)
        if forceMake or not os.path.isfile(self.ver_front_end):
            print('--- Building front-end for v%s' % ver, file=sys.stderr)
            retcode = TestHarness.shell_run('make')
            assert retcode == 0, '\t*** FAILED to make the parser'
            os.rename(FRONTEND_EXE, self.ver_front_end)

    def init_counters(self):
        self.noPassed = 0
        self.noFailed = 0
        self.metrics = None  # Will be a list of metric values
        self.files_using = 0 # No of files >0 for any metric

    def add_metrics(self, this_metrics, booleanise=False):
        assert not self.metrics or len(this_metrics)==len(self.metrics), \
            'inconsistent number of metrics %d' % len(this_metrics)
        if booleanise:
            this_metrics = [min(1,m) for m in this_metrics]
        if not self.metrics:
            self.metrics = list(this_metrics)
        else:
            self.metrics = [i+j for i,j in zip(self.metrics, this_metrics)]
        if sum(this_metrics) > 0:
            self.files_using += 1

    def get_metrics(self):
        return list(self.metrics) 

    def num_metrics(self):
        return len(self.metrics)
    
    def set_verbose(self):
        self.verbose = True

    @staticmethod
    def count_tests(testpath):
        '''Work out the total number of '.py' files'''
        assert os.path.isdir(testpath), testpath + 'must be a directory'
        count = 0
        for _, _, files in os.walk(testpath):
            pyFiles = [filename for filename in files
                       if filename.endswith('.py')]
            count += len(pyFiles)
        return count

    def print_context(self, filename, line_no):
        '''For syntax error, print some lines around the error line '''
        for d in [line_no-1, line_no, line_no+1]:  # one each side
            print('%d:%s' % (d, linecache.getline(filename, d)),
                       file=sys.stderr, flush=True, end='')
        print('')

    def check_return_code(self, retcode, testcase):
        if retcode > 0:  # Syntax error
            if self.verbose:
                print('\n* ' + testcase+ ' failed.', file=sys.stderr)
                with open(ERROR_LOG, 'r') as tmp_fh:
                    error_msg = tmp_fh.read()
                    match = re.match('^(\d+)', error_msg)
                    if match:
                        line_no = int(match.group(1))
                        print(error_msg, file=sys.stderr, flush=True, end='')
                        self.print_context(testcase, line_no)
            self.noFailed += 1
        else: # No error, so collect metrics:
            with open(METRICS_LOG, 'r') as tmp_fh:
                this_metrics = tmp_fh.read().split(':')
                this_metrics = [int(m) for m in this_metrics]
                self.add_metrics(this_metrics, True)
            self.noPassed += 1
        self.delete_logs()

    def test_one_file(self, root, filename):
        testcase = os.path.join(root, filename)
        toExec = ADD_NEWLINE + ' "%s" | %s >%s 2>%s' \
                 % (testcase, self.ver_front_end, METRICS_LOG, ERROR_LOG)
        retcode = TestHarness.shell_run(toExec)
        self.check_return_code(retcode, testcase)

    def test_directory(self, testpath, reinit=False):
        assert os.path.isdir(testpath), testpath + 'should be a directory'
        if reinit:
            self.init_counters()
        for root, dirs, files in os.walk(testpath):
            for filename in files:
                if filename.endswith('.py'):
                    self.test_one_file(root, filename)

    def get_total(self):
        return (self.noPassed + self.noFailed)

    def percent_passed(self):
        return self.noPassed * 100.0 / self.get_total()

    def percent_used(self):
        return self.files_using * 100.0 / self.get_total()

    def __str__(self):
        return '%d Passed, %d Failed (%5.2f%% passed)' \
                % (self.noPassed, self.noFailed, self.percentPassed())

    
def latex_table_row(data, effect=None, want_hline=False):
    row_str = ' & '.join([str(d) for d in data]) + '\\\\'
    if want_hline:
        row_str += '\n\\hline'
    return row_str

def print_latex_table(pyVersions, testroot, testcases, percs, labels=None):
    # First column of table should be the application names:
    if not labels: # Can optionally specify labels for rows
        labels = testcases
    row_data =  [[t] for t in labels]
    # Data columns are the percentages for each version:
    for i, plist in enumerate(percs):
        row_data[i].extend(plist)
    # Last column should be totals for each application:
    for i,testdir in enumerate(testcases):
        testpath = os.path.join(testroot,testdir)
        row_data[i].append('%5d' % TestHarness.count_tests(testpath))
    # Now print the table, row-by-row:
    print('\\begin{tabular}{l*{%d}{c}c}' % len(percs[0]))
    print(latex_table_row(['Application'] + 
                          [p for p in pyVersions] + ['Files'], 'bf', True))
    for row in row_data:
        print(latex_table_row(row))
    print('\\hline')
    print('\\end{tabular}')

def test_all(pyVersions, testroot, testcases):
    # We assemble the data column-by-column (one column per Python version)
    percs =  [[] for t in testcases]  # one row per testcase
    for runver in pyVersions:
        harness = TestHarness(runver, False)
        print("Running front-end for v%s on %d apps:"
              % (runver, len(testcases)),
              file=sys.stderr, flush=True, end='')
        for i,testdir in enumerate(testcases):
            print(" %s," % testdir, file=sys.stderr, flush=True, end='')
            harness.test_directory(os.path.join(testroot,testdir), True)
            percs[i].append(round(harness.percent_passed()))
            percs[i].extend(harness.get_metrics())
            percs[i].append(round(harness.percent_used()))
        print(' done.', file=sys.stderr)
    return percs

        
if __name__ == '__main__':
    ''' Use the command-line args to specify application(s) '''
    full_suite = qualitas.get_dirnames()
    testcases = [ ]
    for arg in sys.argv[1:]:
        if arg in full_suite:
            testcases.append(arg)
        else:
            print('Ignoring argument "%s"' % arg, file=sys.stderr)
    if testcases == []: # None specified, so test *all* the applications
        testcases = full_suite
    percs = test_all(['2.7'], qualitas.get_root_dir(), testcases)
    print_latex_table(['2.7'], qualitas.get_root_dir(), testcases, percs)
