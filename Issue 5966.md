# Issue 5966: sage/sets/primes.py: change doctest so that we check for Primes being != to x^2+x

Issue created by migration from https://trac.sagemath.org/ticket/5966

Original creator: mabshoff

Original creation time: 2009-05-03 00:44:51

Assignee: mabshoff

This was reported by Kiran in https://groups.google.com/group/sage-devel/browse_thread/thread/776d8e0a25735dca

```
sage -t  "devel/sage/sage/sets/primes.py"
**********************************************************************
File "/opt/sage/sage-3.4.2.rc0/devel/sage/sage/sets/primes.py", line
80:
    sage: P>x^2+x
Expected:
    True
Got:
    False
********************************************************************** 
```

Don't test for `>`, but use `!=` since anything else is pointless. We should also compare to an MV polynomial ring ro avoid stating Maxima needlessly. 

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2009-05-04 06:41:46

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-05-04 09:31:52

Merged in Sage 3.4.2.final.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-04 09:31:52

Resolution: fixed
