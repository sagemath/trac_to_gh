# Issue 6326: Reimplement Souvigner_AUTO code by PARI function

archive/issues_006326.json:
```json
{
    "body": "Assignee: justin\n\nKeywords: quadratic form\n\nAll `optional -- souvigner` code involving `Souvigner_AUTO` should be replaced by calls to PARI.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6326\n\n",
    "closed_at": "2015-06-12T22:58:50Z",
    "created_at": "2009-06-16T15:00:34Z",
    "labels": [
        "component: quadratic forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.8",
    "title": "Reimplement Souvigner_AUTO code by PARI function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6326",
    "user": "https://github.com/williamstein"
}
```
Assignee: justin

Keywords: quadratic form

All `optional -- souvigner` code involving `Souvigner_AUTO` should be replaced by calls to PARI.

Issue created by migration from https://trac.sagemath.org/ticket/6326





---

archive/issue_comments_050387.json:
```json
{
    "body": "Souvigner auto/isomorphism code tarball",
    "created_at": "2011-01-09T07:57:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50387",
    "user": "https://github.com/jonhanke"
}
```

Souvigner auto/isomorphism code tarball



---

archive/issue_comments_050388.json:
```json
{
    "body": "Attachment [export.V3.tar](tarball://root/attachments/some-uuid/ticket6326/export.V3.tar) by @jonhanke created at 2011-01-09 08:01:07\n\nI have attached the Souvigner tarball sent to me by Gabi Nebe in March 2008.  I'm not sure how to arrange Sage to build it, but the two files ISOM64 and AUTO64 that the makeflie produces need to renamed as Souvigner_ISOM and Souvigner_AUTO and moved to sage-4.x/local/bin.",
    "created_at": "2011-01-09T08:01:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50388",
    "user": "https://github.com/jonhanke"
}
```

Attachment [export.V3.tar](tarball://root/attachments/some-uuid/ticket6326/export.V3.tar) by @jonhanke created at 2011-01-09 08:01:07

I have attached the Souvigner tarball sent to me by Gabi Nebe in March 2008.  I'm not sure how to arrange Sage to build it, but the two files ISOM64 and AUTO64 that the makeflie produces need to renamed as Souvigner_ISOM and Souvigner_AUTO and moved to sage-4.x/local/bin.



---

archive/issue_comments_050389.json:
```json
{
    "body": "Changing assignee from tbd to justin.",
    "created_at": "2011-01-12T04:29:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50389",
    "user": "https://github.com/jonhanke"
}
```

Changing assignee from tbd to justin.



---

archive/issue_comments_050390.json:
```json
{
    "body": "Changing component from optional packages to quadratic forms.",
    "created_at": "2011-01-12T04:29:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50390",
    "user": "https://github.com/jonhanke"
}
```

Changing component from optional packages to quadratic forms.



---

archive/issue_comments_050391.json:
```json
{
    "body": "There is a bug within the interface the Souvigner code that produces false results:\n\n```\nsage: Q1 = DiagonalQuadraticForm(ZZ, [1,3,5])\nsage: Q2 = QuadraticForm(ZZ, 3, [1,0,0, 2,2, 8])\nsage: Q1.theta_series()\n1 + 2*q + 2*q^3 + 6*q^4 + 2*q^5 + 4*q^6 + 4*q^7 + 4*q^8 + 14*q^9 + O(q^10)\nsage: Q2.theta_series()\n1 + 2*q + 2*q^2 + 4*q^3 + 2*q^4 + 4*q^6 + 6*q^8 + 14*q^9 + O(q^10)\nsage: Q1.is_globally_equivalent_to(Q2)    ## Correct\nFalse\nsage: Q2.is_globally_equivalent_to(Q1)    ## Incorrect\nTrue\n```\n\nThe problem results from the differing possible failure messages (\"...not isometric...\" or \"...not isomorphic...\") returned from the Souvigner Code.  A patch is attached.",
    "created_at": "2011-01-12T04:29:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50391",
    "user": "https://github.com/jonhanke"
}
```

There is a bug within the interface the Souvigner code that produces false results:

```
sage: Q1 = DiagonalQuadraticForm(ZZ, [1,3,5])
sage: Q2 = QuadraticForm(ZZ, 3, [1,0,0, 2,2, 8])
sage: Q1.theta_series()
1 + 2*q + 2*q^3 + 6*q^4 + 2*q^5 + 4*q^6 + 4*q^7 + 4*q^8 + 14*q^9 + O(q^10)
sage: Q2.theta_series()
1 + 2*q + 2*q^2 + 4*q^3 + 2*q^4 + 4*q^6 + 6*q^8 + 14*q^9 + O(q^10)
sage: Q1.is_globally_equivalent_to(Q2)    ## Correct
False
sage: Q2.is_globally_equivalent_to(Q1)    ## Incorrect
True
```

The problem results from the differing possible failure messages ("...not isometric..." or "...not isomorphic...") returned from the Souvigner Code.  A patch is attached.



---

archive/issue_comments_050392.json:
```json
{
    "body": "Fixes a bug in the quadratic forms global equivalence testing using Souvigner's code",
    "created_at": "2011-01-12T04:36:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50392",
    "user": "https://github.com/jonhanke"
}
```

Fixes a bug in the quadratic forms global equivalence testing using Souvigner's code



---

archive/issue_comments_050393.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-12T04:45:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50393",
    "user": "https://github.com/jonhanke"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_050394.json:
```json
{
    "body": "Attachment [ticket_6326_bug_fix.patch](tarball://root/attachments/some-uuid/ticket6326/ticket_6326_bug_fix.patch) by @jonhanke created at 2011-01-12 04:45:58",
    "created_at": "2011-01-12T04:45:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50394",
    "user": "https://github.com/jonhanke"
}
```

Attachment [ticket_6326_bug_fix.patch](tarball://root/attachments/some-uuid/ticket6326/ticket_6326_bug_fix.patch) by @jonhanke created at 2011-01-12 04:45:58



---

archive/issue_comments_050395.json:
```json
{
    "body": "In order for this to get into Sage proper, we'll need to make an spkg which installs the right things to the right places.",
    "created_at": "2011-03-11T06:06:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50395",
    "user": "https://github.com/rlmill"
}
```

In order for this to get into Sage proper, we'll need to make an spkg which installs the right things to the right places.



---

archive/issue_comments_050396.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-03-11T06:06:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50396",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_050397.json:
```json
{
    "body": "Attachment [souvigner-2012-03-10.spkg](tarball://root/attachments/some-uuid/ticket6326/souvigner-2012-03-10.spkg) by @jdemeyer created at 2013-08-13 15:35:53",
    "created_at": "2013-08-13T15:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50397",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [souvigner-2012-03-10.spkg](tarball://root/attachments/some-uuid/ticket6326/souvigner-2012-03-10.spkg) by @jdemeyer created at 2013-08-13 15:35:53



---

archive/issue_events_014856.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6326#event-14856"
}
```



---

archive/issue_events_014857.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6326#event-14857"
}
```



---

archive/issue_events_014858.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6326#event-14858"
}
```



---

archive/issue_events_014859.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6326#event-14859"
}
```



