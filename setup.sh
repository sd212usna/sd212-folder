#!/usr/bin/env bash

set -euo pipefail
cd "$(dirname "$0")"

echo "Configuring git so that your changes won't be overridden..."
git config pull.strategy recursive
git config pull.strategyOption ours
echo "git config done"

echo "Checking whether pixi is installed..."
if [[ ! -e ~/.pixi/bin ]]; then
    echo "pixi not found, installing pixi..."
    curl -fsSL https://pixi.sh/install.sh | sh
    echo "pixi is installed"
else
    echo "pixi is already installed"
fi

echo "Setting up pixi environment..."
~/.pixi/bin/pixi install
echo "pixi packages are installed"

echo "Checking for club..."
if command -v club >/dev/null; then
    echo "club is installed"
else
    echo "installing club..."
    git clone https://gitlab.usna.edu/roche/club.git ~/.club
    mkdir -p ~/bin
    ln -s ../.club/club ~/bin/club
fi

echo
echo "Setup is complete!"
echo "Recommend you close VS code now if it's open,"
echo "then re-open your sd212 folder to get the new environment."

: