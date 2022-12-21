# Issue 2028: Cannot iterate over SymbolicArithmetic objects like you can with poly rings / Eigenspaces() broken for matrices over SR

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-02-02 03:57:59

Assignee: was

The matrix eigenspaces() function is broken for rings over SR since the algorithm iterates over factors of the characteristic polynomial. "for e,f in mat.charpoly().factor()" works for matrices over polynomial rings, but not over the symbolic ring.  This is also brought up in #2021.

Data:


```
sage: a=matrix(SR,[[1,2],[3,4]])
sage: b=matrix(QQ,[[1,2],[3,4]])
sage: [i for i in a.fcp()]
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/grout/sage/devel/sage-main/sage/matrix/<ipython console> in <module>()

<type 'exceptions.TypeError'>: 'SymbolicArithmetic' object is not iterable
sage: [i for i in b.fcp()]
[(x^2 - 5*x - 2, 1)]
```


and 


```
sage: a=matrix(SR,[[1,2],[3,4]])
sage: [i for i in a.fcp().factor_list()]
[(x^2 - 5*x - 2, 1)]
```


So apparently we need to somehow call factor_list() when we have a symbolic matrix or we need to change SymbolicArithmetic? to iterate through factor_list() when we ask for an iterator.  I don't know which is better.  Comments?



---

Comment by was created at 2008-02-02 06:22:58

We could (re-)define fcp for symbolic matrices to call factor_list instead of factor,
and use the factor_list to construct a usual Factorization object.


---

Comment by mhansen created at 2008-02-02 07:07:35

Changing status from new to assigned.


---

Comment by mhansen created at 2008-02-02 07:07:35

Changing assignee from was to mhansen.


---

Attachment

this replaces 2028.patch; it's rebased against 2.10.1.rc4 since 2028.patch fails to apply.


---

Comment by was created at 2008-02-02 09:47:59

This patch fails when the exponents in factorizations aren't 1.  See below. 


```
sage: matrix(ZZ, 5, [1..5^2]).fcp()
x^3 * (x^2 - 65*x - 250)
sage: matrix(SR, 5, [1..5^2]).fcp()
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/was/build/sage-2.10.1.rc4/<ipython console> in <module>()

/Users/was/build/sage-2.10.1.rc4/matrix_symbolic_dense.pyx in sage.matrix.matrix_symbolic_dense.Matrix_symbolic_dense.fcp()

/Users/was/build/sage-2.10.1.rc4/local/lib/python2.5/site-packages/sage/structure/factorization.py in __init__(self, x, unit, cr, sort, simplify)
    101         for t in x:
    102             if not (isinstance(t, tuple) and len(t) == 2 and isinstance(t[1],(int, long, Integer))):
--> 103                 raise TypeError, "x must be a list of tuples of length 2"
    104         list.__init__(self, x)
    105         if unit is None:

<type 'exceptions.TypeError'>: x must be a list of tuples of length 2
```



---

Attachment


---

Comment by mhansen created at 2008-02-03 04:16:46

I posted a new patch (to be applied second) which fixes the issue was reported.


---

Comment by ncalexan created at 2008-02-15 05:00:25

I really don't think Factorization should not about SymbolicConstant at all.

Also, the doctests don't actually test a repeated factor, which would test the second set of failures.

So this should not be applied yet, if at all.


---

Comment by jason created at 2008-02-16 11:15:19

ncalexan, can you clarify what you mean by "I really don't think Factorization should not about SymbolicConstant? at all."?


---

Comment by jason created at 2008-02-18 19:34:28

I think ncalexan meant to say "I really don't think Factorization should know about SymbolicConstant at all." (correct me if I'm wrong).

It appears that Factorization objects should be given a list of factors where the second element of each tuple is an integer.  Making it take SymbolicConstant objects is expanding that definition to include rationals and other sage.functions.constant.Constant objects.  Does this break other stuff?  Do we want Factorization objects to take rational numbers?  So to be on the safe side, I agree with ncalexan that Factorization should not be extended to know about SymbolicConstant objects.  It would probably be enough to try to coerce the argument to an integer.  I'll post up a patch that does that (and makes the error message also mention something about the constraint on the second item).


---

Comment by jason created at 2008-02-18 20:00:06

So apparently this was only part of the problem: the eigenspaces algorithm also does field extensions, etc., all of which break when using symbolic stuff.  I think symbolic matrices should be treated completely differently and should yield results as in Mathematica and Maple, which would mean a different eigenspaces function than the one inherited from matrix2.pyx.


---

Comment by jason created at 2008-02-18 21:21:50

Okay, I'm convinced that merging the symbolic matrix stuff and the general algorithms in matrix2.pyx is a bad idea.  I'm closing this ticket as invalid and opening another two tickets with a few choice tidbits from mhansen's patches above.

If someone doesn't agree, feel free to open it back up or email to have a discussion on sage-devel or something.


---

Comment by jason created at 2008-02-18 21:22:59

Resolution: invalid
