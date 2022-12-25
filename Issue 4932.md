# Issue 4932: Remove solve_left_LU for matrix_double_dense, which was totally broken forever (?)

archive/issues_004932.json:
```json
{
    "body": "Assignee: @jasongrout\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4932\n\n",
    "closed_at": "2015-02-24T00:39:27Z",
    "created_at": "2009-01-03T06:25:33Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.6",
    "title": "Remove solve_left_LU for matrix_double_dense, which was totally broken forever (?)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4932",
    "user": "https://github.com/williamstein"
}
```
Assignee: @jasongrout



Issue created by migration from https://trac.sagemath.org/ticket/4932





---

archive/issue_comments_037341.json:
```json
{
    "body": "Yep, it looks like this might have happened in the transition to numpy and probably was my fault.  Here are errors:\n\n```\nsage: A = matrix(RDF, 3,3, [1,2,5,7.6,2.3,1,1,2,-1]); A\n\n[ 1.0  2.0  5.0]\n[ 7.6  2.3  1.0]\n[ 1.0  2.0 -1.0]\nsage: b = vector(RDF,[1,2,3])\nsage: A.solve_left(b)       \n(-0.113695090439, 1.39018087855, -0.333333333333)\nsage: A.solve_left_LU(b)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/grout/<ipython console> in <module>()\n\n/home/grout/sage/local/lib/python2.5/site-packages/sage/matrix/matrix_double_dense.so in sage.matrix.matrix_double_dense.Matrix_double_dense.solve_left_LU (sage/matrix/matrix_double_dense.c:4930)()\n\nTypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'\nsage: A.LU()\n\n([0.0 1.0 0.0]\n[1.0 0.0 0.0]\n[0.0 0.0 1.0],\n [           1.0            0.0            0.0]\n[0.131578947368            1.0            0.0]\n[0.131578947368            1.0            1.0],\n [          7.6           2.3           1.0]\n[          0.0 1.69736842105 4.86842105263]\n[          0.0           0.0          -6.0])\nsage: A.solve_left_LU(b)\ntoo many axes: 2 (effrank=2), expected rank=1\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (981, 0))\n\n---------------------------------------------------------------------------\nerror                                     Traceback (most recent call last)\n\n/home/grout/<ipython console> in <module>()\n\n/home/grout/sage/local/lib/python2.5/site-packages/sage/matrix/matrix_double_dense.so in sage.matrix.matrix_double_dense.Matrix_double_dense.solve_left_LU (sage/matrix/matrix_double_dense.c:4995)()\n\n/home/grout/sage/local/lib/python2.5/site-packages/scipy/linalg/basic.pyc in lu_solve((lu, piv), b, trans, overwrite_b)\n     48         raise ValueError, \"incompatible dimensions.\"\n     49     getrs, = get_lapack_funcs(('getrs',),(lu,b1))\n---> 50     x,info = getrs(lu,piv,b1,trans=trans,overwrite_b=overwrite_b)\n     51     if info==0:\n     52         return x\n\nerror: failed in converting 2nd argument `piv' of clapack.dgetrs to C/Fortran array\n```\n\nThe first error comes from the code not computing LU before using the cached LU decomposition.  The second error apparently comes from a mistake in calling scipy.",
    "created_at": "2009-01-03T08:08:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4932#issuecomment-37341",
    "user": "https://github.com/jasongrout"
}
```

Yep, it looks like this might have happened in the transition to numpy and probably was my fault.  Here are errors:

