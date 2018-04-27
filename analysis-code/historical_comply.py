'''
    Get the level of compliance for 'old' versions of the apps.
    That is, run the test harness over the suite from 31 Dec in some year.
    Pass-rates are written to files for later use, one file per year/version.
'''

import os
from collections import Counter

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from qualitas import get_dirnames, corpus_for_year
from qualitas_test import test_all, print_latex_table

# Where the output boxplots will go:
_BARCHART_PDF = 'versions-barchart-s{}.pdf'

# Read/write pass rates to this directory to speed things up:
_DATA_DIR = os.path.join(DATA_DIR, 'pass_rates')

_THRESHOLD=98  # Percentage pass rate that counts as compliant  (>=)
_YEAR_LIST = list(range(2005, 2018))



def prettify(versions):
    ''' Delete the revision version number if it is 0; so 3.5.0 -> 3.5 '''
    def pretty(v): 
        vers = v.split('.', maxsplit=2)
        if len(vers)>2 and vers[2]=='0': return '.'.join(vers[:2]) # Trim
        return v
    return [pretty(v) for v in versions]

def find_oldest_ver(versions, percs, threshold=_THRESHOLD):
    ''' Return the oldest version with a pass rate over the threshold; 
        return None if no such version found.
    '''
    assert len(versions)==len(percs), 'Missing data in {}'.format(versions)
    for v, p in zip(versions, percs):
        if p >= threshold:
            return v
    return None


def read_year_percs(filename, year_apps):
    ''' Reads the pass rates from a file; returns a list of percentages.
        In case app names in file don't match given ones, returns None.
    '''
    percs = [ ]
    with open(filename, 'r') as fh:
        for i,line in enumerate(fh):
            app, perc = line.split()
            if app != year_apps[i]:
                return None
            percs.append(float(perc))
    assert len(year_apps)==len(percs), 'Not enough data in {}'.format(percs)
    return percs

def write_year_percs(filename, year_apps, percs):
    ''' Write a list of (app-name, pass-rate) to a txt file '''
    assert len(year_apps)==len(percs), 'Not enough data in {}'.format(percs)
    with open(filename, 'w') as fh:
        for app, perc in zip(year_apps, percs):
            print(app, perc, file=fh)
    

def test_or_read(versions, year, year_apps, year_root):
    ''' Get the percentage pass rates for one particular year of the apps.
        return an array, one row for each app, one column for each version.
        Will re-generate the pass-rate data if it is not found in a file.
    '''
    qname = os.path.basename(corpus_for_year(year)) # Name prefix for data files
    all_percs = [[] for _ in year_apps]  # One row for each app
    for ver in versions:
        filename = os.path.join(_DATA_DIR, '{}-{}.dat'.format(qname,ver))
        percs = None
        if os.path.isfile(filename):
            percs = read_year_percs(filename, year_apps)
        if not percs:  # Not in a file (for these apps): re-generate
            print('--- Year = {}'.format(year), flush=True)
            percs = test_all([ver], year_apps, year_root)
            percs = [p[0] for p in percs]  # Were lists of length 1
            write_year_percs(filename, year_apps, percs)
        assert len(percs)==len(year_apps), 'Want one entry per app {}'.format(percs)
        # Now, append a perc to each row, so one column for each version:
        for i,p in enumerate(percs):
            all_percs[i].append(p)
    return all_percs   # Dimension: apps by versions

def test_all_years(versions, qualapps, year_list):
    ''' For all the given years, get the lowest version with enough passes.
        For each year return a list of (app, oldest-version) pairs.
    '''
    oldest = { }  # Maps year to list of (app, oldest-version) pairs
    for year in year_list:
        oldest[year] = [ ]
        year_root = corpus_for_year(year)
        year_apps = [app for app in get_dirnames(year_root) if app in qualapps]
        percs = test_or_read(versions, year, year_apps, year_root)
        for i,app in enumerate(year_apps):
            best_ver = find_oldest_ver(versions, percs[i])
            if best_ver:
                oldest[year].append((app,best_ver))
    return oldest
            
def sum_year_counts(versions, oldest):
    ''' For each year, calc the number of apps for each Python version.
        Return a list of (year, version-counts), ordered by year.
        This is the raw data for Fig 4 of the ESEM paper.
    '''
    year_counts = [ ]
    for year in sorted(oldest.keys()):
        counts = Counter([p for (_,p) in oldest[year]])
        vcount = [counts.get(v,0) for v in versions]
        year_counts.append((year, vcount))
    return year_counts
    
def show_year_counts(versions, year_counts):
    ''' For each year, list the number of apps for each Python version'''
    plist = lambda ls : ', '.join(['{:>3s}'.format(str(l)) for l in ls])
    print('# Year {}'.format(plist(prettify(versions))))
    for year, vcount in year_counts:
        print(' {} {}'.format(year, plist(vcount)))

