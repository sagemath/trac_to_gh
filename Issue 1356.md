# Issue 1356: [with patch] fix bug when taking abs() of exactly known QQbar

archive/issues_001356.json:
```json
{
    "body": "Assignee: somebody\n\nThe following test fails in 2.8.15.alpha1:\n\n```\n            sage: v = QQbar.zeta(3) + 1\n            sage: v.exactify()\n            sage: v.abs().minpoly()\n```\n\nbut the attached patch fixes it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1356\n\n",
    "created_at": "2007-12-02T01:25:31Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "[with patch] fix bug when taking abs() of exactly known QQbar",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1356",
    "user": "cwitty"
}
```
Assignee: somebody

The following test fails in 2.8.15.alpha1:

```
            sage: v = QQbar.zeta(3) + 1
            sage: v.exactify()
            sage: v.abs().minpoly()
```

but the attached patch fixes it.

Issue created by migration from https://trac.sagemath.org/ticket/1356





---

archive/issue_comments_008673.json:
```json
{
    "body": "Attachment [1356.patch](tarball://root/attachments/some-uuid/ticket1356/1356.patch) by @rlmill created at 2007-12-02 19:34:21\n\nNow:\n\n```\nsage: v = QQbar.zeta(3) + 1\nsage: v.exactify()\nsage: v.abs().minpoly()\nx - 1\n```\n",
    "created_at": "2007-12-02T19:34:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1356#issuecomment-8673",
    "user": "@rlmill"
}
```

Attachment [1356.patch](tarball://root/attachments/some-uuid/ticket1356/1356.patch) by @rlmill created at 2007-12-02 19:34:21

Now:

```
sage: v = QQbar.zeta(3) + 1
sage: v.exactify()
sage: v.abs().minpoly()
x - 1
```




---

archive/issue_comments_008674.json:
```json
{
    "body": "looks good to me.",
    "created_at": "2007-12-02T19:38:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1356#issuecomment-8674",
    "user": "@williamstein"
}
```

looks good to me.



---

archive/issue_comments_008675.json:
```json
{
    "body": "Merged in 2.8.15.rc0.",
    "created_at": "2007-12-02T20:12:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1356#issuecomment-8675",
    "user": "mabshoff"
}
```

Merged in 2.8.15.rc0.



---

archive/issue_comments_008676.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-02T20:12:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1356",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1356#issuecomment-8676",
    "user": "mabshoff"
}
```

Resolution: fixed