```
sage: A = matrix(RDF, 3,3, [1,2,5,7.6,2.3,1,1,2,-1]); A

[ 1.0  2.0  5.0]
[ 7.6  2.3  1.0]
[ 1.0  2.0 -1.0]
sage: b = vector(RDF,[1,2,3])
sage: A.solve_left(b)       
(-0.113695090439, 1.39018087855, -0.333333333333)
sage: A.solve_left_LU(b)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/grout/<ipython console> in <module>()

/home/grout/sage/local/lib/python2.5/site-packages/sage/matrix/matrix_double_dense.so in sage.matrix.matrix_double_dense.Matrix_double_dense.solve_left_LU (sage/matrix/matrix_double_dense.c:4930)()

TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'
sage: A.LU()

([0.0 1.0 0.0]
[1.0 0.0 0.0]
[0.0 0.0 1.0],
 [           1.0            0.0            0.0]
[0.131578947368            1.0            0.0]
[0.131578947368            1.0            1.0],
 [          7.6           2.3           1.0]
[          0.0 1.69736842105 4.86842105263]
[          0.0           0.0          -6.0])
sage: A.solve_left_LU(b)
too many axes: 2 (effrank=2), expected rank=1
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (981, 0))

---------------------------------------------------------------------------
error                                     Traceback (most recent call last)

/home/grout/<ipython console> in <module>()

/home/grout/sage/local/lib/python2.5/site-packages/sage/matrix/matrix_double_dense.so in sage.matrix.matrix_double_dense.Matrix_double_dense.solve_left_LU (sage/matrix/matrix_double_dense.c:4995)()

/home/grout/sage/local/lib/python2.5/site-packages/scipy/linalg/basic.pyc in lu_solve((lu, piv), b, trans, overwrite_b)
     48         raise ValueError, "incompatible dimensions."
     49     getrs, = get_lapack_funcs(('getrs',),(lu,b1))
---> 50     x,info = getrs(lu,piv,b1,trans=trans,overwrite_b=overwrite_b)
     51     if info==0:
     52         return x

error: failed in converting 2nd argument `piv' of clapack.dgetrs to C/Fortran array
```

The first error comes from the code not computing LU before using the cached LU decomposition.  The second error apparently comes from a mistake in calling scipy.



---

archive/issue_comments_037342.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-03T08:08:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4932#issuecomment-37342",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to assigned.



---

archive/issue_comments_037343.json:
```json
{
    "body": "Changing assignee from @williamstein to @jasongrout.",
    "created_at": "2009-01-03T08:08:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4932#issuecomment-37343",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @williamstein to @jasongrout.



---

archive/issue_comments_037344.json:
```json
{
    "body": "Okay, apparently lu_factor and lu in the scipy library return two completely different things.\n\nSome notes from some experimentation:\n\n1. scipy.linalg.lu is usually significantly slower than scipy.linalg.lu_factor\n\n2. scipy.linalg.lu_factor returns a much more compact answer\n\n3. scipy.linalg.lu_factor returns an answer directly suitable for lu_solve, etc.\n\nI say we cache the lu_factor results and then build the P,L,U from these results if needed.\n\nThe strictly lower triangular part of the returned matrix is the L, the upper triangular part is the U, so that the returned matrix is (L-identity)+U.\n\nThe pivot array gives the row swaps needed.  For example, the following code constructs the new order of rows based on the pivot array piv:\n\n```\narr=range(size)\nfor i in range(size):\n    arr[i],arr[piv[i]] = arr[piv[i]],arr[i]\n```\n\nThe P matrix will then have a 1 in the (i,arr[i]) position (or the (arr[i],i) position...).\n\nTHE LU MATRIX RETURNED FROM lu_factor MIGHT BE TRANSPOSED!  It was in my case, for some reason.",
    "created_at": "2009-01-03T10:17:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4932#issuecomment-37344",
    "user": "https://github.com/jasongrout"
}
```

Okay, apparently lu_factor and lu in the scipy library return two completely different things.

Some notes from some experimentation:

1. scipy.linalg.lu is usually significantly slower than scipy.linalg.lu_factor

2. scipy.linalg.lu_factor returns a much more compact answer

3. scipy.linalg.lu_factor returns an answer directly suitable for lu_solve, etc.

I say we cache the lu_factor results and then build the P,L,U from these results if needed.

The strictly lower triangular part of the returned matrix is the L, the upper triangular part is the U, so that the returned matrix is (L-identity)+U.

The pivot array gives the row swaps needed.  For example, the following code constructs the new order of rows based on the pivot array piv:

```
arr=range(size)
for i in range(size):
    arr[i],arr[piv[i]] = arr[piv[i]],arr[i]
```

The P matrix will then have a 1 in the (i,arr[i]) position (or the (arr[i],i) position...).

THE LU MATRIX RETURNED FROM lu_factor MIGHT BE TRANSPOSED!  It was in my case, for some reason.



---

archive/issue_comments_037345.json:
```json
{
    "body": "However, the results from lu_factor also appear to give spurious answers, while the results from lu seem more correct numerically...",
    "created_at": "2009-01-03T10:19:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4932#issuecomment-37345",
    "user": "https://github.com/jasongrout"
}
```

However, the results from lu_factor also appear to give spurious answers, while the results from lu seem more correct numerically...



---

archive/issue_comments_037346.json:
```json
{
    "body": "Replying to [comment:4 jason]:\n> However, the results from lu_factor also appear to give spurious answers, while the results from lu seem more correct numerically...\n\n\nnever mind; it seems like that comment is not true; I get the same spurious answers from lu()",
    "created_at": "2009-01-03T10:20:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4932#issuecomment-37346",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:4 jason]:
> However, the results from lu_factor also appear to give spurious answers, while the results from lu seem more correct numerically...


never mind; it seems like that comment is not true; I get the same spurious answers from lu()



---

archive/issue_events_011353.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-04T19:39:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4932#event-11353"
}
```



---

archive/issue_comments_037347.json:
```json
{
    "body": "Better luck in 3.3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-04T19:39:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4932#issuecomment-37347",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Better luck in 3.3.

Cheers,

Michael



---

archive/issue_events_011354.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-06T22:58:48Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4932#event-11354"
}
```



---

archive/issue_events_011355.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-06T22:58:48Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4932#event-11355"
}
```



---

archive/issue_comments_037348.json:
```json
{
    "body": "3.4 is for ReST tickets only.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-06T22:58:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4932#issuecomment-37348",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

3.4 is for ReST tickets only.

Cheers,

Michael



---

archive/issue_comments_037349.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2009-12-21T15:05:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4932#issuecomment-37349",
    "user": "https://trac.sagemath.org/admin/accounts/users/dagss"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_037350.json:
```json
{
    "body": "I'm thinking of fixing this ticket as soon as I've got time for it.\n\nAt any rate, one piece of opinion:\n\n- `solve_left_LU` should be removed (the current NotImplementedError has served as deprecation for over a year)\n- `solve_left` should, for numerical types, take an `algorithm` argument to switch between different numerical methods for solving, where LU is one of them. `solve_left` should \n- By default, `solve_left` should use some iterative steps to ensure an error below a given treshold (and, say, fall back to QR etc.).\n\nIn addition, numerical matrices should have a `set_solve_algorithm` method. It is often known in the outer, calling code what kind of numerical algorithm is needed to solve a system, while some inner code might want to perform the actual call to `solve_left`. I.e. what algorithms perform well for a matrix is typically a property of the given matrix.",
    "created_at": "2009-12-21T15:05:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4932#issuecomment-37350",
    "user": "https://trac.sagemath.org/admin/accounts/users/dagss"
}
```

I'm thinking of fixing this ticket as soon as I've got time for it.

At any rate, one piece of opinion:

- `solve_left_LU` should be removed (the current NotImplementedError has served as deprecation for over a year)
- `solve_left` should, for numerical types, take an `algorithm` argument to switch between different numerical methods for solving, where LU is one of them. `solve_left` should 
- By default, `solve_left` should use some iterative steps to ensure an error below a given treshold (and, say, fall back to QR etc.).

In addition, numerical matrices should have a `set_solve_algorithm` method. It is often known in the outer, calling code what kind of numerical algorithm is needed to solve a system, while some inner code might want to perform the actual call to `solve_left`. I.e. what algorithms perform well for a matrix is typically a property of the given matrix.



---

archive/issue_comments_037351.json:
```json
{
    "body": "It appears \"straight\" LU decomposition in `SciPy/NumPy` will accept non-square matrices as input, while the LU-factor routine still requires square input.\n\nDo we want to try to support non-square systems with the straight LU decomposition?  It would mean foregoing the built-in solve routine that extens the LU-factor decomposition, and possibly a decision would have to be made about what to cache:  square (very compact) or non-square (more general).",
    "created_at": "2011-02-19T07:12:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4932#issuecomment-37351",
    "user": "https://github.com/rbeezer"
}
```

It appears "straight" LU decomposition in `SciPy/NumPy` will accept non-square matrices as input, while the LU-factor routine still requires square input.

Do we want to try to support non-square systems with the straight LU decomposition?  It would mean foregoing the built-in solve routine that extens the LU-factor decomposition, and possibly a decision would have to be made about what to cache:  square (very compact) or non-square (more general).



---

archive/issue_comments_037352.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2011-02-19T07:12:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4932#issuecomment-37352",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_037353.json:
```json
{
    "body": "According to:\n\nhttp://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.solve.html#numpy.linalg.solve\n\nThe generic \"solve\" from `NumPy` uses LU decomposition anyway, via an LAPACK routine.\n\nSo it does not appear to me that `solve_left_LU` adds anything to `solve_left`?",
    "created_at": "2011-02-24T05:40:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4932#issuecomment-37353",
    "user": "https://github.com/rbeezer"
}
```

According to:

http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.solve.html#numpy.linalg.solve

The generic "solve" from `NumPy` uses LU decomposition anyway, via an LAPACK routine.

So it does not appear to me that `solve_left_LU` adds anything to `solve_left`?



---

archive/issue_comments_037354.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-02-24T22:46:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4932#issuecomment-37354",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_037355.json:
```json
{
    "body": "Attachment [trac_4932-remove-solve-left-LU.patch](tarball://root/attachments/some-uuid/ticket4932/trac_4932-remove-solve-left-LU.patch) by @rbeezer created at 2011-02-24 22:46:37\n\nThis routine needs lots of work, has been \"Not Implemented\" for a long time, and with two routines for solving systems available (#7852), this should be removed.  Patch does just that.",
    "created_at": "2011-02-24T22:46:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4932#issuecomment-37355",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_4932-remove-solve-left-LU.patch](tarball://root/attachments/some-uuid/ticket4932/trac_4932-remove-solve-left-LU.patch) by @rbeezer created at 2011-02-24 22:46:37

This routine needs lots of work, has been "Not Implemented" for a long time, and with two routines for solving systems available (#7852), this should be removed.  Patch does just that.



---

archive/issue_comments_037356.json:
```json
{
    "body": "Replying to [comment:10 rbeezer]:\n> According to:\n> \n> http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.solve.html#numpy.linalg.solve\n> \n> The generic \"solve\" from `NumPy` uses LU decomposition anyway, via an LAPACK routine.\n> \n> So it does not appear to me that `solve_left_LU` adds anything to `solve_left`?\n\n\nThe point behind this patch is that the LU decomposition is cached in the matrix so that multiple solves using this matrix are much faster because you don't have to compute the LU decomposition each time.",
    "created_at": "2011-02-24T23:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4932#issuecomment-37356",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:10 rbeezer]:
> According to:
> 
> http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.solve.html#numpy.linalg.solve
> 
> The generic "solve" from `NumPy` uses LU decomposition anyway, via an LAPACK routine.
> 
> So it does not appear to me that `solve_left_LU` adds anything to `solve_left`?


The point behind this patch is that the LU decomposition is cached in the matrix so that multiple solves using this matrix are much faster because you don't have to compute the LU decomposition each time.



---

archive/issue_comments_037357.json:
```json
{
    "body": "(I mean, the point behind this function...)",
    "created_at": "2011-02-24T23:39:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4932#issuecomment-37357",
    "user": "https://github.com/jasongrout"
}
```

(I mean, the point behind this function...)



---

archive/issue_comments_037358.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2011-02-25T05:16:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4932#issuecomment-37358",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_037359.json:
```json
{
    "body": "OK, that makes sense, I was reading the code, not the doc string.  Three ideas:\n\n* Probably should be `solve_right`.\n\n* How about a more descriptive name, like `solve_right_precomputed`?\n\n* LU decomposition now works for rectangular matrices (#10839).  I'd think it would make the most sense to cache the \"LU factor\" matrix just for this purpose.  That's the *square* matrix where L and U share space and the diagonal 1's are not present.",
    "created_at": "2011-02-25T05:16:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4932#issuecomment-37359",
    "user": "https://github.com/rbeezer"
}
```

OK, that makes sense, I was reading the code, not the doc string.  Three ideas:

* Probably should be `solve_right`.

* How about a more descriptive name, like `solve_right_precomputed`?

* LU decomposition now works for rectangular matrices (#10839).  I'd think it would make the most sense to cache the "LU factor" matrix just for this purpose.  That's the *square* matrix where L and U share space and the diagonal 1's are not present.



---

archive/issue_events_011356.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4932#event-11356"
}
```



---

archive/issue_events_011357.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4932#event-11357"
}
```



---

archive/issue_events_011358.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4932#event-11358"
}
```



---

archive/issue_events_011359.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4932#event-11359"
}
```



---

archive/issue_events_011360.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4932#event-11360"
}
```



---

archive/issue_events_011361.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4932#event-11361"
}
```



---

archive/issue_events_011362.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4932#event-11362"
}
```



---

archive/issue_events_011363.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4932#event-11363"
}
```



---

archive/issue_comments_037360.json:
```json
{
    "body": "New commits:",
    "created_at": "2015-02-23T11:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4932#issuecomment-37360",
    "user": "https://github.com/jdemeyer"
}
```

New commits:



---

archive/issue_comments_037361.json:
```json
{
    "body": "Changing status from needs_info to positive_review.",
    "created_at": "2015-02-23T11:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4932#issuecomment-37361",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_info to positive_review.



---

archive/issue_events_011364.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2015-02-23T11:13:34Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4932#event-11364"
}
```



---

archive/issue_events_011365.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2015-02-23T11:13:34Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "milestone": "sage-6.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4932#event-11365"
}
```



---

archive/issue_events_011366.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-02-24T00:39:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4932#event-11366"
}
```



---

archive/issue_comments_037362.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-02-24T00:39:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4932#issuecomment-37362",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
