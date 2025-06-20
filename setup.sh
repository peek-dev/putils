#!/usr/bin/bash

# NOTE: if installing to /opt/, this script MUST be run with superuser
# privileges.

UTILS_ROOT="/opt/putils/"
BIN_PATH="$UTILS_ROOT/bin"

mkdir -p $UTILS_ROOT
mkdir -p $BIN_PATH

install -v diceware/diceware $BIN_PATH
install -v -d diceware/ "$UTILS_ROOT/diceware"
install -v diceware/* "$UTILS_ROOT/diceware/"
