# Issue 2338: [with patch, needs review] add p.lexLmDeg to PolyBoRi polynomials

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-02-27 20:47:58

Assignee: malb

CC:  burcin

some PolyBoRi functions need it, e.g. ll_encode


---

Attachment

A doctest needs to be added to this.


---

Attachment


---

Comment by malb created at 2008-02-28 00:17:59

The attached patch `lexLmDeg_doctest.patch` adds a doctest to the added method.


---

Comment by mhansen created at 2008-02-28 00:26:15

Applies to 2.10.3.alpha0 and passes tests for me.


---

Comment by mabshoff created at 2008-02-28 00:32:41

Resolution: fixed


---

Comment by mabshoff created at 2008-02-28 00:32:41

Merged both patches in Sage 2.10.3.rc0
