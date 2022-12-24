# Issue 9392: Broken docstring in binpacking method

archive/issues_009392.json:
```json
{
    "body": "Assignee: jason, jkantor\n\nCC:  rlm leif\n\nNot really broken, but subject to change of behaviours depending on the solver used.... ;-)\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/9392\n\n",
    "created_at": "2010-06-30T05:46:10Z",
    "labels": [
        "numerical",
        "major",
        "bug"
    ],
    "title": "Broken docstring in binpacking method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9392",
    "user": "ncohen"
}
```
Assignee: jason, jkantor

CC:  rlm leif

Not really broken, but subject to change of behaviours depending on the solver used.... ;-)

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/9392





---

archive/issue_comments_089415.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-30T05:47:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9392#issuecomment-89415",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089416.json:
```json
{
    "body": "Attachment [trac_9392.patch](tarball://root/attachments/some-uuid/ticket9392/trac_9392.patch) by ncohen created at 2010-06-30 05:47:05\n\nHere it is !\n\nNathann",
    "created_at": "2010-06-30T05:47:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9392#issuecomment-89416",
    "user": "ncohen"
}
```

Attachment [trac_9392.patch](tarball://root/attachments/some-uuid/ticket9392/trac_9392.patch) by ncohen created at 2010-06-30 05:47:05

Here it is !

Nathann



---

archive/issue_comments_089417.json:
```json
{
    "body": "Nathann's patch fails on normal (non-optional) doctesting because of undefined variables/some sections *not* marked \"optional\".",
    "created_at": "2010-07-04T20:15:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9392#issuecomment-89417",
    "user": "leif"
}
```

Nathann's patch fails on normal (non-optional) doctesting because of undefined variables/some sections *not* marked "optional".



---

archive/issue_comments_089418.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-04T20:15:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9392#issuecomment-89418",
    "user": "leif"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089419.json:
```json
{
    "body": "Attachment [trac_9392-first_reviewer.patch](tarball://root/attachments/some-uuid/ticket9392/trac_9392-first_reviewer.patch) by leif created at 2010-07-04 20:16:37\n\nFixes non-optional doctesting. Apply on top of Nathann's patch.",
    "created_at": "2010-07-04T20:16:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9392#issuecomment-89419",
    "user": "leif"
}
```

Attachment [trac_9392-first_reviewer.patch](tarball://root/attachments/some-uuid/ticket9392/trac_9392-first_reviewer.patch) by leif created at 2010-07-04 20:16:37

Fixes non-optional doctesting. Apply on top of Nathann's patch.



---

archive/issue_comments_089420.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-04T20:25:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9392#issuecomment-89420",
    "user": "leif"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089421.json:
```json
{
    "body": "With my reviewer patch applied, at least passes reasonable tests (`-long`, `-long` with `-only-optional=cbc,glpk` in `sage/numerical`) on a 32-bit system where the doctest previously did *not* fail...\n\nLeaving as \"needs review\" for further testing.",
    "created_at": "2010-07-04T20:25:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9392#issuecomment-89421",
    "user": "leif"
}
```

With my reviewer patch applied, at least passes reasonable tests (`-long`, `-long` with `-only-optional=cbc,glpk` in `sage/numerical`) on a 32-bit system where the doctest previously did *not* fail...

Leaving as "needs review" for further testing.



---

archive/issue_comments_089422.json:
```json
{
    "body": "Doesn't this depend on #9312?",
    "created_at": "2010-07-05T21:27:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9392#issuecomment-89422",
    "user": "rlm"
}
```

Doesn't this depend on #9312?



---

archive/issue_comments_089423.json:
```json
{
    "body": "Not really... Though if we say it depends on #9312, then we do not need to add these \"optional\" flags anymore :-D\n\nNathann",
    "created_at": "2010-07-05T21:33:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9392#issuecomment-89423",
    "user": "ncohen"
}
```

Not really... Though if we say it depends on #9312, then we do not need to add these "optional" flags anymore :-D

Nathann



---

archive/issue_comments_089424.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-05T22:32:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9392#issuecomment-89424",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089425.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-05T22:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9392#issuecomment-89425",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_089426.json:
```json
{
    "body": "Well, if GLPK gets a standard package, we should **definitely** remove the `optional` tags, since otherwise these tests are omitted in the usual test process.\n\n(We could just substitute `optional` by `standard` to make life easier in case the package is made optional again for some reason. Same for Nathann's patch at #9312.)",
    "created_at": "2010-07-05T23:11:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9392#issuecomment-89426",
    "user": "leif"
}
```

Well, if GLPK gets a standard package, we should **definitely** remove the `optional` tags, since otherwise these tests are omitted in the usual test process.

(We could just substitute `optional` by `standard` to make life easier in case the package is made optional again for some reason. Same for Nathann's patch at #9312.)



---

archive/issue_comments_089427.json:
```json
{
    "body": "Replying to [comment:9 leif]:\n> Well, if GLPK gets a standard package, we should **definitely** remove the `optional` tags, since otherwise these tests are omitted in the usual test process.\n\nThis is addressed at #9432.",
    "created_at": "2010-07-06T04:03:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9392",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9392#issuecomment-89427",
    "user": "leif"
}
```

Replying to [comment:9 leif]:
> Well, if GLPK gets a standard package, we should **definitely** remove the `optional` tags, since otherwise these tests are omitted in the usual test process.

This is addressed at #9432.
