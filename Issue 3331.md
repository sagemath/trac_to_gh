# Issue 3331: [with patch, needs review] Disable --incref-local-binop in pbuild

archive/issues_003331.json:
```json
{
    "body": "Assignee: gfurnish\n\nCC:  robertwb\n\nKeywords: pbuild\n\nThe --incref-local-binop option in cython seems to be unneeded, and costs performance and readability.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3331\n\n",
    "created_at": "2008-05-29T19:18:27Z",
    "labels": [
        "pbuild",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] Disable --incref-local-binop in pbuild",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3331",
    "user": "gfurnish"
}
```
Assignee: gfurnish

CC:  robertwb

Keywords: pbuild

The --incref-local-binop option in cython seems to be unneeded, and costs performance and readability.

Issue created by migration from https://trac.sagemath.org/ticket/3331





---

archive/issue_comments_023099.json:
```json
{
    "body": "Attachment [trac_3331_extcode.patch](tarball://root/attachments/some-uuid/ticket3331/trac_3331_extcode.patch) by gfurnish created at 2008-05-29 19:18:46",
    "created_at": "2008-05-29T19:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3331#issuecomment-23099",
    "user": "gfurnish"
}
```

Attachment [trac_3331_extcode.patch](tarball://root/attachments/some-uuid/ticket3331/trac_3331_extcode.patch) by gfurnish created at 2008-05-29 19:18:46



---

archive/issue_comments_023100.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-29T19:19:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3331#issuecomment-23100",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_023101.json:
```json
{
    "body": "Patch looks good to me. Positive review. \n\nRobert: I think we can apply the same patch to the current build system. Thoughts?\n\nCheers,\n\nMichael",
    "created_at": "2008-05-31T06:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3331#issuecomment-23101",
    "user": "mabshoff"
}
```

Patch looks good to me. Positive review. 

Robert: I think we can apply the same patch to the current build system. Thoughts?

Cheers,

Michael



---

archive/issue_comments_023102.json:
```json
{
    "body": "Merged in Sage 3.0.3.alpha1",
    "created_at": "2008-05-31T06:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3331#issuecomment-23102",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.3.alpha1



---

archive/issue_comments_023103.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-31T06:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3331#issuecomment-23103",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_023104.json:
```json
{
    "body": "Yep, that's fine. The only reason it was there was to enable inplace operators, but there's issues with NumPy so it's already disabled in the code.",
    "created_at": "2008-06-02T17:47:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3331#issuecomment-23104",
    "user": "robertwb"
}
```

Yep, that's fine. The only reason it was there was to enable inplace operators, but there's issues with NumPy so it's already disabled in the code.
