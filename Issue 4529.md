# Issue 4529: Implement plots with logarithmic scale

archive/issues_004529.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: plot log scale\n\nCurrently plot() has no option to use logarithmic scales.\n\nOne workaround is to use matplotlib directly, with its semilogy(), semilogx() and loglog() functions, but that wouldn't produce plots with the customisations implemented in sage.\nAnother workaround is messing with the plot figure like:\n\n\n```python\nimport pylab\np=plot(x,marker='.')\nf=pylab.figure()\nf.gca().set_xscale('log')\np.save(figure=f)\n```\n\n\nBut that creates two problems:\n\n* The first problem is that the adaptive choosing of points just considers linear scale, so the points get too much spaced apart in the beginning of the plot and too close in the end.\n* The second problem relates to the axis, which, for the same reason, isn't located right.\n\nAlso, this requires the user to know how to deal with figures, which is not directly exposed by sage.\n\nThere are some possibilities to fix that:\n1. Make plot() detect if the figure changes the scales and modify the adaptive algorithm and the axis codes accordingly\n2. Create a kwarg to tell plot() to implement the scale-change internally\n3. Create other functions to use loglog(), semilogx() and semilogy()\n4. Many (or all) of the above together, since they aren't mutually exclusive\n\nFrom what I noticed, Mathematica implements the separate functions way, but it may be better to fix the issue in plot() itself and if the other functions are wanted, just make it so that they call plot() with the correct arguments\n\nIssue created by migration from https://trac.sagemath.org/ticket/4529\n\n",
    "created_at": "2008-11-15T18:59:14Z",
    "labels": [
        "component: graphics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.2",
    "title": "Implement plots with logarithmic scale",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4529",
    "user": "https://trac.sagemath.org/admin/accounts/users/ronanpaixao"
}
```
Assignee: somebody

Keywords: plot log scale

Currently plot() has no option to use logarithmic scales.

One workaround is to use matplotlib directly, with its semilogy(), semilogx() and loglog() functions, but that wouldn't produce plots with the customisations implemented in sage.
Another workaround is messing with the plot figure like:


```python
import pylab
p=plot(x,marker='.')
f=pylab.figure()
f.gca().set_xscale('log')
p.save(figure=f)
```


But that creates two problems:

* The first problem is that the adaptive choosing of points just considers linear scale, so the points get too much spaced apart in the beginning of the plot and too close in the end.
* The second problem relates to the axis, which, for the same reason, isn't located right.

Also, this requires the user to know how to deal with figures, which is not directly exposed by sage.

There are some possibilities to fix that:
1. Make plot() detect if the figure changes the scales and modify the adaptive algorithm and the axis codes accordingly
2. Create a kwarg to tell plot() to implement the scale-change internally
3. Create other functions to use loglog(), semilogx() and semilogy()
4. Many (or all) of the above together, since they aren't mutually exclusive

From what I noticed, Mathematica implements the separate functions way, but it may be better to fix the issue in plot() itself and if the other functions are wanted, just make it so that they call plot() with the correct arguments

Issue created by migration from https://trac.sagemath.org/ticket/4529





---

archive/issue_comments_033562.json:
```json
{
    "body": "Attachment [sage0.png](tarball://root/attachments/some-uuid/ticket4529/sage0.png) by ronanpaixao created at 2008-11-15 18:59:49\n\n\"Wrong\" sage plot with log scale",
    "created_at": "2008-11-15T18:59:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33562",
    "user": "https://trac.sagemath.org/admin/accounts/users/ronanpaixao"
}
```

Attachment [sage0.png](tarball://root/attachments/some-uuid/ticket4529/sage0.png) by ronanpaixao created at 2008-11-15 18:59:49

"Wrong" sage plot with log scale



---

archive/issue_comments_033563.json:
```json
{
    "body": "This is a dupe if #4530\n\nCheers,\n\nMichael",
    "created_at": "2008-11-15T19:03:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33563",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is a dupe if #4530

Cheers,

Michael



---

archive/issue_events_004773.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-11-15T19:03:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4529#event-4773"
}
```



---

archive/issue_comments_033564.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-11-15T19:03:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33564",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: duplicate



---

archive/issue_comments_033565.json:
```json
{
    "body": "Resolution changed from duplicate to ",
    "created_at": "2008-11-15T19:04:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33565",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution changed from duplicate to 



---

archive/issue_comments_033566.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-11-15T19:04:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33566",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_events_004774.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-11-15T19:04:04Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4529#event-4774"
}
```



---

archive/issue_comments_033567.json:
```json
{
    "body": "Changing status from reopened to new.",
    "created_at": "2008-11-15T19:04:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33567",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from reopened to new.



---

archive/issue_comments_033568.json:
```json
{
    "body": "Changing assignee from somebody to ronanpaixao.",
    "created_at": "2008-11-15T19:04:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33568",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from somebody to ronanpaixao.



---

archive/issue_comments_033569.json:
```json
{
    "body": "See #1431 for a way to solve this.",
    "created_at": "2009-11-12T04:13:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33569",
    "user": "https://github.com/jasongrout"
}
```

See #1431 for a way to solve this.



---

archive/issue_comments_033570.json:
```json
{
    "body": "Since #1431 ended up just being about ticks (not the scale), #1431 doesn't directly address how to change the scale of the plot.",
    "created_at": "2011-10-13T13:57:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33570",
    "user": "https://github.com/jasongrout"
}
```

Since #1431 ended up just being about ticks (not the scale), #1431 doesn't directly address how to change the scale of the plot.



---

archive/issue_comments_033571.json:
```json
{
    "body": "Here are some comments about an API.  How about adding a show keyword that specifies the scale of the axes.  \n\n`scale='log'` -- a string specifies the scale of the vertical axis\n\n`scale=('log','linear')` -- a tuple or list of two strings specifies scales for both axes\n\nWe'd probably like some way to pass in arguments to the scale, since different scales have different options.  This looks ugly: `scale=( ('log', {'base': 2}), 'linear')`",
    "created_at": "2011-10-13T14:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33571",
    "user": "https://github.com/jasongrout"
}
```

Here are some comments about an API.  How about adding a show keyword that specifies the scale of the axes.  

`scale='log'` -- a string specifies the scale of the vertical axis

`scale=('log','linear')` -- a tuple or list of two strings specifies scales for both axes

We'd probably like some way to pass in arguments to the scale, since different scales have different options.  This looks ugly: `scale=( ('log', {'base': 2}), 'linear')`



---

archive/issue_comments_033572.json:
```json
{
    "body": "We could also do something like `xscale='log'` or `xscale=('log',{'base': 2})` and similarly for yscale.  I don't like using x and y, though, since the variables in the plot might not be x and y.",
    "created_at": "2011-10-13T14:33:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33572",
    "user": "https://github.com/jasongrout"
}
```

We could also do something like `xscale='log'` or `xscale=('log',{'base': 2})` and similarly for yscale.  I don't like using x and y, though, since the variables in the plot might not be x and y.



---

archive/issue_comments_033573.json:
```json
{
    "body": "My sense is that the API should look like the tick marks API.   \n\nHere are some comments Jason made on sage-support about this.\n\n```\n> To change the scale, you can modify the plot afterwards, but I am \n> running into some sort of problem doing it: \n> sage: p=plot(e^x,(x,0,10)) \n> sage: m=p.matplotlib() \n> sage: from matplotlib.backends.backend_agg import FigureCanvasAgg \n> sage: m.set_canvas(FigureCanvasAgg(m)) \n> sage: m.gca().set_yscale('log') \n> sage: m.savefig('test.png') \n\n\nIt seems something was wrong with the plot in the above example, or \nsomething.  Anyways, starting with: \np=plot(x,(x,1,10)) \nworks fine. \nTo do #4529, I'd suggest adding a keyword to show that defines the \nscales of the x and y axes.  I've added some comments to the ticket. \n```\n\n\n----\n\nHow was I not cc:ed on this ticket before?  ;-)",
    "created_at": "2011-10-13T15:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33573",
    "user": "https://github.com/kcrisman"
}
```

My sense is that the API should look like the tick marks API.   

Here are some comments Jason made on sage-support about this.

```
> To change the scale, you can modify the plot afterwards, but I am 
> running into some sort of problem doing it: 
> sage: p=plot(e^x,(x,0,10)) 
> sage: m=p.matplotlib() 
> sage: from matplotlib.backends.backend_agg import FigureCanvasAgg 
> sage: m.set_canvas(FigureCanvasAgg(m)) 
> sage: m.gca().set_yscale('log') 
> sage: m.savefig('test.png') 


It seems something was wrong with the plot in the above example, or 
something.  Anyways, starting with: 
p=plot(x,(x,1,10)) 
works fine. 
To do #4529, I'd suggest adding a keyword to show that defines the 
scales of the x and y axes.  I've added some comments to the ticket. 
```


----

How was I not cc:ed on this ticket before?  ;-)



---

archive/issue_comments_033574.json:
```json
{
    "body": "Also, #5128 would appear to be slightly related.",
    "created_at": "2011-10-13T15:44:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33574",
    "user": "https://github.com/kcrisman"
}
```

Also, #5128 would appear to be slightly related.



---

archive/issue_comments_033575.json:
```json
{
    "body": "The error with `e^x` is \n\n```\nMaskError: Cannot convert masked element to a Python int.\n```\n\nbut seems to be related to there being something other than linearity involved.  Linear functions work, anything with `^` or `**` or `sin` doesn't.\n\n```\n--> 154         self._renderer.draw_text_image(font.get_image(), int(x), int(y) + 1, angle, gc)\n```\n\nis the problem - it's converting one of the elements, which is supposed to be skipped (masked, right?) to an int.",
    "created_at": "2011-10-13T15:48:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33575",
    "user": "https://github.com/kcrisman"
}
```

The error with `e^x` is 

```
MaskError: Cannot convert masked element to a Python int.
```

but seems to be related to there being something other than linearity involved.  Linear functions work, anything with `^` or `**` or `sin` doesn't.

```
--> 154         self._renderer.draw_text_image(font.get_image(), int(x), int(y) + 1, angle, gc)
```

is the problem - it's converting one of the elements, which is supposed to be skipped (masked, right?) to an int.



---

archive/issue_comments_033576.json:
```json
{
    "body": "plot in logarithmic scale.",
    "created_at": "2012-02-08T12:44:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33576",
    "user": "https://github.com/ppurka"
}
```

plot in logarithmic scale.



---

archive/issue_comments_033577.json:
```json
{
    "body": "Attachment [logplots.py](tarball://root/attachments/some-uuid/ticket4529/logplots.py) by @ppurka created at 2012-02-08 12:50:17\n\n[attachment:logplots.py] has a new class `LogGraphics` that I implemented and have been using for the past few months. Integrating it with Graphics seemed quite a painful process, so I had to go this direction and make my own class. Currently, it handles many *but not all* of the arguments that the `Graphics` class supports. In addition it uses `matplotlib.plt` to do the log plot; otherwise I ran into all sorts of problems with matplotlib (like the ones mentioned in earlier comments).\n\nIn engineering, we often need logarithmic plots and the logarithmic plots sometimes is of the form that the x-axis *decreases* as we go towards the right (for example if we plot decreasing probabilities on the x-axis). This `LogGraphics` takes this into account and makes sure that if a list of x-axis points with decreasing values along the higher indices of the list, then it plots the graph with a decreasing x-axis.",
    "created_at": "2012-02-08T12:50:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33577",
    "user": "https://github.com/ppurka"
}
```

Attachment [logplots.py](tarball://root/attachments/some-uuid/ticket4529/logplots.py) by @ppurka created at 2012-02-08 12:50:17

[attachment:logplots.py] has a new class `LogGraphics` that I implemented and have been using for the past few months. Integrating it with Graphics seemed quite a painful process, so I had to go this direction and make my own class. Currently, it handles many *but not all* of the arguments that the `Graphics` class supports. In addition it uses `matplotlib.plt` to do the log plot; otherwise I ran into all sorts of problems with matplotlib (like the ones mentioned in earlier comments).

In engineering, we often need logarithmic plots and the logarithmic plots sometimes is of the form that the x-axis *decreases* as we go towards the right (for example if we plot decreasing probabilities on the x-axis). This `LogGraphics` takes this into account and makes sure that if a list of x-axis points with decreasing values along the higher indices of the list, then it plots the graph with a decreasing x-axis.



---

archive/issue_comments_033578.json:
```json
{
    "body": "Sorry, I meant `matplotlib.pyplot` in the above comment.",
    "created_at": "2012-02-08T13:02:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33578",
    "user": "https://github.com/ppurka"
}
```

Sorry, I meant `matplotlib.pyplot` in the above comment.



---

archive/issue_comments_033579.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-04-18T02:15:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33579",
    "user": "https://github.com/eviatarbach"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_033580.json:
```json
{
    "body": "I am not sure if this needs to be set to \"needs_review\". The main thing it is lacking is that it doesn't inherit the `Graphics` class, and hence the set of plot options it supports is much less.\n\nOn the other hand, I did try to make it inherit the `Graphics` class but then I ran into a big hurdle: the variables in the `Graphics` class are defined with double underscore `__` and so even after I inherit it, I need to use (IMHO ugly) setters and getters in order to access those variables. I tried to overcome this limitation by inheriting `Graphics` in the class `LogGraphics` and defining a separate (and mostly identical) `__init__` in `LogGraphics` but then the methods wouldn't work. Since I needed to rewrite almost everything, I decided to just rewrite everything from scratch.\n\nOne thing that I plan to do is change all the variables in the `Graphics` class to be defined with a single `_` and see how it works out. Perhaps then it might be possible to integrate this patch better and consequently have access to all the methods (and hence plot options) available to the `plot` command.",
    "created_at": "2012-04-18T06:37:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33580",
    "user": "https://github.com/ppurka"
}
```

I am not sure if this needs to be set to "needs_review". The main thing it is lacking is that it doesn't inherit the `Graphics` class, and hence the set of plot options it supports is much less.

On the other hand, I did try to make it inherit the `Graphics` class but then I ran into a big hurdle: the variables in the `Graphics` class are defined with double underscore `__` and so even after I inherit it, I need to use (IMHO ugly) setters and getters in order to access those variables. I tried to overcome this limitation by inheriting `Graphics` in the class `LogGraphics` and defining a separate (and mostly identical) `__init__` in `LogGraphics` but then the methods wouldn't work. Since I needed to rewrite almost everything, I decided to just rewrite everything from scratch.

One thing that I plan to do is change all the variables in the `Graphics` class to be defined with a single `_` and see how it works out. Perhaps then it might be possible to integrate this patch better and consequently have access to all the methods (and hence plot options) available to the `plot` command.



---

archive/issue_comments_033581.json:
```json
{
    "body": "Hmm, that's odd that you had to do this.   Here are two \"Sage-ic\" ideas.\n* Have it inherit from `GraphicPrimitive`.  That is how most classes are done, and hopefully (?) would work.\n* Have this be a `show` option, or something like that.  In principle, we wouldn't even want the graphic itself to be plotted logarithmically; one could imagine wanting to have a `Line` or other plot and then to view it with log, semilog, reverse log, or regular scales.  See Jason's wise comment:7.",
    "created_at": "2012-04-18T14:21:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33581",
    "user": "https://github.com/kcrisman"
}
```

Hmm, that's odd that you had to do this.   Here are two "Sage-ic" ideas.
* Have it inherit from `GraphicPrimitive`.  That is how most classes are done, and hopefully (?) would work.
* Have this be a `show` option, or something like that.  In principle, we wouldn't even want the graphic itself to be plotted logarithmically; one could imagine wanting to have a `Line` or other plot and then to view it with log, semilog, reverse log, or regular scales.  See Jason's wise comment:7.



---

archive/issue_comments_033582.json:
```json
{
    "body": "* `GraphicsPrimitive` is unfortunately too crude for most purposes. All the important functions are defined in `Graphics`.\n* I did try using `_render_on_subplot` from `line.py` but ran into the same problem as you described in comment:9. It simply doesn't work since matplotlib fails to re-render the line in log scale. Actually I ran into many more problems; I just can't remember what else. The most painless method seemed to be to use pyplot (or even pylab, but we can avoid importing that since we don't need numpy).\n\nThat said, it is IMHO better to have logarithmic plots as a separate class. For instance, it doesn't make much sense to \"add\" plots with different scalings (and I also raise an error in the class I created).",
    "created_at": "2012-04-18T15:29:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33582",
    "user": "https://github.com/ppurka"
}
```

* `GraphicsPrimitive` is unfortunately too crude for most purposes. All the important functions are defined in `Graphics`.
* I did try using `_render_on_subplot` from `line.py` but ran into the same problem as you described in comment:9. It simply doesn't work since matplotlib fails to re-render the line in log scale. Actually I ran into many more problems; I just can't remember what else. The most painless method seemed to be to use pyplot (or even pylab, but we can avoid importing that since we don't need numpy).

That said, it is IMHO better to have logarithmic plots as a separate class. For instance, it doesn't make much sense to "add" plots with different scalings (and I also raise an error in the class I created).



---

archive/issue_comments_033583.json:
```json
{
    "body": "I'm currently cleaning up tickets marked needs_review which have no patches attached, which includes this one, so back to needs_work this goes.",
    "created_at": "2012-05-16T14:09:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33583",
    "user": "https://github.com/kini"
}
```

I'm currently cleaning up tickets marked needs_review which have no patches attached, which includes this one, so back to needs_work this goes.



---

archive/issue_comments_033584.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-05-16T14:09:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33584",
    "user": "https://github.com/kini"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_033585.json:
```json
{
    "body": "Replying to [comment:18 kini]:\n> I'm currently cleaning up tickets marked needs_review which have no patches attached, which includes this one, so back to needs_work this goes.\n\nThat's fine. I am actually working on a patch which\n1. modifies the `Graphics` class to have all the attributes start with a single underscore `._` instead of `.__`. This is already working and passes all doctects at least in `devel/sage/sage/plot`\n2. inherits the `Graphics` class and introduces logarithmic plots in a separate file. This is in progress and I hope I have a patch to attach to this ticket soon.",
    "created_at": "2012-05-16T16:20:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33585",
    "user": "https://github.com/ppurka"
}
```

Replying to [comment:18 kini]:
> I'm currently cleaning up tickets marked needs_review which have no patches attached, which includes this one, so back to needs_work this goes.

That's fine. I am actually working on a patch which
1. modifies the `Graphics` class to have all the attributes start with a single underscore `._` instead of `.__`. This is already working and passes all doctects at least in `devel/sage/sage/plot`
2. inherits the `Graphics` class and introduces logarithmic plots in a separate file. This is in progress and I hope I have a patch to attach to this ticket soon.



---

archive/issue_comments_033586.json:
```json
{
    "body": "Awesome.  Just yesterday I had a feature request for log-log and semilog plots!",
    "created_at": "2012-05-16T16:33:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33586",
    "user": "https://github.com/jasongrout"
}
```

Awesome.  Just yesterday I had a feature request for log-log and semilog plots!



---

archive/issue_comments_033587.json:
```json
{
    "body": "I added a patch to `Graphics` class which introduces log plots. Some salient points\n1. I had to \"disable\" some tick formatting for log plots because matplotlib wasn't behaving well with the formatting that is done in `Graphics().maptplotlib()` (ex. the error in comment:11, out of memory error, etc)\n2. The patch in this ticket relies on the patches in #12974 which is mostly a cleanup of the `Graphics` class.\n3. In trying to implement my own class, I started to look at each of the matplotlib functions more carefully, and found out the reason(s) why setting the scale wasn't working (see point 1.). The result is that I could implement log scale right inside `Graphics` by carefully weeding out the corner cases. I hope I got all the corner cases.\n\nTodo:\n1. A patch to `plot()` and other functions will take more time to implement. :(\n2. Probably need to make sure that user does not specify tick formatters and locators which don't behave well with log plots.\n3. Feedback is welcome! I need to know if I missed something.\n\nExample code:\n\n```\np = plot(exp, 1, 10)\np.set_scale('loglog')\np.show()\nxd=range(-5,5); yd=[10**_ for _ in xd]; p=list_plot(zip(xd, yd),plotjoined=True)\np.set_yscale('log', 2) # Set only y-axis to log and with base of log being 2.\np.show()\n```\n",
    "created_at": "2012-05-19T13:12:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33587",
    "user": "https://github.com/ppurka"
}
```

I added a patch to `Graphics` class which introduces log plots. Some salient points
1. I had to "disable" some tick formatting for log plots because matplotlib wasn't behaving well with the formatting that is done in `Graphics().maptplotlib()` (ex. the error in comment:11, out of memory error, etc)
2. The patch in this ticket relies on the patches in #12974 which is mostly a cleanup of the `Graphics` class.
3. In trying to implement my own class, I started to look at each of the matplotlib functions more carefully, and found out the reason(s) why setting the scale wasn't working (see point 1.). The result is that I could implement log scale right inside `Graphics` by carefully weeding out the corner cases. I hope I got all the corner cases.

Todo:
1. A patch to `plot()` and other functions will take more time to implement. :(
2. Probably need to make sure that user does not specify tick formatters and locators which don't behave well with log plots.
3. Feedback is welcome! I need to know if I missed something.

Example code:

```
p = plot(exp, 1, 10)
p.set_scale('loglog')
p.show()
xd=range(-5,5); yd=[10**_ for _ in xd]; p=list_plot(zip(xd, yd),plotjoined=True)
p.set_yscale('log', 2) # Set only y-axis to log and with base of log being 2.
p.show()
```




---

archive/issue_comments_033588.json:
```json
{
    "body": "Hmm.. there is still a problem if I modify the `Graphics` class. It becomes impossible to add 2D and 3D graphics.",
    "created_at": "2012-05-19T16:07:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33588",
    "user": "https://github.com/ppurka"
}
```

Hmm.. there is still a problem if I modify the `Graphics` class. It becomes impossible to add 2D and 3D graphics.



---

archive/issue_comments_033589.json:
```json
{
    "body": "Replying to [comment:22 ppurka]:\n> Hmm.. there is still a problem if I modify the `Graphics` class. It becomes impossible to add 2D and 3D graphics.\n\nIt was a silly thing. I just needed to reorder the check for `._*scale` to after the check for `Graphics3d` in `__add__()`. The updated patch now passes all doctests in `sage/plot`! Also, `SHOW_OPTIONS, matplotlib()` have two extra arguments: `scale`, `base` which are identical in behavior to the arguments in `set_scale()`. So, now it is possible to do this:\n\n```\np = plot(exp, 1, 10)\np.show(scale=('loglog', 2))\n```\n",
    "created_at": "2012-05-20T10:59:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33589",
    "user": "https://github.com/ppurka"
}
```

Replying to [comment:22 ppurka]:
> Hmm.. there is still a problem if I modify the `Graphics` class. It becomes impossible to add 2D and 3D graphics.

It was a silly thing. I just needed to reorder the check for `._*scale` to after the check for `Graphics3d` in `__add__()`. The updated patch now passes all doctests in `sage/plot`! Also, `SHOW_OPTIONS, matplotlib()` have two extra arguments: `scale`, `base` which are identical in behavior to the arguments in `set_scale()`. So, now it is possible to do this:

```
p = plot(exp, 1, 10)
p.show(scale=('loglog', 2))
```




---

archive/issue_comments_033590.json:
```json
{
    "body": "Apply to devel/sage",
    "created_at": "2012-05-20T17:13:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33590",
    "user": "https://github.com/ppurka"
}
```

Apply to devel/sage



---

archive/issue_comments_033591.json:
```json
{
    "body": "Attachment [trac_4529-add_docs_eg_to_some_user_facing_functions.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-add_docs_eg_to_some_user_facing_functions.patch) by @ppurka created at 2012-05-20 17:14:13\n\nApply to devel/sage",
    "created_at": "2012-05-20T17:14:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33591",
    "user": "https://github.com/ppurka"
}
```

Attachment [trac_4529-add_docs_eg_to_some_user_facing_functions.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-add_docs_eg_to_some_user_facing_functions.patch) by @ppurka created at 2012-05-20 17:14:13

Apply to devel/sage



---

archive/issue_comments_033592.json:
```json
{
    "body": "Added [attachment:trac_4529-add_docs_eg_to_some_user_facing_functions.patch another patch] to other user facing functions. Actually most of the functions in `sage.plot.*` work when `scale=...` is passed as an argument while calling the function. Using the log scale makes sense in only a couple of them though, and I have added some documentation and examples for the cases I think are pertinent.\n\nFinally, I added some extra functions `{loglog,semilogx,semilogy}_plot`, and the corresponding list_plots. I think this should undergo a review now.\n\nThese set of patches passes all doctests in `devel/sage/sage/plot`.",
    "created_at": "2012-05-20T17:17:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33592",
    "user": "https://github.com/ppurka"
}
```

Added [attachment:trac_4529-add_docs_eg_to_some_user_facing_functions.patch another patch] to other user facing functions. Actually most of the functions in `sage.plot.*` work when `scale=...` is passed as an argument while calling the function. Using the log scale makes sense in only a couple of them though, and I have added some documentation and examples for the cases I think are pertinent.

Finally, I added some extra functions `{loglog,semilogx,semilogy}_plot`, and the corresponding list_plots. I think this should undergo a review now.

These set of patches passes all doctests in `devel/sage/sage/plot`.



---

archive/issue_comments_033593.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-05-20T17:17:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33593",
    "user": "https://github.com/ppurka"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_033594.json:
```json
{
    "body": "Patchbot:  Apply [attachment:trac_4529-add_logscale_to_Graphics.patch] and [attachment:trac_4529-add_docs_eg_to_some_user_facing_functions.patch].",
    "created_at": "2012-05-24T22:39:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33594",
    "user": "https://github.com/kcrisman"
}
```

Patchbot:  Apply [attachment:trac_4529-add_logscale_to_Graphics.patch] and [attachment:trac_4529-add_docs_eg_to_some_user_facing_functions.patch].



---

archive/issue_comments_033595.json:
```json
{
    "body": "I hope to be able to go over this very valuable idea at the current Bug Days.  Trivial comment while I'm doing a cursory read-through \n\n```\n- ``linear`` -- both the axes are linear. \n```\n\nshould probably indicate \n\n```\n- ``'linear'`` -- both the axes are linear. \n```\n\nor \n\n```\n- 'linear' -- both the axes are linear. \n```\n\nand similarly in all other cases, especially when looking at inputs (since it's very important that these are strings, not just commands.\n\n\n----\nComments:\n\n* I feel like it would be good to have a little discussion about whether the scale should be \"hardcoded\" into a Graphics object; somehow this feels not right to me, though I'd hate to ignore the work here for that reason.  It just seems better to be able to add plots, then \"show\" them however we want.  Naturally, since a lot of that is set as keywords passed from plot to show, there could be conflicts, but that could be up to the user.\n   Especially since the bulk of the \"work\" done in the code still happens in `show` and friends, I don't see why we couldn't just cherry-pick the keyword `scale` and handle it like we do things like plot tick formatting, separately from `Graphics`.  The interface is cleaner that way.\n\n* Separately, in either case, should we globally import all of these many new functions?  For instance, having the `listplot` variants and `semilogx_list_plot, semilogy_list_plot` both available (as opposed to `semilog_plot(keywords=x or y)`) seems overkill.",
    "created_at": "2012-05-24T22:51:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33595",
    "user": "https://github.com/kcrisman"
}
```

I hope to be able to go over this very valuable idea at the current Bug Days.  Trivial comment while I'm doing a cursory read-through 

```
- ``linear`` -- both the axes are linear. 
```

should probably indicate 

```
- ``'linear'`` -- both the axes are linear. 
```

or 

```
- 'linear' -- both the axes are linear. 
```

and similarly in all other cases, especially when looking at inputs (since it's very important that these are strings, not just commands.


----
Comments:

* I feel like it would be good to have a little discussion about whether the scale should be "hardcoded" into a Graphics object; somehow this feels not right to me, though I'd hate to ignore the work here for that reason.  It just seems better to be able to add plots, then "show" them however we want.  Naturally, since a lot of that is set as keywords passed from plot to show, there could be conflicts, but that could be up to the user.
   Especially since the bulk of the "work" done in the code still happens in `show` and friends, I don't see why we couldn't just cherry-pick the keyword `scale` and handle it like we do things like plot tick formatting, separately from `Graphics`.  The interface is cleaner that way.

* Separately, in either case, should we globally import all of these many new functions?  For instance, having the `listplot` variants and `semilogx_list_plot, semilogy_list_plot` both available (as opposed to `semilog_plot(keywords=x or y)`) seems overkill.



---

archive/issue_comments_033596.json:
```json
{
    "body": "It just seemed easier and cleaner to handle the scaling by hardcoding the scale. I will see how the patch turns out if I don't hardcode it.\n\nMost people will expect the functions `semilog*` and `loglog*` to be present. For instance, matlab has all of those commands (matlab has it only for list plots, the function plotter called `ezplot` does not have it AFAIK), and mathematica has `LogLogPlot` and `LogLinearPlot`.\n\nIf it is not desirable, then we can simply have just two functions `log_plot(scale='loglog'|'semilogx'|'semilogy', funcs, ...)`, and `log_list_plot(scale='loglog'|'semilogx'|'semilogy', data, ...)`.",
    "created_at": "2012-05-24T23:45:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33596",
    "user": "https://github.com/ppurka"
}
```

It just seemed easier and cleaner to handle the scaling by hardcoding the scale. I will see how the patch turns out if I don't hardcode it.

Most people will expect the functions `semilog*` and `loglog*` to be present. For instance, matlab has all of those commands (matlab has it only for list plots, the function plotter called `ezplot` does not have it AFAIK), and mathematica has `LogLogPlot` and `LogLinearPlot`.

If it is not desirable, then we can simply have just two functions `log_plot(scale='loglog'|'semilogx'|'semilogy', funcs, ...)`, and `log_list_plot(scale='loglog'|'semilogx'|'semilogy', data, ...)`.



---

archive/issue_comments_033597.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-05-24T23:45:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33597",
    "user": "https://github.com/ppurka"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_033598.json:
```json
{
    "body": "+1 to having loglog and semilog convenience functions.",
    "created_at": "2012-05-25T00:40:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33598",
    "user": "https://github.com/jasongrout"
}
```

+1 to having loglog and semilog convenience functions.



---

archive/issue_comments_033599.json:
```json
{
    "body": "I think that anything that roughly approximates Mathematica and Matlab is fine, it was just having so many of them that might be a problem.  `log_plot` and `semilog_plot(axis=foo)` or something better would be good, and perhaps a couple similar `list_plot` ones... I have to admit I always just use `points()` instead of `list_plot`, is `list_plot` used as the name in one of these programs?\n\nJason, how **many** would be useful?  It's the `semilogx` and `semilogy` that seems a bit much, though if it's standard in other programs I guess it would be ok.",
    "created_at": "2012-05-25T00:43:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33599",
    "user": "https://github.com/kcrisman"
}
```

I think that anything that roughly approximates Mathematica and Matlab is fine, it was just having so many of them that might be a problem.  `log_plot` and `semilog_plot(axis=foo)` or something better would be good, and perhaps a couple similar `list_plot` ones... I have to admit I always just use `points()` instead of `list_plot`, is `list_plot` used as the name in one of these programs?

Jason, how **many** would be useful?  It's the `semilogx` and `semilogy` that seems a bit much, though if it's standard in other programs I guess it would be ok.



---

archive/issue_comments_033600.json:
```json
{
    "body": "I personally would say a loglog and semilog (defaulting to semilogy) would be good, with an option to switch the semilog to x or y.  I guess a list plot would be convenient too, though I agree with you that points() or line() in general should be used over list_plot.  They are more powerful (mostly) anyway.",
    "created_at": "2012-05-25T00:49:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33600",
    "user": "https://github.com/jasongrout"
}
```

I personally would say a loglog and semilog (defaulting to semilogy) would be good, with an option to switch the semilog to x or y.  I guess a list plot would be convenient too, though I agree with you that points() or line() in general should be used over list_plot.  They are more powerful (mostly) anyway.



---

archive/issue_comments_033601.json:
```json
{
    "body": "Replying to [comment:31 jason]:\n> I personally would say a loglog and semilog (defaulting to semilogy) would be good, with an option to switch the semilog to x or y.  I guess a list plot would be convenient too, though I agree with you that points() or line() in general should be used over list_plot.  They are more powerful (mostly) anyway.\n\nFor *consistency*, we should have just one convention. It is very confusing if the options of `plot` (except for probably `plotjoined` and `data`) are also valid options for `list_plot`, but then we introduce an inconsistency via log plots. So, I would be in favor of either\n1. Don't have any of the `loglog_*, semilog*` and handle scaling only through the `scale` and `base` parameters of `plot` and `list_plot` (and actually all other plots)\n2. Have all the functions `loglog_plot`, `loglog_list_plot` available, and perhaps change `semilog[xy]*` to `semilog*` with an extra optional argument `log_axis='x'/'y'`. In case we follow this second rule, I would like this extra argument to be different from `axis` because it can be confused with `axes=True/False`.\n\nI would really like this issue to be sorted out first.",
    "created_at": "2012-05-25T08:07:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33601",
    "user": "https://github.com/ppurka"
}
```

Replying to [comment:31 jason]:
> I personally would say a loglog and semilog (defaulting to semilogy) would be good, with an option to switch the semilog to x or y.  I guess a list plot would be convenient too, though I agree with you that points() or line() in general should be used over list_plot.  They are more powerful (mostly) anyway.

For *consistency*, we should have just one convention. It is very confusing if the options of `plot` (except for probably `plotjoined` and `data`) are also valid options for `list_plot`, but then we introduce an inconsistency via log plots. So, I would be in favor of either
1. Don't have any of the `loglog_*, semilog*` and handle scaling only through the `scale` and `base` parameters of `plot` and `list_plot` (and actually all other plots)
2. Have all the functions `loglog_plot`, `loglog_list_plot` available, and perhaps change `semilog[xy]*` to `semilog*` with an extra optional argument `log_axis='x'/'y'`. In case we follow this second rule, I would like this extra argument to be different from `axis` because it can be confused with `axes=True/False`.

I would really like this issue to be sorted out first.



---

archive/issue_comments_033602.json:
```json
{
    "body": "> For *consistency*, we should have just one convention. \nAgreed.\n> It is very confusing if the options of `plot` (except for probably `plotjoined` and `data`) are also valid options for `list_plot`, but then we introduce an inconsistency via log plots. So, I would be in favor of either\n\nHow would this introduce an inconsistency?  Is the suggestion on the table that the log option would only be for one of them?   I don't see why we can't have our cake and eat it too.\n* Log options in `show` or `save`\n* `loglog_plot(f,(x,a,b))` is an alias for `plot(f,(x,a,b),scale=foo)`\n\n> 1. Don't have any of the `loglog_*, semilog*` and handle scaling only through the `scale` and `base` parameters of `plot` and `list_plot` (and actually all other plots)\n\nIf Mma and friends have it, this is probably not a good idea.\n\n> 2. Have all the functions `loglog_plot`, `loglog_list_plot` available, and perhaps change `semilog[xy]*` to `semilog*` with an extra optional argument `log_axis='x'/'y'`. In case we follow this second rule, I would like this extra argument to be different from `axis` because it can be confused with `axes=True/False`.\nYes, that's a very good idea!\n> I would really like this issue to be sorted out first.\nAgreed.  Jason, should we raise this on sage-devel?",
    "created_at": "2012-05-25T13:59:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33602",
    "user": "https://github.com/kcrisman"
}
```

> For *consistency*, we should have just one convention. 
Agreed.
> It is very confusing if the options of `plot` (except for probably `plotjoined` and `data`) are also valid options for `list_plot`, but then we introduce an inconsistency via log plots. So, I would be in favor of either

How would this introduce an inconsistency?  Is the suggestion on the table that the log option would only be for one of them?   I don't see why we can't have our cake and eat it too.
* Log options in `show` or `save`
* `loglog_plot(f,(x,a,b))` is an alias for `plot(f,(x,a,b),scale=foo)`

> 1. Don't have any of the `loglog_*, semilog*` and handle scaling only through the `scale` and `base` parameters of `plot` and `list_plot` (and actually all other plots)

If Mma and friends have it, this is probably not a good idea.

> 2. Have all the functions `loglog_plot`, `loglog_list_plot` available, and perhaps change `semilog[xy]*` to `semilog*` with an extra optional argument `log_axis='x'/'y'`. In case we follow this second rule, I would like this extra argument to be different from `axis` because it can be confused with `axes=True/False`.
Yes, that's a very good idea!
> I would really like this issue to be sorted out first.
Agreed.  Jason, should we raise this on sage-devel?



---

archive/issue_comments_033603.json:
```json
{
    "body": "Sure, let's raise it on sage-devel.  Make sure the proposal provides specific options to vote for.",
    "created_at": "2012-05-25T17:21:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33603",
    "user": "https://github.com/jasongrout"
}
```

Sure, let's raise it on sage-devel.  Make sure the proposal provides specific options to vote for.



---

archive/issue_comments_033604.json:
```json
{
    "body": "Replying to [comment:34 jason]:\n> Sure, let's raise it on sage-devel.  Make sure the proposal provides specific options to vote for.\nOkay, hope I did it clearly enough.\n\n[http://groups.google.com/group/sage-devel/browse_thread/thread/af20ea19c09d14a0](http://groups.google.com/group/sage-devel/browse_thread/thread/af20ea19c09d14a0)",
    "created_at": "2012-05-26T05:05:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33604",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:34 jason]:
> Sure, let's raise it on sage-devel.  Make sure the proposal provides specific options to vote for.
Okay, hope I did it clearly enough.

[http://groups.google.com/group/sage-devel/browse_thread/thread/af20ea19c09d14a0](http://groups.google.com/group/sage-devel/browse_thread/thread/af20ea19c09d14a0)



---

archive/issue_comments_033605.json:
```json
{
    "body": "Thanks kcrisman. That poll is comprehensive enough.\n\nUpdated the [attachment:trac_4529-add_logscale_to_Graphics.2.patch Graphics patch]. This now has modifications only to matplotlib and sister functions, and leaves the `Graphics` class's attributes alone.\n\nThere was a problem with the ticker in that the labels were in scientific notation (ex. `1e10`) and not in the `base^exponent` form (ex. `10^10`). This is now fixed, except for the case when the user enters a custom tick formatter. This last case is up to the user to handle.\n\nThe interface to `plot` and `list_plot` remains unchanged. However, I will wait for the poll in sage-devel before deciding what extra plot commands to introduce.",
    "created_at": "2012-05-26T09:07:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33605",
    "user": "https://github.com/ppurka"
}
```

Thanks kcrisman. That poll is comprehensive enough.

Updated the [attachment:trac_4529-add_logscale_to_Graphics.2.patch Graphics patch]. This now has modifications only to matplotlib and sister functions, and leaves the `Graphics` class's attributes alone.

There was a problem with the ticker in that the labels were in scientific notation (ex. `1e10`) and not in the `base^exponent` form (ex. `10^10`). This is now fixed, except for the case when the user enters a custom tick formatter. This last case is up to the user to handle.

The interface to `plot` and `list_plot` remains unchanged. However, I will wait for the poll in sage-devel before deciding what extra plot commands to introduce.



---

archive/issue_comments_033606.json:
```json
{
    "body": "Updated to the correct patch. Apparently I uploaded the wrong patch several hours ago.",
    "created_at": "2012-05-26T12:08:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33606",
    "user": "https://github.com/ppurka"
}
```

Updated to the correct patch. Apparently I uploaded the wrong patch several hours ago.



---

archive/issue_comments_033607.json:
```json
{
    "body": "Some comments:\n* Shouldn't `base=2` raise an error when `scale='linear'` in your example? Maybe the \n\n```\n       if scale is None: \n            return ('linear', 'linear', 10, 10) \n```\n\n   could return 'linear', 'linear', None, None?\n* In `_matplotlib_tick_formatter`, should `base` and `scale` be next to each other in the function definition?  (This is a very minor critique, of course.)\n* Nice consolidation of the `ticklabels` business at the end of the patch.\n* Regardless of the outcome of the poll (on which you can vote), I think one should add a lot more examples in the documentation for `show` for the various options.  Lots of them.\n* What's going on with the `pr, i  = *, 0` thing removed?  I just don't know what it had been doing - seems to have been dead code, but I always get nervous when I have no idea what it *used'' to do...\n* kini says that the `[13:]` seems brittle if matplotlib's API changes; would it be possible to remove the specific string `\\\\mathdefault` instead?\n* I wonder about the not setting of the spines outward when the axes shouldn't cross.  Here is an example which serves the point:\n\n```\nsage: G = plot(exp(x), (x,5,10))\nsage: G.show(scale=('semilogy', 2))\n```\n\n   I don't even think this is a very atypical example to arise in practice.  It should be documented somehow.\n* It's fairly easy to have just one tick in a given direction, which usually raises an error in normal plots but isn't raising an error for yours.  I'm not sure if one would want to raise an error like \"Use a different base so that you get at least two ticks!\" or something.\n\nBut even with all of these comments, and waiting for the post-poll patch, **fantastic** job on this.  Someone had to come along to finally wrap this for us, it's been requested zillions of times, and this is very worth the effort, thank you so much.",
    "created_at": "2012-05-26T23:53:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33607",
    "user": "https://github.com/kcrisman"
}
```

Some comments:
* Shouldn't `base=2` raise an error when `scale='linear'` in your example? Maybe the 

```
       if scale is None: 
            return ('linear', 'linear', 10, 10) 
```

   could return 'linear', 'linear', None, None?
* In `_matplotlib_tick_formatter`, should `base` and `scale` be next to each other in the function definition?  (This is a very minor critique, of course.)
* Nice consolidation of the `ticklabels` business at the end of the patch.
* Regardless of the outcome of the poll (on which you can vote), I think one should add a lot more examples in the documentation for `show` for the various options.  Lots of them.
* What's going on with the `pr, i  = *, 0` thing removed?  I just don't know what it had been doing - seems to have been dead code, but I always get nervous when I have no idea what it *used'' to do...
* kini says that the `[13:]` seems brittle if matplotlib's API changes; would it be possible to remove the specific string `\\mathdefault` instead?
* I wonder about the not setting of the spines outward when the axes shouldn't cross.  Here is an example which serves the point:

```
sage: G = plot(exp(x), (x,5,10))
sage: G.show(scale=('semilogy', 2))
```

   I don't even think this is a very atypical example to arise in practice.  It should be documented somehow.
* It's fairly easy to have just one tick in a given direction, which usually raises an error in normal plots but isn't raising an error for yours.  I'm not sure if one would want to raise an error like "Use a different base so that you get at least two ticks!" or something.

But even with all of these comments, and waiting for the post-poll patch, **fantastic** job on this.  Someone had to come along to finally wrap this for us, it's been requested zillions of times, and this is very worth the effort, thank you so much.



---

archive/issue_comments_033608.json:
```json
{
    "body": "Replying to [comment:39 kcrisman]:\n> Some comments:\n>  * Shouldn't `base=2` raise an error when `scale='linear'` in your example? Maybe the \n> {{{\n>        if scale is None: \n>             return ('linear', 'linear', 10, 10) \n> }}}\n>    could return 'linear', 'linear', None, None?\n\nI had thought about it. My decision was to silently ignore this error because it is not fatal in any way and we handle it properly (i.e. we ignore it and do the right thing).\n\n**Edit:** This seems to be the same behavior as in matplotlib.\n\n>  * In `_matplotlib_tick_formatter`, should `base` and `scale` be next to each other in the function definition?  (This is a very minor critique, of course.)\n\nWell, except for `subplot`, the rest of the arguments are alphabetically arranged. :) Personally, I find it quite hard to find out where a particular function or argument is present in a typical Sage code. There is no particular manner in which the functions are arranged. Especially in several thousand line files like graphics.py it becomes hard to scroll around and edit code.\n\n>  * Regardless of the outcome of the poll (on which you can vote), I think one should add a lot more examples in the documentation for `show` for the various options.  Lots of them.\n\nI will add some more.\n\n>  * What's going on with the `pr, i  = *, 0` thing removed?  I just don't know what it had been doing - seems to have been dead code, but I always get nervous when I have no idea what it *used'' to do...\n\nYes. I have no idea what it was for. It is dead code, so I removed it.\n\n>  * kini says that the `[13:]` seems brittle if matplotlib's API changes; would it be possible to remove the specific string `\\\\mathdefault` instead?\n\nTo remove it from matplotlib, we need to set `rcParams['text.usetex']=True`. But this makes matplotlib try to compile latex on its own and use dvipng to convert from dvi to png, etc. Moreover, this parameter seems to be persistent and remains throughout the current session. So, simply editing the string seemed a more viable option to me.\n\nIf the API changes (which seems unlikely to me), then the fix will be very easy too.\n\n>  * I wonder about the not setting of the spines outward when the axes shouldn't cross.  Here is an example which serves the point:\n> {{{\n> sage: G = plot(exp(x), (x,5,10))\n> sage: G.show(scale=('semilogy', 2))\n> }}}\n>    I don't even think this is a very atypical example to arise in practice.  It should be documented somehow.\n\nI will have to see how to handle this. Messing around with the spines was one of the primary reasons why setting scale wasn't working - the \"converting masked to int\" error.\n\n>  * It's fairly easy to have just one tick in a given direction, which usually raises an error in normal plots but isn't raising an error for yours.  I'm not sure if one would want to raise an error like \"Use a different base so that you get at least two ticks!\" or something.\n\nI think it is up to the user to either change their range, or their base, or provide custom ticks.\n\n> But even with all of these comments, and waiting for the post-poll patch, **fantastic** job on this.  Someone had to come along to finally wrap this for us, it's been requested zillions of times, and this is very worth the effort, thank you so much.\n\nThanks. I needed it for my own research! :)",
    "created_at": "2012-05-27T03:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33608",
    "user": "https://github.com/ppurka"
}
```

Replying to [comment:39 kcrisman]:
> Some comments:
>  * Shouldn't `base=2` raise an error when `scale='linear'` in your example? Maybe the 
> {{{
>        if scale is None: 
>             return ('linear', 'linear', 10, 10) 
> }}}
>    could return 'linear', 'linear', None, None?

I had thought about it. My decision was to silently ignore this error because it is not fatal in any way and we handle it properly (i.e. we ignore it and do the right thing).

**Edit:** This seems to be the same behavior as in matplotlib.

>  * In `_matplotlib_tick_formatter`, should `base` and `scale` be next to each other in the function definition?  (This is a very minor critique, of course.)

Well, except for `subplot`, the rest of the arguments are alphabetically arranged. :) Personally, I find it quite hard to find out where a particular function or argument is present in a typical Sage code. There is no particular manner in which the functions are arranged. Especially in several thousand line files like graphics.py it becomes hard to scroll around and edit code.

>  * Regardless of the outcome of the poll (on which you can vote), I think one should add a lot more examples in the documentation for `show` for the various options.  Lots of them.

I will add some more.

>  * What's going on with the `pr, i  = *, 0` thing removed?  I just don't know what it had been doing - seems to have been dead code, but I always get nervous when I have no idea what it *used'' to do...

Yes. I have no idea what it was for. It is dead code, so I removed it.

>  * kini says that the `[13:]` seems brittle if matplotlib's API changes; would it be possible to remove the specific string `\\mathdefault` instead?

To remove it from matplotlib, we need to set `rcParams['text.usetex']=True`. But this makes matplotlib try to compile latex on its own and use dvipng to convert from dvi to png, etc. Moreover, this parameter seems to be persistent and remains throughout the current session. So, simply editing the string seemed a more viable option to me.

If the API changes (which seems unlikely to me), then the fix will be very easy too.

>  * I wonder about the not setting of the spines outward when the axes shouldn't cross.  Here is an example which serves the point:
> {{{
> sage: G = plot(exp(x), (x,5,10))
> sage: G.show(scale=('semilogy', 2))
> }}}
>    I don't even think this is a very atypical example to arise in practice.  It should be documented somehow.

I will have to see how to handle this. Messing around with the spines was one of the primary reasons why setting scale wasn't working - the "converting masked to int" error.

>  * It's fairly easy to have just one tick in a given direction, which usually raises an error in normal plots but isn't raising an error for yours.  I'm not sure if one would want to raise an error like "Use a different base so that you get at least two ticks!" or something.

I think it is up to the user to either change their range, or their base, or provide custom ticks.

> But even with all of these comments, and waiting for the post-poll patch, **fantastic** job on this.  Someone had to come along to finally wrap this for us, it's been requested zillions of times, and this is very worth the effort, thank you so much.

Thanks. I needed it for my own research! :)



