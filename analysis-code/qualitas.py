'''
   The platform-specific setup for the Qualtias corpus files.

   You should edit _CORPUS_ROOT below for your directory setup.
   This folder should have subdirectories called:
     qualitas: the most recent version of each application
     older-qualitas: the corpus as at 31 Dec each year.
       This in turn has subdirectories of the form qualitas-YYYY-12-31.

   For example, the most recent version of astropy is at
     os.path.join(_CORPUS_ROOT, 'qualitas', 'astropy')

   and the 2012 version of astropy is at
     os.path.join(_CORPUS_ROOT, 'older-qualitas', 
                  'qualitas-2012-31-12', 'astropy')

'''

import sys
import os.path
import getpass

# Where the corpus versions live (default location on James' setup)
_CORPUS_ROOT = '/media/passport/bigApps/corpus-python'
# Configure the next line for Brian:
if getpass.getuser() == 'malloy':
    _CORPUS_ROOT = '/home/malloy/Downloads'

# This is the 'current' version of the Qualitas corpus:
QUALITAS_ROOT = os.path.join(_CORPUS_ROOT, 'qualitas')

# This is where the year-by-year versions are stored:
_OLDER_DIR = os.path.join(_CORPUS_ROOT, 'older-qualitas')

def get_root_dir():
    return QUALITAS_ROOT

def get_older_dir():
    return _OLDER_DIR

def print_older_dir():
    print(_OLDER_DIR)

def file_for(app):
    return os.path.join(QUALITAS_ROOT, app)

def get_dirnames(root=QUALITAS_ROOT):
    ''' Return a list of all subdirectories of a directory '''
    dirs = [d for d in os.listdir(root)
            if os.path.isdir(os.path.join(root,d))]
    return sorted(dirs, key=lambda s: s.lower()) # Case insensitive sort

def count_python_files(root=QUALITAS_ROOT):
    ''' Return the number of Python files in this directory tree '''
    assert os.path.isdir(root), root + 'must be a directory'
    count = 0
    for _, _, files in os.walk(root):
        pyFiles = [filename for filename in files
                   if filename.endswith('.py')]
        count += len(pyFiles)
    return count

def basename(path):
    ''' Only chop off the Qualitas dir, leave subdirs from application'''
    return path[len(QUALITAS_ROOT):]

def corpus_for_year(year, mm=12, dd=31):
    '''Return the name of the root dir for the corpus of the given year'''
    return os.path.join(_OLDER_DIR, 'qualitas-{}-{}-{}'.format(year,mm,dd))

def get_years():
    '''Return a list of the years we have 'older' version for'''
    dirs = [d for d in os.listdir(_OLDER_DIR)
            if os.path.isdir(os.path.join(_OLDER_DIR,d))]
    ypos = len('qualitas-')
    years = [dirname[ypos:ypos+4] for dirname in dirs]
    return sorted(years)


# Default behaviour is to print out root dir (this is handy for shell scripts)
if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print(QUALITAS_ROOT)
    else:
        year = int(sys.argv[1])
        print(corpus_for_year(year))
