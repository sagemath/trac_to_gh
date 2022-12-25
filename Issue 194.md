# Issue 194: another ZZ[x] crash

archive/issues_000194.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: R.<x> = ZZ['x']\nsage: x^3 % 2\nDivRem: quotient undefined over ZZ\n/Users/nalexand/Devel/sage/local/bin/sage-sage: line 174: 13174 Abort\ntrap              sage-ipython -c \"$SAGE_STARTUP_COMMAND;\" \"$@\"\n \nYikes!\nNick\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/194\n\n",
    "created_at": "2007-01-16T05:45:56Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-1.9",
    "title": "another ZZ[x] crash",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/194",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody


```
sage: R.<x> = ZZ['x']
sage: x^3 % 2
DivRem: quotient undefined over ZZ
/Users/nalexand/Devel/sage/local/bin/sage-sage: line 174: 13174 Abort
trap              sage-ipython -c "$SAGE_STARTUP_COMMAND;" "$@"
 
Yikes!
Nick
```


Issue created by migration from https://trac.sagemath.org/ticket/194





---

archive/issue_events_000203.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-01-25T19:09:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/194",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/194#event-203"
}
```



---

archive/issue_comments_000884.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-25T19:09:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/194#issuecomment-884",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_000885.json:
```json
{
    "body": "Fixed by re-enabling sig handling behavior.",
    "created_at": "2007-01-25T19:09:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/194",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/194#issuecomment-885",
    "user": "https://github.com/williamstein"
}
```

Fixed by re-enabling sig handling behavior.
