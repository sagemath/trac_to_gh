# Issue 5983: cmp related doctest failure in sage/schemes/jacobians/abstract_jacobian.py

Issue created by migration from https://trac.sagemath.org/ticket/5983

Original creator: mabshoff

Original creation time: 2009-05-05 03:39:23

Assignee: mabshoff

CC:  alexghitza

This says it all and fails on occasion due to memory layout, etc. Writing a doctest this way is *wrong*:

```
sage -t -long "devel/sage/sage/schemes/jacobians/abstract_jacobian.py"
**********************************************************************
File "/home/mabshoff/build-3.4.2/sage-3.4.2-eno-gcc-4.3.3/devel/sage/sage/schemes/jacobians/abstract_jacobian.py", line 118:
    sage: J1 < P2
Expected:
    False
Got:
    True
**********************************************************************
File "/home/mabshoff/build-3.4.2/sage-3.4.2-eno-gcc-4.3.3/devel/sage/sage/schemes/jacobians/abstract_jacobian.py", line 120:
    sage: J1 > P2
Expected:
    True
Got:
    False
**********************************************************************
```

I am CCing Alex since I believe he wrote this doctest :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-05 03:39:36

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2009-05-05 04:21:02

Resolution: fixed


---

Comment by mabshoff created at 2009-05-05 04:21:02

Merged in Sage 3.4.2.

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-05-05 06:30:47

Replying to [ticket:5983 mabshoff]:
> I am CCing Alex since I believe he wrote this doctest :)

Yes, sorry about that.  It won't happen again (the bad cmp test, not writing doctest in general :)


---

Comment by mabshoff created at 2009-05-05 06:33:47

Replying to [comment:5 AlexGhitza]:

> Yes, sorry about that.  It won't happen again (the bad cmp test, not writing doctest in general :)

Hehe, I didn't catch this issue while running doctests dozens if not hundred of times on sage.math and many other systems, but it just triggered once on a SkyNet box. I also found an analog problem in other places, so you aren't the only one.

Keep the doctests coming ;)

Cheers,

Michael
