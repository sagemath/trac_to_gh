# Issue 9011: the numpy SVD decomposition docstring is wrong

Issue created by migration from https://trac.sagemath.org/ticket/9011

Original creator: was

Original creation time: 2010-05-21 16:48:43

Assignee: jason, was

CC:  mhansen jason

I decided to actually look at the numpy SVD decomposition in preparation for my class today, and quickly found that it is wrong. 


```
sage: import numpy
sage: numpy.linalg.svd?
---
Definition: numpy.linalg.svd(a, full_matrices=1, compute_uv=1)

Docstring:

    Singular Value Decomposition.

    Factorizes the matrix `a` into two unitary matrices, ``U`` and ``Vh``,
    and a 1-dimensional array of singular values, ``s`` (real, non-negative),
    such that ``a == U S Vh``, where ``S`` is the diagonal
    matrix ``np.diag(s)``.
----
```


The statement that S is the diagonal matrix np.diag(s) is just totally false if the input matrix a is nonsquare, since S is also non square. 

The best fix I could find is to replace np.diag(s) by

```
S = numpy.zeros( a )
S[:len(s),:len(s)] = numpy.diag(s)
```


Obviously, this should really be reported and patched upstream.

  


---

Comment by mhansen created at 2010-08-26 19:41:03

In 1.4, the docstring is now


```
Factors the matrix `a` into ``u * np.diag(s) * v.H``, where `u` and `v`
are unitary (i.e., ``u.H = inv(u)`` and similarly for `v`), ``.H`` is the
conjugate transpose operator (which is the ordinary transpose for
real-valued matrices), and `s` is a 1-D array of `a`'s singular values.
```


from http://projects.scipy.org/numpy/browser/tags/1.4.1/numpy/linalg/linalg.py


Is this more to your liking?  We can close this when we update NumPy to 1.4.


---

Comment by rbeezer created at 2011-01-29 04:20:33

This still looks wrong for a rectangular matrix, just based on the dimensions of the matrices.  The .H is an improvement, though.  I couldn't find anything any better in the NumPy docs online.

u  and  v  are returned as square (by default) and `np.diag()` is going to be square, when it really needs to have the same dimensions as the original matrix.  

To wit, in Sage 4.6.2.alpha2:


```
sage: A = np.array([[2,0,0,0],[0,0,0,0]])
sage: ans = np.linalg.svd(A)           
sage: ans[0]*np.diag(ans[1])*ans[2]
ValueError                                Traceback (most recent call last)

/home/sage/sage-4.6.2.alpha2/<ipython console> in <module>()

ValueError: shape mismatch: objects cannot be broadcast to a single shape
```


Jason - can you send this upstream easily?

Rob


---

Comment by jason created at 2011-01-29 04:37:55

Remember that multiplication of numpy arrays is *not* matrix multiplication.  Matrix multiplication is through np.dot().

Here I've mirrored your example using the format in numpy docs:

```
sage: A = np.array([[2,0,0,0],[0,0,0,0]])
sage: U,s,V=np.linalg.svd(A,full_matrices=False)
sage: S=np.diag(s)
sage: np.dot(U,np.dot(S,V))
array([[ 2.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.]])


```


Note that by default, full_matrices is True, though, so you'd have to do something like the first example in the numpy docs: http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.svd.html#numpy.linalg.svd


---

Comment by rbeezer created at 2011-01-29 04:52:25

Replying to [comment:3 jason]:
> Remember that multiplication of numpy arrays is *not* matrix multiplication.  Matrix multiplication is through np.dot().

Yes, the stars in the `NumPy` docs caught me out.

> Note that by default, full_matrices is True, though, so you'd have to do something like the first example in the numpy docs: http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.svd.html#numpy.linalg.svd

But I was on top of this.  I'd still call the factorization given initially a bit misleading, but perhaps not so bad.  Thanks for the clarifications.

Rob


---

Comment by jason created at 2011-01-30 02:01:43

Okay, I agree the docs are misleading because full_matrices defaults to True.  I've written the numpy mailing list: http://mail.scipy.org/pipermail/numpy-discussion/2011-January/054722.html
