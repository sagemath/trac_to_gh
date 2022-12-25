# Issue 2143: [with patch, needs review] wrap scipy optimization routines and cvxopt linear programming, add gradient/hessian to calculus

archive/issues_002143.json:
```json
{
    "body": "Assignee: jkantor\n\nCC:  @dfdeshom\n\nhttp://sage.math.washington.edu/home/jkantor/optimize.patch\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2143\n\n",
    "created_at": "2008-02-12T05:33:27Z",
    "labels": [
        "component: numerical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "[with patch, needs review] wrap scipy optimization routines and cvxopt linear programming, add gradient/hessian to calculus",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2143",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```
Assignee: jkantor

CC:  @dfdeshom

http://sage.math.washington.edu/home/jkantor/optimize.patch



Issue created by migration from https://trac.sagemath.org/ticket/2143





---

archive/issue_comments_014019.json:
```json
{
    "body": "Clicking the link gives:\n\n```\nForbidden\n\nYou don't have permission to access /home/jkantor/optimize.patch on this server.\n```\n\n\nOf course, I could fix that since I'm root on that machine... but I'm too busy at the moment.",
    "created_at": "2008-02-12T05:36:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2143#issuecomment-14019",
    "user": "https://github.com/williamstein"
}
```

Clicking the link gives:

```
Forbidden

You don't have permission to access /home/jkantor/optimize.patch on this server.
```


Of course, I could fix that since I'm root on that machine... but I'm too busy at the moment.



---

archive/issue_comments_014020.json:
```json
{
    "body": "Attachment [optimize.patch](tarball://root/attachments/some-uuid/ticket2143/optimize.patch) by @dfdeshom created at 2008-03-03 21:05:13\n\nAttaching the patch on trac for convenience...",
    "created_at": "2008-03-03T21:05:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2143#issuecomment-14020",
    "user": "https://github.com/dfdeshom"
}
```

Attachment [optimize.patch](tarball://root/attachments/some-uuid/ticket2143/optimize.patch) by @dfdeshom created at 2008-03-03 21:05:13

Attaching the patch on trac for convenience...



---

archive/issue_comments_014021.json:
```json
{
    "body": "Review: \n\nDoctests were failing due to either missing imports or unsuppressed output. I'm attaching a patch where all doctests pass...",
    "created_at": "2008-03-05T05:57:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2143#issuecomment-14021",
    "user": "https://github.com/dfdeshom"
}
```

Review: 

Doctests were failing due to either missing imports or unsuppressed output. I'm attaching a patch where all doctests pass...



---

archive/issue_comments_014022.json:
```json
{
    "body": "Attachment [2143.patch](tarball://root/attachments/some-uuid/ticket2143/2143.patch) by @dfdeshom created at 2008-03-05 05:58:02",
    "created_at": "2008-03-05T05:58:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2143#issuecomment-14022",
    "user": "https://github.com/dfdeshom"
}
```

Attachment [2143.patch](tarball://root/attachments/some-uuid/ticket2143/2143.patch) by @dfdeshom created at 2008-03-05 05:58:02



---

archive/issue_comments_014023.json:
```json
{
    "body": "Attachment [2143-2.patch](tarball://root/attachments/some-uuid/ticket2143/2143-2.patch) by @mwhansen created at 2008-03-15 23:08:43",
    "created_at": "2008-03-15T23:08:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2143#issuecomment-14023",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2143-2.patch](tarball://root/attachments/some-uuid/ticket2143/2143-2.patch) by @mwhansen created at 2008-03-15 23:08:43



---

archive/issue_comments_014024.json:
```json
{
    "body": "I fixed some typos and formatting issues. Both 2143.patch and 2143-2.patch should be applied.",
    "created_at": "2008-03-15T23:09:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2143#issuecomment-14024",
    "user": "https://github.com/mwhansen"
}
```

I fixed some typos and formatting issues. Both 2143.patch and 2143-2.patch should be applied.



---

archive/issue_events_002305.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-16T02:57:15Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2143",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2143#event-2305"
}
```



---

archive/issue_comments_014025.json:
```json
{
    "body": "Merged 2143.patch and 2143-2.patch in Sage 2.10.4.rc0",
    "created_at": "2008-03-16T02:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2143#issuecomment-14025",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 2143.patch and 2143-2.patch in Sage 2.10.4.rc0



---

archive/issue_comments_014026.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-16T02:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2143#issuecomment-14026",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014027.json:
```json
{
    "body": "\n```\nsage: f(x,y)=x^2+y^2\nsage: f.gradient()\n<type 'exceptions.NotImplementedError'>:\nsage: f.parent()\nCallable function ring with arguments (x, y)\nsage: var('x,y')\nsage: g=x^2+y^2\nsage: g.gradient()\nsage: g.parent()\nSymbolic Ring\n(2*x, 2*y)\n```\n\n\nI guess this isn't a bug, just not implemented yet? I thought f(x)=x^2 was equivalent to var('x');f=x^2 but evidently they are different?",
    "created_at": "2008-03-16T03:38:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2143#issuecomment-14027",
    "user": "https://trac.sagemath.org/admin/accounts/users/edrex"
}
```


```
sage: f(x,y)=x^2+y^2
sage: f.gradient()
<type 'exceptions.NotImplementedError'>:
sage: f.parent()
Callable function ring with arguments (x, y)
sage: var('x,y')
sage: g=x^2+y^2
sage: g.gradient()
sage: g.parent()
Symbolic Ring
(2*x, 2*y)
```


I guess this isn't a bug, just not implemented yet? I thought f(x)=x^2 was equivalent to var('x');f=x^2 but evidently they are different?



---

archive/issue_comments_014028.json:
```json
{
    "body": "These are actually different things.\n\n\n```\nsage: preparse('f(x)=x^2')\n'_=var(\"x\");f=symbolic_expression(x**Integer(2)).function(x)'\nsage: preparse(\"var('x');f=x^2\")\n\"var('x');f=x**Integer(2)\"\n```\n",
    "created_at": "2008-03-16T03:40:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2143#issuecomment-14028",
    "user": "https://github.com/mwhansen"
}
```

These are actually different things.


```
sage: preparse('f(x)=x^2')
'_=var("x");f=symbolic_expression(x**Integer(2)).function(x)'
sage: preparse("var('x');f=x^2")
"var('x');f=x**Integer(2)"
```




---

archive/issue_comments_014029.json:
```json
{
    "body": "Ah... I like the f(x,y)=x<sup>2+y</sup>2 syntax/construction better, since it makes the mapping explicit for expressions which may not contain all variables. Filed as #2547",
    "created_at": "2008-03-16T16:48:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2143",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2143#issuecomment-14029",
    "user": "https://trac.sagemath.org/admin/accounts/users/edrex"
}
```

Ah... I like the f(x,y)=x<sup>2+y</sup>2 syntax/construction better, since it makes the mapping explicit for expressions which may not contain all variables. Filed as #2547
