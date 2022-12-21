# Issue 1323: generate all subspaces of a vector space/projective space

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-11-28 20:18:47

Assignee: was

CC:  mhansen

From Chris Godsil's wishlist:


```
>>> Sometimes I want to construct graphs whose vertices are subspaces of a
>>> vector space over a finite field. It could be useful to have a
>>> generator for
>>> the lines of the associated projective space, or even subspaces of a given
>>> dimension.
>> Is there an easy way to generate all of the subspaces of a vector space
>> already in Sage, maybe restricted to a particular dimension, from the
>> original vector space?
> Maybe make a ticket for this?
```




---

Comment by rlm created at 2008-09-25 23:07:40

Here is a method for iterating over dimension `k` subspaces of a space of dimension `n`:

First, suppose that `F` is a finite field, and our ambient vector space is just `F^n`.

Any subspace of dimension `k` is uniquely described as the rowspace of a `k x n` matrix in reduced row echelon form. This is determined by which columns are pivots, and what the entries of the remaining positions are. Thus it suffices to iterate over `k`-subsets of `[0..n-1]`, declaring those to be the pivots. Certain entries must be zero, according to row-reduced form, and the rest can be arbitrary elements of `F`.

Thus, for each `k`-subset of `[0..n-1]`, call it `[j_1, ..., j_k]`, construct a matrix with pivots as described by the `j_i`. For the `m` entries that are nonzero, construct a vector space of dimension `m`, and iterate over it, using the resulting tuples to fill in the matrix.

Voila!

I don't know about projective space, though.


---

Comment by rlm created at 2008-09-25 23:09:35

Oh wait, to get projective space, just shift the dimension by one, duh...


---

Comment by rlm created at 2008-10-16 13:14:00

Changing status from new to assigned.


---

Comment by rlm created at 2008-10-16 13:14:00

Changing assignee from was to rlm.


---

Attachment


---

Comment by wdj created at 2008-10-17 17:31:46

Applies cleanly and passes sage -testall. Looks good. 
GAP has this very useful function and now Sage does. 
Thanks Robert!


---

Comment by mabshoff created at 2008-10-18 20:30:33

Resolution: fixed


---

Comment by mabshoff created at 2008-10-18 20:30:33

Merged in Sage 3.2.alpha0
