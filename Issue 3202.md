# Issue 3202: show() smashes multiplied numbers together so the product looks like a number

archive/issues_003202.json:
```json
{
    "body": "Assignee: boothby\n\nTo see this, evaluate the following in a notebook cell:\n\n\n```\nvar('r,z')\na=(r*z^2).integrate(z,0,r).integrate(r,0,sqrt(9/2))*2*pi\na.show()\nprint a\n```\n\n\nFirefox 3 Beta 5; Ubuntu 8.04\n\nIssue created by migration from https://trac.sagemath.org/ticket/3202\n\n",
    "created_at": "2008-05-14T06:04:13Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "show() smashes multiplied numbers together so the product looks like a number",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3202",
    "user": "https://github.com/jasongrout"
}
```
Assignee: boothby

To see this, evaluate the following in a notebook cell:


```
var('r,z')
a=(r*z^2).integrate(z,0,r).integrate(r,0,sqrt(9/2))*2*pi
a.show()
print a
```


Firefox 3 Beta 5; Ubuntu 8.04

Issue created by migration from https://trac.sagemath.org/ticket/3202





---

archive/issue_comments_022081.json:
```json
{
    "body": "This is a problem with that object's show method, not with the notebook.",
    "created_at": "2009-01-22T00:36:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3202#issuecomment-22081",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

This is a problem with that object's show method, not with the notebook.



---

archive/issue_comments_022082.json:
```json
{
    "body": "Changing assignee from boothby to @burcin.",
    "created_at": "2009-01-22T00:36:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3202#issuecomment-22082",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing assignee from boothby to @burcin.



---

archive/issue_comments_022083.json:
```json
{
    "body": "Changing component from notebook to calculus.",
    "created_at": "2009-01-22T00:36:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3202#issuecomment-22083",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing component from notebook to calculus.



---

archive/issue_comments_022084.json:
```json
{
    "body": "This should be fixed in the pynac symbolics after #5753 is in.",
    "created_at": "2009-04-11T16:13:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3202#issuecomment-22084",
    "user": "https://github.com/burcin"
}
```

This should be fixed in the pynac symbolics after #5753 is in.



---

archive/issue_comments_022085.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-25T10:28:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3202#issuecomment-22085",
    "user": "https://github.com/burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_022086.json:
```json
{
    "body": "This is fixed in 4.0.rc0. There is a doctest mentioning this bug on line 492 of sage/symbolic/expression.pyx.\n\nThis bug should be closed as fixed.",
    "created_at": "2009-05-25T10:28:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3202#issuecomment-22086",
    "user": "https://github.com/burcin"
}
```

This is fixed in 4.0.rc0. There is a doctest mentioning this bug on line 492 of sage/symbolic/expression.pyx.

This bug should be closed as fixed.



---

archive/issue_comments_022087.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-26T17:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3202#issuecomment-22087",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_003420.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-05-26T17:02:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3202",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3202#event-3420"
}
```
