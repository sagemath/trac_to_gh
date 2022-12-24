# Issue 5677: Underscore for repeating output clobbered by symbolic variables

archive/issues_005677.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: underscore repeat output\n\nWhen creating a function with a statement like\n\n`f(x,y) = x<sup>2+y</sup>2`\n\nthe preparser creates a command to declare the variables and assigns it to underscore.  This renders the underscore unusable for repeating the previous output.\n\nA workaround is to use  \n\n`del _` \n\nto restore the functionality.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5677\n\n",
    "created_at": "2009-04-03T21:39:51Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Underscore for repeating output clobbered by symbolic variables",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5677",
    "user": "@rbeezer"
}
```
Assignee: @williamstein

Keywords: underscore repeat output

When creating a function with a statement like

`f(x,y) = x<sup>2+y</sup>2`

the preparser creates a command to declare the variables and assigns it to underscore.  This renders the underscore unusable for repeating the previous output.

A workaround is to use  

`del _` 

to restore the functionality.

Issue created by migration from https://trac.sagemath.org/ticket/5677





---

archive/issue_comments_044411.json:
```json
{
    "body": "Is this still valid?  It looks more like `__tmp__` is used, not `_`, these days:\n\n\n\n```\nsage: preparse(\"f(x,y) = x^2+y^2\")\n'__tmp__=var(\"x,y\"); f = symbolic_expression(x**Integer(2)+y**Integer(2)).function(x,y)'\nsage: 5\n5\nsage: _\n5\nsage: f(x,y) = x^2+y^2\nsage: _\n5\nsage: 7\n7\nsage: _\n7\n```\n",
    "created_at": "2012-05-25T22:55:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5677#issuecomment-44411",
    "user": "dsm"
}
```

Is this still valid?  It looks more like `__tmp__` is used, not `_`, these days:



```
sage: preparse("f(x,y) = x^2+y^2")
'__tmp__=var("x,y"); f = symbolic_expression(x**Integer(2)+y**Integer(2)).function(x,y)'
sage: 5
5
sage: _
5
sage: f(x,y) = x^2+y^2
sage: _
5
sage: 7
7
sage: _
7
```




---

archive/issue_comments_044412.json:
```json
{
    "body": "Yep, I think this is invalid now.",
    "created_at": "2013-07-23T12:56:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5677#issuecomment-44412",
    "user": "@mwhansen"
}
```

Yep, I think this is invalid now.



---

archive/issue_comments_044413.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-07-23T12:56:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5677#issuecomment-44413",
    "user": "@mwhansen"
}
```

Resolution: invalid
