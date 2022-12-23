# Issue 4658: magma -- get rid of redundant caching: just have _magma_init_

Issue created by migration from https://trac.sagemath.org/ticket/4658

Original creator: was

Original creation time: 2008-11-29 23:50:12

Assignee: was




---

Attachment


---

Attachment


---

Comment by mabshoff created at 2008-11-30 08:35:38

Positive review. I had various discussions with William about this patch while he was writing it. 

The patch passes doctests with a booby trapped magma to flush out doctest failures without magma, it passes standard long doctests as well as -only_optional=magma. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-30 08:35:50

Resolution: fixed


---

Comment by mabshoff created at 2008-11-30 08:35:50

Merged in Sage 3.2.1.rc1
