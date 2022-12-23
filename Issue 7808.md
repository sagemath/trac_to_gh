# Issue 7808: Plots seem to be shifted up and to the left by one pixel or so

archive/issues_007808.json:
```json
{
    "body": "Assignee: was\n\nThere was a thread on sage-devel where it seemed like a number of people felt plots (or axes!) were shifted by about one pixel or so.  Here's one manifestation:\n\n\n```\nregion_plot([x^2+y^2<=1, x<=y], (x,-2,2), (y,-2,2),plot_points=400).show(aspect_ratio=1)\n```\n\n\nThere are a lot of other examples in a thread on one of the sage mailing lists, but I can't find the thread.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7808\n\n",
    "created_at": "2010-01-01T18:39:13Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "Plots seem to be shifted up and to the left by one pixel or so",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7808",
    "user": "jason"
}
```
Assignee: was

There was a thread on sage-devel where it seemed like a number of people felt plots (or axes!) were shifted by about one pixel or so.  Here's one manifestation:


```
region_plot([x^2+y^2<=1, x<=y], (x,-2,2), (y,-2,2),plot_points=400).show(aspect_ratio=1)
```


There are a lot of other examples in a thread on one of the sage mailing lists, but I can't find the thread.

Issue created by migration from https://trac.sagemath.org/ticket/7808





---

archive/issue_comments_067542.json:
```json
{
    "body": "Here is another example which clearly shows something is wrong:\n\n\n```\nbl = disk((0.0,0.0), 1, (pi, 3*pi/2), color='yellow')\ntr = disk((0.0,0.0), 1, (0, pi/2), color='yellow')\ntl = disk((0.0,0.0), 1, (pi/2, pi), color='black')\nbr = disk((0.0,0.0), 1, (3*pi/2, 2*pi), color='black')\nP  = tl+tr+bl+br\nP.show(aspect_ratio=1,xmin=-2,xmax=2,ymin=-2,ymax=2)\n```\n\n\n(from the disk doctests)",
    "created_at": "2010-06-11T04:48:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7808#issuecomment-67542",
    "user": "jason"
}
```

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