---

archive/issue_comments_033609.json:
```json
{
    "body": "Oh, I didn't mean to prevent `\\\\mathdefault` from coming into the string at all. I meant to just specifically remove the substring `\\\\mathdefault` (say with `.replace(\"\\\\mathdefault\",\"\")` or something).",
    "created_at": "2012-05-27T03:45:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33609",
    "user": "https://github.com/kini"
}
```

Oh, I didn't mean to prevent `\\mathdefault` from coming into the string at all. I meant to just specifically remove the substring `\\mathdefault` (say with `.replace("\\mathdefault","")` or something).



---

archive/issue_comments_033610.json:
```json
{
    "body": "> I had thought about it. My decision was to silently ignore this error because it is not fatal in any way and we handle it properly (i.e. we ignore it and do the right thing).\n> \n> **Edit:** This seems to be the same behavior as in matplotlib.\n\nOkay, just asking.  Maybe this should be documented (that is, explained that it's ok that no error is raised).\n\n> Well, except for `subplot`, the rest of the arguments are alphabetically arranged. :) Personally, I find it quite hard to find out where a particular function or argument is present in a typical Sage code. There is no particular manner in which the functions are arranged. Especially in several thousand line files like graphics.py it becomes hard to scroll around and edit code.\n\nOh yeah, it's REALLY hard to find stuff - you just have to get used to it.  Ok.\n\n> I will add some more.\n\nGreat.\n\n> Yes. I have no idea what it was for. It is dead code, so I removed it.\n\nExcellent.\n\n> If the API changes (which seems unlikely to me), then the fix will be very easy too.\n\nI think kini explained this sufficiently in comment:41.  I don't care which way it's done.\n\n> >  * I wonder about the not setting of the spines outward when the axes shouldn't cross.  Here is an example which serves the point:\n> I will have to see how to handle this. Messing around with the spines was one of the primary reasons why setting scale wasn't working - the \"converting masked to int\" error.\n\nI see.  It would be good to have consistency, since we went to some trouble to make them not cross any more.\n\n> I think it is up to the user to either change their range, or their base, or provide custom ticks.\n\nAh!  You would think so.  But we actually raise an error in the current code in precisely this situation.  Presumably the code would be easy to just reuse?\n\n> > But even with all of these comments, and waiting for the post-poll patch, **fantastic** job on this.  Someone had to come along to finally wrap this for us, it's been requested zillions of times, and this is very worth the effort, thank you so much.\n> \n> Thanks. I needed it for my own research! :)\n\nAlways good to have a good motivator!  I've found that using things in class or for some random voting theory thing has ... enhanced my motivation to work on a topic.\n\nLooking forward to seeing the global functions.",
    "created_at": "2012-05-27T04:09:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33610",
    "user": "https://github.com/kcrisman"
}
```

> I had thought about it. My decision was to silently ignore this error because it is not fatal in any way and we handle it properly (i.e. we ignore it and do the right thing).
> 
> **Edit:** This seems to be the same behavior as in matplotlib.

Okay, just asking.  Maybe this should be documented (that is, explained that it's ok that no error is raised).

> Well, except for `subplot`, the rest of the arguments are alphabetically arranged. :) Personally, I find it quite hard to find out where a particular function or argument is present in a typical Sage code. There is no particular manner in which the functions are arranged. Especially in several thousand line files like graphics.py it becomes hard to scroll around and edit code.

Oh yeah, it's REALLY hard to find stuff - you just have to get used to it.  Ok.

> I will add some more.

Great.

> Yes. I have no idea what it was for. It is dead code, so I removed it.

Excellent.

> If the API changes (which seems unlikely to me), then the fix will be very easy too.

I think kini explained this sufficiently in comment:41.  I don't care which way it's done.

> >  * I wonder about the not setting of the spines outward when the axes shouldn't cross.  Here is an example which serves the point:
> I will have to see how to handle this. Messing around with the spines was one of the primary reasons why setting scale wasn't working - the "converting masked to int" error.

I see.  It would be good to have consistency, since we went to some trouble to make them not cross any more.

> I think it is up to the user to either change their range, or their base, or provide custom ticks.

Ah!  You would think so.  But we actually raise an error in the current code in precisely this situation.  Presumably the code would be easy to just reuse?

> > But even with all of these comments, and waiting for the post-poll patch, **fantastic** job on this.  Someone had to come along to finally wrap this for us, it's been requested zillions of times, and this is very worth the effort, thank you so much.
> 
> Thanks. I needed it for my own research! :)

Always good to have a good motivator!  I've found that using things in class or for some random voting theory thing has ... enhanced my motivation to work on a topic.

Looking forward to seeing the global functions.



---

archive/issue_comments_033611.json:
```json
{
    "body": "Replying to [comment:41 kini]:\n> Oh, I didn't mean to prevent `\\\\mathdefault` from coming into the string at all. I meant to just specifically remove the substring `\\\\mathdefault` (say with `.replace(\"\\\\mathdefault\",\"\")` or something).\n\nindeed, the replace seems much better. Thanks.",
    "created_at": "2012-05-27T04:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33611",
    "user": "https://github.com/ppurka"
}
```

Replying to [comment:41 kini]:
> Oh, I didn't mean to prevent `\\mathdefault` from coming into the string at all. I meant to just specifically remove the substring `\\mathdefault` (say with `.replace("\\mathdefault","")` or something).

indeed, the replace seems much better. Thanks.



---

archive/issue_comments_033612.json:
```json
{
    "body": "Attachment [trac_4529-check_for_single_tick.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-check_for_single_tick.patch) by @ppurka created at 2012-05-27 09:12:18\n\napply to devel/sage",
    "created_at": "2012-05-27T09:12:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33612",
    "user": "https://github.com/ppurka"
}
```

Attachment [trac_4529-check_for_single_tick.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-check_for_single_tick.patch) by @ppurka created at 2012-05-27 09:12:18

apply to devel/sage



---

archive/issue_comments_033613.json:
```json
{
    "body": "The following are the changes in the latest patches:\n1. labeling of minor ticks was flaky; it is fixed now.\n2. added several examples to `show()`\n3. fixed a problem in axes position of the matplotlib() function when custom xmax, xmin, etc were passed. Try this plot (without these patches) and then try with these patches :)\n\n```\nplot(x).show(xmin=1, xmax=-1)\n```\n\n4. there is an [attachment:trac_4529-check_for_single_tick.patch optional patch] where we check for a single tick. this is tricky and I don't know a good and complete solution. Moreover, it makes most of the functions like 'arc, disk, etc' stop \"just working\" with log scale. It will be good if you have a better idea how to check for ticks which don't affect these functions too. We can't use xmin, xmax, etc to determine ticks because some of them might well be negative and matplotlib will neglect these values.",
    "created_at": "2012-05-27T09:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33613",
    "user": "https://github.com/ppurka"
}
```

The following are the changes in the latest patches:
1. labeling of minor ticks was flaky; it is fixed now.
2. added several examples to `show()`
3. fixed a problem in axes position of the matplotlib() function when custom xmax, xmin, etc were passed. Try this plot (without these patches) and then try with these patches :)

```
plot(x).show(xmin=1, xmax=-1)
```

4. there is an [attachment:trac_4529-check_for_single_tick.patch optional patch] where we check for a single tick. this is tricky and I don't know a good and complete solution. Moreover, it makes most of the functions like 'arc, disk, etc' stop "just working" with log scale. It will be good if you have a better idea how to check for ticks which don't affect these functions too. We can't use xmin, xmax, etc to determine ticks because some of them might well be negative and matplotlib will neglect these values.



---

archive/issue_comments_033614.json:
```json
{
    "body": "Attachment [trac_4529-add_logscale_to_Graphics.2.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-add_logscale_to_Graphics.2.patch) by @ppurka created at 2012-05-27 09:39:26\n\napply to devel/sage",
    "created_at": "2012-05-27T09:39:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33614",
    "user": "https://github.com/ppurka"
}
```

Attachment [trac_4529-add_logscale_to_Graphics.2.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-add_logscale_to_Graphics.2.patch) by @ppurka created at 2012-05-27 09:39:26

apply to devel/sage



---

archive/issue_comments_033615.json:
```json
{
    "body": "Sorry for the delay - I only scheduled a couple hours of work this evening.  Tomorrow I will have more time.\n\nHey, I just had an idea.  Maybe this ticket should be *only* about the ticket description, and then another ticket for adding the \"shortcut\" commands like `plot_loglog` or whatever.  In which case the current patches might be enough!  (After much testing, of course.)  What do you think?\n\nMore comments:\n* Wow, great catch on all those things like the minor ticks etc.  I haven't really tested many of these plots yet, focusing on the code right now, so I'm glad you found a lot of those things.\n* We'll eventually want to add some examples (or replace some of these) with the `plot(...,scale='loglog')` format ones.  And definitely to add some to the file `plot.py`, since that is where a lot of people will look first for how to get this.  **But** that can wait until the end, I'll be happy to do that in a reviewer patch.\n* Catching this thing about the flipped `xmin/xmax` and friends is just a bonus - again, great catch and solution.\n* As to the optional patch, I will think about this some more tomorrow.  I do note that things still \"work\".  For the example you removed `G`, the example you removed did in fact work, for instance.  \n\n```\nsage: G.show(scale=('loglog', 5)) # plots\nsage: G.show(scale=('loglog', 4)) # plots\nsage: G.show(scale=('loglog', 6)) # error\n```\n\n  because it really depends on the *minor* ticks as well.  I'm not sure whether having minor ticks should count as \"having two ticks\", especially in the relatively obscure-looking log plot situation.  I'm not even sure why\n\n```\nsage: G.show(scale=('loglog', 2)) \n```\n\n  works, since there is only one tick on the left!\n* So all that said, I really am not sure why this is a problem.  If someone is dumb enough to plot a CIRCLE with log scales, then they had better know how to pick the right scale so that this works.    But the same would be true for plotting data, as you point out.\n* Along those lines, your example (changed)\n\n```\nsage: p = list_plot(range(1, 10), plotjoined=True)\nsage: p.show(scale='loglog',base=2)\n```\n\n  doesn't show any minor ticks.  Is that just how `LogLocator` works, or is there something wrong?\n\nObviously at this point we are getting close to nitpicking.  I'll try more tomorrow.",
    "created_at": "2012-05-28T05:40:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33615",
    "user": "https://github.com/kcrisman"
}
```

Sorry for the delay - I only scheduled a couple hours of work this evening.  Tomorrow I will have more time.

Hey, I just had an idea.  Maybe this ticket should be *only* about the ticket description, and then another ticket for adding the "shortcut" commands like `plot_loglog` or whatever.  In which case the current patches might be enough!  (After much testing, of course.)  What do you think?

More comments:
* Wow, great catch on all those things like the minor ticks etc.  I haven't really tested many of these plots yet, focusing on the code right now, so I'm glad you found a lot of those things.
* We'll eventually want to add some examples (or replace some of these) with the `plot(...,scale='loglog')` format ones.  And definitely to add some to the file `plot.py`, since that is where a lot of people will look first for how to get this.  **But** that can wait until the end, I'll be happy to do that in a reviewer patch.
* Catching this thing about the flipped `xmin/xmax` and friends is just a bonus - again, great catch and solution.
* As to the optional patch, I will think about this some more tomorrow.  I do note that things still "work".  For the example you removed `G`, the example you removed did in fact work, for instance.  

```
sage: G.show(scale=('loglog', 5)) # plots
sage: G.show(scale=('loglog', 4)) # plots
sage: G.show(scale=('loglog', 6)) # error
```

  because it really depends on the *minor* ticks as well.  I'm not sure whether having minor ticks should count as "having two ticks", especially in the relatively obscure-looking log plot situation.  I'm not even sure why

```
sage: G.show(scale=('loglog', 2)) 
```

  works, since there is only one tick on the left!
* So all that said, I really am not sure why this is a problem.  If someone is dumb enough to plot a CIRCLE with log scales, then they had better know how to pick the right scale so that this works.    But the same would be true for plotting data, as you point out.
* Along those lines, your example (changed)

```
sage: p = list_plot(range(1, 10), plotjoined=True)
sage: p.show(scale='loglog',base=2)
```

  doesn't show any minor ticks.  Is that just how `LogLocator` works, or is there something wrong?

Obviously at this point we are getting close to nitpicking.  I'll try more tomorrow.



---

archive/issue_comments_033616.json:
```json
{
    "body": "Replying to [comment:45 kcrisman]:\n> Sorry for the delay - I only scheduled a couple hours of work this evening.  Tomorrow I will have more time.\n\nNo problems. It is better to have a good implementation than to hurry through a bad one.\n\n> Hey, I just had an idea.  Maybe this ticket should be *only* about the ticket description, and then another ticket for adding the \"shortcut\" commands like `plot_loglog` or whatever.  In which case the current patches might be enough!  (After much testing, of course.)  What do you think?\n\nActually, there is zero change to be done to the code in `plot` or `list_plot`, except to add some examples. The only change that the additional  patch will do is make very thin (one-liners) wrappers which defines the `plot_*` and `list_plot_*` wrappers and pass the correct scale option to `plot` and `list_plot`. The current consensus from the poll seems to favor this syntax. In view of this, the patch [attachment:trac_4529-add_docs_eg_to_some_user_facing_functions.patch] requires only a renaming of the functions, and some extra examples.\n\n> * We'll eventually want to add some examples (or replace some of these) with the `plot(...,scale='loglog')` format ones.  And definitely to add some to the file `plot.py`, since that is where a lot of people will look first for how to get this.  **But** that can wait until the end, I'll be happy to do that in a reviewer patch.\n\nWe can add exactly similar examples to `plot()` and `list_plot()`. Currently, since the function is `Graphics.show()`, I decided to write it as `show(scale=...)` instead of `plot(scale=...)` since the former is more pertinent.\n\n> * Catching this thing about the flipped `xmin/xmax` and friends is just a bonus - again, great catch and solution.\n> * As to the optional patch, I will think about this some more tomorrow.  I do note that things still \"work\".  For the example you removed `G`, the example you removed did in fact work, for instance.  \n\nYes I am aware that the examples I provided work. But most of the examples in the docs of those functions (arc, disk, contour_plot, etc) *do not* work out of the box, and we get the \"too few ticks\" error.\n\n> I'm not sure whether having minor ticks should count as \"having two ticks\", especially in the relatively obscure-looking log plot situation.  I'm not even sure why\n> {{{\n> sage: G.show(scale=('loglog', 2)) \n> }}}\n>   works, since there is only one tick on the left!\n\nYes. That's why I said that the tick checking function is not robust and I also don't know how to make it robust.\n\n> * Along those lines, your example (changed)\n> {{{\n> sage: p = list_plot(range(1, 10), plotjoined=True)\n> sage: p.show(scale='loglog',base=2)\n> }}}\n>   doesn't show any minor ticks.  Is that just how `LogLocator` works, or is there something wrong?\n\nThe minor ticks are generated by passing in multiples of 1/base to the subs parameter of LogLocator. So, for base 10, you will have ticks at say, `0.1*10^-1, 0.2*10^-1, ..., 0.9*10^-1, 10^-1`. This is a typical way how log plots are drawn in all programs (`pyplot.loglog()`, matlab, mathematica, etc). For `base=2` you can have only one tick `1/2*2^i` but this is a major tick at `2^(i-1)`. So, you will always see only one major tick and no minor ticks.\n\n> Obviously at this point we are getting close to nitpicking.  I'll try more tomorrow.\n\nThanks a lot for the feedback. I am sure I have missed something, so I look forward to it. :)",
    "created_at": "2012-05-28T06:04:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33616",
    "user": "https://github.com/ppurka"
}
```

Replying to [comment:45 kcrisman]:
> Sorry for the delay - I only scheduled a couple hours of work this evening.  Tomorrow I will have more time.

No problems. It is better to have a good implementation than to hurry through a bad one.

> Hey, I just had an idea.  Maybe this ticket should be *only* about the ticket description, and then another ticket for adding the "shortcut" commands like `plot_loglog` or whatever.  In which case the current patches might be enough!  (After much testing, of course.)  What do you think?

Actually, there is zero change to be done to the code in `plot` or `list_plot`, except to add some examples. The only change that the additional  patch will do is make very thin (one-liners) wrappers which defines the `plot_*` and `list_plot_*` wrappers and pass the correct scale option to `plot` and `list_plot`. The current consensus from the poll seems to favor this syntax. In view of this, the patch [attachment:trac_4529-add_docs_eg_to_some_user_facing_functions.patch] requires only a renaming of the functions, and some extra examples.

> * We'll eventually want to add some examples (or replace some of these) with the `plot(...,scale='loglog')` format ones.  And definitely to add some to the file `plot.py`, since that is where a lot of people will look first for how to get this.  **But** that can wait until the end, I'll be happy to do that in a reviewer patch.

We can add exactly similar examples to `plot()` and `list_plot()`. Currently, since the function is `Graphics.show()`, I decided to write it as `show(scale=...)` instead of `plot(scale=...)` since the former is more pertinent.

> * Catching this thing about the flipped `xmin/xmax` and friends is just a bonus - again, great catch and solution.
> * As to the optional patch, I will think about this some more tomorrow.  I do note that things still "work".  For the example you removed `G`, the example you removed did in fact work, for instance.  

Yes I am aware that the examples I provided work. But most of the examples in the docs of those functions (arc, disk, contour_plot, etc) *do not* work out of the box, and we get the "too few ticks" error.

> I'm not sure whether having minor ticks should count as "having two ticks", especially in the relatively obscure-looking log plot situation.  I'm not even sure why
> {{{
> sage: G.show(scale=('loglog', 2)) 
> }}}
>   works, since there is only one tick on the left!

Yes. That's why I said that the tick checking function is not robust and I also don't know how to make it robust.

> * Along those lines, your example (changed)
> {{{
> sage: p = list_plot(range(1, 10), plotjoined=True)
> sage: p.show(scale='loglog',base=2)
> }}}
>   doesn't show any minor ticks.  Is that just how `LogLocator` works, or is there something wrong?

The minor ticks are generated by passing in multiples of 1/base to the subs parameter of LogLocator. So, for base 10, you will have ticks at say, `0.1*10^-1, 0.2*10^-1, ..., 0.9*10^-1, 10^-1`. This is a typical way how log plots are drawn in all programs (`pyplot.loglog()`, matlab, mathematica, etc). For `base=2` you can have only one tick `1/2*2^i` but this is a major tick at `2^(i-1)`. So, you will always see only one major tick and no minor ticks.

> Obviously at this point we are getting close to nitpicking.  I'll try more tomorrow.

Thanks a lot for the feedback. I am sure I have missed something, so I look forward to it. :)



---

archive/issue_comments_033617.json:
```json
{
    "body": "> Actually, there is zero change to be done to the code in `plot` or `list_plot`, except to add some examples. The only change that the additional  patch will do is make very thin (one-liners) wrappers which defines the `plot_*` and `list_plot_*` wrappers and pass the correct scale option to `plot` and `list_plot`. The current consensus from the poll seems to favor this syntax. In view of this, the patch [attachment:trac_4529-add_docs_eg_to_some_user_facing_functions.patch] requires only a renaming of the functions, and some extra examples.\n\nOh, I didn't realize that that patch actually already implemented that - I hadn't had time to look at the patches until you had already said which patches to apply!  Yes, I should be able to rebase/rename that well for our purposes, just adding a few more examples which occur fairly frequently.\n\n> We can add exactly similar examples to `plot()` and `list_plot()`. Currently, since the function is `Graphics.show()`, I decided to write it as `show(scale=...)` instead of `plot(scale=...)` since the former is more pertinent.\n\nOf course.\n\n> > * As to the optional patch, I will think about this some more tomorrow.  I do note that things still \"work\".  For the example you removed `G`, the example you removed did in fact work, for instance.  \n> \n> Yes I am aware that the examples I provided work. But most of the examples in the docs of those functions (arc, disk, contour_plot, etc) *do not* work out of the box, and we get the \"too few ticks\" error.\n\nBut they 'work', just not with the log scale, right?\n\n> > I'm not sure whether having minor ticks should count as \"having two ticks\", especially in the relatively obscure-looking log plot situation.  I'm not even sure why\n> > {{{\n> > sage: G.show(scale=('loglog', 2)) \n> > }}}\n> >   works, since there is only one tick on the left!\n> \n> Yes. That's why I said that the tick checking function is not robust and I also don't know how to make it robust.\n\nHaha.  Well, I spent about a half-hour looking in depth at the code for `matplotlib.ticker.LogLocator` and have decided it is nearly impossible.  There will very often, especially for `base=2` and friends, be ticks in the locator which are outside of the viewing range.\n\nSo there are ways to get some of this information... yuck.  I may have something for this later today.  I've been looking at it for over an hour and, at least for plots with only positive data, I think I have something.  For ones with negative data it would be much more ugly and maybe not worth it.\n\nBy the way, I get\n\n```\nsage: sage: disk((0,0), 1, (0, 3*pi/2)).show(scale='semilogx',base=2)\n/Users/.../sage-5.1.beta0/local/lib/python2.7/site-packages/matplotlib/axes.py:1114: UserWarning: aspect is not supported for Axes with xscale=log, yscale=linear\n  % (xscale, yscale))\n```\n\nwhen I try something that has an aspect ratio defined (disk, etc.)\n\n> The minor ticks are generated by passing in multiples of 1/base to the subs parameter of LogLocator. So, for base 10, you will have ticks at say, `0.1*10^-1, 0.2*10^-1, ..., 0.9*10^-1, 10^-1`. This is a typical way how log plots are drawn in all programs (`pyplot.loglog()`, matlab, mathematica, etc). For `base=2` you can have only one tick `1/2*2^i` but this is a major tick at `2^(i-1)`. So, you will always see only one major tick and no minor ticks.\nI understood that, but didn't think through the implications for `base=2`.   By the way, maybe changing\n\n```\nsrange(base_inv, 1+base_inv, base_inv)\n```\n\nto \n\n```\nsrange(2*base_inv, 1, base_inv)\n```\n\nwould be useful, so that minor and major ticks don't overlap... probably doesn't matter, but could be ok.",
    "created_at": "2012-05-28T19:03:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33617",
    "user": "https://github.com/kcrisman"
}
```

> Actually, there is zero change to be done to the code in `plot` or `list_plot`, except to add some examples. The only change that the additional  patch will do is make very thin (one-liners) wrappers which defines the `plot_*` and `list_plot_*` wrappers and pass the correct scale option to `plot` and `list_plot`. The current consensus from the poll seems to favor this syntax. In view of this, the patch [attachment:trac_4529-add_docs_eg_to_some_user_facing_functions.patch] requires only a renaming of the functions, and some extra examples.

Oh, I didn't realize that that patch actually already implemented that - I hadn't had time to look at the patches until you had already said which patches to apply!  Yes, I should be able to rebase/rename that well for our purposes, just adding a few more examples which occur fairly frequently.

> We can add exactly similar examples to `plot()` and `list_plot()`. Currently, since the function is `Graphics.show()`, I decided to write it as `show(scale=...)` instead of `plot(scale=...)` since the former is more pertinent.

Of course.

> > * As to the optional patch, I will think about this some more tomorrow.  I do note that things still "work".  For the example you removed `G`, the example you removed did in fact work, for instance.  
> 
> Yes I am aware that the examples I provided work. But most of the examples in the docs of those functions (arc, disk, contour_plot, etc) *do not* work out of the box, and we get the "too few ticks" error.

But they 'work', just not with the log scale, right?

> > I'm not sure whether having minor ticks should count as "having two ticks", especially in the relatively obscure-looking log plot situation.  I'm not even sure why
> > {{{
> > sage: G.show(scale=('loglog', 2)) 
> > }}}
> >   works, since there is only one tick on the left!
> 
> Yes. That's why I said that the tick checking function is not robust and I also don't know how to make it robust.

Haha.  Well, I spent about a half-hour looking in depth at the code for `matplotlib.ticker.LogLocator` and have decided it is nearly impossible.  There will very often, especially for `base=2` and friends, be ticks in the locator which are outside of the viewing range.

So there are ways to get some of this information... yuck.  I may have something for this later today.  I've been looking at it for over an hour and, at least for plots with only positive data, I think I have something.  For ones with negative data it would be much more ugly and maybe not worth it.

By the way, I get

```
sage: sage: disk((0,0), 1, (0, 3*pi/2)).show(scale='semilogx',base=2)
/Users/.../sage-5.1.beta0/local/lib/python2.7/site-packages/matplotlib/axes.py:1114: UserWarning: aspect is not supported for Axes with xscale=log, yscale=linear
  % (xscale, yscale))
