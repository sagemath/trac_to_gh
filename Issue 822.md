# Issue 822: Some matrix multiplications inefficiencies

archive/issues_000822.json:
```json
{
    "body": "Assignee: somebody\n\nI've observed an errant base_extend call on matrix multiplies and also some unnecessary calls out to the python parent class.  The attached patch fixes both of these.  An example is below:\n\n\n```\nsage: M=MatrixSpace(ZZ,3,3)\nsage: m=M([range(9)])\nsage: n=M([range(1,10)])\nsage: prun m*n\n\u00a0 \u00a0 \u00a0 \u00a0 \u00a020 function calls in 0.000 CPU seconds\n\u00a0 \u00a0Ordered by: internal time\n\u00a0 \u00a0ncalls \u00a0tottime \u00a0percall \u00a0cumtime \u00a0percall filename:lineno(function)\n\u00a0 \u00a0 \u00a0 \u00a0 1 \u00a0 \u00a00.000 \u00a0 \u00a00.000 \u00a0 \u00a00.000 \u00a0 \u00a00.000 <string>:1(<module>)\n\u00a0 \u00a0 \u00a0 \u00a0 2 \u00a0 \u00a00.000 \u00a0 \u00a00.000 \u00a0 \u00a00.000 \u00a0 \u00a00.000 matrix_space.py:105(MatrixSpace)\n\u00a0 \u00a0 \u00a0 \u00a0 1 \u00a0 \u00a00.000 \u00a0 \u00a00.000 \u00a0 \u00a00.000 \u00a0 \u00a00.000 matrix_space.py:282(change_ring)\n\u00a0 \u00a0 \u00a0 \u00a0 1 \u00a0 \u00a00.000 \u00a0 \u00a00.000 \u00a0 \u00a00.000 \u00a0 \u00a00.000 matrix_space.py:306(base_extend)\n\u00a0 \u00a0 \u00a0 \u00a0 1 \u00a0 \u00a00.000 \u00a0 \u00a00.000 \u00a0 \u00a00.000 \u00a0 \u00a00.000 matrix_space.py:648\n(matrix_space)\n\u00a0 \u00a0 \u00a0 \u00a0 3 \u00a0 \u00a00.000 \u00a0 \u00a00.000 \u00a0 \u00a00.000 \u00a0 \u00a00.000 matrix_space.py:670(ncols)\n\u00a0 \u00a0 \u00a0 \u00a0 3 \u00a0 \u00a00.000 \u00a0 \u00a00.000 \u00a0 \u00a00.000 \u00a0 \u00a00.000 matrix_space.py:681(nrows)\n...\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/822\n\n",
    "created_at": "2007-10-04T09:51:37Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.6",
    "title": "Some matrix multiplications inefficiencies",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/822",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```
Assignee: somebody

I've observed an errant base_extend call on matrix multiplies and also some unnecessary calls out to the python parent class.  The attached patch fixes both of these.  An example is below:


```
sage: M=MatrixSpace(ZZ,3,3)
sage: m=M([range(9)])
sage: n=M([range(1,10)])
sage: prun m*n
         20 function calls in 0.000 CPU seconds
   Ordered by: internal time
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        2    0.000    0.000    0.000    0.000 matrix_space.py:105(MatrixSpace)
        1    0.000    0.000    0.000    0.000 matrix_space.py:282(change_ring)
        1    0.000    0.000    0.000    0.000 matrix_space.py:306(base_extend)
        1    0.000    0.000    0.000    0.000 matrix_space.py:648
(matrix_space)
        3    0.000    0.000    0.000    0.000 matrix_space.py:670(ncols)
        3    0.000    0.000    0.000    0.000 matrix_space.py:681(nrows)
...
```


Issue created by migration from https://trac.sagemath.org/ticket/822





---

archive/issue_comments_005081.json:
```json
{
    "body": "Attachment [matrix_coercion.hg](tarball://root/attachments/some-uuid/ticket822/matrix_coercion.hg) by jbmohler created at 2007-10-04 09:52:34\n\nmatrix multiplication optimization",
    "created_at": "2007-10-04T09:52:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/822#issuecomment-5081",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Attachment [matrix_coercion.hg](tarball://root/attachments/some-uuid/ticket822/matrix_coercion.hg) by jbmohler created at 2007-10-04 09:52:34

matrix multiplication optimization



---

archive/issue_comments_005082.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-04T17:57:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/822#issuecomment-5082",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_005083.json:
```json
{
    "body": "This looks very good to me!",
    "created_at": "2007-10-04T17:57:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/822#issuecomment-5083",
    "user": "https://github.com/williamstein"
}
```

This looks very good to me!
