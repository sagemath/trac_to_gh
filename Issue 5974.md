# Issue 5974: [with patch; needs review] the generic linear_combination_of_rows and linear_combination_of_columns functions for matrices are very stupidly slotch

archive/issues_005974.json:
```json
{
    "body": "Assignee: was\n\nCC:  rbeezer\n\nBehold.  By replacing about 40 confusing lines by 2 trivial lines, I get a *speedup* by more than a factor of 10!\n\n\n```\nBEFORE:\nsage: A = random_matrix(QQ,50)\nsage: v = [1..50]\nsage: timeit('A.linear_combination_of_rows(v)')\n125 loops, best of 3: 5.48 ms per loop\n\nAFTER:\nsage: A = random_matrix(QQ,50)\nsage: v = [1..50]\nsage: timeit('A.linear_combination_of_rows(v)')\n625 loops, best of 3: 503 \u00b5s per loop\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5974\n\n",
    "created_at": "2009-05-04T05:22:33Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "[with patch; needs review] the generic linear_combination_of_rows and linear_combination_of_columns functions for matrices are very stupidly slotch",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5974",
    "user": "was"
}
```
Assignee: was

CC:  rbeezer

Behold.  By replacing about 40 confusing lines by 2 trivial lines, I get a *speedup* by more than a factor of 10!


```
BEFORE:
sage: A = random_matrix(QQ,50)
sage: v = [1..50]
sage: timeit('A.linear_combination_of_rows(v)')
125 loops, best of 3: 5.48 ms per loop

AFTER:
sage: A = random_matrix(QQ,50)
sage: v = [1..50]
sage: timeit('A.linear_combination_of_rows(v)')
625 loops, best of 3: 503 µs per loop