```

when I try something that has an aspect ratio defined (disk, etc.)

> The minor ticks are generated by passing in multiples of 1/base to the subs parameter of LogLocator. So, for base 10, you will have ticks at say, `0.1*10^-1, 0.2*10^-1, ..., 0.9*10^-1, 10^-1`. This is a typical way how log plots are drawn in all programs (`pyplot.loglog()`, matlab, mathematica, etc). For `base=2` you can have only one tick `1/2*2^i` but this is a major tick at `2^(i-1)`. So, you will always see only one major tick and no minor ticks.
I understood that, but didn't think through the implications for `base=2`.   By the way, maybe changing

```
srange(base_inv, 1+base_inv, base_inv)
```

to 

```
srange(2*base_inv, 1, base_inv)
```

would be useful, so that minor and major ticks don't overlap... probably doesn't matter, but could be ok.



---

archive/issue_comments_033618.json:
```json
{
    "body": "So I've come up with a solution.  I'll probably post stuff in a little while.  Here's a typical example.\n\n```\nsage: P = plot(x^2,(x,1,8),scale='loglog'); P\nValueError: Either expand the range of the independent variable to allow two different integer powers of your `base`, or change your `base` to a smaller number.\nsage: P.show(xmax=10)\n```\n\n\nSome more food for thought.\n* Your LaTeX hack doesn't work in all cases, apparently.\n\n```\nsage: P = plot(x^2,(x,1,8),scale='loglog', base=1.5); P\n```\n\n  This is because matplotlib has\n\n```\n        else:\n            if usetex:\n                s = r'$%s%d^{%d}$'% (sign_string, b, nearest_long(fx))\n            else:\n                s = r'$\\mathdefault{%s%d^{%d}}$'% (sign_string, b,\n                                                   nearest_long(fx))\n```\n\n  which uses decimal formatting, but of course that only makes sense for integer bases.   I feel like this is a bug in mpl; what do you think?  Anyway, I am hesitant to patch our matplotlib just for this use case, though it should be a new ticket, I think.  The same thing happens with `base=3/2`, unsurprisingly.\n* This also bites your example with `base=float(e)` - did you look at the picture?  Plain old `base=e` should be possible, but hacking around the fact that matplotlib won't accept this maybe makes it not worth it, and in any case I don't know that \"real-life\" people often use that for semilog plots.  Just pointing it out.\n* Here is a fun horrible example that you probably were thinking of with adding plots - maybe we should find a check for this.\n\n```\nsage: G =  plot_vector_field((e^x,e^(x+y)),(x,0.1,10),(y,0.1,10),scale=('loglog', 2))\nsage: H = plot(x^2,(x,0,10),scale='linear')\nsage: G+H\n```\n\n  At least originally you thought this should raise an error.",
    "created_at": "2012-05-28T21:20:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33618",
    "user": "https://github.com/kcrisman"
}
```

So I've come up with a solution.  I'll probably post stuff in a little while.  Here's a typical example.

```
sage: P = plot(x^2,(x,1,8),scale='loglog'); P
ValueError: Either expand the range of the independent variable to allow two different integer powers of your `base`, or change your `base` to a smaller number.
sage: P.show(xmax=10)
```


Some more food for thought.
* Your LaTeX hack doesn't work in all cases, apparently.

```
sage: P = plot(x^2,(x,1,8),scale='loglog', base=1.5); P
```

  This is because matplotlib has

```
        else:
            if usetex:
                s = r'$%s%d^{%d}$'% (sign_string, b, nearest_long(fx))
            else:
                s = r'$\mathdefault{%s%d^{%d}}$'% (sign_string, b,
                                                   nearest_long(fx))
