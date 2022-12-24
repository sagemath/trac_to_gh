# Issue 9744: implicit_plot fill option fills entire plot

archive/issues_009744.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @kcrisman\n\nI was browsing the docs and noticed this example completely fills the plot black:\n\n\n```\nx,y = var('x,y')\nf(x,y) = x^2 + y^2 - 2\nimplicit_plot(f, (-3, 3), (-3, 3),fill=True).show(aspect_ratio=1)\n```\n\n\nThe docs say it should fill the region f(x)<0.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9744\n\n",
    "created_at": "2010-08-14T09:13:18Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "implicit_plot fill option fills entire plot",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9744",
    "user": "@jasongrout"
}
```
Assignee: jason, was

CC:  @kcrisman

I was browsing the docs and noticed this example completely fills the plot black:


```
x,y = var('x,y')
f(x,y) = x^2 + y^2 - 2
implicit_plot(f, (-3, 3), (-3, 3),fill=True).show(aspect_ratio=1)
```


The docs say it should fill the region f(x)<0.

Issue created by migration from https://trac.sagemath.org/ticket/9744





---

archive/issue_comments_095406.json:
```json
{
    "body": "Attachment [implicit-plot-fill.patch](tarball://root/attachments/some-uuid/ticket9744/implicit-plot-fill.patch) by @jasongrout created at 2010-08-14 16:40:45",
    "created_at": "2010-08-14T16:40:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95406",
    "user": "@jasongrout"
}
```

Attachment [implicit-plot-fill.patch](tarball://root/attachments/some-uuid/ticket9744/implicit-plot-fill.patch) by @jasongrout created at 2010-08-14 16:40:45



---

archive/issue_comments_095407.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-08-14T16:43:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95407",
    "user": "@jasongrout"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_095408.json:
```json
{
    "body": "Here is a rough patch which conflicts with #9654, but gives an idea of how this issue could be resolved.",
    "created_at": "2010-08-14T16:43:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95408",
    "user": "@jasongrout"
}
```

Here is a rough patch which conflicts with #9654, but gives an idea of how this issue could be resolved.



---

archive/issue_comments_095409.json:
```json
{
    "body": "Hmm, I feel like there's another ticket about this... but anyway, this is important to fix.",
    "created_at": "2011-04-20T03:02:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95409",
    "user": "@kcrisman"
}
```

Hmm, I feel like there's another ticket about this... but anyway, this is important to fix.



---

archive/issue_comments_095410.json:
```json
{
    "body": "I think it's #8529 that you meant.  Anyway, is there anything wrong with this rough patch?  I don't see what the problem might be.",
    "created_at": "2011-06-14T05:26:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95410",
    "user": "@kcrisman"
}
```

I think it's #8529 that you meant.  Anyway, is there anything wrong with this rough patch?  I don't see what the problem might be.



---

archive/issue_comments_095411.json:
```json
{
    "body": "Attachment [trac_9744.patch](tarball://root/attachments/some-uuid/ticket9744/trac_9744.patch) by @mboratko created at 2011-11-22 16:38:40\n\nThis is just a modification of Jason's fix to work with the current version. I had to change 'contour' to 'contours', and also remove the 'cmap' option in order for it to work (you can see what I mean by comparing the two patches). I'm pretty new to this, so I'm not sure if this is the appropriate fix or not, but it has the desired effect.",
    "created_at": "2011-11-22T16:38:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95411",
    "user": "@mboratko"
}
```

Attachment [trac_9744.patch](tarball://root/attachments/some-uuid/ticket9744/trac_9744.patch) by @mboratko created at 2011-11-22 16:38:40

This is just a modification of Jason's fix to work with the current version. I had to change 'contour' to 'contours', and also remove the 'cmap' option in order for it to work (you can see what I mean by comparing the two patches). I'm pretty new to this, so I'm not sure if this is the appropriate fix or not, but it has the desired effect.



---

archive/issue_comments_095412.json:
```json
{
    "body": "Thanks for this; this would be good for [Sage Days 35.5](http://wiki.sagemath.org/days35.5/bugs).   Please change your name in the Author section to your real name, and (if you don't mind) add it to [the main Trac page](http://trac.sagemath.org/sage_trac/)!",
    "created_at": "2011-11-22T16:42:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95412",
    "user": "@kcrisman"
}
```

Thanks for this; this would be good for [Sage Days 35.5](http://wiki.sagemath.org/days35.5/bugs).   Please change your name in the Author section to your real name, and (if you don't mind) add it to [the main Trac page](http://trac.sagemath.org/sage_trac/)!



---

archive/issue_comments_095413.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-11-22T16:42:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95413",
    "user": "@kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_095414.json:
```json
{
    "body": "I ran into this bug and thought I would review the patch here. The patch applies cleanly to 4.8.alpha6 (I'm still waiting for 4.8.rc0 to build). Doctests on `sage/plot/contour_plot.py` pass. More importantly, I went through all the docstring examples for `implicit_plot` by hand in the notebook to make sure they look correct, and they all do so that's great!\n\nHowever, when I try the following (a modification of one of the doctests):\n\n\n```\nsage: def mandel(n):\n...       c = polygen(CDF, 'c')\n...       z = 0\n...       for i in range(n):\n...           z = z*z + c\n...       def f(x, y):\n...           val = z(CDF(x, y))\n...           return val.norm() - 4\n...       return f\nsage: implicit_plot(mandel(1), (-3, 3), (-3, 3), fill=True)\n```\n\nI get an error:\n\n```\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"_sage_input_21.py\", line 10, in <module>\n    exec compile(u'open(\"___code___.py\",\"w\").write(\"# -*- coding: utf-8 -*-\\\\n\" + _support_.preparse_worksheet_cell(base64.b64decode(\"aW1wbGljaXRfcGxvdChtYW5kZWwoMSksICgtMywgMyksICgtMywgMyksIGZpbGw9VHJ1ZSk=\"),globals())+\"\\\\n\"); execfile(os.path.abspath(\"___code___.py\"))\n  File \"\", line 1, in <module>\n    \n  File \"/tmp/tmpp9xXZj/___code___.py\", line 3, in <module>\n    exec compile(u'implicit_plot(mandel(_sage_const_1 ), (-_sage_const_3 , _sage_const_3 ), (-_sage_const_3 , _sage_const_3 ), fill=True)\n  File \"\", line 1, in <module>\n    \n  File \"/home/jonesbe/sage/sage-4.8.alpha6/local/lib/python2.6/site-packages/sage/misc/decorators.py\", line 534, in wrapper\n    return func(*args, **options)\n  File \"/home/jonesbe/sage/sage-4.8.alpha6/local/lib/python2.6/site-packages/sage/plot/contour_plot.py\", line 609, in implicit_plot\n    return region_plot(f<0, xrange, yrange, borderwidth=linewidths, borderstyle=linestyles, **options)\n  File \"/home/jonesbe/sage/sage-4.8.alpha6/local/lib/python2.6/site-packages/sage/misc/decorators.py\", line 534, in wrapper\n    return func(*args, **options)\n  File \"/home/jonesbe/sage/sage-4.8.alpha6/local/lib/python2.6/site-packages/sage/plot/contour_plot.py\", line 726, in region_plot\n    for func in g],dtype=float)\n  File \"/home/jonesbe/sage/sage-4.8.alpha6/local/lib/python2.6/site-packages/sage/plot/contour_plot.py\", line 783, in <lambda>\n    return lambda x,y: -1 if f(x,y) else 1\nTypeError: 'bool' object is not callable\n```\n\n\nAny idea what's going on here?",
    "created_at": "2012-01-16T20:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95414",
    "user": "@benjaminfjones"
}
```

I ran into this bug and thought I would review the patch here. The patch applies cleanly to 4.8.alpha6 (I'm still waiting for 4.8.rc0 to build). Doctests on `sage/plot/contour_plot.py` pass. More importantly, I went through all the docstring examples for `implicit_plot` by hand in the notebook to make sure they look correct, and they all do so that's great!

However, when I try the following (a modification of one of the doctests):


```
sage: def mandel(n):
...       c = polygen(CDF, 'c')
...       z = 0
...       for i in range(n):
...           z = z*z + c
...       def f(x, y):
...           val = z(CDF(x, y))
...           return val.norm() - 4
...       return f
sage: implicit_plot(mandel(1), (-3, 3), (-3, 3), fill=True)
```

I get an error:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "_sage_input_21.py", line 10, in <module>
    exec compile(u'open("___code___.py","w").write("# -*- coding: utf-8 -*-\\n" + _support_.preparse_worksheet_cell(base64.b64decode("aW1wbGljaXRfcGxvdChtYW5kZWwoMSksICgtMywgMyksICgtMywgMyksIGZpbGw9VHJ1ZSk="),globals())+"\\n"); execfile(os.path.abspath("___code___.py"))
  File "", line 1, in <module>
    
  File "/tmp/tmpp9xXZj/___code___.py", line 3, in <module>
    exec compile(u'implicit_plot(mandel(_sage_const_1 ), (-_sage_const_3 , _sage_const_3 ), (-_sage_const_3 , _sage_const_3 ), fill=True)
  File "", line 1, in <module>
    
  File "/home/jonesbe/sage/sage-4.8.alpha6/local/lib/python2.6/site-packages/sage/misc/decorators.py", line 534, in wrapper
    return func(*args, **options)
  File "/home/jonesbe/sage/sage-4.8.alpha6/local/lib/python2.6/site-packages/sage/plot/contour_plot.py", line 609, in implicit_plot
    return region_plot(f<0, xrange, yrange, borderwidth=linewidths, borderstyle=linestyles, **options)
  File "/home/jonesbe/sage/sage-4.8.alpha6/local/lib/python2.6/site-packages/sage/misc/decorators.py", line 534, in wrapper
    return func(*args, **options)
  File "/home/jonesbe/sage/sage-4.8.alpha6/local/lib/python2.6/site-packages/sage/plot/contour_plot.py", line 726, in region_plot
    for func in g],dtype=float)
  File "/home/jonesbe/sage/sage-4.8.alpha6/local/lib/python2.6/site-packages/sage/plot/contour_plot.py", line 783, in <lambda>
    return lambda x,y: -1 if f(x,y) else 1
TypeError: 'bool' object is not callable
```


