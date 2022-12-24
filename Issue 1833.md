# Issue 1833: [with patch; needs review] plot3d and parametric_plot3d can be very slow on some inputs

archive/issues_001833.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: x,y = var('x,y')\nsage: plot3d(x*y, (x,-1,1), (y,-1,1))\n```\n\nis fast, but \n\n```\nsage: x,y = var('x,y')\nsage: plot3d(x*y, (-1,1), (-1,1))\n```\n\nis shockingly slow (and similar remarks for parametric plots).   The attached patch fixes this problem. \n\nThis also fixes trac #1737.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1833\n\n",
    "created_at": "2008-01-18T16:22:22Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with patch; needs review] plot3d and parametric_plot3d can be very slow on some inputs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1833",
    "user": "was"
}
```
Assignee: was


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

archive/issue_comments_011601.json:
```json
{
    "body": "Changing component from algebraic geometry to graphics.",
    "created_at": "2008-01-18T16:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1833#issuecomment-11601",
    "user": "was"
}
```

Changing component from algebraic geometry to graphics.



---

archive/issue_comments_011602.json:
```json
{
    "body": "This patch also moves plot3d_adaptive into plot3d (i.e., as an option), and deprecates globally exposing plot3d_adaptive.   This is natural to do in the context of this patch.",
    "created_at": "2008-01-18T16:23:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1833#issuecomment-11602",
    "user": "was"
}
```

This patch also moves plot3d_adaptive into plot3d (i.e., as an option), and deprecates globally exposing plot3d_adaptive.   This is natural to do in the context of this patch.



---

archive/issue_comments_011603.json:
```json
{
    "body": "Attachment [trac-1833.patch](tarball://root/attachments/some-uuid/ticket1833/trac-1833.patch) by was created at 2008-01-18 16:24:23",
    "created_at": "2008-01-18T16:24:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1833#issuecomment-11603",
    "user": "was"
}
```

Attachment [trac-1833.patch](tarball://root/attachments/some-uuid/ticket1833/trac-1833.patch) by was created at 2008-01-18 16:24:23



---

archive/issue_comments_011604.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-01-21T03:32:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1833#issuecomment-11604",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_011605.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha1",
    "created_at": "2008-01-21T04:13:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1833#issuecomment-11605",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha1



---

archive/issue_comments_011606.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-21T04:13:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1833",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1833#issuecomment-11606",
    "user": "mabshoff"
}
```

Resolution: fixed
