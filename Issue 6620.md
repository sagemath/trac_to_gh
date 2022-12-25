# Issue 6620: add a method to the Gap class to access elements of records

archive/issues_006620.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  nborie @wdjoyner\n\nAccessing elements of GAP records should be easier.\n\n```\n            sage: rec = gap('rec( a := 1, b := \"2\" )')\n            sage: gap.get_record_element(rec, 'a')\n            1\n            sage: gap.get_record_element(rec, 'b')\n            2\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6620\n\n",
    "created_at": "2009-07-25T17:11:16Z",
    "labels": [
        "component: interfaces"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "add a method to the Gap class to access elements of records",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6620",
    "user": "https://github.com/saliola"
}
```
Assignee: @williamstein

CC:  nborie @wdjoyner

Accessing elements of GAP records should be easier.

```
            sage: rec = gap('rec( a := 1, b := "2" )')
            sage: gap.get_record_element(rec, 'a')
            1
            sage: gap.get_record_element(rec, 'b')
            2
```


Issue created by migration from https://trac.sagemath.org/ticket/6620





---

archive/issue_comments_054147.json:
```json
{
    "body": "Attachment [trac_6620.patch](tarball://root/attachments/some-uuid/ticket6620/trac_6620.patch) by @saliola created at 2009-07-25 17:18:41",
    "created_at": "2009-07-25T17:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6620#issuecomment-54147",
    "user": "https://github.com/saliola"
}
```

Attachment [trac_6620.patch](tarball://root/attachments/some-uuid/ticket6620/trac_6620.patch) by @saliola created at 2009-07-25 17:18:41



---

archive/issue_comments_054148.json:
```json
{
    "body": "Applies fine to 4.1.1.a0, and passes sage -testall. I also played with it a bit and could not find any bugs and the docstrings seem fine.",
    "created_at": "2009-07-27T15:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6620#issuecomment-54148",
    "user": "https://github.com/wdjoyner"
}
```

Applies fine to 4.1.1.a0, and passes sage -testall. I also played with it a bit and could not find any bugs and the docstrings seem fine.



---

archive/issue_comments_054149.json:
```json
{
    "body": "reviewer patch; fix typos in ReST format",
    "created_at": "2009-08-24T13:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6620#issuecomment-54149",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

reviewer patch; fix typos in ReST format



---

archive/issue_comments_054150.json:
```json
{
    "body": "Attachment [trac_6620-reviewer.patch](tarball://root/attachments/some-uuid/ticket6620/trac_6620-reviewer.patch) by mvngu created at 2009-08-24 13:15:23\n\nThe patch `trac_6620-reviewer.patch` fixes some typos in ReST formatting introduced by `trac_6620.patch`. Such typos would result in warnings when (re)building the reference manual.",
    "created_at": "2009-08-24T13:15:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6620#issuecomment-54150",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_6620-reviewer.patch](tarball://root/attachments/some-uuid/ticket6620/trac_6620-reviewer.patch) by mvngu created at 2009-08-24 13:15:23

The patch `trac_6620-reviewer.patch` fixes some typos in ReST formatting introduced by `trac_6620.patch`. Such typos would result in warnings when (re)building the reference manual.



---

archive/issue_comments_054151.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-24T13:42:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6620#issuecomment-54151",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_006860.json:
```json
{
    "actor": "mvngu",
    "created_at": "2009-08-24T13:42:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6620",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6620#event-6860"
}
```



---

archive/issue_comments_054152.json:
```json
{
    "body": "Merged patches in this order:\n\n1. `trac_6620.patch`\n2. `trac_6620-reviewer.patch`",
    "created_at": "2009-08-24T13:42:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6620#issuecomment-54152",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged patches in this order:

1. `trac_6620.patch`
2. `trac_6620-reviewer.patch`
