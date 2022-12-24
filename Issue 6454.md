# Issue 6454: improve sbox linear and differences matrices computation

archive/issues_006454.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  malb\n\nIn particular, use walsh transform for linear_approximation_matrix.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6454\n\n",
    "created_at": "2009-07-01T09:29:14Z",
    "labels": [
        "cryptography",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "improve sbox linear and differences matrices computation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6454",
    "user": "ylchapuy"
}
```
Assignee: somebody

CC:  malb

In particular, use walsh transform for linear_approximation_matrix.

Issue created by migration from https://trac.sagemath.org/ticket/6454





---

archive/issue_comments_051964.json:
```json
{
    "body": "Attachment [trac_6454_sbox.patch](tarball://root/attachments/some-uuid/ticket6454/trac_6454_sbox.patch) by ylchapuy created at 2009-07-01 09:31:17",
    "created_at": "2009-07-01T09:31:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6454#issuecomment-51964",
    "user": "ylchapuy"
}
```

Attachment [trac_6454_sbox.patch](tarball://root/attachments/some-uuid/ticket6454/trac_6454_sbox.patch) by ylchapuy created at 2009-07-01 09:31:17



---

archive/issue_comments_051965.json:
```json
{
    "body": "Hi there, it is embarrassing how bad my naive original code was. Here's a comparison (for the release tour)\n\n**Old***\n\n\n```\nsage: S = mq.SR(1,4,4,8).sbox()\nsage: %time _ = S.difference_distribution_matrix()\nCPU times: user 82.14 s, sys: 0.01 s, total: 82.15 s\nWall time: 82.15 s\n\nsage: %time _ = S.linear_approximation_matrix()\nCPU times: user 145.10 s, sys: 0.02 s, total: 145.12 s\nWall time: 145.12 s\n```\n\n\n***New***\n\n\n```\nsage: S = mq.SR(1,4,4,8).sbox()\nsage: %time _ = S.difference_distribution_matrix()\nCPU times: user 0.32 s, sys: 0.00 s, total: 0.32 s\nWall time: 0.32 s\nsage: %time _ = S.linear_approximation_matrix()\nCPU times: user 1.10 s, sys: 0.00 s, total: 1.10 s\nWall time: 1.10 s\n```\n\n\nThe code looks good, doctests pass.\n\nThe only issue: the `sage -coverage` script will pick up `_walsh_transform` and complain that it isn't documented and doctested. \n\nOf course it is impossible to doctest this inner function directly, but the keyword `# indirect doctest` will do the trick.\n\nThis is a positive review except for the missing documentation.",
    "created_at": "2009-07-01T11:06:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6454#issuecomment-51965",
    "user": "malb"
}
```

Hi there, it is embarrassing how bad my naive original code was. Here's a comparison (for the release tour)

**Old***


```
sage: S = mq.SR(1,4,4,8).sbox()
sage: %time _ = S.difference_distribution_matrix()
CPU times: user 82.14 s, sys: 0.01 s, total: 82.15 s
Wall time: 82.15 s

sage: %time _ = S.linear_approximation_matrix()
CPU times: user 145.10 s, sys: 0.02 s, total: 145.12 s
Wall time: 145.12 s
```


***New***


```
sage: S = mq.SR(1,4,4,8).sbox()
sage: %time _ = S.difference_distribution_matrix()
CPU times: user 0.32 s, sys: 0.00 s, total: 0.32 s
Wall time: 0.32 s
sage: %time _ = S.linear_approximation_matrix()
CPU times: user 1.10 s, sys: 0.00 s, total: 1.10 s
Wall time: 1.10 s
```


The code looks good, doctests pass.

The only issue: the `sage -coverage` script will pick up `_walsh_transform` and complain that it isn't documented and doctested. 

Of course it is impossible to doctest this inner function directly, but the keyword `# indirect doctest` will do the trick.

This is a positive review except for the missing documentation.



---

archive/issue_comments_051966.json:
```json
{
    "body": "Attachment [trac_6454_review.patch](tarball://root/attachments/some-uuid/ticket6454/trac_6454_review.patch) by ylchapuy created at 2009-07-01 12:16:56\n\nBoth patches should be applied.\n\nI added an indirect doctest. I give myself a positive review, feel free to correct me if you disagree.",
    "created_at": "2009-07-01T12:16:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6454#issuecomment-51966",
    "user": "ylchapuy"
}
```

Attachment [trac_6454_review.patch](tarball://root/attachments/some-uuid/ticket6454/trac_6454_review.patch) by ylchapuy created at 2009-07-01 12:16:56

Both patches should be applied.

I added an indirect doctest. I give myself a positive review, feel free to correct me if you disagree.



---

archive/issue_comments_051967.json:
```json
{
    "body": "All good, definitively a positive review.",
    "created_at": "2009-07-01T12:36:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6454#issuecomment-51967",
    "user": "malb"
}
```

All good, definitively a positive review.



---

archive/issue_comments_051968.json:
```json
{
    "body": "Just to let people know, this has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(",
    "created_at": "2009-07-16T10:23:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6454#issuecomment-51968",
    "user": "mvngu"
}
```

Just to let people know, this has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(



---

archive/issue_comments_051969.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-16T21:31:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6454#issuecomment-51969",
    "user": "mvngu"
}
```

Resolution: fixed
