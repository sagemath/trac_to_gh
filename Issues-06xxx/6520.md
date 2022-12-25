# Issue 6520: [with patch, needs work] Implement cached_function with weakref cache

archive/issues_006520.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat @roed314 simonking\n\nKeywords: cached function, weakref\n\nThe preliminary attached patch (taken from the Sage-Combinat patch server) implements a variant of cached_function where the cache uses weak references. Again: preliminary: the test do not pass, ...\n\nFeedback welcome!\n\nThe first planned application is for homsets, after the category stuff #5985 will be in.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6520\n\n",
    "closed_at": "2014-02-11T21:21:39Z",
    "created_at": "2009-07-13T06:16:28Z",
    "labels": [
        "component: misc"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch, needs work] Implement cached_function with weakref cache",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6520",
    "user": "https://github.com/nthiery"
}
```
Assignee: @nthiery

CC:  sage-combinat @roed314 simonking

Keywords: cached function, weakref

The preliminary attached patch (taken from the Sage-Combinat patch server) implements a variant of cached_function where the cache uses weak references. Again: preliminary: the test do not pass, ...

Feedback welcome!

The first planned application is for homsets, after the category stuff #5985 will be in.



Issue created by migration from https://trac.sagemath.org/ticket/6520





---

archive/issue_comments_053054.json:
```json
{
    "body": "Changing assignee from cwitty to @nthiery.",
    "created_at": "2009-07-13T06:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6520#issuecomment-53054",
    "user": "https://github.com/nthiery"
}
```

Changing assignee from cwitty to @nthiery.



---

archive/issue_comments_053055.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-07-13T06:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6520#issuecomment-53055",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to assigned.



---

archive/issue_comments_053056.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-07-13T06:22:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6520#issuecomment-53056",
    "user": "https://github.com/nthiery"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_053057.json:
```json
{
    "body": "Attachment [trac_6520_weakref-cached-function-dr.patch](tarball://root/attachments/some-uuid/ticket6520/trac_6520_weakref-cached-function-dr.patch) by @nthiery created at 2009-07-13 06:36:07",
    "created_at": "2009-07-13T06:36:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6520#issuecomment-53057",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_6520_weakref-cached-function-dr.patch](tarball://root/attachments/some-uuid/ticket6520/trac_6520_weakref-cached-function-dr.patch) by @nthiery created at 2009-07-13 06:36:07



---

archive/issue_comments_053058.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-02-11T15:05:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6520#issuecomment-53058",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_events_015390.json:
```json
{
    "actor": "https://github.com/mezzarobba",
    "created_at": "2014-02-11T15:05:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6520",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6520#event-15390"
}
```



---

archive/issue_comments_053059.json:
```json
{
    "body": "Done in #12215?",
    "created_at": "2014-02-11T15:05:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6520#issuecomment-53059",
    "user": "https://github.com/mezzarobba"
}
```

Done in #12215?



---

archive/issue_comments_053060.json:
```json
{
    "body": "Replying to [comment:3 mmezzarobba]:\n> Done in #12215?\n\n\nI think so.",
    "created_at": "2014-02-11T15:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6520#issuecomment-53060",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:3 mmezzarobba]:
> Done in #12215?


I think so.



---

archive/issue_comments_053061.json:
```json
{
    "body": "This is the same feature as ``@`weak_cached_method` from #12215.",
    "created_at": "2014-02-11T19:49:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6520#issuecomment-53061",
    "user": "https://github.com/tscrim"
}
```

This is the same feature as ``@`weak_cached_method` from #12215.



---

archive/issue_comments_053062.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-02-11T19:49:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6520#issuecomment-53062",
    "user": "https://github.com/tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_053063.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-02-11T21:21:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6520#issuecomment-53063",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_015391.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-02-11T21:21:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6520",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6520#event-15391"
}
```
