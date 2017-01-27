#!/bin/bash

set -e
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DIR=`realpath "$DIR/.."`

TARGET="$DIR/deploy.zip"
if [[ -f "$TARGET" ]]; then 
  rm -f "$TARGET"
fi

find -iname "*.py" ! -iname "test*" | zip -@ deploy.zip 
