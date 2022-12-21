# Issue 2354: bug in matrix_real_double_dense  (trivial to fix)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-02-29 17:41:14

Assignee: was


```
        _n.flags = _n.flags|(NPY_OWNDATA) # this sets the ownership bug
```


but should be

```
        _n.flags = _n.flags|(NPY_OWNDATA) # this sets the ownership bit
```





---

Attachment


---

Comment by dfdeshom created at 2008-03-03 17:57:29

Changing priority from major to trivial.


---

Comment by dfdeshom created at 2008-03-03 17:57:29

Changing assignee from was to dfdeshom.


---

Comment by dfdeshom created at 2008-03-03 17:57:29

Changing status from new to assigned.


---

Comment by AlexGhitza created at 2008-03-11 01:10:50

Looks good.


---

Comment by mabshoff created at 2008-03-12 22:09:01

Resolution: fixed


---

Comment by mabshoff created at 2008-03-12 22:09:01

Merged in Sage 2.10.4.alpha0
