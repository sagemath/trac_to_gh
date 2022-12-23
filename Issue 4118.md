# Issue 4118: [with patch, needs review] fix various Pari-related issues

Issue created by migration from https://trac.sagemath.org/ticket/4118

Original creator: craigcitro

Original creation time: 2008-09-14 11:49:11

Assignee: craigcitro

This patch fixes two things:

 1. In various places, we used something like `x.type() == 't_INT'` in Cython code, and with Pari already linked in. In this case, it's much faster to use `typ(x.g) == t_INT`. 
 1. Several `_sig_on`s were missing, so I've gone through and added the ones I saw missing. 




---

Attachment


---

Comment by mabshoff created at 2008-09-14 11:58:03

Nice patch. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-14 13:32:59

Merged in Sage 3.1.2.rc3


---

Comment by mabshoff created at 2008-09-14 13:32:59

Resolution: fixed
