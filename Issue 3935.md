# Issue 3935: ode_solver __init__ method ignores many parameters

archive/issues_003935.json:
```json
{
    "body": "Assignee: jkantor\n\nThe following example comes from the in-source documentation for ode_solver:\n\n\n```\nsage: T = ode_solver()\nsage: g_1= lambda t,y: [y[1]*y[2],-y[0]*y[2],-0.51*y[0]*y[1]]\nsage: T.function=g_1\nsage: T.y_0=[0,1,1]\nsage: T.scale_abs=[1e-4,1e-4,1e-5]\nsage: T.error_rel=1e-4\nsage: T.ode_solve(t_span=[0,12],num_points=100)\nsage: f = T.interpolate_solution()\nsage: f(pi)              # slightly random precision\n0.53794725135406318\n```\n\n\nIt should be possible to set these attributes using arguments to the constructor, but this fails:\n\n\n```\nsage: T = ode_solver(g_1,y_0=[0,1,1],scale_abs=[1e-4,1e-4,1e-5],error_rel=1e-4)\nsage: T.ode_solve(t_span=[0,12],num_points=100)\nsage: f = T.interpolate_solution()\nsage: f(pi)\nTraceback (click to the left for traceback)\n...\nTypeError: object of type 'NoneType' has no len()\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3935\n\n",
    "created_at": "2008-08-23T18:38:38Z",
    "labels": [
        "component: numerical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "ode_solver __init__ method ignores many parameters",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3935",
    "user": "https://github.com/jicama"
}
```
Assignee: jkantor

The following example comes from the in-source documentation for ode_solver:


```
sage: T = ode_solver()
sage: g_1= lambda t,y: [y[1]*y[2],-y[0]*y[2],-0.51*y[0]*y[1]]
sage: T.function=g_1
sage: T.y_0=[0,1,1]
sage: T.scale_abs=[1e-4,1e-4,1e-5]
sage: T.error_rel=1e-4
sage: T.ode_solve(t_span=[0,12],num_points=100)
sage: f = T.interpolate_solution()
sage: f(pi)              # slightly random precision
0.53794725135406318
```


It should be possible to set these attributes using arguments to the constructor, but this fails:


```
sage: T = ode_solver(g_1,y_0=[0,1,1],scale_abs=[1e-4,1e-4,1e-5],error_rel=1e-4)
sage: T.ode_solve(t_span=[0,12],num_points=100)
sage: f = T.interpolate_solution()
sage: f(pi)
Traceback (click to the left for traceback)
...
TypeError: object of type 'NoneType' has no len()
```


Issue created by migration from https://trac.sagemath.org/ticket/3935





---

archive/issue_comments_028142.json:
```json
{
    "body": "Attachment [ode_solver_patch.patch](tarball://root/attachments/some-uuid/ticket3935/ode_solver_patch.patch) by @jicama created at 2008-08-23 18:39:15\n\nAdds a doctest and fixes the __init__ method",
    "created_at": "2008-08-23T18:39:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3935#issuecomment-28142",
    "user": "https://github.com/jicama"
}
```

Attachment [ode_solver_patch.patch](tarball://root/attachments/some-uuid/ticket3935/ode_solver_patch.patch) by @jicama created at 2008-08-23 18:39:15

Adds a doctest and fixes the __init__ method



---

archive/issue_comments_028143.json:
```json
{
    "body": "One thing I'm worried about is that the tests for ode.pyx already take a long time (more than two minutes), and this makes them take even longer.",
    "created_at": "2008-08-23T18:41:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3935#issuecomment-28143",
    "user": "https://github.com/jicama"
}
```

One thing I'm worried about is that the tests for ode.pyx already take a long time (more than two minutes), and this makes them take even longer.



---

archive/issue_comments_028144.json:
```json
{
    "body": "This seems to work and doctests pass.  However, the given example is not the same as the example before (as the docs claim), since the algorithm used is different.  The referee patch adds an algorithm keyword to make it the same.  Apply the referee patch after the original patch and then it is positive review.",
    "created_at": "2008-08-27T15:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3935#issuecomment-28144",
    "user": "https://github.com/jasongrout"
}
```

This seems to work and doctests pass.  However, the given example is not the same as the example before (as the docs claim), since the algorithm used is different.  The referee patch adds an algorithm keyword to make it the same.  Apply the referee patch after the original patch and then it is positive review.



---

archive/issue_comments_028145.json:
```json
{
    "body": "Attachment [ode_solver_patch-referee.patch](tarball://root/attachments/some-uuid/ticket3935/ode_solver_patch-referee.patch) by @jasongrout created at 2008-08-27 15:49:49\n\njwmerrill, related to the docs of ode_solver, could you review #3966?  Thanks.",
    "created_at": "2008-08-27T15:49:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3935#issuecomment-28145",
    "user": "https://github.com/jasongrout"
}
```

Attachment [ode_solver_patch-referee.patch](tarball://root/attachments/some-uuid/ticket3935/ode_solver_patch-referee.patch) by @jasongrout created at 2008-08-27 15:49:49

jwmerrill, related to the docs of ode_solver, could you review #3966?  Thanks.



---

archive/issue_comments_028146.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-27T22:08:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3935#issuecomment-28146",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_028147.json:
```json
{
    "body": "Merged both patches in Sage 3.1.2.alpha2",
    "created_at": "2008-08-27T22:08:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3935",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3935#issuecomment-28147",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.1.2.alpha2
