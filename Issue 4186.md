# Issue 4186: [with patch, needs review] speed up default __call__

archive/issues_004186.json:
```json
{
    "body": "Assignee: robertwb\n\nAs this is used everywhere, I added a couple more optimizations. Cython generates less then optimal code here too, which I will fix. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4186\n\n",
    "created_at": "2008-09-24T08:41:15Z",
    "labels": [
        "coercion",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] speed up default __call__",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4186",
    "user": "robertwb"
}
```
Assignee: robertwb

As this is used everywhere, I added a couple more optimizations. Cython generates less then optimal code here too, which I will fix. 



Issue created by migration from https://trac.sagemath.org/ticket/4186





---

archive/issue_comments_030382.json:
```json
{
    "body": "Attachment [4186-faster-call.patch](tarball://root/attachments/some-uuid/ticket4186/4186-faster-call.patch) by mhansen created at 2008-09-24 09:23:14\n\nLooks good to me.",
    "created_at": "2008-09-24T09:23:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4186#issuecomment-30382",
    "user": "mhansen"
}
```

Attachment [4186-faster-call.patch](tarball://root/attachments/some-uuid/ticket4186/4186-faster-call.patch) by mhansen created at 2008-09-24 09:23:14

Looks good to me.



---

archive/issue_comments_030383.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-24T10:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4186#issuecomment-30383",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030384.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha1. It does not get the speed down to the old value, but shaves about 40 seconds off, so I will take this improvement :)\n\nCheers,\n\nMichael",
    "created_at": "2008-09-24T10:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4186#issuecomment-30384",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.alpha1. It does not get the speed down to the old value, but shaves about 40 seconds off, so I will take this improvement :)

Cheers,

Michael



---

archive/issue_comments_030385.json:
```json
{
    "body": "Hmm... It was faster on the subset of that test that I ran. There's still improvements to be made though (like when the new Cython comes out it should shave at least that much off again).",
    "created_at": "2008-09-24T16:41:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4186#issuecomment-30385",
    "user": "robertwb"
}
```

Hmm... It was faster on the subset of that test that I ran. There's still improvements to be made though (like when the new Cython comes out it should shave at least that much off again).
