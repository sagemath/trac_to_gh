# Issue 303: modular forms bug

archive/issues_000303.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: m = CuspForms(64,2)\nsage: m.integral_basis()\nTraceback (most recent call last):\n...\nArithmeticError: basis vectors must be linearly independent.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/303\n\n",
    "created_at": "2007-03-01T17:58:02Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.2",
    "title": "modular forms bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/303",
    "user": "was"
}
```
Assignee: was


```
sage: m = CuspForms(64,2)
sage: m.integral_basis()
Traceback (most recent call last):
...
ArithmeticError: basis vectors must be linearly independent.
```


Issue created by migration from https://trac.sagemath.org/ticket/303





---

archive/issue_comments_001449.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-19T01:08:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/303#issuecomment-1449",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_001450.json:
```json
{
    "body": "Fixed for sage-2.8.2 (same fix as for #304).",
    "created_at": "2007-08-19T01:08:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/303#issuecomment-1450",
    "user": "was"
}
```

Fixed for sage-2.8.2 (same fix as for #304).
