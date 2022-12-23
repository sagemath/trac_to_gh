# Issue 5812: option zorder has no effect for point() and polygon()

archive/issues_005812.json:
```json
{
    "body": "Assignee: whuss\n\nCurrently setting the zorder for points and polygons has no effect although zorder is listed as an allowed option.\n\n\n```\nsage: g = polygon([(0,0), (0,1), (1,1), (1,0)], rgbcolor = 'red', zorder = 0)\nsage: g += point((1,1), rgbcolor = 'green', pointsize = 1000, zorder = 1)\nsage: g.show()\n```\n\n\n\n```\nsage: g = polygon([(0,0), (0,1), (1,1), (1,0)], rgbcolor = 'red', zorder = 1)\nsage: g += point((1,1), rgbcolor = 'green', pointsize = 1000, zorder = 0)\nsage: g.show()\n```\n\n\nBoth of the above commands currently give the same output.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5812\n\n",
    "created_at": "2009-04-17T16:38:25Z",
    "labels": [
        "graphics",
        "minor",
        "bug"
    ],
    "title": "option zorder has no effect for point() and polygon()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5812",
    "user": "whuss"
}
```
Assignee: whuss

Currently setting the zorder for points and polygons has no effect although zorder is listed as an allowed option.


```
sage: g = polygon([(0,0), (0,1), (1,1), (1,0)], rgbcolor = 'red', zorder = 0)
sage: g += point((1,1), rgbcolor = 'green', pointsize = 1000, zorder = 1)
sage: g.show()
```



```
sage: g = polygon([(0,0), (0,1), (1,1), (1,0)], rgbcolor = 'red', zorder = 1)
sage: g += point((1,1), rgbcolor = 'green', pointsize = 1000, zorder = 0)
sage: g.show()
```


Both of the above commands currently give the same output.

Issue created by migration from https://trac.sagemath.org/ticket/5812





---

archive/issue_comments_045644.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-04-17T17:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5812#issuecomment-45644",
    "user": "whuss"
}
```

Attachment



---

archive/issue_comments_045645.json:
```json
{
    "body": "Seems to work as advertised - a nice addition!   One question: if I manually set zorder, usually what you expect to happen happens.  But doesn't the order in which the objects are created matter otherwise, if everything has the same zorder?  For instance:\n\n```\nsage: p = polygon([(0,0),(0,1),(1,1)])\nsage: p+= polygon([(0,0),(0,2),(2,2)],rgbcolor='red')\nsage: p.show()\n```\n\ngives only a red triangle, while\n\n```\nsage: p = polygon([(0,0),(0,2),(2,2)],rgbcolor='red')\nsage: p+= polygon([(0,0),(0,1),(1,1)])\nsage: p.show()\n```\n\nshows the blue triangle on top of the red one.  But\n\n```\nsage: g = polygon([(0,0), (0,1), (1,1), (1,0)], rgbcolor = 'red', zorder = 0)\nsage: g += point((1,1), rgbcolor = 'green', pointsize = 1000)\nsage: g.show()\n```\n\nand \n\n```\nsage: g = point((1,1), rgbcolor = 'green', pointsize = 1000)\nsage: g += polygon([(0,0), (0,1), (1,1), (1,0)], rgbcolor = 'red', zorder = 0)\nsage: g.show()\n```\n\ngive the same thing, even though they should also have the same zorder at this point, if I understand the code correctly.  Or does the polygon somehow take precedence naturally in matplotlib?\n\nREVIEW\n\nPositive review of fixing the example given.  With regards to the comments above:\n\nIf this is a bug or design in matplotlib, positive review.\n\nIf it's possible to fix this in one of these files so that the order plots are added behaves consistently, needs work.  \n\nIf it's not possible to do that within these files, but it needs to be done in plot.py or show or something, positive review but please open another ticket.",
    "created_at": "2009-04-28T20:28:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5812#issuecomment-45645",
    "user": "kcrisman"
}
```

Seems to work as advertised - a nice addition!   One question: if I manually set zorder, usually what you expect to happen happens.  But doesn't the order in which the objects are created matter otherwise, if everything has the same zorder?  For instance:

```
sage: p = polygon([(0,0),(0,1),(1,1)])
sage: p+= polygon([(0,0),(0,2),(2,2)],rgbcolor='red')
sage: p.show()
```

gives only a red triangle, while

```
sage: p = polygon([(0,0),(0,2),(2,2)],rgbcolor='red')
sage: p+= polygon([(0,0),(0,1),(1,1)])
sage: p.show()
```

shows the blue triangle on top of the red one.  But

```
sage: g = polygon([(0,0), (0,1), (1,1), (1,0)], rgbcolor = 'red', zorder = 0)
sage: g += point((1,1), rgbcolor = 'green', pointsize = 1000)
sage: g.show()
```

and 

```
sage: g = point((1,1), rgbcolor = 'green', pointsize = 1000)
sage: g += polygon([(0,0), (0,1), (1,1), (1,0)], rgbcolor = 'red', zorder = 0)
sage: g.show()
```

give the same thing, even though they should also have the same zorder at this point, if I understand the code correctly.  Or does the polygon somehow take precedence naturally in matplotlib?

REVIEW

Positive review of fixing the example given.  With regards to the comments above:

If this is a bug or design in matplotlib, positive review.

If it's possible to fix this in one of these files so that the order plots are added behaves consistently, needs work.  

If it's not possible to do that within these files, but it needs to be done in plot.py or show or something, positive review but please open another ticket.



---

archive/issue_comments_045646.json:
```json
{
    "body": "I also just tripped over this bug. I checked that the no-brainer patch fixes it. There is no easy way to doctest the graphical output. \n\nSince the correct patch just sat around for half a year, I will change it to \"positive review\" in hopes that the patch will be applied.\n\nIn case the philosophical issue of how to handle equal zorders ever gets sorted out, please report in bug #6249. But this bug has served its purpose and the patch should be applied asap.",
    "created_at": "2009-10-08T19:34:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5812#issuecomment-45646",
    "user": "vbraun"
}
```

I also just tripped over this bug. I checked that the no-brainer patch fixes it. There is no easy way to doctest the graphical output. 

Since the correct patch just sat around for half a year, I will change it to "positive review" in hopes that the patch will be applied.

In case the philosophical issue of how to handle equal zorders ever gets sorted out, please report in bug #6249. But this bug has served its purpose and the patch should be applied asap.



---

archive/issue_comments_045647.json:
```json
{
    "body": "Dear vbraun,\n\nCan you put your full name here?  The release managers like that, as it makes things easier.",
    "created_at": "2009-10-08T19:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5812#issuecomment-45647",
    "user": "kcrisman"
}
```

Dear vbraun,

Can you put your full name here?  The release managers like that, as it makes things easier.



---

archive/issue_comments_045648.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-08T19:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5812#issuecomment-45648",
    "user": "kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_045649.json:
```json
{
    "body": "Then you can also move it to the \"positive review\" button below.  The new trac workflow will take some getting used to, it's true...",
    "created_at": "2009-10-08T19:38:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5812#issuecomment-45649",
    "user": "kcrisman"
}
```

Then you can also move it to the "positive review" button below.  The new trac workflow will take some getting used to, it's true...



---

archive/issue_comments_045650.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-08T19:46:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5812#issuecomment-45650",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_045651.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T16:17:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5812#issuecomment-45651",
    "user": "mhansen"
}
```

Resolution: fixed
