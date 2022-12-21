# Issue 222: field mutability issue

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-01-26 07:09:28

Assignee: somebody


```
cwitty: Yuck:
[10:48pm] cwitty: sage: RS = RealField(sci_not=True)
[10:48pm] cwitty: sage: R == RS
[10:48pm] cwitty: sage: RS.scientific_notation(False)
[10:48pm] cwitty: sage: RR == RS
[10:48pm] cwitty: (Oops... second line should be "RR == RS")
[10:49pm] cwitty: Second line prints False, fourth line prints True.  Shouldn't fields be immutable?
```



---

Comment by was created at 2007-10-21 02:36:57


```


```



---

Comment by was created at 2007-10-21 02:36:57

Resolution: fixed


---

Attachment
