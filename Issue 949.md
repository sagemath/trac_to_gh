# Issue 949: "sage -f" fails to install packages when given an absolute path

archive/issues_000949.json:
```json
{
    "body": "Assignee: @williamstein\n\nWhen you run this command:\n\n```\ncwitty@magnetar:~/my-sage$ ~/sage/sage -f ~/spkg/mercurial-0.9.5.spkg \n```\n\n\nthe output includes this line:\n\n```\n/home/cwitty/sage/local/bin/sage-spkg: file /home/cwitty/my-sage//home/cwitty/spkg/mercurial-0.9.5.spkg does not exist\n```\n\n\nshowing that \"sage -f\" does some sort of \"convert relative filename to absolute\", but does the operation even if the path is already absolute.\n\nIssue created by migration from https://trac.sagemath.org/ticket/949\n\n",
    "created_at": "2007-10-20T19:52:36Z",
    "labels": [
        "component: user interface",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "\"sage -f\" fails to install packages when given an absolute path",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/949",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @williamstein

When you run this command:

```
cwitty@magnetar:~/my-sage$ ~/sage/sage -f ~/spkg/mercurial-0.9.5.spkg 
```


the output includes this line:

```
/home/cwitty/sage/local/bin/sage-spkg: file /home/cwitty/my-sage//home/cwitty/spkg/mercurial-0.9.5.spkg does not exist
```


showing that "sage -f" does some sort of "convert relative filename to absolute", but does the operation even if the path is already absolute.

Issue created by migration from https://trac.sagemath.org/ticket/949





---

archive/issue_comments_005775.json:
```json
{
    "body": "Attachment [486.patch](tarball://root/attachments/some-uuid/ticket949/486.patch) by cwitty created at 2007-10-20 21:41:20",
    "created_at": "2007-10-20T21:41:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/949#issuecomment-5775",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [486.patch](tarball://root/attachments/some-uuid/ticket949/486.patch) by cwitty created at 2007-10-20 21:41:20



---

archive/issue_comments_005776.json:
```json
{
    "body": "Simple patch: just don't prefix the filename with the current directory if it already starts with a slash.",
    "created_at": "2007-10-20T21:45:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/949#issuecomment-5776",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Simple patch: just don't prefix the filename with the current directory if it already starts with a slash.



---

archive/issue_comments_005777.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-20T22:30:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/949#issuecomment-5777",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
