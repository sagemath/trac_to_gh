# Issue 3669: [with patch; needs review] improve multiple_of_order command for torsion subgroups of modular abelian varieties

Issue created by migration from https://trac.sagemath.org/ticket/3669

Original creator: was

Original creation time: 2008-07-16 23:32:28

Assignee: was




---

Attachment


---

Comment by craigcitro created at 2008-07-17 00:34:26

This looks good. I might consider switching self.__multiple_of_order to self._multiple_of_order, but no other complaints at all.


---

Comment by craigcitro created at 2008-07-17 00:35:20

Mind you, that should say `self.__multiple_of_order` to `self._multiple_of_order`. Silly trac markup.


---

Comment by mabshoff created at 2008-07-18 09:25:36

Resolution: fixed


---

Comment by mabshoff created at 2008-07-18 09:25:36

Merged in Sage 3.0.6.alpha1
