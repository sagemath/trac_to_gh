# Issue 6125: disable testing in flint, mpir, etc. packages

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2009-05-24 15:50:12

Assignee: mabshoff

In 4.0.rc0, at least the FLINT spkg has tests enabled. These should be disabled before the release.


---

Comment by mhansen created at 2009-05-29 04:26:46

Changing assignee from mabshoff to mhansen.


---

Comment by mhansen created at 2009-05-29 04:26:46

I have http://sage.math.washington.edu/home/mhansen/flint-1.2.4.p3.spkg and http://sage.math.washington.edu/home/mhansen/gmp-mpir-1.1.2.spkg which disable the tests.


---

Comment by mhansen created at 2009-05-29 04:26:46

Changing status from new to assigned.


---

Comment by was created at 2009-05-29 13:30:55

I've slightly modified the comment in spkg-install for both of the above spkg to make sense.  The logic is identical.  The modified spkgs:

http://sage.math.washington.edu/home/wstein/tmp/gmp-mpir-1.1.2.spkg

http://sage.math.washington.edu/home/wstein/tmp/flint-1.2.4.p4.spkg


---

Comment by mhansen created at 2009-05-29 17:31:03

Merged in 4.0.rc2.


---

Comment by mhansen created at 2009-05-29 17:31:03

Resolution: fixed
