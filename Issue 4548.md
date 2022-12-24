# Issue 4548: bug in latexing a certain symbolic expression

archive/issues_004548.json:
```json
{
    "body": "Assignee: cwitty\n\nReported by Anders in sage-devel:\n\n\n```\nThere's a problem with powers of negative numbers the latex method for\nsymbolic arithmetic.\nIn version 3.1.4 I get this:\n{{{\nsage: var('n')\nn\nsage: latex((-1)^n)\n{-1}^{n}\n\nIt should, of course, be {(-1)}^{n}.\n -- Anders\n}}}\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4548\n\n",
    "created_at": "2008-11-19T15:35:07Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "bug in latexing a certain symbolic expression",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4548",
    "user": "was"
}
```
Assignee: cwitty

Reported by Anders in sage-devel:


```
There's a problem with powers of negative numbers the latex method for
symbolic arithmetic.
In version 3.1.4 I get this:
{{{
sage: var('n')
n
sage: latex((-1)^n)
{-1}^{n}

It should, of course, be {(-1)}^{n}.
 -- Anders
}}}




Issue created by migration from https://trac.sagemath.org/ticket/4548





---

archive/issue_comments_034075.json:
```json
{
    "body": "#5004 dup'd this, but has a patch.",
    "created_at": "2009-01-18T00:03:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4548",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4548#issuecomment-34075",
    "user": "was"
}
```

#5004 dup'd this, but has a patch.



---

archive/issue_comments_034076.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-01-18T00:03:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4548",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4548#issuecomment-34076",
    "user": "was"
}
```

Resolution: duplicate
