# Issue 2638: complex QQbar expressions exceed maximum recursion depth when exact computation is triggered

archive/issues_002638.json:
```json
{
    "body": "Assignee: somebody\n\nFor example, \n\n```\nsage: s = SFASchur(QQ)\nsage: a=s([3,2]).expand(8)(flatten([[QQbar.zeta(3)^d for d in range(3)], [QQbar.zeta(5)^d for d in range(5)]]))\nsage: a.exactify() \n```\n\n(as reported in http://groups.google.com/group/sage-devel/browse_thread/thread/8cf79f359cceef3d/e931afceebf3fe35#e931afceebf3fe35)\n\nIssue created by migration from https://trac.sagemath.org/ticket/2638\n\n",
    "created_at": "2008-03-21T22:01:45Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "complex QQbar expressions exceed maximum recursion depth when exact computation is triggered",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2638",
    "user": "cwitty"
}
```
Assignee: somebody

For example, 

```
sage: s = SFASchur(QQ)
sage: a=s([3,2]).expand(8)(flatten([[QQbar.zeta(3)^d for d in range(3)], [QQbar.zeta(5)^d for d in range(5)]]))
sage: a.exactify() 
```

(as reported in http://groups.google.com/group/sage-devel/browse_thread/thread/8cf79f359cceef3d/e931afceebf3fe35#e931afceebf3fe35)

Issue created by migration from https://trac.sagemath.org/ticket/2638





---

archive/issue_comments_018136.json:
```json
{
    "body": "Attachment [trac_2638.patch](tarball://root/attachments/some-uuid/ticket2638/trac_2638.patch) by mhansen created at 2009-01-23 02:55:23",
    "created_at": "2009-01-23T02:55:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2638",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2638#issuecomment-18136",
    "user": "mhansen"
}
```

Attachment [trac_2638.patch](tarball://root/attachments/some-uuid/ticket2638/trac_2638.patch) by mhansen created at 2009-01-23 02:55:23



---

archive/issue_comments_018137.json:
```json
{
    "body": "Works for me, all tests in QQbar pass.",
    "created_at": "2009-01-24T11:04:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2638",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2638#issuecomment-18137",
    "user": "boothby"
}
```

Works for me, all tests in QQbar pass.



---

archive/issue_comments_018138.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T19:31:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2638",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2638#issuecomment-18138",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018139.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T19:31:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2638",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2638#issuecomment-18139",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha2

Cheers,

Michael
