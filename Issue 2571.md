# Issue 2571: problem with copy() on sage.rings.integer_mod.IntegerMod_gmp

archive/issues_002571.json:
```json
{
    "body": "Assignee: somebody\n\nJohn Cremona:\n\n```\nsage: a=[Mod(2,next_prime(2^n)) for n in range(28,35)]\nsage: [type(x) for x in a]\n\n[<type 'sage.rings.integer_mod.IntegerMod_int64'>,\n <type 'sage.rings.integer_mod.IntegerMod_int64'>,\n <type 'sage.rings.integer_mod.IntegerMod_int64'>,\n <type 'sage.rings.integer_mod.IntegerMod_gmp'>,\n <type 'sage.rings.integer_mod.IntegerMod_gmp'>,\n <type 'sage.rings.integer_mod.IntegerMod_gmp'>,\n <type 'sage.rings.integer_mod.IntegerMod_gmp'>]\n\nsage: [copy(x) for x in a]\n[2, 2, 2, None, None, None, None]\n\nsage: [deepcopy(x) for x in a]\n[2, 2, 2, 2, 2, 2, 2]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2571\n\n",
    "created_at": "2008-03-17T12:55:24Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "problem with copy() on sage.rings.integer_mod.IntegerMod_gmp",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2571",
    "user": "dfdeshom"
}
```
Assignee: somebody

John Cremona:

```
sage: a=[Mod(2,next_prime(2^n)) for n in range(28,35)]
sage: [type(x) for x in a]

[<type 'sage.rings.integer_mod.IntegerMod_int64'>,
 <type 'sage.rings.integer_mod.IntegerMod_int64'>,
 <type 'sage.rings.integer_mod.IntegerMod_int64'>,
 <type 'sage.rings.integer_mod.IntegerMod_gmp'>,
 <type 'sage.rings.integer_mod.IntegerMod_gmp'>,
 <type 'sage.rings.integer_mod.IntegerMod_gmp'>,
 <type 'sage.rings.integer_mod.IntegerMod_gmp'>]

sage: [copy(x) for x in a]
[2, 2, 2, None, None, None, None]

sage: [deepcopy(x) for x in a]
[2, 2, 2, 2, 2, 2, 2]
```


Issue created by migration from https://trac.sagemath.org/ticket/2571





---

archive/issue_comments_017566.json:
```json
{
    "body": "Attachment [8950.patch](tarball://root/attachments/some-uuid/ticket2571/8950.patch) by cremona created at 2008-03-17 14:24:28",
    "created_at": "2008-03-17T14:24:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2571#issuecomment-17566",
    "user": "cremona"
}
```

Attachment [8950.patch](tarball://root/attachments/some-uuid/ticket2571/8950.patch) by cremona created at 2008-03-17 14:24:28



---

archive/issue_comments_017567.json:
```json
{
    "body": "To fix this I added a return statement to the `__copy__()` function of IntegerMod_gmp.  Patch attached (based on 2.10.4.rc0)",
    "created_at": "2008-03-17T14:27:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2571#issuecomment-17567",
    "user": "cremona"
}
```

To fix this I added a return statement to the `__copy__()` function of IntegerMod_gmp.  Patch attached (based on 2.10.4.rc0)



---

archive/issue_comments_017568.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-17T14:27:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2571#issuecomment-17568",
    "user": "cremona"
}
```

Changing status from new to assigned.



---

archive/issue_comments_017569.json:
```json
{
    "body": "Changing assignee from somebody to cremona.",
    "created_at": "2008-03-17T14:27:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2571#issuecomment-17569",
    "user": "cremona"
}
```

Changing assignee from somebody to cremona.



---

archive/issue_comments_017570.json:
```json
{
    "body": "While you're editing that function, would you mind adding a doctest or 2 to it? That would help with the overall 3.0 goal of >50% function doctest coverage",
    "created_at": "2008-03-17T14:34:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2571#issuecomment-17570",
    "user": "dfdeshom"
}
```

While you're editing that function, would you mind adding a doctest or 2 to it? That would help with the overall 3.0 goal of >50% function doctest coverage



---

archive/issue_comments_017571.json:
```json
{
    "body": "apply after 8950.patch",
    "created_at": "2008-03-17T16:56:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2571#issuecomment-17571",
    "user": "cremona"
}
```

apply after 8950.patch



---

archive/issue_comments_017572.json:
```json
{
    "body": "Attachment [8951.patch](tarball://root/attachments/some-uuid/ticket2571/8951.patch) by cremona created at 2008-03-17 16:56:39\n\nAs suggested, a few doctests have been added, in the second patch.",
    "created_at": "2008-03-17T16:56:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2571#issuecomment-17572",
    "user": "cremona"
}
```

Attachment [8951.patch](tarball://root/attachments/some-uuid/ticket2571/8951.patch) by cremona created at 2008-03-17 16:56:39

As suggested, a few doctests have been added, in the second patch.



---

archive/issue_comments_017573.json:
```json
{
    "body": "These patches fix the bug and add and improve documentation bits.  I've tested everything I could see that could go wrong (including the copy and sqrt/square_root change) and all looks good to me.\n\nThis is a positive review to both patches!",
    "created_at": "2008-03-18T15:39:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2571#issuecomment-17573",
    "user": "jbmohler"
}
```

These patches fix the bug and add and improve documentation bits.  I've tested everything I could see that could go wrong (including the copy and sqrt/square_root change) and all looks good to me.

This is a positive review to both patches!



---

archive/issue_comments_017574.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-19T00:36:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2571#issuecomment-17574",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017575.json:
```json
{
    "body": "Merged both patches in Sage 2.11.alpha0",
    "created_at": "2008-03-19T00:36:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2571",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2571#issuecomment-17575",
    "user": "mabshoff"
}
```

Merged both patches in Sage 2.11.alpha0
