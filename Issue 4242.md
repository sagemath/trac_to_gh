# Issue 4242: Bugfix for dominates() method of partition.py (with patch; needs review)

Issue created by migration from Trac.

Original creator: jbandlow

Original creation time: 2008-10-04 14:06:47

Assignee: mhansen

CC:  sage-combinat

p.dominates(q) would give the wrong answer (True) if q had more boxes than p, but the first (length of p) parts of q were dominated by p.  Attached patch fixes this.


---

Attachment


---

Comment by mhansen created at 2008-10-04 14:37:59

Thanks Jason!  Looks good to me.


---

Comment by mabshoff created at 2008-10-07 17:07:10

Resolution: fixed


---

Comment by mabshoff created at 2008-10-07 17:07:10

Merged in Sage 3.1.3.alpha3


---

Comment by mabshoff created at 2008-10-07 17:39:59

Resolution changed from fixed to 


---

Comment by mabshoff created at 2008-10-07 17:39:59

With the patch applied I get

```
sage -t  devel/sage/sage/combinat/partition.py              
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.alpha3/tmp/partition.py", line 604:
    sage: Partition([]).dominates([1])
Expected:
    False
Got:
    True
**********************************************************************
```


I assumed that at least the patched file would be doctested :(

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-07 17:39:59

Changing status from closed to reopened.


---

Attachment

Looks good to me. Thanks Mike.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-12 19:49:15

Merged in Sage 3.1.3.rc0


---

Comment by mabshoff created at 2008-10-12 19:49:15

Resolution: fixed
