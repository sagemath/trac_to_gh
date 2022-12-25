# Issue 6814: jordan_form transformation lack of precision sage 4.1.1

archive/issues_006814.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: jordan, precision, matrix, transformation\n\nThere is an example for a lack of precision exception in the doc of jordan_form\n\n```\nsage: b = matrix(ZZ,3,3,range(9))\nsage: jf, p = b.jordan_form(RealField(15), transformation=True)\n...\nValueError: cannot compute the transformation matrix due to lack of precision\n```\n\nBut if one increases the precision to the maximum still the same error occurs\n\n```\nsage: b = matrix(ZZ,3,3,range(9))\nsage: jf, p = b.jordan_form(RealField(16777216), transformation=True)\n...\nValueError: cannot compute the transformation matrix due to lack of precision\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6814\n\n",
    "created_at": "2009-08-23T12:45:16Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "jordan_form transformation lack of precision sage 4.1.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6814",
    "user": "https://trac.sagemath.org/admin/accounts/users/Henryk.Trappmann"
}
```
Assignee: tbd

Keywords: jordan, precision, matrix, transformation

There is an example for a lack of precision exception in the doc of jordan_form

```
sage: b = matrix(ZZ,3,3,range(9))
sage: jf, p = b.jordan_form(RealField(15), transformation=True)
...
ValueError: cannot compute the transformation matrix due to lack of precision
```

But if one increases the precision to the maximum still the same error occurs

```
sage: b = matrix(ZZ,3,3,range(9))
sage: jf, p = b.jordan_form(RealField(16777216), transformation=True)
...
ValueError: cannot compute the transformation matrix due to lack of precision
```


Issue created by migration from https://trac.sagemath.org/ticket/6814





---

archive/issue_comments_056093.json:
```json
{
    "body": "Changing component from algebra to linear algebra.",
    "created_at": "2009-11-15T13:07:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6814#issuecomment-56093",
    "user": "https://github.com/aghitza"
}
```

Changing component from algebra to linear algebra.



---

archive/issue_comments_056094.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-01-19T12:26:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6814#issuecomment-56094",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Resolution: invalid



---

archive/issue_events_007048.json:
```json
{
    "actor": "spancratz",
    "created_at": "2010-01-19T12:26:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6814",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6814#event-7048"
}
```



---

archive/issue_comments_056095.json:
```json
{
    "body": "The error messages come up because the code does not actually detect numerically instability.  Instead, it notices when it fails, and assumes the only possible reason for this could be numerical instability.  Instead, there's a bug in the actual code.\n\nThus, this ticket can be closed as being \"invalid\".",
    "created_at": "2010-01-19T12:26:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6814#issuecomment-56095",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

The error messages come up because the code does not actually detect numerically instability.  Instead, it notices when it fails, and assumes the only possible reason for this could be numerical instability.  Instead, there's a bug in the actual code.

Thus, this ticket can be closed as being "invalid".
