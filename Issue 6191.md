# Issue 6191: atlas -- make it so SAGE_FAT_BINARY only used on x86

Issue created by migration from https://trac.sagemath.org/ticket/6191

Original creator: was

Original creation time: 2009-06-02 21:31:27

Assignee: tbd

I couldn't build atlas on itanium and was puzzled why.  It turns out I had the SAGE_FAT_BINARY environ variable set.    This update to the atlas spkg fixes it so that environ variable has no impact on itanium.




---

Comment by was created at 2009-06-02 21:31:50

The spkg is here: http://sage.math.washington.edu/home/wstein/release/4.0.1/alpha0/stuff/atlas-3.8.3.p3.spkg


---

Comment by was created at 2009-06-02 21:32:15

Changing priority from major to blocker.


---

Comment by mhansen created at 2009-06-04 06:39:05

Changes look good to me.

Merged in 4.0.1.rc0.


---

Comment by mhansen created at 2009-06-04 06:39:05

Resolution: fixed
