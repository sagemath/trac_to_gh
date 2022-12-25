# Issue 6121: use metaclasses to support nested class pickling

archive/issues_006121.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  sage-combinat cwitty\n\nKeywords: pickling, nested classes\n\nWe can work around this by shipping and always using a custom cPickle, and hopefully this will eventually be fixed in Python itself, but a metaclass seems to be a less hackish solution. \n\nAnother solution is decorators, but this requires a decorator on every use. \n\nIssue created by migration from https://trac.sagemath.org/ticket/6121\n\n",
    "created_at": "2009-05-22T23:06:34Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "use metaclasses to support nested class pickling",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6121",
    "user": "https://github.com/robertwb"
}
```
Assignee: cwitty

CC:  sage-combinat cwitty

Keywords: pickling, nested classes

We can work around this by shipping and always using a custom cPickle, and hopefully this will eventually be fixed in Python itself, but a metaclass seems to be a less hackish solution. 

Another solution is decorators, but this requires a decorator on every use. 

Issue created by migration from https://trac.sagemath.org/ticket/6121





---

archive/issue_comments_048820.json:
```json
{
    "body": "Thanks in advance for doing it.\n\nNotes:\n- Fundamentally, the two approaches work the same (fixing the name, and inserting it in the module).\n  The only difference is when this occur.\n- We anyway need to ship a patched cPickle for #5985.\n- This is a blocker for a bunch of later patches.",
    "created_at": "2009-05-23T03:30:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6121#issuecomment-48820",
    "user": "https://github.com/nthiery"
}
```

Thanks in advance for doing it.

Notes:
- Fundamentally, the two approaches work the same (fixing the name, and inserting it in the module).
  The only difference is when this occur.
- We anyway need to ship a patched cPickle for #5985.
- This is a blocker for a bunch of later patches.



---

archive/issue_comments_048821.json:
```json
{
    "body": "Depends on #6110\n\nAuthorship credit should go to nthiery as well.",
    "created_at": "2009-06-10T09:03:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6121#issuecomment-48821",
    "user": "https://github.com/robertwb"
}
```

Depends on #6110

Authorship credit should go to nthiery as well.



---

archive/issue_comments_048822.json:
```json
{
    "body": "Attachment [6121-nested-pickle-meta.patch](tarball://root/attachments/some-uuid/ticket6121/6121-nested-pickle-meta.patch) by @robertwb created at 2009-06-10 09:04:06",
    "created_at": "2009-06-10T09:04:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6121#issuecomment-48822",
    "user": "https://github.com/robertwb"
}
```

Attachment [6121-nested-pickle-meta.patch](tarball://root/attachments/some-uuid/ticket6121/6121-nested-pickle-meta.patch) by @robertwb created at 2009-06-10 09:04:06



---

archive/issue_comments_048823.json:
```json
{
    "body": "Applies and test smoothly (and 4.1, with #6110 applied first) and does its job.",
    "created_at": "2009-06-12T15:59:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6121#issuecomment-48823",
    "user": "https://github.com/nthiery"
}
```

Applies and test smoothly (and 4.1, with #6110 applied first) and does its job.



---

archive/issue_comments_048824.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-06-12T15:59:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6121#issuecomment-48824",
    "user": "https://github.com/nthiery"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_048825.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T21:54:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6121#issuecomment-48825",
    "user": "https://github.com/ncalexan"
}
```

Resolution: fixed



---

archive/issue_events_006371.json:
```json
{
    "actor": "@ncalexan",
    "created_at": "2009-06-13T21:54:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6121",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6121#event-6371"
}
```



---

archive/issue_comments_048826.json:
```json
{
    "body": "A comment on #5986 indicates that it may be solved with this ticket.",
    "created_at": "2009-09-22T17:09:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6121#issuecomment-48826",
    "user": "https://github.com/jasongrout"
}
```

A comment on #5986 indicates that it may be solved with this ticket.
