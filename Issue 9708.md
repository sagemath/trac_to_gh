# Issue 9708: mesh= option to plot3d is completely broken?

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-08-08 00:49:42

Assignee: jason, was

CC:  kcrisman novoselt kini gutow

I tried the plot3d example that involves "mesh=True" and it is completely broken.  The plot simply doesn't show a mesh at all.

```
plot3d(sin(x-y)*y*cos(x),(x,-3,3),(y,-3,3), mesh=True)
```

[This is the Trac macro *a 3d plot, but with no mesh* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#a 3d plot, but with no mesh-macro)


---

Comment by kini created at 2012-01-18 02:44:12

Changing keywords from "" to "plot3d mesh".


---

Comment by jason created at 2012-01-18 04:04:32

See #6184 for a previous fix for this.


---

Comment by jason created at 2012-01-18 04:06:28

And #2741 originally implemented these options, so it might also contain clues.

Also CCing Jonathan, who likely knows exactly what the problem is with mesh and dots not working in 3d plots.


---

Comment by jason created at 2012-01-18 06:27:09

It looks like the mesh actually works, but the keywords just aren't getting passed to show.  See http://test.sagenb.org/home/pub/25/

`plot3d(f,(x,-3,3),(y,-3,3),mesh=True) ` doesn't work, but `plot3d(f,(x,-3,3),(y,-3,3)).show(mesh=True) ` does work.


---

Comment by kcrisman created at 2012-01-18 13:48:55

Good sleuthing.   I feel like we might have even discovered that at the JMM booth.  I wonder why #6184 is no longer sufficient?


---

Comment by gutow created at 2012-01-18 14:34:51

I don't have much time to look at this now, but it is very mysterious as #6184, is definitely still in. Maybe we're not calling show properly after building the data set.


---

Comment by kcrisman created at 2012-06-28 21:02:27

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

Comment by leif created at 2013-06-24 20:23:25

Ping.  (Just received the same question on the IRC. ask.sagemath.org gives the work-around though.)


---

Comment by kcrisman created at 2014-11-06 17:32:50

Okay, I think the problem here is likely to be that in all the 3d plot stuff in `src/sage/plot/plot3d/plot3d.py` usually puts ALL keywords into something like

```
texture = Texture(kwds)
```

and it's never seen again.  But in `src/sage/plot/plot3d/texture.py` the initialization of `Texture_class` (which is called by `Texture`) is

```
    def __init__(self, id, color=(.4, .4, 1), opacity=1, ambient=0.5, diffuse=1, specular=0, shininess=1, name=None, **kwds):
```

never then uses any of the `kwds`.  I can imagine fixing this by _only_ allowing "used" keywords to be passed on to `Texture` and the rest (somehow) are passed on to `show()`, or by doing something in `Texture_class`.  I would prefer the former.
