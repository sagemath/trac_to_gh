# Issue 567: ode_solver: display a user-friendly error message if the jacobian is not provided for the bsimp algorithm

archive/issues_000567.json:
```json
{
    "body": "Assignee: @williamstein\n\nWhen using ode_solve with the algorithm 'bsimp' that requires the jacobian to be provided, \nan error  of type ValueError with the message 'error solving'. It would be more user-friendly to\ncheck if the jacobian has been provided, and display a more specific error message.\n\nExample:\n\nsage: f= lambda t,y :[y[1],-y[0]]\nsage: T=ode_solver()\nsage: T.function=f\nsage: T.algorithm='bsimp'\nsage: T.ode_solve(y_\n0=[1,0],t_span=[0,2*pi],num_points=100)\n---------------------------------------------------------------------------\n<type 'exceptions.ValueError'>            Traceback (most recent call last)\n\n/hdc3/pablo.hdc3/sage.new/sage-2.8.3.rc3/<ipython console> in <module>()\n\n/hdc3/pablo.hdc3/sage.new/sage-2.8.3.rc3/ode.pyx in ode.ode_solver.ode_solve()\n\n<type 'exceptions.ValueError'>: error solving\n\n\nI'm submiting a patch for this.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/567\n\n",
    "created_at": "2007-09-02T01:02:31Z",
    "labels": [
        "component: numerical",
        "trivial"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "ode_solver: display a user-friendly error message if the jacobian is not provided for the bsimp algorithm",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/567",
    "user": "https://github.com/pdenapo"
}
```
Assignee: @williamstein

When using ode_solve with the algorithm 'bsimp' that requires the jacobian to be provided, 
an error  of type ValueError with the message 'error solving'. It would be more user-friendly to
check if the jacobian has been provided, and display a more specific error message.

Example:

sage: f= lambda t,y :[y[1],-y[0]]
sage: T=ode_solver()
sage: T.function=f
sage: T.algorithm='bsimp'
sage: T.ode_solve(y_
0=[1,0],t_span=[0,2*pi],num_points=100)
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/hdc3/pablo.hdc3/sage.new/sage-2.8.3.rc3/<ipython console> in <module>()

/hdc3/pablo.hdc3/sage.new/sage-2.8.3.rc3/ode.pyx in ode.ode_solver.ode_solve()

<type 'exceptions.ValueError'>: error solving


I'm submiting a patch for this.



Issue created by migration from https://trac.sagemath.org/ticket/567





---

archive/issue_events_000615.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-09-05T05:02:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/567",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/567#event-615"
}
```



---

archive/issue_comments_002930.json:
```json
{
    "body": "Attachment [ode_solver_jacobian.patch](tarball://root/attachments/some-uuid/ticket567/ode_solver_jacobian.patch) by @williamstein created at 2007-09-05 05:02:08",
    "created_at": "2007-09-05T05:02:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/567#issuecomment-2930",
    "user": "https://github.com/williamstein"
}
```

Attachment [ode_solver_jacobian.patch](tarball://root/attachments/some-uuid/ticket567/ode_solver_jacobian.patch) by @williamstein created at 2007-09-05 05:02:08



---

archive/issue_comments_002931.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-05T05:02:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/567",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/567#issuecomment-2931",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
