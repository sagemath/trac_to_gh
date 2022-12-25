# Issue 6367: polygon2d -- several issues: typo in docs, shouldn't have been renamed

archive/issues_006367.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  ksmith\n\nThe help for polygon2d? says:\n\n\n```\n Type ``polygon.options`` for a dictionary of the default \n    options for polygons.  You can change this to change \n```\n\nbut it should say\n\n```\n Type ``polygon2d.options`` for a dictionary of the default \n    options for polygons.  You can change this to change \n```\n\n\nAnd for the record I think it is unfortunate that somebody changed the function name from polygon to polygon2d, since that it inconsistent with almost all the rest of plotting in Sage, where the 2d version of the function doesn't specifically say it is 2d (e.g., plot, line, text, etc.) Well, there is line2d, to add to the confusion.    The design of Sage graphics is *supposed* to follow the naming scheme in Matheamtica.  In Mathematica there is Polygon and Polygon3D.  That's what Sage should have.\n\nTo resolve this patch, either fix the docstring or change the name back to polygon (not polygon2d).  I prefer the latter for consistency with the rest fo the design of sage 2d graphics. \n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6367\n\n",
    "created_at": "2009-06-20T15:25:14Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.4.1",
    "title": "polygon2d -- several issues: typo in docs, shouldn't have been renamed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6367",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  ksmith

The help for polygon2d? says:


```
 Type ``polygon.options`` for a dictionary of the default 
    options for polygons.  You can change this to change 
```

but it should say

```
 Type ``polygon2d.options`` for a dictionary of the default 
    options for polygons.  You can change this to change 
```


And for the record I think it is unfortunate that somebody changed the function name from polygon to polygon2d, since that it inconsistent with almost all the rest of plotting in Sage, where the 2d version of the function doesn't specifically say it is 2d (e.g., plot, line, text, etc.) Well, there is line2d, to add to the confusion.    The design of Sage graphics is *supposed* to follow the naming scheme in Matheamtica.  In Mathematica there is Polygon and Polygon3D.  That's what Sage should have.

To resolve this patch, either fix the docstring or change the name back to polygon (not polygon2d).  I prefer the latter for consistency with the rest fo the design of sage 2d graphics. 




Issue created by migration from https://trac.sagemath.org/ticket/6367





---

archive/issue_comments_050832.json:
```json
{
    "body": "For the record, this caused some actual problems for a potential Sage user recently, so it should get fixed - and soon.  Probably we'll need to make polygon=polygon2d (for 2d input) for deprecation reasons, for now.",
    "created_at": "2010-07-27T17:25:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6367#issuecomment-50832",
    "user": "https://github.com/kcrisman"
}
```

For the record, this caused some actual problems for a potential Sage user recently, so it should get fixed - and soon.  Probably we'll need to make polygon=polygon2d (for 2d input) for deprecation reasons, for now.



---

archive/issue_comments_050833.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-05-26T21:11:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6367#issuecomment-50833",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_050834.json:
```json
{
    "body": "Unfortunately this is pretty hard to change since `polygon` is expected to work for two and three D input.  This patch does take care of the problem.",
    "created_at": "2012-05-26T21:11:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6367#issuecomment-50834",
    "user": "https://github.com/kcrisman"
}
```

Unfortunately this is pretty hard to change since `polygon` is expected to work for two and three D input.  This patch does take care of the problem.



---

archive/issue_comments_050835.json:
```json
{
    "body": "Attachment [trac_6367-polygon.patch](tarball://root/attachments/some-uuid/ticket6367/trac_6367-polygon.patch) by @kcrisman created at 2012-05-26 21:13:27\n\n> Unfortunately this is pretty hard to change since `polygon` is expected to work for two and three D input.\nWhat I mean, of course, is that it would be hard to change since users probably are using it this way a lot and the deprecation period and all simply isn't worth the effort at this point.  Anyway, needs review.",
    "created_at": "2012-05-26T21:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6367#issuecomment-50835",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_6367-polygon.patch](tarball://root/attachments/some-uuid/ticket6367/trac_6367-polygon.patch) by @kcrisman created at 2012-05-26 21:13:27

> Unfortunately this is pretty hard to change since `polygon` is expected to work for two and three D input.
What I mean, of course, is that it would be hard to change since users probably are using it this way a lot and the deprecation period and all simply isn't worth the effort at this point.  Anyway, needs review.



---

archive/issue_comments_050836.json:
```json
{
    "body": "Oops, totally forgot about #12214, which is a dup of this.  Given that #12214 is virtually the same ticket, this one is much older, and the patch is quite similar, I'm adding the author there to this ticket and closing that one.",
    "created_at": "2012-05-27T06:50:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6367#issuecomment-50836",
    "user": "https://github.com/kcrisman"
}
```

Oops, totally forgot about #12214, which is a dup of this.  Given that #12214 is virtually the same ticket, this one is much older, and the patch is quite similar, I'm adding the author there to this ticket and closing that one.



---

archive/issue_comments_050837.json:
```json
{
    "body": "Looks good to me!",
    "created_at": "2012-11-06T04:14:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6367#issuecomment-50837",
    "user": "https://github.com/vbraun"
}
```

Looks good to me!



---

archive/issue_comments_050838.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-11-06T04:14:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6367#issuecomment-50838",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_050839.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-11-11T09:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6367",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6367#issuecomment-50839",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_006616.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-11-11T09:48:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6367",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6367#event-6616"
}
```
