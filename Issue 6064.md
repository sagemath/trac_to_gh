# Issue 6064: allow rationals in kronecker_symbol and legendre_symbol

archive/issues_006064.json:
```json
{
    "body": "Assignee: tornaria\n\nWith sage-4.0.alpha0:\n\n```\nsage: kronecker(2/3,7)\n...\nTypeError: no conversion of this rational to integer\n```\n\nSame for `kronecker_symbol` and `legendre_symbol`. However, it does make sense for these to be defined on rationals.\n\nThis is actually used by `is_padic_square` when used with rationals, and triggered by some of the new quadratic form doctests.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6064\n\n",
    "created_at": "2009-05-18T05:30:08Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "title": "allow rationals in kronecker_symbol and legendre_symbol",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6064",
    "user": "tornaria"
}
```
Assignee: tornaria

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

archive/issue_comments_048267.json:
```json
{
    "body": "Note: this is needed to fix doctests in quadratic forms (#5954, #6037, #6040).",
    "created_at": "2009-05-18T05:35:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6064#issuecomment-48267",
    "user": "tornaria"
}
```

Note: this is needed to fix doctests in quadratic forms (#5954, #6037, #6040).



---

archive/issue_comments_048268.json:
```json
{
    "body": "Attachment [trac_6064.patch](tarball://root/attachments/some-uuid/ticket6064/trac_6064.patch) by tornaria created at 2009-05-18 05:41:13\n\nallow rationals in kronecker_symbol and legendre_symbol",
    "created_at": "2009-05-18T05:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6064#issuecomment-48268",
    "user": "tornaria"
}
```

Attachment [trac_6064.patch](tarball://root/attachments/some-uuid/ticket6064/trac_6064.patch) by tornaria created at 2009-05-18 05:41:13

allow rationals in kronecker_symbol and legendre_symbol



---

archive/issue_comments_048269.json:
```json
{
    "body": "Joint review with #6062:  applied both patches, both are fine and tests pass.",
    "created_at": "2009-05-18T21:18:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6064#issuecomment-48269",
    "user": "cremona"
}
```

Joint review with #6062:  applied both patches, both are fine and tests pass.



---

archive/issue_comments_048270.json:
```json
{
    "body": "Merged in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-19T00:42:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6064#issuecomment-48270",
    "user": "mabshoff"
}
```

Merged in Sage 4.0.rc0.

Cheers,

Michael



---

archive/issue_comments_048271.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-19T00:42:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6064#issuecomment-48271",
    "user": "mabshoff"
}
```

Resolution: fixed
