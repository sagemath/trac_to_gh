# Issue 2845: [with patch, needs review] PolyBoRi assertion errror

archive/issues_002845.json:
```json
{
    "body": "Assignee: @malb\n\nApparently, PolyBoRi doesn't like to call `lmDeg` on a zero polynomial. The attached patch catches this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2845\n\n",
    "created_at": "2008-04-07T16:14:50Z",
    "labels": [
        "commutative algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch, needs review] PolyBoRi assertion errror",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2845",
    "user": "@malb"
}
```
Assignee: @malb

Apparently, PolyBoRi doesn't like to call `lmDeg` on a zero polynomial. The attached patch catches this.

Issue created by migration from https://trac.sagemath.org/ticket/2845





---

archive/issue_comments_019524.json:
```json
{
    "body": "Attachment [polybori_assert.patch](tarball://root/attachments/some-uuid/ticket2845/polybori_assert.patch) by @malb created at 2008-04-07 16:15:02",
    "created_at": "2008-04-07T16:15:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2845#issuecomment-19524",
    "user": "@malb"
}
```

Attachment [polybori_assert.patch](tarball://root/attachments/some-uuid/ticket2845/polybori_assert.patch) by @malb created at 2008-04-07 16:15:02



---

archive/issue_comments_019525.json:
```json
{
    "body": "Patch looks good. Do we already have a doctest for this?\n\nCheers,\n\nMichael",
    "created_at": "2008-04-07T16:35:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2845#issuecomment-19525",
    "user": "mabshoff"
}
```

Patch looks good. Do we already have a doctest for this?

Cheers,

Michael



---

archive/issue_comments_019526.json:
```json
{
    "body": "Actually, I noticed because we have a doctest. I compiled PolyBoRi with debugging support and this triggered the assertion error when running the doctests.",
    "created_at": "2008-04-07T19:58:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2845#issuecomment-19526",
    "user": "@malb"
}
```

Actually, I noticed because we have a doctest. I compiled PolyBoRi with debugging support and this triggered the assertion error when running the doctests.



---

archive/issue_comments_019527.json:
```json
{
    "body": "Replying to [comment:2 malb]:\n> Actually, I noticed because we have a doctest. I compiled PolyBoRi with debugging support and this triggered the assertion error when running the doctests.\n\nHi malb,\n\nI figured this was actually the case after thinking about this a little later, so I am merging this. No objections, positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-07T20:05:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2845#issuecomment-19527",
    "user": "mabshoff"
}
```

Replying to [comment:2 malb]:
> Actually, I noticed because we have a doctest. I compiled PolyBoRi with debugging support and this triggered the assertion error when running the doctests.

Hi malb,

I figured this was actually the case after thinking about this a little later, so I am merging this. No objections, positive review.

Cheers,

Michael



---

archive/issue_comments_019528.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-07T20:06:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2845#issuecomment-19528",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019529.json:
```json
{
    "body": "Merged in Sage 3.0.alpha3",
    "created_at": "2008-04-07T20:06:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2845#issuecomment-19529",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha3
