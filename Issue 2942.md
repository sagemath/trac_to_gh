# Issue 2942: notebook -- new command line options: sage -n and sage -nb

archive/issues_002942.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  mpatel\n\nAfter a vote, almost everybody (including me) agrees with the following:\n\nsage -n:\n   run the notebook -- equivalent to \"sage -notebook\"\n\nsage -bn:\n   build sage, then run the notebook -- equivalent to \"sage -b; sage -n\"\n\nIssue created by migration from https://trac.sagemath.org/ticket/2942\n\n",
    "created_at": "2008-04-16T11:34:55Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "notebook -- new command line options: sage -n and sage -nb",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2942",
    "user": "was"
}
```
Assignee: boothby

CC:  mpatel

After a vote, almost everybody (including me) agrees with the following:

sage -n:
   run the notebook -- equivalent to "sage -notebook"

sage -bn:
   build sage, then run the notebook -- equivalent to "sage -b; sage -n"

Issue created by migration from https://trac.sagemath.org/ticket/2942





---

archive/issue_comments_020265.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-01-21T06:46:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2942#issuecomment-20265",
    "user": "TimothyClemans"
}
```

Attachment



---

archive/issue_comments_020266.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-21T06:47:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2942#issuecomment-20266",
    "user": "TimothyClemans"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_020267.json:
```json
{
    "body": "This patch makes 'sage -b' run the notebook!  Not cool.",
    "created_at": "2009-01-21T19:15:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2942#issuecomment-20267",
    "user": "ncalexan"
}
```

This patch makes 'sage -b' run the notebook!  Not cool.



---

archive/issue_comments_020268.json:
```json
{
    "body": "Added commands -n and -bn",
    "created_at": "2009-11-30T05:59:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2942#issuecomment-20268",
    "user": "timdumol"
}
```

Added commands -n and -bn



---

archive/issue_comments_020269.json:
```json
{
    "body": "Attachment\n\nThis patch should do the job.",
    "created_at": "2009-11-30T06:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2942#issuecomment-20269",
    "user": "timdumol"
}
```

Attachment

This patch should do the job.



---

archive/issue_comments_020270.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-30T06:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2942#issuecomment-20270",
    "user": "timdumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_020271.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-08T19:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2942#issuecomment-20271",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_020272.json:
```json
{
    "body": "Very, very nice.  It's especially nice how the build function is factored out.\n\nI doubt people will ever use \"sage -bn\", since the notebook is no longer in the sage library.  However, it can't hurt to have it.  I think \"sage -n\" will be very useful. \n\npositive review.",
    "created_at": "2009-12-08T19:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2942#issuecomment-20272",
    "user": "was"
}
```

Very, very nice.  It's especially nice how the build function is factored out.

I doubt people will ever use "sage -bn", since the notebook is no longer in the sage library.  However, it can't hurt to have it.  I think "sage -n" will be very useful. 

positive review.



---

archive/issue_comments_020273.json:
```json
{
    "body": "Note to release manager -- this gets applied to the Sage scripts repo, and has nothing to do with the sagenb spkg.  Hence I'm changing the component to \"build\".",
    "created_at": "2009-12-08T19:26:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2942#issuecomment-20273",
    "user": "was"
}
```

Note to release manager -- this gets applied to the Sage scripts repo, and has nothing to do with the sagenb spkg.  Hence I'm changing the component to "build".



---

archive/issue_comments_020274.json:
```json
{
    "body": "Changing component from notebook to build.",
    "created_at": "2009-12-08T19:26:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2942#issuecomment-20274",
    "user": "was"
}
```

Changing component from notebook to build.



---

archive/issue_comments_020275.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-09T02:36:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2942#issuecomment-20275",
    "user": "mhansen"
}
```

Resolution: fixed
