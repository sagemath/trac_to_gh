# Issue 5408: Matrix kernel with PARI algorithm passes wrong type

archive/issues_005408.json:
```json
{
    "body": "Assignee: rbeezer\n\nKeywords: kernel, PARI\n\nUsing the PARI kernel algorithm returns a PARI object which is unpacked as a list with the rows given as tuples.  When this is passed to hermite_form() the object is not of the right type.\n\n\n```\nsage: a = matrix(ZZ, [[1,2],[2,4]])\nsage: a.kernel(algorithm='pari')\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/rob/.sage/temp/wave/8545/_home_rob__sage_init_sage_0.py in <module>()\n\n/opt/sage-3.3/local/lib/python2.5/site-packages/sage/matrix/matrix_integer_dense.so in sage.matrix.matrix_integer_dense.Matrix_integer_dense.kernel (sage/matrix/matrix_integer_dense.c:16256)()\n\nAttributeError: 'list' object has no attribute 'hermite_form'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5408\n\n",
    "created_at": "2009-03-01T06:26:56Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "Matrix kernel with PARI algorithm passes wrong type",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5408",
    "user": "rbeezer"
}
```
Assignee: rbeezer

Keywords: kernel, PARI

Using the PARI kernel algorithm returns a PARI object which is unpacked as a list with the rows given as tuples.  When this is passed to hermite_form() the object is not of the right type.


```
sage: a = matrix(ZZ, [[1,2],[2,4]])
sage: a.kernel(algorithm='pari')
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/rob/.sage/temp/wave/8545/_home_rob__sage_init_sage_0.py in <module>()

/opt/sage-3.3/local/lib/python2.5/site-packages/sage/matrix/matrix_integer_dense.so in sage.matrix.matrix_integer_dense.Matrix_integer_dense.kernel (sage/matrix/matrix_integer_dense.c:16256)()

AttributeError: 'list' object has no attribute 'hermite_form'
```


Issue created by migration from https://trac.sagemath.org/ticket/5408





---

archive/issue_comments_041800.json:
```json
{
    "body": "Attachment [trac_5408_pari_kernel_matrix.patch](tarball://root/attachments/some-uuid/ticket5408/trac_5408_pari_kernel_matrix.patch) by rbeezer created at 2009-03-01 23:50:38",
    "created_at": "2009-03-01T23:50:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5408#issuecomment-41800",
    "user": "rbeezer"
}
```

Attachment [trac_5408_pari_kernel_matrix.patch](tarball://root/attachments/some-uuid/ticket5408/trac_5408_pari_kernel_matrix.patch) by rbeezer created at 2009-03-01 23:50:38



---

archive/issue_comments_041801.json:
```json
{
    "body": "Replying to [comment:1 rbeezer]:\n\nmatrix_dense_integer._kernel_gens_using_pari() now returns a matrix, when it previously returned a list of tuples, which always caused the calling routine (kernel_matrix) to choke.  Two comments:\n\n1.  I may change the name of this routine as part of http://trac.sagemath.org/sage_trac/ticket/5381\n\n2.  I've tried to be careful about sending back an empty matrix with the right dimensions when the matrix has full rank.  I suspect there are other places that could use changes like this.\n\nApply this patch before http://trac.sagemath.org/sage_trac/ticket/5381",
    "created_at": "2009-03-01T23:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5408#issuecomment-41801",
    "user": "rbeezer"
}
```

Replying to [comment:1 rbeezer]:

matrix_dense_integer._kernel_gens_using_pari() now returns a matrix, when it previously returned a list of tuples, which always caused the calling routine (kernel_matrix) to choke.  Two comments:

1.  I may change the name of this routine as part of http://trac.sagemath.org/sage_trac/ticket/5381

2.  I've tried to be careful about sending back an empty matrix with the right dimensions when the matrix has full rank.  I suspect there are other places that could use changes like this.

Apply this patch before http://trac.sagemath.org/sage_trac/ticket/5381



---

archive/issue_comments_041802.json:
```json
{
    "body": "Review: Looks good, applies ok to 3.4.alpha0 and tests in sage/matrix (plus a whole lot of other random kernel tests I did) pass fine.",
    "created_at": "2009-03-07T17:05:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5408#issuecomment-41802",
    "user": "cremona"
}
```

Review: Looks good, applies ok to 3.4.alpha0 and tests in sage/matrix (plus a whole lot of other random kernel tests I did) pass fine.



---

archive/issue_comments_041803.json:
```json
{
    "body": "Merged in Sage 3.4.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-08T06:16:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5408#issuecomment-41803",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.rc1.

Cheers,

Michael



---

archive/issue_comments_041804.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-08T06:16:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5408",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5408#issuecomment-41804",
    "user": "mabshoff"
}
```

Resolution: fixed
