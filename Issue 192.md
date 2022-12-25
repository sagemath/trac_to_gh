# Issue 192: polynomial arithmetic bug

archive/issues_000192.json:
```json
{
    "body": "Assignee: somebody\n\nFrom Nick A:\n\n```\nHere's a similar error.  I haven't tried with that patch, but my\nspidey-sense suggests a different issue:\n \nsage: R.<x> = Integers(5**2)['x']\nsage: S.<xbar> = R.quo(x^5 - x + 1)\nsage: (5*xbar + 1).lift() % 5\nZZ_p: division by non-invertible element\n/Users/nalexand/Devel/sage/local/bin/sage-sage: line 174: 10371 Abort\ntrap              sage-ipython -c \"$SAGE_STARTUP_COMMAND;\" \"$@\"\n \nNick\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/192\n\n",
    "closed_at": "2007-01-21T21:51:17Z",
    "created_at": "2007-01-15T08:40:06Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-1.8",
    "title": "polynomial arithmetic bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/192",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

From Nick A:

```
Here's a similar error.  I haven't tried with that patch, but my
spidey-sense suggests a different issue:
 
sage: R.<x> = Integers(5**2)['x']
sage: S.<xbar> = R.quo(x^5 - x + 1)
sage: (5*xbar + 1).lift() % 5
ZZ_p: division by non-invertible element
/Users/nalexand/Devel/sage/local/bin/sage-sage: line 174: 10371 Abort
trap              sage-ipython -c "$SAGE_STARTUP_COMMAND;" "$@"
 
Nick
```

Issue created by migration from https://trac.sagemath.org/ticket/192





---

archive/issue_comments_000877.json:
```json
{
    "body": "Changing assignee from @williamstein to somebody.",
    "created_at": "2007-01-15T08:40:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/192#issuecomment-877",
    "user": "https://github.com/williamstein"
}
```

Changing assignee from @williamstein to somebody.



---

archive/issue_comments_000878.json:
```json
{
    "body": "Changing component from algebraic geometry to basic arithmetic.",
    "created_at": "2007-01-15T08:40:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/192#issuecomment-878",
    "user": "https://github.com/williamstein"
}
```

Changing component from algebraic geometry to basic arithmetic.



---

archive/issue_comments_000879.json:
```json
{
    "body": "This will be fixed automatically by fixing trac #196.",
    "created_at": "2007-01-19T09:54:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/192#issuecomment-879",
    "user": "https://github.com/williamstein"
}
```

This will be fixed automatically by fixing trac #196.



---

archive/issue_events_000378.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-01-19T09:57:43Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/192",
    "milestone": "sage-1.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/192#event-378"
}
```



---

archive/issue_comments_000880.json:
```json
{
    "body": "Fixed by fixing trac #196.",
    "created_at": "2007-01-21T21:51:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/192#issuecomment-880",
    "user": "https://github.com/williamstein"
}
```

Fixed by fixing trac #196.



---

archive/issue_comments_000881.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-21T21:51:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/192",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/192#issuecomment-881",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000379.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-01-21T21:51:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/192",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/192#event-379"
}
```
