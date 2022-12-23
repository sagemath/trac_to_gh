# Issue 4529: Implement plots with logarithmic scale

Issue created by migration from https://trac.sagemath.org/ticket/4529

Original creator: ronanpaixao

Original creation time: 2008-11-15 18:59:14

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


---

Attachment

"Wrong" sage plot with log scale


---

Comment by mabshoff created at 2008-11-15 19:03:30

This is a dupe if #4530

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-15 19:03:30

Resolution: duplicate


---

Comment by mabshoff created at 2008-11-15 19:04:04

Resolution changed from duplicate to 


---

Comment by mabshoff created at 2008-11-15 19:04:04

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-11-15 19:04:25

Changing status from reopened to new.


---

Comment by mabshoff created at 2008-11-15 19:04:25

Changing assignee from somebody to ronanpaixao.


---

Comment by jason created at 2009-11-12 04:13:04

See #1431 for a way to solve this.


---

Comment by jason created at 2011-10-13 13:57:32

Since #1431 ended up just being about ticks (not the scale), #1431 doesn't directly address how to change the scale of the plot.


---

Comment by jason created at 2011-10-13 14:32:12

Here are some comments about an API.  How about adding a show keyword that specifies the scale of the axes.  

`scale='log'` -- a string specifies the scale of the vertical axis

`scale=('log','linear')` -- a tuple or list of two strings specifies scales for both axes

We'd probably like some way to pass in arguments to the scale, since different scales have different options.  This looks ugly: `scale=( ('log', {'base': 2}), 'linear')`


---

Comment by jason created at 2011-10-13 14:33:59

We could also do something like `xscale='log'` or `xscale=('log',{'base': 2})` and similarly for yscale.  I don't like using x and y, though, since the variables in the plot might not be x and y.


---

Comment by kcrisman created at 2011-10-13 15:42:07

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

Comment by kcrisman created at 2011-10-13 15:44:03

Also, #5128 would appear to be slightly related.


---

Comment by kcrisman created at 2011-10-13 15:48:53

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

Comment by ppurka created at 2012-02-08 12:44:26

plot in logarithmic scale.


---

Attachment

[attachment:logplots.py] has a new class `LogGraphics` that I implemented and have been using for the past few months. Integrating it with Graphics seemed quite a painful process, so I had to go this direction and make my own class. Currently, it handles many _but not all_ of the arguments that the `Graphics` class supports. In addition it uses `matplotlib.plt` to do the log plot; otherwise I ran into all sorts of problems with matplotlib (like the ones mentioned in earlier comments).

In engineering, we often need logarithmic plots and the logarithmic plots sometimes is of the form that the x-axis _decreases_ as we go towards the right (for example if we plot decreasing probabilities on the x-axis). This `LogGraphics` takes this into account and makes sure that if a list of x-axis points with decreasing values along the higher indices of the list, then it plots the graph with a decreasing x-axis.


---

Comment by ppurka created at 2012-02-08 13:02:12

Sorry, I meant `matplotlib.pyplot` in the above comment.


---

Comment by eviatarbach created at 2012-04-18 02:15:57

Changing status from new to needs_review.


---

Comment by ppurka created at 2012-04-18 06:37:11

I am not sure if this needs to be set to "needs_review". The main thing it is lacking is that it doesn't inherit the `Graphics` class, and hence the set of plot options it supports is much less.

On the other hand, I did try to make it inherit the `Graphics` class but then I ran into a big hurdle: the variables in the `Graphics` class are defined with double underscore `__` and so even after I inherit it, I need to use (IMHO ugly) setters and getters in order to access those variables. I tried to overcome this limitation by inheriting `Graphics` in the class `LogGraphics` and defining a separate (and mostly identical) `__init__` in `LogGraphics` but then the methods wouldn't work. Since I needed to rewrite almost everything, I decided to just rewrite everything from scratch.

One thing that I plan to do is change all the variables in the `Graphics` class to be defined with a single `_` and see how it works out. Perhaps then it might be possible to integrate this patch better and consequently have access to all the methods (and hence plot options) available to the `plot` command.


---

Comment by kcrisman created at 2012-04-18 14:21:25

