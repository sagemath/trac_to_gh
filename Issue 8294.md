# Issue 8294: Copy is broken on 2x2 integer matrix (mutability is not set)

archive/issues_008294.json:
```json
{
    "body": "Assignee: h\n\nKeywords: Matrix 2x2, mutability, copy\n\n\n```\nsage: M = sage.matrix.matrix_integer_2x2.MatrixSpace_ZZ_2x2()\nsage: mat = M([3,4,5,6])\nsage: mat.is_mutable()\nTrue\nsage: mat = copy(mat)\nsage: mat.is_mutable()\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/hivert/<ipython console> in <module>()\n\n/usr/local/sage2/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.is_mutable (sage/matrix/matrix0.c:3928)()\n\nAttributeError: 'NoneType' object has no attribute 'is_mutable'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8294\n\n",
    "created_at": "2010-02-17T15:31:26Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Copy is broken on 2x2 integer matrix (mutability is not set)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8294",
    "user": "hivert"
}
```
Assignee: h

Keywords: Matrix 2x2, mutability, copy


```
sage: M = sage.matrix.matrix_integer_2x2.MatrixSpace_ZZ_2x2()
sage: mat = M([3,4,5,6])
sage: mat.is_mutable()
True
sage: mat = copy(mat)
sage: mat.is_mutable()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/hivert/<ipython console> in <module>()

/usr/local/sage2/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.is_mutable (sage/matrix/matrix0.c:3928)()

AttributeError: 'NoneType' object has no attribute 'is_mutable'
```


Issue created by migration from https://trac.sagemath.org/ticket/8294





---

archive/issue_comments_073478.json:
```json
{
    "body": "Attachment [trac_8294-matrix_2x2_copy_mutability_fix-fh.patch](tarball://root/attachments/some-uuid/ticket8294/trac_8294-matrix_2x2_copy_mutability_fix-fh.patch) by hivert created at 2010-02-17 15:41:33\n\nShould be ready for review.\n\nFlorent",
    "created_at": "2010-02-17T15:41:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8294#issuecomment-73478",
    "user": "hivert"
}
```

Attachment [trac_8294-matrix_2x2_copy_mutability_fix-fh.patch](tarball://root/attachments/some-uuid/ticket8294/trac_8294-matrix_2x2_copy_mutability_fix-fh.patch) by hivert created at 2010-02-17 15:41:33

Should be ready for review.

Florent



---

archive/issue_comments_073479.json:
```json
{
    "body": "Changing assignee from h to hivert.",
    "created_at": "2010-02-17T15:41:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8294#issuecomment-73479",
    "user": "hivert"
}
```

Changing assignee from h to hivert.



---

archive/issue_comments_073480.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-17T15:41:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8294#issuecomment-73480",
    "user": "hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073481.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-20T13:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8294#issuecomment-73481",
    "user": "mraum"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073482.json:
```json
{
    "body": "This applies cleanly and all tests pass. Positive review as is.\n#8276 will follow soon.",
    "created_at": "2010-02-20T13:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8294#issuecomment-73482",
    "user": "mraum"
}
```

This applies cleanly and all tests pass. Positive review as is.
#8276 will follow soon.



---

archive/issue_comments_073483.json:
```json
{
    "body": "Replying to [comment:3 mraum]:\n> This applies cleanly and all tests pass. Positive review as is.\n> #8276 will follow soon.\n\nThanks a lot for this quick help !",
    "created_at": "2010-02-20T13:53:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8294#issuecomment-73483",
    "user": "hivert"
}
```

Replying to [comment:3 mraum]:
> This applies cleanly and all tests pass. Positive review as is.
> #8276 will follow soon.

Thanks a lot for this quick help !



---

archive/issue_comments_073484.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-03T14:27:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8294#issuecomment-73484",
    "user": "mvngu"
}
```

Resolution: fixed
