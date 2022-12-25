# Issue 709: Add doctests to ensure that  scipy and cvxopt build correctly on all platforms.

archive/issues_000709.json:
```json
{
    "body": "Assignee: jkantor\n\nScipy and cvxopt tend to appear to build correctly, but then raise exceptions when modules are imported (usually missing symbols). We need doctests so that this is detected when tests are run.\n\nIssue created by migration from https://trac.sagemath.org/ticket/709\n\n",
    "created_at": "2007-09-20T17:41:37Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "Add doctests to ensure that  scipy and cvxopt build correctly on all platforms.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/709",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```
Assignee: jkantor

Scipy and cvxopt tend to appear to build correctly, but then raise exceptions when modules are imported (usually missing symbols). We need doctests so that this is detected when tests are run.

Issue created by migration from https://trac.sagemath.org/ticket/709





---

archive/issue_comments_003710.json:
```json
{
    "body": "Attachment [709_bugfix.hg](tarball://root/attachments/some-uuid/ticket709/709_bugfix.hg) by jkantor created at 2007-09-20 18:18:47\n\nThe above patch adds a file that is doctested and tests importing modules from cvxopt and scipy that are known to have problems. This together with the fix for bug 700 should fix the cvxopt problem as well as detect future breakage which is good since cvxopt silently broke when we switched from gfortran to g95.",
    "created_at": "2007-09-20T18:18:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/709#issuecomment-3710",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

Attachment [709_bugfix.hg](tarball://root/attachments/some-uuid/ticket709/709_bugfix.hg) by jkantor created at 2007-09-20 18:18:47

The above patch adds a file that is doctested and tests importing modules from cvxopt and scipy that are known to have problems. This together with the fix for bug 700 should fix the cvxopt problem as well as detect future breakage which is good since cvxopt silently broke when we switched from gfortran to g95.



---

archive/issue_comments_003711.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-21T02:12:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/709#issuecomment-3711",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_003712.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-09-21T02:23:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/709#issuecomment-3712",
    "user": "https://github.com/williamstein"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_003713.json:
```json
{
    "body": "I've included this but put a nodoctest in the file until trac #700 is resolved.",
    "created_at": "2007-09-21T02:23:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/709#issuecomment-3713",
    "user": "https://github.com/williamstein"
}
```

I've included this but put a nodoctest in the file until trac #700 is resolved.



---

archive/issue_comments_003714.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-09-21T02:23:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/709#issuecomment-3714",
    "user": "https://github.com/williamstein"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_003715.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-20T19:57:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/709",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/709#issuecomment-3715",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