Hmm, that's odd that you had to do this.   Here are two "Sage-ic" ideas.
 * Have it inherit from `GraphicPrimitive`.  That is how most classes are done, and hopefully (?) would work.
 * Have this be a `show` option, or something like that.  In principle, we wouldn't even want the graphic itself to be plotted logarithmically; one could imagine wanting to have a `Line` or other plot and then to view it with log, semilog, reverse log, or regular scales.  See Jason's wise comment:7.


---

Comment by ppurka created at 2012-04-18 15:29:49

* `GraphicsPrimitive` is unfortunately too crude for most purposes. All the important functions are defined in `Graphics`.
* I did try using `_render_on_subplot` from `line.py` but ran into the same problem as you described in comment:9. It simply doesn't work since matplotlib fails to re-render the line in log scale. Actually I ran into many more problems; I just can't remember what else. The most painless method seemed to be to use pyplot (or even pylab, but we can avoid importing that since we don't need numpy).

That said, it is IMHO better to have logarithmic plots as a separate class. For instance, it doesn't make much sense to "add" plots with different scalings (and I also raise an error in the class I created).


---

Comment by kini created at 2012-05-16 14:09:42

I'm currently cleaning up tickets marked needs_review which have no patches attached, which includes this one, so back to needs_work this goes.


---

Comment by kini created at 2012-05-16 14:09:42

Changing status from needs_review to needs_work.


---

Comment by ppurka created at 2012-05-16 16:20:32

Replying to [comment:18 kini]:
> I'm currently cleaning up tickets marked needs_review which have no patches attached, which includes this one, so back to needs_work this goes.

That's fine. I am actually working on a patch which
1. modifies the `Graphics` class to have all the attributes start with a single underscore `._` instead of `.__`. This is already working and passes all doctects at least in `devel/sage/sage/plot`
2. inherits the `Graphics` class and introduces logarithmic plots in a separate file. This is in progress and I hope I have a patch to attach to this ticket soon.


---

Comment by jason created at 2012-05-16 16:33:37

Awesome.  Just yesterday I had a feature request for log-log and semilog plots!


---

Comment by ppurka created at 2012-05-19 13:12:51

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

Comment by ppurka created at 2012-05-19 16:07:50

Hmm.. there is still a problem if I modify the `Graphics` class. It becomes impossible to add 2D and 3D graphics.


---

Comment by ppurka created at 2012-05-20 10:59:36

Replying to [comment:22 ppurka]:
> Hmm.. there is still a problem if I modify the `Graphics` class. It becomes impossible to add 2D and 3D graphics.

It was a silly thing. I just needed to reorder the check for `._*scale` to after the check for `Graphics3d` in `__add__()`. The updated patch now passes all doctests in `sage/plot`! Also, `SHOW_OPTIONS, matplotlib()` have two extra arguments: `scale`, `base` which are identical in behavior to the arguments in `set_scale()`. So, now it is possible to do this:

```
p = plot(exp, 1, 10)
p.show(scale=('loglog', 2))
```



---

Comment by ppurka created at 2012-05-20 17:13:48

Apply to devel/sage


---

Attachment

Apply to devel/sage


---

Comment by ppurka created at 2012-05-20 17:17:55

Added [attachment:trac_4529-add_docs_eg_to_some_user_facing_functions.patch another patch] to other user facing functions. Actually most of the functions in `sage.plot.*` work when `scale=...` is passed as an argument while calling the function. Using the log scale makes sense in only a couple of them though, and I have added some documentation and examples for the cases I think are pertinent.

Finally, I added some extra functions `{loglog,semilogx,semilogy}_plot`, and the corresponding list_plots. I think this should undergo a review now.

These set of patches passes all doctests in `devel/sage/sage/plot`.


---

Comment by ppurka created at 2012-05-20 17:17:55

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2012-05-24 22:39:02

Patchbot:  Apply [attachment:trac_4529-add_logscale_to_Graphics.patch] and [attachment:trac_4529-add_docs_eg_to_some_user_facing_functions.patch].


---

Comment by kcrisman created at 2012-05-24 22:51:38

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

Comment by ppurka created at 2012-05-24 23:45:00

It just seemed easier and cleaner to handle the scaling by hardcoding the scale. I will see how the patch turns out if I don't hardcode it.

Most people will expect the functions `semilog*` and `loglog*` to be present. For instance, matlab has all of those commands (matlab has it only for list plots, the function plotter called `ezplot` does not have it AFAIK), and mathematica has `LogLogPlot` and `LogLinearPlot`.

If it is not desirable, then we can simply have just two functions `log_plot(scale='loglog'|'semilogx'|'semilogy', funcs, ...)`, and `log_list_plot(scale='loglog'|'semilogx'|'semilogy', data, ...)`.


---

Comment by ppurka created at 2012-05-24 23:45:00

Changing status from needs_review to needs_work.


---

Comment by jason created at 2012-05-25 00:40:00

+1 to having loglog and semilog convenience functions.


---

Comment by kcrisman created at 2012-05-25 00:43:51

I think that anything that roughly approximates Mathematica and Matlab is fine, it was just having so many of them that might be a problem.  `log_plot` and `semilog_plot(axis=foo)` or something better would be good, and perhaps a couple similar `list_plot` ones... I have to admit I always just use `points()` instead of `list_plot`, is `list_plot` used as the name in one of these programs?

Jason, how *many* would be useful?  It's the `semilogx` and `semilogy` that seems a bit much, though if it's standard in other programs I guess it would be ok.


---

Comment by jason created at 2012-05-25 00:49:23

I personally would say a loglog and semilog (defaulting to semilogy) would be good, with an option to switch the semilog to x or y.  I guess a list plot would be convenient too, though I agree with you that points() or line() in general should be used over list_plot.  They are more powerful (mostly) anyway.


---

Comment by ppurka created at 2012-05-25 08:07:03

Replying to [comment:31 jason]:
> I personally would say a loglog and semilog (defaulting to semilogy) would be good, with an option to switch the semilog to x or y.  I guess a list plot would be convenient too, though I agree with you that points() or line() in general should be used over list_plot.  They are more powerful (mostly) anyway.

For _consistency_, we should have just one convention. It is very confusing if the options of `plot` (except for probably `plotjoined` and `data`) are also valid options for `list_plot`, but then we introduce an inconsistency via log plots. So, I would be in favor of either
1. Don't have any of the `loglog_*, semilog*` and handle scaling only through the `scale` and `base` parameters of `plot` and `list_plot` (and actually all other plots)
2. Have all the functions `loglog_plot`, `loglog_list_plot` available, and perhaps change `semilog[xy]*` to `semilog*` with an extra optional argument `log_axis='x'/'y'`. In case we follow this second rule, I would like this extra argument to be different from `axis` because it can be confused with `axes=True/False`.

I would really like this issue to be sorted out first.


---

Comment by kcrisman created at 2012-05-25 13:59:19

> For _consistency_, we should have just one convention. 
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

Comment by jason created at 2012-05-25 17:21:44

Sure, let's raise it on sage-devel.  Make sure the proposal provides specific options to vote for.


---

Comment by kcrisman created at 2012-05-26 05:05:15

Replying to [comment:34 jason]:
> Sure, let's raise it on sage-devel.  Make sure the proposal provides specific options to vote for.
Okay, hope I did it clearly enough.

[http://groups.google.com/group/sage-devel/browse_thread/thread/af20ea19c09d14a0](http://groups.google.com/group/sage-devel/browse_thread/thread/af20ea19c09d14a0)


---

Comment by ppurka created at 2012-05-26 09:07:46

Thanks kcrisman. That poll is comprehensive enough.

Updated the [attachment:trac_4529-add_logscale_to_Graphics.2.patch Graphics patch]. This now has modifications only to matplotlib and sister functions, and leaves the `Graphics` class's attributes alone.

There was a problem with the ticker in that the labels were in scientific notation (ex. `1e10`) and not in the `base^exponent` form (ex. `10^10`). This is now fixed, except for the case when the user enters a custom tick formatter. This last case is up to the user to handle.

The interface to `plot` and `list_plot` remains unchanged. However, I will wait for the poll in sage-devel before deciding what extra plot commands to introduce.


---

Comment by ppurka created at 2012-05-26 12:08:04

Updated to the correct patch. Apparently I uploaded the wrong patch several hours ago.


---

Comment by kcrisman created at 2012-05-26 23:53:09

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
 * What's going on with the `pr, i  = _, 0` thing removed?  I just don't know what it had been doing - seems to have been dead code, but I always get nervous when I have no idea what it _used'' to do...
 * kini says that the `[13:]` seems brittle if matplotlib's API changes; would it be possible to remove the specific string `\\mathdefault` instead?
 * I wonder about the not setting of the spines outward when the axes shouldn't cross.  Here is an example which serves the point:

```
sage: G = plot(exp(x), (x,5,10))
sage: G.show(scale=('semilogy', 2))
```

   I don't even think this is a very atypical example to arise in practice.  It should be documented somehow.
 * It's fairly easy to have just one tick in a given direction, which usually raises an error in normal plots but isn't raising an error for yours.  I'm not sure if one would want to raise an error like "Use a different base so that you get at least two ticks!" or something.

But even with all of these comments, and waiting for the post-poll patch, *fantastic* job on this.  Someone had to come along to finally wrap this for us, it's been requested zillions of times, and this is very worth the effort, thank you so much.


---

Comment by ppurka created at 2012-05-27 03:38:50

Replying to [comment:39 kcrisman]:
> Some comments:
>  * Shouldn't `base=2` raise an error when `scale='linear'` in your example? Maybe the 
> {{{
>        if scale is None: 
>             return ('linear', 'linear', 10, 10) 
> }}}
>    could return 'linear', 'linear', None, None?

I had thought about it. My decision was to silently ignore this error because it is not fatal in any way and we handle it properly (i.e. we ignore it and do the right thing).

*Edit:* This seems to be the same behavior as in matplotlib.

>  * In `_matplotlib_tick_formatter`, should `base` and `scale` be next to each other in the function definition?  (This is a very minor critique, of course.)

Well, except for `subplot`, the rest of the arguments are alphabetically arranged. :) Personally, I find it quite hard to find out where a particular function or argument is present in a typical Sage code. There is no particular manner in which the functions are arranged. Especially in several thousand line files like graphics.py it becomes hard to scroll around and edit code.

>  * Regardless of the outcome of the poll (on which you can vote), I think one should add a lot more examples in the documentation for `show` for the various options.  Lots of them.

I will add some more.

>  * What's going on with the `pr, i  = _, 0` thing removed?  I just don't know what it had been doing - seems to have been dead code, but I always get nervous when I have no idea what it _used'' to do...

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

> But even with all of these comments, and waiting for the post-poll patch, *fantastic* job on this.  Someone had to come along to finally wrap this for us, it's been requested zillions of times, and this is very worth the effort, thank you so much.

Thanks. I needed it for my own research! :)


