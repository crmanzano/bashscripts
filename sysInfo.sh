#!/usr/bin/env bash
#a system information gathering script
#Carlos R. Manzano, 2016 AT&T

#command 1
UNAME="uname -a"
printf "gathering system information with the $UNAME command: \n\n"
$UNAME

#command 2
DISKSPACE="df -h"
printf "gathering system information with the $DISKSPACE command: \n\n"
$DISKSPACE
