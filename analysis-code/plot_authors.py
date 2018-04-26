# Produce a boxplot of the number of committers and authors.
# Simple script, as the data is already in a text file.

import os

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

from data_dir import DATA_DIR


# Where the output boxplots will go:
AUTHORS_PDF = 'authors-box.pdf'
CREATORS_PDF = 'creators-box.pdf'

DATA_FILE = os.path.join(DATA_DIR,'authors.txt')
SEP = '&'


######################################################################
 
def read_authors(data_file):
    ''' Gather a list, each entry is (app, then no. of authors data) '''
    authors = []
    with open(data_file, 'r') as in_fd:
        for line in in_fd:
            if line.startswith('#'):
                continue
            line = line.strip()[:-len('\\\\')]  # remove \\ at end
            data = [col.strip() for col in line.split(SEP)]
            authors.append((data[0], [int(n) for n in data[1:]]))
    return authors


def plot_authors(data, xlabel, xticks, violin=False, save_as=None):
    ''' Violin plot or boxplot'''
    fig, ax = plt.subplots(figsize=(8,2))
    if violin:
        ax.violinplot(data, vert=False, widths=0.7, showmeans=True,
                      showextrema=True, showmedians=True)
    else:
        bplot = ax.boxplot(data, widths=0.5, sym='rx', vert=False, patch_artist=True)
        for path in bplot['boxes']:
            path.set_facecolor('lightblue')
    plt.rc('xtick', labelsize=8) 
    ax.set_xticks(xticks)
    ax.xaxis.grid(True, linestyle='-', which='major', color='lightgrey',
               alpha=0.5)
    ax.set_xlabel(xlabel)
    ax.set_yticks([])  # Nothing on vertical axis
    if save_as:
        plt.savefig(save_as, bbox_inches='tight')
        # Display some data on the quartiles:
        print('min={}, 10%={} Q1={}, median={}, Q3={}, max={}'\
            .format(*np.percentile(data, [0, 10, 25, 50, 75, 100])))
    else:
        plt.show()
              
def plot_authors_hist(data, xlabel, xticks, save_as=None):
    '''Histogram'''
    fig, ax = plt.subplots(figsize=(8,4))
    plt.hist(data, bins=xticks, facecolor='green', alpha=0.75)
    plt.plot(data, np.zeros(data.shape), 'b+', ms=20)
    ax.set_xlabel(xlabel)
    ax.set_xticks(xticks)
    ax.set_ylabel('No. of applications')
    ax.set_yticks(np.arange(0, 25, 2))
    if save_as:
        plt.savefig(save_as, bbox_inches='tight')
    else:
        plt.show()

if __name__ == '__main__':
    author_data = read_authors(DATA_FILE)
    all_authors = np.array([d[1][0] for d in author_data])
    all_creators = np.array([d[1][1] for d in author_data])
    #plot_authors_hist(all_authors, 'No. of committers', np.arange(0, 1700, 100), 'authors-hist.pdf')
    plot_authors(all_authors, 'No. of committers', 
                 np.arange(0, 2000, 100), False, AUTHORS_PDF)
    plot_authors(all_creators, 'No. of creators', 
                 np.arange(0, 360, 20), False, CREATORS_PDF)
