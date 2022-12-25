# Issue 1580: notebook shows graphics out of order

archive/issues_001580.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\nfrom sage.plot.plot3d.all import Sphere\nSphere(1).show()\nplot(x^3,xmin=0,xmax=1).show()\n```\n\n\nshows the plot first and the sphere second on my computer (old 850 Mhz PIII running ubuntu 7.10).  This is confusing.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1580\n\n",
    "created_at": "2007-12-21T08:44:06Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.1",
    "title": "notebook shows graphics out of order",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1580",
    "user": "https://github.com/jasongrout"
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

archive/issue_comments_010042.json:
```json
{
    "body": "William says,\n\n```\nThis will likely happen for everybody.  It is likely caused by the 3d\ngraphics not\ncalling the right function to get the next default png filename.\nThanks for reporting it. \n```\n",
    "created_at": "2007-12-21T21:19:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1580#issuecomment-10042",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
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

archive/issue_comments_010043.json:
```json
{
    "body": "Attachment [trac-1580.patch](tarball://root/attachments/some-uuid/ticket1580/trac-1580.patch) by @rlmill created at 2007-12-22 21:00:42",
    "created_at": "2007-12-22T21:00:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1580#issuecomment-10043",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac-1580.patch](tarball://root/attachments/some-uuid/ticket1580/trac-1580.patch) by @rlmill created at 2007-12-22 21:00:42



---

archive/issue_comments_010044.json:
```json
{
    "body": "merged in 2.9.1 rc2",
    "created_at": "2007-12-23T03:20:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1580#issuecomment-10044",
    "user": "https://github.com/rlmill"
}
```

merged in 2.9.1 rc2



---

archive/issue_events_001736.json:
```json
{
    "actor": "@rlmill",
    "created_at": "2007-12-23T03:20:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1580",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1580#event-1736"
}
```



---

archive/issue_comments_010045.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-23T03:20:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1580",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1580#issuecomment-10045",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
