# Issue 4048: missing minpoly for GF(p)

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-09-03 17:43:18

Assignee: was

Nick Alexander reports in https://groups.google.com/group/sage-devel/browse_thread/thread/e5538e40d2b89002

```
sage: GF(241^2, 'a')(1).minpoly() 
x + 240 
sage: GF(241, 'a')(1).minpoly() 
--------------------------------------------------------------------------- 
AttributeError                            Traceback (most recent call   
last) 
... 
AttributeError: 'sage.rings.integer_mod.IntegerMod_int' object has no   
attribute 'minpoly' 
```





---

Attachment


---

Comment by AlexGhitza created at 2009-01-22 01:22:36

See the attached patch.


---

Comment by boothby created at 2009-01-23 10:51:25

works for me


---

Comment by mabshoff created at 2009-01-24 17:13:57

Merged in Sage 3.3.alpha2


---

Comment by mabshoff created at 2009-01-24 17:13:57

Resolution: fixed
