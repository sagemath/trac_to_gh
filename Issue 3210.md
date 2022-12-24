# Issue 3210: [with patch, needs review] plotting Z_p as a fractal image

archive/issues_003210.json:
```json
{
    "body": "Assignee: was\n\nSee:\n\nAlbert A. Cuoco, Visualizing the p-adic Integers, The American Mathematical Monthly, Vol. 98, No. 4 (Apr., 1991), pp. 355-364\n\nhttp://www.jstor.org/stable/2323809?&Search=yes&term=numbers&term=p-adic&list=hide&searchUri=%2Faction%2FdoBasicSearch%3FQuery%3Dp-adic%2Bnumbers%26jc%3Dj100069&item=2&ttl=190&returnArticleService=showArticle\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3210\n\n",
    "created_at": "2008-05-15T06:45:24Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] plotting Z_p as a fractal image",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3210",
    "user": "robertwb"
}
```
Assignee: was

See:

Albert A. Cuoco, Visualizing the p-adic Integers, The American Mathematical Monthly, Vol. 98, No. 4 (Apr., 1991), pp. 355-364

http://www.jstor.org/stable/2323809?&Search=yes&term=numbers&term=p-adic&list=hide&searchUri=%2Faction%2FdoBasicSearch%3FQuery%3Dp-adic%2Bnumbers%26jc%3Dj100069&item=2&ttl=190&returnArticleService=showArticle


Issue created by migration from https://trac.sagemath.org/ticket/3210





---

archive/issue_comments_022187.json:
```json
{
    "body": "Attachment [3210-plot-Zp.patch](tarball://root/attachments/some-uuid/ticket3210/3210-plot-Zp.patch) by robertwb created at 2008-05-15 06:47:19",
    "created_at": "2008-05-15T06:47:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3210#issuecomment-22187",
    "user": "robertwb"
}
```

