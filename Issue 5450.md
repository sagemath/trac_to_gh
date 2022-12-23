# Issue 5450: plotting a vector as a point plots a sphere, not a point

archive/issues_005450.json:
```json
{
    "body": "Assignee: was\n\nPresumably, plotting a point is more efficient.  However, \n\n\n```\nvector([1,2,3]).plot(plot_type='point')\n```\n\n\nplots a sphere instead of a point3d (or point2d, if 2-dimensional).  This should be changed to plot a point.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5450\n\n",
    "created_at": "2009-03-06T21:44:22Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "title": "plotting a vector as a point plots a sphere, not a point",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5450",
    "user": "jason"
}
```
Assignee: was

Presumably, plotting a point is more efficient.  However, 


```
vector([1,2,3]).plot(plot_type='point')
```


plots a sphere instead of a point3d (or point2d, if 2-dimensional).  This should be changed to plot a point.

Issue created by migration from https://trac.sagemath.org/ticket/5450





---

archive/issue_comments_042194.json:
```json
{
    "body": "Changing assignee from was to jason.",
    "created_at": "2009-03-06T21:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5450#issuecomment-42194",
    "user": "jason"
}
```

Changing assignee from was to jason.



---

archive/issue_comments_042195.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-06T21:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5450#issuecomment-42195",
    "user": "jason"
}
```

Changing status from new to assigned.



---

archive/issue_comments_042196.json:
```json
{
    "body": "Another performance enhancement would be using a line3d with arrow_head=True instead of an arrow3d command.  I think that would also preserve aspect ratio better anyway.",
    "created_at": "2009-03-06T21:55:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5450#issuecomment-42196",
    "user": "jason"
}
```

Another performance enhancement would be using a line3d with arrow_head=True instead of an arrow3d command.  I think that would also preserve aspect ratio better anyway.



---

archive/issue_comments_042197.json:
```json
{
    "body": "using the line3d command instead of the arrow3d command I think would be more in line with the result of vector([1,2]).plot().plot3d() (which I believe uses the line3d command).",
    "created_at": "2009-03-06T22:02:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5450#issuecomment-42197",
    "user": "jason"
}
```

using the line3d command instead of the arrow3d command I think would be more in line with the result of vector([1,2]).plot().plot3d() (which I believe uses the line3d command).



---

archive/issue_comments_042198.json:
```json
{
    "body": "Attachment\n\nThis should make plotting lots of 3d vector arrows or points significantly faster.",
    "created_at": "2009-04-03T21:25:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5450#issuecomment-42198",
    "user": "jason"
}
```

Attachment

This should make plotting lots of 3d vector arrows or points significantly faster.



---

archive/issue_comments_042199.json:
```json
{
    "body": "Looks good.",
    "created_at": "2009-04-16T06:22:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5450#issuecomment-42199",
    "user": "robertwb"
}
```

Looks good.



---

archive/issue_comments_042200.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T11:45:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5450#issuecomment-42200",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc3.

Cheers,

Michael



---

archive/issue_comments_042201.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-16T11:45:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5450",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5450#issuecomment-42201",
    "user": "mabshoff"
}
```

Resolution: fixed
