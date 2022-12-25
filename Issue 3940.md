# Issue 3940: Add a warnings framework to Sage

archive/issues_003940.json:
```json
{
    "body": "Assignee: cwitty\n\nThe builtin python warnings framework allows filtering on subclasses of warnings.  This would be useful to make a sage warnings framework, with different types of sage-specific warnings.\n\nHere, I've added a directory and a basic file with a NumericalPrecisionWarning class that could be triggered, for example, in the eigenvalue computations.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3940\n\n",
    "created_at": "2008-08-24T00:09:30Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Add a warnings framework to Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3940",
    "user": "https://github.com/jasongrout"
}
```
Assignee: cwitty

The builtin python warnings framework allows filtering on subclasses of warnings.  This would be useful to make a sage warnings framework, with different types of sage-specific warnings.

Here, I've added a directory and a basic file with a NumericalPrecisionWarning class that could be triggered, for example, in the eigenvalue computations.

Issue created by migration from https://trac.sagemath.org/ticket/3940





---

archive/issue_comments_028184.json:
```json
{
    "body": "Attachment [warnings.patch](tarball://root/attachments/some-uuid/ticket3940/warnings.patch) by mabshoff created at 2008-08-25 01:15:17\n\nJason,\n\nnow that #3873 has been merged can you check how much of this patch is still useful/applies?\n\nCheers,\n\nMichael",
    "created_at": "2008-08-25T01:15:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3940#issuecomment-28184",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [warnings.patch](tarball://root/attachments/some-uuid/ticket3940/warnings.patch) by mabshoff created at 2008-08-25 01:15:17

Jason,

now that #3873 has been merged can you check how much of this patch is still useful/applies?

Cheers,

Michael



---

archive/issue_comments_028185.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-08-25T14:29:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3940#issuecomment-28185",
    "user": "https://github.com/jasongrout"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_028186.json:
```json
{
    "body": "It is useful and it still applies; the application is still sitting in my queue, though.\n\nBasically, there are some situations where computing eigenvalues/vectors should throw a warning.  Also, the plotting code should throw a warning when some situations come up (when the function can't be evaluated at certain points).  The point of this patch is that: \n\n1. It makes it so that sage-related warnings are always shown by default.\n\n2. It makes it very easy to do something with all sage-related warnings (e.g., throw exceptions or ignore them and don't print them out, etc.)\n\nIf you want to wait until I post a patch that uses this, that's fine.",
    "created_at": "2008-08-25T14:29:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3940#issuecomment-28186",
    "user": "https://github.com/jasongrout"
}
```

It is useful and it still applies; the application is still sitting in my queue, though.

Basically, there are some situations where computing eigenvalues/vectors should throw a warning.  Also, the plotting code should throw a warning when some situations come up (when the function can't be evaluated at certain points).  The point of this patch is that: 

1. It makes it so that sage-related warnings are always shown by default.

2. It makes it very easy to do something with all sage-related warnings (e.g., throw exceptions or ignore them and don't print them out, etc.)

If you want to wait until I post a patch that uses this, that's fine.



---

archive/issue_comments_028187.json:
```json
{
    "body": "BTW, one question I had was whether to make a warnings directory or to just put this under the misc directory.",
    "created_at": "2008-08-25T14:30:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3940#issuecomment-28187",
    "user": "https://github.com/jasongrout"
}
```

BTW, one question I had was whether to make a warnings directory or to just put this under the misc directory.



---

archive/issue_comments_028188.json:
```json
{
    "body": "IMHO if the warnings framework is expected to stay as one file, then it should be in the misc directory; if you expect the warnings framework to expand to multiple files then maybe a new directory would be more appropriate.",
    "created_at": "2008-08-25T15:46:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3940#issuecomment-28188",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

IMHO if the warnings framework is expected to stay as one file, then it should be in the misc directory; if you expect the warnings framework to expand to multiple files then maybe a new directory would be more appropriate.



---

archive/issue_comments_028189.json:
```json
{
    "body": "What is the status here? Not having a proper summary subject makes files fall through the cracks. \n\nEither this code is useful in which case it should be applied or not. It seems that cwitty's has some pointers, so what's going on here? :)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T21:48:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3940#issuecomment-28189",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

What is the status here? Not having a proper summary subject makes files fall through the cracks. 

Either this code is useful in which case it should be applied or not. It seems that cwitty's has some pointers, so what's going on here? :)

Cheers,

Michael



---

archive/issue_comments_028190.json:
```json
{
    "body": "I agree with cwitty:\n\nWork that needs to be done on this patch to get it ready for review:\n\n* Make it one file in the misc directory\n\nIf warnings become a more important part of Sage, then later we can break things into a different directory.",
    "created_at": "2009-04-16T22:30:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3940#issuecomment-28190",
    "user": "https://github.com/jasongrout"
}
```

I agree with cwitty:

Work that needs to be done on this patch to get it ready for review:

* Make it one file in the misc directory

If warnings become a more important part of Sage, then later we can break things into a different directory.



---

archive/issue_comments_028191.json:
```json
{
    "body": "Attachment [sagewarnings.py](tarball://root/attachments/some-uuid/ticket3940/sagewarnings.py) by mraum created at 2010-01-18 21:54:03",
    "created_at": "2010-01-18T21:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3940#issuecomment-28191",
    "user": "https://trac.sagemath.org/admin/accounts/users/mraum"
}
```

Attachment [sagewarnings.py](tarball://root/attachments/some-uuid/ticket3940/sagewarnings.py) by mraum created at 2010-01-18 21:54:03



---

archive/issue_comments_028192.json:
```json
{
    "body": "I uploaded sagewarnings.py which derives from Jason's patch.\nThis extension addresses the lack of use cases by providing some warning classes adapted to particular things I've got in mind. This file is for discussion; See the thread on sage-devel.\n\nI renamed the file warning.py to sagewarnings.py. This seems more consistent with python's warnings module to me.",
    "created_at": "2010-01-18T21:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3940#issuecomment-28192",
    "user": "https://trac.sagemath.org/admin/accounts/users/mraum"
}
```

I uploaded sagewarnings.py which derives from Jason's patch.
This extension addresses the lack of use cases by providing some warning classes adapted to particular things I've got in mind. This file is for discussion; See the thread on sage-devel.

I renamed the file warning.py to sagewarnings.py. This seems more consistent with python's warnings module to me.



---

archive/issue_events_009045.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3940#event-9045"
}
```



---

archive/issue_events_009046.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3940#event-9046"
}
```



---

archive/issue_events_009047.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3940#event-9047"
}
```



