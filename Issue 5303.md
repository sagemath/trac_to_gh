# Issue 5303: Sage 3.3.rc2: numerical noise in sage/schemes/elliptic_curves/sha_tate.py

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-18 11:55:21

Assignee: mabshoff

CC:  cremona


```
sage -t -long "devel/sage/sage/schemes/elliptic_curves/sha_tate.py"
**********************************************************************
File "/Users/mabshoff/sage-3.3.rc1/devel/sage/sage/schemes/elliptic_curves/sha_tate.py", line 88:
    sage: [sha.an_numerical(prec) for prec in xrange(30,100,10)] # long time
Expected:
    [1.0000000,
    1.0000000000,
    1.0000000000000,
    1.0000000000000000,
    1.0000000000000000000,
    1.0000000000000000000000,
    1.0000000000000000000000000]
Got:
    [0.99999969, 1.0000000000, 1.0000000000000, 1.0000000000000000, 1.0000000000000000000, 1.0000000000000000000000, 1.0000000000000000000000000]
**********************************************************************
```



---

Comment by mabshoff created at 2009-02-20 10:46:48

Hi John,

there are several suggestions on how to fix this:

 * start off with 40 bit of precision, but this might hide a bug
 * check if the value is within some eps of 1, the same comment about hiding a bug might apply here

Thoughts?

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2009-02-20 18:18:15

This patch avoids the computation for prec=30 and thus gets rid of the numerical problem. This might not be the right long term fix, but it is a good fix for 3.3.

John: If you think that this should be reverted and fixed in some other way please open another ticket in case this got merged.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 18:18:15

Changing status from new to assigned.


---

Comment by cremona created at 2009-02-20 19:58:14

Replying to [comment:3 was]:

I was not in time but this seems a reasonable compromise to me!


---

Comment by mabshoff created at 2009-02-20 20:55:29

Resolution: fixed


---

Comment by mabshoff created at 2009-02-20 20:55:29

Merged in Sage 3.3.rc3.

Cheers,

Michael
