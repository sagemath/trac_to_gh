# Issue 8381: typo in documentation of rational_reconstruction

archive/issues_008381.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @burcin\n\nKeywords: beginner\n\n```\nsage: rational_reconstruction?\n...\n            `(x,y)=(|v2|,v3*mathrm{sign}(v2))` is then the unique\n```\nThe `mathrm` should be removed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8381\n\n",
    "closed_at": "2011-05-31T09:21:56Z",
    "created_at": "2010-02-26T23:00:00Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.1",
    "title": "typo in documentation of rational_reconstruction",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8381",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: mvngu

CC:  @burcin

Keywords: beginner

```
sage: rational_reconstruction?
...
            `(x,y)=(|v2|,v3*mathrm{sign}(v2))` is then the unique
```
The `mathrm` should be removed.

Issue created by migration from https://trac.sagemath.org/ticket/8381





---

archive/issue_comments_074845.json:
```json
{
    "body": "Changing keywords from \"\" to \"beginner\".",
    "created_at": "2010-05-26T15:18:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8381#issuecomment-74845",
    "user": "https://github.com/jasongrout"
}
```

Changing keywords from "" to "beginner".



---

archive/issue_comments_074846.json:
```json
{
    "body": "Attachment [15468.patch](tarball://root/attachments/some-uuid/ticket8381/15468.patch) by fdiebold created at 2011-05-22 20:06:28\n\nRemove \\mathop and \\mathrm when displaying docs in python",
    "created_at": "2011-05-22T20:06:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8381#issuecomment-74846",
    "user": "https://trac.sagemath.org/admin/accounts/users/fdiebold"
}
```

Attachment [15468.patch](tarball://root/attachments/some-uuid/ticket8381/15468.patch) by fdiebold created at 2011-05-22 20:06:28

Remove \mathop and \mathrm when displaying docs in python



---

archive/issue_comments_074847.json:
```json
{
    "body": "It seems to me that the sage help function should remove these latex commands (\\mathrm and \\mathop, which also occurs in some documentation in that file). The attached patch does that.",
    "created_at": "2011-05-22T20:12:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8381#issuecomment-74847",
    "user": "https://trac.sagemath.org/admin/accounts/users/fdiebold"
}
```

It seems to me that the sage help function should remove these latex commands (\mathrm and \mathop, which also occurs in some documentation in that file). The attached patch does that.



---

archive/issue_comments_074848.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-05-22T20:12:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8381#issuecomment-74848",
    "user": "https://trac.sagemath.org/admin/accounts/users/fdiebold"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074849.json:
```json
{
    "body": "good work! Positive review.\n\nPaul",
    "created_at": "2011-05-23T11:59:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8381#issuecomment-74849",
    "user": "https://github.com/zimmermann6"
}
```

good work! Positive review.

Paul



---

archive/issue_comments_074850.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-05-23T11:59:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8381#issuecomment-74850",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_020089.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-05-24T08:58:02Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8381",
    "milestone": "sage-4.7.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8381#event-20089"
}
```



---

archive/issue_comments_074851.json:
```json
{
    "body": "fdiebold: please add your real name as Author and also add yourself to [http://trac.sagemath.org/sage_trac/#AccountNamesmappedtoRealNames](http://trac.sagemath.org/sage_trac/#AccountNamesmappedtoRealNames)",
    "created_at": "2011-05-30T15:06:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8381#issuecomment-74851",
    "user": "https://github.com/jdemeyer"
}
```

fdiebold: please add your real name as Author and also add yourself to [http://trac.sagemath.org/sage_trac/#AccountNamesmappedtoRealNames](http://trac.sagemath.org/sage_trac/#AccountNamesmappedtoRealNames)



---

archive/issue_comments_074852.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2011-05-30T15:06:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8381#issuecomment-74852",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_074853.json:
```json
{
    "body": "Done.",
    "created_at": "2011-05-30T16:11:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8381#issuecomment-74853",
    "user": "https://trac.sagemath.org/admin/accounts/users/fdiebold"
}
```

Done.



---

archive/issue_events_020090.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-05-31T09:21:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8381",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8381#event-20090"
}
```



---

archive/issue_comments_074854.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-05-31T09:21:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8381#issuecomment-74854",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
