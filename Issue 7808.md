# Issue 7808: Plots seem to be shifted up and to the left by one pixel or so

Issue created by migration from https://trac.sagemath.org/ticket/7808

Original creator: jason

Original creation time: 2010-01-01 18:39:13

Assignee: was

There was a thread on sage-devel where it seemed like a number of people felt plots (or axes!) were shifted by about one pixel or so.  Here's one manifestation:


```
region_plot([x^2+y^2<=1, x<=y], (x,-2,2), (y,-2,2),plot_points=400).show(aspect_ratio=1)
```


There are a lot of other examples in a thread on one of the sage mailing lists, but I can't find the thread.


---

Comment by jason created at 2010-06-11 04:48:34

Here is another example which clearly shows something is wrong:


```
bl = disk((0.0,0.0), 1, (pi, 3*pi/2), color='yellow')
tr = disk((0.0,0.0), 1, (0, pi/2), color='yellow')
tl = disk((0.0,0.0), 1, (pi/2, pi), color='black')
br = disk((0.0,0.0), 1, (3*pi/2, 2*pi), color='black')
P  = tl+tr+bl+br
P.show(aspect_ratio=1,xmin=-2,xmax=2,ymin=-2,ymax=2)
```


(from the disk doctests)


---

Comment by jason created at 2010-06-11 04:55:13

Here's an even better illustration. Try changing the dpi:


```
@interact
def show_shift(dpi=(50,150,1)):
    # 50 dpi = shifted left
    # 70 dpi = shifted up
    # 80 dpi = seems perfect
    # 100 dpi = shifted up and left
    # 105 dpi = shifted up
    # 110 dpi = seems perfect
    bl = disk((0.0,0.0), 1, (pi, 3*pi/2), color='yellow')
    tr = disk((0.0,0.0), 1, (0, pi/2), color='yellow')
    tl = disk((0.0,0.0), 1, (pi/2, pi), color='black')
    br = disk((0.0,0.0), 1, (3*pi/2, 2*pi), color='black')
    P  = tl+tr+bl+br
    P.show(figsize=[10,10],dpi=dpi,aspect_ratio=1,xmin=-2,xmax=2,ymin=-2,ymax=2)
```



---

Comment by jason created at 2010-06-11 04:57:33

One more iteration, this time with the option to see the frame:


```
@interact
def show_shift(dpi=(50,150,1),frame=False):
    # 50 dpi = shifted left
    # 70 dpi = shifted up
    # 80 dpi = seems perfect
    # 100 dpi = shifted up and left
    # 105 dpi = shifted up
    # 110 dpi = seems perfect
    # different results if frame is checked
    bl = disk((0.0,0.0), 1, (pi, 3*pi/2), color='yellow')
    tr = disk((0.0,0.0), 1, (0, pi/2), color='yellow')
    tl = disk((0.0,0.0), 1, (pi/2, pi), color='black')
    br = disk((0.0,0.0), 1, (3*pi/2, 2*pi), color='black')
    P  = tl+tr+bl+br
    P.show(figsize=[10,10],dpi=dpi,frame=frame,aspect_ratio=1,xmin=-2,xmax=2,ymin=-2,ymax=2)
```



---

Comment by jason created at 2010-06-11 05:45:51

Actually, the above examples might just be due to the line width (the line around the disk).  Here is an example that again shows something really is wrong:


```
p=line([[-1,0],[1,0]])+line([[0,-1],[0,1]],color='red')+line([[-1,-1],[1,1]],color='yellow')
p.show(figsize=20,dpi=300)
```


Zooming in very closely shows that the red and blue lines are perfect, but the yellow line is shifted up or to the left or both (note the yellow pixels in quadrant 2, but not in quadrant 4).


---

Comment by jason created at 2010-06-11 06:05:09

I posted a message to matplotlib-devel with what I think is a good example illustrating this in straight matplotlib: http://permalink.gmane.org/gmane.comp.python.matplotlib.devel/8664


---

Comment by jason created at 2010-06-11 18:54:37

Changing status from new to needs_info.


---

Attachment

