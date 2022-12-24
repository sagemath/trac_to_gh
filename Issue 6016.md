# Issue 6016: factoring rational functions

archive/issues_006016.json:
```json
{
    "body": "Assignee: tbd\n\nIt would be nice to be able to factor rational functions. The implementation is trivial, and the enclosed patch tries to do that.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6016\n\n",
    "created_at": "2009-05-11T02:15:12Z",
    "labels": [
        "algebra",
        "trivial",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "factoring rational functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6016",
    "user": "syazdani"
}
```
Assignee: tbd

It would be nice to be able to factor rational functions. The implementation is trivial, and the enclosed patch tries to do that.



Issue created by migration from https://trac.sagemath.org/ticket/6016





---

archive/issue_comments_047865.json:
```json
{
    "body": "Soroosh,\n\nplease post a proper patch.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T02:19:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6016#issuecomment-47865",
    "user": "mabshoff"
}
```

Soroosh,

please post a proper patch.

Cheers,

Michael



---

archive/issue_comments_047866.json:
```json
{
    "body": "Attachment [12063.patch](tarball://root/attachments/some-uuid/ticket6016/12063.patch) by syazdani created at 2009-05-11 04:30:17\n\nIs this the right format?",
    "created_at": "2009-05-11T04:30:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6016#issuecomment-47866",
    "user": "syazdani"
}
```

Attachment [12063.patch](tarball://root/attachments/some-uuid/ticket6016/12063.patch) by syazdani created at 2009-05-11 04:30:17

Is this the right format?



---

archive/issue_comments_047867.json:
```json
{
    "body": "Yep, looks like a nice patch to me :)\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T04:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6016#issuecomment-47867",
    "user": "mabshoff"
}
```

Yep, looks like a nice patch to me :)

Cheers,

Michael



---

archive/issue_comments_047868.json:
```json
{
    "body": "based on sage-3.4.2",
    "created_at": "2009-05-11T05:45:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6016#issuecomment-47868",
    "user": "mvngu"
}
```

based on sage-3.4.2



---

archive/issue_comments_047869.json:
```json
{
    "body": "Attachment [trac_6016-reviewer.patch](tarball://root/attachments/some-uuid/ticket6016/trac_6016-reviewer.patch) by mvngu created at 2009-05-11 05:49:35\n\nREFEREE REPORT\n\n\n\nThe patch `12063.patch` looks good. The new method `factor()` works over `ZZ`, `QQ`, `RR`, `CC`, and `GF`. There's only a trivial Sphinx formatting issue, which is fixed in the reviewer patch `trac_6016-reviewer.patch`.",
    "created_at": "2009-05-11T05:49:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6016#issuecomment-47869",
    "user": "mvngu"
}
```

Attachment [trac_6016-reviewer.patch](tarball://root/attachments/some-uuid/ticket6016/trac_6016-reviewer.patch) by mvngu created at 2009-05-11 05:49:35

REFEREE REPORT



The patch `12063.patch` looks good. The new method `factor()` works over `ZZ`, `QQ`, `RR`, `CC`, and `GF`. There's only a trivial Sphinx formatting issue, which is fixed in the reviewer patch `trac_6016-reviewer.patch`.



---

archive/issue_comments_047870.json:
```json
{
    "body": "I am not sure this should go in as is since the return result is a little strange. Is this consistent with other interfaces in Sage? What does Magma do?\n\nCheers,\n\nMichael",
    "created_at": "2009-05-14T05:44:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6016#issuecomment-47870",
    "user": "mabshoff"
}
```

I am not sure this should go in as is since the return result is a little strange. Is this consistent with other interfaces in Sage? What does Magma do?

Cheers,

Michael



---

archive/issue_comments_047871.json:
```json
{
    "body": "Replying to [comment:6 mabshoff]:\n> I am not sure this should go in as is since the return result is a little strange. Is this consistent with other interfaces in Sage? What does Magma do?\n> \n> Cheers,\n> \n> Michael\n\nThis is entirely consistent with (for example) factorization of rational numbers in Sage:\n\n```\nsage: QQ(123/456).factor()\n2^-3 * 19^-1 * 41\n```\n\nMagma does not allow factorization in QQ or in function fields, which is very annoying (e.g. you cannot factor the discriminant of an elliptic curve (with integral model) over QQ without coercing it into ZZ first).  But Magma does allow for some non-integral factorizations, e.g. of fractional ideals.\n\nSo Michael's worry is a reasonable one but this should definitely be included.  I have therefore removed the \"needs discussion\" tag!",
    "created_at": "2009-05-30T17:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6016#issuecomment-47871",
    "user": "cremona"
}
```

Replying to [comment:6 mabshoff]:
> I am not sure this should go in as is since the return result is a little strange. Is this consistent with other interfaces in Sage? What does Magma do?
> 
> Cheers,
> 
> Michael

This is entirely consistent with (for example) factorization of rational numbers in Sage:

```
sage: QQ(123/456).factor()
2^-3 * 19^-1 * 41
```

Magma does not allow factorization in QQ or in function fields, which is very annoying (e.g. you cannot factor the discriminant of an elliptic curve (with integral model) over QQ without coercing it into ZZ first).  But Magma does allow for some non-integral factorizations, e.g. of fractional ideals.

So Michael's worry is a reasonable one but this should definitely be included.  I have therefore removed the "needs discussion" tag!



---

archive/issue_comments_047872.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-01T04:59:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6016#issuecomment-47872",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_047873.json:
```json
{
    "body": "Merged in 4.0.1.alpha0.",
    "created_at": "2009-06-01T04:59:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6016#issuecomment-47873",
    "user": "mhansen"
}
```

Merged in 4.0.1.alpha0.
