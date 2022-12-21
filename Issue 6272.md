# Issue 6272: upgrade to flint-1.3.0

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-06-12 18:51:11

Assignee: tbd

CC:  craigcitro

packages on sage.math, Craig knows where.


---

Comment by craigcitro created at 2009-06-14 08:31:53

Ok, I just reviewed the FLINT spkg. Everything looks good, with the caveat that we need to remember to turn the `spkg-check` back off before the final release.

On a related note, why do we have a perl script for checking the gcc version? If nothing else, here's a short shell script that does the same thing:

{{{#!/bin/sh

GCC_VERSION=`gcc -dumpversion`

case $GCC_VERSION in
    3.4*)
        echo "Found gcc 3.4.x"
	exit 0
	;;
    3.*)
        echo "WARNING: gcc version less than 3.4.0"
	exit 1
	;;
    2.*)
        echo "WARNING: gcc version less than 3.4.0"
	exit 1
	;;
    1.*)
        echo "WARNING: gcc version less than 3.4.0"
	exit 1
	;;
    *)
        echo "Found gcc 4 or later"
	exit 0
	;;
esac
```


I still prefer Python to both, but this seems more likely to be correctly maintained than the perl one. (Well, by me, anyway.)


---

Comment by craigcitro created at 2009-06-14 22:31:06

Resolution: fixed
