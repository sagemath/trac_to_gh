# Issue 1606: plotting -- add aspect_ratio option to show command

Issue created by migration from https://trac.sagemath.org/ticket/1606

Original creator: was

Original creation time: 2007-12-27 03:19:48

Assignee: was

> 
> I've been looking for a plot.option that ensures a 1:1 aspect ratio
> for 2D plots (e.g. something like AspectRatio->Automatic in Mma). Does
> this exist in Sage? I'm trying to set things up so that
> 
> circle((0,0),2).show()
> 
> shows a circle rather than an ellipse, regardless of the plot window
> dimensions. Apologies if this has already been covered somewhere.

We should just add
    P.show(aspect_ratio="automatic")
etc., exactly as in Mathematica.  The goal with 2d graphics in Sage
is that they at least support all options that Mathematica has. 

Anyway, here is a function show11 that works exactly like show(...), but
it will always show with a 1:1 aspect ratio:


```
def show11(g, figsize=[5,4], **kwds):
    for k in ['xmin', 'xmax', 'ymin', 'ymax']:
        if kwds.has_key(k): g.__getattribute__(k)(kwds[k])
    scale = (g.xmax() - g.xmin())/(g.ymax() - g.ymin())
    g.show(figsize=[figsize[0], figsize[0]/scale], **kwds)
```



```
show11(plot(sin, 0, 5))
```



```
show11(circle((0,0), 2), xmin=-3, xmax=4)
```


 -- William


---

Comment by was created at 2008-01-19 18:51:48

Changing status from new to assigned.


---

Attachment


---

Comment by was created at 2008-01-19 22:18:47

By the way, I also removed explicit mention of mathematica and matlab in the file, in order to not get in trademark trouble with them. 

The main point about this patch is that the notion of aspect_ratio implemented in it is different than in mathematica.  It is very useful though in practice, and consistent with what we've implemented for 3d graphics.


---

Comment by mhansen created at 2008-01-21 03:23:27

Works for me.


---

Comment by mabshoff created at 2008-01-21 03:25:47

Resolution: fixed


---

Comment by mabshoff created at 2008-01-21 03:25:47

Merged in Sage 2.10.1.alpha1
