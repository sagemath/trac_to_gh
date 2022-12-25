# Issue 2942: notebook -- new command line options: sage -n and sage -nb

archive/issues_002942.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @qed777\n\nAfter a vote, almost everybody (including me) agrees with the following:\n\nsage -n:\n   run the notebook -- equivalent to \"sage -notebook\"\n\nsage -bn:\n   build sage, then run the notebook -- equivalent to \"sage -b; sage -n\"\n\nIssue created by migration from https://trac.sagemath.org/ticket/2942\n\n",
    "created_at": "2008-04-16T11:34:55Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "notebook -- new command line options: sage -n and sage -nb",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2942",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

CC:  @qed777

After a vote, almost everybody (including me) agrees with the following:

sage -n:
   run the notebook -- equivalent to "sage -notebook"

sage -bn:
   build sage, then run the notebook -- equivalent to "sage -b; sage -n"

Issue created by migration from https://trac.sagemath.org/ticket/2942





---

archive/issue_comments_020223.json:
```json
{
    "body": "Attachment [scripts-2942.patch](tarball://root/attachments/some-uuid/ticket2942/scripts-2942.patch) by TimothyClemans created at 2009-01-21 06:46:14",
    "created_at": "2009-01-21T06:46:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2942#issuecomment-20223",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [scripts-2942.patch](tarball://root/attachments/some-uuid/ticket2942/scripts-2942.patch) by TimothyClemans created at 2009-01-21 06:46:14



---

archive/issue_comments_020224.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-21T06:47:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2942#issuecomment-20224",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_020225.json:
```json
{
    "body": "This patch makes 'sage -b' run the notebook!  Not cool.",
    "created_at": "2009-01-21T19:15:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2942#issuecomment-20225",
    "user": "https://github.com/ncalexan"
}
```

This patch makes 'sage -b' run the notebook!  Not cool.



---

archive/issue_comments_020226.json:
```json
{
    "body": "Added commands -n and -bn",
    "created_at": "2009-11-30T05:59:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2942#issuecomment-20226",
    "user": "https://github.com/TimDumol"
}
```

Added commands -n and -bn



---

archive/issue_comments_020227.json:
```json
{
    "body": "Attachment [trac_2942-n-and-nb-commandline-opts.patch](tarball://root/attachments/some-uuid/ticket2942/trac_2942-n-and-nb-commandline-opts.patch) by @TimDumol created at 2009-11-30 06:00:19\n\nThis patch should do the job.",
    "created_at": "2009-11-30T06:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2942#issuecomment-20227",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_2942-n-and-nb-commandline-opts.patch](tarball://root/attachments/some-uuid/ticket2942/trac_2942-n-and-nb-commandline-opts.patch) by @TimDumol created at 2009-11-30 06:00:19

This patch should do the job.



---

archive/issue_comments_020228.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-30T06:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2942#issuecomment-20228",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_020229.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-08T19:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2942#issuecomment-20229",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_020230.json:
```json
{
    "body": "Very, very nice.  It's especially nice how the build function is factored out.\n\nI doubt people will ever use \"sage -bn\", since the notebook is no longer in the sage library.  However, it can't hurt to have it.  I think \"sage -n\" will be very useful. \n\npositive review.",
    "created_at": "2009-12-08T19:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2942#issuecomment-20230",
    "user": "https://github.com/williamstein"
}
```

Very, very nice.  It's especially nice how the build function is factored out.

I doubt people will ever use "sage -bn", since the notebook is no longer in the sage library.  However, it can't hurt to have it.  I think "sage -n" will be very useful. 

positive review.



---

archive/issue_comments_020231.json:
```json
{
    "body": "Note to release manager -- this gets applied to the Sage scripts repo, and has nothing to do with the sagenb spkg.  Hence I'm changing the component to \"build\".",
    "created_at": "2009-12-08T19:26:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2942#issuecomment-20231",
    "user": "https://github.com/williamstein"
}
```

Note to release manager -- this gets applied to the Sage scripts repo, and has nothing to do with the sagenb spkg.  Hence I'm changing the component to "build".



---

archive/issue_comments_020232.json:
```json
{
    "body": "Changing component from notebook to build.",
    "created_at": "2009-12-08T19:26:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2942#issuecomment-20232",
    "user": "https://github.com/williamstein"
}
```

Changing component from notebook to build.



---

archive/issue_events_003146.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-12-09T02:36:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2942",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2942#event-3146"
}
```



---

archive/issue_comments_020233.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-09T02:36:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2942#issuecomment-20233",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
