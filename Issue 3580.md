# Issue 3580: ensure that numpy is not imported on startup.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-07 02:56:55

Assignee: cwitty

CC:  craigcitro jvoight

This is a followup to #3577 that is forced by a merge conflict.


---

Comment by mabshoff created at 2008-11-02 03:00:30

Currently sage.rings.number_field.totallyreal_data imports numpy at startup. That might be due to the cythonization of totallyreal*, but I am not sure.

Cheers,

Michael


---

Comment by craigcitro created at 2008-11-07 18:12:02

Moved the `import` further in, which was fine (didn't slow things down).

Michael, should we add the following as a doctest somewhere?


```
sage: search_src("^import", "numpy")

sage: search_src("^from", "numpy")

```



---

Comment by craigcitro created at 2008-11-07 18:12:02

Changing assignee from cwitty to craigcitro.


---

Comment by craigcitro created at 2008-11-07 18:12:02

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-11-07 18:17:09

We already have a doctest that is supposed to catch this (via grepping for numpy in "sage -startuptime"), but I think we should add a test in $SAGE_ROOT/devel/sage/tests that looks for the import of numpy in "from sage import all". Right now John's totally real code imports numpy, but the doctest to detect a numpy import at the top level is broken.

What I would like to see is to not import numpy each time, but use something like the mechanism in 

http://trac.sagemath.org/sage_trac/attachment/ticket/3498/numpy-3.patch

The mechanism from that patch should be be stuck somewhere in the global namespace and we should enforce its use, i.e. a patch reviewed seeing something like a straight numpy import should complain.

Cheers,

Michael


---

Comment by craigcitro created at 2008-11-09 04:23:46

This removes the numpy import from the totally real enumeration code, and it fixes a pesky but somewhat serious bug in the code. 

John Voight and I team wrote/reviewed this.

I will open a new ticket for the new import of numpy on startup.


---

Comment by craigcitro created at 2008-11-09 04:23:46

Changing priority from major to blocker.


---

Comment by mabshoff created at 2008-11-09 08:20:44

There is a slight problem:

```
sage -t -long devel/sage/sage/rings/number_field/totallyreal_data.pyx
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.rc0/devel/sage/sage/rings/number_field/totallyreal_data.pyx", line 200:
    sage: [RealField(10)(x) for x in ls]
Expected:
    [-1.0000, -1.0000]
Got:
    [-1.0, -1.0]
**********************************************************************
1 items had failures:
```



---

Attachment


---

Comment by craigcitro created at 2008-11-09 08:22:37

Oops. Ticket updated.


---

Comment by mabshoff created at 2008-11-09 08:24:18

Resolution: fixed


---

Comment by mabshoff created at 2008-11-09 08:24:18

Merged in Sage 3.2.rc0
