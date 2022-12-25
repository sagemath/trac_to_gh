# Issue 4413: '?' in docstring gets interpreted immediately by the parser

archive/issues_004413.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe following code, entered in the command-line interface to Sage, shows the effect:\n\n```\nsage: def foo(x):\n   ....:     '''\n   ....:     Eh?\nObject `Eh` not found.\n   ....:     '''\n   ....:     return x\n   ....: \n```\n\nThe parser appears to act on the '?' right away, rather than wait for the end of the thing being defined (or realizing that '?' in this case is not to be acted on).\n\nThe effect shows up with both single- and double- quotes, and with and without the \"raw\" qualifier (r!''').\n\nThis may be related to Trac#4405.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4413\n\n",
    "created_at": "2008-10-31T21:05:37Z",
    "labels": [
        "component: user interface",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "'?' in docstring gets interpreted immediately by the parser",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4413",
    "user": "https://trac.sagemath.org/admin/accounts/users/justin"
}
```
Assignee: @williamstein

The following code, entered in the command-line interface to Sage, shows the effect:

```
sage: def foo(x):
   ....:     '''
   ....:     Eh?
Object `Eh` not found.
   ....:     '''
   ....:     return x
   ....: 
```

The parser appears to act on the '?' right away, rather than wait for the end of the thing being defined (or realizing that '?' in this case is not to be acted on).

The effect shows up with both single- and double- quotes, and with and without the "raw" qualifier (r!''').

This may be related to Trac#4405.



Issue created by migration from https://trac.sagemath.org/ticket/4413





---

archive/issue_comments_032402.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-23T13:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4413#issuecomment-32402",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032403.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2009-01-23T13:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4413#issuecomment-32403",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_032404.json:
```json
{
    "body": "This is not related to #4405.  In fact, it is an IPython bug.  I've reported it here: http://lists.ipython.scipy.org/pipermail/ipython-dev/2009-January/004812.html",
    "created_at": "2009-01-23T13:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4413#issuecomment-32404",
    "user": "https://github.com/mwhansen"
}
```

This is not related to #4405.  In fact, it is an IPython bug.  I've reported it here: http://lists.ipython.scipy.org/pipermail/ipython-dev/2009-January/004812.html



---

archive/issue_comments_032405.json:
```json
{
    "body": "This is fixed in IPython 0.12.  We should close this when #12719 gets closed.",
    "created_at": "2012-03-29T07:46:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4413#issuecomment-32405",
    "user": "https://github.com/mwhansen"
}
```

This is fixed in IPython 0.12.  We should close this when #12719 gets closed.



---

archive/issue_comments_032406.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-03-29T07:55:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4413#issuecomment-32406",
    "user": "https://github.com/kini"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_032407.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-03-29T07:56:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4413#issuecomment-32407",
    "user": "https://github.com/kini"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_009968.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-03-29T14:43:16Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4413",
    "milestone": "sage-pending",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4413#event-9968"
}
```



---

archive/issue_events_009969.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-04-04T13:28:01Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4413",
    "milestone": "sage-pending",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4413#event-9969"
}
```



---

archive/issue_events_009970.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-04-04T13:28:01Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4413",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4413#event-9970"
}
```



---

archive/issue_comments_032408.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-01-25T09:47:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4413#issuecomment-32408",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_events_009971.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-01-25T09:47:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4413",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4413#event-9971"
}
```
