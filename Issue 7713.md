# Issue 7713: Use unicode strings for all text in the Sage notebook

Issue created by migration from https://trac.sagemath.org/ticket/7713

Original creator: timdumol

Original creation time: 2009-12-16 13:16:28

Assignee: was

This causes errors, such as those noted in L2261-2266 of `worksheet.py` (UnicodeDecodeError). This is also needed for transition to Python 3, and blocks #7269.


---

Comment by timdumol created at 2010-01-19 16:14:34

Resolution: duplicate


---

Comment by timdumol created at 2010-01-19 16:14:34

#7249 resolves this.