Any idea what's going on here?



---

archive/issue_comments_095415.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-01-27T04:56:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95415",
    "user": "@kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_095416.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2012-01-27T04:56:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95416",
    "user": "@kcrisman"
}
```

Changing priority from major to critical.



---

archive/issue_comments_095417.json:
```json
{
    "body": "BFJ, I assume this means positive review apart from this error?\n\nHuh, yeah, this definitely means 'needs work'.  Even though the functionality didn't work at all before, lambdas shouldn't break too many things, and this is a very natural change to make.    The problem is in `equify` (see the [very bottom of the file](http://hg.sagemath.org/sage-main/file/c239be1054e0/sage/plot/contour_plot.py#l748).\n\n\n```\nsage: c = polygen(CDF,'c')\nsage: z = 0\nsage: for i in range(1):\n    z = z*z + c\n....: \nsage: def g(x,y):\n    val = z(CDF(x, y))\n    return val.norm() - 4\n....: \nsage: implicit_plot(g,(-3,3),(-3,3))  # looks fine, no surprise\n\nsage: sage.plot.contour_plot.equify(g)  # no problem, so plotting should work with fill\n<function <lambda> at 0x10df9d578>\nsage: implicit_plot(g,(-3,3),(-3,3),fill=True) # error above\n```\n\nGot it.  The problem is \n\n```\nf<0\n```\n\nin `region_plot`.   In the case I just did, \n\n```\nsage: g<0\nTrue\n```\n\nso we are now plotting `True` instead of `g`, which of course makes the error message quite understandable.\n\nI tried a few things to see if I could fix it in a few minutes, but I think the \"right\" answer might be more complicated.\n\nUnless we think we *should* just fix this and put in a warning about lambdas being broken?  Seems poor form.",
    "created_at": "2012-01-27T04:56:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95417",
    "user": "@kcrisman"
}
```

BFJ, I assume this means positive review apart from this error?

Huh, yeah, this definitely means 'needs work'.  Even though the functionality didn't work at all before, lambdas shouldn't break too many things, and this is a very natural change to make.    The problem is in `equify` (see the [very bottom of the file](http://hg.sagemath.org/sage-main/file/c239be1054e0/sage/plot/contour_plot.py#l748).


```
sage: c = polygen(CDF,'c')
sage: z = 0
sage: for i in range(1):
    z = z*z + c
