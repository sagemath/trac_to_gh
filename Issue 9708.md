# Issue 9708: mesh= option to plot3d is completely broken?

archive/issues_009708.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @kcrisman @novoselt @kini @gutow\n\nI tried the plot3d example that involves \"mesh=True\" and it is completely broken.  The plot simply doesn't show a mesh at all.\n\n```\nplot3d(sin(x-y)*y*cos(x),(x,-3,3),(y,-3,3), mesh=True)\n```\n\n[This is the Trac macro *a 3d plot, but with no mesh* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#a 3d plot, but with no mesh-macro)\n\nIssue created by migration from https://trac.sagemath.org/ticket/9708\n\n",
    "created_at": "2010-08-08T00:49:42Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "mesh= option to plot3d is completely broken?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9708",
    "user": "https://github.com/williamstein"
}
```
Assignee: jason, was

CC:  @kcrisman @novoselt @kini @gutow

I tried the plot3d example that involves "mesh=True" and it is completely broken.  The plot simply doesn't show a mesh at all.

```
plot3d(sin(x-y)*y*cos(x),(x,-3,3),(y,-3,3), mesh=True)
```

[This is the Trac macro *a 3d plot, but with no mesh* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#a 3d plot, but with no mesh-macro)

Issue created by migration from https://trac.sagemath.org/ticket/9708





---

archive/issue_comments_094463.json:
```json
{
    "body": "Changing keywords from \"\" to \"plot3d mesh\".",
    "created_at": "2012-01-18T02:44:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9708#issuecomment-94463",
    "user": "https://github.com/kini"
}
```

Changing keywords from "" to "plot3d mesh".



---

archive/issue_comments_094464.json:
```json
{
    "body": "See #6184 for a previous fix for this.",
    "created_at": "2012-01-18T04:04:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9708#issuecomment-94464",
    "user": "https://github.com/jasongrout"
}
```

See #6184 for a previous fix for this.



---

archive/issue_comments_094465.json:
```json
{
    "body": "And #2741 originally implemented these options, so it might also contain clues.\n\nAlso CCing Jonathan, who likely knows exactly what the problem is with mesh and dots not working in 3d plots.",
    "created_at": "2012-01-18T04:06:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9708#issuecomment-94465",
    "user": "https://github.com/jasongrout"
}
```

And #2741 originally implemented these options, so it might also contain clues.

Also CCing Jonathan, who likely knows exactly what the problem is with mesh and dots not working in 3d plots.



---

archive/issue_comments_094466.json:
```json
{
    "body": "It looks like the mesh actually works, but the keywords just aren't getting passed to show.  See http://test.sagenb.org/home/pub/25/\n\n`plot3d(f,(x,-3,3),(y,-3,3),mesh=True) ` doesn't work, but `plot3d(f,(x,-3,3),(y,-3,3)).show(mesh=True) ` does work.",
    "created_at": "2012-01-18T06:27:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9708#issuecomment-94466",
    "user": "https://github.com/jasongrout"
}
```

It looks like the mesh actually works, but the keywords just aren't getting passed to show.  See http://test.sagenb.org/home/pub/25/

`plot3d(f,(x,-3,3),(y,-3,3),mesh=True) ` doesn't work, but `plot3d(f,(x,-3,3),(y,-3,3)).show(mesh=True) ` does work.



---

archive/issue_comments_094467.json:
```json
{
    "body": "Good sleuthing.   I feel like we might have even discovered that at the JMM booth.  I wonder why #6184 is no longer sufficient?",
    "created_at": "2012-01-18T13:48:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9708#issuecomment-94467",
    "user": "https://github.com/kcrisman"
}
```

Good sleuthing.   I feel like we might have even discovered that at the JMM booth.  I wonder why #6184 is no longer sufficient?



---

archive/issue_comments_094468.json:
```json
{
    "body": "I don't have much time to look at this now, but it is very mysterious as\u00a0#6184, is definitely still in. Maybe we're not calling show properly after building the data set.",
    "created_at": "2012-01-18T14:34:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9708#issuecomment-94468",
    "user": "https://github.com/gutow"
}
```

I don't have much time to look at this now, but it is very mysterious as #6184, is definitely still in. Maybe we're not calling show properly after building the data set.



---

archive/issue_comments_094469.json:
```json
{
    "body": "This just came up again (see [this interact](http://aleph.sagemath.org/?q=36ba599a-ded6-4afe-97da-2a16b4d166c2), for instance) in the PREP 2012 workshop, as I was trying to help someone set orientation.\n\nRepeating Jason's example from this context,\n\n```\n    p2=plot3d(f(x,y),(x,-5,5),(y,-5,5))\n    show(p2,figsize=3,mesh=True,orientation=(0,0,0,0))\n```\n\nworks, but \n\n```\n    p2=plot3d(f(x,y),(x,-5,5),(y,-5,5),mesh=True,orientation=(0,0,0,0))\n```\n\ndoesn't.  (Doesn't matter what `f` is, pick your favorite.)\n\n#6184 turns out to be a red herring; we are not passing the keywords on, as Jason pointed out.  Hopefully this won't be too hard to fix.",
    "created_at": "2012-06-28T21:02:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9708#issuecomment-94469",
    "user": "https://github.com/kcrisman"
}
```

This just came up again (see [this interact](http://aleph.sagemath.org/?q=36ba599a-ded6-4afe-97da-2a16b4d166c2), for instance) in the PREP 2012 workshop, as I was trying to help someone set orientation.

Repeating Jason's example from this context,

```
    p2=plot3d(f(x,y),(x,-5,5),(y,-5,5))
    show(p2,figsize=3,mesh=True,orientation=(0,0,0,0))
