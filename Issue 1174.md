# Issue 1174: very minor bug in calculs _complex_ coercion.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-11-15 07:46:36

Assignee: was




---

Attachment

I noticed this very slight mistake recently...


---

Comment by robertwb created at 2007-11-18 08:34:14

I approve.


---

Comment by robertwb created at 2007-11-18 08:34:49

But there should be a doctest.


---

Comment by robertwb created at 2007-12-02 07:21:05

The patch is good, the problem is that none of the python functions (e.g. sqrt, sin) handle complex values.


---

Comment by was created at 2007-12-02 20:25:27

apply this after applying the other patch


---

Attachment


---

Attachment

Looks good to me; doctests pass in sage/calculus and sage/rings.  (Apply all three patches, in order.)


---

Comment by mabshoff created at 2007-12-02 22:07:56

Merged in 2.8.15.rc0.


---

Comment by mabshoff created at 2007-12-02 22:07:56

Resolution: fixed
