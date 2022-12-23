# Issue 2919: [with patch, needs review] gcc 4.3: compilation issues in partitions_c.cc

archive/issues_002919.json:
```json
{
    "body": "Assignee: mabshoff\n\npartitions_c.cc does not build with gcc 4.3 since it dislikes \n\n```\ntemplate <> static inline dd_real pi() { return dd_pi; }\n```\n\nThe attached patch fixes those issues, compile tested with gcc 4.3, 4.1 and 4.0\n\nCheers,\n\nMichael \n\nIssue created by migration from https://trac.sagemath.org/ticket/2919\n\n",
    "created_at": "2008-04-14T19:28:37Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] gcc 4.3: compilation issues in partitions_c.cc",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2919",
    "user": "mabshoff"
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

archive/issue_comments_020101.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-14T19:30:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2919#issuecomment-20101",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_020102.json:
```json
{
    "body": "Looks good to me :)",
    "created_at": "2008-04-14T19:31:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2919#issuecomment-20102",
    "user": "mhansen"
}
```

Looks good to me :)



---

archive/issue_comments_020103.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-14T19:57:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2919#issuecomment-20103",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020104.json:
```json
{
    "body": "Merged in Sage 3.0.alpha5",
    "created_at": "2008-04-14T19:57:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2919#issuecomment-20104",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha5
