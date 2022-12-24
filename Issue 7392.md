# Issue 7392: RDF/CDF matrices should call scipy for rank

archive/issues_007392.json:
```json
{
    "body": "Assignee: @williamstein\n\nRight now, we rely on the horrible (for floating point) generic echelon implementation to calculate the rank of an RDF/CDF matrix.\n\nIn fact, over RR, it wouldn't hurt to call numpy/scipy either.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7392\n\n",
    "created_at": "2009-11-04T21:37:51Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "RDF/CDF matrices should call scipy for rank",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7392",
    "user": "@jasongrout"
}
```
Assignee: @williamstein

Right now, we rely on the horrible (for floating point) generic echelon implementation to calculate the rank of an RDF/CDF matrix.

In fact, over RR, it wouldn't hurt to call numpy/scipy either.



Issue created by migration from https://trac.sagemath.org/ticket/7392





---

archive/issue_comments_062170.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-03-17T05:58:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7392#issuecomment-62170",
    "user": "@jasongrout"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_062171.json:
```json
{
    "body": "here is an example and some thoughts:\n\n```\nsage: m=matrix(2,[1.5,1.75,1.5,1.75])\nsage: m\n[1.50000000000000 1.75000000000000]\n[1.50000000000000 1.75000000000000]\nsage: m.rank()\n2\nsage: \n```\n\nThis can be traced to   _echelon_in_place_classical in $SAGE_ROOT/devel/sage/sage/matrix2.pyx, which attempts to compute\nrow-echelon form of this matrix (basically, Gaussian elimination), and fails due to a precision loss.\n \nNumerics people recommend using the QR-decomposition, (i.e. into product of an orthogonal and an upper-triangular matrices q and r) followed by inspection of r. This is apparently more stable.\nFor instance:\n\n```\nsage: from scipy.linalg import qr\nsage: q,r=qr(m)\nsage: q\narray([[-0.70710678,  0.70710678],\n       [ 0.70710678,  0.70710678]])\nsage: r\narray([[ -2.12132034e+00,  -2.47487373e+00],\n       [ -0.00000000e+00,   3.96275894e-16]])\n```\n\n\nOne then has to decide how to round entries of r to 0.0.\nThis would take care of RDF and the like.\n\nInterestingly, the computation of the charpoly is more robust, and can perhaps provide an alternative (just count the powers of x it is divisible by):\n\n```\nsage: m.charpoly()\nx^2 - 3.25000000000000*x\nsage: \n```\n\n\nDima",
    "created_at": "2010-08-17T17:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7392#issuecomment-62171",
    "user": "@dimpase"
}
```

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

archive/issue_comments_062172.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-08-17T17:00:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7392#issuecomment-62172",
    "user": "@dimpase"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_062173.json:
```json
{
    "body": "As a precursor to computing rank, I've written a short routine to get singular values and conveniently work with deciding the cutoff for zero values.  At #10802.  I'll get to this ticket \nnext.\n\nI think a QR decomposition can be less expensive to compute, but a bit less reliable.  And I've got good advice on how to make an automated decision on \"zero\" entries with the SVD.",
    "created_at": "2011-02-19T07:01:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7392#issuecomment-62173",
    "user": "@rbeezer"
}
```

As a precursor to computing rank, I've written a short routine to get singular values and conveniently work with deciding the cutoff for zero values.  At #10802.  I'll get to this ticket 
next.

I think a QR decomposition can be less expensive to compute, but a bit less reliable.  And I've got good advice on how to make an automated decision on "zero" entries with the SVD.



---

archive/issue_comments_062174.json:
```json
{
    "body": "Replying to [comment:3 rbeezer]:\n> As a precursor to computing rank, I've written a short routine to get singular values and conveniently work with deciding the cutoff for zero values.  At #10802.  I'll get to this ticket \n> next.\n> \n> I think a QR decomposition can be less expensive to compute, but a bit less reliable.  And I've got good advice on how to make an automated decision on \"zero\" entries with the SVD.\n\nThat's very interesting.  Should we be submitting it upstream to scipy, where it would be used by a much wider audience than Sage?",
    "created_at": "2011-02-19T15:08:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7392#issuecomment-62174",
    "user": "@jasongrout"
}
```

Replying to [comment:3 rbeezer]:
> As a precursor to computing rank, I've written a short routine to get singular values and conveniently work with deciding the cutoff for zero values.  At #10802.  I'll get to this ticket 
> next.
> 
> I think a QR decomposition can be less expensive to compute, but a bit less reliable.  And I've got good advice on how to make an automated decision on "zero" entries with the SVD.

That's very interesting.  Should we be submitting it upstream to scipy, where it would be used by a much wider audience than Sage?



---

archive/issue_comments_062175.json:
```json
{
    "body": ".",
    "created_at": "2011-10-27T01:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7392#issuecomment-62175",
    "user": "@nexttime"
}
```

.
