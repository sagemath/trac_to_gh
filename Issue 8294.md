# Issue 8294: Copy is broken on 2x2 integer matrix (mutability is not set)

archive/issues_008294.json:
```json
{
    "body": "Assignee: h\n\nKeywords: Matrix 2x2, mutability, copy\n\n```\nsage: M = sage.matrix.matrix_integer_2x2.MatrixSpace_ZZ_2x2()\nsage: mat = M([3,4,5,6])\nsage: mat.is_mutable()\nTrue\nsage: mat = copy(mat)\nsage: mat.is_mutable()\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/hivert/<ipython console> in <module>()\n\n/usr/local/sage2/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.is_mutable (sage/matrix/matrix0.c:3928)()\n\nAttributeError: 'NoneType' object has no attribute 'is_mutable'\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/8294\n\n",
    "created_at": "2010-02-17T15:31:26Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Copy is broken on 2x2 integer matrix (mutability is not set)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8294",
    "user": "https://github.com/hivert"
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

archive/issue_comments_073355.json:
```json
{
    "body": "Attachment [trac_8294-matrix_2x2_copy_mutability_fix-fh.patch](tarball://root/attachments/some-uuid/ticket8294/trac_8294-matrix_2x2_copy_mutability_fix-fh.patch) by @hivert created at 2010-02-17 15:41:33\n\nShould be ready for review.\n\nFlorent",
    "created_at": "2010-02-17T15:41:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8294#issuecomment-73355",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8294-matrix_2x2_copy_mutability_fix-fh.patch](tarball://root/attachments/some-uuid/ticket8294/trac_8294-matrix_2x2_copy_mutability_fix-fh.patch) by @hivert created at 2010-02-17 15:41:33

Should be ready for review.

Florent



---

archive/issue_comments_073356.json:
```json
{
    "body": "Changing assignee from h to @hivert.",
    "created_at": "2010-02-17T15:41:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8294#issuecomment-73356",
    "user": "https://github.com/hivert"
}
```

Changing assignee from h to @hivert.



---

archive/issue_comments_073357.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-17T15:41:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8294#issuecomment-73357",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073358.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-20T13:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8294#issuecomment-73358",
    "user": "https://trac.sagemath.org/admin/accounts/users/mraum"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073359.json:
```json
{
    "body": "This applies cleanly and all tests pass. Positive review as is.\n#8276 will follow soon.",
    "created_at": "2010-02-20T13:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8294#issuecomment-73359",
    "user": "https://trac.sagemath.org/admin/accounts/users/mraum"
}
```

This applies cleanly and all tests pass. Positive review as is.
#8276 will follow soon.



---

archive/issue_comments_073360.json:
```json
{
    "body": "Replying to [comment:3 mraum]:\n> This applies cleanly and all tests pass. Positive review as is.\n> #8276 will follow soon.\n\n\nThanks a lot for this quick help !",
    "created_at": "2010-02-20T13:53:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8294#issuecomment-73360",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:3 mraum]:
> This applies cleanly and all tests pass. Positive review as is.
> #8276 will follow soon.


Thanks a lot for this quick help !



---

archive/issue_comments_073361.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-03T14:27:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8294",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8294#issuecomment-73361",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_019854.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-03-03T14:27:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8294",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8294#event-19854"
}
```
