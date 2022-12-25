# Issue 1084: invalid use of ring notation gives bizarre post-preparser syntax error

archive/issues_001084.json:
```json
{
    "body": "Assignee: @ncalexan\n\nConsider this example:\n\n```\nsage: QQX = QQ['x']\nsage: K.<x> = QQX\n------------------------------------------------------------\n   File \"<ipython console>\", line 1\n     K = QQ,names=(u'x',)); (x,) = K._first_ngens(Integer(1))\n                         ^\n<type 'exceptions.SyntaxError'>: invalid syntax\n```\n\n\nI don't care if this actually works; but if it doesn't, it should fail with a friendlier error message.  And where did the 'X' from QQX go?\n\nIssue created by migration from https://trac.sagemath.org/ticket/1084\n\n",
    "created_at": "2007-11-03T20:09:14Z",
    "labels": [
        "component: user interface",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.12",
    "title": "invalid use of ring notation gives bizarre post-preparser syntax error",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1084",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @ncalexan

Consider this example:

```
sage: QQX = QQ['x']
sage: K.<x> = QQX
------------------------------------------------------------
   File "<ipython console>", line 1
     K = QQ,names=(u'x',)); (x,) = K._first_ngens(Integer(1))
                         ^
<type 'exceptions.SyntaxError'>: invalid syntax
```


I don't care if this actually works; but if it doesn't, it should fail with a friendlier error message.  And where did the 'X' from QQX go?

Issue created by migration from https://trac.sagemath.org/ticket/1084





---

archive/issue_comments_006535.json:
```json
{
    "body": "Attachment [1084-ncalexan-1.hg](tarball://root/attachments/some-uuid/ticket1084/1084-ncalexan-1.hg) by @ncalexan created at 2007-11-04 01:42:11",
    "created_at": "2007-11-04T01:42:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1084#issuecomment-6535",
    "user": "https://github.com/ncalexan"
}
```

Attachment [1084-ncalexan-1.hg](tarball://root/attachments/some-uuid/ticket1084/1084-ncalexan-1.hg) by @ncalexan created at 2007-11-04 01:42:11



---

archive/issue_comments_006536.json:
```json
{
    "body": "Patch may require 1040-ncalexan-2.hg be attached first; check ticket 1040.",
    "created_at": "2007-11-04T01:43:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1084#issuecomment-6536",
    "user": "https://github.com/ncalexan"
}
```

Patch may require 1040-ncalexan-2.hg be attached first; check ticket 1040.



---

archive/issue_comments_006537.json:
```json
{
    "body": "applied to 2.8.12.rc0",
    "created_at": "2007-11-06T22:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1084#issuecomment-6537",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

applied to 2.8.12.rc0



---

archive/issue_events_001208.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-06T22:03:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1084",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1084#event-1208"
}
```



---

archive/issue_comments_006538.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-06T22:03:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1084#issuecomment-6538",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
