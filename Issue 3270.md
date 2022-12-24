# Issue 3270: [with patch, easy review] trivial 100x speedup in coding theory

archive/issues_003270.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @wdjoyner\n\nWas:\n\n```\nsage: C = ExtendedBinaryGolayCode()\nsage: time G = C.permutation_automorphism_group()\nCPU times: user 2.39 s, sys: 0.58 s, total: 2.97 s\nWall time: 24.32\n```\n\nNow:\n\n```\nsage: C = ExtendedBinaryGolayCode()\nsage: time G = C.permutation_automorphism_group()\nCPU times: user 0.19 s, sys: 0.04 s, total: 0.23 s\nWall time: 0.24\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3270\n\n",
    "created_at": "2008-05-22T00:26:04Z",
    "labels": [
        "coding theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "[with patch, easy review] trivial 100x speedup in coding theory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3270",
    "user": "@rlmill"
}
```
Assignee: @rlmill

CC:  @wdjoyner

Was:

```
sage: C = ExtendedBinaryGolayCode()
sage: time G = C.permutation_automorphism_group()
CPU times: user 2.39 s, sys: 0.58 s, total: 2.97 s
Wall time: 24.32
```

Now:

```
sage: C = ExtendedBinaryGolayCode()
sage: time G = C.permutation_automorphism_group()
CPU times: user 0.19 s, sys: 0.04 s, total: 0.23 s
Wall time: 0.24
```


Issue created by migration from https://trac.sagemath.org/ticket/3270





---

archive/issue_comments_022636.json:
```json
{
    "body": "Attachment [3270-bc_default.patch](tarball://root/attachments/some-uuid/ticket3270/3270-bc_default.patch) by @mwhansen created at 2008-05-22 09:16:43\n\nLooks good to me.",
    "created_at": "2008-05-22T09:16:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3270",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3270#issuecomment-22636",
    "user": "@mwhansen"
}
```

Attachment [3270-bc_default.patch](tarball://root/attachments/some-uuid/ticket3270/3270-bc_default.patch) by @mwhansen created at 2008-05-22 09:16:43

Looks good to me.



---

archive/issue_comments_022637.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-22T10:36:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3270",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3270#issuecomment-22637",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022638.json:
```json
{
    "body": "Merged in Sage 3.0.2.rc0",
    "created_at": "2008-05-22T10:36:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3270",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3270#issuecomment-22638",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.2.rc0
