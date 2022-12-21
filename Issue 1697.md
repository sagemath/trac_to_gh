# Issue 1697: two polynomial_modn_dense_ntl.pyx memleaks

Issue created by migration from Trac.

Original creator: wjp

Original creation time: 2008-01-05 23:53:45

Assignee: mabshoff

The classes Polynomial_dense_modn_ntl_zz and Polynomial_dense_modn_ntl_ZZ construct a zz_pX_c resp. ZZ_pX_c object, but have no __dealloc__ method to destruct them.

Patch attached.


---

Attachment


---

Comment by mabshoff created at 2008-01-06 13:03:55

Looks good to me, extensively tested (6+ hours of valgrinding)

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-06 13:04:11

Merged in 2.9.3


---

Comment by mabshoff created at 2008-01-06 13:04:11

Resolution: fixed
