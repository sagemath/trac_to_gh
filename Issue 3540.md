# Issue 3540: [with patch, positive review] Augment messes up the ncols for flat matrices.

archive/issues_003540.json:
```json
{
    "body": "Assignee: @williamstein\n\nFor example:\n\n```\nsage: M = Matrix(GF(2), 0, 0, 0)\nsage: M\n[]\nsage: M.nrows()\n0\nsage: M.ncols()\n0\nsage: N = Matrix(GF(2), 0, 19, 0)\nsage: N\n[]\nsage: N.nrows()\n0\nsage: N.ncols()\n19\nsage: W = M.augment(N)\nsage: W\n[]\nsage: W.nrows()\n0\nsage: W.ncols()\n0\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3540\n\n",
    "closed_at": "2008-07-03T02:53:08Z",
    "created_at": "2008-07-01T19:27:28Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with patch, positive review] Augment messes up the ncols for flat matrices.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3540",
    "user": "https://github.com/rlmill"
}
```
Assignee: @williamstein

For example:

```
sage: M = Matrix(GF(2), 0, 0, 0)
sage: M
[]
sage: M.nrows()
0
sage: M.ncols()
0
sage: N = Matrix(GF(2), 0, 19, 0)
sage: N
[]
sage: N.nrows()
0
sage: N.ncols()
19
sage: W = M.augment(N)
sage: W
[]
sage: W.nrows()
0
sage: W.ncols()
0
```

Issue created by migration from https://trac.sagemath.org/ticket/3540





---

archive/issue_comments_024969.json:
```json
{
    "body": "Attachment [trac3540-augment-gf2.patch](tarball://root/attachments/some-uuid/ticket3540/trac3540-augment-gf2.patch) by @malb created at 2008-07-02 20:30:51\n\nfixes SIGSEGV in first patch",
    "created_at": "2008-07-02T20:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3540#issuecomment-24969",
    "user": "https://github.com/malb"
}
```

Attachment [trac3540-augment-gf2.patch](tarball://root/attachments/some-uuid/ticket3540/trac3540-augment-gf2.patch) by @malb created at 2008-07-02 20:30:51

fixes SIGSEGV in first patch



---

archive/issue_comments_024970.json:
```json
{
    "body": "Attachment [trac3540-augment-gf2-fix.patch](tarball://root/attachments/some-uuid/ticket3540/trac3540-augment-gf2-fix.patch) by @malb created at 2008-07-02 20:31:59\n\nThe original patch introduced a SIGSEGV which I've fixed in `trac-3540-augment-fix.patch`. Together with my fix I'll give it a positive review, so somebody needs to approve my fix.",
    "created_at": "2008-07-02T20:31:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3540#issuecomment-24970",
    "user": "https://github.com/malb"
}
```

Attachment [trac3540-augment-gf2-fix.patch](tarball://root/attachments/some-uuid/ticket3540/trac3540-augment-gf2-fix.patch) by @malb created at 2008-07-02 20:31:59

The original patch introduced a SIGSEGV which I've fixed in `trac-3540-augment-fix.patch`. Together with my fix I'll give it a positive review, so somebody needs to approve my fix.



---

archive/issue_comments_024971.json:
```json
{
    "body": "If I'm allowed to give malb's patch a positive review, I do.",
    "created_at": "2008-07-02T21:38:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3540#issuecomment-24971",
    "user": "https://github.com/rlmill"
}
```

If I'm allowed to give malb's patch a positive review, I do.



---

archive/issue_comments_024972.json:
```json
{
    "body": "Replying to [comment:2 rlm]:\n> If I'm allowed to give malb's patch a positive review, I do. \n\n\nYes, since you know the code and his patch corrects an issue with your patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-03T00:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3540#issuecomment-24972",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:2 rlm]:
> If I'm allowed to give malb's patch a positive review, I do. 


Yes, since you know the code and his patch corrects an issue with your patch.

Cheers,

Michael



---

archive/issue_comments_024973.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-03T02:53:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3540#issuecomment-24973",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_008091.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-03T02:53:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3540",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3540#event-8091"
}
```



---

archive/issue_comments_024974.json:
```json
{
    "body": "Merged both patches in Sage 3.0.4.alpha2",
    "created_at": "2008-07-03T02:53:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3540",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3540#issuecomment-24974",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.0.4.alpha2
