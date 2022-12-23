# Issue 538: remove code duplication between sage/ext and c_lib

Issue created by migration from https://trac.sagemath.org/ticket/538

Original creator: dmharvey

Original creation time: 2007-08-31 01:19:10

Assignee: was

Some code duplication appeared as a result of the fix to #411. Remove all of the sage/ext stuff that now appears in `c_lib`.



---

Comment by dmharvey created at 2007-08-31 01:25:38

the `c_lib` directory in 2.8.3.rc4 also has a spurious .so file in it, which should be removed


---

Comment by craigcitro created at 2007-09-01 06:34:58

I think I've fixed this, though I'd like to test it on more architectures just to make sure. The hg bundle is available at:

http://sage.math.washington.edu/home/citro/patches/c_lib_fixes.hg

I'll also try to attach it to this ticket, but we'll see. Let me know if anyone runs into trouble with this.


---

Comment by craigcitro created at 2007-09-01 06:38:06

Changing assignee from was to craigcitro.


---

Comment by was created at 2007-09-01 17:45:45

Resolution: fixed


---

Attachment
