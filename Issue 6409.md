# Issue 6409: srange inconsistent when including endpoints

archive/issues_006409.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  robertwb craigcitro\n\n\n```\nsage: srange(1,0,include_endpoint=True)\n[]\nsage: srange(1,QQ(0),include_endpoint=True)\n[0]\n```\n\n\nThese two should agree on something.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6409\n\n",
    "created_at": "2009-06-25T16:12:42Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "srange inconsistent when including endpoints",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6409",
    "user": "malb"
}
```
Assignee: somebody

CC:  robertwb craigcitro


```
sage: srange(1,0,include_endpoint=True)
[]
sage: srange(1,QQ(0),include_endpoint=True)
[0]
```


These two should agree on something.

Issue created by migration from https://trac.sagemath.org/ticket/6409





---

archive/issue_comments_051457.json:
```json
{
    "body": "Fixed srange problem. I used xsrange for some cases, which also had the same bug, so I modified xsrange as well. I added some doctests, and tested the speed. It is as fast as the old code for common calls.",
    "created_at": "2010-05-24T23:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6409#issuecomment-51457",
    "user": "mjordan7"
}
```

Fixed srange problem. I used xsrange for some cases, which also had the same bug, so I modified xsrange as well. I added some doctests, and tested the speed. It is as fast as the old code for common calls.



---

archive/issue_comments_051458.json:
```json
{
    "body": "Changing keywords from \"\" to \"srange\".",
    "created_at": "2010-05-24T23:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6409#issuecomment-51458",
    "user": "mjordan7"
}
```

Changing keywords from "" to "srange".



---

archive/issue_comments_051459.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-24T23:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6409#issuecomment-51459",
    "user": "mjordan7"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_051460.json:
```json
{
    "body": "Looks good, but I have made a superficial review with a rebase to 4.4.3, doctest passes, I will check better before giving positive review.",
    "created_at": "2010-06-22T15:49:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6409#issuecomment-51460",
    "user": "lftabera"
}
```

Looks good, but I have made a superficial review with a rebase to 4.4.3, doctest passes, I will check better before giving positive review.



---

archive/issue_comments_051461.json:
```json
{
    "body": "Changed last line of srange, positive review\n\nnew patch the previous one did not apply to a clean sage installation",
    "created_at": "2010-06-24T10:52:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6409#issuecomment-51461",
    "user": "lftabera"
}
```

Changed last line of srange, positive review

new patch the previous one did not apply to a clean sage installation



---

archive/issue_comments_051462.json:
```json
{
    "body": "Attachment [trac_6409.3.patch](tarball://root/attachments/some-uuid/ticket6409/trac_6409.3.patch) by lftabera created at 2010-06-24 10:53:17",
    "created_at": "2010-06-24T10:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6409#issuecomment-51462",
    "user": "lftabera"
}
```

Attachment [trac_6409.3.patch](tarball://root/attachments/some-uuid/ticket6409/trac_6409.3.patch) by lftabera created at 2010-06-24 10:53:17



---

archive/issue_comments_051463.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-24T19:03:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6409#issuecomment-51463",
    "user": "robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_051464.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-06-28T21:30:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6409#issuecomment-51464",
    "user": "rlm"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_051465.json:
```json
{
    "body": "Please tell the release manager which patches to apply. It is not clear here.\n\n-- RLM + SD MSRI tutorial audience :)",
    "created_at": "2010-06-28T21:30:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6409#issuecomment-51465",
    "user": "rlm"
}
```

Please tell the release manager which patches to apply. It is not clear here.

-- RLM + SD MSRI tutorial audience :)



---

archive/issue_comments_051466.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-06-28T23:28:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6409#issuecomment-51466",
    "user": "rlm"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_051467.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-06-28T23:42:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6409#issuecomment-51467",
    "user": "rlm"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_051468.json:
```json
{
    "body": "I was just being overly pedantic to demonstrate how to work with the trac server. I'll delete the older patches.",
    "created_at": "2010-06-28T23:42:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6409#issuecomment-51468",
    "user": "rlm"
}
```

I was just being overly pedantic to demonstrate how to work with the trac server. I'll delete the older patches.



---

archive/issue_comments_051469.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-28T23:43:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6409#issuecomment-51469",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_051470.json:
```json
{
    "body": "It's conventional to put full names, not trac usernames, in the Author and Reviewer fields (as these are used to assemble the release notes). I'm assuming mjordan7 is Mark Jordan.",
    "created_at": "2010-06-29T16:09:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6409#issuecomment-51470",
    "user": "davidloeffler"
}
```

It's conventional to put full names, not trac usernames, in the Author and Reviewer fields (as these are used to assemble the release notes). I'm assuming mjordan7 is Mark Jordan.



---

archive/issue_comments_051471.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T09:17:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6409",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6409#issuecomment-51471",
    "user": "mpatel"
}
```

Resolution: fixed
