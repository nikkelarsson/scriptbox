% SCREENCAPTURE(1) screencapture 0.1.0rc1  
% Niklas Larsson  
% Feb 2022  

# NAME
screencapture - take a screenshot of current screen

# SYNOPSIS
**screencapture**

# DESCRIPTION
**screencapture** uses **imagemagick**'s utility, **import**, to take a
screenshot of the current screen. By default, it also tries to display a
notification using **notify-send**, indicating that a screenshot was taken.

For each day, when taking screenshots, **screencapture** creates a directory,
where it saves the screenshots from that day. Each directory is named with a
date. Furthermore, screenshots in each directory are labeled with a timestamp.
This makes it easy to search screenshots later.