---

Comment by kini created at 2012-05-27 03:45:54

Oh, I didn't mean to prevent `\\mathdefault` from coming into the string at all. I meant to just specifically remove the substring `\\mathdefault` (say with `.replace("\\mathdefault","")` or something).


---

Comment by kcrisman created at 2012-05-27 04:09:31

> I had thought about it. My decision was to silently ignore this error because it is not fatal in any way and we handle it properly (i.e. we ignore it and do the right thing).
> 
> *Edit:* This seems to be the same behavior as in matplotlib.

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

> > But even with all of these comments, and waiting for the post-poll patch, *fantastic* job on this.  Someone had to come along to finally wrap this for us, it's been requested zillions of times, and this is very worth the effort, thank you so much.
> 
> Thanks. I needed it for my own research! :)

Always good to have a good motivator!  I've found that using things in class or for some random voting theory thing has ... enhanced my motivation to work on a topic.

Looking forward to seeing the global functions.


---

Comment by ppurka created at 2012-05-27 04:26:55

Replying to [comment:41 kini]:
> Oh, I didn't mean to prevent `\\mathdefault` from coming into the string at all. I meant to just specifically remove the substring `\\mathdefault` (say with `.replace("\\mathdefault","")` or something).

indeed, the replace seems much better. Thanks.


