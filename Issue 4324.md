# Issue 4324: [with patch, needs review] fix storage of GBs for PolyBoRi

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-10-19 15:54:13

Assignee: tbd

CC:  polybori

The current code prevents certain GB calculations to finish because it throws a ValueError just before the GB is returned (quit annoying).


---

Attachment


---

Comment by PolyBoRi created at 2008-10-21 08:10:42

the patch is okay.
Note, that the bug can only occur, when a system is passed, which is not a minimal GB.
However, that's possible.

In the future version PolyBoRi 0.6 pure reduction can be implemented more efficiently without handling sets.
However, you will need a different workaround there

```
r=ReductionStrategy()
if not p.lead() in r.leading_terms:
  r.add_generator(p)
```



---

Comment by mabshoff created at 2008-10-26 14:13:30

Merged in Sage 3.2.alpha1


---

Comment by mabshoff created at 2008-10-26 14:13:30

Resolution: fixed
