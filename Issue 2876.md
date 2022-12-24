# Issue 2876: sage/server/notebook/twist.py doctest fails when dsage certificates are not present

archive/issues_002876.json:
```json
{
    "body": "Assignee: boothby\n\nSince it's trying to use https, the notebook object will try to generate a self signed certificate when one is not present already. This doesn't work with doctesting since we can't expect user interaction. The fix switches the notebook server to use http instead. It looks like robert did a good job of disabling creating accounts so I don't see any new security holes created by this. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2876\n\n",
    "created_at": "2008-04-11T04:52:50Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "sage/server/notebook/twist.py doctest fails when dsage certificates are not present",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2876",
    "user": "@yqiang"
}
```
Assignee: boothby

Since it's trying to use https, the notebook object will try to generate a self signed certificate when one is not present already. This doesn't work with doctesting since we can't expect user interaction. The fix switches the notebook server to use http instead. It looks like robert did a good job of disabling creating accounts so I don't see any new security holes created by this. 

Issue created by migration from https://trac.sagemath.org/ticket/2876





---

archive/issue_comments_019756.json:
```json
{
    "body": "Cwitty pointed out that if you use the secure=False option, one gets logged on automatically. Does anyone know of an easy way to turn that feature off when doctesting?",
    "created_at": "2008-04-11T05:12:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2876#issuecomment-19756",
    "user": "@yqiang"
}
```

Cwitty pointed out that if you use the secure=False option, one gets logged on automatically. Does anyone know of an easy way to turn that feature off when doctesting?



---

archive/issue_comments_019757.json:
```json
{
    "body": "Attachment [simple_server_doctest.patch](tarball://root/attachments/some-uuid/ticket2876/simple_server_doctest.patch) by @williamstein created at 2008-04-11 23:45:07\n\nWorks perfectly.",
    "created_at": "2008-04-11T23:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2876#issuecomment-19757",
    "user": "@williamstein"
}
```

Attachment [simple_server_doctest.patch](tarball://root/attachments/some-uuid/ticket2876/simple_server_doctest.patch) by @williamstein created at 2008-04-11 23:45:07

Works perfectly.



---

archive/issue_comments_019758.json:
```json
{
    "body": "Merged in Sage 3.0.alpha4",
    "created_at": "2008-04-12T00:11:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2876#issuecomment-19758",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha4



---

archive/issue_comments_019759.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-12T00:11:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2876",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2876#issuecomment-19759",
    "user": "mabshoff"
}
```

Resolution: fixed
