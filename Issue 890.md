# Issue 890: 2.8.7-alpha0: doctest failure in schemes/elliptic_curves/ec_database.py (database lookup failures)

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-10-13 20:40:42

Assignee: failure

Several failures; the following is typical:

```
File "ec_database.py", line 21:
    sage: elliptic_curves.rank(n=5, rank=3, tors=2, labels=True)
Expected:
    ['59450i1', '59450i2', '61376c1', '61376c2', '65481c1']
Got:
    []
```



---

Comment by cwitty created at 2007-10-13 23:03:31

This requires some database I can't find.  Probably the right patch is to mark the tests optional, but maybe William is planning to include this database as a standard package?


---

Comment by was created at 2007-10-14 05:11:46

Resolution: fixed


---

Comment by was created at 2007-10-14 05:11:46

I created the relevant spkg and put it in the repo.
