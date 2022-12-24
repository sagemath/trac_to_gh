# Issue 4250: In QQ[t], 2**t should raise an error, but it crashes

archive/issues_004250.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @malb\n\nKeywords: crash, polynomial ring, rationals\n\nOf course, doing\n\n```\nsage: R.<t>=QQ[]\nsage: 2**t\n```\n\nshould result in a traceback. In fact it does so for `R.<t>=ZZ[]`. But over `QQ`, it crashes with a segmentation fault.\n\nRunning `sage -gdb` yields a very long output, too long to reproduce it here, and sorry that I don't know how to save the output of `bt`.\n\nI use Sage version 3.1.2, and it occurs on two different Linux machines.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4250\n\n",
    "created_at": "2008-10-07T17:34:12Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "In QQ[t], 2**t should raise an error, but it crashes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4250",
    "user": "@simon-king-jena"
}
```
Assignee: @malb

CC:  @malb

Keywords: crash, polynomial ring, rationals

Of course, doing

```
sage: R.<t>=QQ[]
sage: 2**t
```

should result in a traceback. In fact it does so for `R.<t>=ZZ[]`. But over `QQ`, it crashes with a segmentation fault.

Running `sage -gdb` yields a very long output, too long to reproduce it here, and sorry that I don't know how to save the output of `bt`.

I use Sage version 3.1.2, and it occurs on two different Linux machines.

Issue created by migration from https://trac.sagemath.org/ticket/4250





---

archive/issue_comments_030919.json:
```json
{
    "body": "Any progress here? Is anybody working on this?\n\nCheers,\n\nMichael",
    "created_at": "2008-10-26T15:47:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4250#issuecomment-30919",
    "user": "mabshoff"
}
```

Any progress here? Is anybody working on this?

Cheers,

Michael



---

archive/issue_comments_030920.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-31T10:42:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4250#issuecomment-30920",
    "user": "@burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030921.json:
```json
{
    "body": "The segfault is caused by an infinite loop, where 2 is cast to a polynomial and its `__pow__` method is called, and the polynomial ring calls the `__pow__` method of the base ring on constant polynomials.\n\nattachment:trac_4250_QQx_pow_segfault.3.patch (thanks trac for screwing up the name again) fixes the issue.",
    "created_at": "2008-10-31T10:42:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4250#issuecomment-30921",
    "user": "@burcin"
}
```

The segfault is caused by an infinite loop, where 2 is cast to a polynomial and its `__pow__` method is called, and the polynomial ring calls the `__pow__` method of the base ring on constant polynomials.

attachment:trac_4250_QQx_pow_segfault.3.patch (thanks trac for screwing up the name again) fixes the issue.



---

archive/issue_comments_030922.json:
```json
{
    "body": "Changing assignee from @malb to @burcin.",
    "created_at": "2008-10-31T10:42:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4250#issuecomment-30922",
    "user": "@burcin"
}
```

Changing assignee from @malb to @burcin.



---

archive/issue_comments_030923.json:
```json
{
    "body": "Attachment [trac_4250_QQx_pow_segfault.3.patch](tarball://root/attachments/some-uuid/ticket4250/trac_4250_QQx_pow_segfault.3.patch) by @burcin created at 2008-10-31 10:42:56",
    "created_at": "2008-10-31T10:42:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4250#issuecomment-30923",
    "user": "@burcin"
}
```

Attachment [trac_4250_QQx_pow_segfault.3.patch](tarball://root/attachments/some-uuid/ticket4250/trac_4250_QQx_pow_segfault.3.patch) by @burcin created at 2008-10-31 10:42:56



---

archive/issue_comments_030924.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T14:20:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4250#issuecomment-30924",
    "user": "mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_030925.json:
```json
{
    "body": "Merged in Sage 3.2.alpha2",
    "created_at": "2008-10-31T14:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4250#issuecomment-30925",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha2



---

archive/issue_comments_030926.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-31T14:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4250",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4250#issuecomment-30926",
    "user": "mabshoff"
}
```

Resolution: fixed
