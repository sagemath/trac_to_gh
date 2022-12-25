# Issue 2046: [with patch] save(srange(3), './foo') fails

archive/issues_002046.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis bug was reported by Georg here: http://groups.google.com/group/sage-support/browse_thread/thread/a1c5910c053abc90/28f1b635fba382a4#28f1b635fba382a4\n\n```\nsage: save(srange(3), './foo')\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/home/cwitty/<ipython console> in <module>()\n\n/home/cwitty/sage_object.pyx in sage.structure.sage_object.save()\n\n<type 'exceptions.AttributeError'>: 'list' object has no attribute 'save'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2046\n\n",
    "created_at": "2008-02-05T01:51:21Z",
    "labels": [
        "component: user interface",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "[with patch] save(srange(3), './foo') fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2046",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @williamstein

This bug was reported by Georg here: http://groups.google.com/group/sage-support/browse_thread/thread/a1c5910c053abc90/28f1b635fba382a4#28f1b635fba382a4

```
sage: save(srange(3), './foo')
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/home/cwitty/<ipython console> in <module>()

/home/cwitty/sage_object.pyx in sage.structure.sage_object.save()

<type 'exceptions.AttributeError'>: 'list' object has no attribute 'save'
```


Issue created by migration from https://trac.sagemath.org/ticket/2046





---

archive/issue_comments_013219.json:
```json
{
    "body": "Attachment [trac-2046.patch](tarball://root/attachments/some-uuid/ticket2046/trac-2046.patch) by cwitty created at 2008-02-05 01:52:48",
    "created_at": "2008-02-05T01:52:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2046#issuecomment-13219",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac-2046.patch](tarball://root/attachments/some-uuid/ticket2046/trac-2046.patch) by cwitty created at 2008-02-05 01:52:48



---

archive/issue_comments_013220.json:
```json
{
    "body": "it looks right, applies cleanly, and works.",
    "created_at": "2008-02-05T05:07:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2046#issuecomment-13220",
    "user": "https://github.com/williamstein"
}
```

it looks right, applies cleanly, and works.



---

archive/issue_comments_013221.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0",
    "created_at": "2008-02-07T05:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2046#issuecomment-13221",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha0



---

archive/issue_events_004919.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-07T05:27:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2046",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2046#event-4919"
}
```



---

archive/issue_comments_013222.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-07T05:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2046#issuecomment-13222",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
