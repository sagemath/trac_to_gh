# Issue 3275: [with patch, needs review] Make SL2Z distinct

archive/issues_003275.json:
```json
{
    "body": "Assignee: @craigcitro\n\nThis patch changes `SL2Z` to be a distinct object, as opposed to a class. The following error was brought up on `sage-support`:\n\n\n```\nsage: S = SL2Z()([0,-1,1,0])\nsage: T = SL2Z()([1,1,0,1])\nsage: S*T\n...\n<type 'exceptions.RuntimeError'>: There is a bug in the coercion code in SAGE.\n```\n\n\nThe issue (as the poster pointed out) is that the parents of S and T are distinct copies of `SL2Z`, when they don't need to be. Indeed, I don't see any difference between this and other distinct rings in Sage (such as `ZZ`, `QQ`, etc), so I've made it distinct.\n\nNow the above becomes:\n\n```\nsage: S = SL2Z.([0,-1,1,0])\nsage: T = SL2Z.([1,1,0,1])\nsage: S*T\n[ 0 -1]\n[ 1  1]\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3275\n\n",
    "created_at": "2008-05-23T07:58:31Z",
    "labels": [
        "modular forms",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "[with patch, needs review] Make SL2Z distinct",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3275",
    "user": "@craigcitro"
}
```
Assignee: @craigcitro

This patch changes `SL2Z` to be a distinct object, as opposed to a class. The following error was brought up on `sage-support`:


```
sage: S = SL2Z()([0,-1,1,0])
sage: T = SL2Z()([1,1,0,1])
sage: S*T
...
<type 'exceptions.RuntimeError'>: There is a bug in the coercion code in SAGE.
```


The issue (as the poster pointed out) is that the parents of S and T are distinct copies of `SL2Z`, when they don't need to be. Indeed, I don't see any difference between this and other distinct rings in Sage (such as `ZZ`, `QQ`, etc), so I've made it distinct.

Now the above becomes:

```
sage: S = SL2Z.([0,-1,1,0])
sage: T = SL2Z.([1,1,0,1])
sage: S*T
[ 0 -1]
[ 1  1]
```




Issue created by migration from https://trac.sagemath.org/ticket/3275





---

archive/issue_comments_022654.json:
```json
{
    "body": "Attachment [trac-3275.patch](tarball://root/attachments/some-uuid/ticket3275/trac-3275.patch) by @craigcitro created at 2008-05-23 07:59:02",
    "created_at": "2008-05-23T07:59:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3275#issuecomment-22654",
    "user": "@craigcitro"
}
```

Attachment [trac-3275.patch](tarball://root/attachments/some-uuid/ticket3275/trac-3275.patch) by @craigcitro created at 2008-05-23 07:59:02



---

archive/issue_comments_022655.json:
```json
{
    "body": "looks good to me, but i haven't tried applying the patch or testing...",
    "created_at": "2008-05-23T08:01:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3275#issuecomment-22655",
    "user": "@rlmill"
}
```

looks good to me, but i haven't tried applying the patch or testing...



---

archive/issue_comments_022656.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-23T08:20:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3275#issuecomment-22656",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022657.json:
```json
{
    "body": "Merged in Sage 3.0.2.rc0. Testall long passes.",
    "created_at": "2008-05-23T08:20:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3275",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3275#issuecomment-22657",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.2.rc0. Testall long passes.
