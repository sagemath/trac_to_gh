# Issue 5265: Link the matrix_mod2_dense extension against png12

archive/issues_005265.json:
```json
{
    "body": "Assignee: mabshoff\n\nRight now we link the matrix_mod2_dense.pyx aginst libpng:\n\n```\n     Extension('sage.matrix.matrix_mod2_dense',\n               sources = ['sage/matrix/matrix_mod2_dense.pyx'],\n               libraries = ['gmp','m4ri', 'png', 'gd']),\n```\n\nWe need to link against png12 since the new libpng.spkg will only provide libpng12.*.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5265\n\n",
    "created_at": "2009-02-14T09:53:07Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "Link the matrix_mod2_dense extension against png12",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5265",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Right now we link the matrix_mod2_dense.pyx aginst libpng:

```
     Extension('sage.matrix.matrix_mod2_dense',
               sources = ['sage/matrix/matrix_mod2_dense.pyx'],
               libraries = ['gmp','m4ri', 'png', 'gd']),
```

We need to link against png12 since the new libpng.spkg will only provide libpng12.*.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5265





---

archive/issue_comments_040419.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-14T09:53:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5265#issuecomment-40419",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040420.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-02-14T09:54:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5265#issuecomment-40420",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_040421.json:
```json
{
    "body": "Attachment\n\nPlease review both patches. The second patch is needed to make 100% the extension is rebuild in case of an upgrade. Sorry for the two patches, but I couldn't fold them since I committed the first one to my local repo already.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T10:01:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5265#issuecomment-40421",
    "user": "mabshoff"
}
```

Attachment

Please review both patches. The second patch is needed to make 100% the extension is rebuild in case of an upgrade. Sorry for the two patches, but I couldn't fold them since I committed the first one to my local repo already.

Cheers,

Michael



---

archive/issue_comments_040422.json:
```json
{
    "body": "I applied both patches, touched matrix_mod2_dense.pyx, did sage -b, and then ran the tests in matrix_mod2_dense.pyx, and everything passed.  If that's all that is needed to review this patch, then positive review.  If not, the take my positive review off.",
    "created_at": "2009-02-14T10:11:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5265#issuecomment-40422",
    "user": "jason"
}
```

I applied both patches, touched matrix_mod2_dense.pyx, did sage -b, and then ran the tests in matrix_mod2_dense.pyx, and everything passed.  If that's all that is needed to review this patch, then positive review.  If not, the take my positive review off.



---

archive/issue_comments_040423.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-14T13:24:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5265#issuecomment-40423",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040424.json:
```json
{
    "body": "Merged both patches in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T13:24:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5265",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5265#issuecomment-40424",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.3.rc1.

Cheers,

Michael
