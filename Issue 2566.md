# Issue 2566: [with patch, needs review] fix type of "size" in graph_isom and binary_code

archive/issues_002566.json:
```json
{
    "body": "Assignee: rlm\n\nBecause, after all, 14! > 2<sup>32</sup> and 21! > 2<sup>64</sup>.\n\nThis also makes the codewords in `binary_code.pyx` unsigned, because of those pesky signed integer shifting issues...\n\nIssue created by migration from https://trac.sagemath.org/ticket/2566\n\n",
    "created_at": "2008-03-17T06:39:38Z",
    "labels": [
        "coding theory",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] fix type of \"size\" in graph_isom and binary_code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2566",
    "user": "rlm"
}
```
Assignee: rlm

Because, after all, 14! > 2<sup>32</sup> and 21! > 2<sup>64</sup>.

This also makes the codewords in `binary_code.pyx` unsigned, because of those pesky signed integer shifting issues...

Issue created by migration from https://trac.sagemath.org/ticket/2566





---

archive/issue_comments_017494.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-03-19T23:42:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2566#issuecomment-17494",
    "user": "rlm"
}
```

Attachment



---

archive/issue_comments_017495.json:
```json
{
    "body": "Applies and passes tests.  Looks good to me.",
    "created_at": "2008-03-19T23:56:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2566#issuecomment-17495",
    "user": "mhansen"
}
```

Applies and passes tests.  Looks good to me.



---

archive/issue_comments_017496.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-20T00:58:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2566#issuecomment-17496",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017497.json:
```json
{
    "body": "Merged in Sage 2.11.alpha0",
    "created_at": "2008-03-20T00:58:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2566#issuecomment-17497",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha0
