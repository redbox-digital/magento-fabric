import hashlib
import os

def random_filename(extension):
    """A random filename (with optional extension)"""
    extension = '.' + extension if extension else ''
    return hashlib.md5(os.urandom(64)).hexdigest() + extension
