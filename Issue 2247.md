# Issue 2247: [with patch, needs wildly trivial review] comment out long doctest in totallyreal_rel.py

archive/issues_002247.json:
```json
{
    "body": "Assignee: craigcitro\n\nThere's a really long doctest in sage/rings/number_field/totallyreal_rel.py. We can't just `# long` it, because it also needs to use `# 32-bit`/`# 64-bit`, and these two don't play nicely together. This patch makes it into a `# no doctest` for now to avoid timeouts.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2247\n\n",
    "created_at": "2008-02-21T18:15:39Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "[with patch, needs wildly trivial review] comment out long doctest in totallyreal_rel.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2247",
    "user": "craigcitro"
}
```
Assignee: craigcitro

There's a really long doctest in sage/rings/number_field/totallyreal_rel.py. We can't just `# long` it, because it also needs to use `# 32-bit`/`# 64-bit`, and these two don't play nicely together. This patch makes it into a `# no doctest` for now to avoid timeouts.

Issue created by migration from https://trac.sagemath.org/ticket/2247





---

archive/issue_comments_014896.json:
```json
{
    "body": "Attachment [long-test.patch](tarball://root/attachments/some-uuid/ticket2247/long-test.patch) by craigcitro created at 2008-02-21 18:16:07",
    "created_at": "2008-02-21T18:16:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2247",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2247#issuecomment-14896",
    "user": "craigcitro"
}
```

Attachment [long-test.patch](tarball://root/attachments/some-uuid/ticket2247/long-test.patch) by craigcitro created at 2008-02-21 18:16:07



---

archive/issue_comments_014897.json:
```json
{
    "body": "Patch looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-21T18:29:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2247",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2247#issuecomment-14897",
    "user": "mabshoff"
}
```

Patch looks good to me.

Cheers,

Michael



---

archive/issue_comments_014898.json:
```json
{
    "body": "Merged in Sage 2.10.2.rc0",
    "created_at": "2008-02-21T18:29:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2247",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2247#issuecomment-14898",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.rc0



---

archive/issue_comments_014899.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-21T18:29:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2247",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2247#issuecomment-14899",
    "user": "mabshoff"
}
```

Resolution: fixed
