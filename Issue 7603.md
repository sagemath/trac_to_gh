# Issue 7603: add methods to query representation of symbolic expressions

archive/issues_007603.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  fmaltey@nerim.fr\n\nAttached patch adds `_is_symbol()`, `_is_constant()` and `_is_numeric()` methods to `sage.symbolic.expression.Expression` objects.\n\nThese methods are just a thin wrapper around the `is_a<*>()` methods from pynac. They should provide a straightforward interface to query the internal representation of a symbolic expression when `.operator()` returns None.\n\nSome relevant discussion on sage-devel:\n\nhttp://groups.google.com/group/sage-devel/msg/6323b473af195bc7\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7603\n\n",
    "created_at": "2009-12-04T13:07:45Z",
    "labels": [
        "symbolics",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "add methods to query representation of symbolic expressions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7603",
    "user": "burcin"
}
```
Assignee: burcin

CC:  fmaltey@nerim.fr

Attached patch adds `_is_symbol()`, `_is_constant()` and `_is_numeric()` methods to `sage.symbolic.expression.Expression` objects.

These methods are just a thin wrapper around the `is_a<*>()` methods from pynac. They should provide a straightforward interface to query the internal representation of a symbolic expression when `.operator()` returns None.

Some relevant discussion on sage-devel:

http://groups.google.com/group/sage-devel/msg/6323b473af195bc7


Issue created by migration from https://trac.sagemath.org/ticket/7603





---

archive/issue_comments_064870.json:
```json
{
    "body": "Attachment [trac_7603-is_symbol.patch](tarball://root/attachments/some-uuid/ticket7603/trac_7603-is_symbol.patch) by burcin created at 2009-12-04 13:18:09",
    "created_at": "2009-12-04T13:18:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7603#issuecomment-64870",
    "user": "burcin"
}
```

Attachment [trac_7603-is_symbol.patch](tarball://root/attachments/some-uuid/ticket7603/trac_7603-is_symbol.patch) by burcin created at 2009-12-04 13:18:09



---

archive/issue_comments_064871.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-04T13:18:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7603#issuecomment-64871",
    "user": "burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064872.json:
```json
{
    "body": "Looks good.",
    "created_at": "2009-12-06T08:31:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7603#issuecomment-64872",
    "user": "mhansen"
}
```

Looks good.



---

archive/issue_comments_064873.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-06T08:31:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7603#issuecomment-64873",
    "user": "mhansen"
}
```

Resolution: fixed
