# Issue 4711: fix ptest race condition: "file not found"

Issue created by migration from https://trac.sagemath.org/ticket/4711

Original creator: mabshoff

Original creation time: 2008-12-05 06:24:50

Assignee: gfurnish


```

[10:16pm] mabshoff: gfurnish: just hit another race condition with ptest:
[10:16pm] mabshoff: sage -t  devel/sage/sage/gsl/gsl_sf_result.pxi
[10:16pm] mabshoff: Error running /scratch/mabshoff/release-cycle/sage-3.2.2.alpha0/local/bin/sage-doctest, since file gsl_sf_result.pxi does not exist.
[10:16pm] mabshoff: It is probably the same as the one where the doctest is only half written
[10:16pm] gfurnish: hm 
[10:17pm] gfurnish: don't touch anything
[10:17pm] gfurnish: let me look in your directory
[10:17pm] mabshoff: mk
[10:17pm] You are now known as mabs|ds0.
[10:17pm] You are now known as mab|ds9.
[10:17pm] mab|ds9:
[10:17pm] gfurnish: nothing in tmp dir?
[10:18pm] gfurnish: oh nm
[10:18pm] mab|ds9: The last line of the output was also "sage -t  devel/sage/sage/gsl/gsl_sf_result.pxi # File not found"
[10:18pm] gfurnish: that sounds like a ptest bug.
[10:19pm] gfurnish: yeah um
[10:19pm] gfurnish: I know whats causing that problem
[10:19pm] gfurnish: make a ticket
[10:20pm] gfurnish: I fixed the bug in pbuild
[10:20pm] mab|ds9: Is it orthogonal to the other race condition then I assume?
[10:21pm] gfurnish: I think so
```



---

Comment by mabshoff created at 2008-12-10 10:04:39

Gary,

it would be excellent if you could make this a priority since I have been hitting this race condition way more often than I used to.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-10 10:04:39

Changing priority from major to blocker.


---

Comment by gfurnish created at 2008-12-11 14:14:28

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-12-11 14:14:28

This is fixed by #4699 because previously threads were changing the current directory, and current directory is a per process state and not a per thread state.  By switching to pyprocessing, which uses processes instead of threads, the problem is removed.


---

Comment by mabshoff created at 2008-12-11 15:03:51

Fixed by #4699 merged in Sage 3.2.2.alpha2


---

Comment by mabshoff created at 2008-12-11 15:03:51

Resolution: fixed
