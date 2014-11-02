import json
import os
import os.path as path

# Todo: Add some kind of friendly error handling
def _find_config_file():
    """Search in all parent directories for mage-fabric.json."""
    filename = 'mage-fabric.json'
    trial_dir = os.getcwd()

    while True:
        trial_file = path.join(trial_dir, filename)
        trial_parent = path.dirname(trial_dir)
        if path.isfile(trial_file):
            return trial_file
        elif trial_dir == trial_parent:
            raise EnvironmentError('No mage-fabric.json file found in any parent')
        else:
            trial_dir = trial_parent

_config = json.load(open(_find_config_file()))

def get(*args, **kwargs):
    """Proxy to dict.get()"""
    _config.get(*args, **kwargs)

def ssh_is_enabled():
    return get('ssh-host') is not None

