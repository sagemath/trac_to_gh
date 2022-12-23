# Issue 3801: [with patch, needs review] Spring layout for posets!!!

Issue created by migration from https://trac.sagemath.org/ticket/3801

Original creator: rlm

Original creation time: 2008-08-10 22:55:11

Assignee: rlm

This was originally motivated by removing `bruhat_sn.pyx`, but once Franco sat me down, he convinced me to work out spring layout for the `heights=` option. And it was easy!! Along the way we found and fixed several small bugs.


---

Comment by rlm created at 2008-08-10 22:58:40

This needs a small separate patch, on its way...


---

Attachment


---

Attachment


---

Comment by saliola created at 2008-08-11 00:29:15

Installs successfully, poset and graph doctests pass.


---

Comment by mabshoff created at 2008-08-11 00:47:42

Merged all three patches in Sage 3.1.alpha1


---

Comment by mabshoff created at 2008-08-11 00:47:42

Resolution: fixed
