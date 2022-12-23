# Issue 6744: [with patch, needs review] install script stores start time of build

Issue created by migration from https://trac.sagemath.org/ticket/6744

Original creator: schilly

Original creation time: 2009-08-14 09:58:17

Assignee: tbd

In order to track the build progress, it is necessary to store the start time of the build process. (elapsed time, estimate of remaining time, ...) 

This patch inserts a line in "install" which stores the seconds since 1970-1-1 in a hidden file `.BUILDSTART` in `%SAGE_ROOT` when the build process starts. This could also be useful for other applications. 


---

Attachment


---

Comment by mvngu created at 2009-08-14 10:21:02

The patch should be applied against the file `SAGE_ROOT/spkg/install`. That file is not under revision control, so one has to manually apply the patch.


---

Comment by schilly created at 2009-08-14 10:27:37

note: don't forget to update this file on the master-mirror, too! it lives in `sage`@`sagemath:~/www-files/packages/install`


---

Comment by timdumol created at 2009-08-30 18:30:40

I don't see how this can hurt anything. Tried building anyways, no problem.


---

Comment by mvngu created at 2009-08-31 08:20:27

Resolution: fixed


---

Comment by drkirkby created at 2010-09-30 06:25:09

Although this is marked as fixed, it should be noted that it makes use of a non-portable option to the `date` command so fails on some systems. See 

http://www.opengroup.org/onlinepubs/009695399/utilities/date.html

for a list of portable options. 

Since the file created is not actually used by anything it's not a big problem, but if anyone tried using it on a Unix system, it would likely fail. A better method is:


```
# Compute seconds since the Epoch.

# Call 'date'. Note that
# %Y = year including century
# %j = day number (1-365)
# %H = hour (0-23)
# %M = minute (0-59)
# %S = seconds (0-59)

if type env >/dev/null 2>&1 ; then
    set -- `env LC_ALL=C LC_TIME=C LANG=C date -u '+%Y %j %H %M %S'`
else
    set -- `date -u '+%Y %j %H %M %S'`
fi

# $1 = year including century
# $2 = day number (1-365)
# $3 = hour (0-23)
# $4 = minute (0-59)
# $5 = seconds (0-59)

if [ $? -ne 0 ] || [ $# -lt 5 ] ; then
  TIME="Error computing seconds since the Epoch"
fi

DAYS=`expr 365 \* \( $1 - 1970 \) + \( $1 - 1969 \) / 4 + $2 - 1`
TIME=`expr $5 + 60 \* \( $4 + 60 \* \( $3 + 24 \* $DAYS \) \)`
echo $TIME
```

