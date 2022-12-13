#!/usr/bin/env bash
# Post install script for the UI .deb to place symlinks in places to allow the CLI to work similarly in both versions

set -e

ln -s /opt/chinilla/resources/app.asar.unpacked/daemon/chinilla /usr/bin/chinilla || true
ln -s /opt/chinilla/chinilla-blockchain /usr/bin/chinilla-blockchain || true
