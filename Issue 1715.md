# Issue 1715: [with patch, needs review] PolyBoRi pickling/hasing

Issue created by migration from https://trac.sagemath.org/ticket/1715

Original creator: malb

Original creation time: 2008-01-07 15:41:40

Assignee: malb

CC:  burcin mabshoff

Pickling and hashing of PolyBori rings and polynomials.


---

Comment by malb created at 2008-01-09 13:32:47

I've added a speed-up patch `unpickle_polybori.patch` which should be applied after the first patch `trac_1715.patch`


---

Comment by malb created at 2008-01-09 13:33:22

Note that doctests will SEGFAULT with these patches until #1712 is resolved.


---

Comment by mabshoff created at 2008-01-13 17:55:27

Now that I merged #1668 this needs to be rebased. But I could also edit the patch directly and fix the various names analog to #1668.

Cheers,

Michael


---

Attachment


---

Comment by malb created at 2008-01-17 13:24:37

The attached patch `trac_1715.patch` applies cleanly against `2.10.alpha4` and contains all patches posted here earlier, i.e. only this patch needs to be applied.


---

Comment by burcin created at 2008-01-17 14:06:56

The patch looks good, should go in for 2.10.


---

Comment by mabshoff created at 2008-01-17 14:28:21

Merged in Sage 2.10.alpha5


---

Comment by mabshoff created at 2008-01-17 14:28:21

Resolution: fixed


---

Comment by mabshoff created at 2008-01-19 08:40:31

Merged in Sage 2.10.1.alpha0. Initially this was merged in Sage 2.10.alpha5, but since 2.10.alpha4 become the release it was postponed and finally merged now.
