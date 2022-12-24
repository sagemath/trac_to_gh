# Issue 2846: [with patch] no need for bitset.h with new Cython

archive/issues_002846.json:
```json
{
    "body": "Assignee: cwitty\n\nI've modified the .pxi file\n\nIssue created by migration from https://trac.sagemath.org/ticket/2846\n\n",
    "created_at": "2008-04-07T18:36:43Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "[with patch] no need for bitset.h with new Cython",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2846",
    "user": "robertwb"
}
```
Assignee: cwitty

I've modified the .pxi file

Issue created by migration from https://trac.sagemath.org/ticket/2846





---

archive/issue_comments_019530.json:
```json
{
    "body": "Attachment [2846-bitset-no-h.patch](tarball://root/attachments/some-uuid/ticket2846/2846-bitset-no-h.patch) by robertwb created at 2008-04-07 18:37:41",
    "created_at": "2008-04-07T18:37:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2846#issuecomment-19530",
    "user": "robertwb"
}
```

Attachment [2846-bitset-no-h.patch](tarball://root/attachments/some-uuid/ticket2846/2846-bitset-no-h.patch) by robertwb created at 2008-04-07 18:37:41



---

archive/issue_comments_019531.json:
```json
{
    "body": "Patch looks good to me, passes a {{-ba}} followed by a successful `testall long`. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-07T20:49:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2846#issuecomment-19531",
    "user": "mabshoff"
}
```

Patch looks good to me, passes a {{-ba}} followed by a successful `testall long`. Positive review.

Cheers,

Michael



---

archive/issue_comments_019532.json:
```json
{
    "body": "Merged in Sage 3.0.alpha3",
    "created_at": "2008-04-07T20:50:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2846#issuecomment-19532",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha3



---

archive/issue_comments_019533.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-07T20:50:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2846#issuecomment-19533",
    "user": "mabshoff"
}
```

Resolution: fixed
