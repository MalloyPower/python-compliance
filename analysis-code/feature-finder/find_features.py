#!/usr/bin/python3

''' Run the front-end in this directory over the Qualitas suite.
    Assume the front-end is a feature-counter, so it returns totals
    per file; we accumulate these and print totals per application.
    This is an old clone of the qualitas_test.py file used in multitest.
'''


from __future__ import print_function

import os
import sys
import subprocess
import shutil

import re
import linecache

import qualitas

# Metrics are (from scan.l):
#   0: print_as_function ? 1 : 0
#   1: set_count - set_comprehension,
#   2: set_comprehension,
#   3: dict_comprehension,
#   4: extra_func_parens,    <--- I'm deleteing these.
#   5: with_as_count

EXTRA_FUNC_PARENS_POS = 4  # delete data for func parens

METRIC_KINDS = ['Print Fcn', 'Set Lit', 'Set Comp', 'Dict Comp', 'With As']


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
        self.uses_counts = [0] * len(METRIC_KINDS)
        self.file_counts = [0] * len(METRIC_KINDS)
        self.files_using = 0 # No of files >0 for any (non-print-func) metric

    def add_metrics(self, this_uses):
        ''' Add in the metric values from a single file'''
        assert len(this_uses)==len(METRIC_KINDS), \
            'inconsistent number of metrics %d' % len(this_uses)
        # Did this file use any of the 3x features?    
        if sum(this_uses[1:]) > 0:
            self.files_using += 1
        # Now add usage counts in to the running totals:
        self.uses_counts = [i+j for i,j in zip(self.uses_counts, this_uses)]
        # Change usage counts to file counts:
        this_file = [min(1,m) for m in this_uses]  # All 0 or 1
        self.file_counts = [i+j for i,j in zip(self.file_counts, this_file)]

    def get_file_metrics(self):
        return list(self.file_counts) 
        
    def get_use_metrics(self):
        return list(self.uses_counts) 
   
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
                del this_metrics[EXTRA_FUNC_PARENS_POS]
                self.add_metrics(this_metrics)
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

    def get_total_files(self):
        return (self.noPassed + self.noFailed)

    def get_total_uses(self):
        '''Sum of all uses except for print-as-func:'''
        return sum(self.uses_counts[1:])
        
    def total_files_using(self):
        return self.files_using
    
    def percent_files_using(self):
        return self.total_files_using() * 100.0 / self.get_total_files()

    def __str__(self):
        return '%d Passed, %d Failed (%5.2f%% passed)' \
                % (self.noPassed, self.noFailed, self.percentPassed())

    
def latex_table_row(data, effect=None, want_hline=False):
    row_str = ' & '.join(['%5s' % str(d) for d in data]) + ' \\\\'
    if want_hline:
        row_str += '\n\\hline'
    return row_str

def print_latex_table(testcases, metrics, kind, totals):
    # First column of table should be the application names:
    row_data =  [['%12s' % t] for t in testcases]
    print('%%%%% Counting {} %%%%%'.format(kind))
    # Data columns are the metrics for each version:
    for i, plist in enumerate(metrics):
        row_data[i].extend(plist)
    # Now print the table, row-by-row:
    print('\\begin{tabular}{l*{%d}{c}c}' % len(metrics[0]))
    print(latex_table_row(['Application'] + METRIC_KINDS + totals,'bf', True))
    # Print rows, sorted descending by total uses
    for row in sorted(row_data, key=lambda m: m[-2], reverse=True):
        print(latex_table_row(row))
    print('\\hline')
    print('\\end{tabular}')

def test_all(pyVersions, testroot, testcases):
    # We assemble the data column-by-column (one column per Python version)
    use_metrics =  [[] for t in testcases]  # one row per testcase
    file_metrics =  [[] for t in testcases]  # one row per testcase
    for runver in pyVersions:
        harness = TestHarness(runver, False)
        print('Running front-end for v%s on %d apps:'
              % (runver, len(testcases)),
              file=sys.stderr, flush=True, end='')
        for i,testdir in enumerate(testcases):
            print(" %s," % testdir, file=sys.stderr, flush=True, end='')
            harness.test_directory(os.path.join(testroot,testdir), True)
            # Add in uses data for this app:
            use_metrics[i].extend(harness.get_use_metrics())
            use_metrics[i].append(harness.get_total_uses())
            # Add in files data for this app:
            file_metrics[i].extend(harness.get_file_metrics())
            file_metrics[i].append(harness.total_files_using())
            file_metrics[i].append(round(harness.percent_files_using()))
        print(' done.', file=sys.stderr)
    return (use_metrics, file_metrics)

        
''' Use the command-line args to specify application(s) '''
if __name__ == '__main__':
    full_suite = qualitas.get_dirnames()
    testcases = [arg for arg in sys.argv[1:] if arg in full_suite]
    if testcases == []: # None specified, so test *all* the applications
        testcases = full_suite
    QROOT = qualitas.corpus_for_year('2017')
    PYVER = ['2.7']
    (use_metrics, file_metrics) = test_all(PYVER, QROOT, testcases)
    print_latex_table(testcases, use_metrics, 'uses', ['Total Uses'])
    print_latex_table(testcases, file_metrics, 'files', ['Total Files', 'Perc Files'])
