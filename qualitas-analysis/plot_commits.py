# Produce a boxplot of the %age of commits during a particular Python.
# Note this doesn't run any front-ends here, it just looks at the repos
# and counts the commits corresponding to Python release dates.


# Violin plot code from here:
#https://matplotlib.org/examples/statistics/customized_violin_demo.html


import os

import matplotlib.pyplot as plt
import numpy as np

import qualitas
import python_versions

# Where the output boxplots will go:
BOXPLOT_PDF = 'commit-boxplots.pdf'
VIOLINPLOT_PDF = 'commit-violinplots.pdf'

DATA_FILE = os.path.join('data','commit-data.csv')

######################################################################
def print_quartile_numbers(pyvers, bp_dict):
    '''Print the median, first and third quartile from a given boxplot'''
    nums = [[v] for v in pyvers]
    for i,line in enumerate(bp_dict['medians']):
        _, y = line.get_xydata()[1]
        nums[i].append('%d' % y)
    for i,line in enumerate(bp_dict['boxes']):
        _, bot = line.get_xydata()[0]  # Bottom line
        _, top = line.get_xydata()[2]  # Top line line
        nums[i].append('%d' % bot)
        nums[i].append('%d' % top)
    for n in nums:
        print(' '.join(n))

def show_box_plot(pyvers, percs, save_as=None):
    ''' Given the (lists of) percentages for each pyver, produce the boxplot '''
    mpl_fig = plt.figure()
    ax = mpl_fig.add_subplot(111)
    bp_dict = ax.boxplot(percs)
    print_quartile_numbers(pyvers, bp_dict)
    ax.set_xlabel('On or after this Python release')
    ax.set_ylabel('Percentage of commits')
    start, end = ax.get_xlim()
    ax.set_xticklabels(pyvers)
    if save_as:
        plt.savefig(save_as, bbox_inches='tight')
    else:
        plt.show()

######################################################################

def adjacent_values(vals, q1, q3):
    upper_adjacent_value = q3 + (q3 - q1) * 1.5
    upper_adjacent_value = np.clip(upper_adjacent_value, q3, vals[-1])

    lower_adjacent_value = q1 - (q3 - q1) * 1.5
    lower_adjacent_value = np.clip(lower_adjacent_value, vals[0], q1)
    return lower_adjacent_value, upper_adjacent_value


def set_axis_style(ax, labels):
    ax.get_xaxis().set_tick_params(direction='out')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticks(np.arange(1, len(labels) + 1))
    ax.set_xticklabels(labels)
    ax.set_xlim(0.25, len(labels) + 0.75)
    ax.set_xlabel('Sample name')

def show_violin_plot(pyvers, percs, save_as=None):
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12, 6), sharey=True)

    parts = ax.violinplot(
            percs, showmeans=False, showmedians=False,
            showextrema=False)

    for pc in parts['bodies']:
        pc.set_facecolor('#4f90d9')
        pc.set_edgecolor('black')
        pc.set_alpha(1)

    quartile1, medians, quartile3 = np.percentile(percs, [25, 50, 75], axis=1)
    # Print quartile data to screen, just for confirmation
    for v,q1,q2,q3 in zip(pyvers, quartile1, medians, quartile3):
        print('\t{} Q1={:3.0f}, Q2={:3.0f}, Q3={:3.0f}'.format(v, q1, q2, q3))
    whiskers = np.array([
        adjacent_values(sorted_array, q1, q3)
        for sorted_array, q1, q3 in zip(percs, quartile1, quartile3)])
    whiskersMin, whiskersMax = whiskers[:, 0], whiskers[:, 1]

    inds = np.arange(1, len(medians) + 1)
    ax.scatter(inds, medians, marker='o', color='white', s=30, zorder=3)
    ax.vlines(inds, quartile1, quartile3, color='k', linestyle='-', lw=5)
    ax.vlines(inds, whiskersMin, whiskersMax, color='k', linestyle='-', lw=1)

    # set style for the axes
    set_axis_style(ax, pyvers)
    ax.set_xlabel('On or after this Python release')
    ax.set_ylabel('Percentage of commits')
    ax.set_ylim(0,110)
    ax.set_xticklabels(pyvers)
    ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=.25)

    plt.subplots_adjust(bottom=0.15, wspace=0.05)
    if save_as:
        plt.savefig(save_as, bbox_inches='tight')
    else:
        plt.show()

######################################################################
 
def read_date_counts(pyvers, qualapps, data_file):
    ''' Read the commit counts from the given file, one line per app.
        Return a list of percentages, one list for each Python version. 
        i.e. percentages are transposed (and reversed) from order in file.
    '''
    percs = [[] for v in pyvers]
    with open(data_file, 'r') as in_fd:
        for line in in_fd:
            if line.startswith('#'):
                continue
            data = line.split()
            # first entry is app name, last is total, rest are counts-per-version
            assert(data[0] in qualapps), 'Unknown app %s' % data[0]
            total_commits = int(data[-1])
            counts = data[-2:0:-1]  # Reverse, delete first & last
            assert len(counts)==len(pyvers), 'Wrong line length %d'% len(data)
            for i,vercount in enumerate(counts):
                percs[i].append(100*int(vercount)/total_commits)
    return percs


def print_date_percs(pyvers, qualapps, percs):
    ''' Categorise the commits in the repos; calculate percentages,
        and write this data to a file, one line per application.
    '''
    print('{:12s} & {}\\\\'.format('Application', ' & '.join(pyvers)))
    for i, app in enumerate(qualapps):
        thisper = [p[i] for p in percs]
        tidyper = ['{:3.0f}'.format(p) for p in thisper]
        print('{:12s} & {}\\\\'.format(app, ' & '.join(tidyper)))


def plot_date_counts(pyvers, qualapps):
    '''Main driver: generate the data and plot it.  I use an intermediate
       data file so I don't have to keep re-producing the data as I fiddle
       with the boxplot.
    '''
    percs = read_date_counts(pyvers, qualapps, DATA_FILE)
    print_date_percs(pyvers, qualapps, percs)
    #show_box_plot(pyvers, percs, BOXPLOT_PDF)
    show_violin_plot(pyvers, percs, VIOLINPLOT_PDF)
    
if __name__ == '__main__':
    full_suite = qualitas.get_dirnames()
    pyvers = python_versions.get_releases('3')  # Only look at 3.x releases
    #pyvers = pyvers[:-1]  # Delete the last one (Python 3.6)
    plot_date_counts(pyvers, full_suite)
