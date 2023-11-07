#!/usr/bin/env python3

import os
import sys
import subprocess

Binance = [
    # 'aria2c -d ~/Downloads https://download.binance.com/electron-desktop/linux/production/binance-amd64-linux.deb',
    'cd "$HOME"/Downloads',
]


def build_app():
    if len(sys.argv) != 2:
        print("Usage: build-app <argument>")
        return

    argument = sys.argv[1]

    if argument == "binance":
        for cmd in Binance:
            subprocess.run(cmd, shell=True, check=True)


if __name__ == "__main__":
    build_app()
