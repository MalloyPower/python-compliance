import os.path

QUALITAS_ROOT = '/media/passport/bigApps/qualitas-python'

def get_root_dir():
    return QUALITAS_ROOT

def file_for(app):
    return os.path.join(QUALITAS_ROOT, app)

def get_dirnames(root=QUALITAS_ROOT):
    ''' Return a list of all subdirectories of a directory '''
    dirs = [d for d in os.listdir(root)
            if os.path.isdir(os.path.join(root,d))]
    return sorted(dirs, key=lambda s: s.lower()) # Case insensitive sort

def basename(path):
    ''' Only chop off the Qualitas dir, leave subdirs from application'''
    return path[len(QUALITAS_ROOT):]

