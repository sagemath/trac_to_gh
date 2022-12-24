# Issue 361: implement tate's algorithm over number fields.

archive/issues_000361.json:
```json
{
    "body": "Assignee: was\n\nSee attached file.\n\n```\nFrom John Cremona:\n\nSorry I promised this a while ago.\n\nThis is essentially the file I gave to Magma in '02 or '03 which became\ntheir package/Geometry/CrvEll/minmodel.m after a bit of work by Nils\nBruin and Geoff Bailey.  From what I can tell their changes are only\ncosmetic (e.g. replacing my intrinsic with function somewhere, and also\nfiddling with the input & output parameters to make the order of terms\nconsistent with other Magma functions.\n\nApart from that I just replaced UniformizingParameter() with\nMyUniformizingParameter() as explained in the comment.\n\nYou can do what you like with this now!\n\nJohn\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/361\n\n",
    "created_at": "2007-05-07T16:18:33Z",
    "labels": [
        "algebraic geometry",
        "major",
        "enhancement"
    ],
    "title": "implement tate's algorithm over number fields.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/361",
    "user": "was"
}
```
Assignee: was

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

archive/issue_comments_001754.json:
```json
{
    "body": "Implementation of tate's algorithm in MAGMA",
    "created_at": "2007-05-07T16:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/361#issuecomment-1754",
    "user": "was"
}
```

Implementation of tate's algorithm in MAGMA



---

archive/issue_comments_001755.json:
```json
{
    "body": "Attachment [tate.m](tarball://root/attachments/some-uuid/ticket361/tate.m) by mabshoff created at 2007-09-10 02:21:03",
    "created_at": "2007-09-10T02:21:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/361#issuecomment-1755",
    "user": "mabshoff"
}
```

Attachment [tate.m](tarball://root/attachments/some-uuid/ticket361/tate.m) by mabshoff created at 2007-09-10 02:21:03



---

archive/issue_comments_001756.json:
```json
{
    "body": "Changing assignee from was to roed.",
    "created_at": "2007-10-09T13:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/361#issuecomment-1756",
    "user": "roed"
}
```

Changing assignee from was to roed.



---

archive/issue_comments_001757.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-09T13:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/361#issuecomment-1757",
    "user": "roed"
}
```

Changing status from new to assigned.



---

archive/issue_comments_001758.json:
```json
{
    "body": "This was implemented ages ago and so can be closed.",
    "created_at": "2008-04-07T19:39:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/361#issuecomment-1758",
    "user": "cremona"
}
```

This was implemented ages ago and so can be closed.



---

archive/issue_comments_001759.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-07T19:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/361#issuecomment-1759",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_001760.json:
```json
{
    "body": "Fixed as per John Cremona's request.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-07T19:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/361",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/361#issuecomment-1760",
    "user": "mabshoff"
}
```

Fixed as per John Cremona's request.

Cheers,

Michael
