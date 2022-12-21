# Issue 6075: dsage is not yet entirely optional

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-05-18 21:02:20

Assignee: yi

CC:  craigcitro

Keywords: dsage optional spkg

For 4.0, dsage was made an optional spkg.  However, if I rm -rf build/ and sage -ba, the newly built tree has no dsage.


---

Comment by mhansen created at 2009-05-26 20:49:25

Changing assignee from yi to mhansen.


---

Comment by mhansen created at 2009-05-26 20:49:25

Changing status from new to assigned.


---

Comment by mhansen created at 2009-05-26 20:49:25

I've added a patch that makes things continue to work if dsage is not there.  However, we really should make it so that dsage does not install into sage.dsage.  This requires quite a few more changes within dsage itself.


---

Attachment


---

Comment by mhansen created at 2009-05-28 02:47:15

I updated the patch and made http://sage.math.washington.edu/home/mhansen/dsage-1.0.1.spkg which moves DSage from sage.dsage to just dsage.


---

Comment by craigcitro created at 2009-05-28 04:57:51

Yep, this looks good. You have to manually remove `$SAGE_ROOT/devel/sage/build/sage/dsage` to see that this completely works, but then, that's exactly what the patch at #5977 does for you ...


---

Comment by mhansen created at 2009-05-28 05:07:16

Resolution: fixed


---

Comment by mhansen created at 2009-05-28 05:07:16

Merged in 4.0.rc1.
