# Issue 7739: Improvements to AGM

archive/issues_007739.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @JohnCremona\n\nNative (much faster) agm for RDF and CDF, optimized and document agm for RR. \n\nInspired by, but somewhat orthogonal to, #7719.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7739\n\n",
    "created_at": "2009-12-18T23:57:01Z",
    "labels": [
        "component: basic arithmetic"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Improvements to AGM",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7739",
    "user": "https://github.com/robertwb"
}
```
Assignee: @aghitza

CC:  @JohnCremona

Native (much faster) agm for RDF and CDF, optimized and document agm for RR. 

Inspired by, but somewhat orthogonal to, #7719.


Issue created by migration from https://trac.sagemath.org/ticket/7739





---

archive/issue_comments_066388.json:
```json
{
    "body": "Look basically good.  Robert, do you want to add the test for a=0 or b=0 or a=-b in the complex_double case, and also perhaps a=0 or b=0 for the real cases?",
    "created_at": "2009-12-20T16:52:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7739#issuecomment-66388",
    "user": "https://github.com/JohnCremona"
}
```

Look basically good.  Robert, do you want to add the test for a=0 or b=0 or a=-b in the complex_double case, and also perhaps a=0 or b=0 for the real cases?



---

archive/issue_comments_066389.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-07T10:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7739#issuecomment-66389",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066390.json:
```json
{
    "body": "Attachment [7739-cdfrdf-agm.patch](tarball://root/attachments/some-uuid/ticket7739/7739-cdfrdf-agm.patch) by @robertwb created at 2010-01-07 10:50:46\n\nGood idea, I added some degenerate tests and refreshed the patch.",
    "created_at": "2010-01-07T10:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7739#issuecomment-66390",
    "user": "https://github.com/robertwb"
}
```

Attachment [7739-cdfrdf-agm.patch](tarball://root/attachments/some-uuid/ticket7739/7739-cdfrdf-agm.patch) by @robertwb created at 2010-01-07 10:50:46

Good idea, I added some degenerate tests and refreshed the patch.



---

archive/issue_comments_066391.json:
```json
{
    "body": "Attachment [7739-cdfrdf-agm.2.patch](tarball://root/attachments/some-uuid/ticket7739/7739-cdfrdf-agm.2.patch) by @JohnCremona created at 2010-01-07 15:47:39\n\ncorrects typo in previous patch (which it replaces)",
    "created_at": "2010-01-07T15:47:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7739#issuecomment-66391",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [7739-cdfrdf-agm.2.patch](tarball://root/attachments/some-uuid/ticket7739/7739-cdfrdf-agm.2.patch) by @JohnCremona created at 2010-01-07 15:47:39

corrects typo in previous patch (which it replaces)



---

archive/issue_comments_066392.json:
```json
{
    "body": "There's a typo (sgm for agm) in the docstring (line 1944 of complex_double).  I edited the patch to fix that.\n\nOtherwise I'm quite happy -- applies to 4.3 and tests in sage/rings/{real,complex}* all pass.  So: positive review!",
    "created_at": "2010-01-07T15:48:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7739#issuecomment-66392",
    "user": "https://github.com/JohnCremona"
}
```

There's a typo (sgm for agm) in the docstring (line 1944 of complex_double).  I edited the patch to fix that.

Otherwise I'm quite happy -- applies to 4.3 and tests in sage/rings/{real,complex}* all pass.  So: positive review!



---

archive/issue_comments_066393.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-07T15:48:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7739#issuecomment-66393",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_018512.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-13T08:43:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7739",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7739#event-18512"
}
```



---

archive/issue_comments_066394.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-13T08:43:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7739#issuecomment-66394",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_comments_066395.json:
```json
{
    "body": "Thanks.",
    "created_at": "2010-01-13T20:04:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7739",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7739#issuecomment-66395",
    "user": "https://github.com/robertwb"
}
```

Thanks.
