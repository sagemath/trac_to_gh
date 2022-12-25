# Issue 7743: Piecewise integration fixes [with patch; needs review]

archive/issues_007743.json:
```json
{
    "body": "Assignee: @aghitza\n\nKeywords: integration\n\nThis patch fixes two issues with the piecewise class, brought up in this sage-support thread:\n\nhttp://groups.google.com/group/sage-support/browse_thread/thread/18d830ece7826898/86c401e4d6b8f3dd\n\nThe first issue is that when a piece of the function belongs to the Integer ring, integration doesn't work. This is fixed by coercing each piece to the symbolic expression ring.\n\nThe second issue is that there are cases where maxima needs to be given assumptions about the domain of x for the piece being integrated. This is fixed with the assume and forget functions.\n\nAdditional unit tests have been added (or existing tests modified) for each issue.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7743\n\n",
    "created_at": "2009-12-19T22:52:08Z",
    "labels": [
        "component: algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Piecewise integration fixes [with patch; needs review]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7743",
    "user": "https://trac.sagemath.org/admin/accounts/users/pbutler"
}
```
Assignee: @aghitza

Keywords: integration

This patch fixes two issues with the piecewise class, brought up in this sage-support thread:

http://groups.google.com/group/sage-support/browse_thread/thread/18d830ece7826898/86c401e4d6b8f3dd

The first issue is that when a piece of the function belongs to the Integer ring, integration doesn't work. This is fixed by coercing each piece to the symbolic expression ring.

The second issue is that there are cases where maxima needs to be given assumptions about the domain of x for the piece being integrated. This is fixed with the assume and forget functions.

Additional unit tests have been added (or existing tests modified) for each issue.

Issue created by migration from https://trac.sagemath.org/ticket/7743





---

archive/issue_comments_066490.json:
```json
{
    "body": "Attachment [12159.patch](tarball://root/attachments/some-uuid/ticket7743/12159.patch) by @aghitza created at 2009-12-19 23:36:02",
    "created_at": "2009-12-19T23:36:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7743#issuecomment-66490",
    "user": "https://github.com/aghitza"
}
```

