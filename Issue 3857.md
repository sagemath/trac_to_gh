# Issue 3857: BinaryQF_reduced_representatives in binry_qf.py produces extra unreduced forms

Issue created by migration from Trac.

Original creator: choldsworth

Original creation time: 2008-08-14 21:07:07

Assignee: was

For example 

```
sage: BinaryQF_reduced_representatives(-63)

[2*x^2 - x*y + 8*y^2,
 4*x^2 - x*y + 4*y^2,
 x^2 + x*y + 16*y^2,
 2*x^2 + x*y + 8*y^2,
 4*x^2 + x*y + 4*y^2,
 3*x^2 + 3*x*y + 6*y^2]
```


However, clearly:


```
4*x^2 - x*y + 4*y^2
```


isn't a reduced form.
BinaryQF_reduced_representatives is incorrectly classifying some forms.



---

Attachment


---

Comment by cremona created at 2008-08-23 17:26:12

The patch applies cleanly to 3.1.1 and doctests pass.

However, there are some things I really do not like about this implementation:

    1. `self.reduce()` computes (if necessary) caches and returns the reduced form equivalent to self.  I would expect it to change self into the reduced form, and have a different function self.reduced_form() to do what this function does.

    2. The function `is_reduced()` actually reduces self and tests if the result is the same as self.  This is potentially very expensive!  To test `is_reduced()` you should just test that the usual inequalities are satisfied.

    3. The function `BinaryQF_reduced_representatives(D)` -- where the bug was -- proceeds in a way very different to what I have always done, with the outer loop being over b.  For a start you should only loop over b's of the same parity as D, not over all b's and then compute and test if `b^2-D` is a multiple of 4.  Then, this method requires factoring all those values of `(b^2-D)/4` to get possible a's -- another expensive and quite unnecessary set of computations.  Finally, the list is not sorted as I think it should be.

I would like to rewrite this function, but the current patch can be applied and a new ticket opened if anyone agrees with me.


---

Comment by choldsworth created at 2008-08-25 00:36:44

Patch implementing a superior BinaryQF_reduced_representatives method.


---

Attachment

I have submitted a new patch (superseding my first patch), re-implementing the BinaryQF_reduced_representatives method, and addressing your point 3.

I agree the other points need fixing but feel they should have their own ticket, or at least separate patches.

Here are some timings from the new method.

Old code:

```
sage: timeit("BinaryQF_reduced_representatives(-4004)")
5 loops, best of 3: 29.6 s per loop
```


New code:

```
sage: timeit("BinaryQF_reduced_representatives(-4004)")
5 loops, best of 3: 38.9 ms per loop
```



---

Comment by cremona created at 2008-08-25 10:32:29

Apply after the previous patch (ignore the first one)


---

Attachment

That is some speedup!  When I tested the same myself I noticed that during the (long) test of the old code the machine was running lisp, meaning that something was happening using maxima, which it should not.  But that is now in the past.

I have simplified the code a bit more, using xsrange() for the a and b loops, and letting b only loop from 0 (or 1) to a, adding in the form with -b if needed.  This gives another speedup factor of about 2.

This should now have a new independent review -- as far as I am concerned it is ok!  

I'll now review the other patches you made in response to my first two points.


---

Attachment

Apply after the previous two patches (ignore the first one)


---

Comment by NilsSkoruppa created at 2008-09-06 15:24:28

Changing assignee from was to NilsSkoruppa.


---

Comment by NilsSkoruppa created at 2008-09-06 15:24:28

The last patch seemed to be OK. However, I noticed that the bounds for the search region for reduced forms was not optimal. I inserted the optimal bounds and modified the loop logic accordingly, and I gained a speedup of a factor around 10.

Before:

```
sage: timeit( 'BinaryQF_reduced_representatives(-998995)')
5 loops, best of 3: 5.52 s per loop
```


After:

```
sage: timeit( 'BinaryQF_reduced_representatives(-998995)')
5 loops, best of 3: 547 ms per loop
```


Doctest runs successfully and I tested 1000 discriminants with 6 digits each, compared to the corresponding results produced by the last patch and compared number of produced forms with Hurwitz class numbers in gp. I think its OK now. Ready for being reviewed.


---

Comment by cremona created at 2008-09-06 15:44:59

Thanks for the review and great improvement (improved lower bound for b).

I applied all three patches (that is, all but the first attached to this ticket) to 3.1.2.alpha4 successfully, and all doctests in sage.quadraticforms pass.  Nils's testing vs. gp was a very good idea, so I think we can be confident of this.

I vote for this to be adopted, and hope the editor will not feel the need to get in a new reviewer (so far, each reviewer has vastly improved the previous code, but I don't think we can hope for that to happen again!)


---

Comment by mabshoff created at 2008-09-06 19:49:06

Changing assignee from NilsSkoruppa to choldsworth.


---

Comment by mabshoff created at 2008-09-06 23:50:22

Resolution: fixed


---

Comment by mabshoff created at 2008-09-06 23:50:22

Merged 3857.patch, sage-trac3857.patch and 3857-nils-1.patch in Sage 3.1.2.rc0
