# Issue 2028: Cannot iterate over SymbolicArithmetic objects like you can with poly rings / Eigenspaces() broken for matrices over SR

archive/issues_002028.json:
```json
{
    "body": "Assignee: was\n\nThe matrix eigenspaces() function is broken for rings over SR since the algorithm iterates over factors of the characteristic polynomial. \"for e,f in mat.charpoly().factor()\" works for matrices over polynomial rings, but not over the symbolic ring.  This is also brought up in #2021.\n\nData:\n\n\n```\nsage: a=matrix(SR,[[1,2],[3,4]])\nsage: b=matrix(QQ,[[1,2],[3,4]])\nsage: [i for i in a.fcp()]\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/home/grout/sage/devel/sage-main/sage/matrix/<ipython console> in <module>()\n\n<type 'exceptions.TypeError'>: 'SymbolicArithmetic' object is not iterable\nsage: [i for i in b.fcp()]\n[(x^2 - 5*x - 2, 1)]\n```\n\n\nand \n\n\n```\nsage: a=matrix(SR,[[1,2],[3,4]])\nsage: [i for i in a.fcp().factor_list()]\n[(x^2 - 5*x - 2, 1)]\n```\n\n\nSo apparently we need to somehow call factor_list() when we have a symbolic matrix or we need to change SymbolicArithmetic? to iterate through factor_list() when we ask for an iterator.  I don't know which is better.  Comments?\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2028\n\n",
    "created_at": "2008-02-02T03:57:59Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "Cannot iterate over SymbolicArithmetic objects like you can with poly rings / Eigenspaces() broken for matrices over SR",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2028",
    "user": "jason"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/2028





---

archive/issue_comments_013117.json:
```json
{
    "body": "We could (re-)define fcp for symbolic matrices to call factor_list instead of factor,\nand use the factor_list to construct a usual Factorization object.",
    "created_at": "2008-02-02T06:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2028#issuecomment-13117",
    "user": "was"
}
```

We could (re-)define fcp for symbolic matrices to call factor_list instead of factor,
and use the factor_list to construct a usual Factorization object.



---

archive/issue_comments_013118.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-02T07:07:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2028#issuecomment-13118",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_013119.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2008-02-02T07:07:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2028#issuecomment-13119",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_013120.json:
```json
{
    "body": "Attachment\n\nthis replaces 2028.patch; it's rebased against 2.10.1.rc4 since 2028.patch fails to apply.",
    "created_at": "2008-02-02T09:45:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2028#issuecomment-13120",
    "user": "was"
}
```

Attachment

this replaces 2028.patch; it's rebased against 2.10.1.rc4 since 2028.patch fails to apply.



---

archive/issue_comments_013121.json:
```json
{
    "body": "This patch fails when the exponents in factorizations aren't 1.  See below. \n\n\n```\nsage: matrix(ZZ, 5, [1..5^2]).fcp()\nx^3 * (x^2 - 65*x - 250)\nsage: matrix(SR, 5, [1..5^2]).fcp()\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/Users/was/build/sage-2.10.1.rc4/<ipython console> in <module>()\n\n/Users/was/build/sage-2.10.1.rc4/matrix_symbolic_dense.pyx in sage.matrix.matrix_symbolic_dense.Matrix_symbolic_dense.fcp()\n\n/Users/was/build/sage-2.10.1.rc4/local/lib/python2.5/site-packages/sage/structure/factorization.py in __init__(self, x, unit, cr, sort, simplify)\n    101         for t in x:\n    102             if not (isinstance(t, tuple) and len(t) == 2 and isinstance(t[1],(int, long, Integer))):\n--> 103                 raise TypeError, \"x must be a list of tuples of length 2\"\n    104         list.__init__(self, x)\n    105         if unit is None:\n\n<type 'exceptions.TypeError'>: x must be a list of tuples of length 2\n```\n",
    "created_at": "2008-02-02T09:47:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2028#issuecomment-13121",
    "user": "was"
}
```

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

archive/issue_comments_013122.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-03T04:15:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2028#issuecomment-13122",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_013123.json:
```json
{
    "body": "I posted a new patch (to be applied second) which fixes the issue was reported.",
    "created_at": "2008-02-03T04:16:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2028#issuecomment-13123",
    "user": "mhansen"
}
```

I posted a new patch (to be applied second) which fixes the issue was reported.



---

archive/issue_comments_013124.json:
```json
{
    "body": "I really don't think Factorization should not about SymbolicConstant at all.\n\nAlso, the doctests don't actually test a repeated factor, which would test the second set of failures.\n\nSo this should not be applied yet, if at all.",
    "created_at": "2008-02-15T05:00:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2028#issuecomment-13124",
    "user": "ncalexan"
}
```

I really don't think Factorization should not about SymbolicConstant at all.

Also, the doctests don't actually test a repeated factor, which would test the second set of failures.

So this should not be applied yet, if at all.



---

archive/issue_comments_013125.json:
```json
{
    "body": "ncalexan, can you clarify what you mean by \"I really don't think Factorization should not about SymbolicConstant? at all.\"?",
    "created_at": "2008-02-16T11:15:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2028#issuecomment-13125",
    "user": "jason"
}
```

ncalexan, can you clarify what you mean by "I really don't think Factorization should not about SymbolicConstant? at all."?



---

archive/issue_comments_013126.json:
```json
{
    "body": "I think ncalexan meant to say \"I really don't think Factorization should know about SymbolicConstant at all.\" (correct me if I'm wrong).\n\nIt appears that Factorization objects should be given a list of factors where the second element of each tuple is an integer.  Making it take SymbolicConstant objects is expanding that definition to include rationals and other sage.functions.constant.Constant objects.  Does this break other stuff?  Do we want Factorization objects to take rational numbers?  So to be on the safe side, I agree with ncalexan that Factorization should not be extended to know about SymbolicConstant objects.  It would probably be enough to try to coerce the argument to an integer.  I'll post up a patch that does that (and makes the error message also mention something about the constraint on the second item).",
    "created_at": "2008-02-18T19:34:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2028#issuecomment-13126",
    "user": "jason"
}
```

I think ncalexan meant to say "I really don't think Factorization should know about SymbolicConstant at all." (correct me if I'm wrong).

It appears that Factorization objects should be given a list of factors where the second element of each tuple is an integer.  Making it take SymbolicConstant objects is expanding that definition to include rationals and other sage.functions.constant.Constant objects.  Does this break other stuff?  Do we want Factorization objects to take rational numbers?  So to be on the safe side, I agree with ncalexan that Factorization should not be extended to know about SymbolicConstant objects.  It would probably be enough to try to coerce the argument to an integer.  I'll post up a patch that does that (and makes the error message also mention something about the constraint on the second item).



---

archive/issue_comments_013127.json:
```json
{
    "body": "So apparently this was only part of the problem: the eigenspaces algorithm also does field extensions, etc., all of which break when using symbolic stuff.  I think symbolic matrices should be treated completely differently and should yield results as in Mathematica and Maple, which would mean a different eigenspaces function than the one inherited from matrix2.pyx.",
    "created_at": "2008-02-18T20:00:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2028#issuecomment-13127",
    "user": "jason"
}
```

So apparently this was only part of the problem: the eigenspaces algorithm also does field extensions, etc., all of which break when using symbolic stuff.  I think symbolic matrices should be treated completely differently and should yield results as in Mathematica and Maple, which would mean a different eigenspaces function than the one inherited from matrix2.pyx.



---

archive/issue_comments_013128.json:
```json
{
    "body": "Okay, I'm convinced that merging the symbolic matrix stuff and the general algorithms in matrix2.pyx is a bad idea.  I'm closing this ticket as invalid and opening another two tickets with a few choice tidbits from mhansen's patches above.\n\nIf someone doesn't agree, feel free to open it back up or email to have a discussion on sage-devel or something.",
    "created_at": "2008-02-18T21:21:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2028#issuecomment-13128",
    "user": "jason"
}
```

Okay, I'm convinced that merging the symbolic matrix stuff and the general algorithms in matrix2.pyx is a bad idea.  I'm closing this ticket as invalid and opening another two tickets with a few choice tidbits from mhansen's patches above.

If someone doesn't agree, feel free to open it back up or email to have a discussion on sage-devel or something.



---

archive/issue_comments_013129.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-02-18T21:22:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2028",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2028#issuecomment-13129",
    "user": "jason"
}
```

Resolution: invalid
