# Issue 2046: [with patch] save(srange(3), './foo') fails

archive/issues_002046.json:
```json
{
    "body": "Assignee: was\n\nThis bug was reported by Georg here: http://groups.google.com/group/sage-support/browse_thread/thread/a1c5910c053abc90/28f1b635fba382a4#28f1b635fba382a4\n\n```\nsage: save(srange(3), './foo')\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/home/cwitty/<ipython console> in <module>()\n\n/home/cwitty/sage_object.pyx in sage.structure.sage_object.save()\n\n<type 'exceptions.AttributeError'>: 'list' object has no attribute 'save'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2046\n\n",
    "created_at": "2008-02-05T01:51:21Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "title": "[with patch] save(srange(3), './foo') fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2046",
    "user": "cwitty"
}
```
Assignee: was

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

archive/issue_comments_013250.json:
```json
{
    "body": "Attachment [trac-2046.patch](tarball://root/attachments/some-uuid/ticket2046/trac-2046.patch) by cwitty created at 2008-02-05 01:52:48",
    "created_at": "2008-02-05T01:52:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2046#issuecomment-13250",
    "user": "cwitty"
}
```

Attachment [trac-2046.patch](tarball://root/attachments/some-uuid/ticket2046/trac-2046.patch) by cwitty created at 2008-02-05 01:52:48



---

archive/issue_comments_013251.json:
```json
{
    "body": "it looks right, applies cleanly, and works.",
    "created_at": "2008-02-05T05:07:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2046#issuecomment-13251",
    "user": "was"
}
```

it looks right, applies cleanly, and works.



---

archive/issue_comments_013252.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0",
    "created_at": "2008-02-07T05:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2046#issuecomment-13252",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha0



---

archive/issue_comments_013253.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-07T05:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2046",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2046#issuecomment-13253",
    "user": "mabshoff"
}
```

Resolution: fixed
