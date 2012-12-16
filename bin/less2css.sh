#!/bin/sh

cd $ASSETS
lessc less/$NAME.less > css/$NAME.css
exit 0

