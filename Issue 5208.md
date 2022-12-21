# Issue 5208: Differing behavior for matrix left_kernel vs. right_kernel

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2009-02-08 19:34:30

Assignee: rbeezer

Keywords: matrix, left_kernel, right_kernel

Calls to left_kernel() don't properly filter down the class hierarchy for matrices, and so do not always use the most efficient algorithm available.  The transcript below illustrates the difference in time for a mathematically equivalent computation on a random 200 x 200 matrix of two-digit integers.


```
sage: a = random_matrix(ZZ, 200, 200, x=100).change_ring(QQ)

sage: time a.transpose().right_kernel()

Vector space of degree 200 and dimension 0 over Rational Field
Basis matrix:
0 x 200 dense matrix over Rational Field
Time: CPU 0.18 s, Wall: 0.18 s

sage: time a.left_kernel()

Vector space of degree 200 and dimension 0 over Rational Field
Basis matrix:
0 x 200 dense matrix over Rational Field
CPU time: 70.76 s,  Wall time: 71.55 s
```



---

Attachment

High-level code has been renamed from left_kernel() to simply kernel() to maintain consistency with derived classes.  So kernel() is no longer an alias for left_kernel().

right_kernel() is mostly unchanged, calls kernel() on transpose.

left_kernel() now just calls kernel().  This should all ensure the proper versions of kernel() in derived classes are reached.

Doctests for kernel() and left_kernel() are identical except for names used in explanations and the actual calls.  Doctests for right_kernel now have "right" in explantions, otherwise unchanged.

Each of the three versions has a doctest with a symmetric 500 x 500 matrix of rational entries, which requires about 3 seconds of overhead and 1 second for the actual kernel call when patched.  Unpatched version 3.2.3 will take 589 seconds for left_kernel() on this example.  Runtimes seem to be O(n-cubed) if a smaller (faster) example is better.

Timings on patched versions suggest that for rational matrices, the overhead in right_kernel() of transposing the matrix twice has the effect of doubling the runtime versus left_kernel.


---

Comment by mabshoff created at 2009-02-08 23:04:41

Given the large improvement this ought to be in 3.3.

Cheers,

Michael


---

Comment by mhansen created at 2009-02-08 23:18:47

Looks good to me.

One little thing which doesn't matter too much:


```
if K is not None:
```


is a bit easier to read than


```
if not K is None:
```



---

Comment by rbeezer created at 2009-02-09 00:49:10

Replying to [comment:3 mhansen]:

I agree that the orginal phrasing is awkward to read the first time you see it.  But it's lots of places, in the matrix code it occurs this way whenever the cache is queried.  Across all of the source, grep gives me 627 instances of "is None", with 606 of those being "is not None"

Should we engage the battle here with these three instances?  ;-)  I'd be happy to add another patch (though I'm not sure how to mark the title).

> Looks good to me.
> 
> One little thing which doesn't matter too much:
> 
> {{{
> if K is not None:
> }}}
> 
> is a bit easier to read than
> 
> {{{
> if not K is None:
> }}}


---

Comment by rbeezer created at 2009-02-09 01:55:07

Now that I think about it, I'll be adding code to create alternative bases, and will need to mess with caching the varying results, so maybe I'll just pick up these changes as part of that.  Especially since I'll be looking further down the hierarchy.  And maybe I've got my counts confused above, as well.  Anyway, I'll implement this suggestion later.  Thanks.


---

Comment by mabshoff created at 2009-02-09 07:39:04

This patch needs a rebase:

```
mabshoff`@`sage:/scratch/mabshoff/sage-3.3.rc0/devel/sage$ patch -p1 < trac_5208_kernels.patch 
patching file sage/matrix/matrix2.pyx
Hunk #1 succeeded at 1420 with fuzz 2.
Hunk #2 FAILED at 1503.
Hunk #3 succeeded at 1593 (offset 19 lines).
Hunk #4 succeeded at 1621 (offset 19 lines).
Hunk #5 succeeded at 1640 (offset 19 lines).
Hunk #6 succeeded at 1650 (offset 19 lines).
Hunk #7 succeeded at 1669 (offset 19 lines).
```


Cheers,

Michael


---

Comment by mabshoff created at 2009-02-09 07:43:58

This is a rebase version of Rob's patch. The problem was trivial since only doctests had been added to the docstring


---

Attachment

trac_5208_kernels.2.patch is a rebased version of Rob's patch.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-09 07:54:40

Resolution: fixed


---

Comment by mabshoff created at 2009-02-09 07:54:40

Merged trac_5208_kernels.2.patch in Sage 3.3.rc0.

Cheers,

Michael
