# Issue 7790: Setting a default max/min bound when calling MixedIntegerLinearProgram.new_variable

archive/issues_007790.json:
```json
{
    "body": "Assignee: jkantor\n\nCC:  yzh\n\nBeing able to write something like :\n\n\n```\np = MixedIntegerLinearProgram()\nv = p.new_variable(min=3, max =8)\n```\n\n\nWould be really nice !\n\nIssue created by migration from https://trac.sagemath.org/ticket/7790\n\n",
    "created_at": "2009-12-29T18:17:30Z",
    "labels": [
        "numerical",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.8",
    "title": "Setting a default max/min bound when calling MixedIntegerLinearProgram.new_variable",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7790",
    "user": "ncohen"
}
```
Assignee: jkantor

CC:  yzh

Being able to write something like :


```
p = MixedIntegerLinearProgram()
v = p.new_variable(min=3, max =8)
```


Would be really nice !

Issue created by migration from https://trac.sagemath.org/ticket/7790





---

archive/issue_comments_067245.json:
```json
{
    "body": "Changing component from numerical to linear programming.",
    "created_at": "2010-09-06T11:12:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7790#issuecomment-67245",
    "user": "ncohen"
}
```

Changing component from numerical to linear programming.