....: 
sage: def g(x,y):
    val = z(CDF(x, y))
    return val.norm() - 4
....: 
sage: implicit_plot(g,(-3,3),(-3,3))  # looks fine, no surprise

sage: sage.plot.contour_plot.equify(g)  # no problem, so plotting should work with fill
<function <lambda> at 0x10df9d578>
sage: implicit_plot(g,(-3,3),(-3,3),fill=True) # error above
```

Got it.  The problem is 

```
f<0
```

in `region_plot`.   In the case I just did, 

```
sage: g<0
True
```

so we are now plotting `True` instead of `g`, which of course makes the error message quite understandable.

I tried a few things to see if I could fix it in a few minutes, but I think the "right" answer might be more complicated.

Unless we think we *should* just fix this and put in a warning about lambdas being broken?  Seems poor form.



---

archive/issue_comments_095418.json:
```json
{
    "body": "Yeah, seems like we should make it work for lambda's since implicit_plot works just fine, it's only when you set `fill=True` that you get a problem. I'll take a crack at it this afternoon.",
    "created_at": "2012-02-06T17:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95418",
    "user": "@benjaminfjones"
}
```

Yeah, seems like we should make it work for lambda's since implicit_plot works just fine, it's only when you set `fill=True` that you get a problem. I'll take a crack at it this afternoon.



---

archive/issue_comments_095419.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-02-24T01:48:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95419",
    "user": "@benjaminfjones"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_095420.json:
```json
{
    "body": "I uploaded [attachment:trac_9744_v2.patch] which solves the main problem by calling `region_plot(lambda x,y: f(x,y)<0, ...)` instead of `region_plot(f<0, ...)` \n\n...but it introduces a strange artefact. Try the following (this doesn't require applying the patch).\n\n\n```\nsage: region_plot(x^2+y^2-2<0, (x,-3,3), (y,-3,3))\n# looks normal\nsage: region_plot(lambda x,y: x^2+y^2-2<0, (x,-3,3), (y,-3,3))\n# looks ragged around the edges\nsage: region_plot(lambda x,y: x^2+y^2-2<0, (x,-3,3), (y,-3,3), plot_points=200)\n# better, but not great\nsage: region_plot(lambda x,y: x^2+y^2-2<0, (x,-3,3), (y,-3,3), plot_points=500)\n# looks about like the original, but takes a long time.\n```\n",
    "created_at": "2012-02-24T01:48:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95420",
    "user": "@benjaminfjones"
}
```

I uploaded [attachment:trac_9744_v2.patch] which solves the main problem by calling `region_plot(lambda x,y: f(x,y)<0, ...)` instead of `region_plot(f<0, ...)` 

...but it introduces a strange artefact. Try the following (this doesn't require applying the patch).


```
sage: region_plot(x^2+y^2-2<0, (x,-3,3), (y,-3,3))
# looks normal
sage: region_plot(lambda x,y: x^2+y^2-2<0, (x,-3,3), (y,-3,3))
# looks ragged around the edges
sage: region_plot(lambda x,y: x^2+y^2-2<0, (x,-3,3), (y,-3,3), plot_points=200)
# better, but not great
sage: region_plot(lambda x,y: x^2+y^2-2<0, (x,-3,3), (y,-3,3), plot_points=500)
# looks about like the original, but takes a long time.
```




---

archive/issue_comments_095421.json:
```json
{
    "body": "The following doctest that is currently in `region_plot` has the same artefact:\n\n\n```\nregion_plot(lambda x,y: x^2+y^2<1 or x<y, (x,-2,2), (y,-2,2))\n```\n\n\nI uploaded a new, new patch that only has the artefact when a python function is passed\nto implicit_plot in which case the user should increase the point count appropriately. I\nadded a doctest to that effect as well.\n\nWith the patch applied, compare:\n\n\n```\nsage: x,y=var('x,y')\nsage: implicit_plot(x^2+y^2-2, (x,-3,3), (y,-3,3), fill=True)\nsage: g = lambda x,y: x^2+y^2-2\nsage: implicit_plot(g,  (x,-3,3), (y,-3,3), fill=True)\n```\n",
    "created_at": "2012-02-24T02:14:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95421",
    "user": "@benjaminfjones"
}
```

The following doctest that is currently in `region_plot` has the same artefact:


```
region_plot(lambda x,y: x^2+y^2<1 or x<y, (x,-2,2), (y,-2,2))
```


I uploaded a new, new patch that only has the artefact when a python function is passed
to implicit_plot in which case the user should increase the point count appropriately. I
added a doctest to that effect as well.

With the patch applied, compare:


```
sage: x,y=var('x,y')
sage: implicit_plot(x^2+y^2-2, (x,-3,3), (y,-3,3), fill=True)
sage: g = lambda x,y: x^2+y^2-2
sage: implicit_plot(g,  (x,-3,3), (y,-3,3), fill=True)
```




---

archive/issue_comments_095422.json:
```json
{
    "body": "I'm between classes now, but I'll check it out later.  In the meantime, what is going on with the new code?  When is the last line\n\n```\nreturn contour_plot(f, xrange, yrange, linewidths=linewidths, linestyles=linestyles, **options)\n```\n\never reached?\n\nAlso, \n\n```\nif options.pop('fill'):\n```\n\nwill give a `KeyError` if `'fill'` isn't defined in the options dictionary.  Could that happen?  If so, you may want to take the previous entry\n\n```\nif 'color' in options: \n```\n\nand go from there... this may not be a problem, but it's probably wisest to guard against it.",
    "created_at": "2012-02-24T15:50:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95422",
    "user": "@kcrisman"
}
```

I'm between classes now, but I'll check it out later.  In the meantime, what is going on with the new code?  When is the last line

```
return contour_plot(f, xrange, yrange, linewidths=linewidths, linestyles=linestyles, **options)
```

ever reached?

Also, 

```
if options.pop('fill'):
```

will give a `KeyError` if `'fill'` isn't defined in the options dictionary.  Could that happen?  If so, you may want to take the previous entry

```
if 'color' in options: 
```

and go from there... this may not be a problem, but it's probably wisest to guard against it.



---

archive/issue_comments_095423.json:
```json
{
    "body": "The `if options.pop('fill'):` is okay because of the `@`options decorator before `def implicit_plot(...):`\n\n\n```\n@options(plot_points=150, contours=(0,0), fill=False, cmap=[\"blue\"])\n```\n\n\nYou're correct about that last line, somehow I let that slip through. I updated the patch. I think it's more readable and less redundant now.",
    "created_at": "2012-02-24T18:04:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95423",
    "user": "@benjaminfjones"
}
```

The `if options.pop('fill'):` is okay because of the `@`options decorator before `def implicit_plot(...):`


```
@options(plot_points=150, contours=(0,0), fill=False, cmap=["blue"])
```


You're correct about that last line, somehow I let that slip through. I updated the patch. I think it's more readable and less redundant now.



---

archive/issue_comments_095424.json:
```json
{
    "body": "> The `if options.pop('fill'):` is okay because of the `@`options decorator before `def implicit_plot(...):`\n\nI figured, but was too rushed to check.\n\n\n```\nx,y = var('x,y')\nf(x,y) = x^2 + y^2 - 2\nimplicit_plot(f, (-3, 3), (-3, 3),fill=True).show(aspect_ratio=1)\n```\n\nIt works!\n\nLet me just look at a few more things.  I think I'll want to add something to the other example you give, with the region plot lambda, so that it looks nicer in the doc.\n\n----\n\nI was going to complain about `artefact` but then read [this](http://www.worldwidewords.org/qa/qa-art1.htm).  Harrumph.",
    "created_at": "2012-02-24T20:06:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95424",
    "user": "@kcrisman"
}
```

> The `if options.pop('fill'):` is okay because of the `@`options decorator before `def implicit_plot(...):`

I figured, but was too rushed to check.


```
x,y = var('x,y')
f(x,y) = x^2 + y^2 - 2
implicit_plot(f, (-3, 3), (-3, 3),fill=True).show(aspect_ratio=1)
```

It works!

Let me just look at a few more things.  I think I'll want to add something to the other example you give, with the region plot lambda, so that it looks nicer in the doc.

----

I was going to complain about `artefact` but then read [this](http://www.worldwidewords.org/qa/qa-art1.htm).  Harrumph.



---

archive/issue_comments_095425.json:
```json
{
    "body": "That sounds good. Go ahead and change artefact if you want. I'll admit I'm of the generation whose spelling abilities were destroyed by the spell checker. \n\nI was thinking about opening a new ticket to improve results of region_plot when passing a lambda function, but I don't know enough about why the \"artefacts\" occur. Any thoughts?",
    "created_at": "2012-02-24T20:15:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95425",
    "user": "@benjaminfjones"
}
```

That sounds good. Go ahead and change artefact if you want. I'll admit I'm of the generation whose spelling abilities were destroyed by the spell checker. 

I was thinking about opening a new ticket to improve results of region_plot when passing a lambda function, but I don't know enough about why the "artefacts" occur. Any thoughts?



---

archive/issue_comments_095426.json:
```json
{
    "body": "No, I don't know - I haven't plotted too many lambda functions recently, of course.\n\nI'm going to fix a few other doc things.  One that looks like a change, but isn't, is removing the variable declaration - but this is not needed with `f(x,y)` notation.",
    "created_at": "2012-02-24T21:23:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95426",
    "user": "@kcrisman"
}
```

No, I don't know - I haven't plotted too many lambda functions recently, of course.

I'm going to fix a few other doc things.  One that looks like a change, but isn't, is removing the variable declaration - but this is not needed with `f(x,y)` notation.



---

archive/issue_comments_095427.json:
```json
{
    "body": "Reviewer patch looks good to me. Thanks.",
    "created_at": "2012-02-24T21:30:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95427",
    "user": "@benjaminfjones"
}
```

Reviewer patch looks good to me. Thanks.



---

archive/issue_comments_095428.json:
```json
{
    "body": "Wow, I wasn't even done reviewing my own reviewer patch :)   I got hung up on trying to decide whether to add any more `# long time`s, but decided it wasn't worth it.\n\nThe code currently allows this.  \n\n```\nsage: f(x,y) = x^2 + y^2 - 2\nsage: implicit_plot(f, (-3, 3), (-3, 3),fill='55').show(aspect_ratio=1)  # nice graph is filled\n```\n\nShould we maybe raise an error if this happens?  Given that one can ask for all kinds of fills in regular plots, not just `True` or `False`, perhaps this should be disallowed.",
    "created_at": "2012-02-24T21:39:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95428",
    "user": "@kcrisman"
}
```

Wow, I wasn't even done reviewing my own reviewer patch :)   I got hung up on trying to decide whether to add any more `# long time`s, but decided it wasn't worth it.

