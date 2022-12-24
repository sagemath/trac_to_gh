# Issue 1580: notebook shows graphics out of order

archive/issues_001580.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\nfrom sage.plot.plot3d.all import Sphere\nSphere(1).show()\nplot(x^3,xmin=0,xmax=1).show()\n```\n\n\nshows the plot first and the sphere second on my computer (old 850 Mhz PIII running ubuntu 7.10).  This is confusing.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1580\n\n",
    "created_at": "2007-12-21T08:44:06Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.1",
    "title": "notebook shows graphics out of order",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1580",
    "user": "@jasongrout"
}
```
Assignee: boothby


```
from sage.plot.plot3d.all import Sphere
Sphere(1).show()
plot(x^3,xmin=0,xmax=1).show()
```


shows the plot first and the sphere second on my computer (old 850 Mhz PIII running ubuntu 7.10).  This is confusing.


Issue created by migration from https://trac.sagemath.org/ticket/1580





---

archive/issue_comments_010069.json:
```json
{
    "body": "William says,\n\n```\nThis will likely happen for everybody.  It is likely caused by the 3d\ngraphics not\ncalling the right function to get the next default png filename.\nThanks for reporting it. \n```\n",
    "created_at": "2007-12-21T21:19:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1580#issuecomment-10069",
    "user": "cwitty"
}
```

William says,

```
This will likely happen for everybody.  It is likely caused by the 3d
graphics not
calling the right function to get the next default png filename.
Thanks for reporting it. 
```




---

archive/issue_comments_010070.json:
```json
{
    "body": "Attachment [trac-1580.patch](tarball://root/attachments/some-uuid/ticket1580/trac-1580.patch) by @rlmill created at 2007-12-22 21:00:42",
    "created_at": "2007-12-22T21:00:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1580#issuecomment-10070",
    "user": "@rlmill"
}
```

Attachment [trac-1580.patch](tarball://root/attachments/some-uuid/ticket1580/trac-1580.patch) by @rlmill created at 2007-12-22 21:00:42



---

archive/issue_comments_010071.json:
```json
{
    "body": "merged in 2.9.1 rc2",
    "created_at": "2007-12-23T03:20:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1580#issuecomment-10071",
    "user": "@rlmill"
}
```

merged in 2.9.1 rc2



---

archive/issue_comments_010072.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-23T03:20:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1580#issuecomment-10072",
    "user": "@rlmill"
}
```

Resolution: fixed
