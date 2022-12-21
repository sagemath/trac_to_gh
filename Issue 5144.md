# Issue 5144: [with patch, needs review] speed up right_nullity for matrices

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-01-31 01:13:24

Assignee: was

CC:  jason

Keywords: right_nullity

left_nullity currently functions by computing the difference between self.nrows() and self.rank().

right_nullity currently functions by calling left_nullity on the transpose of the matrix, and so it can be sped up if it instead computes self.ncols() - self.rank().  The attached patch does this.

To see the effect, try timing some things with

```
sage: m = random_matrix(ZZ, 50, x=2^16)
```

On my machine, I get

```
sage: timeit('m.left_nullity()')
625 loops, best of 3: 2.29 µs per loop
timeit('m.transpose()')
125 loops, best of 3: 1.72 ms per loop
```

so the transpose operation is really slow.


---

Attachment


---

Comment by jason created at 2009-02-06 18:04:32

Good catch!  The patch looks good and doctests pass in matrix2.pyx.  Positive review.


---

Comment by mabshoff created at 2009-02-06 22:28:31

Resolution: fixed


---

Comment by mabshoff created at 2009-02-06 22:28:31

Merged in Sage 3.3.alpha6.

Cheers,

Michael
