# Issue 9086: LaTeX representation of negative symbolic fractions broken

archive/issues_009086.json:
```json
{
    "body": "Assignee: @burcin\n\nKeywords: symbolic fraction, sign, minus, latex\n\nWhen the numerator of a (negative) symbolic expression happens to be `1` (and only then), the sign is dropped in its LaTeX representation (but not its string representation):\n\n\n```\nsage: latex(-1/x)\n\\frac{1}{x}\nsage: latex(1/-x) \n\\frac{1}{x}\n```\n\n\nOrigin of the new doctest failure in `sage/graphs/generic_graphy.py`, introduced with Sage 4.4.3.alpha0.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9086\n\n",
    "created_at": "2010-05-29T18:44:54Z",
    "labels": [
        "component: symbolics",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.3",
    "title": "LaTeX representation of negative symbolic fractions broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9086",
    "user": "https://github.com/nexttime"
}
```
Assignee: @burcin

Keywords: symbolic fraction, sign, minus, latex

When the numerator of a (negative) symbolic expression happens to be `1` (and only then), the sign is dropped in its LaTeX representation (but not its string representation):


```
sage: latex(-1/x)
\frac{1}{x}
sage: latex(1/-x) 
\frac{1}{x}
```


Origin of the new doctest failure in `sage/graphs/generic_graphy.py`, introduced with Sage 4.4.3.alpha0.

Issue created by migration from https://trac.sagemath.org/ticket/9086





---

archive/issue_comments_084231.json:
```json
{
    "body": "Changing keywords from \"symbolic fraction, sign, minus, latex\" to \"symbolic fraction, sign, minus, latex, pynac\".",
    "created_at": "2010-05-29T18:59:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84231",
    "user": "https://github.com/burcin"
}
```

Changing keywords from "symbolic fraction, sign, minus, latex" to "symbolic fraction, sign, minus, latex, pynac".



---

archive/issue_comments_084232.json:
```json
{
    "body": "Thanks for tracking this down. This patch is the culprit:\n\nhttp://pynac.sagemath.org/hg/rev/cbd65a7dcf6a\n\n\nI will only be able to look at this after next weekend.",
    "created_at": "2010-05-29T18:59:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84232",
    "user": "https://github.com/burcin"
}
```

Thanks for tracking this down. This patch is the culprit:

http://pynac.sagemath.org/hg/rev/cbd65a7dcf6a


I will only be able to look at this after next weekend.



---

