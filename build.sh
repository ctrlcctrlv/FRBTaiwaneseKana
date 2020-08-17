#!/bin/bash

FONTFORGE=/home/osboxes/Workspace/fontforge/build/bin/fontforge
if test -z $DEBUG; then DEBUG='INFO'; fi

if test -e $FONTFORGE; then
    true
else
    FONTFORGE=`which fontforge`
fi

$FONTFORGE -lang=py -script build.py
