# Issue 2218: assuming an expression is not equal to zero doesn't work

archive/issues_002218.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  b.w.barker@smokejive.net\n\n\n```\nsage: v,c = var('v,c')\nsage: assume(c!=0)\nsage: integral((1+v^2/c^2)^3/(1-v^2/c^2)^(3/2),v)\n...\n<type 'exceptions.TypeError'>: Computation failed since Maxima requested additional constraints (use assume):\nIs  c  zero or nonzero?\n```\n\n\nThis is caused by the following:\n\n```\nsage: eq = c != 0\nsage: eq._maxima_init_(assume=True)\n'(c)#(0)'\n\n(%i1) assume(c#0);\n`assume': `#' means syntactic nonequality in Maxima. Maybe you want to use `not equal'.\n -- an error.  To debug this try debugmode(true);\n\n```\n\nand is fixed by the following:\n\n```\nsage: sage.calculus.calculus.maxima.assume('notequal(c,0)');\nsage: integral((1+v^2/c^2)^3/(1-v^2/c^2)^(3/2),v)\n-75*sqrt(c^2)*arcsin(sqrt(c^2)*v/c^2)/8 - v^5/(4*c^4*sqrt(1 - v^2/c^2)) - 17*v^3/(8*c^2*sqrt(1 - v^2/c^2)) + 83*v/(8*sqrt(1 - v^2/c^2))\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2218\n\n",
    "created_at": "2008-02-20T03:50:43Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "assuming an expression is not equal to zero doesn't work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2218",
    "user": "mhansen"
}
```
Assignee: mhansen

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

archive/issue_comments_014699.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-20T03:58:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2218#issuecomment-14699",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014700.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-20T05:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2218#issuecomment-14700",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_014701.json:
```json
{
    "body": "Very nice getting to the bottom of this.",
    "created_at": "2008-02-20T06:08:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2218#issuecomment-14701",
    "user": "was"
}
```

Very nice getting to the bottom of this.



---

archive/issue_comments_014702.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-20T09:41:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2218#issuecomment-14702",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014703.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha2",
    "created_at": "2008-02-20T09:41:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2218",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2218#issuecomment-14703",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha2
