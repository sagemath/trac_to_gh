# Issue 6169: upgrade mpir to 1.2

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-05-31 07:51:14

Assignee: mabshoff

1. Upgrade mpir to version 1.2.

2. Change the name of the spkg from gmp-mpir to mpir and the error message from "there was a problem building gmp" to there was a problem building "mpir", so there are no complaints about us muddying the name of gmp when something goes wrong with building mpir.


---

Comment by was created at 2009-05-31 21:07:25

See http://sage.math.washington.edu/home/wstein/release/4.0.1/alpha0/stuff/mpir-1.2.spkg


---

Comment by was created at 2009-06-02 19:19:32

New version here

http://sage.math.washington.edu/home/wstein/release/4.0.1/alpha0/stuff/mpir-1.2.p1.spkg


---

Comment by mhansen created at 2009-06-04 06:17:29

Looks good to me.

Merged mpir-1.2.p1.spkg in 4.0.1.rc0.


---

Comment by mhansen created at 2009-06-04 06:17:29

Resolution: fixed