The code currently allows this.  

```
sage: f(x,y) = x^2 + y^2 - 2
sage: implicit_plot(f, (-3, 3), (-3, 3),fill='55').show(aspect_ratio=1)  # nice graph is filled
```

Should we maybe raise an error if this happens?  Given that one can ask for all kinds of fills in regular plots, not just `True` or `False`, perhaps this should be disallowed.



---

archive/issue_comments_095429.json:
```json
{
    "body": "Also, it's okay to be a reviewer and an author - you definitely have done both here!",
    "created_at": "2012-02-24T21:40:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95429",
    "user": "@kcrisman"
}
```

Also, it's okay to be a reviewer and an author - you definitely have done both here!



---

archive/issue_comments_095430.json:
```json
{
    "body": "I updated my patch to make the code more readable at the end of `implicit_plot` and to raise an error if fill option is passed and does not equal either `True` or `False`.\n\nThe reviewer patch still applies on top (with a tiny bit of fuzz).",
    "created_at": "2012-02-24T22:25:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95430",
    "user": "@benjaminfjones"
}
```

I updated my patch to make the code more readable at the end of `implicit_plot` and to raise an error if fill option is passed and does not equal either `True` or `False`.

The reviewer patch still applies on top (with a tiny bit of fuzz).



---

archive/issue_comments_095431.json:
```json
{
    "body": "I think you might want to do \n\n```\nif foo is True\n```\n\nnot\n\n```\nif foo == True\n```\n\nfor reasons that escape me right now.",
    "created_at": "2012-02-24T23:33:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95431",
    "user": "@kcrisman"
}
```

