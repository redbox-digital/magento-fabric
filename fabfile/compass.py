import os.path as path
from fabric.api import local

def compass_compile(magento_root):
    """Compile all compass projects.

    Find all Compass projects and compile them. This will not compile
    the Compass projects in the `rwd` theme, because they are given to
    us compiled, and use an unknown version of Compass. And they will
    not change.
    """
    compass_projects = compass_project_roots(magento_root)

    for compass_project in compass_projects:
        compile_project(compass_project)

def compass_clean(magento_root):
    """Clean all compass projects.

    Find all Compass projects and remove all generated files, but not
    those in `rwd` theme.
    """
    compass_projects = compass_project_roots(magento_root)
    for compass_project in compass_projects:
        clean_project(compass_project)

def compass_project_roots(magento_root):
    """Find all Compass projects.

    Search for `config.rb` in `skin/frontend`, and convert this into
    a list. This will not return any Compass projects in the `rwd`
    namespace.
    """
    configs = compass_configs(magento_root)
    return [path.dirname(config) for config in configs]

def compass_configs(magento_root):
    """Find all config.rb files not in `rwd`"""
    path = path.join(magento_root, 'skin/frontend')
    found = local('find -L %s -name config.rb' % path, capture=True)
    return [config for config in found.split('\n') if is_valid(config)]

def is_valid(config):
    """Is a config not in `rwd`?"""
    return 'skin/frontend/rwd' not in config

def compile_project(compass_project):
    """Compile a compass project."""
    local('compass compile %s -e development' % compass_project)

def clean_project(compass_project):
    """Clean a Compass project."""
    local('compass clean %s' % compass_project)

