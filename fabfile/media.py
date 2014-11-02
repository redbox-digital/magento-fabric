import os.path as path

from fabric.api import task, cd, run, get, lcd, local

from .helpers import random_filename

def media_pull(tmp_dir, magerun, magento_root):
    """SSH to remote server and get media folder.

    This uses the magical N98-Magerun, and it needs to be a fairly
    recent version, so make sure that it's installed somewhere globally
    accessible.

    In config.json, there is a field to supply the path to it, so there
    really is no excuse.

    The dump is then downloaded and unzipped into the Magento instance.
    """
    media_filename = random_filename('zip')
    media_location = path.join(tmp_dir, media_filename)

    with cd(magento_root):
        run('%s media:dump --strip %s' %
                (magerun, media_location))

        get(remote_path=media_location, local_path='/tmp')

    with lcd('/tmp'):
        local('unzip %s' % media_filename)
        local('cp -r media %s' % magento_root)