```

  which uses decimal formatting, but of course that only makes sense for integer bases.   I feel like this is a bug in mpl; what do you think?  Anyway, I am hesitant to patch our matplotlib just for this use case, though it should be a new ticket, I think.  The same thing happens with `base=3/2`, unsurprisingly.
* This also bites your example with `base=float(e)` - did you look at the picture?  Plain old `base=e` should be possible, but hacking around the fact that matplotlib won't accept this maybe makes it not worth it, and in any case I don't know that "real-life" people often use that for semilog plots.  Just pointing it out.
* Here is a fun horrible example that you probably were thinking of with adding plots - maybe we should find a check for this.

```
sage: G =  plot_vector_field((e^x,e^(x+y)),(x,0.1,10),(y,0.1,10),scale=('loglog', 2))
sage: H = plot(x^2,(x,0,10),scale='linear')
sage: G+H
```

  At least originally you thought this should raise an error.



---

archive/issue_comments_033619.json:
```json
{
    "body": "Almost done with my changes!  Here are things that definitely have to be decided or fixed.\n* What to do with noninteger bases.  Tell people not to use them?  Throw an exception?  Hack mpl?  Give copious examples of them looking bad?\n* Decide what to do with adding plots.\n\nOther points.\n* I can't get `list_plot` to work with `scale='loglog'` or `'semilogx'` when passing it a list.  From your examples -\n\n```\n        sage: yl = [2**k for k in range(10)]  \n        sage: list_plot(yl, scale='semilogy')       # fine\n        sage: list_plot(yl, scale='loglog')         # horiz. axis weird, no points\n        sage: list_plot_loglog(yl, base=2) # same weird\n```\n\n  I assume this is because there is automatically a change to the list of tuples zipped with `range(n)`, so that there is always a zero involved in the horizontal axis.   Here is the real problem.\n\n```\npoint([(0,1),(1,2),(2,3),(3,4),(4,5)],scale='semilogx',base=2) # doesn't work\n```\n\n  What do you think the \"correct\" behavior is here?\n\nI fixed a bunch of minor doc issues.  I also added a lot of \n\n```\n\n::\n\n```\n\nbetween doctests which were meant to be viewed, because otherwise one will not be able to evaluate these plots in the live documentation (this is standard).",
    "created_at": "2012-05-28T23:28:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33619",
    "user": "https://github.com/kcrisman"
}
```

Almost done with my changes!  Here are things that definitely have to be decided or fixed.
* What to do with noninteger bases.  Tell people not to use them?  Throw an exception?  Hack mpl?  Give copious examples of them looking bad?
* Decide what to do with adding plots.

Other points.
* I can't get `list_plot` to work with `scale='loglog'` or `'semilogx'` when passing it a list.  From your examples -

```
        sage: yl = [2**k for k in range(10)]  
        sage: list_plot(yl, scale='semilogy')       # fine
        sage: list_plot(yl, scale='loglog')         # horiz. axis weird, no points
        sage: list_plot_loglog(yl, base=2) # same weird
