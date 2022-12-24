# Issue 3590: dage_interfaces -- port detection code hangs solid

archive/issues_003590.json:
```json
{
    "body": "Assignee: @yqiang\n\n\n```\nsage -t  devel/sage/sage/dsage/interface/dsage_interface.py *** ***\nError: TIMED OUT! *** ***\n[DSage] Closed connection to localhost\n[DSage] Closed connection to localhost\n[DSage] Closed connection to localhost\n[DSage] Closed connection to localhost\n*** *** Error: TIMED OUT! *** ***\n        [2697.3 s]\n```\n\n\nThis is at\n\n```\nport = find_open_port().next()\n```\n\n\nThis happens on *some machines*, e.g., fermat.math.harvard.edu, but not others.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3590\n\n",
    "created_at": "2008-07-07T20:42:55Z",
    "labels": [
        "dsage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "dage_interfaces -- port detection code hangs solid",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3590",
    "user": "@williamstein"
}
```
Assignee: @yqiang


```
sage -t  devel/sage/sage/dsage/interface/dsage_interface.py *** ***
Error: TIMED OUT! *** ***
[DSage] Closed connection to localhost
[DSage] Closed connection to localhost
[DSage] Closed connection to localhost
[DSage] Closed connection to localhost
*** *** Error: TIMED OUT! *** ***
        [2697.3 s]
```


This is at

```
port = find_open_port().next()
```


This happens on *some machines*, e.g., fermat.math.harvard.edu, but not others.



Issue created by migration from https://trac.sagemath.org/ticket/3590





---

archive/issue_comments_025371.json:
```json
{
    "body": "Attachment [10033.patch](tarball://root/attachments/some-uuid/ticket3590/10033.patch) by @williamstein created at 2008-07-07 23:20:42",
    "created_at": "2008-07-07T23:20:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3590#issuecomment-25371",
    "user": "@williamstein"
}
```

Attachment [10033.patch](tarball://root/attachments/some-uuid/ticket3590/10033.patch) by @williamstein created at 2008-07-07 23:20:42



---

archive/issue_comments_025372.json:
```json
{
    "body": "Attachment [10034.patch](tarball://root/attachments/some-uuid/ticket3590/10034.patch) by @williamstein created at 2008-07-08 00:10:15",
    "created_at": "2008-07-08T00:10:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3590#issuecomment-25372",
    "user": "@williamstein"
}
```

Attachment [10034.patch](tarball://root/attachments/some-uuid/ticket3590/10034.patch) by @williamstein created at 2008-07-08 00:10:15



---

archive/issue_comments_025373.json:
```json
{
    "body": "It's better than the existing code :)",
    "created_at": "2008-07-08T00:19:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3590#issuecomment-25373",
    "user": "@ncalexan"
}
```

It's better than the existing code :)



---

archive/issue_comments_025374.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-08T00:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3590#issuecomment-25374",
    "user": "@williamstein"
}
```

Resolution: fixed
