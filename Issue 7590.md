# Issue 7590: Create Bipartite Graph according to 2 degree sequences

archive/issues_007590.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @wdjoyner\n\nGiven the sequence of degrees for set A and a sequence of degree for set B, create the corresponding bipartite graph if possible.\n\nUse #7301\n\nIssue created by migration from https://trac.sagemath.org/ticket/7590\n\n",
    "created_at": "2009-12-03T12:40:23Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Create Bipartite Graph according to 2 degree sequences",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7590",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: @rlmill

CC:  @wdjoyner

Given the sequence of degrees for set A and a sequence of degree for set B, create the corresponding bipartite graph if possible.

Use #7301

Issue created by migration from https://trac.sagemath.org/ticket/7590





---

archive/issue_comments_064591.json:
```json
{
    "body": "Here it is !",
    "created_at": "2009-12-04T17:51:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7590#issuecomment-64591",
    "user": "https://github.com/nathanncohen"
}
```

Here it is !



---

archive/issue_comments_064592.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-04T17:51:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7590#issuecomment-64592",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064593.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2009-12-15T17:57:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7590#issuecomment-64593",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_064594.json:
```json
{
    "body": "What is the status of #7301 and this patch? The comments on #7301 are a bit confusing, but at the end it seems as if perhaps this patch should depend on the other version instead of #7301?",
    "created_at": "2009-12-15T17:57:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7590#issuecomment-64594",
    "user": "https://github.com/rlmill"
}
```

What is the status of #7301 and this patch? The comments on #7301 are a bit confusing, but at the end it seems as if perhaps this patch should depend on the other version instead of #7301?



---

archive/issue_comments_064595.json:
```json
{
    "body": "Well, I'd say this patch is ready for review (as it is written and functional) even though #7301 is not :-)\n\nThe discussion in #7301 could lead to a gale_ryser function which does not use GLPK  ( and may be even more efficient ), which is good for everybody :-)\n\nAs this function is not so fundamental to Sage, I see no harm in making it wait until #7301 is ready :-)",
    "created_at": "2009-12-16T00:52:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7590#issuecomment-64595",
    "user": "https://github.com/nathanncohen"
}
```

Well, I'd say this patch is ready for review (as it is written and functional) even though #7301 is not :-)

The discussion in #7301 could lead to a gale_ryser function which does not use GLPK  ( and may be even more efficient ), which is good for everybody :-)

As this function is not so fundamental to Sage, I see no harm in making it wait until #7301 is ready :-)



---

archive/issue_comments_064596.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2009-12-16T00:52:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7590#issuecomment-64596",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_064597.json:
```json
{
    "body": "Attachment [trac_7590.patch](tarball://root/attachments/some-uuid/ticket7590/trac_7590.patch) by @rlmill created at 2009-12-16 03:01:01\n\nAdded # optional to some doctests.",
    "created_at": "2009-12-16T03:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7590#issuecomment-64597",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_7590.patch](tarball://root/attachments/some-uuid/ticket7590/trac_7590.patch) by @rlmill created at 2009-12-16 03:01:01

Added # optional to some doctests.



---

archive/issue_comments_064598.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-16T03:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7590#issuecomment-64598",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064599.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-12-16T03:05:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7590#issuecomment-64599",
    "user": "https://github.com/rlmill"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_064600.json:
```json
{
    "body": "(This is fine by me once #7301 is ready...)",
    "created_at": "2009-12-16T03:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7590#issuecomment-64600",
    "user": "https://github.com/rlmill"
}
```

(This is fine by me once #7301 is ready...)



---

archive/issue_comments_064601.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-13T09:03:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7590#issuecomment-64601",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064602.json:
```json
{
    "body": "positive review.",
    "created_at": "2010-01-13T09:04:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7590#issuecomment-64602",
    "user": "https://github.com/rlmill"
}
```

positive review.



---

archive/issue_comments_064603.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-13T09:04:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7590#issuecomment-64603",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_018018.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-13T09:04:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7590#event-18018"
}
```



---

archive/issue_comments_064604.json:
```json
{
    "body": "Thanks !! :-)",
    "created_at": "2010-01-13T09:05:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7590",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7590#issuecomment-64604",
    "user": "https://github.com/nathanncohen"
}
```

Thanks !! :-)
