# Issue 846: Split cdefs.pxi

Issue created by migration from https://trac.sagemath.org/ticket/846

Original creator: robertwb

Original creation time: 2007-10-10 10:53:06

Assignee: was

CC:  craigcitro

This should probably go into several different files. At least the gmp stuff could be moved to a different file (perhaps the current gmp.pxi should be renamed?) 


---

Comment by robertwb created at 2008-10-15 21:32:08

This should be more relevant now that .pxd files are more flexible. cdefs.pxi is sometimes reparsed 5-10 times.


---

Comment by robertwb created at 2008-11-20 23:14:51

Don't forget to put mpz_set_longlong in stdsage.


---

Attachment

Also, this now has the complete list of gmp functions found in the manual.


---

Comment by robertwb created at 2008-11-22 00:43:16

See also #4579 about mpz_set_longlong


---

Comment by robertwb created at 2008-11-22 01:40:12

See also #4580


---

Attachment

Very nice!  My patch fixes a couple of compile errors; with my patch, all doctests pass.

Positive review.  Apply both patches.


---

Comment by mabshoff created at 2008-11-23 03:48:47


```
[7:40pm] cwitty: Argh... and #4564 conflicts with 846-more-gmp-reviewer.patch (I was wondering why the original patch didn't even compile...)
[7:41pm] mabshoff: mmmh
[7:41pm] mabshoff: So I don't need the reviewer patch I assume.
[7:41pm] cwitty: You need the half of it that creates an __init__.py file; probably not the half that patches integer.pyx .
[7:44pm] mabshoff: mk
[7:45pm] mabshoff: I assume that is lost in RobertWB's patch since hg screws up the empty file creation as usual.
[7:45pm] mabshoff: I will copy and paste the last couple lines to the ticket and then merge it.
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-11-23 06:01:44

Resolution: fixed


---

Comment by mabshoff created at 2008-11-23 06:01:44

Merged both patches (the reviewer patch was limited to the first hunk) in Sage 3.2.1.alpha0