```

  I assume this is because there is automatically a change to the list of tuples zipped with `range(n)`, so that there is always a zero involved in the horizontal axis.   Here is the real problem.

```
point([(0,1),(1,2),(2,3),(3,4),(4,5)],scale='semilogx',base=2) # doesn't work
```

  What do you think the "correct" behavior is here?

I fixed a bunch of minor doc issues.  I also added a lot of 

```

::

```

between doctests which were meant to be viewed, because otherwise one will not be able to evaluate these plots in the live documentation (this is standard).



---

archive/issue_comments_033620.json:
```json
{
    "body": "Attachment [trac_4529-add-log-scale.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-add-log-scale.patch) by @kcrisman created at 2012-05-29 00:05:05",
    "created_at": "2012-05-29T00:05:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33620",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_4529-add-log-scale.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-add-log-scale.patch) by @kcrisman created at 2012-05-29 00:05:05



---

archive/issue_comments_033621.json:
```json
{
    "body": "Attachment [trac_4529-single-tick.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-single-tick.patch) by @kcrisman created at 2012-05-29 00:05:17",
    "created_at": "2012-05-29T00:05:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33621",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_4529-single-tick.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-single-tick.patch) by @kcrisman created at 2012-05-29 00:05:17



---

archive/issue_comments_033622.json:
```json
{
    "body": "Attachment [trac_4529-docs-and-funcs.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-docs-and-funcs.patch) by @kcrisman created at 2012-05-29 00:05:29",
    "created_at": "2012-05-29T00:05:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33622",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_4529-docs-and-funcs.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-docs-and-funcs.patch) by @kcrisman created at 2012-05-29 00:05:29



