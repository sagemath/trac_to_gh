# Issue 8006: Identation syntax errors fail silently

Issue created by migration from https://trac.sagemath.org/ticket/8006

Original creator: acleone

Original creation time: 2010-01-20 01:52:43

Assignee: was

CC:  timdumol chapoton

See #6729

This fails silently

```
CELL 1:
 u = 2
  u = 3
CELL 2:
print u # = 2
```


This should fail with an `IdentationError`, as it does in `%python`:

```
CELL 1:
 u = 2
  u = 3
# generates IdentationError
```



---

Comment by kcrisman created at 2014-12-09 19:38:46

This is likely related to https://github.com/sagemath/sagenb/issues/288 as well, though it seems to be slightly different.


---

Comment by kcrisman created at 2014-12-09 19:40:16

See https://github.com/sagemath/sagenb/issues/289


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.


---

Comment by dimpase created at 2020-08-25 09:36:02

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-08-29 15:27:35

Resolution: invalid
