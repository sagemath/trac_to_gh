# Issue 5536: [with patch, review pending] trivial docstring patches for permgp.py

archive/issues_005536.json:
```json
{
    "body": "Assignee: jhpalmieri\n\nThe subject says it all.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5536\n\n",
    "created_at": "2009-03-16T22:50:39Z",
    "labels": [
        "group theory",
        "trivial",
        "bug"
    ],
    "title": "[with patch, review pending] trivial docstring patches for permgp.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5536",
    "user": "jhpalmieri"
}
```
Assignee: jhpalmieri

The subject says it all.


Issue created by migration from https://trac.sagemath.org/ticket/5536





---

archive/issue_comments_043047.json:
```json
{
    "body": "Attachment [permgp.patch](tarball://root/attachments/some-uuid/ticket5536/permgp.patch) by mvngu created at 2009-03-17 05:51:29\n\nREFEREE REPORT\n\n\n\nThe patch **permgp.patch** applies OK against Sage 3.4 and all doctests passed with the options\n\n```\n-t -long\n```\n\nThe reference manual builds fine. Looking at the HTML doc for `sage/groups/perm_gps/permgroup.py`, I see that the patch fixes the formatting issues that it meant to fix. So positive review. \n\n\n\nHowever, while reviewing the patch I noticed that there are more formatting issues in `sage/groups/perm_gps/permgroup.py`. But these are addressed in ticket #5542.",
    "created_at": "2009-03-17T05:51:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5536#issuecomment-43047",
    "user": "mvngu"
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

archive/issue_comments_043048.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-20T21:20:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5536#issuecomment-43048",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_comments_043049.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-20T21:20:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5536#issuecomment-43049",
    "user": "mabshoff"
}
```

Resolution: fixed
