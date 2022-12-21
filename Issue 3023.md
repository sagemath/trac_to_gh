# Issue 3023: make apply_map deal with empty matrices

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-04-25 16:47:26

Assignee: was


```
sage: m=matrix([])
sage: m.apply_map?
sage: m.apply_map(lambda x: x)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/grout/sage/devel/sage-main/sage/matrix/<ipython console> in <module>()

/home/grout/sage/devel/sage-main/sage/matrix/matrix_dense.pyx in sage.matrix.matrix_dense.Matrix_dense.apply_map (sage/matrix/matrix_dense.c:3098)()
    307             v = sage.structure.sequence.Sequence(v)
    308             R = v.universe()
--> 309         M = sage.matrix.matrix_space.MatrixSpace(R, self._nrows,
    310                    self._ncols, sparse=False)
    311         image = M(v)

/home/grout/sage/local/lib/python2.5/site-packages/sage/matrix/matrix_space.py in MatrixSpace(base_ring, nrows, ncols, sparse)
    171     """
    172     if not sage.rings.ring.is_Ring(base_ring):
--> 173         raise TypeError, "base_ring (=%s) must be a ring"%base_ring
    174
    175     if ncols is None: ncols = nrows

<type 'exceptions.TypeError'>: base_ring (=Category of objects) must be a ring
```


m.apply_map(blah) should return an empty matrix in this case.


---

Attachment

doctests in the matrix/ directory pass with the above patch.


---

Comment by mabshoff created at 2008-04-25 18:51:38


```
[19:04] <mabshoff> so, what is the verdict on #3023?
[19:04] <jason> positive review from me :)  I don't think that counts, though
[19:05] <mabshoff> Well, as author it is expected that you think your patch it a good idea.
[19:05] <mabshoff> It seems like the sensible thing to do.
[19:07] <dfdeshom> running testall now, but positive review from me
[19:08] <dfdeshom> (and i'll put it in writing when the tests finish)
```



---

Comment by mabshoff created at 2008-04-25 18:52:45

Resolution: fixed


---

Comment by mabshoff created at 2008-04-25 18:52:45

Merged in Sage 3.0.1.alpha0
