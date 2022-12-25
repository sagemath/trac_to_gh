# Issue 4475: create a native Sage implementation of Dokchitser's L-functions algorithm

archive/issues_004475.json:
```json
{
    "body": "Assignee: @williamstein\n\nSee http://wiki.sagemath.org/days11/projects for now.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4475\n\n",
    "created_at": "2008-11-09T04:26:47Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "create a native Sage implementation of Dokchitser's L-functions algorithm",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4475",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

See http://wiki.sagemath.org/days11/projects for now.

Issue created by migration from https://trac.sagemath.org/ticket/4475





---

archive/issue_comments_032984.json:
```json
{
    "body": "Attachment [sage-4475.patch](tarball://root/attachments/some-uuid/ticket4475/sage-4475.patch) by @williamstein created at 2008-11-09 04:29:22\n\nfirst very preliminary version",
    "created_at": "2008-11-09T04:29:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4475#issuecomment-32984",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-4475.patch](tarball://root/attachments/some-uuid/ticket4475/sage-4475.patch) by @williamstein created at 2008-11-09 04:29:22

first very preliminary version



---

archive/issue_comments_032985.json:
```json
{
    "body": "Jen's original code which this work is based on was at #2568. Obviously Jen should get partial credit once the code from this ticket has been merged.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-09T06:55:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4475#issuecomment-32985",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Jen's original code which this work is based on was at #2568. Obviously Jen should get partial credit once the code from this ticket has been merged.

Cheers,

Michael



---

archive/issue_comments_032986.json:
```json
{
    "body": "Attachment [sage-4475-part3.patch](tarball://root/attachments/some-uuid/ticket4475/sage-4475-part3.patch) by @williamstein created at 2008-11-09 10:02:49",
    "created_at": "2008-11-09T10:02:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4475#issuecomment-32986",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-4475-part3.patch](tarball://root/attachments/some-uuid/ticket4475/sage-4475-part3.patch) by @williamstein created at 2008-11-09 10:02:49



---

archive/issue_comments_032987.json:
```json
{
    "body": "Attachment [sage-4475-part4.patch](tarball://root/attachments/some-uuid/ticket4475/sage-4475-part4.patch) by @williamstein created at 2008-11-18 00:18:42",
    "created_at": "2008-11-18T00:18:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4475#issuecomment-32987",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-4475-part4.patch](tarball://root/attachments/some-uuid/ticket4475/sage-4475-part4.patch) by @williamstein created at 2008-11-18 00:18:42



---

archive/issue_comments_032988.json:
```json
{
    "body": "Attachment [sage-4475-new_hope-part1.patch](tarball://root/attachments/some-uuid/ticket4475/sage-4475-new_hope-part1.patch) by @robertwb created at 2008-11-18 09:53:41",
    "created_at": "2008-11-18T09:53:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4475#issuecomment-32988",
    "user": "https://github.com/robertwb"
}
```

Attachment [sage-4475-new_hope-part1.patch](tarball://root/attachments/some-uuid/ticket4475/sage-4475-new_hope-part1.patch) by @robertwb created at 2008-11-18 09:53:41



---

archive/issue_comments_032989.json:
```json
{
    "body": "Attachment [sage-4475-new_hope-part2.patch](tarball://root/attachments/some-uuid/ticket4475/sage-4475-new_hope-part2.patch) by @robertwb created at 2008-11-18 10:02:13\n\nI attached a wrapping of the G_s(t) terms, and got it working (at least it computes the Riemann zeta function correctly). There is an off-by-one typo in formula (10) of the paper (the computation of the poles should be `rj k!/(pj - s)^(k+1)`). However, this fix still didn't give the right answer so I examined Dokchister's code and he has an extra summation over the poles (very last function of computel.gp) and I couldn't figure out where that was coming from. \n\nThe weight and the exponential factor are used for calculating the intermediate precision/number of terms needed in the various series related to computing G_s(t), which turns out to be the bulk of the work of `initLdata`, so it made things a lot cleaner to simply call that function for now. \n\nIt should be noted that to compute the value at s it may be necessary to compute the power series at s and then evaluate to let the poles and zeros of the gamma factor cancel out poles/zeros of L* appropriately.",
    "created_at": "2008-11-18T10:02:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4475#issuecomment-32989",
    "user": "https://github.com/robertwb"
}
```

Attachment [sage-4475-new_hope-part2.patch](tarball://root/attachments/some-uuid/ticket4475/sage-4475-new_hope-part2.patch) by @robertwb created at 2008-11-18 10:02:13

I attached a wrapping of the G_s(t) terms, and got it working (at least it computes the Riemann zeta function correctly). There is an off-by-one typo in formula (10) of the paper (the computation of the poles should be `rj k!/(pj - s)^(k+1)`). However, this fix still didn't give the right answer so I examined Dokchister's code and he has an extra summation over the poles (very last function of computel.gp) and I couldn't figure out where that was coming from. 

The weight and the exponential factor are used for calculating the intermediate precision/number of terms needed in the various series related to computing G_s(t), which turns out to be the bulk of the work of `initLdata`, so it made things a lot cleaner to simply call that function for now. 

It should be noted that to compute the value at s it may be necessary to compute the power series at s and then evaluate to let the poles and zeros of the gamma factor cancel out poles/zeros of L* appropriately.



---

archive/issue_comments_032990.json:
```json
{
    "body": "Attachment [sage-4475-new_hope-part3.patch](tarball://root/attachments/some-uuid/ticket4475/sage-4475-new_hope-part3.patch) by @robertwb created at 2008-12-20 05:26:49\n\n(Partial) native implementation of the G function.",
    "created_at": "2008-12-20T05:26:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4475",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4475#issuecomment-32990",
    "user": "https://github.com/robertwb"
}
```

Attachment [sage-4475-new_hope-part3.patch](tarball://root/attachments/some-uuid/ticket4475/sage-4475-new_hope-part3.patch) by @robertwb created at 2008-12-20 05:26:49

(Partial) native implementation of the G function.



---

archive/issue_events_010112.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4475",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4475#event-10112"
}
```



---

archive/issue_events_010113.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4475",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4475#event-10113"
}
```



---

archive/issue_events_010114.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4475",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4475#event-10114"
}
```



---

archive/issue_events_010115.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4475",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4475#event-10115"
}
```



---

archive/issue_events_010116.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4475",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4475#event-10116"
}
```



---

archive/issue_events_010117.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4475",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4475#event-10117"
}
```



---

archive/issue_events_010118.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4475",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4475#event-10118"
}
```