I think you might want to do 

```
if foo is True
```

not

```
if foo == True
```

for reasons that escape me right now.



---

archive/issue_comments_095432.json:
```json
{
    "body": "'is' does a pointer comparison, which is much faster and works because True is a singleton.  == does a __eq__ comparison, which is much slower.  When comparing to True, False, or None, you should use 'is' to be much faster.",
    "created_at": "2012-02-24T23:45:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95432",
    "user": "@jasongrout"
}
```

'is' does a pointer comparison, which is much faster and works because True is a singleton.  == does a __eq__ comparison, which is much slower.  When comparing to True, False, or None, you should use 'is' to be much faster.



---

archive/issue_comments_095433.json:
```json
{
    "body": "fixes filled implicit plotting with lambdas",
    "created_at": "2012-02-25T02:28:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95433",
    "user": "@benjaminfjones"
}
```

fixes filled implicit plotting with lambdas



---

archive/issue_comments_095434.json:
```json
{
    "body": "Attachment [trac_9744_v2.patch](tarball://root/attachments/some-uuid/ticket9744/trac_9744_v2.patch) by @benjaminfjones created at 2012-02-25 02:29:30\n\nAh, good point. The new patch should do the job.",
    "created_at": "2012-02-25T02:29:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95434",
    "user": "@benjaminfjones"
}
```

