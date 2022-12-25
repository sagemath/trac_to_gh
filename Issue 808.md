# Issue 808: construction of function fields

archive/issues_000808.json:
```json
{
    "body": "Assignee: somebody\n\nThe following does not work and it seems to fail in an odd way wrt. the preparser\n\n```\nP1.<t> = QQ[].fraction_field()\n```\n\nThere doesn't seem to be a convenient way of constructing a rational function field\nwith a named variable.\n\nIssue created by migration from https://trac.sagemath.org/ticket/808\n\n",
    "created_at": "2007-10-03T15:40:30Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "construction of function fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/808",
    "user": "https://github.com/nbruin"
}
```
Assignee: somebody

The following does not work and it seems to fail in an odd way wrt. the preparser

```
P1.<t> = QQ[].fraction_field()
```

There doesn't seem to be a convenient way of constructing a rational function field
with a named variable.

Issue created by migration from https://trac.sagemath.org/ticket/808





---

archive/issue_comments_004883.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2007-10-03T15:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/808#issuecomment-4883",
    "user": "https://github.com/nbruin"
}
```

Resolution: duplicate
