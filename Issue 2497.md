# Issue 2497: crash in polynomial remainder

archive/issues_002497.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: R.<x> = PolynomialRing(Integers(4))\nsage: f = x^2 + 3\nsage: f % 2\nInvMod: inverse undefined\n/Users/david/sage/local/bin/sage-sage: line 222: 11351 Abort trap              sage-ipython \"$@\" -c \"$SAGE_STARTUP_COMMAND;\"\n```\n\n\nThis is an NTL error message, which is not being trapped or something.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2497\n\n",
    "created_at": "2008-03-12T16:15:01Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "crash in polynomial remainder",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2497",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
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

archive/issue_comments_016889.json:
```json
{
    "body": "This also happens in `__florrdiv__(), quo_rem()`",
    "created_at": "2008-03-14T03:39:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2497#issuecomment-16889",
    "user": "https://github.com/dfdeshom"
}
```

This also happens in `__florrdiv__(), quo_rem()`



---

archive/issue_comments_016890.json:
```json
{
    "body": "Attachment [2497.patch](tarball://root/attachments/some-uuid/ticket2497/2497.patch) by dmharvey created at 2008-04-05 19:24:52",
    "created_at": "2008-04-05T19:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2497#issuecomment-16890",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Attachment [2497.patch](tarball://root/attachments/some-uuid/ticket2497/2497.patch) by dmharvey created at 2008-04-05 19:24:52



---

archive/issue_comments_016891.json:
```json
{
    "body": "#2592 seems related and is not fixed by this patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-07T03:44:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2497#issuecomment-16891",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

#2592 seems related and is not fixed by this patch.

Cheers,

Michael



---

archive/issue_comments_016892.json:
```json
{
    "body": "The patch fixes the issue, adds a doctest for the crash and passes doctests. Positive review.\n\nCheers,\n\nMichaek",
    "created_at": "2008-04-07T03:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2497#issuecomment-16892",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch fixes the issue, adds a doctest for the crash and passes doctests. Positive review.

Cheers,

Michaek



---

archive/issue_comments_016893.json:
```json
{
    "body": "Merged in Sage 3.0.alpha2",
    "created_at": "2008-04-07T03:46:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2497#issuecomment-16893",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha2



---

archive/issue_events_002678.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-04-07T03:46:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2497",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2497#event-2678"
}
```



---

archive/issue_comments_016894.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-07T03:46:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2497",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2497#issuecomment-16894",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
