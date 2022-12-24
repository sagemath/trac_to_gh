# Issue 8535: Various interval field improvements

archive/issues_008535.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nBisection, plotting, max/min, and some doctests.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8535\n\n",
    "created_at": "2010-03-14T09:12:29Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Various interval field improvements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8535",
    "user": "robertwb"
}
```
Assignee: AlexGhitza

Bisection, plotting, max/min, and some doctests.

Issue created by migration from https://trac.sagemath.org/ticket/8535





---

archive/issue_comments_077138.json:
```json
{
    "body": "Attachment [8535-intervals.patch](tarball://root/attachments/some-uuid/ticket8535/8535-intervals.patch) by robertwb created at 2010-04-28 05:09:38",
    "created_at": "2010-04-28T05:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8535#issuecomment-77138",
    "user": "robertwb"
}
```

Attachment [8535-intervals.patch](tarball://root/attachments/some-uuid/ticket8535/8535-intervals.patch) by robertwb created at 2010-04-28 05:09:38



---

archive/issue_comments_077139.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-28T05:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8535#issuecomment-77139",
    "user": "robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077140.json:
```json
{
    "body": "Nice job on making good doctests.  Looks good.  One question, though: in the bisection methods, why did you round things using RNDZ, instead of RNDU or RNDD?",
    "created_at": "2010-05-14T19:05:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8535#issuecomment-77140",
    "user": "jason"
}
```

Nice job on making good doctests.  Looks good.  One question, though: in the bisection methods, why did you round things using RNDZ, instead of RNDU or RNDD?



---

archive/issue_comments_077141.json:
```json
{
    "body": "Doctests pass on rings/*.py[x].  So positive review if RNDZ is the correct thing to do when bisecting intervals.",
    "created_at": "2010-05-14T19:13:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8535#issuecomment-77141",
    "user": "jason"
}
```

Doctests pass on rings/*.py[x].  So positive review if RNDZ is the correct thing to do when bisecting intervals.



---

archive/issue_comments_077142.json:
```json
{
    "body": "I don't think either RNDU or RNDD would be the right thing to use here--who's to say that the upper or lower interval should always get the extra half ulp? Maybe RNDN would have been a better choice, I'll post a new patch.",
    "created_at": "2010-05-15T21:15:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8535#issuecomment-77142",
    "user": "robertwb"
}
```

I don't think either RNDU or RNDD would be the right thing to use here--who's to say that the upper or lower interval should always get the extra half ulp? Maybe RNDN would have been a better choice, I'll post a new patch.



---

archive/issue_comments_077143.json:
```json
{
    "body": "Replying to [comment:4 robertwb]:\n> I don't think either RNDU or RNDD would be the right thing to use here--who's to say that the upper or lower interval should always get the extra half ulp? Maybe RNDN would have been a better choice, I'll post a new patch. \n\nI agree, after thinking about it.  I also agree that RNDN would be a better choice.",
    "created_at": "2010-05-15T21:32:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8535#issuecomment-77143",
    "user": "jason"
}
```

Replying to [comment:4 robertwb]:
> I don't think either RNDU or RNDD would be the right thing to use here--who's to say that the upper or lower interval should always get the extra half ulp? Maybe RNDN would have been a better choice, I'll post a new patch. 

I agree, after thinking about it.  I also agree that RNDN would be a better choice.



---

archive/issue_comments_077144.json:
```json
{
    "body": "Same as previous, but uses GMP_RNDN rather than GMP_RNDZ",
    "created_at": "2010-05-15T21:35:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8535#issuecomment-77144",
    "user": "robertwb"
}
```

Same as previous, but uses GMP_RNDN rather than GMP_RNDZ



---

archive/issue_comments_077145.json:
```json
{
    "body": "Attachment [8535-intervals-rndn.patch](tarball://root/attachments/some-uuid/ticket8535/8535-intervals-rndn.patch) by robertwb created at 2010-05-15 21:36:06\n\nPatch attached.",
    "created_at": "2010-05-15T21:36:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8535#issuecomment-77145",
    "user": "robertwb"
}
```

Attachment [8535-intervals-rndn.patch](tarball://root/attachments/some-uuid/ticket8535/8535-intervals-rndn.patch) by robertwb created at 2010-05-15 21:36:06

Patch attached.



---

archive/issue_comments_077146.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-07T19:54:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8535#issuecomment-77146",
    "user": "robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077147.json:
```json
{
    "body": "Replying to [comment:3 jason]:\n> Doctests pass on rings/*.py[x].  So positive review if RNDZ is the correct thing to do when bisecting intervals.\n\nOK, I'm setting this to positive review then.",
    "created_at": "2010-06-07T19:54:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8535#issuecomment-77147",
    "user": "robertwb"
}
```

Replying to [comment:3 jason]:
> Doctests pass on rings/*.py[x].  So positive review if RNDZ is the correct thing to do when bisecting intervals.

OK, I'm setting this to positive review then.



---

archive/issue_comments_077148.json:
```json
{
    "body": "Note: only apply the second patch, not both!",
    "created_at": "2010-06-29T06:17:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8535#issuecomment-77148",
    "user": "cremona"
}
```

Note: only apply the second patch, not both!



---

archive/issue_comments_077149.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T09:20:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8535",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8535#issuecomment-77149",
    "user": "mpatel"
}
```

Resolution: fixed
