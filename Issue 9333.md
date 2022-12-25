# Issue 9333: the kash optional spkg doesn't work at all on OS X due to mistake in use of tar

archive/issues_009333.json:
```json
{
    "body": "Assignee: tbd\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9333\n\n",
    "created_at": "2010-06-25T03:08:21Z",
    "labels": [
        "component: packages: optional",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.1",
    "title": "the kash optional spkg doesn't work at all on OS X due to mistake in use of tar",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9333",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd



Issue created by migration from https://trac.sagemath.org/ticket/9333





---

archive/issue_comments_087921.json:
```json
{
    "body": "Attachment [trac_9333-kash-tar.patch](tarball://root/attachments/some-uuid/ticket9333/trac_9333-kash-tar.patch) by @jhpalmieri created at 2011-05-27 04:58:07\n\nfor reference only; do not apply",
    "created_at": "2011-05-27T04:58:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9333#issuecomment-87921",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_9333-kash-tar.patch](tarball://root/attachments/some-uuid/ticket9333/trac_9333-kash-tar.patch) by @jhpalmieri created at 2011-05-27 04:58:07

for reference only; do not apply



---

archive/issue_comments_087922.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-05-27T05:01:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9333#issuecomment-87922",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087923.json:
```json
{
    "body": "I've posted a link to a new spkg, along with the patch used to create it.  I have a feeling that it could use more work, but since it's an optional package for software which is 3 years old, I'm not sure if it's worth it.  I also have a feeling that it shouldn't be an optional package, but rather an experimental one: since it only installs on OS X and linux, that's not enough platforms for a good optional package.  But that change should be discussed elsewhere...",
    "created_at": "2011-05-27T05:01:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9333#issuecomment-87923",
    "user": "https://github.com/jhpalmieri"
}
```

I've posted a link to a new spkg, along with the patch used to create it.  I have a feeling that it could use more work, but since it's an optional package for software which is 3 years old, I'm not sure if it's worth it.  I also have a feeling that it shouldn't be an optional package, but rather an experimental one: since it only installs on OS X and linux, that's not enough platforms for a good optional package.  But that change should be discussed elsewhere...



---

archive/issue_comments_087924.json:
```json
{
    "body": "It even works on PPC!\n\nI did find an error in kash.py\n\n```\nsage: a = kash('(9 - 7) * (5 + 6)'); a              # optional -- kash\n\n22\n```\n\nso I get \"expected nothing\" for that one test when I do `./sage -t -optional devel/sage/sage/interfaces/kash.py`.\n\nOtherwise seems like this is reasonable.  Fix that and positive review, modulo my weak understanding of shell script - but the options are the right ones on Mac.  What the heck are those Linux options?\n\nBy the way, the development of KASH seems to have abruptly stopped.  Any chance it will resume?",
    "created_at": "2011-06-08T20:17:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9333#issuecomment-87924",
    "user": "https://github.com/kcrisman"
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

archive/issue_comments_087925.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-06-08T20:17:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9333#issuecomment-87925",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_087926.json:
```json
{
    "body": "Attachment [trac_9333-kash-sage-library.patch](tarball://root/attachments/some-uuid/ticket9333/trac_9333-kash-sage-library.patch) by @jhpalmieri created at 2011-06-08 21:44:37\n\npatch for sage library",
    "created_at": "2011-06-08T21:44:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9333#issuecomment-87926",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_9333-kash-sage-library.patch](tarball://root/attachments/some-uuid/ticket9333/trac_9333-kash-sage-library.patch) by @jhpalmieri created at 2011-06-08 21:44:37

patch for sage library



---

archive/issue_comments_087927.json:
```json
{
    "body": "Removing the blank line fixes the doctest for me.  (I have no idea what the linux options are, by the way.)",
    "created_at": "2011-06-08T21:45:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9333#issuecomment-87927",
    "user": "https://github.com/jhpalmieri"
}
```

Removing the blank line fixes the doctest for me.  (I have no idea what the linux options are, by the way.)



---

archive/issue_comments_087928.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-06-08T21:45:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9333#issuecomment-87928",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_087929.json:
```json
{
    "body": "Thumbs up.",
    "created_at": "2011-06-08T22:15:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9333#issuecomment-87929",
    "user": "https://github.com/kcrisman"
}
```

Thumbs up.



---

archive/issue_comments_087930.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-06-08T22:15:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9333#issuecomment-87930",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087931.json:
```json
{
    "body": "Sage patch merged in sage-4.7.1.alpha4 but the \"optional packages\" page needs to be updated manually.  John, can you take care of this?",
    "created_at": "2011-06-20T19:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9333#issuecomment-87931",
    "user": "https://github.com/jdemeyer"
}
```

Sage patch merged in sage-4.7.1.alpha4 but the "optional packages" page needs to be updated manually.  John, can you take care of this?



---

archive/issue_comments_087932.json:
```json
{
    "body": "Replying to [comment:6 jdemeyer]:\n> Sage patch merged in sage-4.7.1.alpha4 but the \"optional packages\" page needs to be updated manually.  John, can you take care of this?\n\nOkay, done.",
    "created_at": "2011-07-01T18:16:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9333#issuecomment-87932",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:6 jdemeyer]:
> Sage patch merged in sage-4.7.1.alpha4 but the "optional packages" page needs to be updated manually.  John, can you take care of this?

Okay, done.



---

archive/issue_comments_087933.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-07-03T11:17:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9333",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9333#issuecomment-87933",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
