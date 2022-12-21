# Issue 796: Yet another fix for c_lib/scons stuff

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2007-10-03 00:04:24

Assignee: craigcitro

Keywords: c_lib

The scons setup was still sub-par, and after some discussion, we've come up with what looks like a good solution. Here's the new system ... first, we reorganize $SAGE_ROOT/devel/sage/c_lib into c_lib/src and c_lib/include,  and removed some cruft in the c_lib directory. We now have two symlinks:

$SAGE_ROOT/local/lib/libcsage.[so|dylib] --> $SAGE_ROOT/devel/sage/c_lib/libcsage.[so|dylib]

$SAGE_ROOT/local/include/csage --> $SAGE_ROOT/devel/sage/c_lib/include

Now we've had to make some changes to spkg-install to get this to work well. In particular, *this patch should not be added until the next release*, because getting it via hg_sage.pull() could break your working sage. 

There are patches for both sage-main and scripts-main attached.

Email me (craig) if you have any issues with this patch.


---

Attachment


---

Comment by craigcitro created at 2007-10-03 00:06:07

Changing status from new to assigned.


---

Comment by was created at 2007-10-04 17:39:31

Resolution: fixed
