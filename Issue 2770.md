# Issue 2770: plot_region function

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-04-02 07:49:40

Assignee: was

It would be great to have a plot_region function which would plot a region where a system of equations/inequalities were true.

Here is an initial version:


```
def plot_region(funcs, var1_range, var2_range, plot_points=400, **kwds):
    if not isinstance(funcs, (list, tuple)):
        funcs = [funcs]
    hvar, hmin, hmax = var1_range
    vvar, vmin, vmax = var2_range
    funcs = prod([f._fast_float_("%r"%hvar, "%r"%vvar) for f in funcs])
    return contour_plot(funcs, var1_range, var2_range, plot_points=plot_points,**kwds)
```


This uses an idea from cwitty (to use contour_plot) and the patch from #2768.  A screenshot is attached below.


---

Comment by abergeron created at 2008-12-28 01:11:27

Changing assignee from was to abergeron.


---

Attachment

If you want to try out part1, you need to apply the patch at #4884.  At the moment it support only one function.

Multiple function support is coming in part2.


---

Comment by abergeron created at 2008-12-28 20:47:42

Changing status from new to assigned.


---

Attachment

Now it is complete, apply both patches and the patch at #4884 to test.

The example in the screenshot should work, but is rather ugly at the default plot_points setting, try at plot_points=200 to see it looking good.


---

Comment by abergeron created at 2008-12-29 20:50:29

Since there is heavy discussion at #4884 I will wait until that settles to update this patch to work with whatever is decided upon.


---

Comment by abergeron created at 2008-12-30 01:51:27

#4884 is settled


---

Comment by wdj created at 2008-12-30 05:22:58

This has some odd behavior which I hope the author could please comment on:

This looks good:

```
sage: P1 = region_plot(cos(x^2+y^2) <= 0, (-3, 3), (-3, 3), incol='green', bordercol='red')
sage: show(P1)
```


This looks very odd (wrong but maybe the algorithm just needs more points?):

```
sage: P2 = region_plot(cos(x^2+y^2) <= 0, (-30, 30), (-30, 30), incol='green', bordercol='red')
sage: show(P2)
```


This looks plain wrong (and I think we have provided enough points:-):


```
sage: P3 = region_plot(cos(x^2+y^2) <= 0, (-30, 30), (-30, 30), incol='green', bordercol='red', plot_points=1000)
sage: show(P3)
```



---

Comment by wdj created at 2008-12-30 05:24:40

Means to add to the review above:

If you first apply the first patch at #4884 (but not the second), then the two patches above apply cleanly to 3.2.2.


---

Comment by abergeron created at 2008-12-30 05:57:42

The first very wrong case is really because there is not enough data to interpolate properly.

In the second case it's too much of a good thing.  There is too much data and every insignificant contour line gets plotted and since they have a minimum width you get a red picture.

For this example, plot_points=400 looks much more reasonable.


---

Comment by wdj created at 2008-12-30 06:52:39

Okay, thanks for that explanation. This is a useful patch.

My impression is that if it can't be easily fixed, then at least it should be documented how to adjust the parameters to get proper behaviour. I'm guessing that the people who will use this patch are students and teachers, so the more detailed examples the better:-) Does this seem reasonable?

With that's I'd be prepared to give it a positive review.

Other cool examples you could include:

```
sage: region_plot(x*(x-1)*(x+1)+y^2<0, (-3, 2), (-3, 3), incol='lightblue', bordercol='gray', plot_points=400)
sage: region_plot([x*(x-1)*(x+1)+y^2<0, x>-1], (-3, 2), (-3, 3), incol='lightblue', bordercol='gray', plot_points=400)
```

And one similar to Jason's:

```
sage: P = region_plot([x^2+y^2<4, x>-1], (-2, 2), (-2, 2), incol='lightblue', bordercol='gray', plot_points=400)
sage: P.show(aspect_ratio=1)
```

(I know you have 


```
region_plot([x^2+y^2<1, x<y], (-2,2), (-2,2)) 
```

but it looks odd without the aspect ratio set.)

Do these seem reasonable Arnaud?


---

Attachment


---

Comment by abergeron created at 2008-12-30 19:17:36

I agree with more examples.  I just did not have a huge inspiration for them.

The last patch adds your suggested examples.


---

Comment by wdj created at 2008-12-30 23:18:32

The patches applied fine but the test timed out on my machine (amd64 ubuntu 8.10). So, positive review for the patch but I could not do the test using sage -t. (The examples seemed to work okay though.)


---

Comment by mabshoff created at 2009-01-12 01:59:58

This is a slightly rebased version of Arnaud Bergeron's patch


---

Comment by mabshoff created at 2009-01-12 02:00:26

Resolution: fixed


---

Attachment

Merged all three patches in Sage 3.3.alpha0
