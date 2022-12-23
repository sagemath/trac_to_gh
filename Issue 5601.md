# Issue 5601: predefine colors in Sage

Issue created by migration from https://trac.sagemath.org/ticket/5601

Original creator: jason

Original creation time: 2009-03-24 21:26:24

Assignee: was

CC:  kcrisman robertwb wcauchois

See the end of http://groups.google.com/group/sage-support/browse_thread/thread/44971aa416574675


* predefining the colors recognized in strings as Color objects in the global namespace, i.e.,     

```
    "red"   : (1.0,0.0,0.0),
    "orange": (1.0,.5,0.0),
    "yellow": (1.0,1.0,0.0),
    "green" : (0.0,1.0,0.0),
    "blue"  : (0.0,0.0,1.0),
    "purple": (.5,0.0,1.0),
    "white" : (1.0,1.0,1.0),
    "black" : (0.0,0.0,0.0),
    "grey"  : (.5,.5,.5) 
```


* predefine a huge number of colors (all x11 or html color strings?), but stick them in the color
namespace, so they would be accessed like color.goldenrod


---

Comment by was created at 2009-03-25 04:35:01

Just for clarification, we do *NOT* want even red, orange, etc. all defined in the global namespace.  It would be OK for something like the following to work though:

```
 sage: plot(sin(x), (x,0,1), color = colors.red)
```


