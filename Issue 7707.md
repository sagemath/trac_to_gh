# Issue 7707: change picklejar doctest to be more robust

archive/issues_007707.json:
```json
{
    "body": "Assignee: tbd\n\nThe picklejar doctest in structure/sage_object.pyx has to be changed whenever we update the picklejar, when things get deprecated, etc.  That's silly.  Let's change the test to be like this:\n\n```\n        sage: print \"x\"; sage....\n        x...\n        Failed to unpickle 0 objects.\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/7707\n\n",
    "created_at": "2009-12-16T09:11:02Z",
    "labels": [
        "component: doctest coverage"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "change picklejar doctest to be more robust",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7707",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

The picklejar doctest in structure/sage_object.pyx has to be changed whenever we update the picklejar, when things get deprecated, etc.  That's silly.  Let's change the test to be like this:

```
        sage: print "x"; sage....
        x...
        Failed to unpickle 0 objects.
```

Issue created by migration from https://trac.sagemath.org/ticket/7707





---

archive/issue_comments_066033.json:
```json
{
    "body": "Attachment [trac_7707.patch](tarball://root/attachments/some-uuid/ticket7707/trac_7707.patch) by @williamstein created at 2009-12-16 09:13:00",
    "created_at": "2009-12-16T09:13:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7707#issuecomment-66033",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_7707.patch](tarball://root/attachments/some-uuid/ticket7707/trac_7707.patch) by @williamstein created at 2009-12-16 09:13:00



---

archive/issue_comments_066034.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-16T09:13:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7707#issuecomment-66034",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066035.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-19T21:11:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7707#issuecomment-66035",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066036.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-12-19T21:11:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7707#issuecomment-66036",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_events_018406.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-20T07:20:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7707",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7707#event-18406"
}
```



---

archive/issue_comments_066037.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-20T07:20:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7707",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7707#issuecomment-66037",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_018407.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-20T07:25:41Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7707",
    "milestone": "sage-4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7707#event-18407"
}
```
