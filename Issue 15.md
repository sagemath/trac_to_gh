# Issue 15: sin(integer) precision issue

archive/issues_000015.json:
```json
{
    "body": "Assignee: somebody\n\nI don't like how SAGE works for this (see below) (example from Fateman's mathematica review):\n   {{{\n     sage: sin(3141592653589793238.0)   # very good\n     -0.4463151633593201122015 \n     sage: float(sin(3141592653589793238))   # very bad\n     -0.64165348191050475\n   }}}\n   The problem is that SAGE is using the Python math library, which is the C library, which has\n   precision issues.   The fix is to change sin(integer) to use mpfr.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/15\n\n",
    "created_at": "2006-09-12T23:15:45Z",
    "labels": [
        "component: basic arithmetic",
        "minor",
        "bug"
    ],
    "title": "sin(integer) precision issue",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/15",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

I don't like how SAGE works for this (see below) (example from Fateman's mathematica review):
   {{{
     sage: sin(3141592653589793238.0)   # very good
     -0.4463151633593201122015 
     sage: float(sin(3141592653589793238))   # very bad
     -0.64165348191050475
   }}}
   The problem is that SAGE is using the Python math library, which is the C library, which has
   precision issues.   The fix is to change sin(integer) to use mpfr.


Issue created by migration from https://trac.sagemath.org/ticket/15





---

archive/issue_events_000015.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2006-10-15T17:40:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/15",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/15#event-15"
}
```



---

archive/issue_comments_000066.json:
```json
{
    "body": "I don't want to change this.  Keeping it as it is stays very clean; changing it introduces all kinds of subtle issues that could be even more confusing in the long run.",
    "created_at": "2006-10-15T17:40:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/15",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/15#issuecomment-66",
    "user": "https://github.com/williamstein"
}
```

I don't want to change this.  Keeping it as it is stays very clean; changing it introduces all kinds of subtle issues that could be even more confusing in the long run.



---

archive/issue_comments_000067.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2006-10-15T17:40:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/15",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/15#issuecomment-67",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
