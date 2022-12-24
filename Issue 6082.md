# Issue 6082: [with patch, needs review] realloc called too often for Integer construction/deconstruction

archive/issues_006082.json:
```json
{
    "body": "Assignee: somebody\n\nWhen putting objects back into the pool, we realloc the `mpz_t` to a smaller size to be able to reclaim the memory for larger integers. Unfortunately, chopping them to one limb means that they will often need to grow again (even if subsequent arithmetic fits in a limb). \n\nIssue created by migration from https://trac.sagemath.org/ticket/6082\n\n",
    "created_at": "2009-05-19T06:02:38Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] realloc called too often for Integer construction/deconstruction",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6082",
    "user": "robertwb"
}
```
Assignee: somebody

When putting objects back into the pool, we realloc the `mpz_t` to a smaller size to be able to reclaim the memory for larger integers. Unfortunately, chopping them to one limb means that they will often need to grow again (even if subsequent arithmetic fits in a limb). 

Issue created by migration from https://trac.sagemath.org/ticket/6082





---

archive/issue_comments_048407.json:
```json
{
    "body": "Attachment [6082-integer-speed.patch](tarball://root/attachments/some-uuid/ticket6082/6082-integer-speed.patch) by robertwb created at 2009-05-20 21:12:11\n\nNow it only reclaims the memory if more than 10 limbs (80 bytes) are used.",
    "created_at": "2009-05-20T21:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6082#issuecomment-48407",
    "user": "robertwb"
}
```

Attachment [6082-integer-speed.patch](tarball://root/attachments/some-uuid/ticket6082/6082-integer-speed.patch) by robertwb created at 2009-05-20 21:12:11

Now it only reclaims the memory if more than 10 limbs (80 bytes) are used.



---

archive/issue_comments_048408.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-21T02:08:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6082#issuecomment-48408",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_048409.json:
```json
{
    "body": "Merged in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-21T02:08:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6082",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6082#issuecomment-48409",
    "user": "mabshoff"
}
```

Merged in Sage 4.0.rc0.

Cheers,

Michael
