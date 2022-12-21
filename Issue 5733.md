# Issue 5733: bug in 3d plotting of graphs

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-04-10 14:19:31

Assignee: rlm


```
sage: G=Graph({'a':['a','b','b','b','e'],'b':['c','d','e'],'c':
sage: ['c','d','d','d'],'d':['e']})
sage: G.show3d()
Traceback (most recent call last):
...
ZeroDivisionError: float division
```


Reported by alec`@`mihailovs


---

Comment by jason created at 2009-04-10 14:38:18

Apparently show3d() chokes on loops (that's the error: I think it's trying to make a cylinder (edge) with length 0).  Also, show3d doesn't show multiple edges.


---

Comment by rlm created at 2009-04-10 15:32:23

This needs to be implemented, but until then it needs to fail more gracefully. Thus the proposed patch. If implementing this isn't a ticket yet, it probably should be.


---

Attachment


---

Comment by mabshoff created at 2009-04-13 06:23:19

Merged in Sage 3.4.1.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-13 06:23:19

Resolution: fixed
