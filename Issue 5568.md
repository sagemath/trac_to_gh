# Issue 5568: [with patch, needs review] a few latex methods

archive/issues_005568.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nTwo issues: QQbar doesn't seem to have a latex method. Also, the latex method for CC is \"\\\\C\", which is not a valid LaTeX command. For example, if I type \"view(CC)\" in the notebook, jsmath gives an error, and if I type \"view(CC)\" from the command line, I get a blank page.\n\nThis patch provides a latex method for QQbar and changes the latex method for CC (note that it uses `\\mathbf`, just as the latex methods for RR, ZZ, and QQ do).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5568\n\n",
    "created_at": "2009-03-19T17:59:55Z",
    "labels": [
        "component: misc",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, needs review] a few latex methods",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5568",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

Two issues: QQbar doesn't seem to have a latex method. Also, the latex method for CC is "\\C", which is not a valid LaTeX command. For example, if I type "view(CC)" in the notebook, jsmath gives an error, and if I type "view(CC)" from the command line, I get a blank page.

This patch provides a latex method for QQbar and changes the latex method for CC (note that it uses `\mathbf`, just as the latex methods for RR, ZZ, and QQ do).


Issue created by migration from https://trac.sagemath.org/ticket/5568





---

archive/issue_comments_043305.json:
```json
{
    "body": "Attachment [latex-methods.patch](tarball://root/attachments/some-uuid/ticket5568/latex-methods.patch) by @rbeezer created at 2009-03-25 03:25:59\n\nLooks good.  Positive review.",
    "created_at": "2009-03-25T03:25:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5568#issuecomment-43305",
    "user": "https://github.com/rbeezer"
}
```

Attachment [latex-methods.patch](tarball://root/attachments/some-uuid/ticket5568/latex-methods.patch) by @rbeezer created at 2009-03-25 03:25:59

Looks good.  Positive review.



---

archive/issue_comments_043306.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T07:42:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5568#issuecomment-43306",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_events_005814.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-03-25T07:42:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5568",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5568#event-5814"
}
```



---

archive/issue_comments_043307.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-25T07:42:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5568",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5568#issuecomment-43307",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
