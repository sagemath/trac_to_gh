# Issue 6050: Dynkin diagram ascii art for reducible Cartan types (with patch, needs review)

Issue created by migration from Trac.

Original creator: bump

Original creation time: 2009-05-16 22:41:50

Assignee: tbd

After the patch, Dynkin diagram ascii art is available for reducible Cartan types.


```
sage: DynkinDiagram("F4xA2")

O---O=>=O---O
1   2   3   4
O---O
5   6
F4xA2
```



---

Comment by bump created at 2009-05-16 22:47:23

Changing assignee from tbd to bump.


---

Comment by mabshoff created at 2009-05-17 08:23:58

Changing component from algebra to combinatorics.


---

Attachment

Revised: CartanType in `type_reducible.py` needed a `dynkin_diagram` method.


---

Attachment


---

Comment by mhansen created at 2009-06-04 19:01:47

Looks good to me.

Merged in 4.0.1.rc1.


---

Comment by mhansen created at 2009-06-04 19:01:47

Resolution: fixed
