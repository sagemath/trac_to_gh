# Issue 1407: deciding that generators don't generate an order in some extensions can be way way too slow.

Issue created by migration from https://trac.sagemath.org/ticket/1407

Original creator: was

Original creation time: 2007-12-06 04:02:24

Assignee: was

Consider this:


```
sage: P.<a,b,c> = QQ[2^(1/2), 2^(1/3), 2^(1/5)]
sage: P.order([1,a])
*should* go boom very quickly... but runs forever and runs out of RAM
```


In the situation above, a satisfies only a quadratic polynomial so 
there is no possible way it will generate an order in a degree 8 field,
since the index [O_K : ZZ[a]] is clearly infinite.   Sage should
quickly detect this and give an error message, but doesn't for some
reason. 



---

Attachment


---

Attachment

Minor doctest touchups.


---

Comment by mabshoff created at 2007-12-15 11:57:19

Merged in 2.9.rc0.


---

Comment by mabshoff created at 2007-12-15 11:57:19

Resolution: fixed
