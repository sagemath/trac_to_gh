# Issue 1271: update Singular to 3-0-4 release

Issue created by migration from https://trac.sagemath.org/ticket/1271

Original creator: mabshoff

Original creation time: 2007-11-25 18:32:09

Assignee: malb

Singular 3-0-4 should be released shortly. The non-final sources are already available.

This should also close #1074

Cheers,

Michael


---

Comment by malb created at 2007-12-03 11:42:59

An updated spkg can be found at:

http://sage.math.washington.edu/home/malb/pkgs/singular-3-0-4-1-20071202.spkg

which installs fine on my notebook and on sage.math. After installing this spkg the attached patch trac1271.patch needs to be applied to fix a trivial doctest failure.

This new release fixes:
 * Singular is now GPLv2 or GPLv3
 * monitor segfault (#1074)
 * spkg-install modularized


---

Comment by malb created at 2007-12-03 11:42:59

Changing status from new to assigned.


---

Attachment

Patch looks good to me, build testing the new Singular.spkg on OSX.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-03 14:52:37

Resolution: fixed


---

Comment by mabshoff created at 2007-12-03 14:52:37

Merged in 2.8.15.rc1.
