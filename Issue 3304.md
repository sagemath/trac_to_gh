# Issue 3304: [with patch; needs review] Make cddlib Debian package use shared library

Issue created by migration from https://trac.sagemath.org/ticket/3304

Original creator: tabbott

Original creation time: 2008-05-26 01:31:25

Assignee: tabbott

CC:  vbraun mhampton

I've attached a patch to make the Debian package use the cddlib shared library code.


---

Comment by craigcitro created at 2008-06-15 21:31:26

Changing keywords from "" to "editor_mabshoff".


---

Attachment


---

Attachment


---

Comment by tabbott created at 2008-12-12 20:48:44

Earlier today I attached a version of the patch that doesn't mess with dist/debian (since that's no longer relevant).


---

Comment by mabshoff created at 2009-02-15 07:12:26

Well, given how long we have been sitting on this reduce priority to critical.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-15 07:12:26

Changing priority from blocker to critical.


---

Comment by vbraun created at 2010-01-27 17:34:57

Has nothing to do with Debian, maybe that was misleading; summary changed.

The following spkg is patched in a similar way. It essentially contains tabbott's patch, but I found this report only after making the changes myself.

http://www.stp.dias.ie/~vbraun/cddlib-094f.p3.spkg 

Users of the Fedora 12 binary sage distribution must manually re-install mpir-1.2.2.p0.spkg as discussed on http://groups.google.com/group/sage-devel/msg/aec4aa6b3874fe10. This is an unrelated bug of the build system.


---

Comment by vbraun created at 2010-01-27 17:34:57

Changing status from needs_work to needs_review.


---

Comment by vbraun created at 2010-01-27 17:34:57

Changing priority from critical to major.


---

Comment by vbraun created at 2010-01-31 12:57:08

Superseded by #8115


---

Comment by was created at 2010-06-02 23:08:44


```
As I understand,

http://trac.sagemath.org/sage_trac/ticket/3304

should be just closed, not reviewed, since another ticket took care of
the issue.

Since only release managers should close tickets, I am leaving the
ticket as is and posting here.

Thank you,
Andrey
```



---

Comment by was created at 2010-06-02 23:09:00

Resolution: fixed
