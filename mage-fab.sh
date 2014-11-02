#! /usr/bin/env bash

# Location of this file (not the working dir).
# We need this because we only know the location of the fabfile
# relative to where this file is.
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
SCRIPT_DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"

# The fabfile sits as a sibling to this script.
FABFILE="$SCRIPT_DIR/fabfile"

# Run with original arguments.
fab -f "$FABFILE" "$@"

