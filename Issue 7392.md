# Issue 7392: RDF/CDF matrices should call scipy for rank

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-11-04 21:37:51

Assignee: was

Right now, we rely on the horrible (for floating point) generic echelon implementation to calculate the rank of an RDF/CDF matrix.

In fact, over RR, it wouldn't hurt to call numpy/scipy either.




---

Comment by jason created at 2010-03-17 05:58:46

Changing type from defect to enhancement.


---

Comment by dimpase created at 2010-08-17 17:00:09

here is an example and some thoughts:

```
sage: m=matrix(2,[1.5,1.75,1.5,1.75])
sage: m
[1.50000000000000 1.75000000000000]
[1.50000000000000 1.75000000000000]
sage: m.rank()
2
sage: 
```

This can be traced to   _echelon_in_place_classical in $SAGE_ROOT/devel/sage/sage/matrix2.pyx, which attempts to compute
row-echelon form of this matrix (basically, Gaussian elimination), and fails due to a precision loss.
 
Numerics people recommend using the QR-decomposition, (i.e. into product of an orthogonal and an upper-triangular matrices q and r) followed by inspection of r. This is apparently more stable.
For instance:

```
sage: from scipy.linalg import qr
sage: q,r=qr(m)
sage: q
array([[-0.70710678,  0.70710678],
       [ 0.70710678,  0.70710678]])
sage: r
array([[ -2.12132034e+00,  -2.47487373e+00],
       [ -0.00000000e+00,   3.96275894e-16]])
```


One then has to decide how to round entries of r to 0.0.
This would take care of RDF and the like.

Interestingly, the computation of the charpoly is more robust, and can perhaps provide an alternative (just count the powers of x it is divisible by):

```
sage: m.charpoly()
x^2 - 3.25000000000000*x
sage: 
```


Dima


---

Comment by dimpase created at 2010-08-17 17:00:09

Changing status from new to needs_work.


---

Comment by rbeezer created at 2011-02-19 07:01:55

As a precursor to computing rank, I've written a short routine to get singular values and conveniently work with deciding the cutoff for zero values.  At #10802.  I'll get to this ticket 
next.

I think a QR decomposition can be less expensive to compute, but a bit less reliable.  And I've got good advice on how to make an automated decision on "zero" entries with the SVD.


---

Comment by jason created at 2011-02-19 15:08:39

Replying to [comment:3 rbeezer]:
> As a precursor to computing rank, I've written a short routine to get singular values and conveniently work with deciding the cutoff for zero values.  At #10802.  I'll get to this ticket 
> next.
> 
> I think a QR decomposition can be less expensive to compute, but a bit less reliable.  And I've got good advice on how to make an automated decision on "zero" entries with the SVD.

That's very interesting.  Should we be submitting it upstream to scipy, where it would be used by a much wider audience than Sage?


---

Comment by leif created at 2011-10-27 01:39:49

.