---

archive/issue_events_009048.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3940#event-9048"
}
```



---

archive/issue_events_009049.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3940#event-9049"
}
```



---

archive/issue_events_009050.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3940#event-9050"
}
```



---

archive/issue_events_009051.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3940#event-9051"
}
```



---

archive/issue_comments_028193.json:
```json
{
    "body": "outdated, should close",
    "created_at": "2021-08-26T03:45:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3940#issuecomment-28193",
    "user": "https://github.com/mkoeppe"
}
```

outdated, should close



---

archive/issue_comments_028194.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2021-08-26T03:45:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3940#issuecomment-28194",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_events_009052.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-08-26T03:45:59Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3940#event-9052"
}
```



---

archive/issue_events_009053.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-08-26T03:45:59Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3940#event-9053"
}
```



---

archive/issue_comments_028195.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-10-04T22:56:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3940#issuecomment-28195",
    "user": "https://github.com/orlitzky"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_028196.json:
```json
{
    "body": "I think the motivation behind this is still valid. But to proceed today, we'd have to look through `git grep 'warn('` and come up with a set of warnings that map nicely to the existing uses in the tree. (And the names themselves are just asking for a bikeshed thread on sage-devel.) The patches on the ticket are far out-of-date in that respect.\n\nThat said, I could sit down for five minutes and easily come up with a hundred \"wishlist\" items that would be nice to have and that would involve a lot of work that no one is willing to do. So I think after so many years, the small benefit of closing a \"dead\" ticket outweighs whatever we'd gain from keeping this on the wishlist.",
    "created_at": "2021-10-04T22:56:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3940#issuecomment-28196",
    "user": "https://github.com/orlitzky"
}
```

I think the motivation behind this is still valid. But to proceed today, we'd have to look through `git grep 'warn('` and come up with a set of warnings that map nicely to the existing uses in the tree. (And the names themselves are just asking for a bikeshed thread on sage-devel.) The patches on the ticket are far out-of-date in that respect.

That said, I could sit down for five minutes and easily come up with a hundred "wishlist" items that would be nice to have and that would involve a lot of work that no one is willing to do. So I think after so many years, the small benefit of closing a "dead" ticket outweighs whatever we'd gain from keeping this on the wishlist.



---

archive/issue_comments_028197.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-10-04T23:44:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3940#issuecomment-28197",
    "user": "https://github.com/mkoeppe"
}
```

Resolution: invalid



---

archive/issue_events_009054.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-10-04T23:44:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3940",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3940#event-9054"
}
```
