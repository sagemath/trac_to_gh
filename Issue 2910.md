# Issue 2910: bug in Integer(string)

archive/issues_002910.json:
```json
{
    "body": "Assignee: @robertwb\n\nCC:  timothyclemans\n\nThis behavior is inconsistent and could lead to horrible bugs:\n\n```\nsage: int('070')\n70\nsage: Integer('070')\n56\n```\n\n\nBecause Sage uses Python instead of inventing its own language, there\nare issues like this.   The only options to fix this problem\nare (a) make int('070') return 56 or (b) make Integer('070') return 70.\nIrregardless of what Sage *should* do, (a) is not an option since it\nrequires changing the Python interpreter, and an axiom of Sage development\nis that we will never do that.  So (b) it is.   To resolve this trac tick\none must thus do (b).\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2910\n\n",
    "created_at": "2008-04-13T19:11:36Z",
    "labels": [
        "component: coercion",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "bug in Integer(string)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2910",
    "user": "https://github.com/williamstein"
}
```
Assignee: @robertwb

CC:  timothyclemans

This behavior is inconsistent and could lead to horrible bugs:

```
sage: int('070')
70
sage: Integer('070')
56
```


Because Sage uses Python instead of inventing its own language, there
are issues like this.   The only options to fix this problem
are (a) make int('070') return 56 or (b) make Integer('070') return 70.
Irregardless of what Sage *should* do, (a) is not an option since it
requires changing the Python interpreter, and an axiom of Sage development
is that we will never do that.  So (b) it is.   To resolve this trac tick
one must thus do (b).



Issue created by migration from https://trac.sagemath.org/ticket/2910





---

archive/issue_comments_020009.json:
```json
{
    "body": "Ugh. This means\n\n\n```\nsage: Integer('070') == Integer(070)\nFalse\n```\n\n\nSo be it I guess...",
    "created_at": "2008-05-01T05:24:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2910#issuecomment-20009",
    "user": "https://github.com/robertwb"
}
```

Ugh. This means


```
sage: Integer('070') == Integer(070)
False
```


So be it I guess...



---

archive/issue_comments_020010.json:
```json
{
    "body": "A PEP deals with this:\n\nhttp://mail.python.org/pipermail/python-3000/2007-March/006444.html\n\n\n```\nDuring the present discussion, it was almost universally agreed that::\n\n    eval('010') == 8\n\nshould no longer be true, because that is confusing to new users.\n```\n\n\nAdditional thoughts?",
    "created_at": "2009-01-23T10:05:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2910#issuecomment-20010",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

A PEP deals with this:

http://mail.python.org/pipermail/python-3000/2007-March/006444.html


```
During the present discussion, it was almost universally agreed that::

    eval('010') == 8

should no longer be true, because that is confusing to new users.
```


Additional thoughts?



---

archive/issue_comments_020011.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2009-01-23T10:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2910#issuecomment-20011",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Resolution: wontfix



---

archive/issue_events_006668.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/boothby",
    "created_at": "2009-01-23T10:10:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2910",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2910#event-6668"
}
```



---

archive/issue_comments_020012.json:
```json
{
    "body": "William said \"hobgoblin something something consistency foolish something.  close it as wontfix\".",
    "created_at": "2009-01-23T10:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2910#issuecomment-20012",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

William said "hobgoblin something something consistency foolish something.  close it as wontfix".



---

archive/issue_comments_020013.json:
```json
{
    "body": "+1 to wontfix for me",
    "created_at": "2009-01-23T10:16:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2910#issuecomment-20013",
    "user": "https://github.com/robertwb"
}
```

+1 to wontfix for me



---

archive/issue_events_006669.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-23T10:55:19Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2910",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2910#event-6669"
}
```
