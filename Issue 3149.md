# Issue 3149: [with patch, needs review] off-by-one error in real_roots on AA coefficients

archive/issues_003149.json:
```json
{
    "body": "Assignee: @malb\n\nThe code in real_roots.pyx for handling polynomials with AA coefficients had an off-by-one error in the case of integral coefficients.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3149\n\n",
    "created_at": "2008-05-10T17:36:20Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with patch, needs review] off-by-one error in real_roots on AA coefficients",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3149",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @malb

The code in real_roots.pyx for handling polynomials with AA coefficients had an off-by-one error in the case of integral coefficients.

Issue created by migration from https://trac.sagemath.org/ticket/3149





---

archive/issue_comments_021795.json:
```json
{
    "body": "Attachment [real-roots-offbyone.patch](tarball://root/attachments/some-uuid/ticket3149/real-roots-offbyone.patch) by @malb created at 2008-06-03 16:29:16",
    "created_at": "2008-06-03T16:29:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3149#issuecomment-21795",
    "user": "https://github.com/malb"
}
```

Attachment [real-roots-offbyone.patch](tarball://root/attachments/some-uuid/ticket3149/real-roots-offbyone.patch) by @malb created at 2008-06-03 16:29:16



---

archive/issue_comments_021796.json:
```json
{
    "body": "Remove assignee @malb.",
    "created_at": "2008-06-03T16:29:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3149#issuecomment-21796",
    "user": "https://github.com/malb"
}
```

Remove assignee @malb.



---

archive/issue_comments_021797.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_craigcitro\".",
    "created_at": "2008-06-15T21:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3149#issuecomment-21797",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "" to "editor_craigcitro".



---

archive/issue_comments_021798.json:
```json
{
    "body": "Looks good. Just so that it's on record:\n\nthe 4 -> 6 change simply ups the default precision to which something is computed. The `ceil()` to `floor() + 1` change only applies in the case of an exact answer, and this way the strict inequality requested in the new comment is always satisfied. The doctest exactly checks this.",
    "created_at": "2008-06-15T22:34:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3149#issuecomment-21798",
    "user": "https://github.com/craigcitro"
}
```

Looks good. Just so that it's on record:

the 4 -> 6 change simply ups the default precision to which something is computed. The `ceil()` to `floor() + 1` change only applies in the case of an exact answer, and this way the strict inequality requested in the new comment is always satisfied. The doctest exactly checks this.



---

archive/issue_comments_021799.json:
```json
{
    "body": "Set assignee to cwitty.",
    "created_at": "2008-06-16T19:06:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3149#issuecomment-21799",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Set assignee to cwitty.



---

archive/issue_comments_021800.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-23T05:53:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3149#issuecomment-21800",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021801.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha0",
    "created_at": "2008-06-23T05:53:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3149#issuecomment-21801",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha0
