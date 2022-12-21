# Issue 4648: sparse linear algebra: nonzero_positions is slow

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2008-11-29 00:54:49

Assignee: boothby

Keywords: sparse

Currently, generic sparse matrices inherit their nonzero_positions method from matrix0.py.  This should be trivial to fix.


```
def nonzero_positions(self):
    return self._entries.keys()
```



---

Attachment


---

Comment by rlm created at 2009-01-23 13:35:17

Not quite so trivial as two lines, but...


---

Comment by craigcitro created at 2009-01-24 12:02:27

Code looks good. Merge!

However, I think that the fact that all three versions of this code are nearly identical means that a new enhancement ticket should be opened to clean up the classes here. In particular, I think the following might be a reasonable plan:

 * in `matrix_integer_sparse`, rename `_matrix` to `_rows` for consistency (and clarity -- you're getting a list of rows, not a pointer to the whole matrix)
 * clean up the associated vector classes (in fact, `vector_modn_sparse` isn't even a class right now!), and have them all inherit from an abstract class with the same methods they all share (which could all raise `NotImplementedError`s, for all that matters)
 * make each of the sparse matrix classes have a member `_rows` of type `vector_sparse_generic` or whatever, and then move the `_nonzero_positions_by_row` down to the generic class.

It would get rid of this code duplication, clean things up, etc.


---

Comment by mabshoff created at 2009-01-24 19:55:05

Merged in Sage 3.3.alpha2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 19:55:05

Resolution: fixed
