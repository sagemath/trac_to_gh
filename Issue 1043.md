# Issue 1043: constructing number field with check=False doesn't behave as it should

archive/issues_001043.json:
```json
{
    "body": "Assignee: @williamstein\n\nWhy does this take any time?  It shouldn't:\n\n\n```\nsage: p = next_prime(10^24); q = next_prime(10^26); D = p*q; D\nsage: time K.<b> = NumberField(x^2 - D, check=False)\nCPU time: 2.39 s,  Wall time: 3.10 s\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1043\n\n",
    "created_at": "2007-10-31T21:08:39Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.12",
    "title": "constructing number field with check=False doesn't behave as it should",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1043",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Why does this take any time?  It shouldn't:


```
sage: p = next_prime(10^24); q = next_prime(10^26); D = p*q; D
sage: time K.<b> = NumberField(x^2 - D, check=False)
CPU time: 2.39 s,  Wall time: 3.10 s
```


Issue created by migration from https://trac.sagemath.org/ticket/1043





---

archive/issue_comments_006331.json:
```json
{
    "body": "Robert bradshaw can easily fix this.",
    "created_at": "2007-11-03T15:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1043",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1043#issuecomment-6331",
    "user": "https://github.com/williamstein"
}
```

Robert bradshaw can easily fix this.



---

archive/issue_comments_006332.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2007-11-04T02:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1043",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1043#issuecomment-6332",
    "user": "https://github.com/robertwb"
}
```

Resolution: duplicate



---

archive/issue_events_001168.json:
```json
{
    "actor": "https://github.com/robertwb",
    "created_at": "2007-11-04T02:13:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1043",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1043#event-1168"
}
```



---

archive/issue_comments_006333.json:
```json
{
    "body": "See #1055",
    "created_at": "2007-11-04T02:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1043",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1043#issuecomment-6333",
    "user": "https://github.com/robertwb"
}
```

See #1055
