# Issue 241: mod bug

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-02-03 19:13:09

Assignee: somebody


```
Hi William,
 
I don't consider this correct:
 
sage: x = -8
sage: x.mod(3)
-2
sage: x = 8
sage: x.mod(3)
2
 
If the convention where to return a value in (-n/2,n/2] rather than 
[0,n) then this could be justified.  But the output should depend 
only on x in Z/3Z, not on the representative.
 
It is also called in a rather convoluted way -- by creating an 
ideal then calling reduce on the ideal, then extracting the principal 
generator for the ideal.
```



---

Comment by roed created at 2007-04-13 03:55:25

Seems to be fixed in 2.4


---

Comment by roed created at 2007-04-13 03:55:25

Resolution: worksforme
