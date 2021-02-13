#!/usr/bin/env bash
xterm -e git clone --recurse-submodules https://github.com/flightlessmango/MangoHud.git
cd MangoHud
./build.sh build
./build.sh package
./build.sh install
