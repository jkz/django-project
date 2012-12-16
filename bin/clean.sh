#!/bin/ksh
find "$ROOT" -name "*~" -exec rm {} \;
find "$ROOT" -name "*.pyc" -exec rm {} \;

