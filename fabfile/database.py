import os.path as path

import fabric.api as fab
from .helpers import random_filename

def create_database():
    """Create the database specified locally."""
    fab.local('n98-magerun.phar db:create')

def database_pull(tmp_dir, magerun, magento_root):
    """Import a server's database.

    Export a developer stripped database and import it to the local
    installation of Magento.

    Note that this command should be run only on one server role. If
    this advice is ignored, then each database import will overwrite
    the previous one and it will take a lot longer than it needs to.
    """
    db_filename = random_filename('sql')
    remote_db = path.join(tmp_dir, db_filename)
    local_db = path.join('/tmp', db_filename)

    with fab.cd(magento_root):
        fab.run('%s db:dump -s "@development" -f %s' % (magerun, remote_db))

    fab.get(remote_db, local_db)
    fab.local('n98-magerun.phar db:import %s' % local_db)

