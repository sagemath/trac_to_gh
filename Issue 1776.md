# Issue 1776: symbolic function preparser bug

archive/issues_001776.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: preparse('f(x) = x')\n'_=var(\"x\");f=symbolic_expression(x).function(x)'\nsage: preparse('f(x) =+x')\n'f(x) =+x'\nsage: preparse('f(x) =-x')\n'f(x) =-x'\n```\n\n\nThis was found by Jason Grout, with input by Jaap Spies and John Cremona.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1776\n\n",
    "created_at": "2008-01-14T14:14:50Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "symbolic function preparser bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1776",
    "user": "was"
}
```
Assignee: was


```
sage: preparse('f(x) = x')
'_=var("x");f=symbolic_expression(x).function(x)'
sage: preparse('f(x) =+x')
'f(x) =+x'
sage: preparse('f(x) =-x')
'f(x) =-x'
```


This was found by Jason Grout, with input by Jaap Spies and John Cremona.

Issue created by migration from https://trac.sagemath.org/ticket/1776





---

archive/issue_comments_011244.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-14T14:20:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1776#issuecomment-11244",
    "user": "was"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011245.json:
```json
{
    "body": "slightly better fix (there is only one post-equals symbol, namely =).  This also fixes typos and mistakes in some of the docs.",
    "created_at": "2008-01-14T14:36:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1776#issuecomment-11245",
    "user": "was"
}
```

slightly better fix (there is only one post-equals symbol, namely =).  This also fixes typos and mistakes in some of the docs.



---

archive/issue_comments_011246.json:
```json
{
    "body": "Attachment\n\n\n```\nWorks for me!\n\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.10.alpha2, Release Date: 2008-01-11                 |\n| Type notebook() for the GUI, and license() for information.        |\n\nsage: f(x)=-x\n\nsage: f(2)\n -2\n\n\nJaap\n\n```\n",
    "created_at": "2008-01-14T15:27:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1776#issuecomment-11246",
    "user": "jsp"
}
```

Attachment


```
Works for me!

----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.alpha2, Release Date: 2008-01-11                 |
| Type notebook() for the GUI, and license() for information.        |

sage: f(x)=-x

sage: f(2)
 -2


Jaap

```




---

archive/issue_comments_011247.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-14T16:49:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1776#issuecomment-11247",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011248.json:
```json
{
    "body": "Merged in Sage 2.10.alpha3.",
    "created_at": "2008-01-14T16:49:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1776#issuecomment-11248",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.alpha3.