---

archive/issue_comments_033623.json:
```json
{
    "body": "Attachment [trac_4529-more-doc.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-more-doc.patch) by @kcrisman created at 2012-05-29 00:06:15",
    "created_at": "2012-05-29T00:06:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33623",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_4529-more-doc.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-more-doc.patch) by @kcrisman created at 2012-05-29 00:06:15



---

archive/issue_comments_033624.json:
```json
{
    "body": "Okay, ppurka, ready for your comments on this whole mess.  I've uploaded refreshed patches of yours, as well as a new one of doc fixes.  The three issues (non-integer base, adding, list plots with list input) remain, so I am not putting \"needs review\" yet.\n\nPatchbot: Apply trac_4529-add-log-scale.patch, trac_4529-single-tick.patch, trac_4529-docs-and-funcs.patch, and trac_4529-more-doc.patch.",
    "created_at": "2012-05-29T00:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33624",
    "user": "https://github.com/kcrisman"
}
```

Okay, ppurka, ready for your comments on this whole mess.  I've uploaded refreshed patches of yours, as well as a new one of doc fixes.  The three issues (non-integer base, adding, list plots with list input) remain, so I am not putting "needs review" yet.

Patchbot: Apply trac_4529-add-log-scale.patch, trac_4529-single-tick.patch, trac_4529-docs-and-funcs.patch, and trac_4529-more-doc.patch.



---

archive/issue_comments_033625.json:
```json
{
    "body": "* trac_4529-add-log-scale.patch looks good.\n* trac_4529-single-tick.patch also seems ok. I guess, we just have to leave it up to the common sense of the user in certain cases.\n* trac_4529-docs-and-funcs.patch - I see that you fixed some of the typos!\n* trac_4529-more-doc.patch - yes, this is good.\n----\n* Adding another patch which fixes some more typos.\n* `list_plot` does seem to behave a bit weird sometimes. But if we use `plotjoined=True`, then it works fine. Thanks for figuring out where it goes awry. I will have a look into it. Should the fix go into a separate ticket?\n* The plot commands in the documentation of `arc` and other functions don't usually work with the check for ticks and with log scale. This is even with `base=2`. For instance, the plot below. I guess we have to leave this up to the user to give a proper input.\n\n```\narc((2,3), 2, 1, angle=pi/5, sector=(0,pi/2)).show(scale='loglog', base=2)\narc((2,3), 2, 1, sector=(0,pi/2)).show(scale='loglog', base=2)\n```\n\n* For some commands like `disk` where an aspect ratio warning is given by matplotlib, we can leave it up to the user I think. The fix is relatively simple though; see the code for `parametric_plot` in the [attachment:trac_4529-docs-and-funcs.patch]. If we fix `disk`, then we need to weed out all the cases for the rest of the commands in `sage.plot.*`.\n* For adding plots - again we leave it up to the user. At present, adding log + linear works and matplotlib handles it. So, we should leave it at that. In my earlier code, I raised error because it was getting ambiguous what scale to set the `Graphics._xscale`, etc attribute to in case the user set the axis to log scale. It seems matplotlib prefers log over linear and sets everything to log.",
    "created_at": "2012-05-29T03:10:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33625",
    "user": "https://github.com/ppurka"
}
```

* trac_4529-add-log-scale.patch looks good.
* trac_4529-single-tick.patch also seems ok. I guess, we just have to leave it up to the common sense of the user in certain cases.
* trac_4529-docs-and-funcs.patch - I see that you fixed some of the typos!
* trac_4529-more-doc.patch - yes, this is good.
----
* Adding another patch which fixes some more typos.
* `list_plot` does seem to behave a bit weird sometimes. But if we use `plotjoined=True`, then it works fine. Thanks for figuring out where it goes awry. I will have a look into it. Should the fix go into a separate ticket?
* The plot commands in the documentation of `arc` and other functions don't usually work with the check for ticks and with log scale. This is even with `base=2`. For instance, the plot below. I guess we have to leave this up to the user to give a proper input.

```
arc((2,3), 2, 1, angle=pi/5, sector=(0,pi/2)).show(scale='loglog', base=2)
arc((2,3), 2, 1, sector=(0,pi/2)).show(scale='loglog', base=2)
```

* For some commands like `disk` where an aspect ratio warning is given by matplotlib, we can leave it up to the user I think. The fix is relatively simple though; see the code for `parametric_plot` in the [attachment:trac_4529-docs-and-funcs.patch]. If we fix `disk`, then we need to weed out all the cases for the rest of the commands in `sage.plot.*`.
* For adding plots - again we leave it up to the user. At present, adding log + linear works and matplotlib handles it. So, we should leave it at that. In my earlier code, I raised error because it was getting ambiguous what scale to set the `Graphics._xscale`, etc attribute to in case the user set the axis to log scale. It seems matplotlib prefers log over linear and sets everything to log.



---

archive/issue_comments_033626.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-05-29T03:17:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33626",
    "user": "https://github.com/ppurka"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_033627.json:
```json
{
    "body": "Added the typo fixes. I am good with your changes. So, it requires your review (as if you haven't reviewed enough already!) ;)",
    "created_at": "2012-05-29T03:17:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33627",
    "user": "https://github.com/ppurka"
}
```

Added the typo fixes. I am good with your changes. So, it requires your review (as if you haven't reviewed enough already!) ;)



---

archive/issue_comments_033628.json:
```json
{
    "body": "Forgot about noninteger bases: I think we should discourage the users from using them.",
    "created_at": "2012-05-29T03:20:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33628",
    "user": "https://github.com/ppurka"
}
```

Forgot about noninteger bases: I think we should discourage the users from using them.



---

archive/issue_comments_033629.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-05-29T03:23:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33629",
    "user": "https://github.com/ppurka"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_033630.json:
```json
{
    "body": "Thanks for the latest work!\n\nIn your latest patch, I see things like\n\n```\nThe `\"semilogx\"` scale\n```\n\nBut this will typeset as a LaTeX style thing, which is wrong.  Try\n\n```\nThe ``\"semilogx\"`` scale\n```\n\nand then all should be well with those.  Easy enough to update on the last patch.\n\n> Forgot about noninteger bases: I think we should discourage the users from using them.\nHmm, ok.  In that case maybe you can update your latest patch to still do the \"e\" example but make it really clear that this is (currently) not intended input?  I don't want to actually check for integers, though; presumably in some contexts one could want 1.5.   Do you think I should report this upstream to mpl?\n> list_plot does seem to behave a bit weird sometimes. But if we use plotjoined=True, then it works fine. Thanks for figuring out where it goes awry. I will have a look into it. Should the fix go into a separate ticket?\nAs long as we document that things can screw up on the x-axis for list_plot if you don't use plotjoined=True.  That can go in your patch update too :)\n> If we fix disk, then we need to weed out all the cases for the rest of the commands in sage.plot.*\nTrue.  And I noticed the parametric business later on, good catch.  I think this might be worth doing.  Again, I'm not really worried - we had some fun laughing at the plots one gets from loglog plots of arcs and circles here.  But anyway.\n> It seems matplotlib prefers log over linear and sets everything to log.\nOh, that explains what I saw.  I have to say it was very weird.\n\nI await the latest version of the last (?) patch.",
    "created_at": "2012-05-29T03:30:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33630",
    "user": "https://github.com/kcrisman"
}
```

Thanks for the latest work!

In your latest patch, I see things like

```
The `"semilogx"` scale
```

But this will typeset as a LaTeX style thing, which is wrong.  Try

```
The ``"semilogx"`` scale
```

and then all should be well with those.  Easy enough to update on the last patch.

> Forgot about noninteger bases: I think we should discourage the users from using them.
Hmm, ok.  In that case maybe you can update your latest patch to still do the "e" example but make it really clear that this is (currently) not intended input?  I don't want to actually check for integers, though; presumably in some contexts one could want 1.5.   Do you think I should report this upstream to mpl?
> list_plot does seem to behave a bit weird sometimes. But if we use plotjoined=True, then it works fine. Thanks for figuring out where it goes awry. I will have a look into it. Should the fix go into a separate ticket?
As long as we document that things can screw up on the x-axis for list_plot if you don't use plotjoined=True.  That can go in your patch update too :)
> If we fix disk, then we need to weed out all the cases for the rest of the commands in sage.plot.*
True.  And I noticed the parametric business later on, good catch.  I think this might be worth doing.  Again, I'm not really worried - we had some fun laughing at the plots one gets from loglog plots of arcs and circles here.  But anyway.
> It seems matplotlib prefers log over linear and sets everything to log.
Oh, that explains what I saw.  I have to say it was very weird.

I await the latest version of the last (?) patch.



---

archive/issue_comments_033631.json:
```json
{
    "body": "Yes. Working on a lost patch. It should be up in a short while.",
    "created_at": "2012-05-29T04:27:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33631",
    "user": "https://github.com/ppurka"
}
```

Yes. Working on a lost patch. It should be up in a short while.



---

archive/issue_comments_033632.json:
```json
{
    "body": "I found my \"lost\" patch. *phew*",
    "created_at": "2012-05-29T05:13:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33632",
    "user": "https://github.com/ppurka"
}
```

I found my "lost" patch. *phew*



---

archive/issue_comments_033633.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-05-29T05:13:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33633",
    "user": "https://github.com/ppurka"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_033634.json:
```json
{
    "body": "Reporting it to mpl is probably the right way to handle noninteger bases. They can check on their end, and change the labeling to `%.2f^{%d}` if a noninteger base is detected.",
    "created_at": "2012-05-29T05:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33634",
    "user": "https://github.com/ppurka"
}
```

Reporting it to mpl is probably the right way to handle noninteger bases. They can check on their end, and change the labeling to `%.2f^{%d}` if a noninteger base is detected.



---

archive/issue_comments_033635.json:
```json
{
    "body": "> I found my \"lost\" patch. *phew*\nGood thing!\n\nI've opened [https://github.com/matplotlib/matplotlib/issues/909](https://github.com/matplotlib/matplotlib/issues/909) for the mpl issue.  Hopefully we'll hear something eventually.\n\nVery minor request - on an update of your patch, perhaps.\n\n```\nNote: \n\n- Although it is possible to provide a noninteger ``base``, the \n```\n\nmaybe that could be in a standard \n\n```\n.. note\n\n   Although it is possible ...\n```\n\nwhich would render nicely in the built documentation.\n\nThe\n\n```\n.. warning:: \n```\n\nshould have a blank line after it.\n\nHere's the complete list from `sage -docbuild reference html`.\n\n```\n/Users/.../sage-5.1.beta0/local/lib/python2.7/site-packages/sage/plot/graphics.py:docstring of sage.plot.graphics.Graphics.axes_color:3: WARNING: Bullet list ends without a blank line; unexpected unindent.\n/Users/.../sage-5.1.beta0/local/lib/python2.7/site-packages/sage/plot/graphics.py:docstring of sage.plot.graphics.Graphics.axes_color:5: ERROR: Unexpected indentation.\n/Users/.../sage-5.1.beta0/local/lib/python2.7/site-packages/sage/plot/plot.py:docstring of sage.plot.plot:89: WARNING: Explicit markup ends without a blank line; unexpected unindent.\n/Users/.../sage-5.1.beta0/local/lib/python2.7/site-packages/sage/plot/plot.py:docstring of sage.plot.plot:36: WARNING: Explicit markup ends without a blank line; unexpected unindent.\n/Users/.../sage-5.1.beta0/local/lib/python2.7/site-packages/sage/plot/plot.py:docstring of sage.plot.plot:65: WARNING: Bullet list ends without a blank line; unexpected unindent.\n/Users/.../sage-5.1.beta0/local/lib/python2.7/site-packages/sage/plot/plot.py:docstring of sage.plot.plot:67: ERROR: Unexpected indentation.\n```\n\n\nUnfortunately it's too late now for me to properly test everything again - time for bed - but I am not really too concerned, given the stuff I've been trying all along.  If you are able to deal with these formatting issues, I'd be grateful, and even if I have to deal with it slowly we should certainly be ready for positive review by the end of the week.  Hopefully by tomorrow!",
    "created_at": "2012-05-29T06:43:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33635",
    "user": "https://github.com/kcrisman"
}
```

> I found my "lost" patch. *phew*
Good thing!

I've opened [https://github.com/matplotlib/matplotlib/issues/909](https://github.com/matplotlib/matplotlib/issues/909) for the mpl issue.  Hopefully we'll hear something eventually.

Very minor request - on an update of your patch, perhaps.

```
Note: 

