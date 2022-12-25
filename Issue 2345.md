# Issue 2345: negative indicies in vectors

archive/issues_002345.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: vector(RR,range(3))[2]\n 2.00000000000000\n\nsage: vector(RR,range(3))[-1]\n----------------------------------------------------\n\n/home/dfdeshom/custom/sage/devel/sage-gcd2/<ipython\nconsole> in <module>()\n\n/home/dfdeshom/custom/sage/devel/sage-gcd2/free_modu\nle_element.pyx in sage.modules.free_module_element.F\nreeModuleElement_generic_dense.__getitem__()\n\n<type 'exceptions.IndexError'>: index (i=-1) must be\n between 0 and 2\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2345\n\n",
    "created_at": "2008-02-28T08:47:58Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "negative indicies in vectors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2345",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @williamstein


```
sage: vector(RR,range(3))[2]
 2.00000000000000

sage: vector(RR,range(3))[-1]
----------------------------------------------------

/home/dfdeshom/custom/sage/devel/sage-gcd2/<ipython
console> in <module>()

/home/dfdeshom/custom/sage/devel/sage-gcd2/free_modu
le_element.pyx in sage.modules.free_module_element.F
reeModuleElement_generic_dense.__getitem__()

<type 'exceptions.IndexError'>: index (i=-1) must be
 between 0 and 2
```


Issue created by migration from https://trac.sagemath.org/ticket/2345





---

archive/issue_comments_015668.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2008-02-28T09:36:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2345#issuecomment-15668",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_015669.json:
```json
{
    "body": "Attachment [2345.patch](tarball://root/attachments/some-uuid/ticket2345/2345.patch) by @mwhansen created at 2008-02-28 09:36:58",
    "created_at": "2008-02-28T09:36:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2345#issuecomment-15669",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2345.patch](tarball://root/attachments/some-uuid/ticket2345/2345.patch) by @mwhansen created at 2008-02-28 09:36:58



---

archive/issue_comments_015670.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-28T09:36:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2345#issuecomment-15670",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015671.json:
```json
{
    "body": "The patch looks great, thanks!",
    "created_at": "2008-02-28T14:33:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2345#issuecomment-15671",
    "user": "https://github.com/dfdeshom"
}
```

The patch looks great, thanks!



---

archive/issue_events_005532.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-03T02:55:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2345",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2345#event-5532"
}
```



---

archive/issue_comments_015672.json:
```json
{
    "body": "There was a long discussion about it and in the end the patch was voted in in the thread:\n\nhttps://groups.google.com/group/sage-devel/browse_thread/thread/0aadcca5557ea45a/80148bb28bec02d1#80148bb28bec02d1\n\nCheers,\n\nMichael",
    "created_at": "2008-03-03T02:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2345#issuecomment-15672",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

There was a long discussion about it and in the end the patch was voted in in the thread:

https://groups.google.com/group/sage-devel/browse_thread/thread/0aadcca5557ea45a/80148bb28bec02d1#80148bb28bec02d1

Cheers,

Michael



---

archive/issue_comments_015673.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-03T02:55:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2345#issuecomment-15673",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015674.json:
```json
{
    "body": "Merged in 2.10.3.rc1.",
    "created_at": "2008-03-03T03:42:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2345#issuecomment-15674",
    "user": "https://github.com/mwhansen"
}
```

Merged in 2.10.3.rc1.
