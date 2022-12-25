# Issue 1833: [with patch; needs review] plot3d and parametric_plot3d can be very slow on some inputs

archive/issues_001833.json:
```json
{
    "body": "Assignee: @williamstein\n\n```\nsage: x,y = var('x,y')\nsage: plot3d(x*y, (x,-1,1), (y,-1,1))\n```\nis fast, but \n\n```\nsage: x,y = var('x,y')\nsage: plot3d(x*y, (-1,1), (-1,1))\n```\nis shockingly slow (and similar remarks for parametric plots).   The attached patch fixes this problem. \n\nThis also fixes trac #1737.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1833\n\n",
    "created_at": "2008-01-18T16:22:22Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with patch; needs review] plot3d and parametric_plot3d can be very slow on some inputs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1833",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

```
sage: x,y = var('x,y')
sage: plot3d(x*y, (x,-1,1), (y,-1,1))
```
is fast, but 

```
sage: x,y = var('x,y')
sage: plot3d(x*y, (-1,1), (-1,1))
```
is shockingly slow (and similar remarks for parametric plots).   The attached patch fixes this problem. 

This also fixes trac #1737.

Issue created by migration from https://trac.sagemath.org/ticket/1833





---

archive/issue_comments_011572.json:
```json
{
    "body": "Changing component from algebraic geometry to graphics.",
    "created_at": "2008-01-18T16:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1833#issuecomment-11572",
    "user": "https://github.com/williamstein"
}
```

Changing component from algebraic geometry to graphics.



---

archive/issue_comments_011573.json:
```json
{
    "body": "This patch also moves plot3d_adaptive into plot3d (i.e., as an option), and deprecates globally exposing plot3d_adaptive.   This is natural to do in the context of this patch.",
    "created_at": "2008-01-18T16:23:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1833#issuecomment-11573",
    "user": "https://github.com/williamstein"
}
```

This patch also moves plot3d_adaptive into plot3d (i.e., as an option), and deprecates globally exposing plot3d_adaptive.   This is natural to do in the context of this patch.



---

archive/issue_comments_011574.json:
```json
{
    "body": "Attachment [trac-1833.patch](tarball://root/attachments/some-uuid/ticket1833/trac-1833.patch) by @williamstein created at 2008-01-18 16:24:23",
    "created_at": "2008-01-18T16:24:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1833#issuecomment-11574",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-1833.patch](tarball://root/attachments/some-uuid/ticket1833/trac-1833.patch) by @williamstein created at 2008-01-18 16:24:23



---

archive/issue_comments_011575.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-01-21T03:32:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1833#issuecomment-11575",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_011576.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha1",
    "created_at": "2008-01-21T04:13:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1833#issuecomment-11576",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha1



---

archive/issue_comments_011577.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-21T04:13:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1833#issuecomment-11577",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004451.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-21T04:13:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1833",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1833#event-4451"
}
```
