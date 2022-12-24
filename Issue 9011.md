# Issue 9011: the numpy SVD decomposition docstring is wrong

archive/issues_009011.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @mwhansen @jasongrout\n\nI decided to actually look at the numpy SVD decomposition in preparation for my class today, and quickly found that it is wrong. \n\n\n```\nsage: import numpy\nsage: numpy.linalg.svd?\n---\nDefinition: numpy.linalg.svd(a, full_matrices=1, compute_uv=1)\n\nDocstring:\n\n    Singular Value Decomposition.\n\n    Factorizes the matrix `a` into two unitary matrices, ``U`` and ``Vh``,\n    and a 1-dimensional array of singular values, ``s`` (real, non-negative),\n    such that ``a == U S Vh``, where ``S`` is the diagonal\n    matrix ``np.diag(s)``.\n----\n```\n\n\nThe statement that S is the diagonal matrix np.diag(s) is just totally false if the input matrix a is nonsquare, since S is also non square. \n\nThe best fix I could find is to replace np.diag(s) by\n\n```\nS = numpy.zeros( a )\nS[:len(s),:len(s)] = numpy.diag(s)\n```\n\n\nObviously, this should really be reported and patched upstream.\n\n  \n\nIssue created by migration from https://trac.sagemath.org/ticket/9011\n\n",
    "created_at": "2010-05-21T16:48:43Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "the numpy SVD decomposition docstring is wrong",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9011",
    "user": "@williamstein"
}
```
Assignee: jason, was

CC:  @mwhansen @jasongrout

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

  

Issue created by migration from https://trac.sagemath.org/ticket/9011





---

archive/issue_comments_083359.json:
```json
{
    "body": "In 1.4, the docstring is now\n\n\n```\nFactors the matrix `a` into ``u * np.diag(s) * v.H``, where `u` and `v`\nare unitary (i.e., ``u.H = inv(u)`` and similarly for `v`), ``.H`` is the\nconjugate transpose operator (which is the ordinary transpose for\nreal-valued matrices), and `s` is a 1-D array of `a`'s singular values.\n```\n\n\nfrom http://projects.scipy.org/numpy/browser/tags/1.4.1/numpy/linalg/linalg.py\n\n\nIs this more to your liking?  We can close this when we update NumPy to 1.4.",
    "created_at": "2010-08-26T19:41:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9011#issuecomment-83359",
    "user": "@mwhansen"
}
```

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

archive/issue_comments_083360.json:
```json
{
    "body": "This still looks wrong for a rectangular matrix, just based on the dimensions of the matrices.  The .H is an improvement, though.  I couldn't find anything any better in the NumPy docs online.\n\nu  and  v  are returned as square (by default) and `np.diag()` is going to be square, when it really needs to have the same dimensions as the original matrix.  \n\nTo wit, in Sage 4.6.2.alpha2:\n\n\n```\nsage: A = np.array([[2,0,0,0],[0,0,0,0]])\nsage: ans = np.linalg.svd(A)           \nsage: ans[0]*np.diag(ans[1])*ans[2]\nValueError                                Traceback (most recent call last)\n\n/home/sage/sage-4.6.2.alpha2/<ipython console> in <module>()\n\nValueError: shape mismatch: objects cannot be broadcast to a single shape\n```\n\n\nJason - can you send this upstream easily?\n\nRob",
    "created_at": "2011-01-29T04:20:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9011#issuecomment-83360",
    "user": "@rbeezer"
}
```

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

archive/issue_comments_083361.json:
```json
{
    "body": "Remember that multiplication of numpy arrays is *not* matrix multiplication.  Matrix multiplication is through np.dot().\n\nHere I've mirrored your example using the format in numpy docs:\n\n```\nsage: A = np.array([[2,0,0,0],[0,0,0,0]])\nsage: U,s,V=np.linalg.svd(A,full_matrices=False)\nsage: S=np.diag(s)\nsage: np.dot(U,np.dot(S,V))\narray([[ 2.,  0.,  0.,  0.],\n       [ 0.,  0.,  0.,  0.]])\n\n\n```\n\n\nNote that by default, full_matrices is True, though, so you'd have to do something like the first example in the numpy docs: http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.svd.html#numpy.linalg.svd",
    "created_at": "2011-01-29T04:37:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9011#issuecomment-83361",
    "user": "@jasongrout"
}
```

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

archive/issue_comments_083362.json:
```json
{
    "body": "Replying to [comment:3 jason]:\n> Remember that multiplication of numpy arrays is *not* matrix multiplication.  Matrix multiplication is through np.dot().\n\nYes, the stars in the `NumPy` docs caught me out.\n\n> Note that by default, full_matrices is True, though, so you'd have to do something like the first example in the numpy docs: http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.svd.html#numpy.linalg.svd\n\nBut I was on top of this.  I'd still call the factorization given initially a bit misleading, but perhaps not so bad.  Thanks for the clarifications.\n\nRob",
    "created_at": "2011-01-29T04:52:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9011#issuecomment-83362",
    "user": "@rbeezer"
}
```

Replying to [comment:3 jason]:
> Remember that multiplication of numpy arrays is *not* matrix multiplication.  Matrix multiplication is through np.dot().

Yes, the stars in the `NumPy` docs caught me out.

> Note that by default, full_matrices is True, though, so you'd have to do something like the first example in the numpy docs: http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.svd.html#numpy.linalg.svd

But I was on top of this.  I'd still call the factorization given initially a bit misleading, but perhaps not so bad.  Thanks for the clarifications.

Rob



---

archive/issue_comments_083363.json:
```json
{
    "body": "Okay, I agree the docs are misleading because full_matrices defaults to True.  I've written the numpy mailing list: http://mail.scipy.org/pipermail/numpy-discussion/2011-January/054722.html",
    "created_at": "2011-01-30T02:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9011",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9011#issuecomment-83363",
    "user": "@jasongrout"
}
```

Okay, I agree the docs are misleading because full_matrices defaults to True.  I've written the numpy mailing list: http://mail.scipy.org/pipermail/numpy-discussion/2011-January/054722.html
