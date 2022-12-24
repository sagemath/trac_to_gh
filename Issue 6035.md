# Issue 6035: [with patch, needs review] Don't draw vertical asympotes

archive/issues_006035.json:
```json
{
    "body": "Assignee: whuss\n\nThe attached patch adds an option \"detect_poles\" to the plot command,\nwhich if True detects vertical asymptotes of the plotted function.\n\n\n```\nsage: plot(gamma(x), (x, -3, 4), detect_poles = True).show(ymin = -5, ymax = 5)\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6035\n\n",
    "created_at": "2009-05-13T16:43:42Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "[with patch, needs review] Don't draw vertical asympotes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6035",
    "user": "whuss"
}
```
Assignee: whuss

The attached patch adds an option "detect_poles" to the plot command,
which if True detects vertical asymptotes of the plotted function.


```
sage: plot(gamma(x), (x, -3, 4), detect_poles = True).show(ymin = -5, ymax = 5)
```



Issue created by migration from https://trac.sagemath.org/ticket/6035





---

archive/issue_comments_048067.json:
```json
{
    "body": "Attachment [detect_poles.patch](tarball://root/attachments/some-uuid/ticket6035/detect_poles.patch) by mhampton created at 2009-05-20 05:11:54\n\nThis seems to work pretty well, and since its an optional argument I don't see it interfering with any existing code.  The added documentation looks good.",
    "created_at": "2009-05-20T05:11:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6035#issuecomment-48067",
    "user": "mhampton"
}
```

Attachment [detect_poles.patch](tarball://root/attachments/some-uuid/ticket6035/detect_poles.patch) by mhampton created at 2009-05-20 05:11:54

This seems to work pretty well, and since its an optional argument I don't see it interfering with any existing code.  The added documentation looks good.



---

archive/issue_comments_048068.json:
```json
{
    "body": "Merged in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-21T02:07:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6035#issuecomment-48068",
    "user": "mabshoff"
}
```

Merged in Sage 4.0.rc0.

Cheers,

Michael



---

archive/issue_comments_048069.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-21T02:07:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6035",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6035#issuecomment-48069",
    "user": "mabshoff"
}
```

Resolution: fixed