def tabulate_by_app(qualapps, oldest):
    ''' Table: rows are apps, columns are years, cell is best Python version '''
    # First get the data into a 2D array
    by_app = {app:{} for app in qualapps}
    all_years = sorted(oldest.keys()) 
    for year in all_years:
        aplist = oldest[year]
        for vlist in by_app.values():
            vlist[year] = '-'
        for app, ver in aplist:
            by_app[app][year] = ver
    # Then print it:
    print_row = lambda row: print(' & '.join([str(r) for r in row]))
    print_row(['Application'] + all_years)
    for app in qualapps:
        row = [app] + prettify([by_app[app][year] for year in all_years])
        print_row(row)


def tabulate_pass_rates(versions, qualapps, year):
    ''' Table: rows are apps, columns are versions, cell is pass rate.
        Year is given, so the pass rates shown are for just one year.
    '''
    year_root = corpus_for_year(year)
    year_apps = [app for app in get_dirnames(year_root) if app in qualapps]
    percs = test_or_read(versions, year, year_apps, year_root)    
    print_latex_table(prettify(versions), year_apps, year_root, percs)

def plot_pass_rates(versions, qualapps, year, save_as=None):
    ''' Graph of pass rates; x-axis is version, y-axis is % rate.
        Each line on graph represents a single app.
    '''
    # First, get the data:
    year_root = corpus_for_year(year)
    year_apps = [app for app in get_dirnames(year_root) if app in qualapps]
    percs = test_or_read(versions, year, year_apps, year_root)    
    # Now plot:
    fig, ax = plt.subplots(figsize=(9,7))
    ver_xlocs = np.arange(len(versions))
    for appdata in percs:
        ax.plot(ver_xlocs, appdata)
    plt.xlabel('Python Versions')
    plt.xticks(ver_xlocs, prettify(versions))  
    plt.ylabel('Percentage of files passing')
    plt.yticks(np.arange(0, 105, 5))     
    ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=.25)
    plt.savefig(save_as, bbox_inches='tight') if save_as else plt.show()



def plot_bar_chart(versions, year_counts, save_as=None):
    ''' Plot a stacked bar chart, one stacked bar per year, 
        divide each bar on no. of apps per version for that year.
        This is how we get Figs 6&7 of the J.ESE paper.
    '''
    fig, ax1 = plt.subplots(figsize=(9,7))
    # REviewer wants no ticks along bottom axis:
    plt.tick_params(axis='x', which='both', bottom='off', top='off')
    bar_width = 0.45       # the width of the bars
    ver_colors = cm.rainbow(np.linspace(0, 1, len(versions)))[::-1]
    num_years = len(year_counts)
    yr_xlocs = np.arange(num_years)  # x locations for the bars
    yr_bottoms = np.zeros(num_years)  # y locations for the bottom of the bars
    bars = [ ]  # Keep bar data to make legend handle
    for i,_ in enumerate(versions):
        # Plot the bars for this versions, one for each year
        ver_data = [c[i] for _,c in year_counts] # counts (no of apps) per year
        abar = plt.bar(yr_xlocs, ver_data, bar_width, 
                       bottom=yr_bottoms, color=ver_colors[i])
        bars.append(abar)
        #bottom = [b+d for (b,d) in zip(bottom,data)]
        yr_bottoms = yr_bottoms + ver_data
    # Trimmings:
    #plt.title('Change in Python versions over time')
    plt.xticks(yr_xlocs, [y for y,_ in year_counts])  # years on x axis
    plt.ylabel('No. of applications passing')
    plt.yticks(np.arange(0, 51, 5))      # no. of apps on y axis
    ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=.25)
    plt.legend([b[0] for b in bars], prettify(versions), loc=2)
    plt.savefig(save_as, bbox_inches='tight') if save_as else plt.show()


# Probably want to do one or the other of these:
_versions_for = {
    2 : ['2.0', '2.2', '2.4', '2.5', '2.6', '2.7'],
    3 : ['3.0', '3.1', '3.3.0', '3.5.0', '3.6.0'],
}

_SERIES = 3  ### EDIT ME TO SUIT

if __name__ == '__main__':
    qualapps = get_dirnames()  # All applications
    versions = _versions_for[_SERIES]
    oldest = test_all_years(versions, qualapps, _YEAR_LIST)
    year_counts = sum_year_counts(versions, oldest)
    show_year_counts(versions, year_counts)
    tabulate_by_app(qualapps, oldest)
    plot_bar_chart(versions, year_counts, _BARCHART_PDF.format(_SERIES))
    #plot_pass_rates(versions, qualapps, '2016', 
    #                'versions-2016-s{}.pdf'.format(series))
