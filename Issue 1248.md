# Issue 1248: mwrank wrapper defect

archive/issues_001248.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe mwrank wrapper crashes for curves requiring a large precision:\n\n```\nsage: F=EllipticCurve([1, 0, 0, -276367728491702366785, 2435648906608461566891797433225])\nsage: F.gens()\n...\nMwrank crashed executing [1, 0, 0, -276367728491702366785, 2435648906608461566891797433225]\n```\n\nThe workaround is to enlarge the precision, but this does not seem to work:\n\n```\nsage: mwrank_set_precision(40)\nsage: F=EllipticCurve([1, 0, 0, -276367728491702366785, 2435648906608461566891797433225])\nsage: F.gens()\n...\nMwrank crashed executing [1, 0, 0, -276367728491702366785, 2435648906608461566891797433225]\n```\n\nIn comparison, the mwrank console works:\n\n```\npasta% sage -mwrank -p40\n...\nEnter curve: [1, 0, 0, -276367728491702366785, 2435648906608461566891797433225]\n...\nRank = 2\n...\nGenerator 1 is [-64279912864146869343830:9890032513326436827332346415:5023053676376]; height 19.3576595783878252695113978299426894052\nGenerator 2 is [15973785170:1448063200169915:1]; height 4.540177201347877276441819514533365581727\n```\n\nThis proves that the defect is in the mwrank wrapper, not in mwrank itself.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1248\n\n",
    "created_at": "2007-11-23T16:32:03Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "mwrank wrapper defect",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1248",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: @williamstein

The mwrank wrapper crashes for curves requiring a large precision:

```
sage: F=EllipticCurve([1, 0, 0, -276367728491702366785, 2435648906608461566891797433225])
sage: F.gens()
...
Mwrank crashed executing [1, 0, 0, -276367728491702366785, 2435648906608461566891797433225]
```

The workaround is to enlarge the precision, but this does not seem to work:

```
sage: mwrank_set_precision(40)
sage: F=EllipticCurve([1, 0, 0, -276367728491702366785, 2435648906608461566891797433225])
sage: F.gens()
...
Mwrank crashed executing [1, 0, 0, -276367728491702366785, 2435648906608461566891797433225]
```

In comparison, the mwrank console works:

```
pasta% sage -mwrank -p40
...
Enter curve: [1, 0, 0, -276367728491702366785, 2435648906608461566891797433225]
...
Rank = 2
...
Generator 1 is [-64279912864146869343830:9890032513326436827332346415:5023053676376]; height 19.3576595783878252695113978299426894052
Generator 2 is [15973785170:1448063200169915:1]; height 4.540177201347877276441819514533365581727
```

This proves that the defect is in the mwrank wrapper, not in mwrank itself.


Issue created by migration from https://trac.sagemath.org/ticket/1248





---

archive/issue_comments_007796.json:
```json
{
    "body": "John Cremona wrote:\n\n```\nThis was Paul Z's observation and seems to be a wrapper problem, so\n\"anyone\" could try to track that down.\n]]]\n\nCheers,\n\nMichael",
    "created_at": "2007-12-05T19:01:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1248#issuecomment-7796",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

John Cremona wrote:

```
This was Paul Z's observation and seems to be a wrapper problem, so
"anyone" could try to track that down.
]]]

Cheers,

Michael



---

archive/issue_comments_007797.json:
```json
{
    "body": "Since William is rewriting the mwrank wrapper he might take care of this. The crash does happen with Sage 2.10.2.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-15T23:00:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1248#issuecomment-7797",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Since William is rewriting the mwrank wrapper he might take care of this. The crash does happen with Sage 2.10.2.alpha0.

Cheers,

Michael



---

archive/issue_comments_007798.json:
```json
{
    "body": "Hmmm, since William told be that the mwrank wrapper rewrite is practically done it would be nice to get this into Sage and hopefully resolve this issue, too.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-22T21:23:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1248#issuecomment-7798",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hmmm, since William told be that the mwrank wrapper rewrite is practically done it would be nice to get this into Sage and hopefully resolve this issue, too.

Cheers,

Michael



---

archive/issue_comments_007799.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-23T19:14:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1248#issuecomment-7799",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Resolution: fixed



---

archive/issue_comments_007800.json:
```json
{
    "body": "This works for me in Sage 3.1.1 on 32-bit and 64-bit x86; maybe the \"mwrank wrapper rewrite\" referred to above did fix the problem?",
    "created_at": "2008-08-23T19:14:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1248#issuecomment-7800",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

This works for me in Sage 3.1.1 on 32-bit and 64-bit x86; maybe the "mwrank wrapper rewrite" referred to above did fix the problem?



---

archive/issue_events_001390.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/cwitty",
    "created_at": "2008-08-23T19:14:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1248",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1248#event-1390"
}
```
