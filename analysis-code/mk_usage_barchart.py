'''
    Graph the usage of backported Python 3 features (barchart)
    for the top 10 non-Python 3 applications.
    This is a once-off, so the data is hard-coded in the data file.
'''

import os

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from data_dir import DATA_DIR


# Where the output boxplots will go:
_BARCHART_PDF = 'usage-barchart.pdf'

# Read usage rates from this file (copied from latex table):
_DATA_FILE = os.path.join(DATA_DIR, 'features-top10.txt')

legend = ['Set Lit', 'Set Comp', 'Dict Comp', 'With As']




def read_usage(filename=_DATA_FILE):
    ''' Reads the usage rates from a file; returns a list of (app,nums)
    '''
    data = [ ]
    num_bars = len(legend)
    with open(filename, 'r') as fh:
        for line in fh:
            if line.startswith('#'):
                continue
            tokens = line.split(' & ')
            appname = tokens[0]
            data.append((appname, [int(x) for x in tokens[2:2+num_bars]]))
    # Sort based on total number of uses (descending):        
    return sorted(data, key = lambda av : sum(av[1]), reverse=True)



def plot_bar_chart(data, save_as=None):
    ''' Plot a stacked bar chart, one stacked bar per application, 
        divide each bar on no. of usage-types for that app
        This is how we get Fig 8 of the JESE paper.
    '''
    num_apps = len(data)
    fig, ax1 = plt.subplots(figsize=(9,7))
    bar_width = 0.45       # the width of the bars
    ver_colors = cm.rainbow(np.linspace(0, 1, len(legend)))[::-1]
    yr_xlocs = np.arange(num_apps)+0.25   # x locations for the bars
    yr_bottoms = np.zeros(num_apps)  # y locations for the bottom of the bars
    bars = [ ]  # Keep bar data to make legend handle
    for i,_ in enumerate(legend):
        # Plot the bars for this feature, one for each app
        ver_data = [nums[i] for (_,nums) in data] 
        abar = plt.bar(yr_xlocs, ver_data, bar_width, 
                       bottom=yr_bottoms, color=ver_colors[i])
        bars.append(abar)
        #bottom = [b+d for (b,d) in zip(bottom,data)]
        yr_bottoms = yr_bottoms + ver_data
    # Trimmings:
    #plt.title('Change in Python versions over time')
    plt.xlabel('Qualitas application')
    plt.xticks(yr_xlocs, [appname for (appname,_) in data])
    plt.ylabel('No. of 3.x features used')
    plt.yticks(np.arange(0, 1700, 100))      # no. of apps on y axis
    ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=.25)
    plt.legend([b[0] for b in bars], legend, loc=1)
    plt.savefig(save_as, bbox_inches='tight') if save_as else plt.show()



if __name__ == '__main__':
    data = read_usage()
    plot_bar_chart(data, _BARCHART_PDF)
