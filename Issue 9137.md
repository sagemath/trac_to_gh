# Issue 9137: Infinite konqueror windows when opening notebook

archive/issues_009137.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @jasongrout @mwhansen @williamstein\n\nKeywords: konqueror, infinite, windows\n\nThis is to make sage users aware of a bug that apparently exists in KDE and not in SAGE.\n\n**Behavior:**  On certain system setups, when starting SAGE notebook, konqueror goes haywire and starts opening up an infinite number of windows in the taskbar (none of the windows will show themselves).  Konqueror will continue to open new windows until Xorg is killed.\n\n**References:** [https://bugs.kde.org/show_bug.cgi?id=234620](https://bugs.kde.org/show_bug.cgi?id=234620) (includes screenshots of the problem)\n\n**Workaround:** 1) use ` notebook(open_viewer=False) ` and manually open browser to notebook port  2) Use a browser other than konqueror (you can change the defualt browser in KDE system settings).\n\n**Conclusion:** As stated above, this appears to be a bug in KDE as it affects other software as well.  If you see this bug, please contact the KDE developers.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9137\n\n",
    "created_at": "2010-06-03T23:45:26Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Infinite konqueror windows when opening notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9137",
    "user": "ryan"
}
```
Assignee: somebody

CC:  @jasongrout @mwhansen @williamstein

Keywords: konqueror, infinite, windows

This is to make sage users aware of a bug that apparently exists in KDE and not in SAGE.

**Behavior:**  On certain system setups, when starting SAGE notebook, konqueror goes haywire and starts opening up an infinite number of windows in the taskbar (none of the windows will show themselves).  Konqueror will continue to open new windows until Xorg is killed.

**References:** [https://bugs.kde.org/show_bug.cgi?id=234620](https://bugs.kde.org/show_bug.cgi?id=234620) (includes screenshots of the problem)

**Workaround:** 1) use ` notebook(open_viewer=False) ` and manually open browser to notebook port  2) Use a browser other than konqueror (you can change the defualt browser in KDE system settings).

**Conclusion:** As stated above, this appears to be a bug in KDE as it affects other software as well.  If you see this bug, please contact the KDE developers.

Issue created by migration from https://trac.sagemath.org/ticket/9137





---

archive/issue_comments_085164.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-06-03T23:46:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9137#issuecomment-85164",
    "user": "ryan"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_085165.json:
```json
{
    "body": "this bug is closed in KDE 4.5",
    "created_at": "2010-08-28T18:24:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9137#issuecomment-85165",
    "user": "ryan"
}
```

this bug is closed in KDE 4.5



---

archive/issue_comments_085166.json:
```json
{
    "body": "[https://bugs.kde.org/show_bug.cgi?id=240677](https://bugs.kde.org/show_bug.cgi?id=240677)\n\nHere is the KDE bug ticket.",
    "created_at": "2010-08-28T18:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9137#issuecomment-85166",
    "user": "ryan"
}
```

[https://bugs.kde.org/show_bug.cgi?id=240677](https://bugs.kde.org/show_bug.cgi?id=240677)

Here is the KDE bug ticket.



---

archive/issue_comments_085167.json:
```json
{
    "body": "I'm not sure who the current release manager is, but this ticket should be closed (see comments above).",
    "created_at": "2010-08-28T19:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9137#issuecomment-85167",
    "user": "@jasongrout"
}
```

I'm not sure who the current release manager is, but this ticket should be closed (see comments above).



---

archive/issue_comments_085168.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-08-28T19:24:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9137",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9137#issuecomment-85168",
    "user": "@mwhansen"
}
```

Resolution: invalid
