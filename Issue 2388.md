# Issue 2388: linbox charpoly crashes on OS X 10.5-intel

Issue created by migration from Trac.

Original creator: cpernet

Original creation time: 2008-03-04 21:55:42

Assignee: mabshoff

The proposed linbox-1.1.5rc1.p0 crashes on OS X 10.5-intel for charpoly computations.
The bug shows up at initialization of static variables, and may be related to the specific OS X gcc compiler behaviour.

[http://gcc.gnu.org/ml/gcc-bugs/2004-02/msg02055.html](http://gcc.gnu.org/ml/gcc-bugs/2004-02/msg02055.html), may help.


---

Attachment


---

Comment by cpernet created at 2008-03-04 22:03:26

I fixed the bug by changing the algorithm for charpoly, that I had to change anyway (faster).
This fixes the bug, since the buggy code is no longer used.

The fixed spkg is available at
[http://sage.math.washington.edu/home/pernet/linbox-1.1.5rc2.p1.spkg](http://sage.math.washington.edu/home/pernet/linbox-1.1.5rc2.p1.spkg)

The clean fix will be in ticket 2389.


---

Comment by cpernet created at 2008-03-04 22:03:26

Changing assignee from mabshoff to cpernet.


---

Comment by mabshoff created at 2008-03-05 05:51:34

Positive review after fixing various issues in the repo, i.e. 

```
M SPKG.txt
! linbox_wrap/src/linbox_wrap.cpp~
! linbox_wrap/src/linbox_wrap.h~
? linbox_wrap/src/linbox_wrap.cpp.ori
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-03-05 05:52:44

Merged in Sage 2.10.3.rc2


---

Comment by mabshoff created at 2008-03-05 05:52:44

Resolution: fixed
