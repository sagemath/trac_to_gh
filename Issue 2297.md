# Issue 2297: Tensor product of matrices [with patch, needs review]

Issue created by migration from https://trac.sagemath.org/ticket/2297

Original creator: SimonKing

Original creation time: 2008-02-24 20:48:15

Assignee: SimonKing

Keywords: tensor product

I was missing a tensor product for matrices in Sage. While this is easy to obtain using `block_matrix`, it might be nicer to customize this as a method of `Matrix`. Example:


```
sage: M1=Matrix(QQ,[[-1,0],[-1/2,-1]])
sage: M2=Matrix(ZZ,[[1,-1,2],[-2,4,8]])
sage: M1.tensor_product(M2)

[  -1    1   -2|   0    0    0]
[   2   -4   -8|   0    0    0]
[--------------+--------------]
[-1/2  1/2   -1|  -1    1   -2]
[   1   -2   -4|   2   -4   -8]
sage: M2.tensor_product(M1)

[  -1    0|   1    0|  -2    0]
[-1/2   -1| 1/2    1|  -1   -2]
[---------+---------+---------]
[   2    0|  -4    0|  -8    0]
[   1    2|  -2   -4|  -4   -8]
```




---

Attachment


---

Comment by SimonKing created at 2008-02-24 21:11:46

Changing component from algebraic geometry to linear algebra.


---

Comment by mhansen created at 2008-02-24 21:52:07

Hmm... I personally think that this should be called kronecker_product.


---

Comment by SimonKing created at 2008-02-25 08:53:55

Replying to [comment:2 mhansen]:
> Hmm... I personally think that this should be called kronecker_product.

I wouldn't mind to call it like that. However, note that the corresponding function for Singular matrices is called tensor:

```
sage: R=singular.ring(0,'(x,y)','dp')
sage: C=singular.matrix(2,2,'1,-1,0, 2')
sage: D=singular.matrix(3,3,'0,0,-x, 0,y,0, x*y,0,0')
sage: C.tensor(D)

0,  0,-x,0,    0,  x,
0,  y,0, 0,    -y, 0,
x*y,0,0, -x*y, 0,  0,
0,  0,0, 0,    0,  -2*x,
0,  0,0, 0,    2*y,0,
0,  0,0, 2*x*y,0,  0
```

The implementation of the Kronecker product is part of a plot to define tensor products for free modules over polynomial rings (this is what i needed, originally).


---

Comment by AlexGhitza created at 2008-02-26 04:53:56

I've played around with it and I think it looks good.  The name "tensor product" is just as common as "Kronecker product" for this.  (Actually, it's also a much better name than Kronecker product because it says where the operation is coming from).  If there is popular demand for this, we could have another method kronecker_product() that just calls this.

Anyway, I say merge, and I'm eager to see the rest of the tensor product stuff.


---

Comment by mabshoff created at 2008-02-26 05:07:05

Merged in Sage 2.10.3.alpha0


---

Comment by mabshoff created at 2008-02-26 05:07:05

Resolution: fixed
