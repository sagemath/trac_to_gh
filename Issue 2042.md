# Issue 2042: [with patch, needs review] change is_simplified to has_been_simplified in calculus.py

archive/issues_002042.json:
```json
{
    "body": "Assignee: @aghitza\n\nSee\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/e342c0b1020de8bc\n\nThe point of is_simplified() is to keep track of whether the expression has already been simplified, rather than to check whether the expression is simplified.  The attached patch changes the name to has_been_simplified and adds a doctest.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2042\n\n",
    "created_at": "2008-02-04T00:39:37Z",
    "labels": [
        "component: calculus",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch, needs review] change is_simplified to has_been_simplified in calculus.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2042",
    "user": "https://github.com/aghitza"
}
```
Assignee: @aghitza

See
http://groups.google.com/group/sage-devel/browse_thread/thread/e342c0b1020de8bc

The point of is_simplified() is to keep track of whether the expression has already been simplified, rather than to check whether the expression is simplified.  The attached patch changes the name to has_been_simplified and adds a doctest.



Issue created by migration from https://trac.sagemath.org/ticket/2042





---

archive/issue_comments_013204.json:
```json
{
    "body": "Attachment [2042-has_been_simplified.patch](tarball://root/attachments/some-uuid/ticket2042/2042-has_been_simplified.patch) by @aghitza created at 2008-02-04 00:40:30",
    "created_at": "2008-02-04T00:40:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2042#issuecomment-13204",
    "user": "https://github.com/aghitza"
}
```

Attachment [2042-has_been_simplified.patch](tarball://root/attachments/some-uuid/ticket2042/2042-has_been_simplified.patch) by @aghitza created at 2008-02-04 00:40:30



---

archive/issue_comments_013205.json:
```json
{
    "body": "William's patches in #2073 already fix this and much much more.  So close this ticket (as duplicate, I guess) as soon as #2073 gets closed.",
    "created_at": "2008-02-07T04:42:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2042#issuecomment-13205",
    "user": "https://github.com/aghitza"
}
```

William's patches in #2073 already fix this and much much more.  So close this ticket (as duplicate, I guess) as soon as #2073 gets closed.



---

archive/issue_events_002200.json:
```json
{
    "actor": "https://github.com/aghitza",
    "created_at": "2008-02-07T17:44:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2042",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2042#event-2200"
}
```



---

archive/issue_comments_013206.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-02-07T17:44:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2042",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2042#issuecomment-13206",
    "user": "https://github.com/aghitza"
}
```

Resolution: duplicate
