# Issue 5683: Inverse operation for matrices over non integral domain

Issue created by migration from Trac.

Original creator: klee

Original creation time: 2009-04-04 20:33:09

Assignee: somebody

Keywords: inverse

We get this: 


```
sage: R=IntegerModRing(8)
sage: m=matrix(R,2,[2,1,3,3]);
sage: m.inverse()
Traceback (most recent call last):
...
TypeError: self must be an integral domain.
```


The inverse operation for matrices over non integral domain, in particular for over integer mod rings, is a missing feature. Somebody should *definitely* implement this.  A
first reasonable thing would be "lift to ZZ, invert, reduce".


---

Attachment


---

Comment by cremona created at 2009-04-05 15:52:55

Positive review: applies fine to 3.4.1.apha0 and tests in the file changed pass.

I was disappointed that the similar thing does not work for residue rings of number field rings of integers, since I thought I had fixed it so that the reduction maps worked ok, but unfortunately that only works for residue fields, not residue rings.  (Even then, you have to say OK.residue_field(P) and not OK.quotient(P) for it to work properly).

Never mind, this patch is still good!


---

Comment by jhpalmieri created at 2009-04-05 16:46:58

apply on top of the other patch


---

Attachment

You have a slightly misformatted docstring which the second patch fixes.

(This is another use of the patches at #5653: you can view the Sphinx version of an individual docstring to see if it's formatted correctly.  This even works for docstrings which don't appear in the reference manual, such as for functions like `__invert__` which start with an underscore.)


---

Comment by cremona created at 2009-04-05 17:08:04

Replying to [comment:3 jhpalmieri]:
> You have a slightly misformatted docstring which the second patch fixes.
> 
> (This is another use of the patches at #5653: you can view the Sphinx version of an individual docstring to see if it's formatted correctly.  This even works for docstrings which don't appear in the reference manual, such as for functions like `__invert__` which start with an underscore.)

That sounds very useful.  normally I never use the notebook interface, but with this I can see myself using it to test docstring formats if nothing else!


---

Comment by mabshoff created at 2009-04-06 00:46:39

Merged both patches in Sage 3.4.1.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-06 00:46:39

Resolution: fixed