Attachment [trac_9744_v2.patch](tarball://root/attachments/some-uuid/ticket9744/trac_9744_v2.patch) by @benjaminfjones created at 2012-02-25 02:29:30

Ah, good point. The new patch should do the job.



---

archive/issue_comments_095435.json:
```json
{
    "body": "I can't think of any other reasons to hold this up.  I've uploaded a new reviewer patch testing the error raised.  I tested the looks of the implicit plots in schemes and rings, even.  I think we're done here.",
    "created_at": "2012-02-25T04:07:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95435",
    "user": "@kcrisman"
}
```

I can't think of any other reasons to hold this up.  I've uploaded a new reviewer patch testing the error raised.  I tested the looks of the implicit plots in schemes and rings, even.  I think we're done here.



---

archive/issue_comments_095436.json:
```json
{
    "body": "reviewer patch",
    "created_at": "2012-02-25T04:07:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95436",
    "user": "@kcrisman"
}
```

reviewer patch



---

archive/issue_comments_095437.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-02-25T04:09:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95437",
    "user": "@kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095438.json:
```json
{
    "body": "Attachment [trac_9744-reviewer.patch](tarball://root/attachments/some-uuid/ticket9744/trac_9744-reviewer.patch) by @kcrisman created at 2012-02-25 04:09:23",
    "created_at": "2012-02-25T04:09:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95438",
    "user": "@kcrisman"
}
```

Attachment [trac_9744-reviewer.patch](tarball://root/attachments/some-uuid/ticket9744/trac_9744-reviewer.patch) by @kcrisman created at 2012-02-25 04:09:23



---

archive/issue_comments_095439.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-02-27T11:19:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9744",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9744#issuecomment-95439",
    "user": "@jdemeyer"
}
```

Resolution: fixed
