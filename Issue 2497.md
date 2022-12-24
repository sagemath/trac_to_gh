# Issue 2497: crash in polynomial remainder

archive/issues_002497.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: R.<x> = PolynomialRing(Integers(4))\nsage: f = x^2 + 3\nsage: f % 2\nInvMod: inverse undefined\n/Users/david/sage/local/bin/sage-sage: line 222: 11351 Abort trap              sage-ipython \"$@\" -c \"$SAGE_STARTUP_COMMAND;\"\n```\n\n\nThis is an NTL error message, which is not being trapped or something.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2497\n\n",
    "created_at": "2008-03-12T16:15:01Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "crash in polynomial remainder",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2497",
    "user": "dmharvey"
}
```
Assignee: somebody


```
sage: R.<x> = PolynomialRing(Integers(4))
sage: f = x^2 + 3
sage: f % 2
InvMod: inverse undefined
/Users/david/sage/local/bin/sage-sage: line 222: 11351 Abort trap              sage-ipython "$@" -c "$SAGE_STARTUP_COMMAND;"
```


This is an NTL error message, which is not being trapped or something.


Issue created by migration from https://trac.sagemath.org/ticket/2497





---

archive/issue_comments_016925.json:
```json
{
    "body": "This also happens in `__florrdiv__(), quo_rem()`",
    "created_at": "2008-03-14T03:39:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2497#issuecomment-16925",
    "user": "dfdeshom"
}
```

This also happens in `__florrdiv__(), quo_rem()`



---

archive/issue_comments_016926.json:
```json
{
    "body": "Attachment [2497.patch](tarball://root/attachments/some-uuid/ticket2497/2497.patch) by dmharvey created at 2008-04-05 19:24:52",
    "created_at": "2008-04-05T19:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2497#issuecomment-16926",
    "user": "dmharvey"
}
```

Attachment [2497.patch](tarball://root/attachments/some-uuid/ticket2497/2497.patch) by dmharvey created at 2008-04-05 19:24:52



---

archive/issue_comments_016927.json:
```json
{
    "body": "#2592 seems related and is not fixed by this patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-07T03:44:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2497#issuecomment-16927",
    "user": "mabshoff"
}
```

#2592 seems related and is not fixed by this patch.

Cheers,

Michael



---

archive/issue_comments_016928.json:
```json
{
    "body": "The patch fixes the issue, adds a doctest for the crash and passes doctests. Positive review.\n\nCheers,\n\nMichaek",
    "created_at": "2008-04-07T03:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2497#issuecomment-16928",
    "user": "mabshoff"
}
```

The patch fixes the issue, adds a doctest for the crash and passes doctests. Positive review.

Cheers,

Michaek



---

archive/issue_comments_016929.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2",
    "created_at": "2008-04-07T03:46:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2497#issuecomment-16929",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha2



---

archive/issue_comments_016930.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-07T03:46:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2497#issuecomment-16930",
    "user": "mabshoff"
}
```

Resolution: fixed
