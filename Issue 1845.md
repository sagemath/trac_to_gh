# Issue 1845: [with patch, spkg] list_plot3d should be able to accept lists of points in arbitrary positions

archive/issues_001845.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe following patch adds some improvements to list_plot3d\n\nhttp://sage.math.washington.edu/home/jkantor/spkgs/list_plot3d.hg\n\nThe new code requires an updated scipy_sandbox\n\nhttp://sage.math.washington.edu/spkgs/scipy_sandbox-20071020.p1.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/1845\n\n",
    "created_at": "2008-01-19T07:46:24Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with patch, spkg] list_plot3d should be able to accept lists of points in arbitrary positions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1845",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```
Assignee: @williamstein

The following patch adds some improvements to list_plot3d

http://sage.math.washington.edu/home/jkantor/spkgs/list_plot3d.hg

The new code requires an updated scipy_sandbox

http://sage.math.washington.edu/spkgs/scipy_sandbox-20071020.p1.spkg

Issue created by migration from https://trac.sagemath.org/ticket/1845





---

archive/issue_comments_011654.json:
```json
{
    "body": "Attachment [trac-1845-fix-doctest.patch](tarball://root/attachments/some-uuid/ticket1845/trac-1845-fix-doctest.patch) by cwitty created at 2008-01-27 04:52:02",
    "created_at": "2008-01-27T04:52:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1845#issuecomment-11654",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac-1845-fix-doctest.patch](tarball://root/attachments/some-uuid/ticket1845/trac-1845-fix-doctest.patch) by cwitty created at 2008-01-27 04:52:02



---

archive/issue_comments_011655.json:
```json
{
    "body": "Code looks good; doctests pass in sage/plot.  I went through all the doctests by hand and they all work and look pretty.  One of the doctests was malformed (syntax error); the attached trac-1845-fix-doctest.patch fixes that.\n\nI did not look at differences between the old and new scipy_sandbox, or check old functionality of that spkg.\n\nTo apply: apply list_plot3d.hg, then trac-1845-fix-doctest.patch; and install the new scipy_sandbox spkg.",
    "created_at": "2008-01-27T04:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1845#issuecomment-11655",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Code looks good; doctests pass in sage/plot.  I went through all the doctests by hand and they all work and look pretty.  One of the doctests was malformed (syntax error); the attached trac-1845-fix-doctest.patch fixes that.

I did not look at differences between the old and new scipy_sandbox, or check old functionality of that spkg.

To apply: apply list_plot3d.hg, then trac-1845-fix-doctest.patch; and install the new scipy_sandbox spkg.



---

archive/issue_comments_011656.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc1: the bundle and updated scipy_sandbox as well as cwitty's doctest fix patch.",
    "created_at": "2008-01-27T07:18:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1845#issuecomment-11656",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.rc1: the bundle and updated scipy_sandbox as well as cwitty's doctest fix patch.



---

archive/issue_comments_011657.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-27T07:18:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1845#issuecomment-11657",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
