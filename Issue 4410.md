# Issue 4410: [with patch, needs review] Map.__pow__ should return identity for power 0

archive/issues_004410.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  robertwb\n\n`sage.categories.map.Map.__pow__` calls `generic_power`, which messes up power 0. There is this todo note there:\n\n\n```\n        # todo -- what about the case n=0 -- need to specify the identity map somehow.\n```\n\n\nAttached patch returns the identity map for power 0.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4410\n\n",
    "created_at": "2008-10-31T09:05:10Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] Map.__pow__ should return identity for power 0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4410",
    "user": "burcin"
}
```
Assignee: burcin

CC:  robertwb

`sage.categories.map.Map.__pow__` calls `generic_power`, which messes up power 0. There is this todo note there:


```
        # todo -- what about the case n=0 -- need to specify the identity map somehow.
```


Attached patch returns the identity map for power 0.

Issue created by migration from https://trac.sagemath.org/ticket/4410





---

archive/issue_comments_032421.json:
```json
{
    "body": "make Map.__pow__ return identity for power 0",
    "created_at": "2008-10-31T09:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4410#issuecomment-32421",
    "user": "burcin"
}
```

make Map.__pow__ return identity for power 0



---

archive/issue_comments_032422.json:
```json
{
    "body": "Attachment [trac_4410_map_pow.patch](tarball://root/attachments/some-uuid/ticket4410/trac_4410_map_pow.patch) by mabshoff created at 2008-10-31 15:35:42\n\nThis is the suggested fix discussed by RobertWB and Burcin in IRC last night. The code looks correct and passes doctests, positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-31T15:35:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4410#issuecomment-32422",
    "user": "mabshoff"
}
```

Attachment [trac_4410_map_pow.patch](tarball://root/attachments/some-uuid/ticket4410/trac_4410_map_pow.patch) by mabshoff created at 2008-10-31 15:35:42

This is the suggested fix discussed by RobertWB and Burcin in IRC last night. The code looks correct and passes doctests, positive review.

Cheers,

Michael



---

archive/issue_comments_032423.json:
```json
{
    "body": "Merged in Sage 3.2.alpha2",
    "created_at": "2008-10-31T15:36:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4410#issuecomment-32423",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha2



---

archive/issue_comments_032424.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-31T15:36:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4410#issuecomment-32424",
    "user": "mabshoff"
}
```

Resolution: fixed
