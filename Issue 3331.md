# Issue 3331: [with patch, needs review] Disable --incref-local-binop in pbuild

archive/issues_003331.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nCC:  @robertwb\n\nKeywords: pbuild\n\nThe --incref-local-binop option in cython seems to be unneeded, and costs performance and readability.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3331\n\n",
    "created_at": "2008-05-29T19:18:27Z",
    "labels": [
        "component: pbuild"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "[with patch, needs review] Disable --incref-local-binop in pbuild",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3331",
    "user": "https://github.com/garyfurnish"
}
```
Assignee: @garyfurnish

CC:  @robertwb

Keywords: pbuild

The --incref-local-binop option in cython seems to be unneeded, and costs performance and readability.

Issue created by migration from https://trac.sagemath.org/ticket/3331





---

archive/issue_comments_023051.json:
```json
{
    "body": "Attachment [trac_3331_extcode.patch](tarball://root/attachments/some-uuid/ticket3331/trac_3331_extcode.patch) by @garyfurnish created at 2008-05-29 19:18:46",
    "created_at": "2008-05-29T19:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3331#issuecomment-23051",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_3331_extcode.patch](tarball://root/attachments/some-uuid/ticket3331/trac_3331_extcode.patch) by @garyfurnish created at 2008-05-29 19:18:46



---

archive/issue_comments_023052.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-29T19:19:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3331#issuecomment-23052",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_023053.json:
```json
{
    "body": "Patch looks good to me. Positive review. \n\nRobert: I think we can apply the same patch to the current build system. Thoughts?\n\nCheers,\n\nMichael",
    "created_at": "2008-05-31T06:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3331#issuecomment-23053",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me. Positive review. 

Robert: I think we can apply the same patch to the current build system. Thoughts?

Cheers,

Michael



---

archive/issue_comments_023054.json:
```json
{
    "body": "Merged in Sage 3.0.3.alpha1",
    "created_at": "2008-05-31T06:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3331#issuecomment-23054",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.3.alpha1



---

archive/issue_events_007468.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-05-31T06:12:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3331",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3331#event-7468"
}
```



---

archive/issue_comments_023055.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-31T06:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3331#issuecomment-23055",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_023056.json:
```json
{
    "body": "Yep, that's fine. The only reason it was there was to enable inplace operators, but there's issues with NumPy so it's already disabled in the code.",
    "created_at": "2008-06-02T17:47:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3331#issuecomment-23056",
    "user": "https://github.com/robertwb"
}
```

Yep, that's fine. The only reason it was there was to enable inplace operators, but there's issues with NumPy so it's already disabled in the code.
