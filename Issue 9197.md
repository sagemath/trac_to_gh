# Issue 9197: If latex() causes an error or doesn't work, we should just default to repr

archive/issues_009197.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  danaernst\n\nReported by Dana Ernst - for instance, the cayley_table() of a group doesn't work in the notebook if you click 'Typeset'.  But that's not the only place that's a problem.  If there isn't a good latex() command, it should output repr() or something.  This isn't exactly graphics, but I'll put it in there for now.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9197\n\n",
    "created_at": "2010-06-09T16:17:13Z",
    "labels": [
        "graphics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "If latex() causes an error or doesn't work, we should just default to repr",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9197",
    "user": "@kcrisman"
}
```
Assignee: jason, was

CC:  danaernst

Reported by Dana Ernst - for instance, the cayley_table() of a group doesn't work in the notebook if you click 'Typeset'.  But that's not the only place that's a problem.  If there isn't a good latex() command, it should output repr() or something.  This isn't exactly graphics, but I'll put it in there for now.

Issue created by migration from https://trac.sagemath.org/ticket/9197