Attachment [3210-plot-Zp.patch](tarball://root/attachments/some-uuid/ticket3210/3210-plot-Zp.patch) by robertwb created at 2008-05-15 06:47:19



---

archive/issue_comments_022188.json:
```json
{
    "body": "Attachment [Z5.png](tarball://root/attachments/some-uuid/ticket3210/Z5.png) by malb created at 2008-05-15 08:47:42\n\ncool, quick comment, there is a typo in the docstring: \"algebraic an topological\"",
    "created_at": "2008-05-15T08:47:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3210#issuecomment-22188",
    "user": "malb"
}
```

Attachment [Z5.png](tarball://root/attachments/some-uuid/ticket3210/Z5.png) by malb created at 2008-05-15 08:47:42

cool, quick comment, there is a typo in the docstring: "algebraic an topological"



---

archive/issue_comments_022189.json:
```json
{
    "body": "Attachment [3210-plot-Zp-typo-fix.patch](tarball://root/attachments/some-uuid/ticket3210/3210-plot-Zp-typo-fix.patch) by robertwb created at 2008-05-15 08:52:28",
    "created_at": "2008-05-15T08:52:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3210#issuecomment-22189",
    "user": "robertwb"
}
```

Attachment [3210-plot-Zp-typo-fix.patch](tarball://root/attachments/some-uuid/ticket3210/3210-plot-Zp-typo-fix.patch) by robertwb created at 2008-05-15 08:52:28



---

archive/issue_comments_022190.json:
```json
{
    "body": "Attached an updated patch with typo fixed.",
    "created_at": "2008-05-15T08:52:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3210#issuecomment-22190",
    "user": "robertwb"
}
```

Attached an updated patch with typo fixed.



---

archive/issue_comments_022191.json:
```json
{
    "body": "This is a very neat feature, useful if you are teaching number theory or topology, say.\n\nI didn't realize that the second patch was a replacement for the 1st patch, so I tried to \napply them both and of course failed. The 1st patch works as claimed and passes sage -testall.\n(Actually, on my old machine, \n\n\n```\nThe following tests failed:\n\n\n        sage -t  devel/sage/sage/matrix/benchmark.py\n        sage -t  devel/sage/sage/server/notebook/worksheet.py\n```\n\nbut then they passes on retesting.)\n\nMy suggestion, and it really a very minor one, is that the \"radius\"\nwhere the points are plotted should be a parameter the user can reset. \nFor example, if you graph a p=3 and a p=7 then they overlap maybe more\nthat some would like. Not that I see this as important for teaching but might\nbe a fun option for making cool pictures. Just an idea.",
    "created_at": "2008-05-15T18:01:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3210#issuecomment-22191",
    "user": "wdj"
}
```

This is a very neat feature, useful if you are teaching number theory or topology, say.

I didn't realize that the second patch was a replacement for the 1st patch, so I tried to 
apply them both and of course failed. The 1st patch works as claimed and passes sage -testall.
(Actually, on my old machine, 


```
The following tests failed:


        sage -t  devel/sage/sage/matrix/benchmark.py
        sage -t  devel/sage/sage/server/notebook/worksheet.py
```

but then they passes on retesting.)

My suggestion, and it really a very minor one, is that the "radius"
where the points are plotted should be a parameter the user can reset. 
For example, if you graph a p=3 and a p=7 then they overlap maybe more
that some would like. Not that I see this as important for teaching but might
be a fun option for making cool pictures. Just an idea.



---

archive/issue_comments_022192.json:
```json
{
    "body": "FYI, I added another example of the bottom of http://wiki.sagemath.org/pics.",
    "created_at": "2008-05-15T18:17:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3210#issuecomment-22192",
    "user": "wdj"
}
```

FYI, I added another example of the bottom of http://wiki.sagemath.org/pics.



---

archive/issue_comments_022193.json:
```json
{
    "body": "Cool image at http://wiki.sagemath.org/pics. :)\n\nThe \"radius\" can be changed with the pointsize parameter. Also, you could plot it with fewer points (as for p=3 or 7, the \"points\" you're seeing are probably a cluster of even smaller ones).",
    "created_at": "2008-05-15T18:38:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3210#issuecomment-22193",
    "user": "robertwb"
}
```

Cool image at http://wiki.sagemath.org/pics. :)

The "radius" can be changed with the pointsize parameter. Also, you could plot it with fewer points (as for p=3 or 7, the "points" you're seeing are probably a cluster of even smaller ones).



---

archive/issue_comments_022194.json:
```json
{
    "body": "I am talking about a dufferent radius I think. To me\n\n```\nsage: P1 = Zp(3).plot(pointsize=1,rgbcolor=(0,1,0))\nsage: P2 = Zp(7).plot(pointsize=2,rgbcolor=(1,0,0))\n```\n\nand\n\n```\nsage: P1 = Zp(3).plot(pointsize=1,rgbcolor=(0,1,0))\nsage: P2 = Zp(7).plot(pointsize=3,rgbcolor=(1,0,0))\n```\n\nLook the same. I was wondering about a scaling parameter \n\"distance\", say, where \n\n\n```\nsage: P1 = Zp(3).plot(distance=1,rgbcolor=(0,1,0))\n```\n\nwould plot the 3 triangles at (say) a circle of radius 1 from (0,0)\nas it does now, and \n\n\n```\nsage: P1 = Zp(3).plot(distance=2,rgbcolor=(0,1,0))\n```\n\nwould plot the 3 triangles at (say) a circle of radius 2 from (0,0).\n\nIs this possible without introducing a new parameter?",
    "created_at": "2008-05-15T19:12:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3210#issuecomment-22194",
    "user": "wdj"
}
```

I am talking about a dufferent radius I think. To me

```
sage: P1 = Zp(3).plot(pointsize=1,rgbcolor=(0,1,0))
sage: P2 = Zp(7).plot(pointsize=2,rgbcolor=(1,0,0))
```

and

```
sage: P1 = Zp(3).plot(pointsize=1,rgbcolor=(0,1,0))
sage: P2 = Zp(7).plot(pointsize=3,rgbcolor=(1,0,0))
```

Look the same. I was wondering about a scaling parameter 
"distance", say, where 


```
sage: P1 = Zp(3).plot(distance=1,rgbcolor=(0,1,0))
```

would plot the 3 triangles at (say) a circle of radius 1 from (0,0)
as it does now, and 


```
sage: P1 = Zp(3).plot(distance=2,rgbcolor=(0,1,0))
```

would plot the 3 triangles at (say) a circle of radius 2 from (0,0).

Is this possible without introducing a new parameter?



---

archive/issue_comments_022195.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_craigcitro\".",
    "created_at": "2008-06-15T21:44:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3210#issuecomment-22195",
    "user": "craigcitro"
}
```

Changing keywords from "" to "editor_craigcitro".



---

archive/issue_comments_022196.json:
```json
{
    "body": "This looks good, barring the extra feature request wdj has. I'm going to give this positive review, and file another ticket with the extra feature request as an enhancement and assign it to robertwb. \n\nI'm also adding a patch which adds an \"r\" to the docstring, in the hopes that this will cause less heartache with the reference manual.\n\nApply 3210-plot-Zp-typo-fix.patch followed by trac-3210-add-r.patch.",
    "created_at": "2008-06-19T21:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3210#issuecomment-22196",
    "user": "craigcitro"
}
```

This looks good, barring the extra feature request wdj has. I'm going to give this positive review, and file another ticket with the extra feature request as an enhancement and assign it to robertwb. 

I'm also adding a patch which adds an "r" to the docstring, in the hopes that this will cause less heartache with the reference manual.

Apply 3210-plot-Zp-typo-fix.patch followed by trac-3210-add-r.patch.



---

archive/issue_comments_022197.json:
```json
{
    "body": "Attachment [trac-3210-add-r.patch](tarball://root/attachments/some-uuid/ticket3210/trac-3210-add-r.patch) by craigcitro created at 2008-06-19 21:45:25\n\nThe new ticket is #3474.",
    "created_at": "2008-06-19T21:45:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3210#issuecomment-22197",
    "user": "craigcitro"
}
```

Attachment [trac-3210-add-r.patch](tarball://root/attachments/some-uuid/ticket3210/trac-3210-add-r.patch) by craigcitro created at 2008-06-19 21:45:25

The new ticket is #3474.



---

archive/issue_comments_022198.json:
```json
{
    "body": "Merged 3210-plot-Zp-typo-fix.patch and trac-3210-add-r.patch in Sage 3.0.4.alpha0",
    "created_at": "2008-06-23T10:20:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3210#issuecomment-22198",
    "user": "mabshoff"
}
```

Merged 3210-plot-Zp-typo-fix.patch and trac-3210-add-r.patch in Sage 3.0.4.alpha0



---

archive/issue_comments_022199.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-23T10:20:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3210",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3210#issuecomment-22199",
    "user": "mabshoff"
}
```

Resolution: fixed
