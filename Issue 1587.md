# Issue 1587: M.kernel() gives the kernel when M acts on row vectors from the right.

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2007-12-22 13:06:38

Assignee: was

CC:  alexghitza jason

Keywords: matrix, kernel


```
sage: M = matrix([[1,2,3],[1,2,4],[2,4,7]])
sage: M.kernel()

Free module of degree 3 and rank 1 over Integer Ring
Echelon basis matrix:
[ 1  1 -1]
sage: v = vector([1, 1, -1])
sage: M*v
(0, -1, -1)
sage: v*M
(0, 0, 0)
```


This is not what most people expect.  Either the behavior should be changed so that it gives the kernel when acting on columns from the left or some documentation should make the current behavior very clear.


---

Comment by mhansen created at 2007-12-22 13:08:32

Changing priority from major to minor.


---

Comment by was created at 2007-12-27 04:01:18


```
On Dec 26, 2007 7:35 PM, Marshall Hampton <> wrote:
>
> At least in the United States, and I assume some other places as well,
> matrices are usually considered to act from the left.  So the kernel
> of a matrix A would be the set of vectors x such that Ax = 0.  In
> sage, the kernel is given for the matrix acting from the right, i.e.
> the set of vectors y such that yA  = 0.  If there is compelling
> argument as to why that makes sense, I can live with it.

There are 2 or 3 reasons why things are as they are with matrix
actions on vectors in Sage.

1. In Sage vectors are row vectors:
sage: v = vector([1,2,3])
sage: v
(1, 2, 3)              # <-- that's a row

Matrices act naturally from the right on row vectors.

Nonetheless, we now allow both actions in Sage for convenience:

sage: A = random_matrix(QQ,3)
sage: A*v
(5, -4, 3)
sage: v*A
(6, 3/2, -1)

2. David Kohel and I made the decision about which side matrices would act on
when I started Sage, i.e., back when Sage was called "Software for Arithmetic
Geometry Experimentation", and the main goal of Sage was to provide a viable
open source alternative to the subset of Magma that David Kohel and I used, and
to do so in a way that made it as easy as possible to port our code from Magma,
and to go back and forth between Sage and Magma.
In Magma matrices act from the right, probably because vectors are row vectors
and also because Magma is Australian.

3. At some point I was about to change everything to matrices acting from the
left, and David Kohel stopped me.

I don't know if that is a compelling enough reason.   A fourth reason is that
changing things now would be really really really hard, and would likely
introduce numerous bugs all over the place.

A Magma example:
-----

sage: A = random_matrix(QQ,3)
sage: v = vector([1,2,3])
sage: v*A
(9, 4, 3/2)
sage: A*v
(-5, 2, 15/2)
sage: aa = magma(A)
sage: vv = magma('VectorSpace(RationalField(),3)![1,2,3]')   # trac
1605 -- I'm on it.
sage: vv*aa
(  9   4 3/2)
sage: aa*vv
... (boom!)
<type 'exceptions.TypeError'>: Error evaluation Magma code.
IN:_sage_[7] := _sage_[4] * _sage_[5];
OUT:
>> _sage_[7] := _sage_[4] * _sage_[5];
                         ^
Runtime error in '*': Arguments are not compatible
Argument types given: AlgMatElt[FldRat], ModTupFldElt[FldRat]


> But the
> documentation for kernel() obscures, rather than clarifies, this
> issue:
>
> Docstring:
>
>     Return the kernel of x.
>
>     EXAMPLES:
>         sage: M = MatrixSpace(QQ,3,3)
>         sage: A = M([1,2,3,4,5,6,7,8,9])
>         sage: kernel(A)
>         Vector space of degree 3 and dimension 1 over Rational Field
>         Basis matrix:
>         [ 1 -2  1]
>
> The problem with this example is that A is quite an unusual matrix:
> its left-kernel is equal to its right-kernel.  I recommend that a non-
> square example be given that makes the current behavior clearer.

Good idea.  Please create a trac ticket, then put in some examples.
You'll modify the file
   sage/matrix/matrix_rational_dense.pyx
Please put in a bunch (i.e., maybe 4 or 5) of examples to illustrate all
kinds of things, including edge cases (0 by n or n by 0 matrices,
denominators, etc.).

```



---

Comment by mabshoff created at 2008-10-11 12:21:13

I believe this has been fixes by introducing the right and left kernel. 

Alex: If you agree please close the ticket.

Cheers,

Michael


---

Comment by AlexGhitza created at 2008-10-11 12:30:18

Yes, this is in much better shape now, thanks to #2542.

(And I get to close a ticket, how exciting! :)


---

Comment by AlexGhitza created at 2008-10-11 12:30:18

Resolution: fixed


---

Comment by mhansen created at 2008-11-30 20:30:44

Resolution changed from fixed to 


---

Comment by mhansen created at 2008-11-30 20:30:44

Changing status from closed to reopened.


---

Comment by mhansen created at 2008-11-30 20:30:44

The documentation for kernel? is still wrong.


---

Comment by jason created at 2008-12-13 16:52:51

If it's all right, wstein, I'd like to make this part of my linear algebra overhaul over Christmas break, so I'm accepting this ticket.


---

Comment by jason created at 2008-12-13 16:52:51

Changing assignee from was to jason.


---

Comment by jason created at 2008-12-13 16:52:51

Changing status from reopened to new.


---

Comment by jhpalmieri created at 2009-01-18 06:34:27

If you're doing a linear algebra overhaul, please see ticket #5009 for another left/right issue, and see #5001 for another kernel issue.


---

Comment by SimonKing created at 2009-01-23 21:32:51

Adds documentation to the kernel-function and to the kernel-method of rational dense matrices


---

Attachment

I added some words and some examples (including corner cases) to the function `kernel` in `sage/misc/functional.py` and to the `kernel` method in `sage/matrix/matrix_rational_dense.py`. 

Since the examples of the `kernel` method for dense integer matrices and for sparse matrices are clear enough, I believe that my patch suffices to clearify the documentation of `kernel`.


---

Comment by jhpalmieri created at 2009-01-24 15:55:13

Looks good to me.


---

Comment by mabshoff created at 2009-01-25 02:20:24

Merged in Sage 3.3.alpha2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-25 02:20:24

Resolution: fixed
