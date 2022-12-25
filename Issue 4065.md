# Issue 4065: plot3d takes "forever" to plot x^2*y

archive/issues_004065.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jasongrout\n\n\n```\nsage: var('y')\nsage: plot3d(x^2*y,(-1,1),(-1,1))\n```\n\n\nThis takes for ever, even when run as the first command after restarting a notebook.  On the other hand, it takes about 1 second to do\n\n\n```\nsage: var('y')\nsage: plot3d(sin(sin(x) + y^2),(-1,1),(-1,1))\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4065\n\n",
    "created_at": "2008-09-05T01:20:27Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "plot3d takes \"forever\" to plot x^2*y",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4065",
    "user": "https://github.com/jicama"
}
```
Assignee: @williamstein

CC:  @jasongrout


```
sage: var('y')
sage: plot3d(x^2*y,(-1,1),(-1,1))
```


This takes for ever, even when run as the first command after restarting a notebook.  On the other hand, it takes about 1 second to do


```
sage: var('y')
sage: plot3d(sin(sin(x) + y^2),(-1,1),(-1,1))
```


Issue created by migration from https://trac.sagemath.org/ticket/4065





---

archive/issue_comments_029272.json:
```json
{
    "body": "What version of Sage are you running?",
    "created_at": "2008-09-05T16:42:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4065#issuecomment-29272",
    "user": "https://github.com/mwhansen"
}
```

What version of Sage are you running?



---

archive/issue_comments_029273.json:
```json
{
    "body": "3.1.2.alpha2",
    "created_at": "2008-09-05T17:03:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4065#issuecomment-29273",
    "user": "https://github.com/jicama"
}
```

3.1.2.alpha2



---

