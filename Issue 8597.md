# Issue 8597: point(vector((2,3,4))) is broken

archive/issues_008597.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @kcrisman\n\nThe following works :\n\n\n```\nsage: point((2,3))\n\nsage: point((2,3,4))\n\nsage: point(vector((2,3)))\n```\n\n\nbut the following doesn't :\n\n\n```\nsage: point(vector((2,3,4)))\nTraceback (most recent call last):\n\n/Users/slabbe/<ipython console> in <module>()\n\n/Users/slabbe/Applications/sage-4.3.4/local/lib/python2.6/site-packages/sage/plot/point.pyc in point(points, **kwds)\n    300     except (ValueError, TypeError):\n    301         from sage.plot.plot3d.shapes2 import point3d\n--> 302         return point3d(points, **kwds)\n    303 \n    304 @rename_keyword(color='rgbcolor')\n\n/Users/slabbe/Applications/sage-4.3.4/local/lib/python2.6/site-packages/sage/plot/plot3d/shapes2.pyc in point3d(v, size, **kwds)\n    712         return Point(v, size, **kwds)\n    713     else:\n--> 714         A = sum([Point(z, size, **kwds) for z in v])\n    715         A._set_extra_kwds(kwds)\n    716         return A\n\n/Users/slabbe/Applications/sage-4.3.4/local/lib/python2.6/site-packages/sage/plot/plot3d/shapes2.pyc in __init__(self, center, size, **kwds)\n    478     def __init__(self, center, size=1, **kwds):\n    479         PrimitiveObject.__init__(self, **kwds)\n--> 480         self.loc = (float(center[0]), float(center[1]), float(center[2]))\n    481         self.size = size\n    482         self._set_extra_kwds(kwds)\n\nTypeError: 'sage.rings.integer.Integer' object does not support indexing\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8597\n\n",
    "created_at": "2010-03-24T15:14:00Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "point(vector((2,3,4))) is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8597",
    "user": "@seblabbe"
}
```
Assignee: @williamstein

CC:  @kcrisman

The following works :


```
sage: point((2,3))

sage: point((2,3,4))

sage: point(vector((2,3)))
```


but the following doesn't :


```
sage: point(vector((2,3,4)))
Traceback (most recent call last):

/Users/slabbe/<ipython console> in <module>()

/Users/slabbe/Applications/sage-4.3.4/local/lib/python2.6/site-packages/sage/plot/point.pyc in point(points, **kwds)
    300     except (ValueError, TypeError):
    301         from sage.plot.plot3d.shapes2 import point3d
--> 302         return point3d(points, **kwds)
    303 
    304 @rename_keyword(color='rgbcolor')

/Users/slabbe/Applications/sage-4.3.4/local/lib/python2.6/site-packages/sage/plot/plot3d/shapes2.pyc in point3d(v, size, **kwds)
    712         return Point(v, size, **kwds)
    713     else:
--> 714         A = sum([Point(z, size, **kwds) for z in v])
    715         A._set_extra_kwds(kwds)
    716         return A

/Users/slabbe/Applications/sage-4.3.4/local/lib/python2.6/site-packages/sage/plot/plot3d/shapes2.pyc in __init__(self, center, size, **kwds)
    478     def __init__(self, center, size=1, **kwds):
    479         PrimitiveObject.__init__(self, **kwds)
--> 480         self.loc = (float(center[0]), float(center[1]), float(center[2]))
    481         self.size = size
    482         self._set_extra_kwds(kwds)

TypeError: 'sage.rings.integer.Integer' object does not support indexing
```



Issue created by migration from https://trac.sagemath.org/ticket/8597





---

archive/issue_comments_077833.json:
```json
{
    "body": "Changing keywords from \"\" to \"beginner\".",
    "created_at": "2010-05-26T15:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8597#issuecomment-77833",
    "user": "@jasongrout"
}
```

Changing keywords from "" to "beginner".



---

archive/issue_comments_077834.json:
```json
{
    "body": "The problem happens in sage.plot.plot3d.shapes2\n\nit should be calling `return Point(v, size, **kwds)`, but instead executes `A = sum([Point(z, size, **kwds) for z in v])`  \n\nI think there is something wrong with the if condition.",
    "created_at": "2011-01-09T05:18:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8597#issuecomment-77834",
    "user": "ryan"
}
```

The problem happens in sage.plot.plot3d.shapes2

it should be calling `return Point(v, size, **kwds)`, but instead executes `A = sum([Point(z, size, **kwds) for z in v])`  

I think there is something wrong with the if condition.



---

archive/issue_comments_077835.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-09T05:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8597#issuecomment-77835",
    "user": "ryan"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077836.json:
```json
{
    "body": "`point(vector((2,3,4)))` should work now",
    "created_at": "2011-01-09T05:38:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8597#issuecomment-77836",
    "user": "ryan"
}
```

`point(vector((2,3,4)))` should work now



---

archive/issue_comments_077837.json:
```json
{
    "body": "Attachment [trac_8597_point_vector.patch](tarball://root/attachments/some-uuid/ticket8597/trac_8597_point_vector.patch) by ryan created at 2011-01-09 06:18:04\n\nfixes point for 3d vectors",
    "created_at": "2011-01-09T06:18:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8597#issuecomment-77837",
    "user": "ryan"
}
```

Attachment [trac_8597_point_vector.patch](tarball://root/attachments/some-uuid/ticket8597/trac_8597_point_vector.patch) by ryan created at 2011-01-09 06:18:04

fixes point for 3d vectors



---

archive/issue_comments_077838.json:
```json
{
    "body": "latest patch includes small improvement that was suggested to me.",
    "created_at": "2011-01-09T06:19:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8597#issuecomment-77838",
    "user": "ryan"
}
```

latest patch includes small improvement that was suggested to me.



---

archive/issue_comments_077839.json:
```json
{
    "body": "Looks good, but it needs a doctest.  I've added one in the following patch.",
    "created_at": "2011-01-09T23:39:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8597#issuecomment-77839",
    "user": "@adeines"
}
```

Looks good, but it needs a doctest.  I've added one in the following patch.



---

archive/issue_comments_077840.json:
```json
{
    "body": "adds a doctest",
    "created_at": "2011-01-09T23:40:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8597#issuecomment-77840",
    "user": "@adeines"
}
```

adds a doctest



---

archive/issue_comments_077841.json:
```json
{
    "body": "Attachment [trac_8597_point_vector.2.patch](tarball://root/attachments/some-uuid/ticket8597/trac_8597_point_vector.2.patch) by jthurber created at 2011-01-10 11:25:11\n\nThe second patch does not apply on top of the first.\n\nOnly the second patch with doctest should be applied.  Otherwise, it's all good.",
    "created_at": "2011-01-10T11:25:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8597#issuecomment-77841",
    "user": "jthurber"
}
```

Attachment [trac_8597_point_vector.2.patch](tarball://root/attachments/some-uuid/ticket8597/trac_8597_point_vector.2.patch) by jthurber created at 2011-01-10 11:25:11

The second patch does not apply on top of the first.

Only the second patch with doctest should be applied.  Otherwise, it's all good.



---

archive/issue_comments_077842.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-10T11:25:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8597#issuecomment-77842",
    "user": "jthurber"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077843.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-19T22:19:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8597#issuecomment-77843",
    "user": "@jdemeyer"
}
```

Resolution: fixed
