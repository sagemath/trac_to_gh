# Issue 3858: [with patch, needs review] 3.1alpha: fix issues with the reference manual

archive/issues_003858.json:
```json
{
    "body": "Assignee: tba\n\nKeywords: documentation, reference\n\nThis may be premature (and if it is, feel free to ignore/dispose of this ticket), but when I tried to build the reference manual in 3.1alpha, there were a bunch of small errors -- things like `\"\"\"` instead of `r\"\"\"`, immediately followed by a docstring using backslashes.  This patch fixes these.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3858\n\n",
    "created_at": "2008-08-14T22:05:46Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1",
    "title": "[with patch, needs review] 3.1alpha: fix issues with the reference manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3858",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: tba

Keywords: documentation, reference

This may be premature (and if it is, feel free to ignore/dispose of this ticket), but when I tried to build the reference manual in 3.1alpha, there were a bunch of small errors -- things like `"""` instead of `r"""`, immediately followed by a docstring using backslashes.  This patch fixes these.



Issue created by migration from https://trac.sagemath.org/ticket/3858





---

archive/issue_comments_027424.json:
```json
{
    "body": "Attachment [ref.patch](tarball://root/attachments/some-uuid/ticket3858/ref.patch) by mabshoff created at 2008-08-14 22:08:32\n\nHi John,\n\nthanks a lot for doing this. Usually we end up doing this at the last minute, so thanks again :)\n\nCheers,\n\nMichael",
    "created_at": "2008-08-14T22:08:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3858#issuecomment-27424",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [ref.patch](tarball://root/attachments/some-uuid/ticket3858/ref.patch) by mabshoff created at 2008-08-14 22:08:32

Hi John,

thanks a lot for doing this. Usually we end up doing this at the last minute, so thanks again :)

Cheers,

Michael



---

archive/issue_comments_027425.json:
```json
{
    "body": "Patch looks good to me. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-15T09:45:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3858#issuecomment-27425",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me. Positive review.

Cheers,

Michael



---

archive/issue_comments_027426.json:
```json
{
    "body": "Merged in Sage 3.1.rc0",
    "created_at": "2008-08-15T09:45:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3858#issuecomment-27426",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.rc0



---

archive/issue_comments_027427.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-15T09:45:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3858",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3858#issuecomment-27427",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
