# Issue 2218: assuming an expression is not equal to zero doesn't work

archive/issues_002218.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  b.w.barker@smokejive.net\n\n\n```\nsage: v,c = var('v,c')\nsage: assume(c!=0)\nsage: integral((1+v^2/c^2)^3/(1-v^2/c^2)^(3/2),v)\n...\n<type 'exceptions.TypeError'>: Computation failed since Maxima requested additional constraints (use assume):\nIs  c  zero or nonzero?\n```\n\n\nThis is caused by the following:\n\n```\nsage: eq = c != 0\nsage: eq._maxima_init_(assume=True)\n'(c)#(0)'\n\n(%i1) assume(c#0);\n`assume': `#' means syntactic nonequality in Maxima. Maybe you want to use `not equal'.\n -- an error.  To debug this try debugmode(true);\n\n```\n\nand is fixed by the following:\n\n```\nsage: sage.calculus.calculus.maxima.assume('notequal(c,0)');\nsage: integral((1+v^2/c^2)^3/(1-v^2/c^2)^(3/2),v)\n-75*sqrt(c^2)*arcsin(sqrt(c^2)*v/c^2)/8 - v^5/(4*c^4*sqrt(1 - v^2/c^2)) - 17*v^3/(8*c^2*sqrt(1 - v^2/c^2)) + 83*v/(8*sqrt(1 - v^2/c^2))\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2218\n\n",
    "created_at": "2008-02-20T03:50:43Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "assuming an expression is not equal to zero doesn't work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2218",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @mwhansen

CC:  b.w.barker@smokejive.net


```
sage: v,c = var('v,c')
sage: assume(c!=0)
sage: integral((1+v^2/c^2)^3/(1-v^2/c^2)^(3/2),v)
...
<type 'exceptions.TypeError'>: Computation failed since Maxima requested additional constraints (use assume):
Is  c  zero or nonzero?
```


This is caused by the following:

```
sage: eq = c != 0
sage: eq._maxima_init_(assume=True)
'(c)#(0)'

(%i1) assume(c#0);
`assume': `#' means syntactic nonequality in Maxima. Maybe you want to use `not equal'.
 -- an error.  To debug this try debugmode(true);

```

and is fixed by the following:

```
sage: sage.calculus.calculus.maxima.assume('notequal(c,0)');
sage: integral((1+v^2/c^2)^3/(1-v^2/c^2)^(3/2),v)
-75*sqrt(c^2)*arcsin(sqrt(c^2)*v/c^2)/8 - v^5/(4*c^4*sqrt(1 - v^2/c^2)) - 17*v^3/(8*c^2*sqrt(1 - v^2/c^2)) + 83*v/(8*sqrt(1 - v^2/c^2))

```


Issue created by migration from https://trac.sagemath.org/ticket/2218





---

archive/issue_comments_014668.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-20T03:58:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2218#issuecomment-14668",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014669.json:
```json
{
    "body": "Attachment [2218.patch](tarball://root/attachments/some-uuid/ticket2218/2218.patch) by @mwhansen created at 2008-02-20 05:58:39",
    "created_at": "2008-02-20T05:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2218#issuecomment-14669",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2218.patch](tarball://root/attachments/some-uuid/ticket2218/2218.patch) by @mwhansen created at 2008-02-20 05:58:39



---

archive/issue_comments_014670.json:
```json
{
    "body": "Very nice getting to the bottom of this.",
    "created_at": "2008-02-20T06:08:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2218#issuecomment-14670",
    "user": "https://github.com/williamstein"
}
```

Very nice getting to the bottom of this.



---

archive/issue_comments_014671.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-20T09:41:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2218#issuecomment-14671",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014672.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha2",
    "created_at": "2008-02-20T09:41:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2218#issuecomment-14672",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha2



---

archive/issue_events_002388.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-20T09:41:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2218",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2218#event-2388"
}
```
