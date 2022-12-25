# Issue 4095: Major bug in GF(109)['x', 'y']

archive/issues_004095.json:
```json
{
    "body": "Assignee: somebody\n\nNick Alexander reported in http://groups.google.com/group/sage-devel/t/66e73453bc0b863a\n\n```\nsage: GF(109)['x', 'y'](-10)\n-10\nsage: GF(109)['x'](-10)\n99\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4095\n\n",
    "created_at": "2008-09-10T02:22:42Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Major bug in GF(109)['x', 'y']",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4095",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: somebody

Nick Alexander reported in http://groups.google.com/group/sage-devel/t/66e73453bc0b863a

```
sage: GF(109)['x', 'y'](-10)
-10
sage: GF(109)['x'](-10)
99
```


Issue created by migration from https://trac.sagemath.org/ticket/4095





---

archive/issue_comments_029483.json:
```json
{
    "body": "Michael Brickenstein wrote on [sage-devel]:\n\n```\nok, it isn't normalize, but a very small function called npWrite\n\nvoid npWrite (number &a)\n{\n\u00a0 if ((long)a > (npPrimeM >>1)) StringAppend(\"-%d\",(int)(npPrimeM-\n((long)a)));\n\u00a0 else \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0StringAppend(\"%d\",(int)((long)a));\n}\n\nThis is set to the current ring\nin numbers.cc\nn->nWrite = npWrite;\nIt should just affect the output, so I think would be okay to change it.\n```\n",
    "created_at": "2008-09-15T17:45:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4095#issuecomment-29483",
    "user": "https://github.com/malb"
}
```

Michael Brickenstein wrote on [sage-devel]:

```
ok, it isn't normalize, but a very small function called npWrite

void npWrite (number &a)
{
  if ((long)a > (npPrimeM >>1)) StringAppend("-%d",(int)(npPrimeM-
((long)a)));
  else                          StringAppend("%d",(int)((long)a));
}

This is set to the current ring
in numbers.cc
n->nWrite = npWrite;
It should just affect the output, so I think would be okay to change it.
```




---

archive/issue_comments_029484.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:18:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4095",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4095#issuecomment-29484",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_events_009336.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4095",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4095#event-9336"
}
```



---

archive/issue_events_009337.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4095",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4095#event-9337"
}
```



---

archive/issue_events_009338.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4095",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4095#event-9338"
}
```



---

archive/issue_events_009339.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4095",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4095#event-9339"
}
```



---

archive/issue_events_009340.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4095",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4095#event-9340"
}
```



---

archive/issue_events_009341.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4095",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4095#event-9341"
}
```



---

archive/issue_events_009342.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4095",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4095#event-9342"
}
```
