#!/usr/bin/env bash
# Post install script for the UI .deb to place symlinks in places to allow the CLI to work similarly in both versions

set -e

ln -s /usr/lib/chinilla-blockchain/resources/app.asar.unpacked/daemon/chinilla /usr/bin/chinilla || true
ln -s /usr/lib/chinilla-blockchain/resources/app.asar.unpacked/daemon /opt/chinilla || true
