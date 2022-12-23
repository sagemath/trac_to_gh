# Issue 6146: [with patch, needs review] the detection of SAGE_ROOT in $SAGE_ROOT/sage script should expand symlinks recursively (fix this on systems that do *NOT* support readlink -f)

Issue created by migration from https://trac.sagemath.org/ticket/6146

Original creator: was

Original creation time: 2009-05-28 07:00:10

Assignee: cwitty

See #5852.


---

Comment by tornaria created at 2009-07-02 00:00:06

test implementation of realpath in bash for systems which don't support realpath/readlink -f


---

Attachment

I've attached a proof-of-concept of a bash script which correctly computes the SAGE_ROOT as a fully canonicalized path. This is a tarball which includes the script itself, and a bunch of symlinks to the same script in different configurations, plus a test script which shows the result of the computation of SAGE_ROOT in the different cases.

To test, untar, `cd sage-realpath-test` and run `./test`. Sample output:

```
==========================================================
The following lines of output should all be identical, and
point to the canonicalized path of directory sage_root
==========================================================

SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
SAGE_ROOT:/home/tornaria/sage-realpath-test/sage_root:
```

This is a correct run, because all the runs gave the same canonical path (which is the correct canonical path).

The script uses `realpath`, then `readlink -f`, and fall back to a bash function; but for testing purposes, the fallback to bash function is always tried.

I've successfully tested this on:
 - linux with no realpath, but readlink -f works (my laptop)
 - linux with realpath (sage.math)
 - mac with fink (which supports readlink -f)
 - mac with fink disabled (remove it from path)
 - t2 (trying this found out some gnuisms or non-sunisms which I had to fix)

Maybe somebody can try this on the build farm to check that it is safe... Assuming what we really want is for SAGE_ROOT to be the fully canonicalized path (see the last comments in #5852).

BTW, this already gives an absolute path, so there would be no need to `cd $SAGE_ROOT` here and `cd $CUR` back in sage-sage (ugly hack).


---

Comment by mhansen created at 2009-10-19 18:27:14

Changing status from new to needs_review.


---

Comment by malb created at 2010-04-05 16:36:57

Changing status from needs_review to needs_work.


---

Comment by malb created at 2010-04-05 16:36:57

This isn't a patch etc. so it cannot be reviewed yet. I'll change the status to `needs work`.


---

Comment by jdemeyer created at 2011-08-18 21:37:57

Resolution: duplicate


---

Comment by tornaria created at 2011-08-19 01:48:41

Replying to [comment:5 jdemeyer]:
 - resolution set to duplicate

Duplicate of which ticket?

For convenience, here's a copy of the path-detection code in the tarball above. The tarball also contains a number of tests for different cases of symlinks in-the-path or in-the-script.


```/usr/bin/env bash

realpath_bash()
{
    fname="${1%/}" # strips trailing '/'
    while [ -L "$fname" ] ; do
        dir="$(dirname "$fname")"
        fname="$(command ls -l "$fname")"
        fname="${fname#*\> }"
        if [ "$fname" = "." ] ; then
            fname="$dir"
        elif echo "$fname" | grep -v '^/' > /dev/null ; then
            fname="$dir/$fname"
        fi
    done
    pushd "$(dirname "$fname")" > /dev/null
    echo "$(pwd -P)/$(basename "$fname")"
    popd > /dev/null
}

SAGE_PATH="$(realpath "$0" 2> /dev/null)" || \
SAGE_PATH="$(readlink -f "$0" 2> /dev/null)" || \
SAGE_PATH="$(realpath_bash "$0" 2> /dev/null)" || \
SAGE_PATH="$0"

SAGE_ROOT="$(dirname "$SAGE_PATH")"

echo "SAGE_ROOT:$SAGE_ROOT:"
```


Please see also the discussion in #5852, which is concerned with canonicalizing $SAGE_ROOT when readlink -f is available --- a fix that works for that case was merged in 4.0.rc1 and reverted in 4.1.rc0 because it caused a regression for somebody.

This ticket is concerned with how to portably canonicalize $SAGE_ROOT in general (when readlink -f is not available) and it was stalled because canonicalization (as done in #5852) caused other issues that weren't resolved. Once using a fully canonical $SAGE_ROOT is workable (using readlink -f) then we can expand the portability of the canonicalization using the solution proposed here (or any other solution).

[see also #11707]
