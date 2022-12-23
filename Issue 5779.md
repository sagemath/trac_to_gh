# Issue 5779: _fast_floats_'s pow returns garbage for non-integral powers left of zero

Issue created by migration from https://trac.sagemath.org/ticket/5779

Original creator: mabshoff

Original creation time: 2009-04-13 20:04:51

Assignee: mabshoff

CC:  cwitty

I thought we had fixed this via fast_callable, but it is still there:

```
mabshoff@sage:/scratch/mabshoff/sage-3.4.1.rc3$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: f=x^(1/3)
sage: f._fast_float_(x)(-1.2)
nan
sage: 
```

This is exposed via a plotting failure on Solaris where NaNs pop up. Fixing that in the plotting code is a different ticket William will open shortly.
| Sage Version 3.4.1.rc2, Release Date: 2009-04-10                   |
| Type notebook() for the GUI, and license() for information.        |
Cheers,

Michael


---

Comment by mabshoff created at 2009-04-13 20:05:45

Changing assignee from mabshoff to robertwb.


---

Comment by mabshoff created at 2009-04-13 20:13:27

Hmm, the c library is involved here as shown by this on Solaris:

```
-bash-3.00$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: main-sol
sage: f=x^(1/3)
sage: f._fast_float_(x)(-1.2)
-NaN
```

| Sage Version 3.4.1.rc1, Release Date: 2009-04-05                   |
| Type notebook() for the GUI, and license() for information.        |
I am not so sure what is going on or if this is the real issue. I will talk to RobertWB in person about this on the next occasion.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-13 21:53:48

Hmm, the issue here might be plain and simply calling the math libraries pow() function.  So don't invalidate this ticket since we are definitely hitting some issue on Solaris here.

Cheers,

Michael


---

Comment by robertwb created at 2009-04-13 22:24:19

I fixed the new fast float (fast callable) not the old one. However, the old one is a simple fix too--I'll post a patch shortly.


---

Comment by mabshoff created at 2009-04-13 22:59:18

Replying to [comment:4 robertwb]:
> I fixed the new fast float (fast callable) not the old one. However, the old one is a simple fix too--I'll post a patch shortly. 

Cool, note that #5780 does fix an issue when the axes code in plotting encounters a NaN or Infinity, so you might want to apply that one before doctesting.

Cheers,

Michael


---

Attachment

OK, I did the same thing as for fast_callable.


---

Comment by mabshoff created at 2009-04-16 07:40:56

I am happy with this patch even though it likely introduces a slowdown which I did not measure. Since correctness is more important than speed especially in light of completely wrong results I give this patch a positive review. All doctests do pass, too :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-16 07:41:28

Merged in Sage 3.4.1.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-16 07:41:28

Resolution: fixed
