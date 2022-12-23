# Issue 9333: the kash optional spkg doesn't work at all on OS X due to mistake in use of tar

archive/issues_009333.json:
```json
{
    "body": "Assignee: tbd\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9333\n\n",
    "created_at": "2010-06-25T03:08:21Z",
    "labels": [
        "packages: optional",
        "minor",
        "bug"
    ],
    "title": "the kash optional spkg doesn't work at all on OS X due to mistake in use of tar",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9333",
    "user": "was"
}
```
Assignee: tbd



Issue created by migration from https://trac.sagemath.org/ticket/9333





---

archive/issue_comments_088060.json:
```json
{
    "body": "Attachment\n\nfor reference only; do not apply",
    "created_at": "2011-05-27T04:58:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9333#issuecomment-88060",
    "user": "jhpalmieri"
}
```

Attachment

for reference only; do not apply



---

archive/issue_comments_088061.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-05-27T05:01:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9333#issuecomment-88061",
    "user": "jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_088062.json:
```json
{
    "body": "I've posted a link to a new spkg, along with the patch used to create it.  I have a feeling that it could use more work, but since it's an optional package for software which is 3 years old, I'm not sure if it's worth it.  I also have a feeling that it shouldn't be an optional package, but rather an experimental one: since it only installs on OS X and linux, that's not enough platforms for a good optional package.  But that change should be discussed elsewhere...",
    "created_at": "2011-05-27T05:01:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9333#issuecomment-88062",
    "user": "jhpalmieri"
}
```

I've posted a link to a new spkg, along with the patch used to create it.  I have a feeling that it could use more work, but since it's an optional package for software which is 3 years old, I'm not sure if it's worth it.  I also have a feeling that it shouldn't be an optional package, but rather an experimental one: since it only installs on OS X and linux, that's not enough platforms for a good optional package.  But that change should be discussed elsewhere...



---

archive/issue_comments_088063.json:
```json
{
    "body": "It even works on PPC!\n\nI did find an error in kash.py\n\n```\nsage: a = kash('(9 - 7) * (5 + 6)'); a              # optional -- kash\n\n22\n```\n\nso I get \"expected nothing\" for that one test when I do `./sage -t -optional devel/sage/sage/interfaces/kash.py`.\n\nOtherwise seems like this is reasonable.  Fix that and positive review, modulo my weak understanding of shell script - but the options are the right ones on Mac.  What the heck are those Linux options?\n\nBy the way, the development of KASH seems to have abruptly stopped.  Any chance it will resume?",
    "created_at": "2011-06-08T20:17:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9333#issuecomment-88063",
    "user": "kcrisman"
}
```

It even works on PPC!

I did find an error in kash.py

```
sage: a = kash('(9 - 7) * (5 + 6)'); a              # optional -- kash

22
```

so I get "expected nothing" for that one test when I do `./sage -t -optional devel/sage/sage/interfaces/kash.py`.

Otherwise seems like this is reasonable.  Fix that and positive review, modulo my weak understanding of shell script - but the options are the right ones on Mac.  What the heck are those Linux options?

By the way, the development of KASH seems to have abruptly stopped.  Any chance it will resume?



---

archive/issue_comments_088064.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-06-08T20:17:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9333#issuecomment-88064",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_088065.json:
```json
{
    "body": "Attachment\n\npatch for sage library",
    "created_at": "2011-06-08T21:44:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9333#issuecomment-88065",
    "user": "jhpalmieri"
}
```

Attachment

patch for sage library



---

archive/issue_comments_088066.json:
```json
{
    "body": "Removing the blank line fixes the doctest for me.  (I have no idea what the linux options are, by the way.)",
    "created_at": "2011-06-08T21:45:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9333#issuecomment-88066",
    "user": "jhpalmieri"
}
```

Removing the blank line fixes the doctest for me.  (I have no idea what the linux options are, by the way.)



---

archive/issue_comments_088067.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-06-08T21:45:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9333#issuecomment-88067",
    "user": "jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_088068.json:
```json
{
    "body": "Thumbs up.",
    "created_at": "2011-06-08T22:15:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9333#issuecomment-88068",
    "user": "kcrisman"
}
```

Thumbs up.



---

archive/issue_comments_088069.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-06-08T22:15:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9333#issuecomment-88069",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_088070.json:
```json
{
    "body": "Sage patch merged in sage-4.7.1.alpha4 but the \"optional packages\" page needs to be updated manually.  John, can you take care of this?",
    "created_at": "2011-06-20T19:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9333#issuecomment-88070",
    "user": "jdemeyer"
}
```

Sage patch merged in sage-4.7.1.alpha4 but the "optional packages" page needs to be updated manually.  John, can you take care of this?



---

archive/issue_comments_088071.json:
```json
{
    "body": "Replying to [comment:6 jdemeyer]:\n> Sage patch merged in sage-4.7.1.alpha4 but the \"optional packages\" page needs to be updated manually.  John, can you take care of this?\n\nOkay, done.",
    "created_at": "2011-07-01T18:16:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9333#issuecomment-88071",
    "user": "jhpalmieri"
}
```

Replying to [comment:6 jdemeyer]:
> Sage patch merged in sage-4.7.1.alpha4 but the "optional packages" page needs to be updated manually.  John, can you take care of this?

Okay, done.



---

archive/issue_comments_088072.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-07-03T11:17:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9333#issuecomment-88072",
    "user": "jdemeyer"
}
```

Resolution: fixed
