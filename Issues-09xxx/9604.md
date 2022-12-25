# Issue 9604: Tracker bug for toric varieties

archive/issues_009604.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @novoselt\n\nKeywords: toric geometry\n\nThis bug tracks the current status of the toric varieties code and the interdependence of new patches.\n\nGroups separated by blank lines may be applied independently.\n\n* #11559: Speed up Posets and toric Chow group\n\n* #15153: Check embedding morphism when comparing two toric varieties\n\n* #15280: Extensions of PALP normal form, affine normal form and isomorphisms\n\n* #16012: Sublattice fan isomorphism bug\n\n* #16334: Toric divisors from fans in sublattices\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9604\n\n",
    "closed_at": "2019-02-26T13:58:00Z",
    "created_at": "2010-07-26T17:21:42Z",
    "labels": [
        "component: algebraic geometry"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Tracker bug for toric varieties",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9604",
    "user": "https://github.com/vbraun"
}
```
Assignee: @aghitza

CC:  @novoselt

Keywords: toric geometry

This bug tracks the current status of the toric varieties code and the interdependence of new patches.

Groups separated by blank lines may be applied independently.

* #11559: Speed up Posets and toric Chow group

* #15153: Check embedding morphism when comparing two toric varieties

* #15280: Extensions of PALP normal form, affine normal form and isomorphisms

* #16012: Sublattice fan isomorphism bug

* #16334: Toric divisors from fans in sublattices


Issue created by migration from https://trac.sagemath.org/ticket/9604





---

archive/issue_comments_092874.json:
```json
{
    "body": "Can I merge #9470 and #9326 now, or should I wait until every ticket has a positive review?",
    "created_at": "2010-08-07T06:01:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9604#issuecomment-92874",
    "user": "https://github.com/qed777"
}
```

Can I merge #9470 and #9326 now, or should I wait until every ticket has a positive review?



---

archive/issue_comments_092875.json:
```json
{
    "body": "#9470 and #9326 are ready to be merged, but I thought that 4.5.2 is in feature freeze now?",
    "created_at": "2010-08-07T14:31:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9604#issuecomment-92875",
    "user": "https://github.com/vbraun"
}
```

#9470 and #9326 are ready to be merged, but I thought that 4.5.2 is in feature freeze now?



---

archive/issue_comments_092876.json:
```json
{
    "body": "Replying to [comment:3 vbraun]:\n> #9470 and #9326 are ready to be merged, but I thought that 4.5.2 is in feature freeze now?\n\n\nIndeed, we'll release 4.5.2 very soon.  I've been preparing a 4.5.3.alpha0.",
    "created_at": "2010-08-07T19:26:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9604#issuecomment-92876",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:3 vbraun]:
> #9470 and #9326 are ready to be merged, but I thought that 4.5.2 is in feature freeze now?


Indeed, we'll release 4.5.2 very soon.  I've been preparing a 4.5.3.alpha0.



---

archive/issue_comments_092877.json:
```json
{
    "body": "updated patch",
    "created_at": "2010-08-23T21:44:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9604#issuecomment-92877",
    "user": "https://github.com/vbraun"
}
```

updated patch



---

archive/issue_comments_092878.json:
```json
{
    "body": "Attachment [toricvarieties.hg](tarball://root/attachments/some-uuid/ticket9604/toricvarieties.hg) by @novoselt created at 2010-08-26 21:35:42\n\nI'll put bugs in front of toric divisors, since they have chances to be settled quickly.",
    "created_at": "2010-08-26T21:35:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9604#issuecomment-92878",
    "user": "https://github.com/novoselt"
}
```

Attachment [toricvarieties.hg](tarball://root/attachments/some-uuid/ticket9604/toricvarieties.hg) by @novoselt created at 2010-08-26 21:35:42

I'll put bugs in front of toric divisors, since they have chances to be settled quickly.



---

archive/issue_comments_092879.json:
```json
{
    "body": "I sneaked in yet another patch in front of toric divisors, in case it will be useful for Kaehler/Mori cones (maybe not due to dimension limitations), but so far it is independent of #9337 and can be shifted down.",
    "created_at": "2010-08-30T05:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9604#issuecomment-92879",
    "user": "https://github.com/novoselt"
}
```

I sneaked in yet another patch in front of toric divisors, in case it will be useful for Kaehler/Mori cones (maybe not due to dimension limitations), but so far it is independent of #9337 and can be shifted down.



---

archive/issue_comments_092880.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-09-27T17:18:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9604#issuecomment-92880",
    "user": "https://github.com/vbraun"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_092881.json:
```json
{
    "body": "`trac_9664_add_toric_potter.patch` depends on `trac_9972_add_toric_lattice_morphisms.patch`. No logical dependency, but thats how the patch works out. I don't think order matters too much on that one, just wanted to get it right.",
    "created_at": "2010-10-04T20:16:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9604#issuecomment-92881",
    "user": "https://github.com/vbraun"
}
```

`trac_9664_add_toric_potter.patch` depends on `trac_9972_add_toric_lattice_morphisms.patch`. No logical dependency, but thats how the patch works out. I don't think order matters too much on that one, just wanted to get it right.



---

archive/issue_comments_092882.json:
```json
{
    "body": "No more dependence ;-)",
    "created_at": "2010-10-04T20:33:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9604#issuecomment-92882",
    "user": "https://github.com/novoselt"
}
```

No more dependence ;-)