```


Issue created by migration from https://trac.sagemath.org/ticket/5974





---

archive/issue_comments_047373.json:
```json
{
    "body": "While making sure all doctests pass for this, I uncovered the following serious bug:\n\n\n```\nsage: e = random_matrix(QQ,1,2,sparse=True); e.echelon_form().parent().is_dense()\nTrue\nsage: type(e)\n<type 'sage.matrix.matrix_rational_sparse.Matrix_rational_sparse'>\nsage: e = random_matrix(QQ,1,2,sparse=True); e.echelon_form().parent().is_dense()\nTrue\nsage: e = random_matrix(QQ,1,2,sparse=True); e.echelon_form().parent().is_dense()\nTrue\nsage: e = random_matrix(QQ,1,2,sparse=True); e.echelon_form().parent().is_dense()\nTrue\nsage: e = random_matrix(QQ,2,2,sparse=True); e.echelon_form().parent().is_dense()\nFalse\nsage: e = random_matrix(QQ,2,2,sparse=True); e.echelon_form().parent().is_dense()\nTrue\n```\n\n\nWe're getting a sparse matrix with *DENSE* parent out of echelon form for some reason.  This totally breaks my new much better implementation of linear_combination_of_rows, and would of course break all kinds of other code in random and surprising ways eventually.  \n\nThe above is all present in the default sage-3.4.2.rc0.",
    "created_at": "2009-05-04T06:00:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5974#issuecomment-47373",
    "user": "was"
}
```

While making sure all doctests pass for this, I uncovered the following serious bug:


```
sage: e = random_matrix(QQ,1,2,sparse=True); e.echelon_form().parent().is_dense()
True
sage: type(e)
<type 'sage.matrix.matrix_rational_sparse.Matrix_rational_sparse'>
sage: e = random_matrix(QQ,1,2,sparse=True); e.echelon_form().parent().is_dense()
True
sage: e = random_matrix(QQ,1,2,sparse=True); e.echelon_form().parent().is_dense()
True
sage: e = random_matrix(QQ,1,2,sparse=True); e.echelon_form().parent().is_dense()
True
sage: e = random_matrix(QQ,2,2,sparse=True); e.echelon_form().parent().is_dense()
False
sage: e = random_matrix(QQ,2,2,sparse=True); e.echelon_form().parent().is_dense()
True
```


We're getting a sparse matrix with *DENSE* parent out of echelon form for some reason.  This totally breaks my new much better implementation of linear_combination_of_rows, and would of course break all kinds of other code in random and surprising ways eventually.  

The above is all present in the default sage-3.4.2.rc0.



---

archive/issue_comments_047374.json:
```json
{
    "body": "Attachment\n\nI ran a fulldoctest cycle with this patch applied and found yet another serious bug in matrix multiplication (not caused by this patch, but uncovered by it).  E.g., in vanilla released 3.4.1, some multiplies of cyclotomic matrices just go boom!\n\n\n```\nwstein@sage:~$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: K.<zeta6>=CyclotomicField(6); matrix(K,1,2) * matrix(K,2,[0, 1, 0, -2*zeta6, 0, 0, 1, -2*zeta6 + 1])\n---------------------------------------------------------------------------\nIndexError                                Traceback (most recent call last)\n| Sage Version 3.4.1, Release Date: 2009-04-21                       |\n| Type notebook() for the GUI, and license() for information.        |\n/scratch/wstein/sage/temp/sage.math.washington.edu/15110/_scratch_wstein_sage_init_sage_0.py in <module>()\n\n/home/wstein/sage/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.Matrix.__mul__ (sage/structure/element.c:11263)()\n\n/home/wstein/sage/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:5396)()\n\n/home/wstein/sage/local/lib/python2.5/site-packages/sage/matrix/action.so in sage.matrix.action.MatrixMatrixAction._call_ (sage/matrix/action.c:2485)()\n\n/home/wstein/sage/local/lib/python2.5/site-packages/sage/matrix/matrix_cyclo_dense.so in sage.matrix.matrix_cyclo_dense.Matrix_cyclo_dense._matrix_times_matrix_ (sage/matrix/matrix_cyclo_dense.cpp:5674)()\n\n/home/wstein/sage/local/lib/python2.5/site-packages/sage/matrix/matrix_integer_dense.so in sage.matrix.matrix_integer_dense._lift_crt (sage/matrix/matrix_integer_dense.c:32188)()\n\nIndexError: list index out of range\n```\n",
    "created_at": "2009-05-04T13:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5974#issuecomment-47374",
    "user": "was"
}
```

Attachment

I ran a fulldoctest cycle with this patch applied and found yet another serious bug in matrix multiplication (not caused by this patch, but uncovered by it).  E.g., in vanilla released 3.4.1, some multiplies of cyclotomic matrices just go boom!


```
wstein@sage:~$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: K.<zeta6>=CyclotomicField(6); matrix(K,1,2) * matrix(K,2,[0, 1, 0, -2*zeta6, 0, 0, 1, -2*zeta6 + 1])
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
| Sage Version 3.4.1, Release Date: 2009-04-21                       |
| Type notebook() for the GUI, and license() for information.        |
/scratch/wstein/sage/temp/sage.math.washington.edu/15110/_scratch_wstein_sage_init_sage_0.py in <module>()

/home/wstein/sage/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.Matrix.__mul__ (sage/structure/element.c:11263)()

/home/wstein/sage/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:5396)()

/home/wstein/sage/local/lib/python2.5/site-packages/sage/matrix/action.so in sage.matrix.action.MatrixMatrixAction._call_ (sage/matrix/action.c:2485)()

/home/wstein/sage/local/lib/python2.5/site-packages/sage/matrix/matrix_cyclo_dense.so in sage.matrix.matrix_cyclo_dense.Matrix_cyclo_dense._matrix_times_matrix_ (sage/matrix/matrix_cyclo_dense.cpp:5674)()

/home/wstein/sage/local/lib/python2.5/site-packages/sage/matrix/matrix_integer_dense.so in sage.matrix.matrix_integer_dense._lift_crt (sage/matrix/matrix_integer_dense.c:32188)()

