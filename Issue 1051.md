# Issue 1051: pari/gp extended help stops working when sage tree is moved

archive/issues_001051.json:
```json
{
    "body": "Assignee: cwitty\n\nWith the new pari-2.3.2.p4.spkg, the ?? help works.  However, it stops working when the Sage tree is moved, because libpari hardcodes the path to the gphelp binary.\n\nThis path can be overridden with the GPHELP environment variable; sage-env should set that variable.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1051\n\n",
    "created_at": "2007-11-01T06:25:48Z",
    "labels": [
        "relocation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.11",
    "title": "pari/gp extended help stops working when sage tree is moved",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1051",
    "user": "cwitty"
}
```
Assignee: cwitty

With the new pari-2.3.2.p4.spkg, the ?? help works.  However, it stops working when the Sage tree is moved, because libpari hardcodes the path to the gphelp binary.

This path can be overridden with the GPHELP environment variable; sage-env should set that variable.

Issue created by migration from https://trac.sagemath.org/ticket/1051





---

archive/issue_comments_006397.json:
```json
{
    "body": "Attachment [1051.patch](tarball://root/attachments/some-uuid/ticket1051/1051.patch) by cwitty created at 2007-11-02 01:02:13",
    "created_at": "2007-11-02T01:02:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1051#issuecomment-6397",
    "user": "cwitty"
}
```

Attachment [1051.patch](tarball://root/attachments/some-uuid/ticket1051/1051.patch) by cwitty created at 2007-11-02 01:02:13



---

archive/issue_comments_006398.json:
```json
{
    "body": "The attached patch (to sage_scripts) fixes this problem.",
    "created_at": "2007-11-02T01:03:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1051#issuecomment-6398",
    "user": "cwitty"
}
```

The attached patch (to sage_scripts) fixes this problem.



---

archive/issue_comments_006399.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-02T02:00:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1051#issuecomment-6399",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006400.json:
```json
{
    "body": "applied to 2.8.11.rc1",
    "created_at": "2007-11-02T02:00:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1051#issuecomment-6400",
    "user": "mabshoff"
}
```

applied to 2.8.11.rc1
