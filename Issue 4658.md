# Issue 4658: magma -- get rid of redundant caching: just have _magma_init_

archive/issues_004658.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4658\n\n",
    "created_at": "2008-11-29T23:50:12Z",
    "labels": [
        "interfaces",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "magma -- get rid of redundant caching: just have _magma_init_",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4658",
    "user": "@williamstein"
}
```
Assignee: @williamstein



Issue created by migration from https://trac.sagemath.org/ticket/4658





---

archive/issue_comments_035088.json:
```json
{
    "body": "Attachment [trac_extcode-4658.patch](tarball://root/attachments/some-uuid/ticket4658/trac_extcode-4658.patch) by @williamstein created at 2008-11-30 07:35:48",
    "created_at": "2008-11-30T07:35:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4658#issuecomment-35088",
    "user": "@williamstein"
}
```

Attachment [trac_extcode-4658.patch](tarball://root/attachments/some-uuid/ticket4658/trac_extcode-4658.patch) by @williamstein created at 2008-11-30 07:35:48



---

archive/issue_comments_035089.json:
```json
{
    "body": "Attachment [trac_4658-sage.patch](tarball://root/attachments/some-uuid/ticket4658/trac_4658-sage.patch) by @williamstein created at 2008-11-30 07:42:03",
    "created_at": "2008-11-30T07:42:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4658#issuecomment-35089",
    "user": "@williamstein"
}
```

Attachment [trac_4658-sage.patch](tarball://root/attachments/some-uuid/ticket4658/trac_4658-sage.patch) by @williamstein created at 2008-11-30 07:42:03



---

archive/issue_comments_035090.json:
```json
{
    "body": "Positive review. I had various discussions with William about this patch while he was writing it. \n\nThe patch passes doctests with a booby trapped magma to flush out doctest failures without magma, it passes standard long doctests as well as -only_optional=magma. \n\nCheers,\n\nMichael",
    "created_at": "2008-11-30T08:35:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4658#issuecomment-35090",
    "user": "mabshoff"
}
```

Positive review. I had various discussions with William about this patch while he was writing it. 

The patch passes doctests with a booby trapped magma to flush out doctest failures without magma, it passes standard long doctests as well as -only_optional=magma. 

Cheers,

Michael



---

archive/issue_comments_035091.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-30T08:35:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4658#issuecomment-35091",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_035092.json:
```json
{
    "body": "Merged in Sage 3.2.1.rc1",
    "created_at": "2008-11-30T08:35:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4658#issuecomment-35092",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.rc1
