# Issue 9601: Fix cvxopt on FreeBSD

archive/issues_009601.json:
```json
{
    "body": "Assignee: pjeremy\n\ncvxopt requires C99 math functions that are not part of the base FreeBSD libraries.  #9543 uses cephes to provide these missing functions but referencing them requires that cvxopt search $SAGE_LOCAL/include.  The attached patch modified spkg-install to\ninclude this.\n\nThis patch is local to Sage and does not need to be reported upstream.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9601\n\n",
    "created_at": "2010-07-26T11:12:31Z",
    "labels": [
        "porting: BSD",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Fix cvxopt on FreeBSD",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9601",
    "user": "pjeremy"
}
```
Assignee: pjeremy

cvxopt requires C99 math functions that are not part of the base FreeBSD libraries.  #9543 uses cephes to provide these missing functions but referencing them requires that cvxopt search $SAGE_LOCAL/include.  The attached patch modified spkg-install to
include this.

This patch is local to Sage and does not need to be reported upstream.

Issue created by migration from https://trac.sagemath.org/ticket/9601





---

archive/issue_comments_092921.json:
```json
{
    "body": "Attachment [cvxopt-0.9.p8.patch](tarball://root/attachments/some-uuid/ticket9601/cvxopt-0.9.p8.patch) by schilly created at 2010-07-27 13:53:48\n\nhi, i think this should be coordinated with #6456",
    "created_at": "2010-07-27T13:53:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9601#issuecomment-92921",
    "user": "schilly"
}
```

