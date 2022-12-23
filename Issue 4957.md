# Issue 4957: inconsistent integer hashing

Issue created by migration from https://trac.sagemath.org/ticket/4957

Original creator: robertwb

Original creation time: 2009-01-09 02:26:00

Assignee: somebody


```
sage: z = 18446462603027742720
sage: hash(z)
66912258
sage: hash(int(z))
-131071
sage: hash(long(z))
-131071
```


This causes problems with looking up values in hashtables...


---

Comment by craigcitro created at 2009-01-23 12:51:21

This was *ugly*. It turns out that we were shifting an `int` to the right by 45 bits on a 32 bit machine, which one might think would result in zero, but in fact shifts to the right by `(45%32) = 13` bits.

The attached patch fixes this, and adds some doctests.


---

Comment by craigcitro created at 2009-01-23 12:51:21

Changing assignee from somebody to craigcitro.


---

Comment by craigcitro created at 2009-01-23 12:51:21

Changing status from new to assigned.


---

Comment by robertwb created at 2009-01-23 13:22:14

Excellent. I haven't been able to break it, and the code (and comment) look good.


---

Comment by mabshoff created at 2009-01-24 14:22:51

This is broken on 64 bit linux:

```
sage -t -long "devel/sage/sage/rings/integer.pyx"           
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha2/devel/sage/sage/rings/integer.pyx", line 2085:
    sage: n = -920390823904823094890238490238484; n.__hash__()
Expected:
    6874330978542788722   
Got:
    6917515397235318898
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha2/devel/sage/sage/rings/integer.pyx", line 2101:
    sage: hash(n)
Expected:
    -9223372036854767616      
Got:
    8192
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha2/devel/sage/sage/rings/integer.pyx", line 2104:
    sage: hash(n) == hash(int(n))
Expected:
    True
Got:
    False
**********************************************************************
```



---

Comment by robertwb created at 2009-01-24 21:50:10

Darn :(. The first two may be OK (we need to see what hash(int(n)) is, but the second one is a problem.


---

Attachment


---

Comment by craigcitro created at 2009-01-24 23:25:17

Ok, I fixed it. It turns out it was some sloppy C coding on my part: I really wanted `sizeof(mp_limb_t)` instead of `sizeof(int)`.


---

Comment by robertwb created at 2009-01-24 23:27:02

I bet this is the right fix, could you re-run the tests on a 64 bit machine?


---

Comment by robertwb created at 2009-01-24 23:40:35

That does the trick on sage.math


---

Comment by mabshoff created at 2009-01-25 21:01:36

Merged in Sage 3.3.alpha3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-25 21:01:36

Resolution: fixed
