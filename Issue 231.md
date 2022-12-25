# Issue 231: inconsistent working directory

archive/issues_000231.json:
```json
{
    "body": "Assignee: boothby\n\nBetween executing a cell for the first time and then reexecuting that cell, the \"current directory\" changes:\n\n```\n%sh\npwd\n```\n\nthe first time gives the \"home directory\"\n\n```\n/usr/local/sage/nobody\n```\n\nupon reexecution I get\n\n```\n/usr/local/sage/nobody/sage_notebook/worksheets/loaderror/cells/2\n```\n\ni.e., the cell directory.\n\nIssue created by migration from https://trac.sagemath.org/ticket/231\n\n",
    "created_at": "2007-01-29T19:26:02Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.3",
    "title": "inconsistent working directory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/231",
    "user": "https://github.com/nbruin"
}
```
Assignee: boothby

Between executing a cell for the first time and then reexecuting that cell, the "current directory" changes:

```
%sh
pwd
```

the first time gives the "home directory"

```
/usr/local/sage/nobody
```

upon reexecution I get

```
/usr/local/sage/nobody/sage_notebook/worksheets/loaderror/cells/2
```

i.e., the cell directory.

Issue created by migration from https://trac.sagemath.org/ticket/231





---

archive/issue_comments_001022.json:
```json
{
    "body": "this fixes the bug (and more)",
    "created_at": "2007-08-29T02:37:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/231#issuecomment-1022",
    "user": "https://github.com/williamstein"
}
```

this fixes the bug (and more)



---

archive/issue_comments_001023.json:
```json
{
    "body": "Attachment [5958.patch](tarball://root/attachments/some-uuid/ticket231/5958.patch) by @williamstein created at 2007-08-29 02:37:55",
    "created_at": "2007-08-29T02:37:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/231#issuecomment-1023",
    "user": "https://github.com/williamstein"
}
```

Attachment [5958.patch](tarball://root/attachments/some-uuid/ticket231/5958.patch) by @williamstein created at 2007-08-29 02:37:55



---

archive/issue_comments_001024.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-29T02:37:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/231#issuecomment-1024",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