archive/issue_comments_029274.json:
```json
{
    "body": "Yep, this computation still calls Maxima. Any idea why _fast_float is not used?\n\nCheers,\n\nMichael",
    "created_at": "2008-09-09T04:56:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4065#issuecomment-29274",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Yep, this computation still calls Maxima. Any idea why _fast_float is not used?

Cheers,

Michael



---

archive/issue_comments_029275.json:
```json
{
    "body": "I can't duplicate this on 3.1.2.rc0.",
    "created_at": "2008-09-09T05:07:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4065#issuecomment-29275",
    "user": "https://github.com/mwhansen"
}
```

I can't duplicate this on 3.1.2.rc0.



---

archive/issue_comments_029276.json:
```json
{
    "body": "On bsd\n\n\n```\nsage: var('y')\ny\nsage: %time p = plot3d(x^2*y,(-1,1),(-1,1))\nCPU times: user 0.16 s, sys: 0.08 s, total: 0.24 s\nWall time: 0.78 s\nsage: %time p = plot3d(x^2*y,(-1,1),(-1,1))\nCPU times: user 0.14 s, sys: 0.06 s, total: 0.21 s\nWall time: 0.44 s\nsage: %time p = plot3d(x^2*y,(-1,1),(-1,1))\nCPU times: user 0.15 s, sys: 0.07 s, total: 0.22 s\nWall time: 0.48 s\n```\n",
    "created_at": "2008-09-09T05:08:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4065#issuecomment-29276",
    "user": "https://github.com/mwhansen"
}
```

On bsd


```
sage: var('y')
y
sage: %time p = plot3d(x^2*y,(-1,1),(-1,1))
CPU times: user 0.16 s, sys: 0.08 s, total: 0.24 s
Wall time: 0.78 s
sage: %time p = plot3d(x^2*y,(-1,1),(-1,1))
CPU times: user 0.14 s, sys: 0.06 s, total: 0.21 s
Wall time: 0.44 s
sage: %time p = plot3d(x^2*y,(-1,1),(-1,1))
CPU times: user 0.15 s, sys: 0.07 s, total: 0.22 s
Wall time: 0.48 s
```




---

archive/issue_comments_029277.json:
```json
{
    "body": "This is very strange to say the least:\n\n```\nsage: time p=plot3d(sin(sin(x) + y^2),(-1,1),(-1,1))\nCPU times: user 0.34 s, sys: 0.08 s, total: 0.42 s\nWall time: 3.07 s\nsage: %time p = plot3d(x^2*y,(-1,1),(-1,1))\nCPU times: user 0.16 s, sys: 0.06 s, total: 0.22 s\nWall time: 1.61 s\n```\n\nI must have started an old Sage. If someone can reproduce this with Sage 3.1.2.rc0 or later please give detailed information how to reproduce this. Fixed.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-09T05:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4065#issuecomment-29277",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is very strange to say the least:

```
sage: time p=plot3d(sin(sin(x) + y^2),(-1,1),(-1,1))
CPU times: user 0.34 s, sys: 0.08 s, total: 0.42 s
Wall time: 3.07 s
sage: %time p = plot3d(x^2*y,(-1,1),(-1,1))
CPU times: user 0.16 s, sys: 0.06 s, total: 0.22 s
Wall time: 1.61 s
```

I must have started an old Sage. If someone can reproduce this with Sage 3.1.2.rc0 or later please give detailed information how to reproduce this. Fixed.

Cheers,

Michael



---

archive/issue_comments_029278.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-09T05:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4065#issuecomment-29278",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004299.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-09-09T05:21:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4065",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4065#event-4299"
}
```



---

archive/issue_comments_029279.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-09-09T20:04:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4065#issuecomment-29279",
    "user": "https://github.com/jicama"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_029280.json:
```json
{
    "body": "I just reproduced this problem on a freshly built 3.1.2.rc1, on OS X 10.5.4 intel macbook.  All I did was start sage in the terminal:\n\n\n```\nsage: version()\n'SAGE Version 3.1.2.rc1, Release Date: 2008-09-08'\nsage: var('y')\ny\nsage: plot3d(x^2*y,(-1,1),(-1,1))\n```\n\n\nThis is still going 5 minutes later.  There is a process called lisp.run eating up about 90% of my processor power, with memory usage steady around 17 MB.  The same thing happens in the notebook.  Pressinc ctrl-c gives\n\n\n```\nControl-C pressed.  Interrupting Maxima. Please wait a few seconds...\n```\n\n\nWhich also seems to persist indefinitely.  I eventually killed things by closing the terminal window.\n\nHere's something else that takes virtually no time to run:\n\n\n```\nsage: plot3d(x^2*y,(x,-1,1),(y,-1,1))\n```\n\n\nBut these commands also run indefinitely\n\n\n```\nsage: plot3d(x + y,(-1,1),(-1,1))\nsage: plot3d(y*x,(-1,1),(-1,1))\n```\n",
    "created_at": "2008-09-09T20:04:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4065#issuecomment-29280",
    "user": "https://github.com/jicama"
}
```

I just reproduced this problem on a freshly built 3.1.2.rc1, on OS X 10.5.4 intel macbook.  All I did was start sage in the terminal:


```
sage: version()
'SAGE Version 3.1.2.rc1, Release Date: 2008-09-08'
sage: var('y')
y
sage: plot3d(x^2*y,(-1,1),(-1,1))
```


This is still going 5 minutes later.  There is a process called lisp.run eating up about 90% of my processor power, with memory usage steady around 17 MB.  The same thing happens in the notebook.  Pressinc ctrl-c gives


```
Control-C pressed.  Interrupting Maxima. Please wait a few seconds...
```


Which also seems to persist indefinitely.  I eventually killed things by closing the terminal window.

Here's something else that takes virtually no time to run:


```
sage: plot3d(x^2*y,(x,-1,1),(y,-1,1))
```


But these commands also run indefinitely


```
sage: plot3d(x + y,(-1,1),(-1,1))
sage: plot3d(y*x,(-1,1),(-1,1))
```




---

archive/issue_comments_029281.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-09-09T20:04:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4065#issuecomment-29281",
    "user": "https://github.com/jicama"
}
```

Changing status from closed to reopened.



---

archive/issue_events_004300.json:
```json
{
    "actor": "@jicama",
    "created_at": "2008-09-09T20:04:37Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/4065",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4065#event-4300"
}
```



---

archive/issue_comments_029282.json:
```json
{
    "body": "Changing assignee from @williamstein to @jicama.",
    "created_at": "2008-09-09T20:58:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4065#issuecomment-29282",
    "user": "https://github.com/jicama"
}
```

Changing assignee from @williamstein to @jicama.



---

archive/issue_comments_029283.json:
```json
{
    "body": "Changing status from reopened to new.",
    "created_at": "2008-09-09T20:58:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4065#issuecomment-29283",
    "user": "https://github.com/jicama"
}
```

Changing status from reopened to new.



---

archive/issue_comments_029284.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-10-31T19:30:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4065#issuecomment-29284",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: invalid



---

archive/issue_events_004301.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-10-31T19:30:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4065",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4065#event-4301"
}
```



---

archive/issue_comments_029285.json:
```json
{
    "body": "The problem here is likely a clisp linked against either the system or a MacPorts/Fink libpng.dylib. Various people have attempted to reproduce this problem and have failed. So I am closing it as invalid since one can no longer build with MacPorts/Fink in $PATH.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T19:30:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4065#issuecomment-29285",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The problem here is likely a clisp linked against either the system or a MacPorts/Fink libpng.dylib. Various people have attempted to reproduce this problem and have failed. So I am closing it as invalid since one can no longer build with MacPorts/Fink in $PATH.

Cheers,

Michael