---

Attachment

apply to devel/sage


---

Comment by ppurka created at 2012-05-27 09:26:22

The following are the changes in the latest patches:
1. labeling of minor ticks was flaky; it is fixed now.
2. added several examples to `show()`
3. fixed a problem in axes position of the matplotlib() function when custom xmax, xmin, etc were passed. Try this plot (without these patches) and then try with these patches :)

```
plot(x).show(xmin=1, xmax=-1)
```

4. there is an [attachment:trac_4529-check_for_single_tick.patch optional patch] where we check for a single tick. this is tricky and I don't know a good and complete solution. Moreover, it makes most of the functions like 'arc, disk, etc' stop "just working" with log scale. It will be good if you have a better idea how to check for ticks which don't affect these functions too. We can't use xmin, xmax, etc to determine ticks because some of them might well be negative and matplotlib will neglect these values.


---

Attachment

apply to devel/sage


---

Comment by kcrisman created at 2012-05-28 05:40:57

Sorry for the delay - I only scheduled a couple hours of work this evening.  Tomorrow I will have more time.

Hey, I just had an idea.  Maybe this ticket should be _only_ about the ticket description, and then another ticket for adding the "shortcut" commands like `plot_loglog` or whatever.  In which case the current patches might be enough!  (After much testing, of course.)  What do you think?