Attachment [cvxopt-0.9.p8.patch](tarball://root/attachments/some-uuid/ticket9601/cvxopt-0.9.p8.patch) by schilly created at 2010-07-27 13:53:48

hi, i think this should be coordinated with #6456



---

archive/issue_comments_092922.json:
```json
{
    "body": "An equivalent patch for cvxopt-1.1.2.p1 has been attached to #6456.  On the assumption that the newer cvxopt will supplant cvxopt-0.9, this ticket can be closed.",
    "created_at": "2010-07-27T23:03:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9601#issuecomment-92922",
    "user": "pjeremy"
}
```

An equivalent patch for cvxopt-1.1.2.p1 has been attached to #6456.  On the assumption that the newer cvxopt will supplant cvxopt-0.9, this ticket can be closed.



---

archive/issue_comments_092923.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-28T01:00:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9601#issuecomment-92923",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092924.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-28T01:00:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9601#issuecomment-92924",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092925.json:
```json
{
    "body": "Whilst I realise this should be coordinated with #6456, I thought it wise that this got positive review first, to make merging easier. \n\nThe fix is clearly FreeBSD specific, so will not impact any other system.",
    "created_at": "2010-07-28T01:02:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9601#issuecomment-92925",
    "user": "drkirkby"
}
```

Whilst I realise this should be coordinated with #6456, I thought it wise that this got positive review first, to make merging easier. 

The fix is clearly FreeBSD specific, so will not impact any other system.



---

archive/issue_comments_092926.json:
```json
{
    "body": "There hasn't been very recent activity at #6456.  Does it make sense to put together a new p10 (based on the p9 in 4.6.alpha2), so we can merge this ticket?",
    "created_at": "2010-10-03T09:35:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9601#issuecomment-92926",
    "user": "mpatel"
}
```

There hasn't been very recent activity at #6456.  Does it make sense to put together a new p10 (based on the p9 in 4.6.alpha2), so we can merge this ticket?



---

archive/issue_comments_092927.json:
```json
{
    "body": "I've just done some more work on #6456.",
    "created_at": "2010-10-12T00:35:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9601#issuecomment-92927",
    "user": "mhansen"
}
```

I've just done some more work on #6456.



---

archive/issue_comments_092928.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-10-25T03:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9601#issuecomment-92928",
    "user": "mpatel"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_092929.json:
```json
{
    "body": "This ticket is not actionable without an updated spkg or a positive review at #6456, so I'm changing the status to \"needs work\".",
    "created_at": "2010-10-25T03:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9601#issuecomment-92929",
    "user": "mpatel"
}
```

This ticket is not actionable without an updated spkg or a positive review at #6456, so I'm changing the status to "needs work".



---

archive/issue_comments_092930.json:
```json
{
    "body": "Apparently [Stephen Montgomery-Smith](http://groups.google.com/group/sage-devel/browse_thread/thread/2feec7c5511c4ae5/857a00a9aa271f17) has had some success with this recently as a \"port\"",
    "created_at": "2012-01-31T02:04:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9601#issuecomment-92930",
    "user": "kcrisman"
}
```

Apparently [Stephen Montgomery-Smith](http://groups.google.com/group/sage-devel/browse_thread/thread/2feec7c5511c4ae5/857a00a9aa271f17) has had some success with this recently as a "port"



---

archive/issue_comments_092931.json:
```json
{
    "body": "Is anyone working on the FreeBSD port now? I'm not aware of Peter working on it. I think he got a bit fed up with what he called the \n\n\"release it now, we'll make it work later\" mentality.\n\n(They are Peter's words, not mine. See #9601.)\n\nDave",
    "created_at": "2012-01-31T21:53:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9601#issuecomment-92931",
    "user": "drkirkby"
}
```

Is anyone working on the FreeBSD port now? I'm not aware of Peter working on it. I think he got a bit fed up with what he called the 

"release it now, we'll make it work later" mentality.

(They are Peter's words, not mine. See #9601.)

Dave



---

archive/issue_comments_092932.json:
```json
{
    "body": "Replying to [comment:10 drkirkby]:\n> Is anyone working on the FreeBSD port now? I'm not aware of Peter working on it. I think he got a bit fed up with what he called the \n> \n> \"release it now, we'll make it work later\" mentality.\n> \n> (They are Peter's words, not mine. See #9601.)\n> \n> Dave \n\nOops, Peter put his comments on #6456, not #9601 which is this ticket! \n\nDave.",
    "created_at": "2012-01-31T21:55:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9601#issuecomment-92932",
    "user": "drkirkby"
}
```

Replying to [comment:10 drkirkby]:
> Is anyone working on the FreeBSD port now? I'm not aware of Peter working on it. I think he got a bit fed up with what he called the 
> 
> "release it now, we'll make it work later" mentality.
> 
> (They are Peter's words, not mine. See #9601.)
> 
> Dave 

Oops, Peter put his comments on #6456, not #9601 which is this ticket! 

Dave.



---

archive/issue_comments_092933.json:
```json
{
    "body": "> > Is anyone working on the FreeBSD port now? I'm not aware of Peter working on it. I think he got a bit fed up with what he \nWell, a friend of one of the WeBWorK developers did manage to make a Sage that passed most tests not too long ago.   See the link in comment:9.",
    "created_at": "2012-02-01T01:46:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9601#issuecomment-92933",
    "user": "kcrisman"
}
```

> > Is anyone working on the FreeBSD port now? I'm not aware of Peter working on it. I think he got a bit fed up with what he 
Well, a friend of one of the WeBWorK developers did manage to make a Sage that passed most tests not too long ago.   See the link in comment:9.



---

archive/issue_comments_092934.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-05-28T08:08:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9601#issuecomment-92934",
    "user": "mhansen"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_092935.json:
```json
{
    "body": "I think this can be closed now since this is in the current cvxopt.",
    "created_at": "2012-05-28T08:08:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9601#issuecomment-92935",
    "user": "mhansen"
}
```

I think this can be closed now since this is in the current cvxopt.



---

archive/issue_comments_092936.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd40.5\".",
    "created_at": "2012-05-28T08:08:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9601#issuecomment-92936",
    "user": "mhansen"
}
```

Changing keywords from "" to "sd40.5".



---

archive/issue_comments_092937.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-06-02T12:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9601",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9601#issuecomment-92937",
    "user": "jdemeyer"
}
```

Resolution: duplicate
