# Issue 5832: [with patch, not ready for review] reducible root system fixes

archive/issues_005832.json:
```json
{
    "body": "Assignee: @dwbump\n\nCC:  sage-combinat\n\nThe methods simple_roots(), fundamental_weights() and simple_coroots() for the ambient space of a root system are supposed to return a family. This was never correctly implemented for the reducible types, and the patch corrects this.\n\nThere are also some changes in weyl_characters.py, where it was assumed that the root system was irreducible in a few places. The patch corrects this.\n\nThe patch is probably correct but I haven't confirmed that it applies cleanly to sage-3.4.1.rc3 or that it passes `sage --testall` so wait to review.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5832\n\n",
    "created_at": "2009-04-20T05:12:05Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch, not ready for review] reducible root system fixes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5832",
    "user": "https://github.com/dwbump"
}
```
Assignee: @dwbump

CC:  sage-combinat

The methods simple_roots(), fundamental_weights() and simple_coroots() for the ambient space of a root system are supposed to return a family. This was never correctly implemented for the reducible types, and the patch corrects this.

There are also some changes in weyl_characters.py, where it was assumed that the root system was irreducible in a few places. The patch corrects this.

The patch is probably correct but I haven't confirmed that it applies cleanly to sage-3.4.1.rc3 or that it passes `sage --testall` so wait to review.

Issue created by migration from https://trac.sagemath.org/ticket/5832





---

archive/issue_comments_045755.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-04-20T05:16:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5832",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5832#issuecomment-45755",
    "user": "https://github.com/dwbump"
}
```

Resolution: duplicate



---

archive/issue_comments_045756.json:
```json
{
    "body": "For the record: This is a dupe of #5832.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-20T06:02:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5832",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5832#issuecomment-45756",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

For the record: This is a dupe of #5832.

Cheers,

Michael



---

archive/issue_comments_045757.json:
```json
{
    "body": "Ehh, obviously a dupe not of this ticket, but #5831.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-20T06:04:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5832",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5832#issuecomment-45757",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ehh, obviously a dupe not of this ticket, but #5831.

Cheers,

Michael
