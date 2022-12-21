# Issue 187: [Pyrex] c-code mis-interpretation

Issue created by migration from Trac.

Original creator: joel

Original creation time: 2006-12-19 02:32:23

Assignee: was

I found a small bit of code that gets compiled incorrectly to c.  A sample is:


```
def unlist():
        lst = [1,2]
        lst,m = lst
```


The translated c-code from this will produce an Unindexable exception.  This 
results from the fact that the variable "lst" is bound to the first element 
of the list (the integer 1) before the second element is extracted 
from "lst".  Hence it tries to unpack from the integer rather than the list.


---

Comment by mabshoff created at 2007-08-28 18:56:22

This is a rather old bug. We should verify that the problem still exists.

tagged for 2.9, hopefully to be resolved during Sage Bug Day 2.

Cheers,

Michael


---

Comment by was created at 2008-01-19 23:29:10

Resolution: fixed


---

Comment by was created at 2008-01-19 23:29:10

works for me now.
