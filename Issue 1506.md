# Issue 1506: ntl spkg -- dumb intentional error during the build

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-14 17:11:11

Assignee: was

This is dumb:


```
dmharvey: i'm building sage-2.9alpha7, and there's a problem in the build log with the NTL build, but the rest of it seems to be going okay (for the moment)
[06:49am] dmharvey: i686-apple-darwin8-g++-4.0.1: unrecognized option '-shared'
[06:49am] dmharvey: _main
[06:49am] dmharvey: ___gmpn_add_n
[06:49am] dmharvey: ___gmpn_addmul_1
[06:49am] dmharvey: ___gmpn_divrem_1
[06:49am] dmharvey: ___gmpn_gcd
```



---

Comment by was created at 2007-12-14 17:35:23

New spkg at 

 http://sage.math.washington.edu/home/was/tmp/ntl-5.4.1.p8.spkg


---

Comment by mabshoff created at 2007-12-14 22:28:06

Resolution: fixed


---

Comment by mabshoff created at 2007-12-14 22:28:06

Merged in 2.9.rc0.
