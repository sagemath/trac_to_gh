# Issue 2219: docs for root_field should say the polynomial needs to be irreducible

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-02-20 03:51:37

Assignee: was


```
root_field()
-- whose docstring does not say that self should be irreducible,
though in fact it must. 
```


See http://groups.google.com/group/sage-devel/browse_thread/thread/32fe12de12d5f6a5/c91753b5e65fe7b9#c91753b5e65fe7b9


---

Attachment

See the attached patch.


---

Comment by mhansen created at 2008-04-14 23:08:24

Looks good to me.


---

Comment by mabshoff created at 2008-04-15 00:31:55

Merged in Sage 3.0.alpha5


---

Comment by mabshoff created at 2008-04-15 00:31:55

Resolution: fixed