Attachment [12159.patch](tarball://root/attachments/some-uuid/ticket7743/12159.patch) by @aghitza created at 2009-12-19 23:36:02



---

archive/issue_comments_066491.json:
```json
{
    "body": "Changing component from algebra to calculus.",
    "created_at": "2009-12-19T23:36:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7743#issuecomment-66491",
    "user": "https://github.com/aghitza"
}
```

Changing component from algebra to calculus.



---

archive/issue_comments_066492.json:
```json
{
    "body": "Changing assignee from @aghitza to @burcin.",
    "created_at": "2009-12-19T23:36:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7743#issuecomment-66492",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from @aghitza to @burcin.



---

archive/issue_comments_066493.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2009-12-20T13:33:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7743#issuecomment-66493",
    "user": "https://github.com/wdjoyner"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_066494.json:
```json
{
    "body": "This patch failed to apply to sage-4.3.a1 and 4.3.rc0. Maybe it needs rebasing?",
    "created_at": "2009-12-20T13:33:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7743#issuecomment-66494",
    "user": "https://github.com/wdjoyner"
}
```

This patch failed to apply to sage-4.3.a1 and 4.3.rc0. Maybe it needs rebasing?



---

archive/issue_comments_066495.json:
```json
{
    "body": "Attachment [13311.patch](tarball://root/attachments/some-uuid/ticket7743/13311.patch) by pbutler created at 2009-12-20 17:03:46",
    "created_at": "2009-12-20T17:03:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7743#issuecomment-66495",
    "user": "https://trac.sagemath.org/admin/accounts/users/pbutler"
}
```

Attachment [13311.patch](tarball://root/attachments/some-uuid/ticket7743/13311.patch) by pbutler created at 2009-12-20 17:03:46



---

archive/issue_comments_066496.json:
```json
{
    "body": "My mistake; I was using a much older version of sage. I've attached another patch that should apply to sage-4.2, but I'm not sure to actually obtain the latest development version of sage-4.3 for testing. Is there documentation on this somewhere?",
    "created_at": "2009-12-20T17:10:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7743#issuecomment-66496",
    "user": "https://trac.sagemath.org/admin/accounts/users/pbutler"
}
```

My mistake; I was using a much older version of sage. I've attached another patch that should apply to sage-4.2, but I'm not sure to actually obtain the latest development version of sage-4.3 for testing. Is there documentation on this somewhere?



---

archive/issue_comments_066497.json:
```json
{
    "body": "Replying to [comment:3 pbutler]:\n> My mistake; I was using a much older version of sage. I've attached another \n> patch that should apply to sage-4.2, but I'm not sure to actually obtain \n\n\n\nThis doesn't work either.\n\n> the latest development version of sage-4.3 for testing. Is there documentation \n> on this somewhere?\n\n\nI sent you the link by separate email to your gmail address.",
    "created_at": "2009-12-21T02:10:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7743#issuecomment-66497",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:3 pbutler]:
> My mistake; I was using a much older version of sage. I've attached another 
> patch that should apply to sage-4.2, but I'm not sure to actually obtain 



This doesn't work either.

> the latest development version of sage-4.3 for testing. Is there documentation 
> on this somewhere?


I sent you the link by separate email to your gmail address.



---

archive/issue_events_018520.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-12-24T07:06:42Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7743",
    "milestone": "sage-4.3.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7743#event-18520"
}
```



---

archive/issue_comments_066498.json:
```json
{
    "body": "I'm declaring a total feature freeze on sage-4.3.",
    "created_at": "2009-12-24T07:06:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7743#issuecomment-66498",
    "user": "https://github.com/williamstein"
}
```

I'm declaring a total feature freeze on sage-4.3.



---

archive/issue_comments_066499.json:
```json
{
    "body": "Attachment [13535.patch](tarball://root/attachments/some-uuid/ticket7743/13535.patch) by pbutler created at 2010-01-06 05:06:41",
    "created_at": "2010-01-06T05:06:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7743#issuecomment-66499",
    "user": "https://trac.sagemath.org/admin/accounts/users/pbutler"
}
```

Attachment [13535.patch](tarball://root/attachments/some-uuid/ticket7743/13535.patch) by pbutler created at 2010-01-06 05:06:41



---

archive/issue_comments_066500.json:
```json
{
    "body": "I've attached 13535.patch and tested that it can be applied on sage 4.3, but it doesn't look much different from the previous one (aside from a try/except that I had to add because of a change to the behaviour of `assume`). If it still doesn't apply, could you paste the shell transcript?",
    "created_at": "2010-01-06T06:03:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7743#issuecomment-66500",
    "user": "https://trac.sagemath.org/admin/accounts/users/pbutler"
}
```

I've attached 13535.patch and tested that it can be applied on sage 4.3, but it doesn't look much different from the previous one (aside from a try/except that I had to add because of a change to the behaviour of `assume`). If it still doesn't apply, could you paste the shell transcript?



---

archive/issue_comments_066501.json:
```json
{
    "body": "Thanks, I'll review it.",
    "created_at": "2010-01-06T23:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7743#issuecomment-66501",
    "user": "https://github.com/wdjoyner"
}
```

Thanks, I'll review it.



---

archive/issue_comments_066502.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-06T23:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7743#issuecomment-66502",
    "user": "https://github.com/wdjoyner"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066503.json:
```json
{
    "body": "Applies to 4.3.1.a0 (the hacked version) and 4.3. Passes all tests but sagedoc on 64bit ubuntu 9.10 with 4.3.1.a0\nand only with seemingly unrelated failures on imac 10.6.2 with 4.3.\n\nThanks for fixing this bug!\n\nPositive review.",
    "created_at": "2010-01-07T00:00:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7743#issuecomment-66503",
    "user": "https://github.com/wdjoyner"
}
```

Applies to 4.3.1.a0 (the hacked version) and 4.3. Passes all tests but sagedoc on 64bit ubuntu 9.10 with 4.3.1.a0
and only with seemingly unrelated failures on imac 10.6.2 with 4.3.

Thanks for fixing this bug!

Positive review.



---

archive/issue_comments_066504.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-07T00:00:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7743#issuecomment-66504",
    "user": "https://github.com/wdjoyner"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066505.json:
```json
{
    "body": "merged just 13535.patch",
    "created_at": "2010-01-13T09:12:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7743#issuecomment-66505",
    "user": "https://github.com/rlmill"
}
```

merged just 13535.patch



---

archive/issue_events_018521.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-13T09:12:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7743",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7743#event-18521"
}
```



---

archive/issue_comments_066506.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-13T09:12:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7743#issuecomment-66506",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
