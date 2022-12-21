# Issue 2727: [with patch; needs review] uninitialized cdef in multi_polynomial_libsingular.pyx

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-03-29 22:32:55

Assignee: tabbott

The mysterious libsingular.dll errors in the Debian SAGE port were caused by an uninitialized variable masking the real error.


---

Attachment

Patch looks good to me. Positive review.


---

Comment by mabshoff created at 2008-03-29 23:06:25

Resolution: fixed


---

Comment by mabshoff created at 2008-03-29 23:06:25

Merged in Sage 2.11.rc0
