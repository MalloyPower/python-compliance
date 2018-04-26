'''
    Very simple code to calculate the inter-quartile ranges for some data.
    I hard-coded the data here as I only use it once.
'''
import numpy as np


counts = {
     # From table 1 (total files per application):
     'Total files in suite' : [
          711, 584, 774, 1375, 110, 176, 2457, 845, 558, 264, 203, 1150, 
          139, 819, 343, 436, 425, 343, 726, 855, 428, 520, 1434, 151, 
          401, 153, 270, 407, 733, 267, 2563, 462, 214, 188, 645, 128, 
          2224, 463, 693, 1220, 138, 122, 327, 122, 1116, 167, 999, 
          206, 400, 1514, 321],

    # From table 1 (total  KLOC per application):
    'Total KLOC in suite' : [
          197, 218, 147, 387, 24, 28, 272, 106, 181, 55, 20, 285, 23, 
          192, 55, 79, 39, 34, 201, 174, 124, 97, 217, 27, 170, 14, 
          37, 96, 112, 40, 228, 55, 20, 34, 92, 56, 1257, 66, 174, 
          430, 18, 38, 96, 24, 301, 49, 429, 40, 118, 695, 40],
          
    # From table 3 (total # of uses of 3x features):
    'Uses of 3x features' : [
        1535,  814,  711,  620,  565,  402,  165,  141,  129,  125,  119,   
        91,   75,   68,   64,   57,   37,   26,   18,   17,   17,   16,   
        15,   15,   14,   12,    7,    6,    4,    3,    3,    3,    3,    
        3,    2,    2,    1,    1,    1,    0,    0,    0,    0,    0,    
        0,    0,    0,    0,    0,    0,    0],
}
    

def print_quartiles(header, data):
    print(header+':')
    quartiles = np.percentile(data, np.arange(0, 100, 25))
    print('\tmin is {}, max is {}'.format(min(data), max(data)))
    print('\tQ1 = {}, Q2 = {} (median), Q3 = {}'.format(
        quartiles[1], quartiles[2], quartiles[3]))
    iqr = quartiles[3]-quartiles[1]
    print('\tIQR=', iqr)
    #Tukey's test for outliers:
    out_top = quartiles[2] + 1.5 * iqr
    out_bot = quartiles[2] - 1.5 * iqr
    print('\tTukey: outliers are under', out_bot, 'or over', out_top)


for label, numbers in counts.items():
    print_quartiles(label, numbers)

