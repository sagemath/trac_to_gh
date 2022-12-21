# Issue 260: transparent graphics output

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-02-12 04:20:44

Assignee: boothby

CC:  kcrisman


```

It may be helpful for users who want to use SAGE graphics on their web
pages to be able to set the background as transparent.
```



---

Attachment

The attached patch adds a keyword argument `transparency` to `plot.show()`.  The default value is `None`, which makes the image background opaque.  A number between 0 (transparent) and 1 (opaque) determines the degree of transparency.

Please test and make changes.  I'm new to the plotting code, so it's likely that I've missed and/or broken something.


---

Comment by mpatel created at 2009-08-11 02:26:00

Added examples.


---

Attachment

Perhaps `opacity` is a more appropriate keyword (`alpha` gave errors).


---

Comment by mpatel created at 2009-08-17 09:13:52

Changing component from notebook to graphics.


---

Comment by mpatel created at 2009-08-17 09:13:52

Changing assignee from boothby to was.


---

Comment by mpatel created at 2009-08-30 11:31:58

Ticket #5448 may necessitate an update.


---

Comment by jason created at 2009-08-31 13:25:15

Yes, I'm almost sure that #5448 will necessitate an update (or this will necessitate an update of #5448).

1. I would change the keyword argument to something that is used more in Sage (like alpha or opacity) if we are going to have multiple levels of transparency.  If it is just a True/False option, then "transparent" seems like a fine keyword.

2. What do you think about using the "transparent" option of savefig, as documented here: http://matplotlib.sourceforge.net/api/figure_api.html#matplotlib.figure.Figure.savefig ?

3. The transparent option of savefig has the following code.  It looks like this code not only sets the figure patch, but goes through each axes object in the figure and sets the axes patch alpha level.  We should probably do the same.


```
 1036         if transparent:
 1037             original_figure_alpha = self.patch.get_alpha()
 1038             self.patch.set_alpha(0.0)
 1039             original_axes_alpha = []
 1040             for ax in self.axes:
 1041                 patch = ax.patch
 1042                 original_axes_alpha.append(patch.get_alpha())
 1043                 patch.set_alpha(0.0)
```



---

Comment by mpatel created at 2009-08-31 22:51:50

How about adapting `savefig()`'s code for a numerical scalar option with keyword `alpha`?  Or should we consider allowing color 4-tuples, e.g., RGBA, for different figure components and plotted objects?  A disclaimer: I'm not very familiar with how matplotlib or Sage plotting works.

I'm happy to postpone this ticket's review until #5448 merges.  Alternatively, I can recommend closing this one, if it's easier to treat transparency at #5448.


---

Comment by jason created at 2009-09-01 15:59:26

I added a quick "transparent" option to the patch at #5448.  If you think it is needed, I think this ticket ought to go ahead and implement a "background_color" and/or "background_opacity" keywords, or something like that, that lets a user specify a background color and opacity.

Please look at the patch at #5448 and let me know if I didn't cover something you need done.


---

Comment by jason created at 2009-09-17 08:20:20

FYI, #5448 did implement the transparency=True/False option to show.  However, this ticket can have larger scope.  I'm slightly enlarging the title/description to reflect that fact.

On the other hand, if it's not wanted, maybe we should close this ticket after all.


---

Comment by mpatel created at 2009-09-18 06:04:49

A quick (and crude) change to `Graphics.save()` sets up a `background_color` option:

```python
        if savenow:
[...]
            background_color = None
            if kwds.has_key('background_color'):
                background_color = kwds.pop('background_color', False)

            figure=self.matplotlib(*args, **kwds)
[...]
            if background_color:
                figure.patch.set_color(background_color)
                for ax in figure.axes:
                    ax.patch.set_color(background_color)
                # Not sure how to avoid using these:
                options['edgecolor'] = background_color
                options['facecolor'] = background_color

            figure.savefig(filename,dpi=dpi,bbox_inches='tight',**options)
```

If we can avoid using the `savefig()` options, perhaps we can set a background color _and_ transparency level entirely in `matplotlib()`.  Then, I think, we could handle combinations like

 * `transparent=True, opacity=0.5`
 * `opacity=0.8, background_color='#ffbefa'`

in a way a user expects.  Thoughts?


---

Comment by mpatel created at 2009-10-23 00:25:26

Add opacity and background_color plot options.  Apply only this patch.


---

Attachment

The [attachment:trac_260-plot_bg_alpha.patch new patch] adds `background_color` and `opacity` keyword options to `plot()`.  Examples:

```python
sage: plot(x^cos(x^(sin(x))), (0, 30),  fill='axis', fillcolor='yellow', opacity=0.5)
```


```python
sage: C = 1.0
sage: a, b = var('a, b')
sage: lem = contour_plot(2 * C^2 * (b^2 - a^2) - (a^2 + b^2)^2, (a, -2, 2), (b, -2, 2), plot_points=100, transparent=True, contours=25, cmap='Spectral')
sage: lem.show(aspect_ratio=1.0, background_color='khaki')
```


Can a Sage plotting or matplotlib expert point out how to make the background uniform when _both_ `background_color` and `opacity` are given?  Try this:

```python
sage: plot(x^cos(x^(sin(x))), (0, 30),  fill='axis', fillcolor='yellow', background_color='red', opacity=0.5)
```

Note how the plot's thick "border" has a different apparent transparency level.  Is this an [alpha compositing](http://en.wikipedia.org/wiki/Alpha_compositing) or blending problem?


---

Comment by mpatel created at 2009-10-23 00:35:44

Changing status from needs_work to needs_review.


---

Comment by jason created at 2009-10-23 01:07:08

It looks like there are two patches; one for the image, and one for the axes background.  Each is set to 50% opacity, and they are layered on top of each other.

But post to the matplotlib mailing list.  I'm sure they'll have a good answer for you.


---

Comment by mpatel created at 2009-12-11 11:19:47

Changing status from needs_review to needs_work.


---

Comment by mpatel created at 2009-12-11 11:41:15

Replying to [comment:12 jason]:
> But post to the matplotlib mailing list.  I'm sure they'll have a good answer for you.

Oops.  I didn't notice your response.  I'll ask the matplotlib mavens.


---

Comment by kcrisman created at 2010-07-27 17:49:19

Any responses?


---

Comment by mpatel created at 2010-07-29 07:08:21

No, because I stupidly neglected to ask.  Sorry about this!  I'll try to ask on the matplotlib mailing list soon, probably after we release Sage 4.5.2.


---

Comment by mpatel created at 2010-09-02 07:18:48

Replying to [comment:16 mpatel]:
> No, because I stupidly neglected to ask.  Sorry about this!  I'll try to ask on the matplotlib mailing list soon, probably after we release Sage 4.5.2.

I've [posted to matplotlib-users](http://sourceforge.net/mailarchive/forum.php?thread_name=4C7F4F10.8060208%40gmail.com&forum_name=matplotlib-users).


---

Attachment

Rebased.  Applies cleanly to Sage 4.6.2.


---

Comment by ryan created at 2011-04-16 05:17:57

Rebased for Sage 4.6.2 so it applies cleanly.  Hopefully this helps with further testing.


---

Comment by kcrisman created at 2011-04-17 00:05:57

If I recall correctly, the only issue was this image versus background thing, and the mpl devels in the thread above didn't have much to say that was helpful.  If things look okay with this, maybe fixing whatever is left could be another ticket.  It's sort of said we don't have this merged yet.


---

Comment by kcrisman created at 2013-01-29 20:55:19

Well, Jason, what do you think?  I wonder if mpl has new ways of designating these things now... anyway, just pinging about the status of this.