---

archive/issue_events_014860.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6326#event-14860"
}
```



---

archive/issue_events_014861.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6326#event-14861"
}
```



---

archive/issue_events_014862.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6326#event-14862"
}
```



---

archive/issue_comments_050398.json:
```json
{
    "body": "If anybody cares about this: this functionality is now also provided by the PARI functions `qfisom()` and `qfauto()`.",
    "created_at": "2015-06-10T20:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50398",
    "user": "https://github.com/jdemeyer"
}
```

If anybody cares about this: this functionality is now also provided by the PARI functions `qfisom()` and `qfauto()`.



---

archive/issue_events_014863.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2015-06-10T20:28:14Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6326#event-14863"
}
```



---

archive/issue_events_014864.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2015-06-10T20:28:14Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "milestone": "sage-6.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6326#event-14864"
}
```



---

archive/issue_comments_050399.json:
```json
{
    "body": "New commits:",
    "created_at": "2015-06-10T21:36:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50399",
    "user": "https://github.com/jdemeyer"
}
```

New commits:



---

archive/issue_comments_050400.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2015-06-10T21:36:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50400",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_050401.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-06-10T21:37:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50401",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_050402.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2015-06-11T08:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50402",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_050403.json:
```json
{
    "body": "Changing keywords from \"\" to \"quadratic form\".",
    "created_at": "2015-06-12T15:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50403",
    "user": "https://github.com/fchapoton"
}
```

Changing keywords from "" to "quadratic form".



---

archive/issue_comments_050404.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-06-12T15:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50404",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_050405.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2015-06-12T15:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50405",
    "user": "https://github.com/fchapoton"
}
```

Looks good to me.



---

archive/issue_comments_050406.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-06-12T22:58:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6326#issuecomment-50406",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_014865.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-06-12T22:58:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6326",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6326#event-14865"
}
```
