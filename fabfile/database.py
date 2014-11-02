import os.path as path

import fabric.api as fab
from .helpers import random_filename

def create_database():
    """Create the database specified locally."""
    with lcd(magento_root):
        local('n98-magerun.phar db:create')

def database_pull(tmp_dir, magerun, magento_root):
    """Import a server's database.

    Export a developer stripped database and import it to the local
    installation of Magento.

    Note that this command should be run only on one server role. If
    this advice is ignored, then each database import will overwrite
    the previous one and it will take a lot longer than it needs to.
    """
    db_filename = random_filename('sql.gz')
    remote_db = path.join(tmp_dir, db_filename)
    local_db = path.join('/tmp', db_filename)

    with cd(magento_root):
        run('%s db:dump -s "@development" -f %s' % (magerun, db_filename))

    get(db_filename, db_filename)
    local('n98-magerun db:import %s' % db_filename)