Morever, I definitely definitely do not see any advantage at all to predefining a huge number of colors (Jason suggests all HTML -- that's 16777216 different colors!).  Instead one should be able to easily make colors... like you can already do right now.

 -- William


---

Comment by mpatel created at 2009-11-14 09:00:19

Possibilities:

 * CSS3 / SVG colors [alphabetically](http://www.w3.org/TR/css3-color/#svg-color) or [by hue](http://en.wikipedia.org/wiki/Web_colors#X11_color_names) - About 110.
 * [X11 colors](http://en.wikipedia.org/wiki/X11_color_names) - About 500.
 * [Wikipedia's list](http://en.wikipedia.org/wiki/List_of_colors).

We can make these available as in the comment above.  In effect:

```
sage.plot.colors.colors['aliceblue'] = (240.0/255.0, 248.0/255.0, 255.0/255.0)
sage.plot.colors.aliceblue = Color(sage.plot.colors.colors['aliceblue'])
```


Should we define just the official CSS3 / SVG colors?  The X11 colors include four shades for about 75 colors (e.g., `goldenrod1`, `goldenrod2`, `goldenrod3`, and `goldenrod4`), as well as 100 shades of `gray`/`grey` (from black to white).  They may be convenient.  Or we could suggest using `.lighter()` and `.darker()` (cf. #5602).


---

Comment by jason created at 2009-11-14 14:54:32

I think just the CSS3 official colors should be sufficient.  Are the names the same for the intersection between CSS3 and X11 colors?  I like the idea of using .lighter and .darker.

We should also have several lists of colors (like the predefined cmaps in matplotlib) that go well together, so you can do

colors.winter[0]

colors.winter[1]

etc. for a nice set of colors that go well together.


---

Comment by jason created at 2009-11-14 14:56:48

See http://reference.wolfram.com/mathematica/guide/Colors.html for the predefined mma colors (not very many!) and http://reference.wolfram.com/mathematica/guide/ColorSchemes.html for the predefined color schemes.


---

Attachment

Add CSS3/SVG colors, lighter/darker methods, HSV and HSL/HLS constructors


---

Comment by mpatel created at 2009-11-18 04:41:35

The attached patch should add:

 * CSS3 / SVG colors - #5601.  Actually, this replaces the previous colors.
 * `Color.lighter` and `Color.darker` - #5602.
 * HSV and HSL/HLS `Color` constructors - #5605.

Predefined palette:

```python
import sage.plot.colors as cc
p = Graphics()
for i, color in enumerate(cc.colors.keys()):
    x = floor(i / 12) + 1
    y = i % 12 + x * 0.5 + 1
    p += point((x, y), pointsize=500, faceted=True, color=color)
    p += text(color, (x + 0.15, y), rgbcolor='black', fontsize=10, horizontal_alignment='left')
show(p, figsize=[25,10], ymin=0, xmax=14, ymax=19, axes=False)
```



---

Comment by mpatel created at 2009-11-18 04:41:35

Changing status from new to needs_review.


---

Comment by mpatel created at 2009-11-18 04:44:15

The patch should also address [comment:2:ticket:5605 this comment] at #5605.


---

Comment by mpatel created at 2009-11-18 05:19:42

Replying to [comment:3 jason]:
> I think just the CSS3 official colors should be sufficient.  Are the names the same for the intersection between CSS3 and X11 colors?

Almost.  See [this](http://en.wikipedia.org/wiki/X11_color_names#Color_names_that_clash_between_X11_and_HTML.2FCSS).

> We should also have several lists of colors (like the predefined cmaps in matplotlib) that go well together, so you can do
> 
> colors.winter[0]
> 
> colors.winter[1]
> 
> etc. for a nice set of colors that go well together.

Oops!  I haven't done this.  Which of matplotlib's [color maps](http://www.scipy.org/Cookbook/Matplotlib/Show_colormaps) should we use?


```python
from matplotlib import cm
summer = []
for i in xrange(cm.summer.N):
    summer.append(tuple(cm.summer(i)[0:3]))
```


`N = 256` for all of them.  Should we make our lists the same length?


---

Comment by jason created at 2009-11-18 06:34:12

Replying to [comment:8 mpatel]:
> 
> Almost.  See [this](http://en.wikipedia.org/wiki/X11_color_names#Color_names_that_clash_between_X11_and_HTML.2FCSS).

Interesting--I didn't know that HTML green was not #00FF00



> 
> > We should also have several lists of colors (like the predefined cmaps in matplotlib) that go well together, so you can do
> > 
> > colors.winter[0]
> > 
> > colors.winter[1]
> > 
> > etc. for a nice set of colors that go well together.
> 
> Oops!  I haven't done this.  Which of matplotlib's [color maps](http://www.scipy.org/Cookbook/Matplotlib/Show_colormaps) should we use?
> 
> {{{
> #!python
> from matplotlib import cm
> summer = []
> for i in xrange(cm.summer.N):
>     summer.append(tuple(cm.summer(i)[0:3]))
> }}}
> 
> `N = 256` for all of them.  Should we make our lists the same length?


How much do we want to invent/wrap things versus just using their classes directly?  Maybe we should just import their colormaps into our color namespace, so people just have to remember colors.winter, rather than having to import matplotlib?

A *really* cool thing we could do with the gradients, though, is somehow helping people pick gradients according to the criteria here:

http://colorbrewer2.org/

(note that lots of the matplotlib color maps came from that website).

Note that on that website, you can easily pick gradients that are color-blind safe, that are safe for photocopying, that are print-friendly, etc.  It would be really cool to have basically the functionality of that flash applet at a user's disposal in Sage.  So, for example:

colors.gradients(num_colors=5,color_blind=True,print_friendly=True)

would return a dictionary of gradients that satisfy the criteria (like clicking the boxes on that flash applet).  Additionally, we should incorporate the recommendations from the phd thesis studying the color-blind aspects of the schemes---see p. 87 of http://www.personal.psu.edu/cab38/ColorBrewer/Steve_Gardner_thesis_PSU.pdf


That said, what I describe above is probably work for another ticket (unless you want to take it on in this patch!)


---

Comment by mpatel created at 2009-11-18 09:08:46

Replying to [comment:9 jason]:
> That said, what I describe above is probably work for another ticket (unless you want to take it on in this patch!)

Version 2 adds the matplotlib colormaps.  Otherwise: Agreed!


---

Comment by mpatel created at 2009-11-18 09:10:30

Added matplotlib colormaps.  Apply only this patch.


---

Attachment

Sage colors.  Not a patch.


---

Attachment

<img src="sage_colors.png" width=900px>


---

Comment by robertwb created at 2009-11-20 05:42:37

In general, I like this change, especially being able to do stuff like define color lists and doing lighter/darker(). 

The big color list is verbose, and (at least for me) a bit hard to read. Maybe it would be easier to make a dict of their hex values, then run over the dict converting them?


---

Comment by robertwb created at 2009-11-20 05:53:02

Is there a way to do some of this lazily, e.g. not import matplotlib at startup?


---

Comment by mpatel created at 2009-11-20 10:20:45

Replying to [comment:14 robertwb]:
> Is there a way to do some of this lazily, e.g. not import matplotlib at startup? 
The following is ad hoc, but it appears to work.  I removed the global import and the code that sets up the module-scope colormaps.  To the _end_ of `sage.plot.colors` I added

```python
# matplotlib color maps, loaded on-demand.
class ColormapLoader(object):
    def __init__(self, globs):
        self.cm = None
        for key in globs:
            self.__setattr__(key, globs[key])

    def __getattr__(self, name):
        if name == '__path__':
            return __path__

        if not self.cm:
            print 'loading matplotlib.cm'
            from matplotlib import cm            
            self.cm = cm

        try:
            cmap = self.cm.__getattribute__(name)
        except AttributeError:
            raise AttributeError, 'no colormap with name %s' % name

        self.__setattr__(name, cmap)
        return cmap

colormaps = ColormapLoader(vars())

import sys
sys.modules['sage.plot.colors'] = colormaps
```



---

Comment by jason created at 2009-11-20 10:25:27

You can also look how we import numpy/scipy in matrix/matrix_double_dense.pyx:

At the top, we have:

numpy=None

when we need to use it, we have code like:

```
        global numpy
        if numpy is None:
            import numpy
```



---

Attachment

Start with HTML hex colors.  No change to colormap imports.  Apply only this patch.


---

Comment by mpatel created at 2009-11-20 14:41:07

The "ad hoc" example above adds module-scope colormaps on-the-fly, with or without the "numpy" simplification, but it appears to confuse the doctesting script.  If it's OK to make the maps accessible as `sage.plot.colors.colormaps.mapname` instead of `sage.plot.colors.mapname`, say, I can add a simple subclass of [collections.Mapping](http://docs.python.org/library/collections.html#abcs-abstract-base-classes) that lazily loads the maps as attributes of a `sage.plot.colors.colormaps` object.

On the other hand, importing just `matplotlib.cm` seems to be fast.  We could keep the current code.


---

Comment by mpatel created at 2009-11-22 00:03:57

I just noticed #7502, which could be relevant and useful here.


---

Comment by mpatel created at 2009-11-22 00:08:37

I should have entered 'kcrisman' in the "Cc" field.  Sorry about that!  Or, if you did not wish to be alerted, the correction...


---

Comment by mpatel created at 2009-11-22 03:41:06

From `sage.plot.colors.float_to_html`'s docstring:

```
This may not seem necessary, but there are some odd cases where matplotlib is just plain schizophrenic – for an example, do

sage: vertex_colors = {(1.0, 0.8571428571428571, 0.0): [4, 5, 6], (0.28571428571428559, 0.0, 1.0): [14, 15, 16], (1.0, 0.0, 0.0): [0, 1, 2, 3], (0.0, 0.57142857142857162, 1.0): [12, 13], (1.0, 0.0, 0.85714285714285676): [17, 18, 19], (0.0, 1.0, 0.57142857142857162): [10, 11], (0.28571428571428581, 1.0, 0.0): [7, 8, 9]}
sage: graphs.DodecahedralGraph().show(vertex_colors=vertex_colors)

Notice how the colors don’t respect the partition at all.....
```

Is this still true?  The example appears to work for me, but I could be misinterpreting it.


---

Attachment

Add to reference manual.  Defer loading of color maps.  Apply only this patch.


---

Comment by mpatel created at 2009-11-22 05:41:47

Version 4:

 * Tweaks some docstrings.
 * Adds `sage.plot.colors` to the reference manual.
 * Lazily loads matplotlib's colormaps into `sage.plot.colors.colormaps`.
 * Adds `colors` and `colormaps` to the objects imported in `sage.plot.all`.
 * Does not include the `float_to_html` example above.

Feel free to make or suggest changes!


---

Comment by kcrisman created at 2009-11-24 01:43:56

Sorry I won't be able to review this (travel) in the next little bit.  I do not actually think that the float_to_html thing is broken anymore, but I kept it when I refactored some of this stuff; as long as all the graph coloring and plot coloring things still work in the Sage library, it should be okay.  The more we do from mpl, the better, though.

I do like the pink/punk and grassmann things, that's a little fun but also shows the errors.  Otherwise it seems this keeps the previous behavior while adding good access to important stuff.  One thing I don't like is that the diff is very hard to read for some reason - it might be worth doing a options='--no-commit' and then recommit, just to see if it will be easier to compare new and old!  But that's fairly trivial.


---

Comment by mpatel created at 2009-11-24 08:01:28

Replying to [comment:22 kcrisman]:
> One thing I don't like is that the diff is very hard to read for some reason - [...]

This may stem from my changing the order of some definitions.


---

Comment by mpatel created at 2009-11-25 08:09:27

To do:

 * Make `colormaps.<TAB>` list the colormaps, too.
 * Make `colors.<TAB>` list the colors.


---

Attachment

Attribute access for colors and color maps.  Apply only this patch.


---

Comment by mpatel created at 2009-11-26 05:38:39

Replying to [comment:24 mpatel]:
> To do:
> 
>  * Make `colormaps.<TAB>` list the colormaps, too.
>  * Make `colors.<TAB>` list the colors.

Version 5 does both.


---

Comment by mpatel created at 2009-11-27 08:05:50

I just discovered [__add__ and friends](http://docs.python.org/reference/datamodel.html#emulating-numeric-types), so please wait on the review.


---

Attachment

[Scalar] add and multiply colors.  This patch only.


---

Comment by mpatel created at 2009-12-03 16:24:57

Version 6:

 * Makes it possible to scalar add and multiply Sage `Color`s (cf. #5604.).  The RGB coordinates are reduced modulo 1.0 after each operation --- watch the order!  The `scale` and `lighter` methods simply cap values at 1.0.  For the sake of clarity: Adding colors does not take the arithmetic mean of their corresponding components.

 * Uses Sage `Color`s, instead of 3-tuples, for the values in `sage.plot.colors.colors`.  This is for the sake of uniformity and seems to make sense.  Later, we could extend the class from RGB to RGBA.  I added `__iter__` and `__getitem__` methods, so that doctests under `plot/` pass, but please report any problems!

On primary, secondary, tertiary, and quaternary colors, see, e.g., [this](http://members.cox.net/sn3nut/color%20theory.htm), [this](http://en.wikipedia.org/wiki/Tertiary_color), or [this](http://books.google.com/books?id=oFmoFNx-pDwC&pg=PA24&lpg=PA24&dq=quaternary+color+tertiary&source=bl&ots=Dnu8NaVDAD&sig=O6AWEkn9FLnf6pLWKT1a96DhcFU&hl=en&ei=yuIXS5HTOIngsQPWya2ZDg&sa=X&oi=book_result&ct=result&resnum=4&ved=0CBAQ6AEwAw#v=onepage&q=quaternary%20color%20tertiary&f=false).


---

Comment by mpatel created at 2009-12-03 16:25:57

By the way, I definitely _won't_ try to roll #5603 into this ticket.


---

Comment by kcrisman created at 2009-12-10 14:21:20

Believe it or not, this _also_ takes care of ticket #5083, I think.  Truly a giant-slayer of a patch.


---

Comment by jason created at 2009-12-10 14:53:59

This is great stuff.

Some initial comments:

 # Lots of doctests are marked #random that shouldn't be (there should be no #random doctests).  Use ... to take care of memory addresses changing, and use sort(dict.items()) to take care of things like dictionaries.

 # .lighter() and .darker() seem to have too little contrast.  Can we make it so that they about double their steps?  In other words, can we make it so that .lighter() does what .lighter().lighter() does in this patch?

 # Interestingly, colors.white.darker() gives gray values, but colors.black.lighter() does not give gray values.

Of these the first is the real technical issue.  Other things are fine-tuning that can be put off to another patch.


---

Comment by jason created at 2009-12-10 14:57:26

Here's another issue:
`circle((0,0),radius=1,fill=True,facecolor=colors.white+colors.green)` produces a purple circle!


---

Comment by kcrisman created at 2009-12-10 18:25:10

I just looked at this too.  Overall, a great patch, and well documented and well thought out.  One quibble is whether it should be "An Red-Green-Blue" or "A"; I know it's "An RGB", but this seems awkward.  Is it necessary for ColorMaps to inherit from collections.whatever, also?

But the downside of such a patch is that all these things are together, so we can't give positive review to the good parts.  And adding colors and the lighter/darker do not function at all properly.  In addition to Jason's example, red+yellow=green, not orange, with this addition; further, you can't make red lighter (to, say, pink) and making it darker gives... brown.  

So  I think that all of those things should use HSV or HSL, and you can increase or decrease S or L as seems to work best for lighter/darker, and do a color-wheel addition of hues for addition.  This is a little tricky - because the color wheel has nontrivial fundamental group, you can't get a unique answer for adding orange and blue, say.  (There are some interesting psych experiments where subjects shown complementary colors in the two eyes see either a superimposition of the colors, or the colors switching back and forth.)  Oh, and what the heck does multiplying a color by a color mean?  I think that should be removed unless there is a natural interpretation; scalar mult only, please, and that can be the RGB mult.

Anyway, I think this is all doable, but it's a shame this would hold up the excellent refactoring and improvement of colors and colormaps.  Why not just remove the not properly working things, and keep their tickets open, but do the base stuff here?

And as for the random doctests... Jason, I think he marked them that way because the default colors and colormaps may change.  But probably that will just be something that should be fixed each time we upgrade matplotlib or something.


---

Comment by kcrisman created at 2009-12-10 18:25:10

Changing status from needs_review to needs_work.


---

Comment by jason created at 2009-12-10 18:30:21

Replying to [comment:33 kcrisman]:

> Anyway, I think this is all doable, but it's a shame this would hold up the excellent refactoring and improvement of colors and colormaps.  Why not just remove the not properly working things, and keep their tickets open, but do the base stuff here?

I agree.  Let's remove (or at least comment out) the addition stuff right now until we have a better grasp of what we want and how to get it.

I believe MMA just implements a Blend function, and then makes lighter and darker just blending with black or white, and it's also consistent with blending other colors.


> And as for the random doctests... Jason, I think he marked them that way because the default colors and colormaps may change.  But probably that will just be something that should be fixed each time we upgrade matplotlib or something.

I don't think the colormaps in matplotlib have been touched in a long time.  I wouldn't worry too much about having to fix things up very often.  And it's much better to fix it up than to have it not doctested by putting a #random there.


---

Comment by jason created at 2009-12-10 18:32:30

MMA Blend function: http://reference.wolfram.com/mathematica/ref/Blend.html


---

Comment by jason created at 2009-12-10 18:42:13

I think MMA just does a weighted average of colors.  In other words, for each component, color1.blend(color2,fraction) would create a new color (1-fraction)*color1+(fraction)*color2.

I thought color1+color2 would be color1.blend(color2,1/2)

MMA then has:

color.lighter() is just color.blend(colors.white,1/3)

color.darker() is just color.blend(colors.black,1/2)

I'm not quite sure what this patch does.


---

Comment by jason created at 2009-12-10 23:38:13

apply on top of previous patch; implements blending


---

Attachment

I attached a *rough* patch that implements the mma-style blending, lighter(), and darker().  What do you think?  I don't know that much about color theory, so I don't know what "should" happen, but now colors.yellow+colors.green gives yellowgreenish colors.


---

Comment by jason created at 2009-12-11 00:05:26

According to http://stackoverflow.com/questions/398224/how-to-mix-colors-naturally-with-c/398268#398268, we really want to work in Lab space to mix colors, because then linear changes become linear changes in perception (i.e., Lab is designed so that it is easy to change the perception by a certain amount).

Also, here's some results using alpha values: http://stackoverflow.com/questions/726549/algorithm-for-additive-color-mixing-for-rgb-values

For lightening or darkening, some suggestions here are to convert to hsl or hsv and modify the correct component: http://stackoverflow.com/questions/97646/how-do-i-determine-darker-or-lighter-color-variant-of-a-given-color

So, as always, it is not as easy as it appears at all.  However, it looks like it might be easy to convert to hsl or hsv for the darker/lighter commands pretty easily, especially since we already have functions to do that.


---

Comment by robertwb created at 2009-12-11 00:47:10

+1 to working in non-RGB space for color mixing. 

Also, it might be nice if lighter() and darker() take an optional parameter, so c.lighter(3) would be the same as c.ligher().lighter().lighter()


---

Comment by jason created at 2009-12-11 01:04:22

Good point.  In the mma model (and my patch), c.lighter() is just c.blend(white,1/3).  c.lighter(k) is just c.blend(white,k), so c.lighter(0) is c, and c.lighter(1) is white.  I can see where your idea would be very useful too, though.  We ought to make lighter/darker take the fraction as a keyword argument, though, and make the number of times the first positional argument:

def lighter(self, times=1, fraction=1.0/3.0):
    fraction=float(fraction)
    c = self
    for i in range(times):
        c = c.blend((1.0, 1.0, 1.0), fraction)
    return c

(that is, if we decide to go with the blending patch for now)


---

Comment by jason created at 2009-12-11 01:05:06

Of course:

```
def lighter(self, times=1, fraction=1.0/3.0):
    fraction=float(fraction) 
    c = self 
    for i in range(times):
        c = c.blend((1.0, 1.0, 1.0), fraction)
    return c
```



---

Comment by mpatel created at 2009-12-11 11:11:31

On lighter/darker: V6 just scalar multiplied the RGB coordinates, which I think is equivalent to scaling L in HSL or V in HSV.  For scaling up from black, in this approach, I should have returned some grey.  But interpolation looks good to me!

Anyway, I apologize for the mess, especially for claiming to cover #5604.  Thanks for the feedback and corrections!


---

Attachment

Doctest fixes.  Combined patch rebased vs. 4.3.3.alpha1.  Apply only this patch.


---

Comment by mpatel created at 2010-02-22 01:01:05

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2010-02-22 01:01:05

I've attached V7, which is V6 + Jason Grout's "blending" patch + doctest / docstring fixes.

Please review, experiment, blend, plot, test, etc., and let me know if there are problems!

I've added Bill Cauchois to the Cc: list, since I've updated some tests in `sage.plot.plot3d.base` (cf. #7985, #8235).


---

Comment by mpatel created at 2010-02-22 01:01:37

Replying to [comment:43 mpatel]:
> Please review, experiment, blend, plot, test, etc., and let me know if there are problems!
Or fix them. :)


---

Attachment

Fix `interact` doctest.  *sagenb* repo.


---

Comment by jason created at 2010-02-27 20:58:26

Changing status from needs_review to positive_review.


---

Comment by jason created at 2010-02-27 20:58:26

I've looked at this pretty carefully before.  The examples I give above seem to work.  I presume that your incorporation of my blending patch is a positive review of that part.  All doctests pass in plot/* and plot/plot3d/*.  I also played around with it a bit more and it seems like everything is very nicely done.  So positive review!


---

Comment by mvngu created at 2010-03-03 14:13:29

Merged [trac_5601-builtin_colors_v7.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/5601/trac_5601-builtin_colors_v7.patch) in the Sage library. I leave it to the SageNB project manager to merge [trac_5601-sagenb_doctest.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/5601/trac_5601-sagenb_doctest.patch) into the SageNB repository. After doing so, the said manager could close this ticket as fixed.


---

Comment by jhpalmieri created at 2010-03-03 22:29:05

Note: merging trac_5601-sagenb_doctest.patch should fix one of the doctest failures listed at #8430.


---

Comment by mpatel created at 2010-03-04 22:35:45

I'm merging [attachment:trac_5601-sagenb_doctest.patch] into SageNB 0.7.5.2.  See #8435.


---

Comment by mpatel created at 2010-03-04 22:50:24

What should we do about #5602, #5603, #5604, and #5605?  Close them and open new tickets for the ideas mentioned above?


---

Comment by mpatel created at 2010-03-06 15:50:53

Resolution: fixed


---

Comment by drkirkby created at 2010-03-08 02:28:02

Unless I am mistaken, the release manager should close this, and mark the resolution as 'fixed'. Since this is not merged yet, it looks to me that this might get overlooked if you are not careful. 

Dave
