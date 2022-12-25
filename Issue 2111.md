# Issue 2111: [with patch, with positive review] Gröbner bases over any field

archive/issues_002111.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @zimmermann6\n\nThis now works (but is very very slow):\n\n```\nsage: R.<x,y> = PolynomialRing(GF(2147483659),order='lex')\nsage: ideal([x^3-2*y^2,3*x+y^4]).groebner_basis()\n[x + 1431655773*y^4, y^12 + 54*y^2]\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2111\n\n",
    "closed_at": "2008-02-15T04:54:47Z",
    "created_at": "2008-02-08T12:17:23Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "[with patch, with positive review] Gr\u00f6bner bases over any field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2111",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  @zimmermann6

This now works (but is very very slow):

```
sage: R.<x,y> = PolynomialRing(GF(2147483659),order='lex')
sage: ideal([x^3-2*y^2,3*x+y^4]).groebner_basis()
[x + 1431655773*y^4, y^12 + 54*y^2]
```

Issue created by migration from https://trac.sagemath.org/ticket/2111





---

archive/issue_comments_013732.json:
```json
{
    "body": "Attachment [native_gb.patch](tarball://root/attachments/some-uuid/ticket2111/native_gb.patch) by @malb created at 2008-02-08 12:17:34",
    "created_at": "2008-02-08T12:17:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2111#issuecomment-13732",
    "user": "https://github.com/malb"
}
```

Attachment [native_gb.patch](tarball://root/attachments/some-uuid/ticket2111/native_gb.patch) by @malb created at 2008-02-08 12:17:34



---

archive/issue_comments_013733.json:
```json
{
    "body": "Attachment [trac_2111_2.patch](tarball://root/attachments/some-uuid/ticket2111/trac_2111_2.patch) by @malb created at 2008-02-13 13:26:34\n\nmisc additional improvements, apply after first patch",
    "created_at": "2008-02-13T13:26:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2111#issuecomment-13733",
    "user": "https://github.com/malb"
}
```

Attachment [trac_2111_2.patch](tarball://root/attachments/some-uuid/ticket2111/trac_2111_2.patch) by @malb created at 2008-02-13 13:26:34

misc additional improvements, apply after first patch



---

archive/issue_comments_013734.json:
```json
{
    "body": "Both patches look good, there's a lot to like in the first patch.  Apply!\n\nI personally prefer long outputs of doctests to be all one line -- I find it makes it easier to find errors -- but that's no reason to reject a good patch :)",
    "created_at": "2008-02-15T03:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2111#issuecomment-13734",
    "user": "https://github.com/ncalexan"
}
```

Both patches look good, there's a lot to like in the first patch.  Apply!

I personally prefer long outputs of doctests to be all one line -- I find it makes it easier to find errors -- but that's no reason to reject a good patch :)



---

archive/issue_events_005060.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-15T04:54:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2111",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2111#event-5060"
}
```



---

archive/issue_comments_013735.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0",
    "created_at": "2008-02-15T04:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2111#issuecomment-13735",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha0



---

archive/issue_comments_013736.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-15T04:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2111",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2111#issuecomment-13736",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
