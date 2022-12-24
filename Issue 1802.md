# Issue 1802: unify possible finite field representations

archive/issues_001802.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: usability\n\nIf Givaro implements the finite extension field then the parameter \"int\" or \"log\" changes the representation of elements. This doesn't work for larger fields and thus is ambiguous. So either the `repr=\"int\"` parameter should be dropped for Givaro or allowed for all other implementations.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1802\n\n",
    "created_at": "2008-01-17T19:15:18Z",
    "labels": [
        "user interface",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "unify possible finite field representations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1802",
    "user": "@malb"
}
```
Assignee: @williamstein

Keywords: usability

If Givaro implements the finite extension field then the parameter "int" or "log" changes the representation of elements. This doesn't work for larger fields and thus is ambiguous. So either the `repr="int"` parameter should be dropped for Givaro or allowed for all other implementations.

Issue created by migration from https://trac.sagemath.org/ticket/1802


