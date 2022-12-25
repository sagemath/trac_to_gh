# Issue 2816: unify eigen* functions for different matrix classes

archive/issues_002816.json:
```json
{
    "body": "Assignee: @williamstein\n\nSee the conclusions from the discussion: \n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/c8d2001f2b19a9bc#\n\nIssue created by migration from https://trac.sagemath.org/ticket/2816\n\n",
    "created_at": "2008-04-05T22:17:44Z",
    "labels": [
        "component: linear algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "unify eigen* functions for different matrix classes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2816",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

See the conclusions from the discussion: 

http://groups.google.com/group/sage-devel/browse_thread/thread/c8d2001f2b19a9bc#

Issue created by migration from https://trac.sagemath.org/ticket/2816





---

archive/issue_comments_019293.json:
```json
{
    "body": "Attachment [linear-algebra-interface.patch](tarball://root/attachments/some-uuid/ticket2816/linear-algebra-interface.patch) by @jasongrout created at 2008-07-19 18:48:32",
    "created_at": "2008-07-19T18:48:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2816#issuecomment-19293",
    "user": "https://github.com/jasongrout"
}
```

Attachment [linear-algebra-interface.patch](tarball://root/attachments/some-uuid/ticket2816/linear-algebra-interface.patch) by @jasongrout created at 2008-07-19 18:48:32



---

archive/issue_comments_019294.json:
```json
{
    "body": "The documentation isn't all there, but you can see the functions.",
    "created_at": "2008-07-19T18:49:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2816#issuecomment-19294",
    "user": "https://github.com/jasongrout"
}
```

The documentation isn't all there, but you can see the functions.



---

archive/issue_comments_019295.json:
```json
{
    "body": "This depends on #3654",
    "created_at": "2008-07-19T18:49:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2816#issuecomment-19295",
    "user": "https://github.com/jasongrout"
}
```

This depends on #3654



---

archive/issue_comments_019296.json:
```json
{
    "body": "See http://groups.google.com/group/sage-devel/browse_thread/thread/3ef6da9c8fa7db36 for \"documentation\" on the functions.",
    "created_at": "2008-07-19T18:52:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2816#issuecomment-19296",
    "user": "https://github.com/jasongrout"
}
```

See http://groups.google.com/group/sage-devel/browse_thread/thread/3ef6da9c8fa7db36 for "documentation" on the functions.



---

archive/issue_comments_019297.json:
```json
{
    "body": "I know this is preliminary but just wanted to report for others testers that this has a boat-load of doctest failures:\n\n\n```\n...\n        sage -t  devel/sage/sage/calculus/wester.py\n        sage -t  devel/sage/sage/matrix/matrix2.pyx\n        sage -t  devel/sage/sage/matrix/tests.py\n        sage -t  devel/sage/sage/modular/modform/half_integral.py\n        sage -t  devel/sage/sage/rings/finite_field_ntl_gf2e.pyx\n        sage -t  devel/sage/sage/misc/functional.py\n```\n\nI ran testall twice and it seems that I did not pick up the failure of sage -t  devel/sage/sage/calculus/wester.py or of devel/sage/sage/modular/modform/half_integral.py the first time. These aside, looks like it will eventually be a valuable contribution to SAGE.",
    "created_at": "2008-07-20T02:39:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2816#issuecomment-19297",
    "user": "https://github.com/wdjoyner"
}
```

I know this is preliminary but just wanted to report for others testers that this has a boat-load of doctest failures:


```
...
        sage -t  devel/sage/sage/calculus/wester.py
        sage -t  devel/sage/sage/matrix/matrix2.pyx
        sage -t  devel/sage/sage/matrix/tests.py
        sage -t  devel/sage/sage/modular/modform/half_integral.py
        sage -t  devel/sage/sage/rings/finite_field_ntl_gf2e.pyx
        sage -t  devel/sage/sage/misc/functional.py
```

I ran testall twice and it seems that I did not pick up the failure of sage -t  devel/sage/sage/calculus/wester.py or of devel/sage/sage/modular/modform/half_integral.py the first time. These aside, looks like it will eventually be a valuable contribution to SAGE.



---

archive/issue_comments_019298.json:
```json
{
    "body": "Thanks for running testall.  Some doctests are fixed in the current patch; I'll fix the other doctests in an updated patch.",
    "created_at": "2008-07-20T03:32:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2816#issuecomment-19298",
    "user": "https://github.com/jasongrout"
}
```

Thanks for running testall.  Some doctests are fixed in the current patch; I'll fix the other doctests in an updated patch.



---

archive/issue_comments_019299.json:
```json
{
    "body": "This is part of the linear algebra SEP: http://wiki.sagemath.org/LinearAlgebraSEP",
    "created_at": "2009-01-22T01:52:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2816#issuecomment-19299",
    "user": "https://github.com/jasongrout"
}
```

This is part of the linear algebra SEP: http://wiki.sagemath.org/LinearAlgebraSEP



---

archive/issue_comments_019300.json:
```json
{
    "body": "What is going on here?\n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T22:37:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2816#issuecomment-19300",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

What is going on here?

Cheers,

Michael



---

archive/issue_comments_019301.json:
```json
{
    "body": "Well, it probably needs massive rebasing because of the rest transition, for one.  It's on my back burner; I'll probably get to it before June, since I'm teaching linear algebra for the first part of the summer.  However, if someone else is interested in working on this, don't hesitate to post a message here and start working!",
    "created_at": "2009-04-19T00:00:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2816#issuecomment-19301",
    "user": "https://github.com/jasongrout"
}
```

Well, it probably needs massive rebasing because of the rest transition, for one.  It's on my back burner; I'll probably get to it before June, since I'm teaching linear algebra for the first part of the summer.  However, if someone else is interested in working on this, don't hesitate to post a message here and start working!



---

archive/issue_events_006477.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2816",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2816#event-6477"
}
```



---

archive/issue_events_006478.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2816",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2816#event-6478"
}
```



---

archive/issue_events_006479.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2816",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2816#event-6479"
}
```



---

archive/issue_events_006480.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2816",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2816#event-6480"
}
```



---

archive/issue_events_006481.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2816",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2816#event-6481"
}
```



---

archive/issue_events_006482.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2816",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2816#event-6482"
}
```



---

archive/issue_events_006483.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2816",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2816#event-6483"
}
```
