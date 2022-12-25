# Issue 8529: default colors for plot and implicit_plot are not consistent

archive/issues_008529.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @kcrisman\n\nKeywords: plot default color beginner\n\nWhen plotting a function using `plot`, the default color for the graph of the function is blue.  The default color for `implicit_plot` is black.  It would be preferable to have the same default color.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8529\n\n",
    "closed_at": "2010-11-01T10:05:49Z",
    "created_at": "2010-03-13T22:34:10Z",
    "labels": [
        "component: graphics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "default colors for plot and implicit_plot are not consistent",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8529",
    "user": "https://github.com/aghitza"
}
```
Assignee: @williamstein

CC:  @kcrisman

Keywords: plot default color beginner

When plotting a function using `plot`, the default color for the graph of the function is blue.  The default color for `implicit_plot` is black.  It would be preferable to have the same default color.

Issue created by migration from https://trac.sagemath.org/ticket/8529





---

archive/issue_comments_076947.json:
```json
{
    "body": "Changing keywords from \"plot default color\" to \"plot default color beginner\".",
    "created_at": "2010-05-26T15:44:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76947",
    "user": "https://github.com/jasongrout"
}
```

Changing keywords from "plot default color" to "plot default color beginner".



---

archive/issue_comments_076948.json:
```json
{
    "body": "the attached patch will change the default color of plot to black (so that it matches implicit_plot).",
    "created_at": "2010-07-27T23:39:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76948",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

the attached patch will change the default color of plot to black (so that it matches implicit_plot).



---

archive/issue_comments_076949.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-07-27T23:44:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76949",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_076950.json:
```json
{
    "body": "Ryan!  Welcome to Trac!  Congratulations on your patch!\n\nI think maybe it would be better to make the implicit plot default color be blue.  I like that a plot is a different color than the axes so that it's easier to distinguish the two.\n\nAlso, when a patch is ready for review, change the state below to \"needs review\".",
    "created_at": "2010-07-27T23:44:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76950",
    "user": "https://github.com/jasongrout"
}
```

Ryan!  Welcome to Trac!  Congratulations on your patch!

I think maybe it would be better to make the implicit plot default color be blue.  I like that a plot is a different color than the axes so that it's easier to distinguish the two.

Also, when a patch is ready for review, change the state below to "needs review".



---

archive/issue_comments_076951.json:
```json
{
    "body": "See http://sagenb.org/home/jason3/230/ for how to plot implicit plots in a different color:\n\n```\nvar('x,y')\nimplicit_plot(x^2-y^2==1, (x,-5,5), (y,-5,5), cmap=[\"red\"])\n```\n\nI think it might be enough to give another argument to the `@`options decorator for implicit_plot: `cmap=[\"blue\"]`",
    "created_at": "2010-07-27T23:55:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76951",
    "user": "https://github.com/jasongrout"
}
```

See http://sagenb.org/home/jason3/230/ for how to plot implicit plots in a different color:

```
var('x,y')
implicit_plot(x^2-y^2==1, (x,-5,5), (y,-5,5), cmap=["red"])
```

I think it might be enough to give another argument to the `@`options decorator for implicit_plot: `cmap=["blue"]`



---

archive/issue_comments_076952.json:
```json
{
    "body": "Even better, do `cmap=(\"blue\")`, since then the tuple can not be modified by other things.",
    "created_at": "2010-07-27T23:59:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76952",
    "user": "https://github.com/jasongrout"
}
```

Even better, do `cmap=("blue")`, since then the tuple can not be modified by other things.



---

archive/issue_comments_076953.json:
```json
{
    "body": "Replying to [comment:6 jason]:\n> Even better, do `cmap=(\"blue\")`, since then the tuple can not be modified by other things.\n\n\nI mean `cmap=(\"blue\",)`, so that it's a tuple, not just a string in parentheses.",
    "created_at": "2010-07-28T00:01:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76953",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:6 jason]:
> Even better, do `cmap=("blue")`, since then the tuple can not be modified by other things.


I mean `cmap=("blue",)`, so that it's a tuple, not just a string in parentheses.



---

archive/issue_comments_076954.json:
```json
{
    "body": "Replying to [comment:5 jason]:\n> See http://sagenb.org/home/jason3/230/ for how to plot implicit plots in a different color:\n\n\nIf you published this, you didn't include the link.\n> \n> \n> ```\n> var('x,y')\n> implicit_plot(x^2-y^2==1, (x,-5,5), (y,-5,5), cmap=[\"red\"])\n> ```\n\n\nSo annoying that color='red' wouldn't work.  What happens with that?",
    "created_at": "2010-07-28T01:17:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76954",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:5 jason]:
> See http://sagenb.org/home/jason3/230/ for how to plot implicit plots in a different color:


If you published this, you didn't include the link.
> 
> 
> ```
> var('x,y')
> implicit_plot(x^2-y^2==1, (x,-5,5), (y,-5,5), cmap=["red"])
> ```


So annoying that color='red' wouldn't work.  What happens with that?



---

archive/issue_comments_076955.json:
```json
{
    "body": "Replying to [comment:4 jason]:\n> Ryan!  Welcome to Trac!  Congratulations on your patch!\n> \n\n\nYes!  You aren't by chance the famed little brother of Jason, are you?",
    "created_at": "2010-07-28T01:18:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76955",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:4 jason]:
> Ryan!  Welcome to Trac!  Congratulations on your patch!
> 


Yes!  You aren't by chance the famed little brother of Jason, are you?



---

archive/issue_comments_076956.json:
```json
{
    "body": "Replying to [comment:8 kcrisman]:\n\n\n> So annoying that color='red' wouldn't work.  What happens with that?\n\n\nThat would take one or two more lines of code to support.  Probably add it to `@`options, and then make a cmap=[<color>] argument that is passed to contour_plot.",
    "created_at": "2010-07-28T08:00:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76956",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:8 kcrisman]:


> So annoying that color='red' wouldn't work.  What happens with that?


That would take one or two more lines of code to support.  Probably add it to `@`options, and then make a cmap=[<color>] argument that is passed to contour_plot.



---

archive/issue_comments_076957.json:
```json
{
    "body": "ok...here's the new patch.\n\nOne can now set the color of implicit_plot using cmap or the \"new\" color option (idea curtesy of kcrisman).  Note: syntax for cmap is still the same.  Syntax for color is ` color='blue' `\n\n`@`kcrisman: Yeah, I'm Jason's little brother.  \n\nHave fun with all those colorful plots :)",
    "created_at": "2010-07-30T20:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76957",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

ok...here's the new patch.

One can now set the color of implicit_plot using cmap or the "new" color option (idea curtesy of kcrisman).  Note: syntax for cmap is still the same.  Syntax for color is ` color='blue' `

`@`kcrisman: Yeah, I'm Jason's little brother.  

Have fun with all those colorful plots :)



---

archive/issue_comments_076958.json:
```json
{
    "body": "This is great.  Just one more thing: there should be some sort of doctest illustrating this (the question of how to change the color of an implicit plot has come up before, and it's bound to come up again, so it'd be nice to just point them to the documentation of the function).\n\nJust take your favorite example and put it in the EXAMPLES section of the docstring of the function, following the format of the examples around it.",
    "created_at": "2010-07-31T04:33:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76958",
    "user": "https://github.com/jasongrout"
}
```

This is great.  Just one more thing: there should be some sort of doctest illustrating this (the question of how to change the color of an implicit plot has come up before, and it's bound to come up again, so it'd be nice to just point them to the documentation of the function).

Just take your favorite example and put it in the EXAMPLES section of the docstring of the function, following the format of the examples around it.



---

archive/issue_comments_076959.json:
```json
{
    "body": "(and it's more than nice; patches are required to have doctests if they fix a bug or add new features these days...)\n\nAfter you add a doctest, then you can run:\n\n```\nsage -b\n```\n\nto rebuild, and then \n\n```\nsage -t contour_plot.py\n```\n\nto run the tests.",
    "created_at": "2010-07-31T04:35:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76959",
    "user": "https://github.com/jasongrout"
}
```

(and it's more than nice; patches are required to have doctests if they fix a bug or add new features these days...)

After you add a doctest, then you can run:

```
sage -b
```

to rebuild, and then 

```
sage -t contour_plot.py
```

to run the tests.



---

archive/issue_comments_076960.json:
```json
{
    "body": "(Patch + Documentation) Change color of implicit plot.",
    "created_at": "2010-08-01T01:21:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76960",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

(Patch + Documentation) Change color of implicit plot.



---

archive/issue_comments_076961.json:
```json
{
    "body": "Attachment [trac_8529_color_implicit_plot.patch](tarball://root/attachments/some-uuid/ticket8529/trac_8529_color_implicit_plot.patch) by ryan created at 2010-08-01 01:22:54\n\nok...updated patch (with documentation).\n\nThanks jason for the reminder add the documentation.  This patch passed the doctests.",
    "created_at": "2010-08-01T01:22:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76961",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Attachment [trac_8529_color_implicit_plot.patch](tarball://root/attachments/some-uuid/ticket8529/trac_8529_color_implicit_plot.patch) by ryan created at 2010-08-01 01:22:54

ok...updated patch (with documentation).

Thanks jason for the reminder add the documentation.  This patch passed the doctests.



---

archive/issue_comments_076962.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-03T06:38:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76962",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076963.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-10T16:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76963",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076964.json:
```json
{
    "body": "This is nice - positive review.  \n\nI fixed some minor doc issues added a really cool example I stumbled upon while testing it (picture attached), and also updated some other minor doc issues which became apparent with this - all of which are basically related to the color or are just typos.\n\nTo release manager: Apply `trac_8529-color-implicit-plot` and then `trac-8529-reviewer`.",
    "created_at": "2010-08-10T16:06:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76964",
    "user": "https://github.com/kcrisman"
}
```

This is nice - positive review.  

I fixed some minor doc issues added a really cool example I stumbled upon while testing it (picture attached), and also updated some other minor doc issues which became apparent with this - all of which are basically related to the color or are just typos.

To release manager: Apply `trac_8529-color-implicit-plot` and then `trac-8529-reviewer`.



---

archive/issue_comments_076965.json:
```json
{
    "body": "Apply after initial patch",
    "created_at": "2010-08-10T16:07:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76965",
    "user": "https://github.com/kcrisman"
}
```

Apply after initial patch



---

archive/issue_comments_076966.json:
```json
{
    "body": "Attachment [trac_8529-reviewer.patch](tarball://root/attachments/some-uuid/ticket8529/trac_8529-reviewer.patch) by @kcrisman created at 2010-08-10 16:07:40\n\nSuper-cool example picture of this patch working",
    "created_at": "2010-08-10T16:07:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76966",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_8529-reviewer.patch](tarball://root/attachments/some-uuid/ticket8529/trac_8529-reviewer.patch) by @kcrisman created at 2010-08-10 16:07:40

Super-cool example picture of this patch working



---

archive/issue_comments_076967.json:
```json
{
    "body": "Attachment [ColorfulCircles.png](tarball://root/attachments/some-uuid/ticket8529/ColorfulCircles.png) by @jasongrout created at 2010-08-14 08:40:34\n\nThis solves #9654 too.",
    "created_at": "2010-08-14T08:40:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76967",
    "user": "https://github.com/jasongrout"
}
```

Attachment [ColorfulCircles.png](tarball://root/attachments/some-uuid/ticket8529/ColorfulCircles.png) by @jasongrout created at 2010-08-14 08:40:34

This solves #9654 too.



---

archive/issue_comments_076968.json:
```json
{
    "body": "please apply my reviewer-reviewer patch on top of everything else; it simplifies the doc source a little.",
    "created_at": "2010-08-14T14:47:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76968",
    "user": "https://github.com/jasongrout"
}
```

please apply my reviewer-reviewer patch on top of everything else; it simplifies the doc source a little.



---

archive/issue_comments_076969.json:
```json
{
    "body": "Replying to [comment:18 jason]:\n> please apply my reviewer-reviewer patch on top of everything else; it simplifies the doc source a little.\n\nThanks, I didn't know about this `~` notation.",
    "created_at": "2010-08-16T12:31:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76969",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:18 jason]:
> please apply my reviewer-reviewer patch on top of everything else; it simplifies the doc source a little.

Thanks, I didn't know about this `~` notation.



---

archive/issue_comments_076970.json:
```json
{
    "body": "Just FYI, the (essentially) positively reviewed #9203 and #9076 add functions with the same `~` not being used, and won't apply properly with this one.  I recommend that those be applied first, then this one applied to see what would need to be updated, and then this one updated - since those implement actual new functionality.  Or we can split this one up into a different ticket for updating the plot doc, or add that in with #9746.",
    "created_at": "2010-08-16T12:54:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76970",
    "user": "https://github.com/kcrisman"
}
```

Just FYI, the (essentially) positively reviewed #9203 and #9076 add functions with the same `~` not being used, and won't apply properly with this one.  I recommend that those be applied first, then this one applied to see what would need to be updated, and then this one updated - since those implement actual new functionality.  Or we can split this one up into a different ticket for updating the plot doc, or add that in with #9746.



---

archive/issue_comments_076971.json:
```json
{
    "body": "With the other tickets merged into 4.6.alpha1, I get\n\n```\n[...]\n$ hg qpush\napplying trac-8529-reviewer-reviewer.patch\npatching file sage/plot/plot.py\nHunk #1 FAILED at 6\n1 out of 3 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac-8529-reviewer-reviewer.patch\n```\nThe .rej file:\n\n```diff\n--- plot.py\n+++ plot.py\n@@ -7,20 +7,20 @@\n The following graphics primitives are supported:\n \n \n--  :func:`arrow() <sage.plot.arrow.arrow>` - an arrow from a min point to a max point.\n-\n--  :func:`circle() <sage.plot.circle.circle>` - a circle with given radius\n-\n--  :func:`disk() <sage.plot.disk.disk>` - a filled disk (i.e. a sector or wedge of a circle)\n-\n--  :func:`line() <sage.plot.line.line>` - a line determined by a sequence of points (this need not\n+-  :func:`~sage.plot.arrow.arrow` - an arrow from a min point to a max point.\n+\n+-  :func:`~sage.plot.circle.circle` - a circle with given radius\n+\n+-  :func:`~sage.plot.disk.disk` - a filled disk (i.e. a sector or wedge of a circle)\n+\n+-  :func:`~sage.plot.line.line` - a line determined by a sequence of points (this need not\n    be straight!)\n \n--  :func:`point() <sage.plot.point.point>` - a point\n-\n--  :func:`text() <sage.plot.text.text>` - some text\n-\n--  :func:`polygon() <sage.plot.polygon.polygon>` - a filled polygon\n+-  :func:`~sage.plot.point.point` - a point\n+\n+-  :func:`~sage.plot.text.text` - some text\n+\n+-  :func:`~sage.plot.polygon.polygon` - a filled polygon\n \n \n The following plotting functions are supported:\n```\nCould someone rebase the \"reviewer-reviewer\" patch when 4.6.alpha1 is out?",
    "created_at": "2010-09-18T07:37:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76971",
    "user": "https://github.com/qed777"
}
```

With the other tickets merged into 4.6.alpha1, I get

```
[...]
$ hg qpush
applying trac-8529-reviewer-reviewer.patch
patching file sage/plot/plot.py
Hunk #1 FAILED at 6
1 out of 3 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac-8529-reviewer-reviewer.patch
```
The .rej file:

```diff
--- plot.py
+++ plot.py
@@ -7,20 +7,20 @@
 The following graphics primitives are supported:
 
 
--  :func:`arrow() <sage.plot.arrow.arrow>` - an arrow from a min point to a max point.
-
--  :func:`circle() <sage.plot.circle.circle>` - a circle with given radius
-
--  :func:`disk() <sage.plot.disk.disk>` - a filled disk (i.e. a sector or wedge of a circle)
-
--  :func:`line() <sage.plot.line.line>` - a line determined by a sequence of points (this need not
+-  :func:`~sage.plot.arrow.arrow` - an arrow from a min point to a max point.
+
+-  :func:`~sage.plot.circle.circle` - a circle with given radius
+
+-  :func:`~sage.plot.disk.disk` - a filled disk (i.e. a sector or wedge of a circle)
+
+-  :func:`~sage.plot.line.line` - a line determined by a sequence of points (this need not
    be straight!)
 
--  :func:`point() <sage.plot.point.point>` - a point
-
--  :func:`text() <sage.plot.text.text>` - some text
-
--  :func:`polygon() <sage.plot.polygon.polygon>` - a filled polygon
+-  :func:`~sage.plot.point.point` - a point
+
+-  :func:`~sage.plot.text.text` - some text
+
+-  :func:`~sage.plot.polygon.polygon` - a filled polygon
 
 
 The following plotting functions are supported:
```
Could someone rebase the "reviewer-reviewer" patch when 4.6.alpha1 is out?



---

archive/issue_comments_076972.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-18T07:37:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76972",
    "user": "https://github.com/qed777"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_076973.json:
```json
{
    "body": "apply on top of previous patches",
    "created_at": "2010-10-19T06:12:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76973",
    "user": "https://github.com/jasongrout"
}
```

apply on top of previous patches



---

archive/issue_comments_076974.json:
```json
{
    "body": "Attachment [trac-8529-reviewer-reviewer.patch](tarball://root/attachments/some-uuid/ticket8529/trac-8529-reviewer-reviewer.patch) by @jasongrout created at 2010-10-19 06:26:26\n\nI rebased the reviewer-reviewer patch for 4.6.alpha3.  In fact, that reviewer-reviewer patch was so picky, it probably would have been okay to just ignore it anyway.",
    "created_at": "2010-10-19T06:26:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76974",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-8529-reviewer-reviewer.patch](tarball://root/attachments/some-uuid/ticket8529/trac-8529-reviewer-reviewer.patch) by @jasongrout created at 2010-10-19 06:26:26

I rebased the reviewer-reviewer patch for 4.6.alpha3.  In fact, that reviewer-reviewer patch was so picky, it probably would have been okay to just ignore it anyway.



---

archive/issue_comments_076975.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-10-19T06:26:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76975",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_076976.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-01T10:05:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8529#issuecomment-76976",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_020522.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-11-01T10:05:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8529#event-20522"
}
```



---

archive/issue_events_020523.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-11-01T10:26:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8529",
    "milestone": "sage-4.6.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8529#event-20523"
}
```
