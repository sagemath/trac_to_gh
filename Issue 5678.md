# Issue 5678: LaTeX typesetting for two letters phi and Phi

archive/issues_005678.json:
```json
{
    "body": "Assignee: cwitty\n\nKeywords: Latex,\n\nIn the list \"common_varnames\" (in sage/misc/latex.py) two\nGreek letters \"phi\" and \"Phi\" are missing. So LaTeX typesetting\nfor them doesn't work unlike other Greek letters.\n\nThis issue has been discussed in the thread\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/a51f269f057d8223\n\nA patch (created on top of sage-3.4) to fix this issue is attached.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5678\n\n",
    "created_at": "2009-04-04T01:34:08Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "title": "LaTeX typesetting for two letters phi and Phi",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5678",
    "user": "gmhossain"
}
```
Assignee: cwitty

Keywords: Latex,

In the list "common_varnames" (in sage/misc/latex.py) two
Greek letters "phi" and "Phi" are missing. So LaTeX typesetting
for them doesn't work unlike other Greek letters.

This issue has been discussed in the thread

http://groups.google.com/group/sage-devel/browse_thread/thread/a51f269f057d8223

A patch (created on top of sage-3.4) to fix this issue is attached.

Issue created by migration from https://trac.sagemath.org/ticket/5678





---

archive/issue_comments_044414.json:
```json
{
    "body": "Attachment [missing-phi-Phi.patch](tarball://root/attachments/some-uuid/ticket5678/missing-phi-Phi.patch) by gmhossain created at 2009-04-04 01:34:41",
    "created_at": "2009-04-04T01:34:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5678#issuecomment-44414",
    "user": "gmhossain"
}
```

Attachment [missing-phi-Phi.patch](tarball://root/attachments/some-uuid/ticket5678/missing-phi-Phi.patch) by gmhossain created at 2009-04-04 01:34:41



---

archive/issue_comments_044415.json:
```json
{
    "body": "Looks good to me: a trivial fix.\n\n(gmhossain: your subject should have been: \"[with patch, needs review] LaTeX typesetting for two letters phi and Phi\")",
    "created_at": "2009-04-06T23:06:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5678#issuecomment-44415",
    "user": "jhpalmieri"
}
```

Looks good to me: a trivial fix.

(gmhossain: your subject should have been: "[with patch, needs review] LaTeX typesetting for two letters phi and Phi")



---

archive/issue_comments_044416.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-09T09:42:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5678#issuecomment-44416",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_044417.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T09:42:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5678#issuecomment-44417",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc2.

Cheers,

Michael
