#!/bin/bash
# Cleans up files/directories that may be left over from previous runs for a clean slate before starting a new build

set -o errexit

PWD=$(pwd)

rm -rf ../venv || true
rm -rf venv || true
rm -rf chinilla_blockchain.egg-info || true
rm -rf build_scripts/final_installer || true
rm -rf build_scripts/dist || true
rm -rf build_scripts/pyinstaller || true
rm -rf chinilla-blockchain-gui/build || true
rm -rf chinilla-blockchain-gui/daemon || true
rm -rf chinilla-blockchain-gui/node_modules || true
rm -rf chinilla-blockchain-gui/api/dist || true
rm -rf chinilla-blockchain-gui/api/node_modules || true
rm -rf chinilla-blockchain-gui/api-react/dist || true
rm -rf chinilla-blockchain-gui/api-react/node_modules || true
rm -rf chinilla-blockchain-gui/core/dist || true
rm -rf chinilla-blockchain-gui/core/node_modules || true
rm -rf chinilla-blockchain-gui/gui/build || true
rm -rf chinilla-blockchain-gui/gui/node_modules || true
rm -rf chinilla-blockchain-gui/icons/dist || true
rm -rf chinilla-blockchain-gui/icons/node_modules || true
rm -rf chinilla-blockchain-gui/wallets/dist || true
rm -rf chinilla-blockchain-gui/wallets/node_modules || true
rm chinilla-blockchain-gui/temp.json || true
( cd "$PWD/chinilla-blockchain-gui" && git checkout HEAD -- package-lock.json ) || true
cd "$PWD" || true

# Clean up old globally installed node_modules that might conflict with the current build
rm -rf /opt/homebrew/lib/node_modules || true

# Clean up any installed versions of node so we can start fresh
brew list | grep "^node\@\|^node$" | xargs -L1 brew uninstall || true