More comments:
* Wow, great catch on all those things like the minor ticks etc.  I haven't really tested many of these plots yet, focusing on the code right now, so I'm glad you found a lot of those things.
* We'll eventually want to add some examples (or replace some of these) with the `plot(...,scale='loglog')` format ones.  And definitely to add some to the file `plot.py`, since that is where a lot of people will look first for how to get this.  *But* that can wait until the end, I'll be happy to do that in a reviewer patch.
* Catching this thing about the flipped `xmin/xmax` and friends is just a bonus - again, great catch and solution.
* As to the optional patch, I will think about this some more tomorrow.  I do note that things still "work".  For the example you removed `G`, the example you removed did in fact work, for instance.  

```
sage: G.show(scale=('loglog', 5)) # plots
sage: G.show(scale=('loglog', 4)) # plots
sage: G.show(scale=('loglog', 6)) # error
```

  because it really depends on the _minor_ ticks as well.  I'm not sure whether having minor ticks should count as "having two ticks", especially in the relatively obscure-looking log plot situation.  I'm not even sure why

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

Comment by ppurka created at 2012-05-28 06:04:56

Replying to [comment:45 kcrisman]:
> Sorry for the delay - I only scheduled a couple hours of work this evening.  Tomorrow I will have more time.

No problems. It is better to have a good implementation than to hurry through a bad one.

> Hey, I just had an idea.  Maybe this ticket should be _only_ about the ticket description, and then another ticket for adding the "shortcut" commands like `plot_loglog` or whatever.  In which case the current patches might be enough!  (After much testing, of course.)  What do you think?

Actually, there is zero change to be done to the code in `plot` or `list_plot`, except to add some examples. The only change that the additional  patch will do is make very thin (one-liners) wrappers which defines the `plot_*` and `list_plot_*` wrappers and pass the correct scale option to `plot` and `list_plot`. The current consensus from the poll seems to favor this syntax. In view of this, the patch [attachment:trac_4529-add_docs_eg_to_some_user_facing_functions.patch] requires only a renaming of the functions, and some extra examples.

> * We'll eventually want to add some examples (or replace some of these) with the `plot(...,scale='loglog')` format ones.  And definitely to add some to the file `plot.py`, since that is where a lot of people will look first for how to get this.  *But* that can wait until the end, I'll be happy to do that in a reviewer patch.

We can add exactly similar examples to `plot()` and `list_plot()`. Currently, since the function is `Graphics.show()`, I decided to write it as `show(scale=...)` instead of `plot(scale=...)` since the former is more pertinent.

> * Catching this thing about the flipped `xmin/xmax` and friends is just a bonus - again, great catch and solution.
> * As to the optional patch, I will think about this some more tomorrow.  I do note that things still "work".  For the example you removed `G`, the example you removed did in fact work, for instance.  

Yes I am aware that the examples I provided work. But most of the examples in the docs of those functions (arc, disk, contour_plot, etc) _do not_ work out of the box, and we get the "too few ticks" error.

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

Comment by kcrisman created at 2012-05-28 19:03:33