```

works, but 

```
    p2=plot3d(f(x,y),(x,-5,5),(y,-5,5),mesh=True,orientation=(0,0,0,0))
```

doesn't.  (Doesn't matter what `f` is, pick your favorite.)

#6184 turns out to be a red herring; we are not passing the keywords on, as Jason pointed out.  Hopefully this won't be too hard to fix.



---

archive/issue_comments_094470.json:
```json
{
    "body": "Ping.  (Just received the same question on the IRC. ask.sagemath.org gives the work-around though.)",
    "created_at": "2013-06-24T20:23:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9708#issuecomment-94470",
    "user": "https://github.com/nexttime"
}
```

Ping.  (Just received the same question on the IRC. ask.sagemath.org gives the work-around though.)



---

archive/issue_comments_094471.json:
```json
{
    "body": "Okay, I think the problem here is likely to be that in all the 3d plot stuff in `src/sage/plot/plot3d/plot3d.py` usually puts ALL keywords into something like\n\n```\ntexture = Texture(kwds)\n```\n\nand it's never seen again.  But in `src/sage/plot/plot3d/texture.py` the initialization of `Texture_class` (which is called by `Texture`) is\n\n```\n    def __init__(self, id, color=(.4, .4, 1), opacity=1, ambient=0.5, diffuse=1, specular=0, shininess=1, name=None, **kwds):\n```\n\nnever then uses any of the `kwds`.  I can imagine fixing this by *only* allowing \"used\" keywords to be passed on to `Texture` and the rest (somehow) are passed on to `show()`, or by doing something in `Texture_class`.  I would prefer the former.",
    "created_at": "2014-11-06T17:32:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9708#issuecomment-94471",
    "user": "https://github.com/kcrisman"
}
```

Okay, I think the problem here is likely to be that in all the 3d plot stuff in `src/sage/plot/plot3d/plot3d.py` usually puts ALL keywords into something like

```
texture = Texture(kwds)
```

and it's never seen again.  But in `src/sage/plot/plot3d/texture.py` the initialization of `Texture_class` (which is called by `Texture`) is

```
    def __init__(self, id, color=(.4, .4, 1), opacity=1, ambient=0.5, diffuse=1, specular=0, shininess=1, name=None, **kwds):
```

never then uses any of the `kwds`.  I can imagine fixing this by *only* allowing "used" keywords to be passed on to `Texture` and the rest (somehow) are passed on to `show()`, or by doing something in `Texture_class`.  I would prefer the former.