archive/issue_comments_067543.json:
```json
{
    "body": "Here's an even better illustration. Try changing the dpi:\n\n\n```\n@interact\ndef show_shift(dpi=(50,150,1)):\n    # 50 dpi = shifted left\n    # 70 dpi = shifted up\n    # 80 dpi = seems perfect\n    # 100 dpi = shifted up and left\n    # 105 dpi = shifted up\n    # 110 dpi = seems perfect\n    bl = disk((0.0,0.0), 1, (pi, 3*pi/2), color='yellow')\n    tr = disk((0.0,0.0), 1, (0, pi/2), color='yellow')\n    tl = disk((0.0,0.0), 1, (pi/2, pi), color='black')\n    br = disk((0.0,0.0), 1, (3*pi/2, 2*pi), color='black')\n    P  = tl+tr+bl+br\n    P.show(figsize=[10,10],dpi=dpi,aspect_ratio=1,xmin=-2,xmax=2,ymin=-2,ymax=2)\n```\n",
    "created_at": "2010-06-11T04:55:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7808#issuecomment-67543",
    "user": "jason"
}
```

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

archive/issue_comments_067544.json:
```json
{
    "body": "One more iteration, this time with the option to see the frame:\n\n\n```\n@interact\ndef show_shift(dpi=(50,150,1),frame=False):\n    # 50 dpi = shifted left\n    # 70 dpi = shifted up\n    # 80 dpi = seems perfect\n    # 100 dpi = shifted up and left\n    # 105 dpi = shifted up\n    # 110 dpi = seems perfect\n    # different results if frame is checked\n    bl = disk((0.0,0.0), 1, (pi, 3*pi/2), color='yellow')\n    tr = disk((0.0,0.0), 1, (0, pi/2), color='yellow')\n    tl = disk((0.0,0.0), 1, (pi/2, pi), color='black')\n    br = disk((0.0,0.0), 1, (3*pi/2, 2*pi), color='black')\n    P  = tl+tr+bl+br\n    P.show(figsize=[10,10],dpi=dpi,frame=frame,aspect_ratio=1,xmin=-2,xmax=2,ymin=-2,ymax=2)\n```\n",
    "created_at": "2010-06-11T04:57:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7808#issuecomment-67544",
    "user": "jason"
}
```

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

archive/issue_comments_067545.json:
```json
{
    "body": "Actually, the above examples might just be due to the line width (the line around the disk).  Here is an example that again shows something really is wrong:\n\n\n```\np=line([[-1,0],[1,0]])+line([[0,-1],[0,1]],color='red')+line([[-1,-1],[1,1]],color='yellow')\np.show(figsize=20,dpi=300)\n```\n\n\nZooming in very closely shows that the red and blue lines are perfect, but the yellow line is shifted up or to the left or both (note the yellow pixels in quadrant 2, but not in quadrant 4).",
    "created_at": "2010-06-11T05:45:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7808#issuecomment-67545",
    "user": "jason"
}
```

Actually, the above examples might just be due to the line width (the line around the disk).  Here is an example that again shows something really is wrong:


```
p=line([[-1,0],[1,0]])+line([[0,-1],[0,1]],color='red')+line([[-1,-1],[1,1]],color='yellow')
p.show(figsize=20,dpi=300)
```


Zooming in very closely shows that the red and blue lines are perfect, but the yellow line is shifted up or to the left or both (note the yellow pixels in quadrant 2, but not in quadrant 4).



---

archive/issue_comments_067546.json:
```json
{
    "body": "I posted a message to matplotlib-devel with what I think is a good example illustrating this in straight matplotlib: http://permalink.gmane.org/gmane.comp.python.matplotlib.devel/8664",
    "created_at": "2010-06-11T06:05:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7808#issuecomment-67546",
    "user": "jason"
}
```

I posted a message to matplotlib-devel with what I think is a good example illustrating this in straight matplotlib: http://permalink.gmane.org/gmane.comp.python.matplotlib.devel/8664



---

archive/issue_comments_067547.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-06-11T18:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7808#issuecomment-67547",
    "user": "jason"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_067548.json:
```json
{
    "body": "Attachment\n\nI've attached a patch which is a workaround solving the problem.  However, it causes other side effects (fuzzy lines, since now lines are not snapped to whole-pixels).  You can uncomment the antialiased line in the patch to not get fuzzy lines, but then sometimes one axis will be one pixel wider than the other, which looks bad.  I haven't tested how these options affect vector graphics output (e.g., pdf).\n\nSo we have three options:\n\n1. Leave things the way they are\n2. Turn off snapping, but deal with possible fuzzy lines\n3. Turn off snapping and turn off antialiasing, and deal with axes that sometimes don't match in width.\n\nPick your poison.",
    "created_at": "2010-06-11T18:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7808#issuecomment-67548",
    "user": "jason"
}
```

Attachment

I've attached a patch which is a workaround solving the problem.  However, it causes other side effects (fuzzy lines, since now lines are not snapped to whole-pixels).  You can uncomment the antialiased line in the patch to not get fuzzy lines, but then sometimes one axis will be one pixel wider than the other, which looks bad.  I haven't tested how these options affect vector graphics output (e.g., pdf).

So we have three options:

1. Leave things the way they are
2. Turn off snapping, but deal with possible fuzzy lines
3. Turn off snapping and turn off antialiasing, and deal with axes that sometimes don't match in width.

Pick your poison.



---

archive/issue_comments_067549.json:
```json
{
    "body": "Instead of applying the patch above, you can also do:\n\n1. Install #9208 (to the scripts repository)\n2. If you've moved Sage from the build directory, then move it back to the original build location, delete SAGE_ROOT/local/lib/sage-current-location.txt, install #9210, start up and close down Sage, (and then you can move the sage directory back to wherever you had it in step 1).\n2. Install the new matplotlib spkg at #9202\n\nNow just type this in a notebook cell:\n\n\n```\nimport matplotlib\nmatplotlib.rcParams['path.snap'] = False\n```\n\n\nThen the plots will go right through the origin.  This is equivalent (better, actually), than the patch above, as it makes *all* horizontal/vertical lines not snap to the nearest pixel.\n\nSo now the debate is if we should make path.snap by default False (it is True by default in matplotlib).",
    "created_at": "2010-06-11T21:05:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7808#issuecomment-67549",
    "user": "jason"
}
```

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

archive/issue_comments_067550.json:
```json
{
    "body": "The new matplotlib spkg with the path.snap parameter has been moved to #9221",
    "created_at": "2010-06-11T21:42:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7808#issuecomment-67550",
    "user": "jason"
}
```

The new matplotlib spkg with the path.snap parameter has been moved to #9221



---

archive/issue_comments_067551.json:
```json
{
    "body": "I'm uncomfortable with the following comment in the patch\n\n```\n(but drawing another \n # horizontal/vertical line through the origin may not!) \n```\n\nBut would that still be the case for the mpl upgrade piece?  \n\nOtherwise it seems that 2 is the best option.  Axes that don't match is a similarly annoying thing to the moved-over pixel.",
    "created_at": "2010-06-12T02:25:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7808#issuecomment-67551",
    "user": "kcrisman"
}
```

I'm uncomfortable with the following comment in the patch

```
(but drawing another 
 # horizontal/vertical line through the origin may not!) 
```

But would that still be the case for the mpl upgrade piece?  

Otherwise it seems that 2 is the best option.  Axes that don't match is a similarly annoying thing to the moved-over pixel.



---

archive/issue_comments_067552.json:
```json
{
    "body": "Replying to [comment:10 kcrisman]:\n> I'm uncomfortable with the following comment in the patch\n> {{{\n> (but drawing another \n>  # horizontal/vertical line through the origin may not!) \n> }}}\n> But would that still be the case for the mpl upgrade piece?  \n\nSetting path.snap to False makes all horizontal/vertical lines do the .set_snap(False) (not just the axes).  So using the rcParam as above would make all horizontal and vertical lines consistent.\n\n\n> \n> Otherwise it seems that 2 is the best option.  Axes that don't match is a similarly annoying thing to the moved-over pixel.  \n\nIn that case, all we have to do is set the matplotlib path.snap config parameter somewhere (either in our code, or provide a default matplotlibrc, or modify the default matplotlibrc in the spkg.\n\nI played a little with Mathematica, and it seems like they have both crisp horizontal lines *and* perfect axes.  I'm not quite sure what they are doing, though.",
    "created_at": "2010-06-12T02:46:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7808#issuecomment-67552",
    "user": "jason"
}
```

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

archive/issue_comments_067553.json:
```json
{
    "body": "Well, anyway one would want to have pictures to vote on first :)",
    "created_at": "2010-06-12T02:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7808#issuecomment-67553",
    "user": "kcrisman"
}
```

Well, anyway one would want to have pictures to vote on first :)



---

archive/issue_comments_067554.json:
```json
{
    "body": "Just another note - with respect to #9221 - mpl itself actually even shows this thing, if you look carefully at [this](http://matplotlib.sourceforge.net/plot_directive/mpl_examples/pylab_examples/spine_placement_demo_01.hires.png) picture from one of the latest updates.",
    "created_at": "2010-07-07T14:14:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7808#issuecomment-67554",
    "user": "kcrisman"
}
```

Just another note - with respect to #9221 - mpl itself actually even shows this thing, if you look carefully at [this](http://matplotlib.sourceforge.net/plot_directive/mpl_examples/pylab_examples/spine_placement_demo_01.hires.png) picture from one of the latest updates.



---

archive/issue_comments_067555.json:
```json
{
    "body": "Is this now ready for review, with #9221 merged?  Or do we still have to decide on one of 1-3?",
    "created_at": "2010-11-09T01:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7808#issuecomment-67555",
    "user": "kcrisman"
}
```

Is this now ready for review, with #9221 merged?  Or do we still have to decide on one of 1-3?



---

archive/issue_comments_067556.json:
```json
{
    "body": "Replying to [comment:14 kcrisman]:\n> Is this now ready for review, with #9221 merged?  Or do we still have to decide on one of 1-3?\n\nI don't think the patch should be merged.  Instead, a new patch that does this:\n\n\n```\nimport matplotlib\nmatplotlib.rcParams['path.snap'] = False\n```\n\n\nsomewhere should be posted.  I think a vote should also be taken on sage-devel with before and after pics.",
    "created_at": "2010-11-09T01:39:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7808#issuecomment-67556",
    "user": "jason"
}
```

Replying to [comment:14 kcrisman]:
> Is this now ready for review, with #9221 merged?  Or do we still have to decide on one of 1-3?

I don't think the patch should be merged.  Instead, a new patch that does this:


```
import matplotlib
matplotlib.rcParams['path.snap'] = False
```


somewhere should be posted.  I think a vote should also be taken on sage-devel with before and after pics.



---

archive/issue_comments_067557.json:
```json
{
    "body": "> I don't think the patch should be merged.  Instead, a new patch that does this:\n> \n> {{{\n> import matplotlib\n> matplotlib.rcParams['path.snap'] = False\n> }}}\n> \n> somewhere should be posted.  I think a vote should also be taken on sage-devel with before and after pics.\n\nThanks for volunteering :)  Thankfully, I've not even been taking home a computer that can compile Sage in less than one day home lately.\n\nThe reason I thought of this is a recent ask.sagemath.org post.",
    "created_at": "2010-11-09T01:41:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7808",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7808#issuecomment-67557",
    "user": "kcrisman"
}
```

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
