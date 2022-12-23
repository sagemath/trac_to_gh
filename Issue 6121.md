# Issue 6121: use metaclasses to support nested class pickling

archive/issues_006121.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  sage-combinat cwitty\n\nKeywords: pickling, nested classes\n\nWe can work around this by shipping and always using a custom cPickle, and hopefully this will eventually be fixed in Python itself, but a metaclass seems to be a less hackish solution. \n\nAnother solution is decorators, but this requires a decorator on every use. \n\nIssue created by migration from https://trac.sagemath.org/ticket/6121\n\n",
    "created_at": "2009-05-22T23:06:34Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "use metaclasses to support nested class pickling",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6121",
    "user": "robertwb"
}
```
Assignee: cwitty

CC:  sage-combinat cwitty

Keywords: pickling, nested classes

We can work around this by shipping and always using a custom cPickle, and hopefully this will eventually be fixed in Python itself, but a metaclass seems to be a less hackish solution. 

Another solution is decorators, but this requires a decorator on every use. 

Issue created by migration from https://trac.sagemath.org/ticket/6121





---

archive/issue_comments_048915.json:
```json
{
    "body": "Thanks in advance for doing it.\n\nNotes:\n- Fundamentally, the two approaches work the same (fixing the name, and inserting it in the module).\n  The only difference is when this occur.\n- We anyway need to ship a patched cPickle for #5985.\n- This is a blocker for a bunch of later patches.",
    "created_at": "2009-05-23T03:30:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6121#issuecomment-48915",
    "user": "nthiery"
}
```

Thanks in advance for doing it.

Notes:
- Fundamentally, the two approaches work the same (fixing the name, and inserting it in the module).
  The only difference is when this occur.
- We anyway need to ship a patched cPickle for #5985.
- This is a blocker for a bunch of later patches.



---

archive/issue_comments_048916.json:
```json
{
    "body": "Depends on #6110\n\nAuthorship credit should go to nthiery as well.",
    "created_at": "2009-06-10T09:03:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6121#issuecomment-48916",
    "user": "robertwb"
}
```

Depends on #6110

Authorship credit should go to nthiery as well.



---

archive/issue_comments_048917.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-06-10T09:04:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6121#issuecomment-48917",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_048918.json:
```json
{
    "body": "Applies and test smoothly (and 4.1, with #6110 applied first) and does its job.",
    "created_at": "2009-06-12T15:59:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6121#issuecomment-48918",
    "user": "nthiery"
}
```

Applies and test smoothly (and 4.1, with #6110 applied first) and does its job.



---

archive/issue_comments_048919.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-06-12T15:59:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6121#issuecomment-48919",
    "user": "nthiery"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_048920.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T21:54:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6121#issuecomment-48920",
    "user": "ncalexan"
}
```

Resolution: fixed



---

archive/issue_comments_048921.json:
```json
{
    "body": "A comment on #5986 indicates that it may be solved with this ticket.",
    "created_at": "2009-09-22T17:09:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6121#issuecomment-48921",
    "user": "jason"
}
```

A comment on #5986 indicates that it may be solved with this ticket.
