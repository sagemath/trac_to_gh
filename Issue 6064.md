# Issue 6064: allow rationals in kronecker_symbol and legendre_symbol

archive/issues_006064.json:
```json
{
    "body": "Assignee: @tornaria\n\nWith sage-4.0.alpha0:\n\n```\nsage: kronecker(2/3,7)\n...\nTypeError: no conversion of this rational to integer\n```\n\nSame for `kronecker_symbol` and `legendre_symbol`. However, it does make sense for these to be defined on rationals.\n\nThis is actually used by `is_padic_square` when used with rationals, and triggered by some of the new quadratic form doctests.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6064\n\n",
    "created_at": "2009-05-18T05:30:08Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "allow rationals in kronecker_symbol and legendre_symbol",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6064",
    "user": "https://github.com/tornaria"
}
```
Assignee: @tornaria

With sage-4.0.alpha0:

```
sage: kronecker(2/3,7)
...
TypeError: no conversion of this rational to integer
```

Same for `kronecker_symbol` and `legendre_symbol`. However, it does make sense for these to be defined on rationals.

This is actually used by `is_padic_square` when used with rationals, and triggered by some of the new quadratic form doctests.

Issue created by migration from https://trac.sagemath.org/ticket/6064





---

archive/issue_comments_048176.json:
```json
{
    "body": "Note: this is needed to fix doctests in quadratic forms (#5954, #6037, #6040).",
    "created_at": "2009-05-18T05:35:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6064#issuecomment-48176",
    "user": "https://github.com/tornaria"
}
```

Note: this is needed to fix doctests in quadratic forms (#5954, #6037, #6040).



---

archive/issue_comments_048177.json:
```json
{
    "body": "Attachment [trac_6064.patch](tarball://root/attachments/some-uuid/ticket6064/trac_6064.patch) by @tornaria created at 2009-05-18 05:41:13\n\nallow rationals in kronecker_symbol and legendre_symbol",
    "created_at": "2009-05-18T05:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6064#issuecomment-48177",
    "user": "https://github.com/tornaria"
}
```

Attachment [trac_6064.patch](tarball://root/attachments/some-uuid/ticket6064/trac_6064.patch) by @tornaria created at 2009-05-18 05:41:13

allow rationals in kronecker_symbol and legendre_symbol



---

archive/issue_comments_048178.json:
```json
{
    "body": "Joint review with #6062:  applied both patches, both are fine and tests pass.",
    "created_at": "2009-05-18T21:18:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6064#issuecomment-48178",
    "user": "https://github.com/JohnCremona"
}
```

Joint review with #6062:  applied both patches, both are fine and tests pass.



---

archive/issue_comments_048179.json:
```json
{
    "body": "Merged in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-19T00:42:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6064#issuecomment-48179",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 4.0.rc0.

Cheers,

Michael



---

archive/issue_events_006319.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-05-19T00:42:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6064",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6064#event-6319"
}
```



---

archive/issue_comments_048180.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-19T00:42:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6064#issuecomment-48180",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
