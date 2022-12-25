# Issue 9537: trial_division in Sage is really slow

archive/issues_009537.json:
```json
{
    "body": "Assignee: @aghitza\n\nSee my talk:\n*  http://wiki.sagemath.org/days24/schedule?action=AttachFile&do=view&target=stein-cython.pdf\n* http://sagenb.org/home/pub/2256/\n\nBasically, this sucks:\n\n```\nsage: n = 20110000038209\nsage: timeit('trial_division(n)')\n125 loops, best of 3: 2.75 ms per loop\n```\n\n\nEven in pure python one can easily implement this so it runs in about 650microseconds.  In C, it takes only 6 microseconds!\n\nIssue created by migration from https://trac.sagemath.org/ticket/9537\n\n",
    "created_at": "2010-07-18T14:31:40Z",
    "labels": [
        "component: basic arithmetic",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "trial_division in Sage is really slow",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9537",
    "user": "https://github.com/williamstein"
}
```
Assignee: @aghitza

See my talk:
*  http://wiki.sagemath.org/days24/schedule?action=AttachFile&do=view&target=stein-cython.pdf
* http://sagenb.org/home/pub/2256/

Basically, this sucks:

```
sage: n = 20110000038209
sage: timeit('trial_division(n)')
125 loops, best of 3: 2.75 ms per loop
```


Even in pure python one can easily implement this so it runs in about 650microseconds.  In C, it takes only 6 microseconds!

Issue created by migration from https://trac.sagemath.org/ticket/9537





---

archive/issue_comments_091739.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-18T19:22:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9537#issuecomment-91739",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091740.json:
```json
{
    "body": "good.",
    "created_at": "2010-07-18T19:44:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9537#issuecomment-91740",
    "user": "https://github.com/williamstein"
}
```

good.



---

archive/issue_comments_091741.json:
```json
{
    "body": "Attachment [trac_9537-fast_trial_division.patch](tarball://root/attachments/some-uuid/ticket9537/trac_9537-fast_trial_division.patch) by spancratz created at 2010-07-18 20:13:31",
    "created_at": "2010-07-18T20:13:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9537#issuecomment-91741",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Attachment [trac_9537-fast_trial_division.patch](tarball://root/attachments/some-uuid/ticket9537/trac_9537-fast_trial_division.patch) by spancratz created at 2010-07-18 20:13:31



---

archive/issue_comments_091742.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-18T20:13:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9537#issuecomment-91742",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091743.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T09:21:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9537#issuecomment-91743",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_009689.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-07-20T09:21:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9537",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9537#event-9689"
}
```
