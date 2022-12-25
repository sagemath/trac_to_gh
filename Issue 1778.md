# Issue 1778: plot() does not follow the same interval range conventions as plot3d()

archive/issues_001778.json:
```json
{
    "body": "Assignee: @bobmoretti\n\nKeywords: plotting, plot3d, plot\n\nsage: plot3d(x^2 + y^2, (x,-2,2), (y,-2,2))\n\nis valid, however, to do a 2d plot, you use the syntax\n\nsage: plot(x^2, x, -2, 2).\n\nI spoke with William about this, he wants to deprecate the plot(x^2, -2, 2) syntax for 2d plotting and introduce a new preferred syntax:\n\nsage: plot(x^2, (x, -2, 2))\n\nIssue created by migration from https://trac.sagemath.org/ticket/1778\n\n",
    "created_at": "2008-01-14T22:58:12Z",
    "labels": [
        "component: graphics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "plot() does not follow the same interval range conventions as plot3d()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1778",
    "user": "https://github.com/bobmoretti"
}
```
Assignee: @bobmoretti

Keywords: plotting, plot3d, plot

sage: plot3d(x^2 + y^2, (x,-2,2), (y,-2,2))

is valid, however, to do a 2d plot, you use the syntax

sage: plot(x^2, x, -2, 2).

I spoke with William about this, he wants to deprecate the plot(x^2, -2, 2) syntax for 2d plotting and introduce a new preferred syntax:

sage: plot(x^2, (x, -2, 2))

Issue created by migration from https://trac.sagemath.org/ticket/1778





---

archive/issue_comments_011227.json:
```json
{
    "body": "Attachment [plot.patch](tarball://root/attachments/some-uuid/ticket1778/plot.patch) by @bobmoretti created at 2008-01-15 00:24:10\n\nIgnore the previous patch, it does not have all the required changes.",
    "created_at": "2008-01-15T00:24:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1778#issuecomment-11227",
    "user": "https://github.com/bobmoretti"
}
```

Attachment [plot.patch](tarball://root/attachments/some-uuid/ticket1778/plot.patch) by @bobmoretti created at 2008-01-15 00:24:10

Ignore the previous patch, it does not have all the required changes.



---

archive/issue_comments_011228.json:
```json
{
    "body": "Attachment [plot.hg](tarball://root/attachments/some-uuid/ticket1778/plot.hg) by @bobmoretti created at 2008-01-15 00:24:36",
    "created_at": "2008-01-15T00:24:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1778#issuecomment-11228",
    "user": "https://github.com/bobmoretti"
}
```

Attachment [plot.hg](tarball://root/attachments/some-uuid/ticket1778/plot.hg) by @bobmoretti created at 2008-01-15 00:24:36



---

archive/issue_comments_011229.json:
```json
{
    "body": "I implemented this in the attached. It makes both the old and new style of plot() syntax valid. However the documentation mentions that plot(x^2, (x, a, b)) is the preferred syntax. Please test it out.",
    "created_at": "2008-01-15T00:34:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1778#issuecomment-11229",
    "user": "https://github.com/bobmoretti"
}
```

I implemented this in the attached. It makes both the old and new style of plot() syntax valid. However the documentation mentions that plot(x^2, (x, a, b)) is the preferred syntax. Please test it out.



---

archive/issue_comments_011230.json:
```json
{
    "body": "That this doesn't work anymore is definitely a bug:\n\n```\nsage: plot(sin(2), (x,0,10*pi))\nBOOM!\n```\n\n\nLikewise for \n\n```\nsage: plot(sin(2), 0,10*pi)\nBOOM\n```\n\n\nI'll try to fix this....",
    "created_at": "2008-01-15T05:52:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1778#issuecomment-11230",
    "user": "https://github.com/williamstein"
}
```

That this doesn't work anymore is definitely a bug:

```
sage: plot(sin(2), (x,0,10*pi))
BOOM!
```


Likewise for 

```
sage: plot(sin(2), 0,10*pi)
BOOM
```


I'll try to fix this....



---

archive/issue_comments_011231.json:
```json
{
    "body": "It turns out the `plot(sin(2), (x,0,10*pi))` problem above was a really genuine bug coming from an indentation mistake on line 624 (I will attach a patch fixing this and other issues).",
    "created_at": "2008-01-15T05:55:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1778#issuecomment-11231",
    "user": "https://github.com/williamstein"
}
```

It turns out the `plot(sin(2), (x,0,10*pi))` problem above was a really genuine bug coming from an indentation mistake on line 624 (I will attach a patch fixing this and other issues).



---

archive/issue_comments_011232.json:
```json
{
    "body": "Attachment [trac-1778-referee.patch](tarball://root/attachments/some-uuid/ticket1778/trac-1778-referee.patch) by @williamstein created at 2008-01-15 06:20:29\n\napply the hg bundle that bobby posted, then apply this plain text patch which fixes one serious bug.",
    "created_at": "2008-01-15T06:20:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1778#issuecomment-11232",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-1778-referee.patch](tarball://root/attachments/some-uuid/ticket1778/trac-1778-referee.patch) by @williamstein created at 2008-01-15 06:20:29

apply the hg bundle that bobby posted, then apply this plain text patch which fixes one serious bug.



---

archive/issue_comments_011233.json:
```json
{
    "body": "Apply the plot.hg followed by trac-1778-referee.patch",
    "created_at": "2008-01-15T06:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1778#issuecomment-11233",
    "user": "https://github.com/williamstein"
}
```

Apply the plot.hg followed by trac-1778-referee.patch



---

archive/issue_comments_011234.json:
```json
{
    "body": "I had to resolve some slight merge conflict with #1779 in `setup.py`.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-15T07:12:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1778#issuecomment-11234",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I had to resolve some slight merge conflict with #1779 in `setup.py`.

Cheers,

Michael



---

archive/issue_comments_011235.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-15T07:12:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1778#issuecomment-11235",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_001935.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-15T07:12:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1778",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1778#event-1935"
}
```



---

archive/issue_comments_011236.json:
```json
{
    "body": "Merged in Sage 2.10.alpha3",
    "created_at": "2008-01-15T07:12:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1778#issuecomment-11236",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.alpha3
