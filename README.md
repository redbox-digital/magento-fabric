

# Magento Fabric Tasks

A set of fabric tasks to make setting up local projects easier.

I wrote these tasks while I was developing a Vagrant set up. What I
found was that these were useful enough in their own right to become a
separate thing. This is that thing.


## Dependencies

Naturally, Fabric and its dependencies need to be installed. Further,
these tasks make heavy use of N98-Magerun. You will need to install it
both on your local computer, and on the server you're pulling data from.

If you want to run the `compass_*` commands, of course you will need
Compass installed. If you don't want compass, then just don't call the
relevant tasks.


## Installation

Install with composer. A pull request has been sent to the composer
repository. Currently, you have to add this repository manually.

Once it's added, you can call `mage-fab.sh` in `vendor/bin`. However,
since you might want to use this globally, you can install it
globally with composer, and then use it across all projects. This is
the preferred approach.

Either way, just call that shell file and give it the task name and
any necessary arguments as normal arguments.


## Usage

To use any of the tasks described below, put yourself in the root of
your Magento installation and run `mage-fab task_name`.

In order for any task that gets information from a server to work,
you will need to have a file named `mage-fabric.json` in a directory
somewhere above you. The possible fields are below. For fields labelled
as optional, the value they hold is the default:

```javascript
{
  // A valid hostname:
  "ssh-host": /* unset */,
  // (optional) Port to connect to:
  "ssh-port": 22,
  // Username to connect as:
  "ssh-user": /* unset */,
  // (optional) SSH password:
  "ssh-password": /* unset */,
  // (optional) Location of SSH key to connect with:
  "ssh-key-filename": /* unset */,

  // (optional) Location of N98-Magerun on the server:
  "magerun": "/usr/local/bin/n98-magerun.phar",
  // (optional) Temporary directory on the server:
  "tmp-dir": "/tmp",
  // Location of Magento installation on the server:
  "magento-root": /* unset */
}
```

Note that if you are only using commands that do not talk to a server,
you will still need a `mage-fabric.json` file, and it needs to be a
valid JSON file (which is just `{}`). Sorry that it means another
stupid JSON file in the root of your project.


## Tasks

### Compass

The compass tasks find all compass projects under `skin/frontend`, but
ignore `rwd/default` and `rwd/enterprise`.


#### `compass_compile`

Clean and compile all compass projects.


#### `compass_clean`

Clean all Compass projects. That is to say, remove all generated
content. Note that this is run each time `compass_compile` is
called anyway, so there is no need to run it beforehand.


### Database

#### `database_pull`

Make a stripped dump on the configured server, pull it down, and
import it to the current local project.

#### `database_create`

Create the database as specified in `local.xml`


### Media

Currently, the only task added is `media_pull`, which makes a dump of
the media directory on the server, pulls it down and recursively copies
it to the current local project.

