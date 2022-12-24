# Issue 5369: [with patch, needs review] Optimize transpose for matrix_integer_dense and matrix_rational_dense

archive/issues_005369.json:
```json
{
    "body": "Assignee: was\n\nCC:  rbeezer\n\nKeywords: transpose\n\nmatrix_integer_dense and matrix_rational_dense don't have any optimize transpose functions, so add it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5369\n\n",
    "created_at": "2009-02-25T10:00:02Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "[with patch, needs review] Optimize transpose for matrix_integer_dense and matrix_rational_dense",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5369",
    "user": "ylchapuy"
}
```
Assignee: was

CC:  rbeezer

Keywords: transpose

matrix_integer_dense and matrix_rational_dense don't have any optimize transpose functions, so add it.

Issue created by migration from https://trac.sagemath.org/ticket/5369





---

archive/issue_comments_041354.json:
```json
{
    "body": "Attachment [trac-5369-transpose-gmp-matrix.patch](tarball://root/attachments/some-uuid/ticket5369/trac-5369-transpose-gmp-matrix.patch) by ylchapuy created at 2009-02-25 10:08:48\n\nI did only one ticket for both as they are both gmp based.\n\nI mostly copied the logic used in the __copy__ function (by the way I also simplified the __copy__ function in matrix_rational_dense.pyx)\n\ntimings (wall time) for\n\n```\nm=identity_matrix(3000);\ntime m2=m.transpose(); m3=m.antitranspose();\n```\n\n* sage 3-3: 15.44\n* with #5345: 3.38\n* with this patch: 2.01",
    "created_at": "2009-02-25T10:08:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5369#issuecomment-41354",
    "user": "ylchapuy"
}
```

Attachment [trac-5369-transpose-gmp-matrix.patch](tarball://root/attachments/some-uuid/ticket5369/trac-5369-transpose-gmp-matrix.patch) by ylchapuy created at 2009-02-25 10:08:48

I did only one ticket for both as they are both gmp based.

I mostly copied the logic used in the __copy__ function (by the way I also simplified the __copy__ function in matrix_rational_dense.pyx)

timings (wall time) for

```
m=identity_matrix(3000);
time m2=m.transpose(); m3=m.antitranspose();
```

* sage 3-3: 15.44
* with #5345: 3.38
* with this patch: 2.01



---

archive/issue_comments_041355.json:
```json
{
    "body": "Attachment [trac-5369-transpose-gmp-matrix.2.patch](tarball://root/attachments/some-uuid/ticket5369/trac-5369-transpose-gmp-matrix.2.patch) by mhansen created at 2009-02-25 18:25:29\n\nLooks good.  I updated the patch to the new docstring format in 3.4.\n\nApply only trac-5369-transpose-gmp-matrix.2.patch",
    "created_at": "2009-02-25T18:25:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5369#issuecomment-41355",
    "user": "mhansen"
}
```

Attachment [trac-5369-transpose-gmp-matrix.2.patch](tarball://root/attachments/some-uuid/ticket5369/trac-5369-transpose-gmp-matrix.2.patch) by mhansen created at 2009-02-25 18:25:29

Looks good.  I updated the patch to the new docstring format in 3.4.

Apply only trac-5369-transpose-gmp-matrix.2.patch



---

archive/issue_comments_041356.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-28T21:04:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5369#issuecomment-41356",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_041357.json:
```json
{
    "body": "Merged trac-5369-transpose-gmp-matrix.2.patch in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-28T21:04:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5369#issuecomment-41357",
    "user": "mabshoff"
}
```

Merged trac-5369-transpose-gmp-matrix.2.patch in Sage 3.4.rc0.

Cheers,

Michael
