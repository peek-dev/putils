#!/usr/bin/bash

UTILS_ROOT="/opt/putils/"
BIN_PATH="$UTILS_ROOT/bin"

mkdir -p $UTILS_ROOT
mkdir $BIN_PATH

install diceware/diceware $BIN_PATH
install -d diceware/ "$UTILS_ROOT/diceware"