IndexError: list index out of range
```




---

archive/issue_comments_047375.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-05-04T15:15:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5974#issuecomment-47375",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_047376.json:
```json
{
    "body": "In trac_5974.patch, I like the new code better than the old and I see the speed up (not quite 10 times on my machine, but close).  However, should you raise an error if the length of v is longer than the number of rows of the matrix, the way the old code did?  With the new code, I get an error about sizes of matrices being wrong, which is a little opaque:\n\n```\nsage: A = random_matrix(QQ,50)                                                               \nsage: v = [1..52]                                                                            \nsage: A.linear_combination_of_rows(v)                                                        \n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n...\nTypeError: unsupported operand parent(s) for '*': 'Full MatrixSpace of 1 by 52 dense matrices over Integer Ring' and 'Full MatrixSpace of 50 by 50 dense matrices over Rational Field'\n```\n\nAlso, this is a little silly, but if A is a matrix with 0 rows, then `A.linear_combination_of_rows(range(3000))` works just fine.\n\nOtherwise, looks good.  All tests pass on sage.math.",
    "created_at": "2009-05-06T21:04:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5974#issuecomment-47376",
    "user": "jhpalmieri"
}
```

In trac_5974.patch, I like the new code better than the old and I see the speed up (not quite 10 times on my machine, but close).  However, should you raise an error if the length of v is longer than the number of rows of the matrix, the way the old code did?  With the new code, I get an error about sizes of matrices being wrong, which is a little opaque:

```
sage: A = random_matrix(QQ,50)                                                               
sage: v = [1..52]                                                                            
sage: A.linear_combination_of_rows(v)                                                        
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
...
TypeError: unsupported operand parent(s) for '*': 'Full MatrixSpace of 1 by 52 dense matrices over Integer Ring' and 'Full MatrixSpace of 50 by 50 dense matrices over Rational Field'
```

Also, this is a little silly, but if A is a matrix with 0 rows, then `A.linear_combination_of_rows(range(3000))` works just fine.

Otherwise, looks good.  All tests pass on sage.math.



---

archive/issue_comments_047377.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-05-07T21:18:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5974#issuecomment-47377",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_047378.json:
```json
{
    "body": "Looks good.",
    "created_at": "2009-05-07T21:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5974#issuecomment-47378",
    "user": "jhpalmieri"
}
```

Looks good.



---

archive/issue_comments_047379.json:
```json
{
    "body": "This patch causes two doctest failures for me:\n\n```\n        sage -t -long devel/sage/sage/combinat/species/series.py\n        sage -t -long devel/sage/sage/rings/padics/padic_capped_absolute_element.pyx # Segfault\n```\n\n\nThey seems to be not reproducible at the moment, but I am paranoid enough to wait and see post 4.0.a0 so I can valgrind this.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T12:07:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5974#issuecomment-47379",
    "user": "mabshoff"
}
```

This patch causes two doctest failures for me:

```
        sage -t -long devel/sage/sage/combinat/species/series.py
        sage -t -long devel/sage/sage/rings/padics/padic_capped_absolute_element.pyx # Segfault
```


They seems to be not reproducible at the moment, but I am paranoid enough to wait and see post 4.0.a0 so I can valgrind this.

Cheers,

Michael



---

archive/issue_comments_047380.json:
```json
{
    "body": "Merged in Sage 4.0.alpha0. I reran long doctests eight times and did not see any more issues. Should something lurk in here (or expose some other problem) we will catch it post 4.0.a.0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T12:41:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5974#issuecomment-47380",
    "user": "mabshoff"
}
```

Merged in Sage 4.0.alpha0. I reran long doctests eight times and did not see any more issues. Should something lurk in here (or expose some other problem) we will catch it post 4.0.a.0.

Cheers,

Michael



---

archive/issue_comments_047381.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-11T12:41:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5974#issuecomment-47381",
    "user": "mabshoff"
}
```

Resolution: fixed
