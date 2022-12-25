# Issue 5678: [with patch, positive review] LaTeX typesetting for two letters phi and Phi

archive/issues_005678.json:
```json
{
    "body": "Assignee: cwitty\n\nKeywords: Latex,\n\nIn the list \"common_varnames\" (in sage/misc/latex.py) two\nGreek letters \"phi\" and \"Phi\" are missing. So LaTeX typesetting\nfor them doesn't work unlike other Greek letters.\n\nThis issue has been discussed in the thread\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/a51f269f057d8223\n\nA patch (created on top of sage-3.4) to fix this issue is attached.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5678\n\n",
    "closed_at": "2009-04-09T09:42:51Z",
    "created_at": "2009-04-04T01:34:08Z",
    "labels": [
        "component: misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, positive review] LaTeX typesetting for two letters phi and Phi",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5678",
    "user": "https://github.com/golam-m-hossain"
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

archive/issue_comments_044329.json:
```json
{
    "body": "Attachment [missing-phi-Phi.patch](tarball://root/attachments/some-uuid/ticket5678/missing-phi-Phi.patch) by @golam-m-hossain created at 2009-04-04 01:34:41",
    "created_at": "2009-04-04T01:34:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5678#issuecomment-44329",
    "user": "https://github.com/golam-m-hossain"
}
```

Attachment [missing-phi-Phi.patch](tarball://root/attachments/some-uuid/ticket5678/missing-phi-Phi.patch) by @golam-m-hossain created at 2009-04-04 01:34:41



---

archive/issue_comments_044330.json:
```json
{
    "body": "Looks good to me: a trivial fix.\n\n(gmhossain: your subject should have been: \"[with patch, needs review] LaTeX typesetting for two letters phi and Phi\")",
    "created_at": "2009-04-06T23:06:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5678#issuecomment-44330",
    "user": "https://github.com/jhpalmieri"
}
```

Looks good to me: a trivial fix.

(gmhossain: your subject should have been: "[with patch, needs review] LaTeX typesetting for two letters phi and Phi")



---

archive/issue_events_013352.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-09T09:42:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5678",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5678#event-13352"
}
```



---

archive/issue_comments_044331.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-09T09:42:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5678#issuecomment-44331",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_044332.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T09:42:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5678",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5678#issuecomment-44332",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc2.

Cheers,

Michael



---

archive/issue_events_013353.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-09T09:42:51Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5678",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5678#event-13353"
}
```
