# Issue 5536: [with patch, review pending] trivial docstring patches for permgp.py

archive/issues_005536.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nThe subject says it all.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5536\n\n",
    "created_at": "2009-03-16T22:50:39Z",
    "labels": [
        "component: group theory",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, review pending] trivial docstring patches for permgp.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5536",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

The subject says it all.


Issue created by migration from https://trac.sagemath.org/ticket/5536





---

archive/issue_comments_042963.json:
```json
{
    "body": "Attachment [permgp.patch](tarball://root/attachments/some-uuid/ticket5536/permgp.patch) by mvngu created at 2009-03-17 05:51:29\n\nREFEREE REPORT\n\n\n\nThe patch **permgp.patch** applies OK against Sage 3.4 and all doctests passed with the options\n\n```\n-t -long\n```\nThe reference manual builds fine. Looking at the HTML doc for `sage/groups/perm_gps/permgroup.py`, I see that the patch fixes the formatting issues that it meant to fix. So positive review. \n\n\n\nHowever, while reviewing the patch I noticed that there are more formatting issues in `sage/groups/perm_gps/permgroup.py`. But these are addressed in ticket #5542.",
    "created_at": "2009-03-17T05:51:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5536#issuecomment-42963",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [permgp.patch](tarball://root/attachments/some-uuid/ticket5536/permgp.patch) by mvngu created at 2009-03-17 05:51:29

REFEREE REPORT



The patch **permgp.patch** applies OK against Sage 3.4 and all doctests passed with the options

```
-t -long
```
The reference manual builds fine. Looking at the HTML doc for `sage/groups/perm_gps/permgroup.py`, I see that the patch fixes the formatting issues that it meant to fix. So positive review. 



However, while reviewing the patch I noticed that there are more formatting issues in `sage/groups/perm_gps/permgroup.py`. But these are addressed in ticket #5542.



---

archive/issue_events_012993.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-20T21:20:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5536",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5536#event-12993"
}
```



---

archive/issue_comments_042964.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-20T21:20:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5536#issuecomment-42964",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_comments_042965.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-20T21:20:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5536#issuecomment-42965",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
