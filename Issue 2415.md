# Issue 2415: update NTL to 5.4.2 (bugfix release)

Issue created by migration from https://trac.sagemath.org/ticket/2415

Original creator: dmharvey

Original creation time: 2008-03-07 03:31:08

Assignee: mabshoff

Changelog says:

 * Fixed a bug in the sub(ZZ_pEX, ZZ_pE, ZZ_pEX) and sub(zz_pEX, zz_pE, zz_pEX) routines (reported by Charanjit Jutla). Under certain circumstances, these could outout wrong answers.



---

Comment by mabshoff created at 2008-03-24 14:29:42

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.11/alpha2/ntl-5.4.2.spkg

upgrade to the 5.4.2 release, fixes SPKG.txt and also integrates the OSX 10.5 64 bit build support.

Builds fine on Linux and OSX.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-24 14:29:42

Changing status from new to assigned.


---

Comment by jkantor created at 2008-03-24 17:15:24

Tested that the package built. Also did testall, all tests passed.


---

Comment by mabshoff created at 2008-03-24 17:17:12

Resolution: fixed


---

Comment by mabshoff created at 2008-03-24 17:17:12

Merged in Sage 2.11.alpha2
