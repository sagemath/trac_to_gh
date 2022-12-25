# Issue 5312: command line -- bug in preparser and "time"

archive/issues_005312.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @orlitzky\n\nThere is a weird interaction between time and preparser, almost as if input to time is being preparsed *twice*:\n\n```\nwstein@sage:~/build/sage-3.3.rc1$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: k = 3r\nsage: type(k)\n<type 'int'>\nsage: time k = 3r\nCPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s\nWall time: 0.00 s\nsage: type(k)\n<type 'sage.rings.integer.Integer'>\nsage: preparse('k = 3r')\n'k = 3'\nsage: preparse('time k = 3r')\n'time k = 3'\n```\n| Sage Version 3.3.rc1, Release Date: 2009-02-16                     |\n| Type notebook() for the GUI, and license() for information.        |\nIn the above, type(k) should have been int in all cases.  Why isn't it the second time.  WEIRD.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5312\n\n",
    "closed_at": "2013-07-23T12:21:53Z",
    "created_at": "2009-02-19T08:31:41Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "command line -- bug in preparser and \"time\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5312",
    "user": "https://github.com/williamstein"
}
```
Assignee: cwitty

CC:  @orlitzky

There is a weird interaction between time and preparser, almost as if input to time is being preparsed *twice*:

```
wstein@sage:~/build/sage-3.3.rc1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: k = 3r
sage: type(k)
<type 'int'>
sage: time k = 3r
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
sage: type(k)
<type 'sage.rings.integer.Integer'>
sage: preparse('k = 3r')
'k = 3'
sage: preparse('time k = 3r')
'time k = 3'
```
| Sage Version 3.3.rc1, Release Date: 2009-02-16                     |
| Type notebook() for the GUI, and license() for information.        |
In the above, type(k) should have been int in all cases.  Why isn't it the second time.  WEIRD.

Issue created by migration from https://trac.sagemath.org/ticket/5312





---

archive/issue_comments_040835.json:
```json
{
    "body": "This works now:\n\n```\nsage: k = 3r\nsage: type(k)\n<type 'int'>\nsage: time k = 3r\nTime: CPU 0.00 s, Wall: 0.00 s\nsage: type(k)\n<type 'int'>\n```\n\nWhere's the best place to add a doctest?",
    "created_at": "2012-01-09T02:17:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5312",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5312#issuecomment-40835",
    "user": "https://github.com/orlitzky"
}
```

This works now:

```
sage: k = 3r
sage: type(k)
<type 'int'>
sage: time k = 3r
Time: CPU 0.00 s, Wall: 0.00 s
sage: type(k)
<type 'int'>
```

Where's the best place to add a doctest?



---

archive/issue_events_012368.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2013-07-23T12:21:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5312",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5312#event-12368"
}
```



---

archive/issue_comments_040836.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-07-23T12:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5312",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5312#issuecomment-40836",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid



---

archive/issue_events_012369.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2013-07-23T12:21:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5312",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5312#event-12369"
}
```



---

archive/issue_comments_040837.json:
```json
{
    "body": "I think we can just mark it as invalid since \"%time\" is now handled by IPython.",
    "created_at": "2013-07-23T12:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5312",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5312#issuecomment-40837",
    "user": "https://github.com/mwhansen"
}
```

I think we can just mark it as invalid since "%time" is now handled by IPython.
