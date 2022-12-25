# Issue 5448: [with patch, not ready for review] rework save/show in plot, use Matplotlib's axes code

archive/issues_005448.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  wcauchois @kcrisman\n\nThis removes the axes.py code from Sage and switches to Matplotlib's code.  This allows for things like log scales as well as more flexibility in controlling how the ticks are labeled formatted.  It also fixes a number of existing bugs (like 2754).  After this change, it will be trivial to add a viewer='flot' option to Graphics.\n\nThe patch still needs some work a.k.a. doctests.  There are also a few things that don't work yet (like tick color and tick fontsize), and matrix_plot needs a matplotlib Locater and Formatter.  Also, GraphicsArray needs to be updated and should get lots of doctests for it added.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5448\n\n",
    "created_at": "2009-03-06T03:38:48Z",
    "labels": [
        "component: graphics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, not ready for review] rework save/show in plot, use Matplotlib's axes code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5448",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @williamstein

CC:  wcauchois @kcrisman

This removes the axes.py code from Sage and switches to Matplotlib's code.  This allows for things like log scales as well as more flexibility in controlling how the ticks are labeled formatted.  It also fixes a number of existing bugs (like 2754).  After this change, it will be trivial to add a viewer='flot' option to Graphics.

The patch still needs some work a.k.a. doctests.  There are also a few things that don't work yet (like tick color and tick fontsize), and matrix_plot needs a matplotlib Locater and Formatter.  Also, GraphicsArray needs to be updated and should get lots of doctests for it added.

Issue created by migration from https://trac.sagemath.org/ticket/5448





---

archive/issue_comments_042051.json:
```json
{
    "body": "Attachment [plot.patch](tarball://root/attachments/some-uuid/ticket5448/plot.patch) by @mwhansen created at 2009-03-06 03:39:15",
    "created_at": "2009-03-06T03:39:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42051",
    "user": "https://github.com/mwhansen"
}
```

Attachment [plot.patch](tarball://root/attachments/some-uuid/ticket5448/plot.patch) by @mwhansen created at 2009-03-06 03:39:15



---

archive/issue_comments_042052.json:
```json
{
    "body": "mhansen: are you still working on this, or are you posting it in hopes that someone else will work on it?",
    "created_at": "2009-03-06T21:31:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42052",
    "user": "https://github.com/jasongrout"
}
```

mhansen: are you still working on this, or are you posting it in hopes that someone else will work on it?



---

archive/issue_comments_042053.json:
```json
{
    "body": "I was planning on finishing this up in the near future.  I posted it because I wanted to see what all I had left to do and possibly to get feedback from others.",
    "created_at": "2009-03-07T19:21:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42053",
    "user": "https://github.com/mwhansen"
}
```

I was planning on finishing this up in the near future.  I posted it because I wanted to see what all I had left to do and possibly to get feedback from others.



---

archive/issue_comments_042054.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-07T19:21:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42054",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_042055.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2009-03-07T19:21:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42055",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_042056.json:
```json
{
    "body": "Here's another project that provides nice axes functionality for matplotlib, for reference:\n\nhttp://sourceforge.net/mailarchive/forum.php?thread_name=6e8d907b0903252232u66427cd5obbd78867424e2651%40mail.gmail.com&forum_name=matplotlib-devel",
    "created_at": "2009-03-27T04:17:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42056",
    "user": "https://github.com/jasongrout"
}
```

Here's another project that provides nice axes functionality for matplotlib, for reference:

http://sourceforge.net/mailarchive/forum.php?thread_name=6e8d907b0903252232u66427cd5obbd78867424e2651%40mail.gmail.com&forum_name=matplotlib-devel



---

archive/issue_comments_042057.json:
```json
{
    "body": "Just a very naive question: It seems like a lot of work to include Matplotlib's functionality in plot(). Wouldn't it be easier to just transfer the list of values generated by plot() to Matplotlib? Then, the rest could be done with the conventional Matplotlib commands. So far, I have been able to do everything I wanted using Matplotlib, the only impasse being the generation of points to plot, which I believe is solved in plot() a lot more elegantly than just evaluating a number of equidistant points. I apologise in advance for my ignorance.",
    "created_at": "2009-06-26T13:29:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42057",
    "user": "https://trac.sagemath.org/admin/accounts/users/schymans"
}
```

Just a very naive question: It seems like a lot of work to include Matplotlib's functionality in plot(). Wouldn't it be easier to just transfer the list of values generated by plot() to Matplotlib? Then, the rest could be done with the conventional Matplotlib commands. So far, I have been able to do everything I wanted using Matplotlib, the only impasse being the generation of points to plot, which I believe is solved in plot() a lot more elegantly than just evaluating a number of equidistant points. I apologise in advance for my ignorance.



---

archive/issue_comments_042058.json:
```json
{
    "body": "PLEASE KEEP MIKE'S PATCH ATTACHED TO THIS TICKET FOR NOW\n\n(I think he might have some more elegant ways of doing things than I did, which I'd like to copy to my patch).\nThe trac-5448-matplotlib-axes-gridlines.patch requires the new matplotlib spkg at http://sage.math.washington.edu/home/jason/matplotlib-0.99.0.spkg\n\nPlease give feedback!",
    "created_at": "2009-08-19T07:20:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42058",
    "user": "https://github.com/jasongrout"
}
```

PLEASE KEEP MIKE'S PATCH ATTACHED TO THIS TICKET FOR NOW

(I think he might have some more elegant ways of doing things than I did, which I'd like to copy to my patch).
The trac-5448-matplotlib-axes-gridlines.patch requires the new matplotlib spkg at http://sage.math.washington.edu/home/jason/matplotlib-0.99.0.spkg

Please give feedback!



---

archive/issue_comments_042059.json:
```json
{
    "body": "Here is the old description (applicable to Mike's patch, and some of which may be applicable to my patch): \n\nThis removes the axes.py code from Sage and switches to Matplotlib's code.  This allows for things like log scales as well as more flexibility in controlling how the ticks are labeled formatted.  It also fixes a number of existing bugs (like 2754).  After this change, it will be trivial to add a viewer='flot' option to Graphics.\n\nThe patch still needs some work a.k.a. doctests.  There are also a few things that don't work yet (like tick color and tick fontsize), and matrix_plot needs a matplotlib Locater and Formatter.  Also, GraphicsArray needs to be updated and should get lots of doctests for it added.",
    "created_at": "2009-08-19T07:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42059",
    "user": "https://github.com/jasongrout"
}
```

Here is the old description (applicable to Mike's patch, and some of which may be applicable to my patch): 

This removes the axes.py code from Sage and switches to Matplotlib's code.  This allows for things like log scales as well as more flexibility in controlling how the ticks are labeled formatted.  It also fixes a number of existing bugs (like 2754).  After this change, it will be trivial to add a viewer='flot' option to Graphics.

The patch still needs some work a.k.a. doctests.  There are also a few things that don't work yet (like tick color and tick fontsize), and matrix_plot needs a matplotlib Locater and Formatter.  Also, GraphicsArray needs to be updated and should get lots of doctests for it added.



---

archive/issue_comments_042060.json:
```json
{
    "body": "Just a question to Jason - will this break any currently existing code that has rgbcolor instead of color in use?  I assume not but thought I would ask - ditto for any other options for plot or show that would be deprecated?",
    "created_at": "2009-08-20T16:50:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42060",
    "user": "https://github.com/kcrisman"
}
```

Just a question to Jason - will this break any currently existing code that has rgbcolor instead of color in use?  I assume not but thought I would ask - ditto for any other options for plot or show that would be deprecated?



---

archive/issue_comments_042061.json:
```json
{
    "body": "Replying to [comment:8 kcrisman]:\n> Just a question to Jason - will this break any currently existing code that has rgbcolor instead of color in use?  I assume not but thought I would ask - ditto for any other options for plot or show that would be deprecated?  \n\n\nI think the only code it might break is the use of rgbcolor in gridline styles, which according to the docs, should not have been allowed anyway (matplotlib lines do not have an rgbcolor option).  For everything else, I've been careful to doctest everything in plot.py, and all tests pass.",
    "created_at": "2009-08-20T17:01:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42061",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:8 kcrisman]:
> Just a question to Jason - will this break any currently existing code that has rgbcolor instead of color in use?  I assume not but thought I would ask - ditto for any other options for plot or show that would be deprecated?  


I think the only code it might break is the use of rgbcolor in gridline styles, which according to the docs, should not have been allowed anyway (matplotlib lines do not have an rgbcolor option).  For everything else, I've been careful to doctest everything in plot.py, and all tests pass.



---

archive/issue_comments_042062.json:
```json
{
    "body": "Okay, first off patch needs work if only because it does not apply to 4.1.1!  Fix is to correct all spellings of \"apect\" in the patch to \"aspect\" and to replace one instance of \"png's\" at the end to \"PNG's\".  Also, eventually presumably axes.py should go to dev/null, right?  I also get a bunch of deprecation warnings, but presumably that is known.\n\nAs to the stuff itself: \n\n1. When using pointsize, matplotlib axes (or the way in which they are used) has some whitespace cutting off points, for example when pointsize is large (20 worked for me, but unfortunately I can't cut and paste and example here).\n\n2. I'm not sure I like the non-intersecting axes on regular plots.  That is weird, especially in graphs like the plot of x squared type things.  plot(x**2,0,1) looks great; plot(x**2,-1,1) looks... interesting.\n\n3. For some reasons, showing some plots yields the #5956 ValueError of \"ValueError: width and height must each be below 32768\" which apparently comes from matplotlib/backends/backend_agg.py, the RendererAgg (whatever that is).  I should point out these are plots which worked before.  Apparently it has something to do with adding axes_labels, because without them, this problem does not appear.  Did something get a LOT bigger on the axis labels?\n\n4. The two zeros where axes intersect is distracting.  I'm not sure what else to say about that, other than that it's true.  This is especially true when the graph gets close to the origin.  Of course, the reason for labeling it has been discussed elsewhere - it just may have to get \"smart\".  Maybe when the origin IS the intersection point of the axes (as one might expect), this could be tacitly omitted?\n\n5. For some reason William's example in some talk where he does a little eye candy with image manipulation (e.g., \"compressed using x eigenvalues\") doesn't work right; only the second matrix_plot works properly, the other one does not.  So something with the new axes and frame isn't working right.\n\n6. Ironically, switching slope fields to normal (not frame) axes is worse, because it's hard to see the numbers with any reasonably density of the points for the slopes.\n\n7. This is just a question: is it possible to get custom labeling for axis numbering now in matrix plots?  E.g., (!) if I am taking just the 4th-6th powers of some numbers and plotting them in a grid, can I label those columns as 4-6?  I don't know if mpl has this; the axes_grid thing on the website looked conceivably related, maybe even good for matrix_plot or multiple graphics.\n\nBut great work notwithstanding!  Looking forward to whatever comes out of this ticket, and the mpl upgrade seems nice.",
    "created_at": "2009-08-26T02:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42062",
    "user": "https://github.com/kcrisman"
}
```

Okay, first off patch needs work if only because it does not apply to 4.1.1!  Fix is to correct all spellings of "apect" in the patch to "aspect" and to replace one instance of "png's" at the end to "PNG's".  Also, eventually presumably axes.py should go to dev/null, right?  I also get a bunch of deprecation warnings, but presumably that is known.

As to the stuff itself: 

1. When using pointsize, matplotlib axes (or the way in which they are used) has some whitespace cutting off points, for example when pointsize is large (20 worked for me, but unfortunately I can't cut and paste and example here).

2. I'm not sure I like the non-intersecting axes on regular plots.  That is weird, especially in graphs like the plot of x squared type things.  plot(x**2,0,1) looks great; plot(x**2,-1,1) looks... interesting.

3. For some reasons, showing some plots yields the #5956 ValueError of "ValueError: width and height must each be below 32768" which apparently comes from matplotlib/backends/backend_agg.py, the RendererAgg (whatever that is).  I should point out these are plots which worked before.  Apparently it has something to do with adding axes_labels, because without them, this problem does not appear.  Did something get a LOT bigger on the axis labels?

4. The two zeros where axes intersect is distracting.  I'm not sure what else to say about that, other than that it's true.  This is especially true when the graph gets close to the origin.  Of course, the reason for labeling it has been discussed elsewhere - it just may have to get "smart".  Maybe when the origin IS the intersection point of the axes (as one might expect), this could be tacitly omitted?

5. For some reason William's example in some talk where he does a little eye candy with image manipulation (e.g., "compressed using x eigenvalues") doesn't work right; only the second matrix_plot works properly, the other one does not.  So something with the new axes and frame isn't working right.

6. Ironically, switching slope fields to normal (not frame) axes is worse, because it's hard to see the numbers with any reasonably density of the points for the slopes.

7. This is just a question: is it possible to get custom labeling for axis numbering now in matrix plots?  E.g., (!) if I am taking just the 4th-6th powers of some numbers and plotting them in a grid, can I label those columns as 4-6?  I don't know if mpl has this; the axes_grid thing on the website looked conceivably related, maybe even good for matrix_plot or multiple graphics.

But great work notwithstanding!  Looking forward to whatever comes out of this ticket, and the mpl upgrade seems nice.



---

archive/issue_comments_042063.json:
```json
{
    "body": "Thanks for looking at this!  I haven't had time to come back to it yet (our semester started...)\n\nReplying to [comment:10 kcrisman]:\n> 1. When using pointsize, matplotlib axes (or the way in which they are used) has some whitespace cutting off points, for example when pointsize is large (20 worked for me, but unfortunately I can't cut and paste and example here).\n\nOn the one hand, I can turn off clipping.  However, that tends to make really ugly plots when you have frame axes (since then the dots go outside of the frames).  On the other hand, we can automatically enlarge the plot axes (so that if you request -3..3, it might actually cover -3.5..3.5).  This could be frustrating, but is sort of what happens now.  I guess you have to make a choice between things extending beyond your plot (no clipping) or extending your plot.  For right now, I was hoping that people would just make their ranges a bit bigger by hand.\n\n\n\n> \n> 2. I'm not sure I like the non-intersecting axes on regular plots.  That is weird, especially in graphs like the plot of x squared type things.  plot(x**2,0,1) looks great; plot(x**2,-1,1) looks... interesting.\n\nYeah, it's a bit different, but after playing with it for a while, I liked it.  At a glance, it oriented me to what I was looking at and how it was compared to the infinite plane.  This is definitely something that should go up for a vote.\n\nAlso, I'd like to add an option for a custom crossing point.  That would be another 5 lines of code, maybe.\n\n\n\n> \n> 3. For some reasons, showing some plots yields the #5956 ValueError of \"ValueError: width and height must each be below 32768\" which apparently comes from matplotlib/backends/backend_agg.py, the RendererAgg (whatever that is).  I should point out these are plots which worked before.  Apparently it has something to do with adding axes_labels, because without them, this problem does not appear.  Did something get a LOT bigger on the axis labels?\n\n\nFor right now, I automatically expand things to not clip axes labels.  There might be a bug in that.  Can you post an example?\n\n\n\n> \n> 4. The two zeros where axes intersect is distracting.  I'm not sure what else to say about that, other than that it's true.  This is especially true when the graph gets close to the origin.  Of course, the reason for labeling it has been discussed elsewhere - it just may have to get \"smart\".  Maybe when the origin IS the intersection point of the axes (as one might expect), this could be tacitly omitted?\n\nIt would be easy to omit one or both of these zeros in these cases.\n\n\n> \n> 5. For some reason William's example in some talk where he does a little eye candy with image manipulation (e.g., \"compressed using x eigenvalues\") doesn't work right; only the second matrix_plot works properly, the other one does not.  So something with the new axes and frame isn't working right.\n\nOkay, I'll try to look at this.\n\n\n\n> \n> 6. Ironically, switching slope fields to normal (not frame) axes is worse, because it's hard to see the numbers with any reasonably density of the points for the slopes.\n\n\nand your proposed fix is...?\n\n\n> \n> 7. This is just a question: is it possible to get custom labeling for axis numbering now in matrix plots?  E.g., (!) if I am taking just the 4th-6th powers of some numbers and plotting them in a grid, can I label those columns as 4-6?  I don't know if mpl has this; the axes_grid thing on the website looked conceivably related, maybe even good for matrix_plot or multiple graphics.\n\n\nTotally easy.  You have the full power of matplotlib at your command.  You just do something like:\n\np=plot(m).matplotlib()\n# p is now a matplotlib figure object\n\nNow just do custom axes locators for axes in p, like in http://matplotlib.sourceforge.net/examples/pylab_examples/custom_ticker1.html\n\nWhen you are done, just do:\n\np.save_fig('test.png') # or something like this\n\nor (with another change that should be coming soon, now that I understand matplotlib a lot better):\n\nGraphics(p) # This is now a sage Graphics object...",
    "created_at": "2009-08-26T03:18:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42063",
    "user": "https://github.com/jasongrout"
}
```

Thanks for looking at this!  I haven't had time to come back to it yet (our semester started...)

Replying to [comment:10 kcrisman]:
> 1. When using pointsize, matplotlib axes (or the way in which they are used) has some whitespace cutting off points, for example when pointsize is large (20 worked for me, but unfortunately I can't cut and paste and example here).

On the one hand, I can turn off clipping.  However, that tends to make really ugly plots when you have frame axes (since then the dots go outside of the frames).  On the other hand, we can automatically enlarge the plot axes (so that if you request -3..3, it might actually cover -3.5..3.5).  This could be frustrating, but is sort of what happens now.  I guess you have to make a choice between things extending beyond your plot (no clipping) or extending your plot.  For right now, I was hoping that people would just make their ranges a bit bigger by hand.



> 
> 2. I'm not sure I like the non-intersecting axes on regular plots.  That is weird, especially in graphs like the plot of x squared type things.  plot(x**2,0,1) looks great; plot(x**2,-1,1) looks... interesting.

Yeah, it's a bit different, but after playing with it for a while, I liked it.  At a glance, it oriented me to what I was looking at and how it was compared to the infinite plane.  This is definitely something that should go up for a vote.

Also, I'd like to add an option for a custom crossing point.  That would be another 5 lines of code, maybe.



> 
> 3. For some reasons, showing some plots yields the #5956 ValueError of "ValueError: width and height must each be below 32768" which apparently comes from matplotlib/backends/backend_agg.py, the RendererAgg (whatever that is).  I should point out these are plots which worked before.  Apparently it has something to do with adding axes_labels, because without them, this problem does not appear.  Did something get a LOT bigger on the axis labels?


For right now, I automatically expand things to not clip axes labels.  There might be a bug in that.  Can you post an example?



> 
> 4. The two zeros where axes intersect is distracting.  I'm not sure what else to say about that, other than that it's true.  This is especially true when the graph gets close to the origin.  Of course, the reason for labeling it has been discussed elsewhere - it just may have to get "smart".  Maybe when the origin IS the intersection point of the axes (as one might expect), this could be tacitly omitted?

It would be easy to omit one or both of these zeros in these cases.


> 
> 5. For some reason William's example in some talk where he does a little eye candy with image manipulation (e.g., "compressed using x eigenvalues") doesn't work right; only the second matrix_plot works properly, the other one does not.  So something with the new axes and frame isn't working right.

Okay, I'll try to look at this.



> 
> 6. Ironically, switching slope fields to normal (not frame) axes is worse, because it's hard to see the numbers with any reasonably density of the points for the slopes.


and your proposed fix is...?


> 
> 7. This is just a question: is it possible to get custom labeling for axis numbering now in matrix plots?  E.g., (!) if I am taking just the 4th-6th powers of some numbers and plotting them in a grid, can I label those columns as 4-6?  I don't know if mpl has this; the axes_grid thing on the website looked conceivably related, maybe even good for matrix_plot or multiple graphics.


Totally easy.  You have the full power of matplotlib at your command.  You just do something like:

p=plot(m).matplotlib()
# p is now a matplotlib figure object

Now just do custom axes locators for axes in p, like in http://matplotlib.sourceforge.net/examples/pylab_examples/custom_ticker1.html

When you are done, just do:

p.save_fig('test.png') # or something like this

or (with another change that should be coming soon, now that I understand matplotlib a lot better):

Graphics(p) # This is now a sage Graphics object...



---

archive/issue_comments_042064.json:
```json
{
    "body": "Replying to [comment:11 jason]:\n> Thanks for looking at this!  I haven't had time to come back to it yet (our semester started...)\n> \n> Replying to [comment:10 kcrisman]:\n> > 1. When using pointsize, matplotlib axes (or the way in which they are used) has some whitespace cutting off points, for example when pointsize is large (20 worked for me, but unfortunately I can't cut and paste and example here).\n> \n> On the one hand, I can turn off clipping.  However, that tends to make really ugly plots when you have frame axes (since then the dots go outside of the frames).  On the other hand, we can automatically enlarge the plot axes (so that if you request -3..3, it might actually cover -3.5..3.5).  This could be frustrating, but is sort of what happens now.  I guess you have to make a choice between things extending beyond your plot (no clipping) or extending your plot.  For right now, I was hoping that people would just make their ranges a bit bigger by hand.\n\nDefinitely should be automatic, I think, if it's already-existing behavior.  \n> \n> \n> \n> > \n> > 2. I'm not sure I like the non-intersecting axes on regular plots.  That is weird, especially in graphs like the plot of x squared type things.  plot(x**2,0,1) looks great; plot(x**2,-1,1) looks... interesting.\n> \n> Yeah, it's a bit different, but after playing with it for a while, I liked it.  At a glance, it oriented me to what I was looking at and how it was compared to the infinite plane.  This is definitely something that should go up for a vote.\n\nI'm not sure what you are looking at.  The axes do not actually cross!  That is bad, imho.\n> \n> Also, I'd like to add an option for a custom crossing point.  That would be another 5 lines of code, maybe.\n> \n\nYeah, that would be good, though hopefully not often needed.\n\n> \n> \n> > \n> > 4. The two zeros where axes intersect is distracting.  I'm not sure what else to say about that, other than that it's true.  This is especially true when the graph gets close to the origin.  Of course, the reason for labeling it has been discussed elsewhere - it just may have to get \"smart\".  Maybe when the origin IS the intersection point of the axes (as one might expect), this could be tacitly omitted?\n> \n> It would be easy to omit one or both of these zeros in these cases.\n> \n\nSomething to think about.  Presumably the other labels would make it clear it's a zero.\n \n> > \n> > 6. Ironically, switching slope fields to normal (not frame) axes is worse, because it's hard to see the numbers with any reasonably density of the points for the slopes.\n> \n> \n> and your proposed fix is...?\n> \n\nUsing frames again for slope fields (the previous behavior).",
    "created_at": "2009-08-26T12:13:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42064",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:11 jason]:
> Thanks for looking at this!  I haven't had time to come back to it yet (our semester started...)
> 
> Replying to [comment:10 kcrisman]:
> > 1. When using pointsize, matplotlib axes (or the way in which they are used) has some whitespace cutting off points, for example when pointsize is large (20 worked for me, but unfortunately I can't cut and paste and example here).
> 
> On the one hand, I can turn off clipping.  However, that tends to make really ugly plots when you have frame axes (since then the dots go outside of the frames).  On the other hand, we can automatically enlarge the plot axes (so that if you request -3..3, it might actually cover -3.5..3.5).  This could be frustrating, but is sort of what happens now.  I guess you have to make a choice between things extending beyond your plot (no clipping) or extending your plot.  For right now, I was hoping that people would just make their ranges a bit bigger by hand.

Definitely should be automatic, I think, if it's already-existing behavior.  
> 
> 
> 
> > 
> > 2. I'm not sure I like the non-intersecting axes on regular plots.  That is weird, especially in graphs like the plot of x squared type things.  plot(x**2,0,1) looks great; plot(x**2,-1,1) looks... interesting.
> 
> Yeah, it's a bit different, but after playing with it for a while, I liked it.  At a glance, it oriented me to what I was looking at and how it was compared to the infinite plane.  This is definitely something that should go up for a vote.

I'm not sure what you are looking at.  The axes do not actually cross!  That is bad, imho.
> 
> Also, I'd like to add an option for a custom crossing point.  That would be another 5 lines of code, maybe.
> 

Yeah, that would be good, though hopefully not often needed.

> 
> 
> > 
> > 4. The two zeros where axes intersect is distracting.  I'm not sure what else to say about that, other than that it's true.  This is especially true when the graph gets close to the origin.  Of course, the reason for labeling it has been discussed elsewhere - it just may have to get "smart".  Maybe when the origin IS the intersection point of the axes (as one might expect), this could be tacitly omitted?
> 
> It would be easy to omit one or both of these zeros in these cases.
> 

Something to think about.  Presumably the other labels would make it clear it's a zero.
 
> > 
> > 6. Ironically, switching slope fields to normal (not frame) axes is worse, because it's hard to see the numbers with any reasonably density of the points for the slopes.
> 
> 
> and your proposed fix is...?
> 

Using frames again for slope fields (the previous behavior).



---

archive/issue_comments_042065.json:
```json
{
    "body": "Replying to [comment:11 jason]:\n> > 3. For some reasons, showing some plots yields the #5956 ValueError of \"ValueError: width and height must each be below 32768\" which apparently comes from matplotlib/backends/backend_agg.py, the RendererAgg (whatever that is).  I should point out these are plots which worked before.  Apparently it has something to do with adding axes_labels, because without them, this problem does not appear.  Did something get a LOT bigger on the axis labels?\n> \n> \n> For right now, I automatically expand things to not clip axes labels.  There might be a bug in that.  Can you post an example?\n>\n\nIt appears to have something to do with where the labels are located. \n\n```\nsage: plot(x**2,0,1,axes_labels=['x','y'])\n```\n\nis fine, but \n\n```\nsage: plot(x**2,99,100,axes_labels=['x','y'])\n```\n\nyields the problem.  This also happens with point sets:\n\n\n```\nsage: data=[(1990,1611),(1991,1586)]\nsage: plot1=point(data)\nsage: show(plot1,axes_labels=['x','y'])\n```\n\n\nBack to the other issues, note that while the following does plot\n\n```\nsage: show(plot1)\n```\n\nit also is not ideal, as the axes don't even come close to touching.  By the way, the pointsize is irrelevant - even with no pointsize given, the points are still cut off.  Also, there is a mysterious cut-off thing at the bottom which look like +1.00e3, but it's cut off so I can't tell for sure.  Any ideas on that?",
    "created_at": "2009-08-26T13:02:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42065",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:11 jason]:
> > 3. For some reasons, showing some plots yields the #5956 ValueError of "ValueError: width and height must each be below 32768" which apparently comes from matplotlib/backends/backend_agg.py, the RendererAgg (whatever that is).  I should point out these are plots which worked before.  Apparently it has something to do with adding axes_labels, because without them, this problem does not appear.  Did something get a LOT bigger on the axis labels?
> 
> 
> For right now, I automatically expand things to not clip axes labels.  There might be a bug in that.  Can you post an example?
>

It appears to have something to do with where the labels are located. 

```
sage: plot(x**2,0,1,axes_labels=['x','y'])
```

is fine, but 

```
sage: plot(x**2,99,100,axes_labels=['x','y'])
```

yields the problem.  This also happens with point sets:


```
sage: data=[(1990,1611),(1991,1586)]
sage: plot1=point(data)
sage: show(plot1,axes_labels=['x','y'])
```


Back to the other issues, note that while the following does plot

```
sage: show(plot1)
```

it also is not ideal, as the axes don't even come close to touching.  By the way, the pointsize is irrelevant - even with no pointsize given, the points are still cut off.  Also, there is a mysterious cut-off thing at the bottom which look like +1.00e3, but it's cut off so I can't tell for sure.  Any ideas on that?



---

archive/issue_comments_042066.json:
```json
{
    "body": "Replying to [comment:12 kcrisman]:\n> Replying to [comment:11 jason]:\n> > Thanks for looking at this!  I haven't had time to come back to it yet (our semester started...)\n> > \n> > Replying to [comment:10 kcrisman]:\n> > > 1. When using pointsize, matplotlib axes (or the way in which they are used) has some whitespace cutting off points, for example when pointsize is large (20 worked for me, but unfortunately I can't cut and paste and example here).\n> > \n> > On the one hand, I can turn off clipping.  However, that tends to make really ugly plots when you have frame axes (since then the dots go outside of the frames).  On the other hand, we can automatically enlarge the plot axes (so that if you request -3..3, it might actually cover -3.5..3.5).  This could be frustrating, but is sort of what happens now.  I guess you have to make a choice between things extending beyond your plot (no clipping) or extending your plot.  For right now, I was hoping that people would just make their ranges a bit bigger by hand.\n> \n> Definitely should be automatic, I think, if it's already-existing behavior.  \n\n\nOkay, I think I have an idea that will do this (find the bounding box of the scatter plots, convert those coordinates to axes coordinates, and then enlarge the axes to include those bounding boxes)\n\n\n> > \n> > \n> > \n> > > \n> > > 2. I'm not sure I like the non-intersecting axes on regular plots.  That is weird, especially in graphs like the plot of x squared type things.  plot(x**2,0,1) looks great; plot(x**2,-1,1) looks... interesting.\n> > \n> > Yeah, it's a bit different, but after playing with it for a while, I liked it.  At a glance, it oriented me to what I was looking at and how it was compared to the infinite plane.  This is definitely something that should go up for a vote.\n> \n> I'm not sure what you are looking at.  The axes do not actually cross!  That is bad, imho.\n\n\nAnd, after I played with it for a bit, I thought it was great!  The axes only ever cross at the origin.  That is wonderfully refreshing and consistent, and leads to being able to immediately orient yourself in the graph without having to examine and think about the axes tick labels.  If there is some space, then that means you are way above the axis (and the side the axis is on tells you where the axis really is).  I think of it sort of like a small zigzag break in the axes.  Maybe if we put that in an explicit small zigzag symbol, would that help you?\n\n\n> > > \n> > > 6. Ironically, switching slope fields to normal (not frame) axes is worse, because it's hard to see the numbers with any reasonably density of the points for the slopes.\n> > \n> > \n> > and your proposed fix is...?\n> > \n> \n> Using frames again for slope fields (the previous behavior).\n\n\nAh, I thought I did this.  I did it for contour plots; doing it for vector fields is about a one-line change (just add frame=True to the `@`options decorator before the vector field plotting function)",
    "created_at": "2009-08-26T14:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42066",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:12 kcrisman]:
> Replying to [comment:11 jason]:
> > Thanks for looking at this!  I haven't had time to come back to it yet (our semester started...)
> > 
> > Replying to [comment:10 kcrisman]:
> > > 1. When using pointsize, matplotlib axes (or the way in which they are used) has some whitespace cutting off points, for example when pointsize is large (20 worked for me, but unfortunately I can't cut and paste and example here).
> > 
> > On the one hand, I can turn off clipping.  However, that tends to make really ugly plots when you have frame axes (since then the dots go outside of the frames).  On the other hand, we can automatically enlarge the plot axes (so that if you request -3..3, it might actually cover -3.5..3.5).  This could be frustrating, but is sort of what happens now.  I guess you have to make a choice between things extending beyond your plot (no clipping) or extending your plot.  For right now, I was hoping that people would just make their ranges a bit bigger by hand.
> 
> Definitely should be automatic, I think, if it's already-existing behavior.  


Okay, I think I have an idea that will do this (find the bounding box of the scatter plots, convert those coordinates to axes coordinates, and then enlarge the axes to include those bounding boxes)


> > 
> > 
> > 
> > > 
> > > 2. I'm not sure I like the non-intersecting axes on regular plots.  That is weird, especially in graphs like the plot of x squared type things.  plot(x**2,0,1) looks great; plot(x**2,-1,1) looks... interesting.
> > 
> > Yeah, it's a bit different, but after playing with it for a while, I liked it.  At a glance, it oriented me to what I was looking at and how it was compared to the infinite plane.  This is definitely something that should go up for a vote.
> 
> I'm not sure what you are looking at.  The axes do not actually cross!  That is bad, imho.


And, after I played with it for a bit, I thought it was great!  The axes only ever cross at the origin.  That is wonderfully refreshing and consistent, and leads to being able to immediately orient yourself in the graph without having to examine and think about the axes tick labels.  If there is some space, then that means you are way above the axis (and the side the axis is on tells you where the axis really is).  I think of it sort of like a small zigzag break in the axes.  Maybe if we put that in an explicit small zigzag symbol, would that help you?


> > > 
> > > 6. Ironically, switching slope fields to normal (not frame) axes is worse, because it's hard to see the numbers with any reasonably density of the points for the slopes.
> > 
> > 
> > and your proposed fix is...?
> > 
> 
> Using frames again for slope fields (the previous behavior).


Ah, I thought I did this.  I did it for contour plots; doing it for vector fields is about a one-line change (just add frame=True to the `@`options decorator before the vector field plotting function)



---

archive/issue_comments_042067.json:
```json
{
    "body": "> > > > 2. I'm not sure I like the non-intersecting axes on regular plots.  That is weird, especially in graphs like the plot of x squared type things.  plot(x**2,0,1) looks great; plot(x**2,-1,1) looks... interesting.\n> > > \n> > > Yeah, it's a bit different, but after playing with it for a while, I liked it.  At a glance, it oriented me to what I was looking at and how it was compared to the infinite plane.  This is definitely something that should go up for a vote.\n> > \n> > I'm not sure what you are looking at.  The axes do not actually cross!  That is bad, imho.\n> \n> \n> And, after I played with it for a bit, I thought it was great!  The axes only ever cross at the origin.  That is wonderfully refreshing and consistent, and leads to being able to immediately orient yourself in the graph without having to examine and think about the axes tick labels.  If there is some space, then that means you are way above the axis (and the side the axis is on tells you where the axis really is).  I think of it sort of like a small zigzag break in the axes.  Maybe if we put that in an explicit small zigzag symbol, would that help you?\n> \n> \n\nI see.  The problem is that this is just as non-standard as the previous behavior, which people also complained about. For sure it shouldn't happen with\n\n```\nsage: plot(x**2,-1,1) \n```\n\nI do agree that it is more consistent, if you can get it to be consistent - and if it is REALLY well documented, i.e. right up at the top of the plot docs and in the tutorial.  If you think the rest of the stuff is ready for prime time, you should definitely put the various versions in screenshots up for a vote on sage-devel, since improved axes would really be great to have.",
    "created_at": "2009-08-26T14:13:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42067",
    "user": "https://github.com/kcrisman"
}
```

> > > > 2. I'm not sure I like the non-intersecting axes on regular plots.  That is weird, especially in graphs like the plot of x squared type things.  plot(x**2,0,1) looks great; plot(x**2,-1,1) looks... interesting.
> > > 
> > > Yeah, it's a bit different, but after playing with it for a while, I liked it.  At a glance, it oriented me to what I was looking at and how it was compared to the infinite plane.  This is definitely something that should go up for a vote.
> > 
> > I'm not sure what you are looking at.  The axes do not actually cross!  That is bad, imho.
> 
> 
> And, after I played with it for a bit, I thought it was great!  The axes only ever cross at the origin.  That is wonderfully refreshing and consistent, and leads to being able to immediately orient yourself in the graph without having to examine and think about the axes tick labels.  If there is some space, then that means you are way above the axis (and the side the axis is on tells you where the axis really is).  I think of it sort of like a small zigzag break in the axes.  Maybe if we put that in an explicit small zigzag symbol, would that help you?
> 
> 

I see.  The problem is that this is just as non-standard as the previous behavior, which people also complained about. For sure it shouldn't happen with

```
sage: plot(x**2,-1,1) 
```

I do agree that it is more consistent, if you can get it to be consistent - and if it is REALLY well documented, i.e. right up at the top of the plot docs and in the tutorial.  If you think the rest of the stuff is ready for prime time, you should definitely put the various versions in screenshots up for a vote on sage-devel, since improved axes would really be great to have.



---

archive/issue_comments_042068.json:
```json
{
    "body": "Replying to [comment:13 kcrisman]:\n> Replying to [comment:11 jason]:\n> > > 3. For some reasons, showing some plots yields the #5956 ValueError of \"ValueError: width and height must each be below 32768\" which apparently comes from matplotlib/backends/backend_agg.py, the RendererAgg (whatever that is).  I should point out these are plots which worked before.  Apparently it has something to do with adding axes_labels, because without them, this problem does not appear.  Did something get a LOT bigger on the axis labels?\n> > \n> > \n> > For right now, I automatically expand things to not clip axes labels.  There might be a bug in that.  Can you post an example?\n> >\n> \n> It appears to have something to do with where the labels are located. \n> {{{\n> sage: plot(x**2,0,1,axes_labels=['x','y'])\n> }}}\n> is fine, but \n> {{{\n> sage: plot(x**2,99,100,axes_labels=['x','y'])\n> }}}\n> yields the problem.  This also happens with point sets:\n> \n> {{{\n> sage: data=[(1990,1611),(1991,1586)]\n> sage: plot1=point(data)\n> sage: show(plot1,axes_labels=['x','y'])\n> }}}\n> \n\nI figured out what the problem was.  I'm setting the x-axis label y-coordinate to y=0, which is obviously wrong if y=0 is not in the picture.  I'm doing a similar thing with the y-axis label.  I've emailed the matplotlib list for help on getting the right matplotlib transform to get the label to be offset from the actual axis in the picture.",
    "created_at": "2009-08-30T04:17:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42068",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:13 kcrisman]:
> Replying to [comment:11 jason]:
> > > 3. For some reasons, showing some plots yields the #5956 ValueError of "ValueError: width and height must each be below 32768" which apparently comes from matplotlib/backends/backend_agg.py, the RendererAgg (whatever that is).  I should point out these are plots which worked before.  Apparently it has something to do with adding axes_labels, because without them, this problem does not appear.  Did something get a LOT bigger on the axis labels?
> > 
> > 
> > For right now, I automatically expand things to not clip axes labels.  There might be a bug in that.  Can you post an example?
> >
> 
> It appears to have something to do with where the labels are located. 
> {{{
> sage: plot(x**2,0,1,axes_labels=['x','y'])
> }}}
> is fine, but 
> {{{
> sage: plot(x**2,99,100,axes_labels=['x','y'])
> }}}
> yields the problem.  This also happens with point sets:
> 
> {{{
> sage: data=[(1990,1611),(1991,1586)]
> sage: plot1=point(data)
> sage: show(plot1,axes_labels=['x','y'])
> }}}
> 

I figured out what the problem was.  I'm setting the x-axis label y-coordinate to y=0, which is obviously wrong if y=0 is not in the picture.  I'm doing a similar thing with the y-axis label.  I've emailed the matplotlib list for help on getting the right matplotlib transform to get the label to be offset from the actual axis in the picture.



---

archive/issue_comments_042069.json:
```json
{
    "body": "The new patch:\n\n* is rebased against 4.1.1\n* omits the tick labels for the origin when the axes cross inside of the picture\n* puts the axis labels where they go by default in matplotlib, instead of trying to make them like mathematica.  This is temporary until I hear back from the matplotlib mailing list about the best way to make it so that the labels are at the end of the axes.\n* changes vector field and slope field plots to have frame=True by default",
    "created_at": "2009-08-30T05:21:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42069",
    "user": "https://github.com/jasongrout"
}
```

The new patch:

* is rebased against 4.1.1
* omits the tick labels for the origin when the axes cross inside of the picture
* puts the axis labels where they go by default in matplotlib, instead of trying to make them like mathematica.  This is temporary until I hear back from the matplotlib mailing list about the best way to make it so that the labels are at the end of the axes.
* changes vector field and slope field plots to have frame=True by default



---

archive/issue_comments_042070.json:
```json
{
    "body": "A minor question about #260: When I rebase its patch, should I change this part:\n\n```\n# Set the degree of transparency.  Since the matplotlib axes \n# are hidden, we omit subplot.patch.set_alpha(transparency). \nif transparency is not None: \n    figure.patch.set_alpha(transparency)\n```\n\n?",
    "created_at": "2009-08-30T11:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42070",
    "user": "https://github.com/qed777"
}
```

A minor question about #260: When I rebase its patch, should I change this part:

```
# Set the degree of transparency.  Since the matplotlib axes 
# are hidden, we omit subplot.patch.set_alpha(transparency). 
if transparency is not None: 
    figure.patch.set_alpha(transparency)
```

?



---

archive/issue_comments_042071.json:
```json
{
    "body": "Sorry about the dumb question, but how do I apply this patch?\n\nFollowing the instructions at http://www.sagemath.org/doc/developer/producing_patches.html, I did: \nhg_sage.patch('trac-5448-matplotlib-axes-gridlines.patch')\n\nHowever, this launched me straight into editing the patch, which I was not really up to. Exiting the editors led to the following message:\n\nRuntimeError: Refusing to do operation since you still have unrecorded changes. You must check in all changes in your working repository first.\n\nThanks for your help!\n\nStan",
    "created_at": "2009-08-31T06:42:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42071",
    "user": "https://trac.sagemath.org/admin/accounts/users/schymans"
}
```

Sorry about the dumb question, but how do I apply this patch?

Following the instructions at http://www.sagemath.org/doc/developer/producing_patches.html, I did: 
hg_sage.patch('trac-5448-matplotlib-axes-gridlines.patch')

However, this launched me straight into editing the patch, which I was not really up to. Exiting the editors led to the following message:

RuntimeError: Refusing to do operation since you still have unrecorded changes. You must check in all changes in your working repository first.

Thanks for your help!

Stan



---

archive/issue_comments_042072.json:
```json
{
    "body": "Try this from the command line:\n\n```\n$ sage -sh\n$ cd $SAGE_ROOT/devel/sage/sage/\n$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5448/trac-5448-matplotlib-axes-gridlines.patch\n$ hg qpush\n```\n\n\n(there is a way to do this inside of Sage too, like you tried above, but I never use that and don't know exactly what to type).\n\nThe error message above says that you were modifying files, though.  To see what has been changed, do:\n\n\n```\n$ sage -sh\n$ cd $SAGE_ROOT/devel/sage/sage/\n$ hg diff\n```\n\n\nIf you don't want to save any of your changes, you can do the following.  WARNING: this will delete all changes you've made to Sage files that you haven't checked into the repository.\n\n\n```\nhg revert --all\n```\n\n\nand then do the above hg qimport commands.",
    "created_at": "2009-08-31T13:13:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42072",
    "user": "https://github.com/jasongrout"
}
```

Try this from the command line:

```
$ sage -sh
$ cd $SAGE_ROOT/devel/sage/sage/
$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5448/trac-5448-matplotlib-axes-gridlines.patch
$ hg qpush
```


(there is a way to do this inside of Sage too, like you tried above, but I never use that and don't know exactly what to type).

The error message above says that you were modifying files, though.  To see what has been changed, do:


```
$ sage -sh
$ cd $SAGE_ROOT/devel/sage/sage/
$ hg diff
```


If you don't want to save any of your changes, you can do the following.  WARNING: this will delete all changes you've made to Sage files that you haven't checked into the repository.


```
hg revert --all
```


and then do the above hg qimport commands.



---

archive/issue_comments_042073.json:
```json
{
    "body": "Replying to [comment:18 mpatel]:\n> A minor question about #260: When I rebase its patch, should I change this part:\n> {{{\n> # Set the degree of transparency.  Since the matplotlib axes \n> # are hidden, we omit subplot.patch.set_alpha(transparency). \n> if transparency is not None: \n>     figure.patch.set_alpha(transparency)\n> }}}\n> ?\n\nI've posted up some comments on #260.  Either that patch or this patch will need to be updated.",
    "created_at": "2009-08-31T13:38:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42073",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:18 mpatel]:
> A minor question about #260: When I rebase its patch, should I change this part:
> {{{
> # Set the degree of transparency.  Since the matplotlib axes 
> # are hidden, we omit subplot.patch.set_alpha(transparency). 
> if transparency is not None: 
>     figure.patch.set_alpha(transparency)
> }}}
> ?

I've posted up some comments on #260.  Either that patch or this patch will need to be updated.



---

archive/issue_comments_042074.json:
```json
{
    "body": "Thanks for your help, Jason. Unfortunately, I get the following error:\n$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5448/trac-5448-matplotlib-axes-gridlines.patch\n\nhg: unknown command 'qimport'\n\nMaybe there is something wrong with my installation of sage? I'm on OSX 10.4.\n\nThe hg revert --all took me a few steps further using hg_sage.patch from within sage, until:\n\npatching file sage/plot/matrix_plot.py\nHunk #1 FAILED at 155\n1 out of 1 hunks FAILED -- saving rejects to file sage/plot/matrix_plot.py.rej\npatching file sage/plot/plot.py\nHunk #6 FAILED at 1222\nHunk #10 FAILED at 1770\nHunk #11 FAILED at 1812\n3 out of 14 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej\nabort: patch failed to apply\n\n:-(\n\nNot sure if this is the right place for this kind of support. Should I post about it to the support mailing list?\n\nCheers,\nStan",
    "created_at": "2009-08-31T14:44:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42074",
    "user": "https://trac.sagemath.org/admin/accounts/users/schymans"
}
```

Thanks for your help, Jason. Unfortunately, I get the following error:
$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5448/trac-5448-matplotlib-axes-gridlines.patch

hg: unknown command 'qimport'

Maybe there is something wrong with my installation of sage? I'm on OSX 10.4.

The hg revert --all took me a few steps further using hg_sage.patch from within sage, until:

patching file sage/plot/matrix_plot.py
Hunk #1 FAILED at 155
1 out of 1 hunks FAILED -- saving rejects to file sage/plot/matrix_plot.py.rej
patching file sage/plot/plot.py
Hunk #6 FAILED at 1222
Hunk #10 FAILED at 1770
Hunk #11 FAILED at 1812
3 out of 14 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej
abort: patch failed to apply

:-(

Not sure if this is the right place for this kind of support. Should I post about it to the support mailing list?

Cheers,
Stan



---

archive/issue_comments_042075.json:
```json
{
    "body": "Replying to [comment:22 schymans]:\n> Thanks for your help, Jason. Unfortunately, I get the following error:\n> $ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5448/trac-5448-matplotlib-axes-gridlines.patch\n> \n> hg: unknown command 'qimport'\n> \n> Maybe there is something wrong with my installation of sage? I'm on OSX 10.4.\n> \n> The hg revert --all took me a few steps further using hg_sage.patch from within sage, until:\n> \n> patching file sage/plot/matrix_plot.py\n> Hunk #1 FAILED at 155\n> 1 out of 1 hunks FAILED -- saving rejects to file sage/plot/matrix_plot.py.rej\n> patching file sage/plot/plot.py\n> Hunk #6 FAILED at 1222\n> Hunk #10 FAILED at 1770\n> Hunk #11 FAILED at 1812\n> 3 out of 14 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej\n> abort: patch failed to apply\n> \n> :-(\n> \n> Not sure if this is the right place for this kind of support. Should I post about it to the support mailing list?\n\n\n1. Are you applying this to 4.1.1?  Have you made any changes or applied any other patches before this one?\n\n2. Did you download the latest version of the patch?  I updated it Saturday to work with 4.1.1.",
    "created_at": "2009-08-31T16:53:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42075",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:22 schymans]:
> Thanks for your help, Jason. Unfortunately, I get the following error:
> $ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5448/trac-5448-matplotlib-axes-gridlines.patch
> 
> hg: unknown command 'qimport'
> 
> Maybe there is something wrong with my installation of sage? I'm on OSX 10.4.
> 
> The hg revert --all took me a few steps further using hg_sage.patch from within sage, until:
> 
> patching file sage/plot/matrix_plot.py
> Hunk #1 FAILED at 155
> 1 out of 1 hunks FAILED -- saving rejects to file sage/plot/matrix_plot.py.rej
> patching file sage/plot/plot.py
> Hunk #6 FAILED at 1222
> Hunk #10 FAILED at 1770
> Hunk #11 FAILED at 1812
> 3 out of 14 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej
> abort: patch failed to apply
> 
> :-(
> 
> Not sure if this is the right place for this kind of support. Should I post about it to the support mailing list?


1. Are you applying this to 4.1.1?  Have you made any changes or applied any other patches before this one?

2. Did you download the latest version of the patch?  I updated it Saturday to work with 4.1.1.



---

archive/issue_comments_042076.json:
```json
{
    "body": "Replying to [comment:22 schymans]:\n> Thanks for your help, Jason. Unfortunately, I get the following error:\n> $ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5448/trac-5448-matplotlib-axes-gridlines.patch\n> \n> hg: unknown command 'qimport'\n> \nYou have to have the Mercurial queues to do this (I don't, either).  Your previous command should work, as long as you do NOT have any (uncommitted) changes to your code in the branch you attach it to.\n\nThat said, this sort of thing probably does belong on support next time, because others will likely have the same problem and it's not specific to this patch.  Good luck!",
    "created_at": "2009-08-31T20:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42076",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:22 schymans]:
> Thanks for your help, Jason. Unfortunately, I get the following error:
> $ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/5448/trac-5448-matplotlib-axes-gridlines.patch
> 
> hg: unknown command 'qimport'
> 
You have to have the Mercurial queues to do this (I don't, either).  Your previous command should work, as long as you do NOT have any (uncommitted) changes to your code in the branch you attach it to.

That said, this sort of thing probably does belong on support next time, because others will likely have the same problem and it's not specific to this patch.  Good luck!



---

archive/issue_comments_042077.json:
```json
{
    "body": "Thanks for your help, guys! I keep getting messages about uncommitted changes, probably from previous unsuccessful attempts to apply the patch. I'll move the discussion to sage-devel.\n\nCheers,\nStan",
    "created_at": "2009-09-01T00:45:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42077",
    "user": "https://trac.sagemath.org/admin/accounts/users/schymans"
}
```

Thanks for your help, guys! I keep getting messages about uncommitted changes, probably from previous unsuccessful attempts to apply the patch. I'll move the discussion to sage-devel.

Cheers,
Stan



---

archive/issue_comments_042078.json:
```json
{
    "body": "Comments on the latest iteration:\n\nI like the new look of vector/slope fields, actually - clear, because there are internal axes now!\n\nHere are some small technical details I do not like, which cause it to still \"need work\".\n\n1. plot(x**2,-1,1) is unacceptable.  No one will believe that even though the origin is in the graph, the axes don't cross!  Instead they will assume that the origin is not in the graph.  Presumably there is a way to have the algorithm do this, though, on an adhoc basis.\n\n2. plot(x**3,-1,1,axes_labels=['x','y']) shows that we should wait with this patch until there is a good way to move the axes - this is too confusing.  Try replacing 'y' with 'zany' and it's just silly.  Matplotlib style axis labels only work with frames.\n\n3. there needs to be a slightly better algorithm for deciding what direction the ticks face.  E.g. look at plot(x**3,-1,0).\n\n4. compare plot(x**4,-1,54) and plot(x**4,-1,55).  Notice how once the scientific notation comes into play, matplotlib doesn't label correctly.\n\nThat's all I found for now :)  But it's nice to have some time to try to get this good.  Assuming we actually want to do so, that is - is it more effort than its worth?  Maybe the matplotlib upgrade could be a separate ticket, because that is certainly worthwhile and presumably doesn't cause any problems.",
    "created_at": "2009-09-01T02:01:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42078",
    "user": "https://github.com/kcrisman"
}
```

Comments on the latest iteration:

I like the new look of vector/slope fields, actually - clear, because there are internal axes now!

Here are some small technical details I do not like, which cause it to still "need work".

1. plot(x**2,-1,1) is unacceptable.  No one will believe that even though the origin is in the graph, the axes don't cross!  Instead they will assume that the origin is not in the graph.  Presumably there is a way to have the algorithm do this, though, on an adhoc basis.

2. plot(x**3,-1,1,axes_labels=['x','y']) shows that we should wait with this patch until there is a good way to move the axes - this is too confusing.  Try replacing 'y' with 'zany' and it's just silly.  Matplotlib style axis labels only work with frames.

3. there needs to be a slightly better algorithm for deciding what direction the ticks face.  E.g. look at plot(x**3,-1,0).

4. compare plot(x**4,-1,54) and plot(x**4,-1,55).  Notice how once the scientific notation comes into play, matplotlib doesn't label correctly.

That's all I found for now :)  But it's nice to have some time to try to get this good.  Assuming we actually want to do so, that is - is it more effort than its worth?  Maybe the matplotlib upgrade could be a separate ticket, because that is certainly worthwhile and presumably doesn't cause any problems.



---

archive/issue_comments_042079.json:
```json
{
    "body": "Replying to [comment:26 kcrisman]:\n> Comments on the latest iteration:\n> \n> I like the new look of vector/slope fields, actually - clear, because there are internal axes now!\n> \n> Here are some small technical details I do not like, which cause it to still \"need work\".\n> \n> 1. plot(x**2,-1,1) is unacceptable.  No one will believe that even though the origin is in the graph, the axes don't cross!  Instead they will assume that the origin is not in the graph.  Presumably there is a way to have the algorithm do this, though, on an adhoc basis.\n\nYes, it seems that numerical error is our enemy here:\n\n\n```\nsage: ax=plot(x**2,-1,1).matplotlib().axes[0]\nsage: ax.get_ylim()\n(2.2226365446612245e-06, 1.0)\n```\n\n\nI modified the code so that if 0 is within 1% of the range, but not included in the range, then we enlarge the range to include 0.  We could change this 1% parameter, or make it user-settable.\n\nThis is fixed in the patch I'm posting up in a second.\n\n> \n> 2. plot(x**3,-1,1,axes_labels=['x','y']) shows that we should wait with this patch until there is a good way to move the axes - this is too confusing.  Try replacing 'y' with 'zany' and it's just silly.  Matplotlib style axis labels only work with frames.\n> \n\n\nI've fixed this---well, except for one exceptional case. I'm waiting to hear back on the matplotlib mailing list (it might be a bug in matplotlib).  I'll post up a patch in a second.\n\n\n> 3. there needs to be a slightly better algorithm for deciding what direction the ticks face.  E.g. look at plot(x**3,-1,0).\n\nAgreed.  Do you have a suggestion?  Maybe if the axis is in the middle of the picture, put ticks on both sides, and if it is on the side of the picture, put ticks facing inwards?\n\n\n> \n> 4. compare plot(x**4,-1,54) and plot(x**4,-1,55).  Notice how once the scientific notation comes into play, matplotlib doesn't label correctly.\n\nAs in the top is cut off?  Is that what you are talking about?\n\nWe can change how the labels are printed pretty easily.  What do you suggest?\n\n> \n> That's all I found for now :)  But it's nice to have some time to try to get this good.  Assuming we actually want to do so, that is - is it more effort than its worth?  Maybe the matplotlib upgrade could be a separate ticket, because that is certainly worthwhile and presumably doesn't cause any problems.\n\nThis is great.  I think we are close enough to being done with this (or at least, close enough to a sage-devel discussion) that it's not worth trying to package 0.99.0 separately.  Most of the reason why 0.99.0 is worth it is for these changes, I think.",
    "created_at": "2009-09-01T15:41:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42079",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:26 kcrisman]:
> Comments on the latest iteration:
> 
> I like the new look of vector/slope fields, actually - clear, because there are internal axes now!
> 
> Here are some small technical details I do not like, which cause it to still "need work".
> 
> 1. plot(x**2,-1,1) is unacceptable.  No one will believe that even though the origin is in the graph, the axes don't cross!  Instead they will assume that the origin is not in the graph.  Presumably there is a way to have the algorithm do this, though, on an adhoc basis.

Yes, it seems that numerical error is our enemy here:


```
sage: ax=plot(x**2,-1,1).matplotlib().axes[0]
sage: ax.get_ylim()
(2.2226365446612245e-06, 1.0)
```


I modified the code so that if 0 is within 1% of the range, but not included in the range, then we enlarge the range to include 0.  We could change this 1% parameter, or make it user-settable.

This is fixed in the patch I'm posting up in a second.

> 
> 2. plot(x**3,-1,1,axes_labels=['x','y']) shows that we should wait with this patch until there is a good way to move the axes - this is too confusing.  Try replacing 'y' with 'zany' and it's just silly.  Matplotlib style axis labels only work with frames.
> 


I've fixed this---well, except for one exceptional case. I'm waiting to hear back on the matplotlib mailing list (it might be a bug in matplotlib).  I'll post up a patch in a second.


> 3. there needs to be a slightly better algorithm for deciding what direction the ticks face.  E.g. look at plot(x**3,-1,0).

Agreed.  Do you have a suggestion?  Maybe if the axis is in the middle of the picture, put ticks on both sides, and if it is on the side of the picture, put ticks facing inwards?


> 
> 4. compare plot(x**4,-1,54) and plot(x**4,-1,55).  Notice how once the scientific notation comes into play, matplotlib doesn't label correctly.

As in the top is cut off?  Is that what you are talking about?

We can change how the labels are printed pretty easily.  What do you suggest?

> 
> That's all I found for now :)  But it's nice to have some time to try to get this good.  Assuming we actually want to do so, that is - is it more effort than its worth?  Maybe the matplotlib upgrade could be a separate ticket, because that is certainly worthwhile and presumably doesn't cause any problems.

This is great.  I think we are close enough to being done with this (or at least, close enough to a sage-devel discussion) that it's not worth trying to package 0.99.0 separately.  Most of the reason why 0.99.0 is worth it is for these changes, I think.



---

archive/issue_comments_042080.json:
```json
{
    "body": "I updated the patch to:\n\n1. if zero is within 1% of the range, but is not included in the range, then extend the range to include zero.\n\n2. fix axes labels for cases where the axes are not on the top or the right.  A full solution is waiting for a response on the matplotlib mailing list---there might be a bug in how matplotlib handles things.\n\n3. Introduced a simple \"transparent\" option to show, which saves the image with transparent background.  This is a subset of the functionality implemented at #260.  I think #260 ought to go ahead and implement its functionality in full generality (i.e., let the user specify the background color and opacity of a plot), but my change in this patch lets the user easily generate a transparent background using the function already provided by matplotlib.",
    "created_at": "2009-09-01T15:56:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42080",
    "user": "https://github.com/jasongrout"
}
```

I updated the patch to:

1. if zero is within 1% of the range, but is not included in the range, then extend the range to include zero.

2. fix axes labels for cases where the axes are not on the top or the right.  A full solution is waiting for a response on the matplotlib mailing list---there might be a bug in how matplotlib handles things.

3. Introduced a simple "transparent" option to show, which saves the image with transparent background.  This is a subset of the functionality implemented at #260.  I think #260 ought to go ahead and implement its functionality in full generality (i.e., let the user specify the background color and opacity of a plot), but my change in this patch lets the user easily generate a transparent background using the function already provided by matplotlib.



---

archive/issue_comments_042081.json:
```json
{
    "body": "> \n> > 3. there needs to be a slightly better algorithm for deciding what direction the ticks face.  E.g. look at plot(x**3,-1,0).\n> \n> Agreed.  Do you have a suggestion?  Maybe if the axis is in the middle of the picture, put ticks on both sides, and if it is on the side of the picture, put ticks facing inwards?\n> \n\nI thought that was already the convention, but it was screwed up in this plot.  I think that in general ticks on the right/top are okay, except where the axis is beyond the entire plot.  Probably that isn't the case for this plot, but it still looks weird.\n\n> \n> > \n> > 4. compare plot(x**4,-1,54) and plot(x**4,-1,55).  Notice how once the scientific notation comes into play, matplotlib doesn't label correctly.\n> \n> As in the top is cut off?  Is that what you are talking about?\n> \n> We can change how the labels are printed pretty easily.  What do you suggest?\n> \n\nNo, I mean that the labels are WRONG.  The scientific notation only shows up at the very top e.g. 2e8 or something, and the rest are just 1, 1.5, etc; certainly the fourth power function does not stay around 1, 1.5 very long.  Having 2e8 or 1.5e8 is okay, of course.\n\n> > \n> > That's all I found for now :)  But it's nice to have some time to try to get this good.  Assuming we actually want to do so, that is - is it more effort than its worth?  Maybe the matplotlib upgrade could be a separate ticket, because that is certainly worthwhile and presumably doesn't cause any problems.\n> \n> This is great.  I think we are close enough to being done with this (or at least, close enough to a sage-devel discussion) that it's not worth trying to package 0.99.0 separately.  Most of the reason why 0.99.0 is worth it is for these changes, I think.\n> \n\nOkay.",
    "created_at": "2009-09-01T17:24:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42081",
    "user": "https://github.com/kcrisman"
}
```

> 
> > 3. there needs to be a slightly better algorithm for deciding what direction the ticks face.  E.g. look at plot(x**3,-1,0).
> 
> Agreed.  Do you have a suggestion?  Maybe if the axis is in the middle of the picture, put ticks on both sides, and if it is on the side of the picture, put ticks facing inwards?
> 

I thought that was already the convention, but it was screwed up in this plot.  I think that in general ticks on the right/top are okay, except where the axis is beyond the entire plot.  Probably that isn't the case for this plot, but it still looks weird.

> 
> > 
> > 4. compare plot(x**4,-1,54) and plot(x**4,-1,55).  Notice how once the scientific notation comes into play, matplotlib doesn't label correctly.
> 
> As in the top is cut off?  Is that what you are talking about?
> 
> We can change how the labels are printed pretty easily.  What do you suggest?
> 

No, I mean that the labels are WRONG.  The scientific notation only shows up at the very top e.g. 2e8 or something, and the rest are just 1, 1.5, etc; certainly the fourth power function does not stay around 1, 1.5 very long.  Having 2e8 or 1.5e8 is okay, of course.

> > 
> > That's all I found for now :)  But it's nice to have some time to try to get this good.  Assuming we actually want to do so, that is - is it more effort than its worth?  Maybe the matplotlib upgrade could be a separate ticket, because that is certainly worthwhile and presumably doesn't cause any problems.
> 
> This is great.  I think we are close enough to being done with this (or at least, close enough to a sage-devel discussion) that it's not worth trying to package 0.99.0 separately.  Most of the reason why 0.99.0 is worth it is for these changes, I think.
> 

Okay.



---

archive/issue_comments_042082.json:
```json
{
    "body": "Replying to [comment:29 kcrisman]:\n> > \n> > > 3. there needs to be a slightly better algorithm for deciding what direction the ticks face.  E.g. look at plot(x**3,-1,0).\n> > \n> > Agreed.  Do you have a suggestion?  Maybe if the axis is in the middle of the picture, put ticks on both sides, and if it is on the side of the picture, put ticks facing inwards?\n> > \n> \n> I thought that was already the convention, but it was screwed up in this plot.  I think that in general ticks on the right/top are okay, except where the axis is beyond the entire plot.  Probably that isn't the case for this plot, but it still looks weird.\n> \n\n\nRight now the convention was to put left-facing ticks unless the axis was beyond the plot on the right.  Then put right-facing ticks.  In your example, the axes were still considered to be inside the plot.\n\n\n\n> > \n> > > \n> > > 4. compare plot(x**4,-1,54) and plot(x**4,-1,55).  Notice how once the scientific notation comes into play, matplotlib doesn't label correctly.\n> > \n> > As in the top is cut off?  Is that what you are talking about?\n> > \n> > We can change how the labels are printed pretty easily.  What do you suggest?\n> > \n> \n> No, I mean that the labels are WRONG.  The scientific notation only shows up at the very top e.g. 2e8 or something, and the rest are just 1, 1.5, etc; certainly the fourth power function does not stay around 1, 1.5 very long.  Having 2e8 or 1.5e8 is okay, of course.\n> \n\n\nI think they mean that the number at the top of the axis shows the units of the labels.  You would rather have labels in units of 1 always, I presume?",
    "created_at": "2009-09-01T17:34:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42082",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:29 kcrisman]:
> > 
> > > 3. there needs to be a slightly better algorithm for deciding what direction the ticks face.  E.g. look at plot(x**3,-1,0).
> > 
> > Agreed.  Do you have a suggestion?  Maybe if the axis is in the middle of the picture, put ticks on both sides, and if it is on the side of the picture, put ticks facing inwards?
> > 
> 
> I thought that was already the convention, but it was screwed up in this plot.  I think that in general ticks on the right/top are okay, except where the axis is beyond the entire plot.  Probably that isn't the case for this plot, but it still looks weird.
> 


Right now the convention was to put left-facing ticks unless the axis was beyond the plot on the right.  Then put right-facing ticks.  In your example, the axes were still considered to be inside the plot.



> > 
> > > 
> > > 4. compare plot(x**4,-1,54) and plot(x**4,-1,55).  Notice how once the scientific notation comes into play, matplotlib doesn't label correctly.
> > 
> > As in the top is cut off?  Is that what you are talking about?
> > 
> > We can change how the labels are printed pretty easily.  What do you suggest?
> > 
> 
> No, I mean that the labels are WRONG.  The scientific notation only shows up at the very top e.g. 2e8 or something, and the rest are just 1, 1.5, etc; certainly the fourth power function does not stay around 1, 1.5 very long.  Having 2e8 or 1.5e8 is okay, of course.
> 


I think they mean that the number at the top of the axis shows the units of the labels.  You would rather have labels in units of 1 always, I presume?



---

archive/issue_comments_042083.json:
```json
{
    "body": "Replying to [comment:30 jason]:\n> Replying to [comment:29 kcrisman]:\n> > > \n> > > > 3. there needs to be a slightly better algorithm for deciding what direction the ticks face.  E.g. look at plot(x**3,-1,0).\n> > > \n> > > Agreed.  Do you have a suggestion?  Maybe if the axis is in the middle of the picture, put ticks on both sides, and if it is on the side of the picture, put ticks facing inwards?\n> > > \n> > \n> > I thought that was already the convention, but it was screwed up in this plot.  I think that in general ticks on the right/top are okay, except where the axis is beyond the entire plot.  Probably that isn't the case for this plot, but it still looks weird.\n> > \n> \n> \n> Right now the convention was to put left-facing ticks unless the axis was beyond the plot on the right.  Then put right-facing ticks.  In your example, the axes were still considered to be inside the plot.\n> \n\nBecause x=0 was in it... hmm, maybe that should be axis <= plot, instead of axis < plot?  If that makes sense.  This is obviously painting the shed, of course.\n\n> \n> \n> > > \n> > > > \n> > > > 4. compare plot(x**4,-1,54) and plot(x**4,-1,55).  Notice how once the scientific notation comes into play, matplotlib doesn't label correctly.\n> > > \n> > > As in the top is cut off?  Is that what you are talking about?\n> > > \n> > > We can change how the labels are printed pretty easily.  What do you suggest?\n> > > \n> > \n> > No, I mean that the labels are WRONG.  The scientific notation only shows up at the very top e.g. 2e8 or something, and the rest are just 1, 1.5, etc; certainly the fourth power function does not stay around 1, 1.5 very long.  Having 2e8 or 1.5e8 is okay, of course.\n> > \n> \n> \n> I think they mean that the number at the top of the axis shows the units of the labels.  You would rather have labels in units of 1 always, I presume?\n\nWell, since the number at the top of the axis was getting cut off, that was a problem.  I still think it could be confusing, though 1e200000 is probably not an ideal label if you got numbers that large (if they were even plottable).  I like what happened before with \n\n```\nsage: plot(x^4,-1,2000)\n```\n\nbetter, though it was also sometimes inconsistent and things got cut off, for instance\n\n```\nsage: plot(x^4,-1,1500)\n```\n\nSo it seems that explicit and longer is better than implicit and shorter, in this case.\n\nMaybe it's time to start declaring this reviewed and make new tickets for the other things...",
    "created_at": "2009-09-01T17:56:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42083",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:30 jason]:
> Replying to [comment:29 kcrisman]:
> > > 
> > > > 3. there needs to be a slightly better algorithm for deciding what direction the ticks face.  E.g. look at plot(x**3,-1,0).
> > > 
> > > Agreed.  Do you have a suggestion?  Maybe if the axis is in the middle of the picture, put ticks on both sides, and if it is on the side of the picture, put ticks facing inwards?
> > > 
> > 
> > I thought that was already the convention, but it was screwed up in this plot.  I think that in general ticks on the right/top are okay, except where the axis is beyond the entire plot.  Probably that isn't the case for this plot, but it still looks weird.
> > 
> 
> 
> Right now the convention was to put left-facing ticks unless the axis was beyond the plot on the right.  Then put right-facing ticks.  In your example, the axes were still considered to be inside the plot.
> 

Because x=0 was in it... hmm, maybe that should be axis <= plot, instead of axis < plot?  If that makes sense.  This is obviously painting the shed, of course.

> 
> 
> > > 
> > > > 
> > > > 4. compare plot(x**4,-1,54) and plot(x**4,-1,55).  Notice how once the scientific notation comes into play, matplotlib doesn't label correctly.
> > > 
> > > As in the top is cut off?  Is that what you are talking about?
> > > 
> > > We can change how the labels are printed pretty easily.  What do you suggest?
> > > 
> > 
> > No, I mean that the labels are WRONG.  The scientific notation only shows up at the very top e.g. 2e8 or something, and the rest are just 1, 1.5, etc; certainly the fourth power function does not stay around 1, 1.5 very long.  Having 2e8 or 1.5e8 is okay, of course.
> > 
> 
> 
> I think they mean that the number at the top of the axis shows the units of the labels.  You would rather have labels in units of 1 always, I presume?

Well, since the number at the top of the axis was getting cut off, that was a problem.  I still think it could be confusing, though 1e200000 is probably not an ideal label if you got numbers that large (if they were even plottable).  I like what happened before with 

```
sage: plot(x^4,-1,2000)
```

better, though it was also sometimes inconsistent and things got cut off, for instance

```
sage: plot(x^4,-1,1500)
```

So it seems that explicit and longer is better than implicit and shorter, in this case.

Maybe it's time to start declaring this reviewed and make new tickets for the other things...



---

archive/issue_comments_042084.json:
```json
{
    "body": "Matplotlib has very nice pluggable formatting framework for ticks.  The standard formatter is this one: http://matplotlib.sourceforge.net/api/ticker_api.html#matplotlib.ticker.ScalarFormatter  We can set it not to use scientific notation, or set the cutoff, or write our own.  Or we could use the FuncFormatter with our own (user-overridable) function.  Or we could just let the user pass a printf-style format string and use another matplotlib pluggable formatter.  Some examples are:\n\nhttp://matplotlib.sourceforge.net/examples/pylab_examples/newscalarformatter_demo.html\n\nhttp://matplotlib.sourceforge.net/examples/pylab_examples/custom_ticker1.html\n\nI think that once the matplotlib people get back to me about fixing the bug or my misunderstanding where axis labels aren't correct for top or right axes, we can post some images to sage-devel and move this forward on a vote.",
    "created_at": "2009-09-01T18:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42084",
    "user": "https://github.com/jasongrout"
}
```

Matplotlib has very nice pluggable formatting framework for ticks.  The standard formatter is this one: http://matplotlib.sourceforge.net/api/ticker_api.html#matplotlib.ticker.ScalarFormatter  We can set it not to use scientific notation, or set the cutoff, or write our own.  Or we could use the FuncFormatter with our own (user-overridable) function.  Or we could just let the user pass a printf-style format string and use another matplotlib pluggable formatter.  Some examples are:

http://matplotlib.sourceforge.net/examples/pylab_examples/newscalarformatter_demo.html

http://matplotlib.sourceforge.net/examples/pylab_examples/custom_ticker1.html

I think that once the matplotlib people get back to me about fixing the bug or my misunderstanding where axis labels aren't correct for top or right axes, we can post some images to sage-devel and move this forward on a vote.



---

archive/issue_comments_042085.json:
```json
{
    "body": "Incidentally, there are a HUGE slew of error messages, largely in sage/combinat, when doing sage -t, which all look like this:\n\n```\n    doctest:18: DeprecationWarning: \n    **********************************************************\n    matplotlib.numerix and all its subpackages are deprecated.\n    They will be removed soon.  Please use numpy instead.\n    **********************************************************\n    <BLANKLINE>\n```\n\nI'm not interested in doing that patch!  But it should only be tedious, not hard... unless someone removes sage/combinat's dependence on numerix.  But that's for another ticket.",
    "created_at": "2009-09-01T18:53:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42085",
    "user": "https://github.com/kcrisman"
}
```

Incidentally, there are a HUGE slew of error messages, largely in sage/combinat, when doing sage -t, which all look like this:

```
    doctest:18: DeprecationWarning: 
    **********************************************************
    matplotlib.numerix and all its subpackages are deprecated.
    They will be removed soon.  Please use numpy instead.
    **********************************************************
    <BLANKLINE>
```

I'm not interested in doing that patch!  But it should only be tedious, not hard... unless someone removes sage/combinat's dependence on numerix.  But that's for another ticket.



---

archive/issue_comments_042086.json:
```json
{
    "body": "See also [https://networkx.lanl.gov/trac/ticket/258](https://networkx.lanl.gov/trac/ticket/258), where the networkx folks fix this (the new mpl leads to lots of test failures in sage/graphs, too, unfortunately...)",
    "created_at": "2009-09-01T19:02:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42086",
    "user": "https://github.com/kcrisman"
}
```

See also [https://networkx.lanl.gov/trac/ticket/258](https://networkx.lanl.gov/trac/ticket/258), where the networkx folks fix this (the new mpl leads to lots of test failures in sage/graphs, too, unfortunately...)



---

archive/issue_comments_042087.json:
```json
{
    "body": "Ugh.  For now, I say we disable the deprecation warning.  I'm not looking forward to upgrading networkx at the moment---that's a bigger job.",
    "created_at": "2009-09-01T19:08:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42087",
    "user": "https://github.com/jasongrout"
}
```

Ugh.  For now, I say we disable the deprecation warning.  I'm not looking forward to upgrading networkx at the moment---that's a bigger job.



---

archive/issue_comments_042088.json:
```json
{
    "body": "Actually, my guess is that all of these errors come from networkx.  We could apply the networkx patch changeset you point out above to our networkx spkg and it seems like all would be well.",
    "created_at": "2009-09-01T19:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42088",
    "user": "https://github.com/jasongrout"
}
```

Actually, my guess is that all of these errors come from networkx.  We could apply the networkx patch changeset you point out above to our networkx spkg and it seems like all would be well.



---

archive/issue_comments_042089.json:
```json
{
    "body": "Okay, I updated the networkx spkg.  Please install:\n\nhttp://sage.math.washington.edu/home/jason/networkx-0.99.p1-fake_really-0.36.p1.spkg",
    "created_at": "2009-09-01T19:24:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42089",
    "user": "https://github.com/jasongrout"
}
```

Okay, I updated the networkx spkg.  Please install:

http://sage.math.washington.edu/home/jason/networkx-0.99.p1-fake_really-0.36.p1.spkg



---

archive/issue_comments_042090.json:
```json
{
    "body": "apply instead of previous patch.",
    "created_at": "2009-09-01T22:35:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42090",
    "user": "https://github.com/jasongrout"
}
```

apply instead of previous patch.



---

archive/issue_comments_042091.json:
```json
{
    "body": "Attachment [trac-5448-matplotlib-axes-gridlines.patch](tarball://root/attachments/some-uuid/ticket5448/trac-5448-matplotlib-axes-gridlines.patch) by @jasongrout created at 2009-09-01 23:41:22\n\nI posted a long post to sage-devel calling for comment and a vote on this axes placement strategy.  The post is here: http://groups.google.com/group/sage-devel/browse_thread/thread/5ad2b32d68bf8b87",
    "created_at": "2009-09-01T23:41:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42091",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-5448-matplotlib-axes-gridlines.patch](tarball://root/attachments/some-uuid/ticket5448/trac-5448-matplotlib-axes-gridlines.patch) by @jasongrout created at 2009-09-01 23:41:22

I posted a long post to sage-devel calling for comment and a vote on this axes placement strategy.  The post is here: http://groups.google.com/group/sage-devel/browse_thread/thread/5ad2b32d68bf8b87



---

archive/issue_comments_042092.json:
```json
{
    "body": "I can't figure out how to make transparent=True work (some pics would be nice for you to post).  But it doesn't break anything, so based on the devel discussion, let's get this in - everything works more or less as well as I can help right now. \n\nThings to think about: Note there are some mpl warnings about numerix and other deprecated things (e.g., legend.handlelen) when you start up the notebook.  Make sure that #260 works off this patch, as mpatel has indicated willingness to do.\n\nNote to release manager: needs both new matplotlib AND new networkx spkgs in order to avoid many, many deprecation warnings.",
    "created_at": "2009-09-02T14:08:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42092",
    "user": "https://github.com/kcrisman"
}
```

I can't figure out how to make transparent=True work (some pics would be nice for you to post).  But it doesn't break anything, so based on the devel discussion, let's get this in - everything works more or less as well as I can help right now. 

Things to think about: Note there are some mpl warnings about numerix and other deprecated things (e.g., legend.handlelen) when you start up the notebook.  Make sure that #260 works off this patch, as mpatel has indicated willingness to do.

Note to release manager: needs both new matplotlib AND new networkx spkgs in order to avoid many, many deprecation warnings.



---

archive/issue_comments_042093.json:
```json
{
    "body": "It seems that the problem of cutting off axes labels of large numbers is just a matter of when the axis switches to scientific notation. Consider this:\n\n`sage: plot(2^(20*x),(x,1,2.))`\n\nOnly numbers > 1.e+11 are converted to scientific notation, while the smaller ones get cut off. This could be fixed by changing to scientific notation at much smaller numbers. Actually, the change from decimal to scientific notation half way across the axis is something that bothered me in MMA already. Could you either let the user decide which notation to use or make it the same for the whole axis, depending on whether the largest (or smallest) number requires it? \n\nJust a few ideas for when you get to fixing the matplotlib tick stuff.\n\nCheers\nStan",
    "created_at": "2009-09-02T15:22:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42093",
    "user": "https://trac.sagemath.org/admin/accounts/users/schymans"
}
```

It seems that the problem of cutting off axes labels of large numbers is just a matter of when the axis switches to scientific notation. Consider this:

`sage: plot(2^(20*x),(x,1,2.))`

Only numbers > 1.e+11 are converted to scientific notation, while the smaller ones get cut off. This could be fixed by changing to scientific notation at much smaller numbers. Actually, the change from decimal to scientific notation half way across the axis is something that bothered me in MMA already. Could you either let the user decide which notation to use or make it the same for the whole axis, depending on whether the largest (or smallest) number requires it? 

Just a few ideas for when you get to fixing the matplotlib tick stuff.

Cheers
Stan



---

archive/issue_comments_042094.json:
```json
{
    "body": "Both of you, please make sure you are using the most recent version of the patch (from around the time I posted to sage-devel).  Sorry for the rapid iteration---your feedback has very helpful.\n\n1. Transparency: this should just be an option to show now, so this should work:\n\n\n```\nsage: plot(x^2, (x, 0, 1), transparent=True)\n```\n\n\nOf course, in a web browser, you will \"see\" a white background through the image.  If you save the image, you can \"see\" the transparent background.  Your viewer may not be showing you the transparency easily.\n\n2. Deprecations: Just delete (or update) your .sage/matplotlibrc file.  If you haven't touched that file, then deleting it is fine.\n\n3. scientific notation: I switched to using the \"old\" matplotlib tick formatter in the most recent patch.  I'm not on a computer that has 4.1.1, so I can't test what you are seeing at the moment.  In any case, it will be really easy to do whatever you want with formatting ticks once this patch goes in.",
    "created_at": "2009-09-02T16:34:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42094",
    "user": "https://github.com/jasongrout"
}
```

Both of you, please make sure you are using the most recent version of the patch (from around the time I posted to sage-devel).  Sorry for the rapid iteration---your feedback has very helpful.

1. Transparency: this should just be an option to show now, so this should work:


```
sage: plot(x^2, (x, 0, 1), transparent=True)
```


Of course, in a web browser, you will "see" a white background through the image.  If you save the image, you can "see" the transparent background.  Your viewer may not be showing you the transparency easily.

2. Deprecations: Just delete (or update) your .sage/matplotlibrc file.  If you haven't touched that file, then deleting it is fine.

3. scientific notation: I switched to using the "old" matplotlib tick formatter in the most recent patch.  I'm not on a computer that has 4.1.1, so I can't test what you are seeing at the moment.  In any case, it will be really easy to do whatever you want with formatting ticks once this patch goes in.



---

archive/issue_comments_042095.json:
```json
{
    "body": "Oh, based on the problems I mentioned in the sage-devel thread, I'm not quite comfortable with this going in yet, unless there's an understanding that there is a fix-up patch before the next release.  So I'm changing this back to \"needs work\" for now.  I hope that by the weekend, the issues will be resolved.",
    "created_at": "2009-09-02T16:35:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42095",
    "user": "https://github.com/jasongrout"
}
```

Oh, based on the problems I mentioned in the sage-devel thread, I'm not quite comfortable with this going in yet, unless there's an understanding that there is a fix-up patch before the next release.  So I'm changing this back to "needs work" for now.  I hope that by the weekend, the issues will be resolved.



---

archive/issue_comments_042096.json:
```json
{
    "body": "And one more thing needs to be done: documentation! (for the new functions added, and check the documentation for functions that were changed).",
    "created_at": "2009-09-02T16:51:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42096",
    "user": "https://github.com/jasongrout"
}
```

And one more thing needs to be done: documentation! (for the new functions added, and check the documentation for functions that were changed).



---

archive/issue_comments_042097.json:
```json
{
    "body": "Attachment [trac-5448-matplotlib-axes-gridlines.2.patch](tarball://root/attachments/some-uuid/ticket5448/trac-5448-matplotlib-axes-gridlines.2.patch) by @jasongrout created at 2009-09-05 03:54:34\n\napply instead of previous patches",
    "created_at": "2009-09-05T03:54:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42097",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-5448-matplotlib-axes-gridlines.2.patch](tarball://root/attachments/some-uuid/ticket5448/trac-5448-matplotlib-axes-gridlines.2.patch) by @jasongrout created at 2009-09-05 03:54:34

apply instead of previous patches



---

archive/issue_comments_042098.json:
```json
{
    "body": "Attachment [trac-5448-matplotlib-axes-gridlines.3.patch](tarball://root/attachments/some-uuid/ticket5448/trac-5448-matplotlib-axes-gridlines.3.patch) by @jasongrout created at 2009-09-05 04:12:35",
    "created_at": "2009-09-05T04:12:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42098",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-5448-matplotlib-axes-gridlines.3.patch](tarball://root/attachments/some-uuid/ticket5448/trac-5448-matplotlib-axes-gridlines.3.patch) by @jasongrout created at 2009-09-05 04:12:35



---

archive/issue_comments_042099.json:
```json
{
    "body": "I am deleting the following code from the patch because it is not used right now.  If in the future we want to have more control over the size of the figure, but still want to automatically shrink the plot to fit everything (labels, etc.) inside of the figure without clipping them, then the following code will prove useful.  I'm pasting the code here so that it is some sort of permanent record.\n\n\nThis is an extension of an idea in the matplotlib FAQ.\n\n\n```\n# Put the following somewhere in your routine that saves the file, after you've created the FigureCanvas object, but before you've actually saved the canvas.\n\n#canvas.mpl_connect('draw_event', on_draw)\n\ndef on_draw(event):\n    \"\"\"\n    TODO: write documentation\n    \"\"\"\n    import matplotlib.transforms as mtransforms\n    figure=event.canvas.figure\n    bboxes = []\n    for ax in figure.axes:\n        bbox = ax.xaxis.get_label().get_window_extent()\n        # the figure transform goes from relative coords->pixels and we\n        # want the inverse of that\n        bboxi = bbox.inverse_transformed(figure.transFigure)\n        bboxes.append(bboxi)\n\n        bbox = ax.yaxis.get_label().get_window_extent()\n        bboxi = bbox.inverse_transformed(figure.transFigure)\n        bboxes.append(bboxi)\n        for label in (ax.get_xticklabels()+ax.get_yticklabels() \\\n                          + ax.get_xticklabels(minor=True) \\\n                          +ax.get_yticklabels(minor=True)):\n            bbox = label.get_window_extent()\n            bboxi = bbox.inverse_transformed(figure.transFigure)\n            bboxes.append(bboxi)\n    \n    # this is the bbox that bounds all the bboxes, again in relative\n    # figure coords\n    bbox = mtransforms.Bbox.union(bboxes)\n    adjusted=adjust_figure_to_contain_bbox(figure,bbox)\n    \n    if adjusted:\n        figure.canvas.draw()\n    return False\n\ndef adjust_figure_to_contain_bbox(fig, bbox):\n    \"\"\"\n    TODO: write documentation\n    \"\"\"\n    adjusted=False\n    if bbox.xmin<0:\n        fig.subplots_adjust(left=fig.subplotpars.left-bbox.xmin)\n        adjusted=True\n    if bbox.ymin<0:\n        fig.subplots_adjust(bottom=fig.subplotpars.bottom-bbox.ymin)\n        adjusted=True\n    if bbox.xmax>1:\n        fig.subplots_adjust(right=fig.subplotpars.right-(bbox.xmax-1))\n        adjusted=True\n    if bbox.ymax>1:\n        fig.subplots_adjust(top=fig.subplotpars.top-(bbox.ymax-1))\n        adjusted=True\n    return adjusted\n```\n",
    "created_at": "2009-09-05T05:15:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42099",
    "user": "https://github.com/jasongrout"
}
```

I am deleting the following code from the patch because it is not used right now.  If in the future we want to have more control over the size of the figure, but still want to automatically shrink the plot to fit everything (labels, etc.) inside of the figure without clipping them, then the following code will prove useful.  I'm pasting the code here so that it is some sort of permanent record.


This is an extension of an idea in the matplotlib FAQ.


```
# Put the following somewhere in your routine that saves the file, after you've created the FigureCanvas object, but before you've actually saved the canvas.

#canvas.mpl_connect('draw_event', on_draw)

def on_draw(event):
    """
    TODO: write documentation
    """
    import matplotlib.transforms as mtransforms
    figure=event.canvas.figure
    bboxes = []
    for ax in figure.axes:
        bbox = ax.xaxis.get_label().get_window_extent()
        # the figure transform goes from relative coords->pixels and we
        # want the inverse of that
        bboxi = bbox.inverse_transformed(figure.transFigure)
        bboxes.append(bboxi)

        bbox = ax.yaxis.get_label().get_window_extent()
        bboxi = bbox.inverse_transformed(figure.transFigure)
        bboxes.append(bboxi)
        for label in (ax.get_xticklabels()+ax.get_yticklabels() \
                          + ax.get_xticklabels(minor=True) \
                          +ax.get_yticklabels(minor=True)):
            bbox = label.get_window_extent()
            bboxi = bbox.inverse_transformed(figure.transFigure)
            bboxes.append(bboxi)
    
    # this is the bbox that bounds all the bboxes, again in relative
    # figure coords
    bbox = mtransforms.Bbox.union(bboxes)
    adjusted=adjust_figure_to_contain_bbox(figure,bbox)
    
    if adjusted:
        figure.canvas.draw()
    return False

def adjust_figure_to_contain_bbox(fig, bbox):
    """
    TODO: write documentation
    """
    adjusted=False
    if bbox.xmin<0:
        fig.subplots_adjust(left=fig.subplotpars.left-bbox.xmin)
        adjusted=True
    if bbox.ymin<0:
        fig.subplots_adjust(bottom=fig.subplotpars.bottom-bbox.ymin)
        adjusted=True
    if bbox.xmax>1:
        fig.subplots_adjust(right=fig.subplotpars.right-(bbox.xmax-1))
        adjusted=True
    if bbox.ymax>1:
        fig.subplots_adjust(top=fig.subplotpars.top-(bbox.ymax-1))
        adjusted=True
    return adjusted
```




---

archive/issue_comments_042100.json:
```json
{
    "body": "Attachment [trac-5448-matplotlib-axes-gridlines.4.patch](tarball://root/attachments/some-uuid/ticket5448/trac-5448-matplotlib-axes-gridlines.4.patch) by @jasongrout created at 2009-09-05 09:01:40\n\napply instead of previous patches",
    "created_at": "2009-09-05T09:01:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42100",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-5448-matplotlib-axes-gridlines.4.patch](tarball://root/attachments/some-uuid/ticket5448/trac-5448-matplotlib-axes-gridlines.4.patch) by @jasongrout created at 2009-09-05 09:01:40

apply instead of previous patches



---

archive/issue_comments_042101.json:
```json
{
    "body": "I believe I've taken care of all outstanding issues, so this patch is ready to be (re-)reviewed.",
    "created_at": "2009-09-05T09:04:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42101",
    "user": "https://github.com/jasongrout"
}
```

I believe I've taken care of all outstanding issues, so this patch is ready to be (re-)reviewed.



---

archive/issue_comments_042102.json:
```json
{
    "body": "I've moved Mike's plot.patch to #6893, so that patch can be deleted from this ticket.  In fact, all patches except for trac-5448-matplotlib-axes-gridlines.4.patch can be deleted from this ticket.",
    "created_at": "2009-09-05T09:10:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42102",
    "user": "https://github.com/jasongrout"
}
```

I've moved Mike's plot.patch to #6893, so that patch can be deleted from this ticket.  In fact, all patches except for trac-5448-matplotlib-axes-gridlines.4.patch can be deleted from this ticket.



---

archive/issue_comments_042103.json:
```json
{
    "body": "Positive review - behaves as advertised after actually viewing many, many of the plots in the sage/plot/ directory, and testing on a few others which had given trouble before.   \n\nI look forward to doing custom axes soon; perhaps that should be wrapped, and then a few other tickets could be closed.  These might include (not just axes-related, and not necessarily, but worth checking into) #6548, #5645, #5128, #4689, #4384, #4194, #2900, #2189, and #1431.  Good things; transparent definitely DOES now work, complex plots and matrix plots look better because they're \"set off\" a bit, etc. \n\nHere are things to address in a follow-up ticket, at least maybe:\n\nContour plot - if fill=False and contours are grayscale, the axes could be misinterpreted\n\nContour plot - show(axes=False) and show(axes=True) seem to be identical on the last example\n\nPlotting - how well documented is the new axis behavior, where it does NOT intersect? This should be clear, e.g. the Riemann zeta example in plot.py looks funny, until you realize it's from 1 to 27.  It still seems weird to me when it's that close, but I suppose it's okay as long as it is very very clear in documentation.\n\nAxis labels - should point out difference between ['x','y'] and ['$x$','$y$'].  Some people might not like the LaTeXed version\n\nWhen scientific notation comes into play is not always clear, and should be in the documentation - compare plot(x**2, 490,500) and plot(x**2,-490,500), which have the same \"height\" but only one gets e, presumably since it covers a larger range",
    "created_at": "2009-09-06T02:37:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42103",
    "user": "https://github.com/kcrisman"
}
```

Positive review - behaves as advertised after actually viewing many, many of the plots in the sage/plot/ directory, and testing on a few others which had given trouble before.   

I look forward to doing custom axes soon; perhaps that should be wrapped, and then a few other tickets could be closed.  These might include (not just axes-related, and not necessarily, but worth checking into) #6548, #5645, #5128, #4689, #4384, #4194, #2900, #2189, and #1431.  Good things; transparent definitely DOES now work, complex plots and matrix plots look better because they're "set off" a bit, etc. 

Here are things to address in a follow-up ticket, at least maybe:

Contour plot - if fill=False and contours are grayscale, the axes could be misinterpreted

Contour plot - show(axes=False) and show(axes=True) seem to be identical on the last example

Plotting - how well documented is the new axis behavior, where it does NOT intersect? This should be clear, e.g. the Riemann zeta example in plot.py looks funny, until you realize it's from 1 to 27.  It still seems weird to me when it's that close, but I suppose it's okay as long as it is very very clear in documentation.

Axis labels - should point out difference between ['x','y'] and ['$x$','$y$'].  Some people might not like the LaTeXed version

When scientific notation comes into play is not always clear, and should be in the documentation - compare plot(x**2, 490,500) and plot(x**2,-490,500), which have the same "height" but only one gets e, presumably since it covers a larger range



---

archive/issue_comments_042104.json:
```json
{
    "body": "Merged `trac-5448-matplotlib-axes-gridlines.4.patch`. The updated packages `matplotlib-0.99.0.spkg` and `networkx-0.99.p1-fake_really-0.36.p1.spkg` are merged in the standard packages repository.",
    "created_at": "2009-09-07T18:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42104",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged `trac-5448-matplotlib-axes-gridlines.4.patch`. The updated packages `matplotlib-0.99.0.spkg` and `networkx-0.99.p1-fake_really-0.36.p1.spkg` are merged in the standard packages repository.



---

archive/issue_comments_042105.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-07T18:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5448#issuecomment-42105",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_005700.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-07T18:25:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5448",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5448#event-5700"
}
```
