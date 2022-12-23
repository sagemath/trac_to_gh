# Issue 2477: 3d plotting of graphs -- need to force aspect_ratio=[1,1,1] by default (trivial to fix this!)

Issue created by migration from https://trac.sagemath.org/ticket/2477

Original creator: was

Original creation time: 2008-03-11 23:13:24

Assignee: rlm


```
sage: g = graphs.PetersenGraph()
sage: g.plot3d()
[a crappy looking plot]
sage: g = graphs.PetersenGraph()
sage: g.plot3d(aspect_ratio=[1,1,1])
[a much better looking plot]
```



---

Attachment


---

Comment by rlm created at 2008-03-14 14:54:18

This is a different bug, but the funny thing is my experience is

```
sage: g = graphs.PetersenGraph()
sage: g.plot3d()
[a crappy looking plot]
sage: g = graphs.PetersenGraph()
sage: g.plot3d(aspect_ratio=[1,1,1])
[an even crappier looking plot]
```

The new plot has vertices with holes in them. I have no idea what is causing this at all.


---

Comment by jason created at 2008-03-29 20:05:11

I think the patch ought to use:


```
aspect_ratio = kwds.setdefault('aspect_ratio', [1,1,1])
```


or even just


```
kwds.setdefault('aspect_ratio', [1,1,1])
```


which is the python way to do this.


---

Comment by rlm created at 2008-03-29 20:14:44

The reason this ticket wasn't flagged was because setting aspect ratio to 1,1,1 causes the vertices to look very bad on some systems. In order for this to happen, something needs to happen, either in the code for spheres, or the way graphs are calling them. This isn't ready.


---

Comment by jason created at 2008-03-29 20:34:40

The aspect_ratio:

aspect_ratio=[1,1,1.0000001]

works great for me, while the aspect_ratio=[1,1,1] gives the holes.

I'd say just make the aspect ratio the above (which is *really* close to 1,1,1).


---

Comment by rlm created at 2008-03-29 20:52:24

Playing around with this, it doesn't seem very reliable. In fact, the two problems of inconsistent edge thickness and vertex holeyness seem to come and go in loose inverse proportion of each other (although I've seen all holes and all messed up edges and I've seen no holes and no messed up edges too...). Just try fiddling that last parameter around, 1.1, 1.01, 1.00000001, they all come out very different for me (and none of them problem-free!)


---

Comment by jason created at 2008-03-29 21:05:16

I think the issue here is the radius of the vertices (0.06).  We see the same problem with the following:


sphere(center=(-1,0,0),size=.06) + sphere(center=(1,0,0), size=0.06, 
aspect_ratio=[1,1,1])

For me, an alternative to setting the aspect_ratio to [1,1,1.000001] would be setting the radius of the vertices to 0.1 (at least, a radius of 0.1 fixes the holes in the above spheres).


---

Comment by jason created at 2008-03-29 21:08:15

This looks like a jmol issue to me in rendering very small spheres.


---

Comment by jason created at 2008-03-29 21:09:25

This post addresses this exact issue:

http://www.mail-archive.com/jmol-users`@`lists.sourceforge.net/msg07676.html

(and the followup threads)


---

Comment by jason created at 2008-03-29 21:16:45

http://jmol.sourceforge.net/docs/surface/ seems to indicate that the default is resolution 2, if I've read it right.

I'd say we fix this ticket with an aspect_ratio of [1,1,1] and then open another ticket that sets the resolution of sphere.jmol_repr when a small sphere is drawn.


---

Comment by robertwb created at 2008-03-30 00:02:20

See http://trac.sagemath.org/sage_trac/ticket/2729 for the sphere holes issue.


---

Comment by jason created at 2008-03-30 00:42:35

apply instead of the previous patch.


---

Attachment

The patch at 2729 fixes the vertices so they don't look like tinker toys.  The second patch above should be reviewed (it's a simplifications of the first patch).  Apply second patch only (and give rlm credit for the initial version of the patch).


---

Comment by robertwb created at 2008-03-30 00:49:30

Is this only a jmol thing, or should it be applied at a higher level?


---

Comment by rlm created at 2008-03-30 00:51:03

Looks good. Apply after #2279.

This is just a graphs issue, but the issue at #2279 is more applicable to jmol in general.


---

Comment by rlm created at 2008-03-30 00:51:33

Err, #2729.


---

Comment by mabshoff created at 2008-03-31 13:44:28

Merged trac-2477-aspect-ratio.patch in Sage 3.0.alpha0


---

Comment by mabshoff created at 2008-03-31 13:44:28

Resolution: fixed
