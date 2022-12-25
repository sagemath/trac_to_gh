# Issue 7942: latex(I) should be the string "i" not "I"

archive/issues_007942.json:
```json
{
    "body": "Assignee: @burcin\n\n\n```\n\nThat is dumb and should be fixed!\n\nsage: latex(I)\nI\nsage: latex(i)\nI\n\nIt should output \"i\" not \"I\".\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7942\n\n",
    "created_at": "2010-01-16T03:27:15Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "latex(I) should be the string \"i\" not \"I\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7942",
    "user": "https://github.com/williamstein"
}
```
Assignee: @burcin


```

That is dumb and should be fixed!

sage: latex(I)
I
sage: latex(i)
I

It should output "i" not "I".
```


Issue created by migration from https://trac.sagemath.org/ticket/7942





---

archive/issue_events_019006.json:
```json
{
    "actor": "https://github.com/burcin",
    "created_at": "2010-01-16T09:12:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7942",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7942#event-19006"
}
```



---

archive/issue_comments_069162.json:
```json
{
    "body": "This is a duplicate of #6405. Number field elements don't support a separate latex name option, so we have 3 options:\n* Use `i` for both modes\n* Use `I` for both modes\n* implement a latex_name option for number field elements.",
    "created_at": "2010-01-16T09:12:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7942#issuecomment-69162",
    "user": "https://github.com/burcin"
}
```

This is a duplicate of #6405. Number field elements don't support a separate latex name option, so we have 3 options:
* Use `i` for both modes
* Use `I` for both modes
* implement a latex_name option for number field elements.



---

archive/issue_comments_069163.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-01-16T09:12:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7942#issuecomment-69163",
    "user": "https://github.com/burcin"
}
```

Resolution: duplicate



---

archive/issue_events_019007.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-16T09:31:39Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7942",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7942#event-19007"
}
```
