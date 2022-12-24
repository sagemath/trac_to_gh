# Issue 6038: add implicit_plot3d to the reference manual (and maybe an example in the tutorial)

archive/issues_006038.json:
```json
{
    "body": "Assignee: tba\n\nCC:  wcauchois\n\nPlease add the wonderful implicit_plot3d to the reference manual, and possibly even add an example to the tutorial.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6038\n\n",
    "created_at": "2009-05-14T15:26:53Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "add implicit_plot3d to the reference manual (and maybe an example in the tutorial)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6038",
    "user": "@williamstein"
}
```
Assignee: tba

CC:  wcauchois

Please add the wonderful implicit_plot3d to the reference manual, and possibly even add an example to the tutorial.

Issue created by migration from https://trac.sagemath.org/ticket/6038





---

archive/issue_comments_048083.json:
```json
{
    "body": "Attachment [trac6038.patch](tarball://root/attachments/some-uuid/ticket6038/trac6038.patch) by wcauchois created at 2009-05-25 05:37:25\n\n(This patch is based on Sage 4.0.rc0.)\n\nIn order to make the automatically generated reference documentation clearer, I moved the implicit_plot3d() function into a separate file called \"implicit_plot3d.py\". I see this has been done for some of the other plotting functions as well. I also took the liberty of adding a little bit to the meager section on \"Three-Dimensional Plots\" in the tour of Sage.",
    "created_at": "2009-05-25T05:37:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6038#issuecomment-48083",
    "user": "wcauchois"
}
```

Attachment [trac6038.patch](tarball://root/attachments/some-uuid/ticket6038/trac6038.patch) by wcauchois created at 2009-05-25 05:37:25

(This patch is based on Sage 4.0.rc0.)

In order to make the automatically generated reference documentation clearer, I moved the implicit_plot3d() function into a separate file called "implicit_plot3d.py". I see this has been done for some of the other plotting functions as well. I also took the liberty of adding a little bit to the meager section on "Three-Dimensional Plots" in the tour of Sage.



---

archive/issue_comments_048084.json:
```json
{
    "body": "Looks good to me.\n\nMerged in Sage 4.0.rc1.",
    "created_at": "2009-05-26T16:49:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6038#issuecomment-48084",
    "user": "@mwhansen"
}
```

Looks good to me.

Merged in Sage 4.0.rc1.



---

archive/issue_comments_048085.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-26T16:49:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6038",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6038#issuecomment-48085",
    "user": "@mwhansen"
}
```

Resolution: fixed