> Actually, there is zero change to be done to the code in `plot` or `list_plot`, except to add some examples. The only change that the additional  patch will do is make very thin (one-liners) wrappers which defines the `plot_*` and `list_plot_*` wrappers and pass the correct scale option to `plot` and `list_plot`. The current consensus from the poll seems to favor this syntax. In view of this, the patch [attachment:trac_4529-add_docs_eg_to_some_user_facing_functions.patch] requires only a renaming of the functions, and some extra examples.

Oh, I didn't realize that that patch actually already implemented that - I hadn't had time to look at the patches until you had already said which patches to apply!  Yes, I should be able to rebase/rename that well for our purposes, just adding a few more examples which occur fairly frequently.

> We can add exactly similar examples to `plot()` and `list_plot()`. Currently, since the function is `Graphics.show()`, I decided to write it as `show(scale=...)` instead of `plot(scale=...)` since the former is more pertinent.

Of course.

> > * As to the optional patch, I will think about this some more tomorrow.  I do note that things still "work".  For the example you removed `G`, the example you removed did in fact work, for instance.  
> 
> Yes I am aware that the examples I provided work. But most of the examples in the docs of those functions (arc, disk, contour_plot, etc) _do not_ work out of the box, and we get the "too few ticks" error.

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

Comment by kcrisman created at 2012-05-28 21:20:28

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

Comment by kcrisman created at 2012-05-28 23:28:38

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

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Comment by kcrisman created at 2012-05-29 00:09:22

Okay, ppurka, ready for your comments on this whole mess.  I've uploaded refreshed patches of yours, as well as a new one of doc fixes.  The three issues (non-integer base, adding, list plots with list input) remain, so I am not putting "needs review" yet.

Patchbot: Apply trac_4529-add-log-scale.patch, trac_4529-single-tick.patch, trac_4529-docs-and-funcs.patch, and trac_4529-more-doc.patch.


---

Comment by ppurka created at 2012-05-29 03:10:37

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

Comment by ppurka created at 2012-05-29 03:17:59

Changing status from needs_work to needs_review.


---

Comment by ppurka created at 2012-05-29 03:17:59

Added the typo fixes. I am good with your changes. So, it requires your review (as if you haven't reviewed enough already!) ;)


---

Comment by ppurka created at 2012-05-29 03:20:55

Forgot about noninteger bases: I think we should discourage the users from using them.


---

Comment by ppurka created at 2012-05-29 03:23:12

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2012-05-29 03:30:04

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

Comment by ppurka created at 2012-05-29 04:27:42

Yes. Working on a lost patch. It should be up in a short while.


---

Comment by ppurka created at 2012-05-29 05:13:46

I found my "lost" patch. *phew*


---

Comment by ppurka created at 2012-05-29 05:13:46

Changing status from needs_work to needs_review.


---

Comment by ppurka created at 2012-05-29 05:20:31

Reporting it to mpl is probably the right way to handle noninteger bases. They can check on their end, and change the labeling to `%.2f^{%d}` if a noninteger base is detected.


---

Comment by kcrisman created at 2012-05-29 06:43:38

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

Attachment


---

Comment by ppurka created at 2012-05-29 07:18:41

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

Attachment


---

Comment by kcrisman created at 2012-05-29 17:28:45

Patchbot: 

Apply 
 * [attachment:trac_4529-add-log-scale.patch]
 * [attachment:trac_4529-single-tick.patch]
 * [attachment:trac_4529-docs-and-funcs.patch]
 * [attachment:trac_4529-more-doc.patch]
 * [attachment:trac_4529-typo_fixes.patch]
 * [attachment:trac_4529-final-fixes.patch]


---

Comment by kcrisman created at 2012-05-29 17:32:26

Okay, this morning I had time to make one final formatting change and add a few more tests, and change some that would not have looked right.  In particular I put the whole warning thing into one warning block - cosmetic, but useful.

I think there are probably a few more corner case things we haven't thought of, but the functionality is now robust enough and well-documented enough in the corner cases we did discover that it's ready for positive review.  Although some disagree with this philosophy, my opinion is that for a project like Sage it is better to add new functionality that is 99% ready and then provide quick fixes to minor issues that remain; we simply don't have the resources to spend days trying to break it.  If you're happy with it, I'm happy with it.  What do you think?


---

Comment by ppurka created at 2012-05-30 01:30:52

I am happy with the changes. :)

