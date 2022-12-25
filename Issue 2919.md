# Issue 2919: [with patch, needs review] gcc 4.3: compilation issues in partitions_c.cc

archive/issues_002919.json:
```json
{
    "body": "Assignee: mabshoff\n\npartitions_c.cc does not build with gcc 4.3 since it dislikes \n\n```\ntemplate <> static inline dd_real pi() { return dd_pi; }\n```\n\nThe attached patch fixes those issues, compile tested with gcc 4.3, 4.1 and 4.0\n\nCheers,\n\nMichael \n\nIssue created by migration from https://trac.sagemath.org/ticket/2919\n\n",
    "created_at": "2008-04-14T19:28:37Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch, needs review] gcc 4.3: compilation issues in partitions_c.cc",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2919",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

partitions_c.cc does not build with gcc 4.3 since it dislikes 

```
template <> static inline dd_real pi() { return dd_pi; }
```

The attached patch fixes those issues, compile tested with gcc 4.3, 4.1 and 4.0

Cheers,

Michael 

Issue created by migration from https://trac.sagemath.org/ticket/2919





---

archive/issue_comments_020060.json:
```json
{
    "body": "Attachment [trac_2919_sagelib-gcc-4.3-fixes.patch](tarball://root/attachments/some-uuid/ticket2919/trac_2919_sagelib-gcc-4.3-fixes.patch) by mabshoff created at 2008-04-14 19:30:13",
    "created_at": "2008-04-14T19:30:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2919#issuecomment-20060",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_2919_sagelib-gcc-4.3-fixes.patch](tarball://root/attachments/some-uuid/ticket2919/trac_2919_sagelib-gcc-4.3-fixes.patch) by mabshoff created at 2008-04-14 19:30:13



---

archive/issue_comments_020061.json:
```json
{
    "body": "Looks good to me :)",
    "created_at": "2008-04-14T19:31:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2919#issuecomment-20061",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me :)



---

archive/issue_events_006682.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-14T19:57:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2919",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2919#event-6682"
}
```



---

archive/issue_comments_020062.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-14T19:57:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2919#issuecomment-20062",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020063.json:
```json
{
    "body": "Merged in Sage 3.0.alpha5",
    "created_at": "2008-04-14T19:57:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2919#issuecomment-20063",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha5
