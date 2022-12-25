# Issue 5078: bug in factoring out constant literal

archive/issues_005078.json:
```json
{
    "body": "Assignee: cwitty\n\n```\nsage: R1 = PolynomialRing(QQ, 'x,y,z')\nsage: R1.0\nTraceback (most recent call last):\n...\nNameError: name 'R1_sage_const_p0' is not defined\nsage: R1.gen(0)\nx\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/5078\n\n",
    "created_at": "2009-01-23T22:23:39Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "bug in factoring out constant literal",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5078",
    "user": "https://github.com/williamstein"
}
```
Assignee: cwitty

```
sage: R1 = PolynomialRing(QQ, 'x,y,z')
sage: R1.0
Traceback (most recent call last):
...
NameError: name 'R1_sage_const_p0' is not defined
sage: R1.gen(0)
x
```

Issue created by migration from https://trac.sagemath.org/ticket/5078





---

archive/issue_comments_038595.json:
```json
{
    "body": "Attachment [5078-preparse-const.patch](tarball://root/attachments/some-uuid/ticket5078/5078-preparse-const.patch) by @robertwb created at 2009-01-24 02:05:15",
    "created_at": "2009-01-24T02:05:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5078#issuecomment-38595",
    "user": "https://github.com/robertwb"
}
```

Attachment [5078-preparse-const.patch](tarball://root/attachments/some-uuid/ticket5078/5078-preparse-const.patch) by @robertwb created at 2009-01-24 02:05:15



---

archive/issue_comments_038596.json:
```json
{
    "body": "Works for me.",
    "created_at": "2009-01-24T02:36:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5078#issuecomment-38596",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Works for me.



---

archive/issue_events_011716.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-24T16:28:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5078",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5078#event-11716"
}
```



---

archive/issue_comments_038597.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T16:28:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5078#issuecomment-38597",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha2



---

archive/issue_comments_038598.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T16:28:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5078",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5078#issuecomment-38598",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
