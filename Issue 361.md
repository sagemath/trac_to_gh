# Issue 361: implement tate's algorithm over number fields.

archive/issues_000361.json:
```json
{
    "body": "Assignee: @williamstein\n\nSee attached file.\n\n```\nFrom John Cremona:\n\nSorry I promised this a while ago.\n\nThis is essentially the file I gave to Magma in '02 or '03 which became\ntheir package/Geometry/CrvEll/minmodel.m after a bit of work by Nils\nBruin and Geoff Bailey.  From what I can tell their changes are only\ncosmetic (e.g. replacing my intrinsic with function somewhere, and also\nfiddling with the input & output parameters to make the order of terms\nconsistent with other Magma functions.\n\nApart from that I just replaced UniformizingParameter() with\nMyUniformizingParameter() as explained in the comment.\n\nYou can do what you like with this now!\n\nJohn\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/361\n\n",
    "created_at": "2007-05-07T16:18:33Z",
    "labels": [
        "component: algebraic geometry"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "implement tate's algorithm over number fields.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/361",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

See attached file.

```
From John Cremona:

Sorry I promised this a while ago.

This is essentially the file I gave to Magma in '02 or '03 which became
their package/Geometry/CrvEll/minmodel.m after a bit of work by Nils
Bruin and Geoff Bailey.  From what I can tell their changes are only
cosmetic (e.g. replacing my intrinsic with function somewhere, and also
fiddling with the input & output parameters to make the order of terms
consistent with other Magma functions.

Apart from that I just replaced UniformizingParameter() with
MyUniformizingParameter() as explained in the comment.

You can do what you like with this now!

John
```

Issue created by migration from https://trac.sagemath.org/ticket/361





---

archive/issue_comments_001748.json:
```json
{
    "body": "Implementation of tate's algorithm in MAGMA",
    "created_at": "2007-05-07T16:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/361#issuecomment-1748",
    "user": "https://github.com/williamstein"
}
```

Implementation of tate's algorithm in MAGMA



---

archive/issue_comments_001749.json:
```json
{
    "body": "Attachment [tate.m](tarball://root/attachments/some-uuid/ticket361/tate.m) by mabshoff created at 2007-09-10 02:21:03",
    "created_at": "2007-09-10T02:21:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/361#issuecomment-1749",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [tate.m](tarball://root/attachments/some-uuid/ticket361/tate.m) by mabshoff created at 2007-09-10 02:21:03



---

archive/issue_comments_001750.json:
```json
{
    "body": "Changing assignee from @williamstein to @roed314.",
    "created_at": "2007-10-09T13:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/361#issuecomment-1750",
    "user": "https://github.com/roed314"
}
```

Changing assignee from @williamstein to @roed314.



---

archive/issue_comments_001751.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-09T13:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/361#issuecomment-1751",
    "user": "https://github.com/roed314"
}
```

Changing status from new to assigned.



---

archive/issue_comments_001752.json:
```json
{
    "body": "This was implemented ages ago and so can be closed.",
    "created_at": "2008-04-07T19:39:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/361#issuecomment-1752",
    "user": "https://github.com/JohnCremona"
}
```

This was implemented ages ago and so can be closed.



---

archive/issue_events_000847.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-07T19:41:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/361",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/361#event-847"
}
```



---

archive/issue_comments_001753.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-07T19:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/361#issuecomment-1753",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_001754.json:
```json
{
    "body": "Fixed as per John Cremona's request.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-07T19:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/361#issuecomment-1754",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed as per John Cremona's request.

Cheers,

Michael



---

archive/issue_events_000848.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-07T19:41:50Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/361",
    "milestone": "sage-3.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/361#event-848"
}
```
