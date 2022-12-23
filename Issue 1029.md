# Issue 1029: update flint in sage again

Issue created by migration from https://trac.sagemath.org/ticket/1029

Original creator: was

Original creation time: 2007-10-29 05:39:31

Assignee: somebody

From Bill Hart:


```
Hi William,

I've just dug another pile of bugs out of FLINT. All functions in
fmpz_poly normalise correctly now (or at least they should).

I ran a much more comprehensive set of tests, checking for unusual
corner cases. I found a handful of them and removed them.

I've also added a make all to the makefile.

Functions still may not deal with length zero polynomials correctly
(though most functions do) and with aliased inputs, so there will
probably be more changes over the next few days. But for now, FLINT is
much more bulletproof than it was.
```


Moreover, the svn revision to get it: 1045


---

Comment by was created at 2007-10-29 19:16:41

Actually, update to 1047:

```
As of revision 1047 all functions now deal correctly with length zero
functions. I have also added some managed functions for scalar
multiplication of a polynomial by a scalar. I've also hardened some of
the memory management functions so that stupid users who try to
allocate -1 limbs won't run into unexpected trouble.
```



---

Comment by robertwb created at 2007-11-15 01:39:13

Changing assignee from somebody to was.


---

Comment by robertwb created at 2007-11-15 01:39:13

Changing component from basic arithmetic to packages.


---

Comment by robertwb created at 2007-11-15 01:39:13

New flint spkg and bundle (to apply to sage-main) up at

http://sage.math.washington.edu/home/robertwb/flint/


---

Comment by mabshoff created at 2007-11-15 15:47:26

Ok, this should go into 2.8.13. I will ask for somebody to review this.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-18 10:28:49

This looks good to me and should be in 2.8.13.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-18 14:18:44

Resolution: fixed


---

Comment by mabshoff created at 2007-11-18 14:18:44

Merged in 2.8.13.alpha0.


---

Comment by mabshoff created at 2007-11-18 21:08:51

I fixed a ntl linking issue, so now there is a flint-0.9.p0.spkg

Cheers,

Michael
