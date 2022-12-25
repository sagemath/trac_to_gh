# Issue 7678: shorten very long doctests in rings/arith.py

archive/issues_007678.json:
```json
{
    "body": "Assignee: tbd\n\nOn sage.math, before the patch:\n\n\n```\nsage -t -long \"devel/sage-main/sage/rings/arith.py\"         \n         [162.6 s]\n```\n\n\nAnd after the patch:\n\n\n```\nsage -t -long \"devel/sage-main/sage/rings/arith.py\"         \n         [50.2 s]\n```\n\n\nI'm putting the milestone as 4.3 only because this is almost certainly not going to break anything whatsoever.  Please change it to 4.3.1 if you think that's more appropriate.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7678\n\n",
    "created_at": "2009-12-13T22:32:51Z",
    "labels": [
        "component: doctest coverage",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "shorten very long doctests in rings/arith.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7678",
    "user": "https://github.com/aghitza"
}
```
Assignee: tbd

On sage.math, before the patch:


```
sage -t -long "devel/sage-main/sage/rings/arith.py"         
         [162.6 s]
```


And after the patch:


```
sage -t -long "devel/sage-main/sage/rings/arith.py"         
         [50.2 s]
```


I'm putting the milestone as 4.3 only because this is almost certainly not going to break anything whatsoever.  Please change it to 4.3.1 if you think that's more appropriate.


Issue created by migration from https://trac.sagemath.org/ticket/7678





---

archive/issue_comments_065738.json:
```json
{
    "body": "Attachment [trac_7678.patch](tarball://root/attachments/some-uuid/ticket7678/trac_7678.patch) by @aghitza created at 2009-12-13 22:34:17",
    "created_at": "2009-12-13T22:34:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7678#issuecomment-65738",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_7678.patch](tarball://root/attachments/some-uuid/ticket7678/trac_7678.patch) by @aghitza created at 2009-12-13 22:34:17



---

archive/issue_comments_065739.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-13T22:34:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7678#issuecomment-65739",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065740.json:
```json
{
    "body": "I see what you did here: (1) you removed tha 'gap' algorithm from the test, presumably because it was slowest, and (2) instead of testing all i in each of the ranges 2 to 2255 and 2256 to  5000 you pick 500 random indices from those ranges and use those.\n\nI don't think that strategy (2) is a good idea, since if this test ever fails it will be hard to find out exactly where (i.e. for which i).  The tests in our standard test suite should surely be deterministic.  What I did in a similar situation was to once and for all pick a random set of indices, and make the doctest test those indices only.  This does not prevent us from having a more strenuous test to do on occasion, I am only proposing limiting what happens every time the whole of Sage is tested.\n\nFor that reason (only) I have put this as \"needs work\", and will post to sage-devel so that others who commented on your observation can come and have their say.",
    "created_at": "2009-12-14T15:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7678#issuecomment-65740",
    "user": "https://github.com/JohnCremona"
}
```

I see what you did here: (1) you removed tha 'gap' algorithm from the test, presumably because it was slowest, and (2) instead of testing all i in each of the ranges 2 to 2255 and 2256 to  5000 you pick 500 random indices from those ranges and use those.

I don't think that strategy (2) is a good idea, since if this test ever fails it will be hard to find out exactly where (i.e. for which i).  The tests in our standard test suite should surely be deterministic.  What I did in a similar situation was to once and for all pick a random set of indices, and make the doctest test those indices only.  This does not prevent us from having a more strenuous test to do on occasion, I am only proposing limiting what happens every time the whole of Sage is tested.

For that reason (only) I have put this as "needs work", and will post to sage-devel so that others who commented on your observation can come and have their say.



---

archive/issue_comments_065741.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-14T15:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7678#issuecomment-65741",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_065742.json:
```json
{
    "body": "All of the random seeds are set at the beginning of the doctest, so it would be deterministic.",
    "created_at": "2009-12-14T15:33:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7678#issuecomment-65742",
    "user": "https://github.com/mwhansen"
}
```

All of the random seeds are set at the beginning of the doctest, so it would be deterministic.



---

archive/issue_comments_065743.json:
```json
{
    "body": "In that case I'm changing this to \"positive review\".  Except that I can't, there is no such button below!",
    "created_at": "2009-12-14T16:49:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7678#issuecomment-65743",
    "user": "https://github.com/JohnCremona"
}
```

In that case I'm changing this to "positive review".  Except that I can't, there is no such button below!



---

archive/issue_comments_065744.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-14T19:43:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7678#issuecomment-65744",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_065745.json:
```json
{
    "body": "Can't give a positive review until it needs a review.",
    "created_at": "2009-12-14T19:43:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7678#issuecomment-65745",
    "user": "https://github.com/robertwb"
}
```

Can't give a positive review until it needs a review.



---

archive/issue_comments_065746.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-14T19:43:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7678#issuecomment-65746",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065747.json:
```json
{
    "body": "Replying to [comment:2 cremona]:\n> I see what you did here: (1) you removed tha 'gap' algorithm from the test, presumably because it was slowest\n\nActually, the splitting into range(2, 2255) including 'gap' and range(2256, 5000) excluding 'gap' was there before I touched this, and it was indeed because gap gets rather slow at doing this computation.  The only real change I made was to pick 500 integers in each range instead of testing the whole range.",
    "created_at": "2009-12-14T21:25:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7678#issuecomment-65747",
    "user": "https://github.com/aghitza"
}
```

Replying to [comment:2 cremona]:
> I see what you did here: (1) you removed tha 'gap' algorithm from the test, presumably because it was slowest

Actually, the splitting into range(2, 2255) including 'gap' and range(2256, 5000) excluding 'gap' was there before I touched this, and it was indeed because gap gets rather slow at doing this computation.  The only real change I made was to pick 500 integers in each range instead of testing the whole range.



---

archive/issue_comments_065748.json:
```json
{
    "body": "Attachment [trac_7678.2.patch](tarball://root/attachments/some-uuid/ticket7678/trac_7678.2.patch) by @aghitza created at 2009-12-14 21:30:33",
    "created_at": "2009-12-14T21:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7678#issuecomment-65748",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_7678.2.patch](tarball://root/attachments/some-uuid/ticket7678/trac_7678.2.patch) by @aghitza created at 2009-12-14 21:30:33



---

archive/issue_comments_065749.json:
```json
{
    "body": "I did something stupid in the first patch though, namely to remove `#long time` from two doctests that depend on previous long time computations.  This of course has no effect on `sage -t -long` but it breaks `sage -t`.  (Note to self: should test with and without -long in the future.)\n\nApply only the new patch, which fixes this.  And I guess this should technically be reviewed again.",
    "created_at": "2009-12-14T21:33:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7678#issuecomment-65749",
    "user": "https://github.com/aghitza"
}
```

I did something stupid in the first patch though, namely to remove `#long time` from two doctests that depend on previous long time computations.  This of course has no effect on `sage -t -long` but it breaks `sage -t`.  (Note to self: should test with and without -long in the future.)

Apply only the new patch, which fixes this.  And I guess this should technically be reviewed again.



---

archive/issue_comments_065750.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-12-14T21:33:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7678#issuecomment-65750",
    "user": "https://github.com/aghitza"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_065751.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-14T21:33:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7678#issuecomment-65751",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_065752.json:
```json
{
    "body": "That's very odd since I definitely ran the test with and without -long.  I'll have to do it again.",
    "created_at": "2009-12-14T22:32:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7678#issuecomment-65752",
    "user": "https://github.com/JohnCremona"
}
```

That's very odd since I definitely ran the test with and without -long.  I'll have to do it again.



---

archive/issue_comments_065753.json:
```json
{
    "body": "I did it again (eventually) and am now happy to give this a positive review.",
    "created_at": "2009-12-30T15:46:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7678#issuecomment-65753",
    "user": "https://github.com/JohnCremona"
}
```

I did it again (eventually) and am now happy to give this a positive review.



---

archive/issue_comments_065754.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-30T15:46:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7678#issuecomment-65754",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065755.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-03T22:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7678#issuecomment-65755",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_007897.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2010-01-03T22:16:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7678",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7678#event-7897"
}
```
