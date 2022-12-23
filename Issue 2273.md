# Issue 2273: matrix exponentials

Issue created by migration from https://trac.sagemath.org/ticket/2273

Original creator: AlexGhitza

Original creation time: 2008-02-23 01:46:16

Assignee: was

CC:  jason

Right now, thanks to #2049, we can (have Maxima) compute the exponential of a symbolic matrix:


```
sage: var('t')
sage: A = Matrix(SR, [[t, 0], [0, t]])
sage: A.exp()
[e^t   0]
[  0 e^t]
```


This is great, but it would also be nice to have this for numerical matrices.  On a related note, the following is perplexing (to me):


```
sage: A=Matrix(RDF,[[1,-2],[2,-1]])
sage: exp(A)
...
<type 'exceptions.TypeError'>: cannot coerce type '<type 'sage.matrix.matrix_real_double_dense.Matrix_real_double_dense'>' into a SymbolicExpression.
sage: exp(1.0*A)
...
<type 'exceptions.TypeError'>: cannot coerce type '<type 'sage.matrix.matrix_real_double_dense.Matrix_real_double_dense'>' into a SymbolicExpression.
sage: exp(pi/(3*sqrt(3))*A)
[ 1 -1]
[ 1  0]
```


Yes folks, the last one works (and gives the right answer, btw).  Weird.



---

Comment by pdenapo created at 2008-02-28 20:19:14

Now that we have the Jordan canonical form (#874) we could use it to compute the matrix exponential.


---

Comment by pdenapo created at 2008-03-20 14:55:17

For implementing this using the Jordan canonical form, being able to compute that canonical form is not enough, we would need to compute the Jordan basis as well (see #2615)


---

Comment by jason created at 2008-12-07 04:51:43

Changing status from new to assigned.


---

Comment by jason created at 2008-12-07 04:51:43

#4733 implements this, though it could be done better, maybe, with the Jordan form code.


---

Comment by jason created at 2008-12-07 04:51:43

Changing assignee from was to jason.


---

Comment by mabshoff created at 2008-12-07 04:57:28

I agree that this is a duplicate of #4733 and since there is a patch there I am closing this as a dupe.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-07 04:57:28

Resolution: duplicate
