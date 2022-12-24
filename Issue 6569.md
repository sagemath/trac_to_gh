# Issue 6569: sparse integer matrix doesn't raise an error on non-integer index

archive/issues_006569.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @rbeezer @orlitzky\n\n\n```\n{{{\nsage: a=matrix(4,range(1,17),sparse=True)\nsage: a[[2.3],[2.1]]                     \n[0]\n}}}\n\nas compared to\n\n{{{\nsage: a=matrix(4,range(1,17))            \nsage: a[[2.3],[2.1]]         \n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/grout/.sage/temp/tiny/8143/_home_grout__sage_init_sage_0.py in <module>()\n\n/home/grout/sage/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.__getitem__ (sage/matrix/matrix0.c:4999)()\n\n/home/grout/sage/local/lib/python2.6/site-packages/sage/matrix/matrix1.so in sage.matrix.matrix1.Matrix.matrix_from_rows_and_columns (sage/matrix/matrix1.c:8613)()\n\nTypeError: 'sage.rings.real_mpfr.RealLiteral' object cannot be interpreted as an index\n}}}\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6569\n\n",
    "created_at": "2009-07-20T13:53:42Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "sparse integer matrix doesn't raise an error on non-integer index",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6569",
    "user": "@jasongrout"
}
```
Assignee: @williamstein

CC:  @rbeezer @orlitzky


```
{{{
sage: a=matrix(4,range(1,17),sparse=True)
sage: a[[2.3],[2.1]]                     
[0]
}}}

as compared to

{{{
sage: a=matrix(4,range(1,17))            
sage: a[[2.3],[2.1]]         
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/grout/.sage/temp/tiny/8143/_home_grout__sage_init_sage_0.py in <module>()

/home/grout/sage/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.__getitem__ (sage/matrix/matrix0.c:4999)()

/home/grout/sage/local/lib/python2.6/site-packages/sage/matrix/matrix1.so in sage.matrix.matrix1.Matrix.matrix_from_rows_and_columns (sage/matrix/matrix1.c:8613)()

TypeError: 'sage.rings.real_mpfr.RealLiteral' object cannot be interpreted as an index
}}}


Issue created by migration from https://trac.sagemath.org/ticket/6569





---

archive/issue_comments_053636.json:
```json
{
    "body": "Catch invalid indices in Matrix.__getitem__ and add doctests.",
    "created_at": "2012-01-22T19:36:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6569#issuecomment-53636",
    "user": "@orlitzky"
}
```

Catch invalid indices in Matrix.__getitem__ and add doctests.



---

archive/issue_comments_053637.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-01-22T19:38:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6569#issuecomment-53637",
    "user": "@orlitzky"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_053638.json:
```json
{
    "body": "Attachment [sage-trac_6569.patch](tarball://root/attachments/some-uuid/ticket6569/sage-trac_6569.patch) by @orlitzky created at 2012-01-22 19:38:14\n\nSome invalid indices weren't being caught in the general matrix[foo] accessor; the fact that non-sparse matrices failed with an error was an implementation detail.\n\nI think I've fixed them all, and doctested that sparse/dense behave the same way now.",
    "created_at": "2012-01-22T19:38:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6569#issuecomment-53638",
    "user": "@orlitzky"
}
```

Attachment [sage-trac_6569.patch](tarball://root/attachments/some-uuid/ticket6569/sage-trac_6569.patch) by @orlitzky created at 2012-01-22 19:38:14

Some invalid indices weren't being caught in the general matrix[foo] accessor; the fact that non-sparse matrices failed with an error was an implementation detail.

I think I've fixed them all, and doctested that sparse/dense behave the same way now.



---

archive/issue_comments_053639.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-01-24T19:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6569#issuecomment-53639",
    "user": "@williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_053640.json:
```json
{
    "body": "1.  I just looked at this and I'm shocked that `ind` is of type int.  This will work fine on 32-bit, but will be totally broken/buggy in subtle and surprising ways on 64-bit machines.  The type of ind should be `Py_ssize_t`, just like the type of `i`.  \nI realize that your patch does not introduce ind.  It was introduced in #4973...\n\nNobody will notice this now, because there is some sort of massive weird inefficiency in the creation of sparse matrices (maybe the parent space has its basis constructed or something idiotic like that), which makes it impossible to make a large sparse matrix, even though this should be trivial, instant, fast, and take no memory:\n\n```\nsage: time a = matrix(QQ, 2^25, sparse=True)\nTime: CPU 5.88 s, Wall: 8.46 s\nsage: get_memory_usage()   # what ?\n3908.29296875\n```\n\n\nI've made the ind and memory issue trac #12348.\n\n\n2. That said, everything in this particular patch looks great to me.  Positive review!   \n\nI hope you can address #12348 though next.  At least the trivial change of ind to `Py_ssize_t`.",
    "created_at": "2012-01-24T19:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6569#issuecomment-53640",
    "user": "@williamstein"
}
```

1.  I just looked at this and I'm shocked that `ind` is of type int.  This will work fine on 32-bit, but will be totally broken/buggy in subtle and surprising ways on 64-bit machines.  The type of ind should be `Py_ssize_t`, just like the type of `i`.  
I realize that your patch does not introduce ind.  It was introduced in #4973...

Nobody will notice this now, because there is some sort of massive weird inefficiency in the creation of sparse matrices (maybe the parent space has its basis constructed or something idiotic like that), which makes it impossible to make a large sparse matrix, even though this should be trivial, instant, fast, and take no memory:

```
sage: time a = matrix(QQ, 2^25, sparse=True)
Time: CPU 5.88 s, Wall: 8.46 s
sage: get_memory_usage()   # what ?
3908.29296875
```


I've made the ind and memory issue trac #12348.


2. That said, everything in this particular patch looks great to me.  Positive review!   

I hope you can address #12348 though next.  At least the trivial change of ind to `Py_ssize_t`.



---

archive/issue_comments_053641.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-02-02T12:52:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6569#issuecomment-53641",
    "user": "@jdemeyer"
}
```

Resolution: fixed