NB: The patchbot won't work, because it needs to apply the dependency ticket first.


---

Comment by kini created at 2012-05-30 02:53:48

The patchbot will work - I will make it work!

Patchbot, listen carefully! apply trac_4529-add-log-scale.patch trac_4529-single-tick.patch trac_4529-docs-and-funcs.patch trac_4529-more-doc.patch trac_4529-typo_fixes.patch trac_4529-final-fixes.patch !!!


---

Comment by jason created at 2012-05-30 03:31:13

I was hoping you'd say: "Patch bot, these are the files you are looking for"  (I hope that space makes this comment really just a comment!) (and, uh, that was a star wars reference...)


---

Comment by ppurka created at 2012-05-30 03:51:41

Replying to [comment:65 jason]:
> I was hoping you'd say: "Patch bot, these are the files you are looking for"  (I hope that space makes this comment really just a comment!) (and, uh, that was a star wars reference...)

Ha ha! The bot listens only to kini!


---

Comment by kini created at 2012-05-30 03:56:40

You don't actually have to address the patchbot to make it understand - you just need the word "apply" followed by the correct patch names in the correct order in plain text, possibly on the same line, I don't remember. I just mention the patchbot so people don't wonder what the cryptic comment with patch filenames in it is about.


---

Comment by kcrisman created at 2012-05-30 04:34:17

Changing status from needs_review to positive_review.


---

Attachment

Luckily I only had to rebase one of these, due to some fuzz which the release manager doesn't always like.  Otherwise this is good to go!  Note the long list of dependencies, only so that all patches apply properly on 5.1.beta1.

Positive review!

Patchbot, apply apply trac_4529-add-log-scale.patch trac_4529-single-tick.patch trac_4529-docs-and-funcs.patch trac_4529-more-doc.patch trac_4529-typo_fixes-rebase.patch trac_4529-final-fixes.patch


---

Comment by ppurka created at 2012-05-30 10:56:03

Patchbot apply: trac_4529-add-log-scale.patch trac_4529-single-tick.patch trac_4529-docs-and-funcs.patch trac_4529-more-doc.patch trac_4529-typo_fixes-rebase.patch trac_4529-final-fixes.patch


---

Attachment


---

Attachment


---

Comment by ppurka created at 2012-06-02 02:56:44

I noticed that the case when `scale` is a list wasn't handled for changing aspect ratio in the new code. It's a non-fatal case, but it is nice to make sure that user doesn't get warnings from mpl. Updated two of the patches. Changes can be [seen here](https://github.com/ppurka/sage-patches/commit/36f9d7997ca3d6023c84d5146bc138a9952f91cc).

Patchbot apply: trac_4529-add-log-scale.patch trac_4529-single-tick.patch trac_4529-docs-and-funcs.2.patch trac_4529-more-doc.patch trac_4529-typo_fixes-rebase.2.patch trac_4529-final-fixes.patch


---

Comment by kcrisman created at 2012-06-02 03:25:33

Okay by me as long as it all still applies, as it appears you have been very careful to ensure!  You really do find some good corner cases!


---

Comment by kcrisman created at 2012-06-28 13:37:34

I'll try to rebase #12974 this morning.


---

Comment by jdemeyer created at 2012-06-28 13:43:53

Note that #12974 needs work though...


---

Comment by kcrisman created at 2012-06-28 14:31:55

> Note that #12974 needs work though...
Yes, I saw that.  It looks like they are all the result of just one name-mangling change or something, though, so hopefully not a problem.


---

Comment by kcrisman created at 2012-06-28 15:02:54

Okay, #12974 seems to be all set, so one would just have to check that this still applied on top of that.


---

Comment by kcrisman created at 2012-06-28 18:10:31

Yuck.  Lots of places it doesn't apply correctly.  I'll try to take care of this now.


---

Comment by kcrisman created at 2012-06-28 18:34:05

