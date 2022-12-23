# Issue 5184: nonzero_positions is broken for sparse vectors

Issue created by migration from https://trac.sagemath.org/ticket/5184

Original creator: jhpalmieri

Original creation time: 2009-02-05 03:07:15

Assignee: was

Here is an illustration:

```
sage: v = vector({1: 1, 3: -1})
sage: w = vector({1: -1, 3: 0})
sage: v
(0, 1, 0, -1)
sage: w
(0, -1, 0, 0)
sage: v+w
(0, 0, 0, -1)
sage: (v+w).nonzero_positions()
[1, 3]
```

(I don't think this is related to #4648.  nonzero_positions for sums of sparse matrices seems to behave well in the one example I tried.)




---

Comment by jhpalmieri created at 2009-02-05 03:12:29

Changing priority from minor to major.


---

Comment by jhpalmieri created at 2009-02-05 03:12:29

Maybe this is related:

```
sage: v = vector({1: 1, 3: -1})
sage: w = vector({1: -1, 3: 1})
sage: v+w
(0, 0, 0, 0)
sage: (v+w).is_zero()
False
```



---

Comment by jhpalmieri created at 2009-02-05 04:07:56

No, they're not related.  I'm putting the "is_zero" issue into #5185.  This ticket should only deal with nonzero_positions.


---

Comment by jhpalmieri created at 2009-02-17 21:14:39

Changing status from new to assigned.


---

Comment by jhpalmieri created at 2009-02-17 21:14:39

Changing assignee from was to jhpalmieri.


---

Comment by jhpalmieri created at 2009-02-17 21:14:39

Here's a patch.  This doesn't actually change `nonzero_positions` (except for adding a doctest); instead it changes addition, subtraction, and scalar multiplication for sparse free module elements so that these only keep nonzero dictionary entries.


---

Attachment

Instead of tests like `if a != 0:`, it should use `if a:`.   The code is a little uglier and harder to understand, but it's much faster; these are approximations of the sorts of timing differences you would see:

```
sage: foo = QQbar(3)
sage: timeit('bool(foo)')
625 loops, best of 3: 1.24 µs per loop
sage: timeit('foo != 0r')
625 loops, best of 3: 100 µs per loop
sage: foo = 3
sage: timeit('bool(foo)')
625 loops, best of 3: 286 ns per loop
sage: timeit('foo != 0r')
625 loops, best of 3: 4.2 µs per loop
```


(Also, in the places where you deleted "A dense a sparse", is it worth adding a note that says something like "(This is true even if one is sparse and the other is dense.)"?)


---

Comment by jhpalmieri created at 2009-02-21 17:24:10

only apply this one


---

Attachment

I changed the tests from `a != 0` to `a`, and I put in a comment about sparse vs. dense -- actually, I put it in twice.  I had to rebase the patch, also (and it will probably have to be rebased after the ReST changes, too...).


---

Comment by jhpalmieri created at 2009-02-25 23:57:56

rebased against 3.4.alpha0; apply only this patch


---

Attachment

Here's a new patch, rebased against 3.4.alpha0.


---

Comment by cwitty created at 2009-02-26 00:40:31

Code looks good, doctests pass.  Positive review.  (Apply only 5184-rebased.patch .)


---

Comment by mabshoff created at 2009-02-28 21:02:39

Resolution: fixed


---

Comment by mabshoff created at 2009-02-28 21:02:39

Merged 5184-rebased.patch in Sage 3.4.rc0.

Cheers,

Michael
