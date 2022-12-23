# Issue 4478: delete spkg-debian-maybe

Issue created by migration from https://trac.sagemath.org/ticket/4478

Original creator: was

Original creation time: 2008-11-09 08:13:11

Assignee: tabbott

How can this file be serious?

```
wstein@one:~/devel/sage$ more spkg-debian-maybe
#!/bin/sh -x
BUILD_ROOT=../../../
mv dist/debian $BUILD_ROOT
cd $BUILD_ROOT/..
echo "Starting Debian build"
dasource ./sage-2.10.1
sbuildhack "$DEBIAN_RELEASE" *.dsc
echo "Debian Build complete"
```


See for example the "sage-2.10.1"


---

Comment by tabbott created at 2008-11-10 02:54:37

The system for building all the dependencies Sage needed as Debian packages that never really worked for Sage itself, but this was a prototype for it dating to the sage 2.10 era.  Feel free to delete it.


---

Comment by mabshoff created at 2008-11-10 04:14:05

Changing assignee from tabbott to mabshoff.


---

Comment by mabshoff created at 2008-11-10 04:14:05

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-11-10 04:14:05

This needs some careful fix, i.e. the file exists in two places:

```
./local/bin/spkg-debian-maybe
./devel/sage-main/spkg-debian-maybe
```

But it is also referred to in two places:

```
devel/sage-main/setup.py
devel/sage-main/spkg-dist
```


Cheers,

Michael


---

Attachment

patch for local/bin repository


---

Comment by craigcitro created at 2009-05-27 04:36:20

I've added two patches to fix this. Note that `spkg-debian-maybe` was *not* under version control in `$SAGE_ROOT/local/bin` -- it was only mentioned in `.hgignore`. (It wouldn't hurt to leave that in there, I guess, so feel free to ignore the second patch.)

Note that the main repo patch depends on #6133 -- both touch `MANIFEST.in`, so one had to depend on the other in the end ... and I wrote the other first, so that's how it ended up.

I'm sure this patch could wait for `4.0.1` -- but the "clean dead files in the build directory" script I'm just finishing for #5977 notices it, so we might as well just kill it now.


---

Comment by craigcitro created at 2009-05-27 04:36:20

Changing status from assigned to new.


---

Comment by craigcitro created at 2009-05-27 04:36:20

Changing assignee from mabshoff to craigcitro.


---

Attachment


---

Comment by mhansen created at 2009-05-28 20:07:54

Resolution: fixed


---

Comment by mhansen created at 2009-05-28 20:07:54

The previous patch was doubled up so it caused failures on applying.  The new trac-4478.patch applies.

Both patches merged in 4.0.rc2.
