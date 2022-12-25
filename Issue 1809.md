# Issue 1809: [with patch] refactoring to improve finite field reference manual

archive/issues_001809.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe patch removes `FiniteField_prime_modn` from `finite_field.py` because it was odd that this implementation was the only showing up in the reference manual. Also, `GF` is now defined in `rings.all` rather than in `rings.finite_field` to avoid that the documentation for it shows up twice. Finally, a more verbose description of the finite field module is given at the top of the `finite_field.py` file and some doctests were added to `FiniteField_prime_modn`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1809\n\n",
    "closed_at": "2008-01-17T22:14:08Z",
    "created_at": "2008-01-17T21:29:18Z",
    "labels": [
        "component: distribution"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch] refactoring to improve finite field reference manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1809",
    "user": "https://github.com/malb"
}
```
Assignee: mabshoff

The patch removes `FiniteField_prime_modn` from `finite_field.py` because it was odd that this implementation was the only showing up in the reference manual. Also, `GF` is now defined in `rings.all` rather than in `rings.finite_field` to avoid that the documentation for it shows up twice. Finally, a more verbose description of the finite field module is given at the top of the `finite_field.py` file and some doctests were added to `FiniteField_prime_modn`.

Issue created by migration from https://trac.sagemath.org/ticket/1809





---

archive/issue_comments_011410.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-01-17T22:14:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1809#issuecomment-11410",
    "user": "https://github.com/malb"
}
```

Resolution: duplicate



---

archive/issue_events_004414.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2008-01-17T22:14:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1809",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1809#event-4414"
}
```