I've attached a patch which is a workaround solving the problem.  However, it causes other side effects (fuzzy lines, since now lines are not snapped to whole-pixels).  You can uncomment the antialiased line in the patch to not get fuzzy lines, but then sometimes one axis will be one pixel wider than the other, which looks bad.  I haven't tested how these options affect vector graphics output (e.g., pdf).

So we have three options:

1. Leave things the way they are
2. Turn off snapping, but deal with possible fuzzy lines
3. Turn off snapping and turn off antialiasing, and deal with axes that sometimes don't match in width.

Pick your poison.


---

Comment by jason created at 2010-06-11 21:05:33

Instead of applying the patch above, you can also do:

1. Install #9208 (to the scripts repository)
2. If you've moved Sage from the build directory, then move it back to the original build location, delete SAGE_ROOT/local/lib/sage-current-location.txt, install #9210, start up and close down Sage, (and then you can move the sage directory back to wherever you had it in step 1).
2. Install the new matplotlib spkg at #9202

Now just type this in a notebook cell:


```
import matplotlib
matplotlib.rcParams['path.snap'] = False
```


Then the plots will go right through the origin.  This is equivalent (better, actually), than the patch above, as it makes *all* horizontal/vertical lines not snap to the nearest pixel.

So now the debate is if we should make path.snap by default False (it is True by default in matplotlib).


---

Comment by jason created at 2010-06-11 21:42:41

The new matplotlib spkg with the path.snap parameter has been moved to #9221


---

Comment by kcrisman created at 2010-06-12 02:25:37

I'm uncomfortable with the following comment in the patch

```
(but drawing another 
 # horizontal/vertical line through the origin may not!) 
```

But would that still be the case for the mpl upgrade piece?  

Otherwise it seems that 2 is the best option.  Axes that don't match is a similarly annoying thing to the moved-over pixel.


---

Comment by jason created at 2010-06-12 02:46:19

Replying to [comment:10 kcrisman]:
> I'm uncomfortable with the following comment in the patch
> {{{
> (but drawing another 
>  # horizontal/vertical line through the origin may not!) 
> }}}
> But would that still be the case for the mpl upgrade piece?  

Setting path.snap to False makes all horizontal/vertical lines do the .set_snap(False) (not just the axes).  So using the rcParam as above would make all horizontal and vertical lines consistent.


> 
> Otherwise it seems that 2 is the best option.  Axes that don't match is a similarly annoying thing to the moved-over pixel.  

In that case, all we have to do is set the matplotlib path.snap config parameter somewhere (either in our code, or provide a default matplotlibrc, or modify the default matplotlibrc in the spkg.

I played a little with Mathematica, and it seems like they have both crisp horizontal lines *and* perfect axes.  I'm not quite sure what they are doing, though.


---

Comment by kcrisman created at 2010-06-12 02:51:51

Well, anyway one would want to have pictures to vote on first :)


---

Comment by kcrisman created at 2010-07-07 14:14:58

Just another note - with respect to #9221 - mpl itself actually even shows this thing, if you look carefully at [this](http://matplotlib.sourceforge.net/plot_directive/mpl_examples/pylab_examples/spine_placement_demo_01.hires.png) picture from one of the latest updates.


---

Comment by kcrisman created at 2010-11-09 01:32:12

Is this now ready for review, with #9221 merged?  Or do we still have to decide on one of 1-3?


---

Comment by jason created at 2010-11-09 01:39:31

Replying to [comment:14 kcrisman]:
> Is this now ready for review, with #9221 merged?  Or do we still have to decide on one of 1-3?

I don't think the patch should be merged.  Instead, a new patch that does this:


```
import matplotlib
matplotlib.rcParams['path.snap'] = False
```


somewhere should be posted.  I think a vote should also be taken on sage-devel with before and after pics.


---

Comment by kcrisman created at 2010-11-09 01:41:02

> I don't think the patch should be merged.  Instead, a new patch that does this:
> 
> {{{
> import matplotlib
> matplotlib.rcParams['path.snap'] = False
> }}}
> 
> somewhere should be posted.  I think a vote should also be taken on sage-devel with before and after pics.

Thanks for volunteering :)  Thankfully, I've not even been taking home a computer that can compile Sage in less than one day home lately.

The reason I thought of this is a recent ask.sagemath.org post.