archive/issue_comments_084233.json:
```json
{
    "body": "Attachment [trac_9086.patch](tarball://root/attachments/some-uuid/ticket9086/trac_9086.patch) by @williamstein created at 2010-06-03 01:25:17\n\napply to sage library",
    "created_at": "2010-06-03T01:25:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84233",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_9086.patch](tarball://root/attachments/some-uuid/ticket9086/trac_9086.patch) by @williamstein created at 2010-06-03 01:25:17

apply to sage library



---

archive/issue_comments_084234.json:
```json
{
    "body": "Attachment [trac_9086-apply_to_pynac.patch](tarball://root/attachments/some-uuid/ticket9086/trac_9086-apply_to_pynac.patch) by @williamstein created at 2010-06-03 01:25:34\n\napply to src/ repo in pynac spkg",
    "created_at": "2010-06-03T01:25:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84234",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_9086-apply_to_pynac.patch](tarball://root/attachments/some-uuid/ticket9086/trac_9086-apply_to_pynac.patch) by @williamstein created at 2010-06-03 01:25:34

apply to src/ repo in pynac spkg



---

archive/issue_comments_084235.json:
```json
{
    "body": "The patch to the pynac spkg is long, but is logically nearly trivial.  I just copied some code for printing a sign, which Burcin forgot.\n\nThe patch to the sage library is merely to test that this is fixed. \n\nWilliam",
    "created_at": "2010-06-03T01:26:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84235",
    "user": "https://github.com/williamstein"
}
```

The patch to the pynac spkg is long, but is logically nearly trivial.  I just copied some code for printing a sign, which Burcin forgot.

The patch to the sage library is merely to test that this is fixed. 

William



---

archive/issue_comments_084236.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-03T01:26:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84236",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084237.json:
```json
{
    "body": "Changing priority from critical to blocker.",
    "created_at": "2010-06-03T01:26:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84237",
    "user": "https://github.com/williamstein"
}
```

Changing priority from critical to blocker.



---

archive/issue_comments_084238.json:
```json
{
    "body": "New spkg here:\n\n   http://sage.math.washington.edu/home/wstein/patches/pynac-0.2.0.p1.spkg",
    "created_at": "2010-06-03T01:28:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84238",
    "user": "https://github.com/williamstein"
}
```

New spkg here:

   http://sage.math.washington.edu/home/wstein/patches/pynac-0.2.0.p1.spkg



---

archive/issue_comments_084239.json:
```json
{
    "body": "This looks good to me and fixes the issue.  There was a change for #9037 that didn't get included in the spkg merged so far in 4.4.3 so I've included it at \n\nhttp://sage.math.washington.edu/home/mhansen/pynac-0.2.0.p1.spkg\n\nwhich should be used instead of the above link.",
    "created_at": "2010-06-03T01:43:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84239",
    "user": "https://github.com/mwhansen"
}
```

This looks good to me and fixes the issue.  There was a change for #9037 that didn't get included in the spkg merged so far in 4.4.3 so I've included it at 

http://sage.math.washington.edu/home/mhansen/pynac-0.2.0.p1.spkg

which should be used instead of the above link.



---

archive/issue_comments_084240.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-03T01:43:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84240",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084241.json:
```json
{
    "body": "Mike, Can you give #9037 a positive review?",
    "created_at": "2010-06-03T04:11:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84241",
    "user": "https://github.com/williamstein"
}
```

Mike, Can you give #9037 a positive review?



---

archive/issue_comments_084242.json:
```json
{
    "body": "Positive review up at #9037.",
    "created_at": "2010-06-03T04:19:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84242",
    "user": "https://github.com/mwhansen"
}
```

Positive review up at #9037.



---

archive/issue_events_022282.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-06-03T15:27:10Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "milestone": "sage-4.4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9086#event-22282"
}
```



---

archive/issue_comments_084243.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-03T16:01:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84243",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_022283.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-06-03T16:01:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9086#event-22283"
}
```



---

archive/issue_comments_084244.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-06-21T20:25:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84244",
    "user": "https://trac.sagemath.org/admin/accounts/users/damm"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_084245.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-06-21T20:25:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84245",
    "user": "https://trac.sagemath.org/admin/accounts/users/damm"
}
```

Changing status from closed to new.



---

archive/issue_events_022284.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/damm",
    "created_at": "2010-06-21T20:25:20Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9086#event-22284"
}
```



---

archive/issue_comments_084246.json:
```json
{
    "body": "Replying to [comment:10 damm]:\nSorry, i've changed the description and couldn't revert the change.\n\nI think the fix didn't solve all problems:\n\n\n```\nsage: var('x y')\nsage: latex(-x/y) \n\\frac{x}{y}\n```\n",
    "created_at": "2010-06-21T20:44:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84246",
    "user": "https://trac.sagemath.org/admin/accounts/users/damm"
}
```

Replying to [comment:10 damm]:
Sorry, i've changed the description and couldn't revert the change.

I think the fix didn't solve all problems:


```
sage: var('x y')
sage: latex(-x/y) 
\frac{x}{y}
```




---

archive/issue_comments_084247.json:
```json
{
    "body": "Replying to [comment:12 damm]:\n> I think the fix didn't solve all problems\n\nIndeed. Despite the ticket's name, I think this second case should be addressed on another ticket, since this one had already been merged.",
    "created_at": "2010-06-22T16:39:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84247",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:12 damm]:
> I think the fix didn't solve all problems

Indeed. Despite the ticket's name, I think this second case should be addressed on another ticket, since this one had already been merged.



---

archive/issue_comments_084248.json:
```json
{
    "body": "Done. http://trac.sagemath.org/sage_trac/ticket/9314",
    "created_at": "2010-06-22T18:22:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84248",
    "user": "https://trac.sagemath.org/admin/accounts/users/damm"
}
```

Done. http://trac.sagemath.org/sage_trac/ticket/9314



---

archive/issue_comments_084249.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-22T18:50:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9086#issuecomment-84249",
    "user": "https://github.com/nexttime"
}
```

Resolution: fixed



---

archive/issue_events_022285.json:
```json
{
    "actor": "https://github.com/nexttime",
    "created_at": "2010-06-22T18:50:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9086",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9086#event-22285"
}
```
