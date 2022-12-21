# Issue 943: echelon_form over ZZ (hermite form) -- add ntl as additional optional algorithm

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-10-20 11:37:43

Assignee: was

We have in Magma (64-bit linux 2.33ghz):

```

> time A := MatrixAlgebra(IntegerRing(),200)![Random(-2,2) : i in [1..200^2]];
> time d := Determinant(A);
Time: 0.140
> time H := HermiteForm(A);
Time: 0.290
```


This blows away Sage:

```
sage: a = MatrixSpace(ZZ,200).random_element(x=-2, y=2)    # -2 to 2
sage: time b=a.echelon_form()
CPU times: user 13.13 s, sys: 0.09 s, total: 13.22 s
Wall time: 13.27
sage: time b=a.det()
CPU times: user 1.81 s, sys: 0.00 s, total: 1.81 s
Wall time: 1.87
```


But NTL is better -- it's twice as fast or more:


```
            sage: a = MatrixSpace(ZZ,200).random_element(x=-2, y=2)    # -2 to 2
            sage: A = ntl.mat_ZZ(200,200)
            sage: for i in xrange(a.nrows()):
            ...     for j in xrange(a.ncols()):
            ...         A[i,j] = a[i,j]
            ...
            sage: t = cputime(); d = A.determinant()
            sage: cputime(t)
            0.33201999999999998
            sage: t = cputime(); B = A.HNF(d)
            sage: cputime(t)
            6.4924050000000006
```


So at least we should use NTL for det and/or Hermite normal form for now, and at least make it
easy to choose to use NTL. 

In the longer run we need to implement a fast multimodular algorithm.



---

Comment by was created at 2007-10-20 11:37:52

Changing type from defect to enhancement.


---

Attachment


---

Attachment

The attached patches implement the NTL wrapping. They also make echelon_form fall back gracefully if ntl.mat_ZZ.HNF fails. However in that case NTL prints "HNF: bad input" which also shows up during the doctests.


---

Comment by was created at 2007-10-20 21:42:29

I've applied this patch and it works.


---

Comment by was created at 2007-10-20 21:42:29

Resolution: fixed