---

archive/issue_comments_092883.json:
```json
{
    "body": "Sorry for temporarily making #10513 a dependency. This ticket isn't ready, yet. Thus I reoved the dependency again.",
    "created_at": "2010-12-22T13:35:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9604#issuecomment-92883",
    "user": "https://github.com/simon-king-jena"
}
```

Sorry for temporarily making #10513 a dependency. This ticket isn't ready, yet. Thus I reoved the dependency again.



---

archive/issue_comments_092884.json:
```json
{
    "body": "Tried to make all dependencies and especially their absences more clear.\n\nVolker, I am a little confused by comments on #8169 and #9918 - do they depend on/conflict with each other somehow?",
    "created_at": "2010-12-22T16:12:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9604#issuecomment-92884",
    "user": "https://github.com/novoselt"
}
```

Tried to make all dependencies and especially their absences more clear.

Volker, I am a little confused by comments on #8169 and #9918 - do they depend on/conflict with each other somehow?



---

archive/issue_comments_092885.json:
```json
{
    "body": "#9918 uses the TOPCOM spkg (in #8169) if it is available, and falls back to its own implementation if not. So there is no dependency either way. Except that applying #8169 without #9918 would be meaningless as there would be nothing in the sage library to use TOPCOM.",
    "created_at": "2010-12-22T16:23:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9604#issuecomment-92885",
    "user": "https://github.com/vbraun"
}
```

#9918 uses the TOPCOM spkg (in #8169) if it is available, and falls back to its own implementation if not. So there is no dependency either way. Except that applying #8169 without #9918 would be meaningless as there would be nothing in the sage library to use TOPCOM.



---

archive/issue_comments_092886.json:
```json
{
    "body": "So none of the patches of #8169 should be applied, it just provides an optional package, correct?",
    "created_at": "2010-12-22T16:27:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9604#issuecomment-92886",
    "user": "https://github.com/novoselt"
}
```

So none of the patches of #8169 should be applied, it just provides an optional package, correct?



---

archive/issue_comments_092887.json:
```json
{
    "body": "Yes, none of the patches in #8169 should be applied.",
    "created_at": "2010-12-22T16:29:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9604#issuecomment-92887",
    "user": "https://github.com/vbraun"
}
```

Yes, none of the patches in #8169 should be applied.



---

archive/issue_comments_092888.json:
```json
{
    "body": "I've started to put my patch queue into a mercurial repository itself. See\n\nhttps://bitbucket.org/vbraun/mq-for-sage-toric-varieties/src",
    "created_at": "2010-12-28T00:16:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9604#issuecomment-92888",
    "user": "https://github.com/vbraun"
}
```

I've started to put my patch queue into a mercurial repository itself. See

https://bitbucket.org/vbraun/mq-for-sage-toric-varieties/src



---

archive/issue_comments_092889.json:
```json
{
    "body": "Changing keywords from \"\" to \"toric geometry\".",
    "created_at": "2011-03-03T02:44:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9604#issuecomment-92889",
    "user": "https://github.com/novoselt"
}
```

Changing keywords from "" to "toric geometry".



---

archive/issue_events_023920.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9604#event-23920"
}
```



---

archive/issue_events_023921.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9604#event-23921"
}
```



---

archive/issue_events_023922.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9604#event-23922"
}
```



---

archive/issue_events_023923.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9604#event-23923"
}
```



---

archive/issue_events_023924.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9604#event-23924"
}
```



---

archive/issue_events_023925.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9604#event-23925"
}
```



---

archive/issue_events_023926.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9604#event-23926"
}
```



---

archive/issue_comments_092890.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2017-01-02T22:54:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9604#issuecomment-92890",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_092891.json:
```json
{
    "body": "With trac dependencies, long history here, and generally low toric activity I propose closing this ticket.",
    "created_at": "2017-01-02T22:54:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9604#issuecomment-92891",
    "user": "https://github.com/novoselt"
}
```

With trac dependencies, long history here, and generally low toric activity I propose closing this ticket.



---

archive/issue_comments_092892.json:
```json
{
    "body": "indeed. And there is still the \"toric\" keyword to gather these tickets",
    "created_at": "2018-11-30T20:52:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9604#issuecomment-92892",
    "user": "https://github.com/fchapoton"
}
```

indeed. And there is still the "toric" keyword to gather these tickets



---

archive/issue_comments_092893.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-11-30T20:52:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9604#issuecomment-92893",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_023927.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2018-11-30T20:52:55Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9604#event-23927"
}
```



---

archive/issue_events_023928.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2018-11-30T20:52:55Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9604#event-23928"
}
```



---

archive/issue_events_023929.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2019-02-26T13:58:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9604#event-23929"
}
```



---

archive/issue_comments_092894.json:
```json
{
    "body": "Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.",
    "created_at": "2019-02-26T13:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9604#issuecomment-92894",
    "user": "https://github.com/embray"
}
```

Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.



---

archive/issue_comments_092895.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2019-02-26T13:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9604",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9604#issuecomment-92895",
    "user": "https://github.com/embray"
}
```

Resolution: invalid