- Although it is possible to provide a noninteger ``base``, the 
```

maybe that could be in a standard 

```
.. note

   Although it is possible ...
```

which would render nicely in the built documentation.

The

```
.. warning:: 
```

should have a blank line after it.

Here's the complete list from `sage -docbuild reference html`.

```
/Users/.../sage-5.1.beta0/local/lib/python2.7/site-packages/sage/plot/graphics.py:docstring of sage.plot.graphics.Graphics.axes_color:3: WARNING: Bullet list ends without a blank line; unexpected unindent.
/Users/.../sage-5.1.beta0/local/lib/python2.7/site-packages/sage/plot/graphics.py:docstring of sage.plot.graphics.Graphics.axes_color:5: ERROR: Unexpected indentation.
/Users/.../sage-5.1.beta0/local/lib/python2.7/site-packages/sage/plot/plot.py:docstring of sage.plot.plot:89: WARNING: Explicit markup ends without a blank line; unexpected unindent.
/Users/.../sage-5.1.beta0/local/lib/python2.7/site-packages/sage/plot/plot.py:docstring of sage.plot.plot:36: WARNING: Explicit markup ends without a blank line; unexpected unindent.
/Users/.../sage-5.1.beta0/local/lib/python2.7/site-packages/sage/plot/plot.py:docstring of sage.plot.plot:65: WARNING: Bullet list ends without a blank line; unexpected unindent.
/Users/.../sage-5.1.beta0/local/lib/python2.7/site-packages/sage/plot/plot.py:docstring of sage.plot.plot:67: ERROR: Unexpected indentation.
```


Unfortunately it's too late now for me to properly test everything again - time for bed - but I am not really too concerned, given the stuff I've been trying all along.  If you are able to deal with these formatting issues, I'd be grateful, and even if I have to deal with it slowly we should certainly be ready for positive review by the end of the week.  Hopefully by tomorrow!



---

archive/issue_comments_033636.json:
```json
{
    "body": "Attachment [trac_4529-typo_fixes.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-typo_fixes.patch) by @ppurka created at 2012-05-29 07:17:00",
    "created_at": "2012-05-29T07:17:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33636",
    "user": "https://github.com/ppurka"
}
```

Attachment [trac_4529-typo_fixes.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-typo_fixes.patch) by @ppurka created at 2012-05-29 07:17:00



---

archive/issue_comments_033637.json:
```json
{
    "body": "updated the last patch. It should fix the rest of the warnings.\n\n```\n.../sage-5.1beta0/devel/sage\u00bb ../../sage -b && ../../sage -docbuild reference html\n\n----------------------------------------------------------\nsage: Building and installing modified Sage library files.\n\n\nInstalling c_lib\nscons: `install' is up to date.\nUpdating Cython code....\nsetup.py:650: UserWarning: could not find dependency <vector> included in /home/punarbasu/Installations/sage-5.1beta0/local/lib/python/site-packages/Cython/Includes/libcpp/vector.pxd. I will assume it is a system C/C++ header.\n  warnings.warn(msg+' I will assume it is a system C/C++ header.')\nsetup.py:650: UserWarning: could not find dependency <string> included in /home/punarbasu/Installations/sage-5.1beta0/local/lib/python/site-packages/Cython/Includes/libcpp/string.pxd. I will assume it is a system C/C++ header.\n  warnings.warn(msg+' I will assume it is a system C/C++ header.')\nExecuting 0 commands (using 0 threads)\nTime to execute 0 commands: 0.0459749698639 seconds\nFinished compiling Cython code (time = 0.499665021896 seconds)\nrunning install\nrunning build\nrunning build_py\ncopying sage/plot/plot.py -> build/lib.linux-x86_64-2.7/sage/plot\nrunning build_ext\nwarning: Replacing library search directory in linker command:\n  \"/home/punarbasu/Installations/sage-5.0.rc0/local/lib\" -> \"/home/punarbasu/Installations/sage-5.1beta0/local/lib\"\n\nExecuting 0 commands (using 0 threads)\nTime to execute 0 commands: 0.00115895271301 seconds\nTotal time spent compiling C/C++ extensions:  0.0369729995728 seconds.\nrunning install_lib\ncopying build/lib.linux-x86_64-2.7/sage/plot/plot.py -> /home/punarbasu/Installations/sage-5.1beta0/local/lib/python2.7/site-packages/sage/plot\nbyte-compiling /home/punarbasu/Installations/sage-5.1beta0/local/lib/python2.7/site-packages/sage/plot/plot.py to plot.pyc\nrunning install_egg_info\nRemoving /home/punarbasu/Installations/sage-5.1beta0/local/lib/python2.7/site-packages/sage-0.0.0-py2.7.egg-info\nWriting /home/punarbasu/Installations/sage-5.1beta0/local/lib/python2.7/site-packages/sage-0.0.0-py2.7.egg-info\n\nreal\t0m1.513s\nuser\t0m1.202s\nsys\t0m0.206s\nsphinx-build -b html -d /home/punarbasu/Installations/sage-5.1beta0/devel/sage/doc/output/doctrees/en/reference    /home/punarbasu/Installations/sage-5.1beta0/devel/sage/doc/en/reference /home/punarbasu/Installations/sage-5.1beta0/devel/sage/doc/output/html/en/reference\nRunning Sphinx v1.1.2\nloading pickled environment... done\nloading intersphinx inventory from /home/punarbasu/Installations/sage-5.1beta0/devel/sage/doc/common/python.inv...\nbuilding [html]: targets for 1 source files that are out of date\nupdating environment: 0 added, 1 changed, 0 removed\nreading sources... [100%] sage/plot/plot                                        \nlooking for now-outdated files... none found\npickling environment... done\nchecking consistency... done\npreparing documents... done\nWARNING: dvipng command 'dvipng' cannot be run (needed for math display), check the pngmath_dvipng setting\nwriting output... [100%] sage/plot/plot                                         \nwriting additional files... genindex py-modindex search\ncopying static files... done\ndumping search index... done\ndumping object inventory... done\nbuild succeeded, 1 warning.\nBuild finished.  The built documents can be found in /home/punarbasu/Installations/sage-5.1beta0/devel/sage/doc/output/html/en/reference\n```\n",
    "created_at": "2012-05-29T07:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33637",
    "user": "https://github.com/ppurka"
}
```

updated the last patch. It should fix the rest of the warnings.

```
.../sage-5.1beta0/devel/sage» ../../sage -b && ../../sage -docbuild reference html

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
setup.py:650: UserWarning: could not find dependency <vector> included in /home/punarbasu/Installations/sage-5.1beta0/local/lib/python/site-packages/Cython/Includes/libcpp/vector.pxd. I will assume it is a system C/C++ header.
  warnings.warn(msg+' I will assume it is a system C/C++ header.')
setup.py:650: UserWarning: could not find dependency <string> included in /home/punarbasu/Installations/sage-5.1beta0/local/lib/python/site-packages/Cython/Includes/libcpp/string.pxd. I will assume it is a system C/C++ header.
  warnings.warn(msg+' I will assume it is a system C/C++ header.')
Executing 0 commands (using 0 threads)
Time to execute 0 commands: 0.0459749698639 seconds
Finished compiling Cython code (time = 0.499665021896 seconds)
running install
running build
running build_py
copying sage/plot/plot.py -> build/lib.linux-x86_64-2.7/sage/plot
running build_ext
warning: Replacing library search directory in linker command:
  "/home/punarbasu/Installations/sage-5.0.rc0/local/lib" -> "/home/punarbasu/Installations/sage-5.1beta0/local/lib"

Executing 0 commands (using 0 threads)
Time to execute 0 commands: 0.00115895271301 seconds
Total time spent compiling C/C++ extensions:  0.0369729995728 seconds.
running install_lib
copying build/lib.linux-x86_64-2.7/sage/plot/plot.py -> /home/punarbasu/Installations/sage-5.1beta0/local/lib/python2.7/site-packages/sage/plot
byte-compiling /home/punarbasu/Installations/sage-5.1beta0/local/lib/python2.7/site-packages/sage/plot/plot.py to plot.pyc
running install_egg_info
Removing /home/punarbasu/Installations/sage-5.1beta0/local/lib/python2.7/site-packages/sage-0.0.0-py2.7.egg-info
Writing /home/punarbasu/Installations/sage-5.1beta0/local/lib/python2.7/site-packages/sage-0.0.0-py2.7.egg-info

real	0m1.513s
user	0m1.202s
sys	0m0.206s
sphinx-build -b html -d /home/punarbasu/Installations/sage-5.1beta0/devel/sage/doc/output/doctrees/en/reference    /home/punarbasu/Installations/sage-5.1beta0/devel/sage/doc/en/reference /home/punarbasu/Installations/sage-5.1beta0/devel/sage/doc/output/html/en/reference
Running Sphinx v1.1.2
loading pickled environment... done
loading intersphinx inventory from /home/punarbasu/Installations/sage-5.1beta0/devel/sage/doc/common/python.inv...
building [html]: targets for 1 source files that are out of date
updating environment: 0 added, 1 changed, 0 removed
reading sources... [100%] sage/plot/plot                                        
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
WARNING: dvipng command 'dvipng' cannot be run (needed for math display), check the pngmath_dvipng setting
writing output... [100%] sage/plot/plot                                         
writing additional files... genindex py-modindex search
copying static files... done
dumping search index... done
dumping object inventory... done
build succeeded, 1 warning.
Build finished.  The built documents can be found in /home/punarbasu/Installations/sage-5.1beta0/devel/sage/doc/output/html/en/reference
```




---

archive/issue_comments_033638.json:
```json
{
    "body": "Attachment [trac_4529-final-fixes.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-final-fixes.patch) by @kcrisman created at 2012-05-29 17:27:39",
    "created_at": "2012-05-29T17:27:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33638",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_4529-final-fixes.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-final-fixes.patch) by @kcrisman created at 2012-05-29 17:27:39



---

archive/issue_comments_033639.json:
```json
{
    "body": "Patchbot: \n\nApply \n* [attachment:trac_4529-add-log-scale.patch]\n* [attachment:trac_4529-single-tick.patch]\n* [attachment:trac_4529-docs-and-funcs.patch]\n* [attachment:trac_4529-more-doc.patch]\n* [attachment:trac_4529-typo_fixes.patch]\n* [attachment:trac_4529-final-fixes.patch]",
    "created_at": "2012-05-29T17:28:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33639",
    "user": "https://github.com/kcrisman"
}
```

Patchbot: 

Apply 
* [attachment:trac_4529-add-log-scale.patch]
* [attachment:trac_4529-single-tick.patch]
* [attachment:trac_4529-docs-and-funcs.patch]
* [attachment:trac_4529-more-doc.patch]
* [attachment:trac_4529-typo_fixes.patch]
* [attachment:trac_4529-final-fixes.patch]



---

archive/issue_comments_033640.json:
```json
{
    "body": "Okay, this morning I had time to make one final formatting change and add a few more tests, and change some that would not have looked right.  In particular I put the whole warning thing into one warning block - cosmetic, but useful.\n\nI think there are probably a few more corner case things we haven't thought of, but the functionality is now robust enough and well-documented enough in the corner cases we did discover that it's ready for positive review.  Although some disagree with this philosophy, my opinion is that for a project like Sage it is better to add new functionality that is 99% ready and then provide quick fixes to minor issues that remain; we simply don't have the resources to spend days trying to break it.  If you're happy with it, I'm happy with it.  What do you think?",
    "created_at": "2012-05-29T17:32:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33640",
    "user": "https://github.com/kcrisman"
}
```

Okay, this morning I had time to make one final formatting change and add a few more tests, and change some that would not have looked right.  In particular I put the whole warning thing into one warning block - cosmetic, but useful.

I think there are probably a few more corner case things we haven't thought of, but the functionality is now robust enough and well-documented enough in the corner cases we did discover that it's ready for positive review.  Although some disagree with this philosophy, my opinion is that for a project like Sage it is better to add new functionality that is 99% ready and then provide quick fixes to minor issues that remain; we simply don't have the resources to spend days trying to break it.  If you're happy with it, I'm happy with it.  What do you think?



---

archive/issue_comments_033641.json:
```json
{
    "body": "I am happy with the changes. :)\n\nNB: The patchbot won't work, because it needs to apply the dependency ticket first.",
    "created_at": "2012-05-30T01:30:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33641",
    "user": "https://github.com/ppurka"
}
```

I am happy with the changes. :)

NB: The patchbot won't work, because it needs to apply the dependency ticket first.



---

archive/issue_comments_033642.json:
```json
{
    "body": "The patchbot will work - I will make it work!\n\nPatchbot, listen carefully! apply trac_4529-add-log-scale.patch trac_4529-single-tick.patch trac_4529-docs-and-funcs.patch trac_4529-more-doc.patch trac_4529-typo_fixes.patch trac_4529-final-fixes.patch !!!",
    "created_at": "2012-05-30T02:53:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33642",
    "user": "https://github.com/kini"
}
```

The patchbot will work - I will make it work!

Patchbot, listen carefully! apply trac_4529-add-log-scale.patch trac_4529-single-tick.patch trac_4529-docs-and-funcs.patch trac_4529-more-doc.patch trac_4529-typo_fixes.patch trac_4529-final-fixes.patch !!!



---

archive/issue_comments_033643.json:
```json
{
    "body": "I was hoping you'd say: \"Patch bot, these are the files you are looking for\"  (I hope that space makes this comment really just a comment!) (and, uh, that was a star wars reference...)",
    "created_at": "2012-05-30T03:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33643",
    "user": "https://github.com/jasongrout"
}
```

I was hoping you'd say: "Patch bot, these are the files you are looking for"  (I hope that space makes this comment really just a comment!) (and, uh, that was a star wars reference...)



---

archive/issue_comments_033644.json:
```json
{
    "body": "Replying to [comment:65 jason]:\n> I was hoping you'd say: \"Patch bot, these are the files you are looking for\"  (I hope that space makes this comment really just a comment!) (and, uh, that was a star wars reference...)\n\nHa ha! The bot listens only to kini!",
    "created_at": "2012-05-30T03:51:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33644",
    "user": "https://github.com/ppurka"
}
```

Replying to [comment:65 jason]:
> I was hoping you'd say: "Patch bot, these are the files you are looking for"  (I hope that space makes this comment really just a comment!) (and, uh, that was a star wars reference...)

Ha ha! The bot listens only to kini!



---

archive/issue_comments_033645.json:
```json
{
    "body": "You don't actually have to address the patchbot to make it understand - you just need the word \"apply\" followed by the correct patch names in the correct order in plain text, possibly on the same line, I don't remember. I just mention the patchbot so people don't wonder what the cryptic comment with patch filenames in it is about.",
    "created_at": "2012-05-30T03:56:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33645",
    "user": "https://github.com/kini"
}
```

You don't actually have to address the patchbot to make it understand - you just need the word "apply" followed by the correct patch names in the correct order in plain text, possibly on the same line, I don't remember. I just mention the patchbot so people don't wonder what the cryptic comment with patch filenames in it is about.



---

