# Issue 711: control-c and singular interface -- it doesn't quit singular for real.

archive/issues_000711.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: P = PolynomialRing(QQ,10,'x')\nsage:  I = sage.rings.ideal.Katsura(P)\nsage: I.groebner_basis()\nInterrupting Singular...\nInterrupting Singular...\n\n<type 'exceptions.TypeError'>: Restarting Singular (WARNING: all variables defined in previous session are now invalid)\n```\n\nbut singular is still running!\n\nIssue created by migration from https://trac.sagemath.org/ticket/711\n\n",
    "created_at": "2007-09-20T18:19:40Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.5",
    "title": "control-c and singular interface -- it doesn't quit singular for real.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/711",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
sage: P = PolynomialRing(QQ,10,'x')
sage:  I = sage.rings.ideal.Katsura(P)
sage: I.groebner_basis()
Interrupting Singular...
Interrupting Singular...

<type 'exceptions.TypeError'>: Restarting Singular (WARNING: all variables defined in previous session are now invalid)
```

but singular is still running!

Issue created by migration from https://trac.sagemath.org/ticket/711





---

archive/issue_events_001901.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-21T01:01:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/711",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/711#event-1901"
}
```



---

archive/issue_comments_003718.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-21T01:01:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/711",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/711#issuecomment-3718",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
