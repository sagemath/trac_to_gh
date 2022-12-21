# Issue 4123: TOOLCHAIN_ENV script

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-09-15 01:09:50

Assignee: mabshoff




---

Comment by mabshoff created at 2008-09-15 10:51:17

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-09-15 10:51:17

If $SAGE_ROOT/toolchain/toolchain-env exists we should source it from sage-env so that using a custom toolchain (for example for Solaris, Linux MIPS64, Itanioum) is trivial.

Cheers,

Michael


---

Attachment


---

Comment by rlm created at 2008-09-15 11:45:15

Looks good.


---

Comment by mabshoff created at 2008-09-15 11:45:56

Merged in Sage 3.1.2.rc4


---

Comment by mabshoff created at 2008-09-15 11:45:56

Resolution: fixed