archive/issue_comments_033646.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-05-30T04:34:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33646",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_033647.json:
```json
{
    "body": "Attachment [trac_4529-typo_fixes-rebase.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-typo_fixes-rebase.patch) by @kcrisman created at 2012-05-30 04:34:17\n\nLuckily I only had to rebase one of these, due to some fuzz which the release manager doesn't always like.  Otherwise this is good to go!  Note the long list of dependencies, only so that all patches apply properly on 5.1.beta1.\n\nPositive review!\n\nPatchbot, apply apply trac_4529-add-log-scale.patch trac_4529-single-tick.patch trac_4529-docs-and-funcs.patch trac_4529-more-doc.patch trac_4529-typo_fixes-rebase.patch trac_4529-final-fixes.patch",
    "created_at": "2012-05-30T04:34:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33647",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_4529-typo_fixes-rebase.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-typo_fixes-rebase.patch) by @kcrisman created at 2012-05-30 04:34:17

Luckily I only had to rebase one of these, due to some fuzz which the release manager doesn't always like.  Otherwise this is good to go!  Note the long list of dependencies, only so that all patches apply properly on 5.1.beta1.

Positive review!

Patchbot, apply apply trac_4529-add-log-scale.patch trac_4529-single-tick.patch trac_4529-docs-and-funcs.patch trac_4529-more-doc.patch trac_4529-typo_fixes-rebase.patch trac_4529-final-fixes.patch



---

archive/issue_comments_033648.json:
```json
{
    "body": "Patchbot apply: trac_4529-add-log-scale.patch trac_4529-single-tick.patch trac_4529-docs-and-funcs.patch trac_4529-more-doc.patch trac_4529-typo_fixes-rebase.patch trac_4529-final-fixes.patch",
    "created_at": "2012-05-30T10:56:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33648",
    "user": "https://github.com/ppurka"
}
```

Patchbot apply: trac_4529-add-log-scale.patch trac_4529-single-tick.patch trac_4529-docs-and-funcs.patch trac_4529-more-doc.patch trac_4529-typo_fixes-rebase.patch trac_4529-final-fixes.patch



---

archive/issue_comments_033649.json:
```json
{
    "body": "Attachment [trac_4529-docs-and-funcs.2.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-docs-and-funcs.2.patch) by @ppurka created at 2012-06-02 02:52:17",
    "created_at": "2012-06-02T02:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33649",
    "user": "https://github.com/ppurka"
}
```

Attachment [trac_4529-docs-and-funcs.2.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-docs-and-funcs.2.patch) by @ppurka created at 2012-06-02 02:52:17



---

archive/issue_comments_033650.json:
```json
{
    "body": "Attachment [trac_4529-typo_fixes-rebase.2.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-typo_fixes-rebase.2.patch) by @ppurka created at 2012-06-02 02:53:32",
    "created_at": "2012-06-02T02:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33650",
    "user": "https://github.com/ppurka"
}
```

Attachment [trac_4529-typo_fixes-rebase.2.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-typo_fixes-rebase.2.patch) by @ppurka created at 2012-06-02 02:53:32



---

archive/issue_comments_033651.json:
```json
{
    "body": "I noticed that the case when `scale` is a list wasn't handled for changing aspect ratio in the new code. It's a non-fatal case, but it is nice to make sure that user doesn't get warnings from mpl. Updated two of the patches. Changes can be [seen here](https://github.com/ppurka/sage-patches/commit/36f9d7997ca3d6023c84d5146bc138a9952f91cc).\n\nPatchbot apply: trac_4529-add-log-scale.patch trac_4529-single-tick.patch trac_4529-docs-and-funcs.2.patch trac_4529-more-doc.patch trac_4529-typo_fixes-rebase.2.patch trac_4529-final-fixes.patch",
    "created_at": "2012-06-02T02:56:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33651",
    "user": "https://github.com/ppurka"
}
```

I noticed that the case when `scale` is a list wasn't handled for changing aspect ratio in the new code. It's a non-fatal case, but it is nice to make sure that user doesn't get warnings from mpl. Updated two of the patches. Changes can be [seen here](https://github.com/ppurka/sage-patches/commit/36f9d7997ca3d6023c84d5146bc138a9952f91cc).

Patchbot apply: trac_4529-add-log-scale.patch trac_4529-single-tick.patch trac_4529-docs-and-funcs.2.patch trac_4529-more-doc.patch trac_4529-typo_fixes-rebase.2.patch trac_4529-final-fixes.patch



---

archive/issue_comments_033652.json:
```json
{
    "body": "Okay by me as long as it all still applies, as it appears you have been very careful to ensure!  You really do find some good corner cases!",
    "created_at": "2012-06-02T03:25:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33652",
    "user": "https://github.com/kcrisman"
}
```

Okay by me as long as it all still applies, as it appears you have been very careful to ensure!  You really do find some good corner cases!



---

archive/issue_comments_033653.json:
```json
{
    "body": "I'll try to rebase #12974 this morning.",
    "created_at": "2012-06-28T13:37:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33653",
    "user": "https://github.com/kcrisman"
}
```

I'll try to rebase #12974 this morning.



---

archive/issue_comments_033654.json:
```json
{
    "body": "Note that #12974 needs work though...",
    "created_at": "2012-06-28T13:43:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33654",
    "user": "https://github.com/jdemeyer"
}
```

Note that #12974 needs work though...



---

archive/issue_comments_033655.json:
```json
{
    "body": "> Note that #12974 needs work though...\nYes, I saw that.  It looks like they are all the result of just one name-mangling change or something, though, so hopefully not a problem.",
    "created_at": "2012-06-28T14:31:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33655",
    "user": "https://github.com/kcrisman"
}
```

> Note that #12974 needs work though...
Yes, I saw that.  It looks like they are all the result of just one name-mangling change or something, though, so hopefully not a problem.



---

archive/issue_comments_033656.json:
```json
{
    "body": "Okay, #12974 seems to be all set, so one would just have to check that this still applied on top of that.",
    "created_at": "2012-06-28T15:02:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33656",
    "user": "https://github.com/kcrisman"
}
```

Okay, #12974 seems to be all set, so one would just have to check that this still applied on top of that.



---

archive/issue_comments_033657.json:
```json
{
    "body": "Yuck.  Lots of places it doesn't apply correctly.  I'll try to take care of this now.",
    "created_at": "2012-06-28T18:10:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33657",
    "user": "https://github.com/kcrisman"
}
```

Yuck.  Lots of places it doesn't apply correctly.  I'll try to take care of this now.



---

archive/issue_comments_033658.json:
```json
{
    "body": "Every single conflict was due to whitespace (and hence probably fallout from #12974's extra patch.  Grr.  Patches coming up.",
    "created_at": "2012-06-28T18:34:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33658",
    "user": "https://github.com/kcrisman"
}
```

Every single conflict was due to whitespace (and hence probably fallout from #12974's extra patch.  Grr.  Patches coming up.



---

archive/issue_comments_033659.json:
```json
{
    "body": "Wasn't the whitespace patch from #12974 removed?  Why are there still conflicts?",
    "created_at": "2012-06-28T18:39:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33659",
    "user": "https://github.com/jasongrout"
}
```

Wasn't the whitespace patch from #12974 removed?  Why are there still conflicts?



---

archive/issue_comments_033660.json:
```json
{
    "body": "> Wasn't the whitespace patch from #12974 removed?  Why are there still conflicts?\nIt *was* removed.   But these patches are all based on the 'old' #12974.  There would *not* have been conflicts if we had kept that patch.\n\nAnyway, I just finished, so hold on a sec.  It would be good for someone to look at things to make sure I did the rebasing right.",
    "created_at": "2012-06-28T18:43:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33660",
    "user": "https://github.com/kcrisman"
}
```

> Wasn't the whitespace patch from #12974 removed?  Why are there still conflicts?
It *was* removed.   But these patches are all based on the 'old' #12974.  There would *not* have been conflicts if we had kept that patch.

Anyway, I just finished, so hold on a sec.  It would be good for someone to look at things to make sure I did the rebasing right.



---

archive/issue_comments_033661.json:
```json
{
    "body": "Attachment [trac_4529-patch2.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-patch2.patch) by @kcrisman created at 2012-06-28 19:15:36",
    "created_at": "2012-06-28T19:15:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33661",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_4529-patch2.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-patch2.patch) by @kcrisman created at 2012-06-28 19:15:36



---

archive/issue_comments_033662.json:
```json
{
    "body": "Attachment [trac_4529-patch5.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-patch5.patch) by @kcrisman created at 2012-06-28 19:16:23",
    "created_at": "2012-06-28T19:16:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33662",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_4529-patch5.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-patch5.patch) by @kcrisman created at 2012-06-28 19:16:23



---

archive/issue_comments_033663.json:
```json
{
    "body": "Attachment [trac_4529-patch6.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-patch6.patch) by @kcrisman created at 2012-06-28 19:16:40",
    "created_at": "2012-06-28T19:16:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33663",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_4529-patch6.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-patch6.patch) by @kcrisman created at 2012-06-28 19:16:40



---

archive/issue_comments_033664.json:
```json
{
    "body": "Sorry for all the patches, but I was trying to make sure things looked the same.  These are the same six patches, just in numerical number - didn't want to add more rebase suffixes.\n\n\nApply \n* [attachment:trac_4529-patch1.patch]\n* [attachment:trac_4529-patch2.patch]\n* [attachment:trac_4529-patch3.patch]\n* [attachment:trac_4529-patch4.patch]\n* [attachment:trac_4529-patch5.patch]\n* [attachment:trac_4529-patch6.patch]",
    "created_at": "2012-06-28T19:19:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33664",
    "user": "https://github.com/kcrisman"
}
```

Sorry for all the patches, but I was trying to make sure things looked the same.  These are the same six patches, just in numerical number - didn't want to add more rebase suffixes.


Apply 
* [attachment:trac_4529-patch1.patch]
* [attachment:trac_4529-patch2.patch]
* [attachment:trac_4529-patch3.patch]
* [attachment:trac_4529-patch4.patch]
* [attachment:trac_4529-patch5.patch]
* [attachment:trac_4529-patch6.patch]



---

archive/issue_comments_033665.json:
```json
{
    "body": "Plots seem fine still.\n\nWith respect to one minor issue - this is nothing to do with positive review, but a question for ppurka.  \n\nCompare\n\n```\nplot(x,(x,-1,1),xmin=1,xmax=-1)\nplot(x,(x,-1,1)).show(xmin=1,xmax=-1)\n```\n\nwith the patches (or even just first patch).  I would think they should be the same (i.e., like the second one, as commented in the first patch).",
    "created_at": "2012-06-28T19:32:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33665",
    "user": "https://github.com/kcrisman"
}
```

Plots seem fine still.

With respect to one minor issue - this is nothing to do with positive review, but a question for ppurka.  

Compare

```
plot(x,(x,-1,1),xmin=1,xmax=-1)
plot(x,(x,-1,1)).show(xmin=1,xmax=-1)
```

with the patches (or even just first patch).  I would think they should be the same (i.e., like the second one, as commented in the first patch).



---

archive/issue_comments_033666.json:
```json
{
    "body": "Hello, sorry for not being able to participate. Currntly posting from an airport kiosk. I thought they should be the same. I will have to check if the code is only triggered from matplotlib, or if the points are sorted before the `render_to_subplot`.",
    "created_at": "2012-06-28T19:37:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33666",
    "user": "https://github.com/ppurka"
}
```

Hello, sorry for not being able to participate. Currntly posting from an airport kiosk. I thought they should be the same. I will have to check if the code is only triggered from matplotlib, or if the points are sorted before the `render_to_subplot`.



---

archive/issue_comments_033667.json:
```json
{
    "body": "By the way many thanks to you (kcrisman), jason and jeroen for doing the rebasing :)",
    "created_at": "2012-06-28T19:41:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33667",
    "user": "https://github.com/ppurka"
}
```

By the way many thanks to you (kcrisman), jason and jeroen for doing the rebasing :)



---

archive/issue_comments_033668.json:
```json
{
    "body": "> Hello, sorry for not being able to participate. Currntly posting from an airport kiosk. I thought they should be the same. I will have to check if the code is only triggered from matplotlib, or if the points are sorted before the `render_to_subplot`.\nI wouldn't be surprised if they were.\n\nAnyway, when you figure it out, open a ticket :)  Have a great trip, wherever you go.",
    "created_at": "2012-06-28T19:51:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33668",
    "user": "https://github.com/kcrisman"
}
```

> Hello, sorry for not being able to participate. Currntly posting from an airport kiosk. I thought they should be the same. I will have to check if the code is only triggered from matplotlib, or if the points are sorted before the `render_to_subplot`.
I wouldn't be surprised if they were.

Anyway, when you figure it out, open a ticket :)  Have a great trip, wherever you go.



---

archive/issue_comments_033669.json:
```json
{
    "body": "Replying to [comment:86 kcrisman]:\n> Sorry for all the patches, but I was trying to make sure things looked the same.  These are the same six patches, just in numerical number\n\nAwesome!",
    "created_at": "2012-06-29T15:45:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33669",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:86 kcrisman]:
> Sorry for all the patches, but I was trying to make sure things looked the same.  These are the same six patches, just in numerical number

Awesome!



---

archive/issue_comments_033670.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2012-07-03T09:55:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33670",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_033671.json:
```json
{
    "body": "[attachment:trac_4529-patch4.patch] needs a proper commit message.",
    "created_at": "2012-07-03T09:55:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33671",
    "user": "https://github.com/jdemeyer"
}
```

[attachment:trac_4529-patch4.patch] needs a proper commit message.



---

archive/issue_comments_033672.json:
```json
{
    "body": "> [attachment:trac_4529-patch4.patch] needs a proper commit message.\nHuh, that happened the last time too.  Sorry, I don't know how I missed that.  Coming up.",
    "created_at": "2012-07-03T13:17:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33672",
    "user": "https://github.com/kcrisman"
}
```

> [attachment:trac_4529-patch4.patch] needs a proper commit message.
Huh, that happened the last time too.  Sorry, I don't know how I missed that.  Coming up.



---

archive/issue_comments_033673.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2012-07-03T13:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33673",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_033674.json:
```json
{
    "body": "Attachment [trac_4529-patch4.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-patch4.patch) by @kcrisman created at 2012-07-03 13:18:40",
    "created_at": "2012-07-03T13:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33674",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_4529-patch4.patch](tarball://root/attachments/some-uuid/ticket4529/trac_4529-patch4.patch) by @kcrisman created at 2012-07-03 13:18:40



---

archive/issue_comments_033675.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-07-03T13:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33675",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_033676.json:
```json
{
    "body": "Ok, should be all set.",
    "created_at": "2012-07-03T13:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33676",
    "user": "https://github.com/kcrisman"
}
```

Ok, should be all set.



---

archive/issue_events_004775.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2012-07-07T22:28:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4529#event-4775"
}
```



---

archive/issue_comments_033677.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-07-07T22:28:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33677",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_033678.json:
```json
{
    "body": "Replying to [comment:59 kcrisman]:\n> > I found my \"lost\" patch. *phew*\n> Good thing!\n> \n> I've opened [https://github.com/matplotlib/matplotlib/issues/909](https://github.com/matplotlib/matplotlib/issues/909) for the mpl issue.  Hopefully we'll hear something eventually.\n\nppurka:\n\nDid we ever open a ticket for fixing this?  Anyway, [it's been resolved](https://github.com/matplotlib/matplotlib/issues/909#issuecomment-7756212) in [this mpl pull request](https://github.com/matplotlib/matplotlib/pull/960), apparently.  I *think* that we put in a comment about how this doesn't (yet) work, so there would be something to do now that this has been done.",
    "created_at": "2012-08-15T14:00:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4529",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4529#issuecomment-33678",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:59 kcrisman]:
> > I found my "lost" patch. *phew*
> Good thing!
> 
> I've opened [https://github.com/matplotlib/matplotlib/issues/909](https://github.com/matplotlib/matplotlib/issues/909) for the mpl issue.  Hopefully we'll hear something eventually.

ppurka:

Did we ever open a ticket for fixing this?  Anyway, [it's been resolved](https://github.com/matplotlib/matplotlib/issues/909#issuecomment-7756212) in [this mpl pull request](https://github.com/matplotlib/matplotlib/pull/960), apparently.  I *think* that we put in a comment about how this doesn't (yet) work, so there would be something to do now that this has been done.