Every single conflict was due to whitespace (and hence probably fallout from #12974's extra patch.  Grr.  Patches coming up.


---

Comment by jason created at 2012-06-28 18:39:51

Wasn't the whitespace patch from #12974 removed?  Why are there still conflicts?


---

Comment by kcrisman created at 2012-06-28 18:43:16

> Wasn't the whitespace patch from #12974 removed?  Why are there still conflicts?
It _was_ removed.   But these patches are all based on the 'old' #12974.  There would _not_ have been conflicts if we had kept that patch.

Anyway, I just finished, so hold on a sec.  It would be good for someone to look at things to make sure I did the rebasing right.


---

Attachment


---

Attachment


---

Attachment


---

Comment by kcrisman created at 2012-06-28 19:19:26

Sorry for all the patches, but I was trying to make sure things looked the same.  These are the same six patches, just in numerical number - didn't want to add more rebase suffixes.


Apply 
 * [attachment:trac_4529-patch1.patch]
 * [attachment:trac_4529-patch2.patch]
 * [attachment:trac_4529-patch3.patch]
 * [attachment:trac_4529-patch4.patch]
 * [attachment:trac_4529-patch5.patch]
 * [attachment:trac_4529-patch6.patch]


---

Comment by kcrisman created at 2012-06-28 19:32:40

Plots seem fine still.

With respect to one minor issue - this is nothing to do with positive review, but a question for ppurka.  

Compare

```
plot(x,(x,-1,1),xmin=1,xmax=-1)
plot(x,(x,-1,1)).show(xmin=1,xmax=-1)
```

with the patches (or even just first patch).  I would think they should be the same (i.e., like the second one, as commented in the first patch).


---

Comment by ppurka created at 2012-06-28 19:37:29

Hello, sorry for not being able to participate. Currntly posting from an airport kiosk. I thought they should be the same. I will have to check if the code is only triggered from matplotlib, or if the points are sorted before the `render_to_subplot`.


---

Comment by ppurka created at 2012-06-28 19:41:58

By the way many thanks to you (kcrisman), jason and jeroen for doing the rebasing :)


---

Comment by kcrisman created at 2012-06-28 19:51:04

> Hello, sorry for not being able to participate. Currntly posting from an airport kiosk. I thought they should be the same. I will have to check if the code is only triggered from matplotlib, or if the points are sorted before the `render_to_subplot`.
I wouldn't be surprised if they were.

Anyway, when you figure it out, open a ticket :)  Have a great trip, wherever you go.


---

Comment by jdemeyer created at 2012-06-29 15:45:55

Replying to [comment:86 kcrisman]:
> Sorry for all the patches, but I was trying to make sure things looked the same.  These are the same six patches, just in numerical number

Awesome!


---

Comment by jdemeyer created at 2012-07-03 09:55:22

Changing status from positive_review to needs_info.


---

Comment by jdemeyer created at 2012-07-03 09:55:22

[attachment:trac_4529-patch4.patch] needs a proper commit message.


---

Comment by kcrisman created at 2012-07-03 13:17:47

> [attachment:trac_4529-patch4.patch] needs a proper commit message.
Huh, that happened the last time too.  Sorry, I don't know how I missed that.  Coming up.


---

Comment by kcrisman created at 2012-07-03 13:18:40

Changing status from needs_info to needs_review.


---

Attachment


---

Comment by kcrisman created at 2012-07-03 13:18:56

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2012-07-03 13:18:56

Ok, should be all set.


---

Comment by jdemeyer created at 2012-07-07 22:28:35

Resolution: fixed


---

Comment by kcrisman created at 2012-08-15 14:00:41

Replying to [comment:59 kcrisman]:
> > I found my "lost" patch. *phew*
> Good thing!
> 
> I've opened [https://github.com/matplotlib/matplotlib/issues/909](https://github.com/matplotlib/matplotlib/issues/909) for the mpl issue.  Hopefully we'll hear something eventually.

ppurka:

Did we ever open a ticket for fixing this?  Anyway, [it's been resolved](https://github.com/matplotlib/matplotlib/issues/909#issuecomment-7756212) in [this mpl pull request](https://github.com/matplotlib/matplotlib/pull/960), apparently.  I _think_ that we put in a comment about how this doesn't (yet) work, so there would be something to do now that this has been done.
