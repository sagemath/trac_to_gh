# Issue 6709: There are many doctest failues on Solaris 32-bit builds.

archive/issues_006709.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  david.kirkby@onetel.net @dimpase\n\nI'll post a couple of logs later, but thought I'd create a ticket for this. \n\nIssue created by migration from https://trac.sagemath.org/ticket/6709\n\n",
    "closed_at": "2020-07-15T07:18:41Z",
    "created_at": "2009-08-09T10:24:07Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "There are many doctest failues on Solaris 32-bit builds.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6709",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  david.kirkby@onetel.net @dimpase

I'll post a couple of logs later, but thought I'd create a ticket for this. 

Issue created by migration from https://trac.sagemath.org/ticket/6709





---

archive/issue_comments_054984.json:
```json
{
    "body": "Test failues on sage-4.1.1.rc0 with Maxima 5.19.0",
    "created_at": "2009-08-09T18:43:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6709#issuecomment-54984",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Test failues on sage-4.1.1.rc0 with Maxima 5.19.0



---

archive/issue_comments_054985.json:
```json
{
    "body": "Attachment [test.log](tarball://root/attachments/some-uuid/ticket6709/test.log) by drkirkby created at 2009-08-11 09:56:53\n\ntest.log on SPARC after bug fix to ECL 9.8.1",
    "created_at": "2009-08-11T09:56:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6709#issuecomment-54985",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [test.log](tarball://root/attachments/some-uuid/ticket6709/test.log) by drkirkby created at 2009-08-11 09:56:53

test.log on SPARC after bug fix to ECL 9.8.1



---

archive/issue_comments_054986.json:
```json
{
    "body": "After adding the bug fix to sysfun.lsp which was added by one of ECL developers on the 10th August 2009, here is the output on a SPARC box running Solaris 10 update 7.",
    "created_at": "2009-08-11T10:01:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6709#issuecomment-54986",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

After adding the bug fix to sysfun.lsp which was added by one of ECL developers on the 10th August 2009, here is the output on a SPARC box running Solaris 10 update 7.



---

archive/issue_comments_054987.json:
```json
{
    "body": "I added \"32-bit\" to the title, as this ticket was created when Sage was only building 64-bit. \n\nIt can be closed as fixed, as all doctests have passed on Solaris or OpenSolaris both SPARC and x86 for a long time.",
    "created_at": "2011-04-02T12:35:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6709#issuecomment-54987",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I added "32-bit" to the title, as this ticket was created when Sage was only building 64-bit. 

It can be closed as fixed, as all doctests have passed on Solaris or OpenSolaris both SPARC and x86 for a long time.



---

archive/issue_comments_054988.json:
```json
{
    "body": "Changing assignee from tbd to drkirkby.",
    "created_at": "2011-04-02T12:35:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6709#issuecomment-54988",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing assignee from tbd to drkirkby.



---

archive/issue_comments_054989.json:
```json
{
    "body": "Replying to [comment:3 drkirkby]:\n> I added \"32-bit\" to the title, as this ticket was created when Sage was only building 64-bit. \n\n\nI mean the ticket was opened when Sage was only building 32-bit. Now it will build 64-bit, but does not work very well in 64-bit mode.",
    "created_at": "2011-04-02T12:37:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6709#issuecomment-54989",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:3 drkirkby]:
> I added "32-bit" to the title, as this ticket was created when Sage was only building 64-bit. 


I mean the ticket was opened when Sage was only building 32-bit. Now it will build 64-bit, but does not work very well in 64-bit mode.



---

archive/issue_events_015832.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6709",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6709#event-15832"
}
```



---

archive/issue_events_015833.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6709",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6709#event-15833"
}
```



---

archive/issue_events_015834.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6709",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6709#event-15834"
}
```



---

archive/issue_events_015835.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6709",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6709#event-15835"
}
```



---

archive/issue_events_015836.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6709",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6709#event-15836"
}
```



---

archive/issue_events_015837.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6709",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6709#event-15837"
}
```



---

archive/issue_events_015838.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6709",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6709#event-15838"
}
```



---

archive/issue_events_015839.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-07-08T16:51:35Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6709",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6709#event-15839"
}
```



---

archive/issue_events_015840.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-07-08T16:51:35Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6709",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6709#event-15840"
}
```



---

archive/issue_comments_054990.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-07-08T16:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6709#issuecomment-54990",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_054991.json:
```json
{
    "body": "Outdated, should be closed",
    "created_at": "2020-07-08T16:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6709#issuecomment-54991",
    "user": "https://github.com/mkoeppe"
}
```

Outdated, should be closed



---

archive/issue_comments_054992.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-07-12T19:57:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6709#issuecomment-54992",
    "user": "https://github.com/orlitzky"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_054993.json:
```json
{
    "body": "The goal of these tickets is laudable, but:\n\n* We need at least one user who is able to test.\n* The package/OS information on this ticket is outdated beyond usefulness.\n* Upstream is a better place to report portability issues these days.",
    "created_at": "2020-07-12T19:57:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6709#issuecomment-54993",
    "user": "https://github.com/orlitzky"
}
```

The goal of these tickets is laudable, but:

* We need at least one user who is able to test.
* The package/OS information on this ticket is outdated beyond usefulness.
* Upstream is a better place to report portability issues these days.



---

archive/issue_comments_054994.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-07-15T07:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6709#issuecomment-54994",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid



---

archive/issue_events_015841.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-07-15T07:18:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6709",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6709#event-15841"
}
```



---

archive/issue_comments_054995.json:
```json
{
    "body": "Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.",
    "created_at": "2020-07-15T07:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6709#issuecomment-54995",
    "user": "https://github.com/fchapoton"
}
```

Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.
