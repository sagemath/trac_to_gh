# Issue 2806: Sage 3.0.a2: numerical noise in sage/misc/prandom.py doctest

Issue created by migration from https://trac.sagemath.org/ticket/2806

Original creator: mabshoff

Original creation time: 2008-04-05 14:28:33

Assignee: jkantor

CC:  cremona

John Cremona reported:

```
sage -t  devel/sage/sage/misc/prandom.py
**********************************************************************
File "/home/jec/sage-3.0.alpha1/tmp/prandom.py", line 285:
    sage: [vonmisesvariate(1.0r, 3.0r) for i in range(1, 5)]
Expected:
    [0.89832863935542584, 0.67180300070412846, 2.0308777524813397,
1.7143252537251459]
Got:
    [0.89832863935542584, 0.67180300070412846, 2.0308777524813397,
1.7143252537251454]
**********************************************************************
```


Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-04-05 15:22:14

John,

can you test if this trivial patch fixes the issue for you? The problem is that vonmisesvariate() uses standard libm math functions and hence has some precision issues.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-05 15:22:14

Changing assignee from jkantor to mabshoff.


---

Comment by mabshoff created at 2008-04-05 15:22:14

Changing status from new to assigned.


---

Comment by cremona created at 2008-04-05 15:51:13

Yes, that works for me.


---

Comment by mabshoff created at 2008-04-05 16:19:01

Resolution: fixed


---

Comment by mabshoff created at 2008-04-05 16:19:01

Merged in Sage 3.0.alpha2
