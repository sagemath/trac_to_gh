# Issue 3478: clisp picks up wrong dvipdf

archive/issues_003478.json:
```json
{
    "body": "Assignee: mabshoff\n\non my OSX 10.4.11 intel,\n\nthe clisp build was picking up dvipdf from the wrong place (fink or darwinports or something) and failed while trying to build its docs.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3478\n\n",
    "created_at": "2008-06-19T22:26:24Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "clisp picks up wrong dvipdf",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3478",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: mabshoff

on my OSX 10.4.11 intel,

the clisp build was picking up dvipdf from the wrong place (fink or darwinports or something) and failed while trying to build its docs.


Issue created by migration from https://trac.sagemath.org/ticket/3478





---

archive/issue_comments_024463.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-16T01:53:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3478#issuecomment-24463",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_024464.json:
```json
{
    "body": "This is no longer an issue since Sage with MacPorts or Fink in $PATH will refuse to build. Also note that the libpng update at #5217 will fix the problem in a different way.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-16T01:53:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3478",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3478#issuecomment-24464",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is no longer an issue since Sage with MacPorts or Fink in $PATH will refuse to build. Also note that the libpng update at #5217 will fix the problem in a different way.

Cheers,

Michael
