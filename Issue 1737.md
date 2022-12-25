# Issue 1737: ctl-c doesn't exit job in parametric_plot3d

archive/issues_001737.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe following paraterization of the Mobius strip\ntakes a very long time and won't quit when ctl-c is\nused:\n\nsage: u,v = var(\"u,v\")\nsage: parametric_plot3d([cos(u)*(1+v*cos(u/2)), sin(u)*(1+v*cos(u/2)), v*sin(u/2)], (-2, 2), (-2, 2)).show()\n^D\n^CControl-C pressed.  Interrupting Maxima. Please wait a few seconds...\n\nThis error message repeats ever time you proess ctl-c.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1737\n\n",
    "created_at": "2008-01-09T17:40:24Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "ctl-c doesn't exit job in parametric_plot3d",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1737",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: @williamstein

The following paraterization of the Mobius strip
takes a very long time and won't quit when ctl-c is
used:

sage: u,v = var("u,v")
sage: parametric_plot3d([cos(u)*(1+v*cos(u/2)), sin(u)*(1+v*cos(u/2)), v*sin(u/2)], (-2, 2), (-2, 2)).show()
^D
^CControl-C pressed.  Interrupting Maxima. Please wait a few seconds...

This error message repeats ever time you proess ctl-c.

Issue created by migration from https://trac.sagemath.org/ticket/1737





---

archive/issue_comments_010964.json:
```json
{
    "body": "This works much faster:\nsage: parametric_plot3d([0.5*cos(u)*(1+v*cos(u/2)), 0.5*sin(u)*(1+v*cos(u/2)), v*sin(u/2)], (u,-2, 2), (v,-2, 2)).show()\n\nand is more efficient.",
    "created_at": "2008-01-09T18:10:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1737#issuecomment-10964",
    "user": "https://github.com/wdjoyner"
}
```

This works much faster:
sage: parametric_plot3d([0.5*cos(u)*(1+v*cos(u/2)), 0.5*sin(u)*(1+v*cos(u/2)), v*sin(u/2)], (u,-2, 2), (v,-2, 2)).show()

and is more efficient.



---

archive/issue_comments_010965.json:
```json
{
    "body": "This is fixed by #1833.",
    "created_at": "2008-01-18T16:24:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1737#issuecomment-10965",
    "user": "https://github.com/williamstein"
}
```

This is fixed by #1833.



---

archive/issue_events_001895.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-21T04:13:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1737",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1737#event-1895"
}
```



---

archive/issue_comments_010966.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-21T04:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1737#issuecomment-10966",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010967.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha1 (patch from #1833)",
    "created_at": "2008-01-21T04:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1737",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1737#issuecomment-10967",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha1 (patch from #1833)
