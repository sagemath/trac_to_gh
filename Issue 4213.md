# Issue 4213: Bug in Permutations(n, k)

archive/issues_004213.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\n\n```\nsage: list(Permutations([1,2,3,4,5], 4))\n\n[ ...\n [2, 3, 1, 5],\n [2, 3, 3, 1],\n [2, 3, 3, 4],\n [2, 3, 3, 5],\n [2, 3, 4, 1],\n ...\n [3, 2, 1, 5],\n [3, 2, 2, 1],\n [3, 2, 2, 4],\n [3, 2, 2, 5],\n [3, 2, 4, 1],\n ...\n [4, 2, 1, 5],\n [4, 2, 2, 1],\n [4, 2, 2, 3],\n [4, 2, 2, 5],\n [4, 2, 3, 1],\n ...\n [5, 2, 1, 4],\n [5, 2, 2, 1],\n [5, 2, 2, 3],\n [5, 2, 2, 4],\n [5, 2, 3, 1],\n```\n\n\nOnly the buggy parts are shown.\n\nThis does not occur for lists smaller that 5 or when len(n) == k.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4213\n\n",
    "created_at": "2008-09-28T21:26:17Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "Bug in Permutations(n, k)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4213",
    "user": "anakha"
}
```
Assignee: mhansen

CC:  sage-combinat


```
sage: list(Permutations([1,2,3,4,5], 4))

[ ...
 [2, 3, 1, 5],
 [2, 3, 3, 1],
 [2, 3, 3, 4],
 [2, 3, 3, 5],
 [2, 3, 4, 1],
 ...
 [3, 2, 1, 5],
 [3, 2, 2, 1],
 [3, 2, 2, 4],
 [3, 2, 2, 5],
 [3, 2, 4, 1],
 ...
 [4, 2, 1, 5],
 [4, 2, 2, 1],
 [4, 2, 2, 3],
 [4, 2, 2, 5],
 [4, 2, 3, 1],
 ...
 [5, 2, 1, 4],
 [5, 2, 2, 1],
 [5, 2, 2, 3],
 [5, 2, 2, 4],
 [5, 2, 3, 1],
```


Only the buggy parts are shown.

This does not occur for lists smaller that 5 or when len(n) == k.

Issue created by migration from https://trac.sagemath.org/ticket/4213





---

archive/issue_comments_030614.json:
```json
{
    "body": "Attachment [trac_4213.patch](tarball://root/attachments/some-uuid/ticket4213/trac_4213.patch) by mhansen created at 2008-09-28 21:51:14",
    "created_at": "2008-09-28T21:51:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4213#issuecomment-30614",
    "user": "mhansen"
}
```

Attachment [trac_4213.patch](tarball://root/attachments/some-uuid/ticket4213/trac_4213.patch) by mhansen created at 2008-09-28 21:51:14



---

archive/issue_comments_030615.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-28T21:51:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4213#issuecomment-30615",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030616.json:
```json
{
    "body": "Passes tests and fixes the problem on my end.",
    "created_at": "2008-09-28T22:13:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4213#issuecomment-30616",
    "user": "anakha"
}
```

Passes tests and fixes the problem on my end.



---

archive/issue_comments_030617.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha2",
    "created_at": "2008-09-29T02:14:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4213#issuecomment-30617",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.alpha2



---

archive/issue_comments_030618.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-29T02:14:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4213",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4213#issuecomment-30618",
    "user": "mabshoff"
}
```

Resolution: fixed
