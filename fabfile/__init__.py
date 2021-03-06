from fabric.api import task, env
from . import database, media, compass, config

if config.ssh_is_enabled():
    env.hosts = [config.get('ssh-host')]
    env.port = config.get('ssh-port')
    env.user = config.get('ssh-username')
    env.password = config.get('ssh-password')
    env.key_filename = config.get('ssh-key-filename')
else:
    pass

@task
def create_database():
    """Create the database specified in local.xml."""
    database.create_database()

@task
def database_pull():
    """Pull a stripped database from the server."""
    tmp_dir = config.get('tmp-dir')
    magerun = config.get('magerun')
    magento_root = config.get('magento-root')
    database.database_pull(tmp_dir, magerun, magento_root)

@task
def media_pull():
    """Pull media dump from server."""
    tmp_dir = config.get('tmp-dir')
    magerun = config.get('magerun')
    magento_root = config.get('magento-root')
    media.media_pull(tmp_dir, magerun, magento_root)

@task
def compass_compile():
    """Compile all compass projects."""
    compass.compass_compile()

@task
def compass_clean():
    """Clean all compass projects."""
    compass.compass_clean()

