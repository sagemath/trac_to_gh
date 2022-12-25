# Issue 5450: plotting a vector as a point plots a sphere, not a point

archive/issues_005450.json:
```json
{
    "body": "Assignee: @williamstein\n\nPresumably, plotting a point is more efficient.  However, \n\n\n```\nvector([1,2,3]).plot(plot_type='point')\n```\n\n\nplots a sphere instead of a point3d (or point2d, if 2-dimensional).  This should be changed to plot a point.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5450\n\n",
    "created_at": "2009-03-06T21:44:22Z",
    "labels": [
        "component: graphics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "plotting a vector as a point plots a sphere, not a point",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5450",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

Presumably, plotting a point is more efficient.  However, 


```
vector([1,2,3]).plot(plot_type='point')
```


plots a sphere instead of a point3d (or point2d, if 2-dimensional).  This should be changed to plot a point.

Issue created by migration from https://trac.sagemath.org/ticket/5450





---

archive/issue_comments_042112.json:
```json
{
    "body": "Changing assignee from @williamstein to @jasongrout.",
    "created_at": "2009-03-06T21:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5450#issuecomment-42112",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @williamstein to @jasongrout.



---

archive/issue_comments_042113.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-06T21:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5450#issuecomment-42113",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to assigned.



---

archive/issue_comments_042114.json:
```json
{
    "body": "Another performance enhancement would be using a line3d with arrow_head=True instead of an arrow3d command.  I think that would also preserve aspect ratio better anyway.",
    "created_at": "2009-03-06T21:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5450#issuecomment-42114",
    "user": "https://github.com/jasongrout"
}
```

Another performance enhancement would be using a line3d with arrow_head=True instead of an arrow3d command.  I think that would also preserve aspect ratio better anyway.



---

archive/issue_comments_042115.json:
```json
{
    "body": "using the line3d command instead of the arrow3d command I think would be more in line with the result of vector([1,2]).plot().plot3d() (which I believe uses the line3d command).",
    "created_at": "2009-03-06T22:02:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5450#issuecomment-42115",
    "user": "https://github.com/jasongrout"
}
```

using the line3d command instead of the arrow3d command I think would be more in line with the result of vector([1,2]).plot().plot3d() (which I believe uses the line3d command).



---

archive/issue_comments_042116.json:
```json
{
    "body": "Attachment [trac-5450-vector_plot_fast3d.patch](tarball://root/attachments/some-uuid/ticket5450/trac-5450-vector_plot_fast3d.patch) by @jasongrout created at 2009-04-03 21:25:51\n\nThis should make plotting lots of 3d vector arrows or points significantly faster.",
    "created_at": "2009-04-03T21:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5450#issuecomment-42116",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-5450-vector_plot_fast3d.patch](tarball://root/attachments/some-uuid/ticket5450/trac-5450-vector_plot_fast3d.patch) by @jasongrout created at 2009-04-03 21:25:51

This should make plotting lots of 3d vector arrows or points significantly faster.



---

archive/issue_comments_042117.json:
```json
{
    "body": "Looks good.",
    "created_at": "2009-04-16T06:22:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5450#issuecomment-42117",
    "user": "https://github.com/robertwb"
}
```

Looks good.



---

archive/issue_comments_042118.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T11:45:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5450#issuecomment-42118",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc3.

Cheers,

Michael



---

archive/issue_comments_042119.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-16T11:45:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5450#issuecomment-42119",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
