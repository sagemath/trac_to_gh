# Issue 827: nfrootsof1 from Pari

archive/issues_000827.json:
```json
{
    "body": "Assignee: @williamstein\n\nImport nfrootsof1 from Pari so as to count the number of roots of unity in a number field.\n\nIssue created by migration from https://trac.sagemath.org/ticket/827\n\n",
    "created_at": "2007-10-05T00:00:23Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "nfrootsof1 from Pari",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/827",
    "user": "https://github.com/jvoight"
}
```
Assignee: @williamstein

Import nfrootsof1 from Pari so as to count the number of roots of unity in a number field.

Issue created by migration from https://trac.sagemath.org/ticket/827





---

archive/issue_comments_005108.json:
```json
{
    "body": "Attachment [ncalexan-827.patch](tarball://root/attachments/some-uuid/ticket827/ncalexan-827.patch) by @ncalexan created at 2008-01-19 20:56:32\n\nIt appears that nfrootsof1 is available, i.e. via K.pari_nf().nfrootsof1.  This just uses it, and fixes (what I think is) a small bug in CyclotomicField(7).zeta(14).",
    "created_at": "2008-01-19T20:56:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/827#issuecomment-5108",
    "user": "https://github.com/ncalexan"
}
```

Attachment [ncalexan-827.patch](tarball://root/attachments/some-uuid/ticket827/ncalexan-827.patch) by @ncalexan created at 2008-01-19 20:56:32

It appears that nfrootsof1 is available, i.e. via K.pari_nf().nfrootsof1.  This just uses it, and fixes (what I think is) a small bug in CyclotomicField(7).zeta(14).



---

archive/issue_comments_005109.json:
```json
{
    "body": "Attachment [ncalexan-827-updated.patch](tarball://root/attachments/some-uuid/ticket827/ncalexan-827-updated.patch) by @ncalexan created at 2008-01-19 23:56:17",
    "created_at": "2008-01-19T23:56:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/827#issuecomment-5109",
    "user": "https://github.com/ncalexan"
}
```

Attachment [ncalexan-827-updated.patch](tarball://root/attachments/some-uuid/ticket827/ncalexan-827-updated.patch) by @ncalexan created at 2008-01-19 23:56:17



---

archive/issue_comments_005110.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-20T00:42:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/827#issuecomment-5110",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_005111.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha0",
    "created_at": "2008-01-20T00:42:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/827",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/827#issuecomment-5111",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha0



---

archive/issue_events_000938.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-01-20T00:42:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/827",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/827#event-938"
}
```
