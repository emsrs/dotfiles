#!/bin/sh
#
# ~/.xinitrc
#
# Executed by startx (run your window manager from here)

xset r rate 300 50 &
feh --bg-fill ~/Pictures/Nord.png &
redshift &
exec dwm 
