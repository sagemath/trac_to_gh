# Issue 9795: Add a "diagonal" method for matrices

archive/issues_009795.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  kcrisman\n\nSee http://ask.sagemath.org/question/54/how-to-get-the-diagonal-of-a-matrix\n\nIssue created by migration from https://trac.sagemath.org/ticket/9796\n\n",
    "created_at": "2010-08-24T15:54:40Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "title": "Add a \"diagonal\" method for matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9795",
    "user": "jason"
}
```
Assignee: jason, was

CC:  kcrisman

See http://ask.sagemath.org/question/54/how-to-get-the-diagonal-of-a-matrix

Issue created by migration from https://trac.sagemath.org/ticket/9796





---

archive/issue_comments_096167.json:
```json
{
    "body": "Attachment",
    "created_at": "2011-01-13T04:29:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9795#issuecomment-96167",
    "user": "rbeezer"
}
```

Attachment



---

archive/issue_comments_096168.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-29T03:50:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9795#issuecomment-96168",
    "user": "rbeezer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096169.json:
```json
{
    "body": "Changing keywords from \"\" to \"beginner\".",
    "created_at": "2011-01-29T03:50:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9795#issuecomment-96169",
    "user": "rbeezer"
}
```

Changing keywords from "" to "beginner".



---

archive/issue_comments_096170.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-02-04T22:13:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9795#issuecomment-96170",
    "user": "tomc"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096171.json:
```json
{
    "body": "This looks good.  Running:\n\n```\nsage -testall -long\n```\n\ngives that all doctests pass except five unrelated tests (in sage/plot/plot3d/tachyon.py and sage/plot/plot3d/base.pyx) that also fail in an unpatched copy of Sage (version 4.6.1, built from source on 64-bit Linux).",
    "created_at": "2011-02-04T22:13:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9795#issuecomment-96171",
    "user": "tomc"
}
```

This looks good.  Running:

```
sage -testall -long
```

gives that all doctests pass except five unrelated tests (in sage/plot/plot3d/tachyon.py and sage/plot/plot3d/base.pyx) that also fail in an unpatched copy of Sage (version 4.6.1, built from source on 64-bit Linux).



---

archive/issue_comments_096172.json:
```json
{
    "body": "Replying to [comment:3 tomc]:\n\nThanks for the review, Tom - the help is appreciated.\n\nRob",
    "created_at": "2011-02-05T23:10:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9795#issuecomment-96172",
    "user": "rbeezer"
}
```

Replying to [comment:3 tomc]:

Thanks for the review, Tom - the help is appreciated.

Rob



---

archive/issue_comments_096173.json:
```json
{
    "body": "I hope it's okay that I 'guessed' the reviewer's name from the trac main page!",
    "created_at": "2011-02-06T01:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9795#issuecomment-96173",
    "user": "kcrisman"
}
```

I hope it's okay that I 'guessed' the reviewer's name from the trac main page!



---

archive/issue_comments_096174.json:
```json
{
    "body": "Replying to [comment:5 kcrisman]:\n> I hope it's okay that I 'guessed' the reviewer's name from the trac main page!\n\nI suppose so, I do that all the time.",
    "created_at": "2011-02-07T08:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9795#issuecomment-96174",
    "user": "jdemeyer"
}
```

Replying to [comment:5 kcrisman]:
> I hope it's okay that I 'guessed' the reviewer's name from the trac main page!

I suppose so, I do that all the time.



---

archive/issue_comments_096175.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-02-16T08:49:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9795",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9795#issuecomment-96175",
    "user": "jdemeyer"
}
```

Resolution: fixed
