# Issue 9599: re-merge #1396 and insure that Sage starts on t2.math

archive/issues_009599.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @wjp simonking @malb @jhpalmieri\n\nA patch at #1396 was merged in 4.5.2.alpha0, but that caused Sage to segfault when starting on t2.math. That ticket was backed out in 4.5.2.alpha1, and should be re-merged. See #9583 for discussion.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9599\n\n",
    "created_at": "2010-07-26T08:14:06Z",
    "labels": [
        "porting: Solaris",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "re-merge #1396 and insure that Sage starts on t2.math",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9599",
    "user": "@dandrake"
}
```
Assignee: drkirkby

CC:  @wjp simonking @malb @jhpalmieri

A patch at #1396 was merged in 4.5.2.alpha0, but that caused Sage to segfault when starting on t2.math. That ticket was backed out in 4.5.2.alpha1, and should be re-merged. See #9583 for discussion.

Issue created by migration from https://trac.sagemath.org/ticket/9599





---

archive/issue_comments_092880.json:
```json
{
    "body": "To summarize the lengthy discussion on #9583:\n\n#1396 exposed a symbol clash between Singular and Pari with some linkers.\n\nTo fix this, we rename Singular's `mu` to `Kstd1_mu`. This could be done either with the SPKG at #9583 which changes only this, or with the SPKG at #8059 which upgrades Singular to a new version that includes the renamed `mu`.",
    "created_at": "2010-07-26T08:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9599#issuecomment-92880",
    "user": "@wjp"
}
```

To summarize the lengthy discussion on #9583:

#1396 exposed a symbol clash between Singular and Pari with some linkers.

To fix this, we rename Singular's `mu` to `Kstd1_mu`. This could be done either with the SPKG at #9583 which changes only this, or with the SPKG at #8059 which upgrades Singular to a new version that includes the renamed `mu`.



---

archive/issue_comments_092881.json:
```json
{
    "body": "See\n\n\u00a0http://groups.google.com/group/libsingular-devel/browse_thread/thread/e49fe19e034ec774\n\nfor upstream's reaction.",
    "created_at": "2010-07-28T12:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9599#issuecomment-92881",
    "user": "@malb"
}
```

See

 http://groups.google.com/group/libsingular-devel/browse_thread/thread/e49fe19e034ec774

for upstream's reaction.



---

archive/issue_comments_092882.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-08T15:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9599#issuecomment-92882",
    "user": "@malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092883.json:
```json
{
    "body": "The rebased patch passes doctests for me. It still needs testing on t2.",
    "created_at": "2011-01-08T15:19:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9599#issuecomment-92883",
    "user": "@malb"
}
```

The rebased patch passes doctests for me. It still needs testing on t2.



---

archive/issue_comments_092884.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-13T09:34:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9599#issuecomment-92884",
    "user": "@malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092885.json:
```json
{
    "body": "The patch applies fine to 4.6.1.rc1 and doctests pass on t2, except:\n\n\n```\nsage -t  -long -force_lib devel/sage/sage/tests/cmdline.py # 19 doctests failed, timeouts\nsage -t  -long -force_lib devel/sage/sage/parallel/decorate.py # 1 doctests failed, OSError: [Errno 12] Not enough space\nsage -t  -long -force_lib devel/sage/sage/misc/trace.py # 2 doctests failed, \n```\n\n\nThese don't seem related to this patch.\n\nThe patch did have a positive review before and the only issue was a SIGSEGV on startup on t2. I'll thus set this patch to a positive review.",
    "created_at": "2011-01-13T09:34:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9599#issuecomment-92885",
    "user": "@malb"
}
```

The patch applies fine to 4.6.1.rc1 and doctests pass on t2, except:


```
sage -t  -long -force_lib devel/sage/sage/tests/cmdline.py # 19 doctests failed, timeouts
sage -t  -long -force_lib devel/sage/sage/parallel/decorate.py # 1 doctests failed, OSError: [Errno 12] Not enough space
sage -t  -long -force_lib devel/sage/sage/misc/trace.py # 2 doctests failed, 
```


These don't seem related to this patch.

The patch did have a positive review before and the only issue was a SIGSEGV on startup on t2. I'll thus set this patch to a positive review.



---

archive/issue_comments_092886.json:
```json
{
    "body": "Is there a reason the milestone is sage-5.0?",
    "created_at": "2011-01-23T20:31:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9599#issuecomment-92886",
    "user": "@jdemeyer"
}
```

Is there a reason the milestone is sage-5.0?



---

archive/issue_comments_092887.json:
```json
{
    "body": "No :)",
    "created_at": "2011-01-23T21:27:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9599#issuecomment-92887",
    "user": "@malb"
}
```

No :)



---

archive/issue_comments_092888.json:
```json
{
    "body": "The commit message will have to be changed to reflect number, also you should split it over multiple lines if it's that long (but make sure the first line makes sense by itself).",
    "created_at": "2011-01-26T18:39:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9599#issuecomment-92888",
    "user": "@jdemeyer"
}
```

The commit message will have to be changed to reflect number, also you should split it over multiple lines if it's that long (but make sure the first line makes sense by itself).



---

archive/issue_comments_092889.json:
```json
{
    "body": "Attachment [trac_9599.patch](tarball://root/attachments/some-uuid/ticket9599/trac_9599.patch) by @malb created at 2011-01-26 20:22:11",
    "created_at": "2011-01-26T20:22:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9599#issuecomment-92889",
    "user": "@malb"
}
```

Attachment [trac_9599.patch](tarball://root/attachments/some-uuid/ticket9599/trac_9599.patch) by @malb created at 2011-01-26 20:22:11



---

archive/issue_comments_092890.json:
```json
{
    "body": "done",
    "created_at": "2011-01-26T20:24:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9599#issuecomment-92890",
    "user": "@malb"
}
```

done



---

archive/issue_comments_092891.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-27T13:14:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9599",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9599#issuecomment-92891",
    "user": "@jdemeyer"
}
```

Resolution: fixed
