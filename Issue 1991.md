# Issue 1991: PSage -- (parallel sage): every time you create a new psage object, the first view shows it as not finished, but it is!

archive/issues_001991.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: s = PSage()\nsage: a = s('2+2')\nsage: a   # wait 10 seconds and press return\n<<currently executing code>>\nsage: a\n4\nsage: s = PSage()\nsage: a = s('2+2'); s = str(a); a\n4\n```\n\n\nNotice above that the first output of a says current executing, but that is wrong.\nIn the second, we query a, and display it and it is already done very quickly. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1991\n\n",
    "created_at": "2008-01-31T04:19:51Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "PSage -- (parallel sage): every time you create a new psage object, the first view shows it as not finished, but it is!",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1991",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
sage: s = PSage()
sage: a = s('2+2')
sage: a   # wait 10 seconds and press return
<<currently executing code>>
sage: a
4
sage: s = PSage()
sage: a = s('2+2'); s = str(a); a
4
```


Notice above that the first output of a says current executing, but that is wrong.
In the second, we query a, and display it and it is already done very quickly. 

Issue created by migration from https://trac.sagemath.org/ticket/1991





---

archive/issue_events_004798.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:34:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1991",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1991#event-4798"
}
```



---

archive/issue_events_004799.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1991",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1991#event-4799"
}
```



---

archive/issue_events_004800.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1991",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1991#event-4800"
}
```



---

archive/issue_events_004801.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:19:32Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1991",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1991#event-4801"
}
```



---

archive/issue_events_004802.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:19:32Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1991",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1991#event-4802"
}
```



---

archive/issue_events_004803.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1991",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1991#event-4803"
}
```



---

archive/issue_events_004804.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1991",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1991#event-4804"
}
```
