# Issue 9126: Symbolic arguments() method

archive/issues_009126.json:
```json
{
    "body": "Assignee: @burcin\n\nRight now, the following works:\n\n```\nsage: a=(x+y)\nsage: a.arguments()\n(x, y)\n```\n\nHowever, we deprecated the following a long time ago:\n\n```\nsage: a(1,2)\n/Users/grout/sage/local/lib/python2.6/site-packages/IPython/iplib.py:2073:\nDeprecationWarning: Substitution using function-call syntax and unnamed\narguments is deprecated and will be removed from a future release of\nSage; you can use named arguments instead, like EXPR(x=..., y=...)\n   exec code_obj in self.user_global_ns, self.user_ns\n3\n```\n\nI propose that a.arguments() should return a deprecation warning:\n\n```\nsage: a.arguments()\n/Users/grout/sage/local/lib/python2.6/site-packages/IPython/iplib.py:2073:\nDeprecationWarning: (Since Sage version 4.4.2) symbolic expressions do\nnot have default callable arguments.  Please use the variables() method\n   exec code_obj in self.user_global_ns, self.user_ns\n(x, y)\n```\n\nThis will impact other things as well, since apparently things have been\nusing .arguments() when they should have been using .variables().  I can\npost a patch for this.  Here, I'm just calling for comment, especially\nfrom those that think this will mess everything up in some way.\n\nNote that callable functions will still have sensible return values:\n\n```\nsage: f(x,y)=x+y\nsage: f.arguments()\n(x, y) \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9126\n\n",
    "created_at": "2010-06-03T05:11:07Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Symbolic arguments() method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9126",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @burcin

Right now, the following works:

```
sage: a=(x+y)
sage: a.arguments()
(x, y)
```

However, we deprecated the following a long time ago:

```
sage: a(1,2)
/Users/grout/sage/local/lib/python2.6/site-packages/IPython/iplib.py:2073:
DeprecationWarning: Substitution using function-call syntax and unnamed
arguments is deprecated and will be removed from a future release of
Sage; you can use named arguments instead, like EXPR(x=..., y=...)
   exec code_obj in self.user_global_ns, self.user_ns
3
```

I propose that a.arguments() should return a deprecation warning:

```
sage: a.arguments()
/Users/grout/sage/local/lib/python2.6/site-packages/IPython/iplib.py:2073:
DeprecationWarning: (Since Sage version 4.4.2) symbolic expressions do
not have default callable arguments.  Please use the variables() method
   exec code_obj in self.user_global_ns, self.user_ns
(x, y)
```

This will impact other things as well, since apparently things have been
using .arguments() when they should have been using .variables().  I can
post a patch for this.  Here, I'm just calling for comment, especially
from those that think this will mess everything up in some way.

Note that callable functions will still have sensible return values:

```
sage: f(x,y)=x+y
sage: f.arguments()
(x, y) 
```


Issue created by migration from https://trac.sagemath.org/ticket/9126





---

archive/issue_comments_084769.json:
```json
{
    "body": "Attachment [trac-9126-arguments.patch](tarball://root/attachments/some-uuid/ticket9126/trac-9126-arguments.patch) by @jasongrout created at 2010-06-03 05:12:31",
    "created_at": "2010-06-03T05:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9126#issuecomment-84769",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-9126-arguments.patch](tarball://root/attachments/some-uuid/ticket9126/trac-9126-arguments.patch) by @jasongrout created at 2010-06-03 05:12:31



---

archive/issue_comments_084770.json:
```json
{
    "body": "I've attached a rough patch which needs work to finish fixing the ramifications of this change.",
    "created_at": "2010-06-03T05:13:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9126#issuecomment-84770",
    "user": "https://github.com/jasongrout"
}
```

I've attached a rough patch which needs work to finish fixing the ramifications of this change.



---

archive/issue_comments_084771.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-06-03T05:13:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9126#issuecomment-84771",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_work.



---

archive/issue_events_022408.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9126",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9126#event-22408"
}
```



---

archive/issue_events_022409.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9126",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9126#event-22409"
}
```



---

archive/issue_events_022410.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9126",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9126#event-22410"
}
```



---

archive/issue_events_022411.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9126",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9126#event-22411"
}
```



---

archive/issue_events_022412.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9126",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9126#event-22412"
}
```



---

archive/issue_events_022413.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9126",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9126#event-22413"
}
```



---

archive/issue_events_022414.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9126",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9126#event-22414"
}
```



---

archive/issue_events_022415.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-09-06T05:39:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9126",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9126#event-22415"
}
```



---

archive/issue_events_022416.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-09-06T05:39:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9126",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9126#event-22416"
}
```



---

archive/issue_comments_084772.json:
```json
{
    "body": "dup of #32227, can close",
    "created_at": "2021-09-06T05:39:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9126#issuecomment-84772",
    "user": "https://github.com/mkoeppe"
}
```

dup of #32227, can close



---

archive/issue_comments_084773.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2021-09-06T05:39:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9126#issuecomment-84773",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084774.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-11-20T21:19:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9126#issuecomment-84774",
    "user": "https://github.com/orlitzky"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_022417.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-11-20T23:57:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9126",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9126#event-22417"
}
```



---

archive/issue_comments_084775.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-11-20T23:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9126",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9126#issuecomment-84775",
    "user": "https://github.com/mkoeppe"
}
```

Resolution: invalid
