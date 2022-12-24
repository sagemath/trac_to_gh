# Issue 3890: exact division syntax in finite fields of prime order

archive/issues_003890.json:
```json
{
    "body": "Assignee: somebody\n\nIt appears that the // operator is supported for most fields, but not for GF(prime).\n\nThe example involving GF(7,'a') should not produce a TypeError.\n\n\n```\nsage: GF(49,'a')(121)//GF(49,'a')(124)\n6\nsage: GF(7,'a')(121)//GF(7,'a')(124)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/joel/sage-patches/<ipython console> in <module>()\n\nTypeError: unsupported operand type(s) for //: 'sage.rings.integer_mod.IntegerMod_int' and 'sage.rings.integer_mod.IntegerMod_int'\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3890\n\n",
    "created_at": "2008-08-18T13:56:34Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "exact division syntax in finite fields of prime order",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3890",
    "user": "jbmohler"
}
```
Assignee: somebody

It appears that the // operator is supported for most fields, but not for GF(prime).

The example involving GF(7,'a') should not produce a TypeError.


```
sage: GF(49,'a')(121)//GF(49,'a')(124)
6
sage: GF(7,'a')(121)//GF(7,'a')(124)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/joel/sage-patches/<ipython console> in <module>()

TypeError: unsupported operand type(s) for //: 'sage.rings.integer_mod.IntegerMod_int' and 'sage.rings.integer_mod.IntegerMod_int'
```



Issue created by migration from https://trac.sagemath.org/ticket/3890





---

archive/issue_comments_027801.json:
```json
{
    "body": "Attachment [3890](tarball://root/attachments/some-uuid/ticket3890/3890) by roed created at 2009-01-23 02:50:04",
    "created_at": "2009-01-23T02:50:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3890#issuecomment-27801",
    "user": "roed"
}
```

Attachment [3890](tarball://root/attachments/some-uuid/ticket3890/3890) by roed created at 2009-01-23 02:50:04



---

archive/issue_comments_027802.json:
```json
{
    "body": "Not much to say here. Positive review.",
    "created_at": "2009-01-23T21:49:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3890#issuecomment-27802",
    "user": "kedlaya"
}
```

Not much to say here. Positive review.



---

archive/issue_comments_027803.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-25T20:58:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3890#issuecomment-27803",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael



---

archive/issue_comments_027804.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-25T20:58:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3890#issuecomment-27804",
    "user": "mabshoff"
}
```

Resolution: fixed
