#!/usr/bin/python3

'''
    Test harness: this is just a wrapper for qualiatas_test, 
    adapted for the "other" (or non-Qualitas) suites.
'''


import sys
import os

import qualitas_test as qt

# This is where I put the other suites:
OTHER_ROOT = '/media/passport/bigApps/corpus-python/jese-2018-versions/'

# The names of the non-qualitas suites:
OTHER_PROGS = ['linchen', 'destefanis', 'anaconda3', 
               'getpython3', 'newer-qualitas']


def root_for(suite):
    '''Return the root directory for a given suite'''
    if suite == 'anaconda3': # Go down a layer to get SciPy sub-packages
        return os.path.join(OTHER_ROOT, suite, 'pkgs')
    if suite in OTHER_PROGS:
        return os.path.join(OTHER_ROOT, suite)
    print_usage('suite "{}"'.format(suite))


# Like qt.print_latex_table, but sort in descending order of size
# and ignore sub-packages with no files.
# Latex 'longtable' package splits tables over multiple pages.
def print_long_latex_table(pyVersions, appnames, testroot, percs):
    # First column of table should be the application names:
    row_data =  [[t.replace('_', '\_')] for t in appnames]
    # Data columns are the percentages for each version:
    for i, plist in enumerate(percs):
        row_data[i].extend([qt.print_perc(p) for p in plist])
    # Last column should be totals for each application:
    for i,testdir in enumerate(appnames):
        testpath = os.path.join(testroot,testdir)
        row_data[i].append('%5d' % qt.qualitas.count_python_files(testpath))
    # Now print the table, row-by-row:
    print('\n\n\n')
    print('\\begin{longtable}{l*{%d}{c}c}' % len(pyVersions))
    print(qt.latex_table_row(['Application'] + 
                          [p for p in pyVersions] + ['Files'], 'bf', True))
    for row in sorted(row_data, key=lambda r:int(r[-1]), reverse=True):
        if int(row[-1]) > 0:
            qt.safe_print(qt.latex_table_row(row))
    print('\\hline')
    print('\\end{longtable}')


def print_usage(msg):
    print('Unknown argument:', msg)
    print('Usage:', sys.argv[0], '<suite> <pyver> <pyver> ...')
    sys.exit(1)

# On the command line you can specify 
#   (1) the suite
#   (2) the apps from the suite (optional)
#   (3) the Python versions (optional)
if __name__ == '__main__':
    suite = sys.argv[1]
    suite_root = root_for(suite)
    versions, appnames = qt.get_pyvers_appnames(sys.argv[2:], suite_root)
    percs = qt.test_all(versions, appnames, suite_root)
    if suite == 'anaconda3':
        print_long_latex_table(versions, appnames, suite_root, percs)
    else:
        qt.print_latex_table(versions, appnames, suite_root, percs)
