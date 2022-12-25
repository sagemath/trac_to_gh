# Issue 2299: [with patch, positive review] add zero_matrix constructor.

archive/issues_002299.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @ncalexan\n\nKeywords: zero matrix identity one\n\nThis adds the `zero_matrix` convenience constructor, just like `identity_matrix`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2299\n\n",
    "closed_at": "2008-02-28T00:48:29Z",
    "created_at": "2008-02-25T08:10:33Z",
    "labels": [
        "component: linear algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "[with patch, positive review] add zero_matrix constructor.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2299",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @williamstein

CC:  @ncalexan

Keywords: zero matrix identity one

This adds the `zero_matrix` convenience constructor, just like `identity_matrix`.

Issue created by migration from https://trac.sagemath.org/ticket/2299





---

archive/issue_comments_015216.json:
```json
{
    "body": "Changing assignee from @malb to @williamstein.",
    "created_at": "2008-02-25T11:29:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2299#issuecomment-15216",
    "user": "https://github.com/malb"
}
```

Changing assignee from @malb to @williamstein.



---

archive/issue_comments_015217.json:
```json
{
    "body": "Changing component from commutative algebra to linear algebra.",
    "created_at": "2008-02-25T11:29:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2299#issuecomment-15217",
    "user": "https://github.com/malb"
}
```

Changing component from commutative algebra to linear algebra.



---

archive/issue_comments_015218.json:
```json
{
    "body": "Attachment [2299-ncalexan-zero-matrix-1.patch](tarball://root/attachments/some-uuid/ticket2299/2299-ncalexan-zero-matrix-1.patch) by @malb created at 2008-02-25 11:29:23\n\nYou replaced \"n x n\" by \"$n \\times n$\" which reads nicer if typesetted. However, it is harder to comprehend from the command line (`foo?`).\n\nI am not sure that we need `identity_matrix` and `zero_matrix` (i.e. the functional versions of `MS(0)` and `MS(1)`) but that is a matter of taste.",
    "created_at": "2008-02-25T11:29:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2299#issuecomment-15218",
    "user": "https://github.com/malb"
}
```

Attachment [2299-ncalexan-zero-matrix-1.patch](tarball://root/attachments/some-uuid/ticket2299/2299-ncalexan-zero-matrix-1.patch) by @malb created at 2008-02-25 11:29:23

You replaced "n x n" by "$n \times n$" which reads nicer if typesetted. However, it is harder to comprehend from the command line (`foo?`).

I am not sure that we need `identity_matrix` and `zero_matrix` (i.e. the functional versions of `MS(0)` and `MS(1)`) but that is a matter of taste.



---

archive/issue_comments_015219.json:
```json
{
    "body": "I really want `identity_matrix` and `zero_matrix` because I often don't want to name the matrix space in advance.  `MS(0)` requires me to create said space first.\n\nAs for latex in docstrings... I don't care either way.  I think it should be latex but I parse simple latex from tex without trouble.",
    "created_at": "2008-02-25T18:07:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2299#issuecomment-15219",
    "user": "https://github.com/ncalexan"
}
```

I really want `identity_matrix` and `zero_matrix` because I often don't want to name the matrix space in advance.  `MS(0)` requires me to create said space first.

As for latex in docstrings... I don't care either way.  I think it should be latex but I parse simple latex from tex without trouble.



---

archive/issue_comments_015220.json:
```json
{
    "body": "Just a quick remark.  You can make a zero matrix using the matrix function:\n\n```\nsage: matrix(ZZ, 2,3)\n[0 0 0]\n[0 0 0]\n```\n\nI don't think that's a good reason not to add zero_matrix and identity_matrix\nfunctions though, both of which I would like to have too.",
    "created_at": "2008-02-25T18:09:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2299#issuecomment-15220",
    "user": "https://github.com/williamstein"
}
```

Just a quick remark.  You can make a zero matrix using the matrix function:

```
sage: matrix(ZZ, 2,3)
[0 0 0]
[0 0 0]
```

I don't think that's a good reason not to add zero_matrix and identity_matrix
functions though, both of which I would like to have too.



---

archive/issue_comments_015221.json:
```json
{
    "body": "I think zero_ and identity_ declare programmer intent nicely.  Will someone say positive or negative and this either goes to the bit-bucket or gets applied?",
    "created_at": "2008-02-25T18:17:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2299#issuecomment-15221",
    "user": "https://github.com/ncalexan"
}
```

I think zero_ and identity_ declare programmer intent nicely.  Will someone say positive or negative and this either goes to the bit-bucket or gets applied?



---

archive/issue_comments_015222.json:
```json
{
    "body": "REFEREE REPORT:\n\nI definitely think these functions should go in, but with TWO caveats. \n\n1. I think the zero_matrix should have an option to be nonsquare though.  Please post another patch that adds that, so, e.g.,\n\n```\nsage: zero_matrix(ZZ, 2,3)\n[0 0 0]\n[0 0 0]\n```\n\nworks. \n\n2. There should be a sparse option for both zero_matrix and\nidentity_matrix.\n\n```\nsage: zero_matrix(ZZ, 2,3, sparse=True).parent()\nFull MatrixSpace of 2 by 3 sparse matrices over Integer Ring\n```\n\n -- William",
    "created_at": "2008-02-25T18:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2299#issuecomment-15222",
    "user": "https://github.com/williamstein"
}
```

REFEREE REPORT:

I definitely think these functions should go in, but with TWO caveats. 

1. I think the zero_matrix should have an option to be nonsquare though.  Please post another patch that adds that, so, e.g.,

```
sage: zero_matrix(ZZ, 2,3)
[0 0 0]
[0 0 0]
```

works. 

2. There should be a sparse option for both zero_matrix and
identity_matrix.

```
sage: zero_matrix(ZZ, 2,3, sparse=True).parent()
Full MatrixSpace of 2 by 3 sparse matrices over Integer Ring
```

 -- William



---

archive/issue_comments_015223.json:
```json
{
    "body": "Attachment [2299-ncalexan-zero-matrix-2.patch](tarball://root/attachments/some-uuid/ticket2299/2299-ncalexan-zero-matrix-2.patch) by @ncalexan created at 2008-02-25 19:13:16",
    "created_at": "2008-02-25T19:13:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2299#issuecomment-15223",
    "user": "https://github.com/ncalexan"
}
```

Attachment [2299-ncalexan-zero-matrix-2.patch](tarball://root/attachments/some-uuid/ticket2299/2299-ncalexan-zero-matrix-2.patch) by @ncalexan created at 2008-02-25 19:13:16



---

archive/issue_comments_015224.json:
```json
{
    "body": "`2299-ncalexan-zero-matrix-2.patch` should apply without the previous patch, and should address the referee's comments.\n\nI generated this patch using hg diff between two revisions, not hg export.  Let me know if it's not okay.",
    "created_at": "2008-02-25T19:14:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2299#issuecomment-15224",
    "user": "https://github.com/ncalexan"
}
```

`2299-ncalexan-zero-matrix-2.patch` should apply without the previous patch, and should address the referee's comments.

I generated this patch using hg diff between two revisions, not hg export.  Let me know if it's not okay.



---

archive/issue_comments_015225.json:
```json
{
    "body": "Works for me in 2.10.3.alpha0.  Note that only the last patch should be apply and that it is a \"raw\" patch.",
    "created_at": "2008-02-27T22:08:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2299#issuecomment-15225",
    "user": "https://github.com/mwhansen"
}
```

Works for me in 2.10.3.alpha0.  Note that only the last patch should be apply and that it is a "raw" patch.



---

archive/issue_comments_015226.json:
```json
{
    "body": "Attachment [2299.patch](tarball://root/attachments/some-uuid/ticket2299/2299.patch) by @mwhansen created at 2008-02-27 22:16:00",
    "created_at": "2008-02-27T22:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2299#issuecomment-15226",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2299.patch](tarball://root/attachments/some-uuid/ticket2299/2299.patch) by @mwhansen created at 2008-02-27 22:16:00



---

archive/issue_comments_015227.json:
```json
{
    "body": "I just realized this conflicts with #874.  #874 should be applied first, and then 2299.patch should be applied.",
    "created_at": "2008-02-27T22:16:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2299#issuecomment-15227",
    "user": "https://github.com/mwhansen"
}
```

I just realized this conflicts with #874.  #874 should be applied first, and then 2299.patch should be applied.



---

archive/issue_comments_015228.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-28T00:48:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2299#issuecomment-15228",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015229.json:
```json
{
    "body": "Merged 2299.patch in Sage 2.10.3.rc0",
    "created_at": "2008-02-28T00:48:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2299#issuecomment-15229",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 2299.patch in Sage 2.10.3.rc0



---

archive/issue_events_005421.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-28T00:48:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2299",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2299#event-5421"
}
```
