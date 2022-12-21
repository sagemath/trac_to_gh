# Issue 3063: empty matrices: norm() returns a ValueError

Issue created by migration from Trac.

Original creator: dfdeshom

Original creation time: 2008-04-30 15:10:44

Assignee: was


```
sage: a = matrix([])

sage: a.norm()
---------------------------------------------------------------------------

<type 'exceptions.ValueError'>: max() arg is an empty sequence
```


I think the answer in this case should be 0.


---

Attachment


---

Comment by dfdeshom created at 2008-04-30 17:54:47

Patch attached.


---

Comment by mabshoff created at 2008-05-01 05:46:36

Resolution: fixed


---

Comment by mabshoff created at 2008-05-01 05:46:36

Merged in Sage 3.0.1.alpha1
