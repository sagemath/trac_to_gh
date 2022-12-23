# Issue 5716: lifting a subdivided matrix should preserve the subdivision, but doesn't.

Issue created by migration from https://trac.sagemath.org/ticket/5716

Original creator: was

Original creation time: 2009-04-08 19:18:52

Assignee: was

CC:  jason


```
sage: a = random_matrix(GF(3),4)
sage: a.subdivide(2,2)
sage: a
[2 0|0 2]
[2 1|1 0]
[---+---]
[1 2|1 0]
[1 0|0 1]
sage: a.lift()
[2 0 0 2]
[2 1 1 0]
[1 2 1 0]
[1 0 0 1]
```



---

Comment by mabshoff created at 2009-04-09 18:45:49

Is this a high priority issue? I am not convinced and since there is no patch and no sign of anyone working on fixing this I am bumping this to 3.4.2. There are also various dupes, one of which go reopened, i.e. #5715, so let's figure this out. 

Cheers,

Michael


---

Comment by jhpalmieri created at 2009-05-06 22:30:13

(I don't think this is actually a duplicate.)


---

Comment by jhpalmieri created at 2009-05-07 04:35:20

Here's a patch.  This should change things so that subdivisions are preserved when calling `mat.change_ring()`, `mat.lift()`, `mat.dense_matrix()`, and `mat.sparse_matrix()`.


---

Comment by jhpalmieri created at 2009-05-07 04:35:20

Changing status from new to assigned.


---

Comment by jhpalmieri created at 2009-05-07 04:35:20

Changing assignee from was to jhpalmieri.


---

Comment by davidloeffler created at 2009-05-29 11:03:56

This applies fine to 4.0.rc1 and all doctests in sage/matrix pass (except the known numerical-noise failure which is nothing to do with this patch). But I'm not completely happy with it, because not all of the functions where the behaviour has changed have doctests to prove it, so I'm changing this to "needs work". 

David


---

Comment by jhpalmieri created at 2009-05-29 18:48:55

Okay, here's a new patch.  I think that this tests everything, although there is at least one function (sparse_matrix, maybe) which is tested in a doctest for another (by looking at `a.dense_matrix().sparse_matrix()` or something like that).


---

Attachment


---

Comment by jason created at 2009-05-30 05:52:53

It passes doctests (and everything is tested).  Looks good to me.  Positive review.


---

Comment by mhansen created at 2009-05-31 23:47:34

Merged in 4.0.alpha0.


---

Comment by mhansen created at 2009-05-31 23:47:34

Resolution: fixed
