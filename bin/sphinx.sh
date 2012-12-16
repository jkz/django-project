#!/bin/sh

cd $ROOT/doc
sphinx-build -b html ./source ./build
exit 0

