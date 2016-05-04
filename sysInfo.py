#!/usr/bin/env python
#a system information gathering script
#Carlos R. Manzano, 2016 AT&T
import subprocess

#command 1
uname = "uname"
uname_arg = "-a"
printf "gathering system information with %s command:\n" % uname
subprocess.call([uname, uname_arg])

#command 2
diskspace = "df"
diskspace_arg = "-h"
printf "gathering system information with %s command:\n" % diskspace
subprocess.call([diskspace, diskspace_arg])
