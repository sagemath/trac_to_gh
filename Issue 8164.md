# Issue 8164: automatic rainbow coloring of multiple plot lines

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-02-03 05:28:45

Assignee: was

CC:  wcauchois kcrisman alauve paulmasson

Right now, `plot([x,x^2,log(x)], (x,0,1), fill=True)` does a great job of selecting different colors for the fills.  It would be fantastic if `plot([x,x^2,log(x)], (x,0,1))` also picked a different color for each of the lines.

It would also be nice if `plot([x,x^2,log(x)], (x,0,1), color=<list of colors>)` worked well, just cycling through the list for each plot.


---

Comment by kcrisman created at 2010-02-03 15:37:00

I strongly disagree.   The default should be monochromatic - maybe even black, but we haven't done that, so stick with blue for now.   But the multiple colors can be very distracting, and also difficult for some people to see.

However, I _do_ agree that it should be super-easy to do what you suggest.  Maybe even 'colors=True' or something like that.


---

Comment by jason created at 2010-02-03 18:33:28

I'd love to hear why you have that preference.

We can just extend `plot([x,x^2,log(x)], (x,0,1), color=<list of colors>)` to do something like `plot([x,x^2,log(x)], (x,0,1), color=colors.rainbow(3))`, or even `plot([x,x^2,log(x)], (x,0,1), color=colors.rainbow)`.


---

Comment by kcrisman created at 2011-10-28 17:57:30

From [this sage-support thread](http://groups.google.com/group/sage-support/browse_thread/thread/797289bc476b089a):

```

> >> Try something like:
> 
> >> colors=rainbow(len([0,1,..3]))
> >> sum(plot(derivative((f(x), a) , (x,0,2*pi), color =
> >> colors[i],label="Plot %d"%i) for i,a in enumerate([0,1,..3]))
> 
> >> Make each curve an individual plot, and then sum them together.
> 
> > Though for years I've wanted to do
> 
> > plot([f,g,h],(x,0,1),color=['red','blue','green'])
> 
> > Don't know how hard it would be to send color to list and check if it
> > had the right length...  probably not?
> 
> Almost surely it's not hard.  My guess is that it would involve maybe
> one or two lines of code change, right at the start where it detects if
> you have multiple functions and calls plot for each function.
> 
> That's around line 3216 of plot/plot.py, right after this comment:
> 
>      #check to see if funcs is a list of functions that will
>      #be all plotted together.
> 
```



---

Comment by kcrisman created at 2011-10-28 17:58:37

Also, #6894 turned out to be a dup.

```
Example: plot([lambda x: x,lambda x: -x], (-5,5)) should plot x->x and x->-x in two different colors.
```



---

Comment by novoselt created at 2011-11-21 04:15:00

I actually think that auto-rainbow is cool. It should be very easy to get monochromatic and in particular black-and-white plots, e.g. for inclusion into stuff that will be printed in B&W, but as a default during interactive work I think it would be nice to automatically have different colors and legend.

Regarding difficulty of seeing - perhaps it should not be just rainbow but, say, 50% rainbow plus 50% black, so that all colors remain high-contrast with background. I used plain rainbows a couple weeks ago (https://sage.math.ualberta.ca:8073/home/pub/5/) and I think that green does not look that great, especially when using a projector.

Maybe it would be a good idea also to make the legend background lighter by default. Maybe even white to match the usual background color of the plot itself...


---

Comment by kcrisman created at 2012-07-11 00:50:40

See http://sage.maa.org/home/pub/140/ for what we have to do now.  I still think that having all the same color is better for accessibility and non-confusion reasons, but it should be very easy, and of course having the list of colors (like `rainbow(5)`) would be very very good as pointed out in the description.


---

Comment by jason created at 2013-09-02 17:33:52

Here's a very interesting article from HackerNews about choosing colors procedurally: http://devmag.org.za/2012/07/29/how-to-choose-colours-procedurally-algorithms/.  The Golden Ratio method looks particularly interesting.  See also http://martin.ankerl.com/2009/12/09/how-to-create-random-colors-programmatically/ and the HackerNews comment thread: https://news.ycombinator.com/item?id=6309989 (where someone mentions that Mathematica uses the GoldenRatio method too.)


---

Comment by kcrisman created at 2015-07-25 01:48:50

It may turn out that this is part of #12962 but it would be nice to have some discussion of this.


---

Comment by alauve created at 2015-07-25 04:15:01

My two cents, regarding making multi-color curves the default...

Perhaps, "Mathematica and Maple do it," is not a convincing enough argument for most (though I think it is), but what about, "because that's what a novice user needs"? Anyhow, this was the impetus for creating #12962, as I was not getting what I expected. I certainly wouldn't expect my (pre-)calculus student to figure out dictionaries and plot-addition to help them distinguish one function from the next.

Regarding B&W readability, yes, this could be a problem with `rainbow()`... and I notice that Mathematica chooses very dark shades for their default colors. However, there is an additional problem with `rainbow()`: sometimes your second function would be plotted with cyan, sometimes your fourth function would be (depending on how many are plotted, in total). For a novice trying to learn the different behavior of assorted functions, this hardly seems like a good idea. 

Regarding alternatives to `rainbow()`, I really like the golden-ratio idea (and it solves my 'additional problem' above). We should start from 'blue' as this is Sage's preferred plot color. Try: 

```
h = golden_ratio_conjugate = 0.618033988749895
graphics_array([circle((.2,.2),.5,facecolor=Color((.666666+i*h)%1,1,.45,space='hsl'),fill=True,edgecolor='white') for i in range(10)]).show(axes=False,figsize=7)
```

and notice that the first ten entries are identical to those here:

```
h = golden_ratio_conjugate = 0.618033988749895
graphics_array([circle((.2,.2),.5,facecolor=Color((.666666+i*h)%1,1,.45, space='hsl'),fill=True,edgecolor='white') for i in range(15)]).show(axes=False,figsize=10)
```


I've implemented the following function in #12962, in case anybody wants to pull that branch and have a look.

```
def rainbow_color(i):
    # note: 'blue' has hue-saturation-lightness values (2/3, 1, 1/2).
    h = golden_ratio_conjugate = 0.618033988749895
    return Color((0.666666666666+i*h) % 1, 1, 0.4, space='hsl')
```



---

Comment by ppurka created at 2015-07-26 03:00:45

This website for [seaborn](http://stanford.edu/~mwaskom/software/seaborn/tutorial/color_palettes.html#palette-tutorial) has an interesting discourse on the color palette that should be chosen for visualization. We can take some hints from that.


---

Comment by alauve created at 2015-07-27 19:45:41

The website [seaborn](http://stanford.edu/~mwaskom/software/seaborn/tutorial/color_palettes.html) suggests we use a "qualitative" color palette, so the [Preiss/Ankerl](http://martin.ankerl.com/2009/12/09/how-to-create-random-colors-programmatically/) idea of using the _golden ratio_ is fine. (I actually prefer it to what seaborn does, as the latter would result in the first plot in a list of seven being colored differently than the first plot in a list of six.)

Do we have access to seaborn in Sage? Its attempt to adjust for human perception of hue seems like a good idea. It draws "hue polygons" as a function of brightness, then intersects a given hue's ray with the polygon ([HUSL](http://www.husl-colors.org/)). (If not, one could port over Boronine's [python code](https://github.com/husl-colors/husl-python), on which seaborn is based.)

*Proposed algorithm:*

```
step 1: pick a hue using golden_ratio()
step 2: adjust hue using husl()
```


Note that brightness-level isn't mentioned in the algorithm. We should agree on a level to use, independent of hue. If I understand Boronine's discussion (and [HSL sliders demo](http://www.husl-colors.org/)) correctly, there is only one hue-polygon that contains the color 'blue' (brightness = 32.3).
 * We might choose brightness = 32.3, to respect Sage's default plot color. However, the hues along the boundary of the polygon are quite a bit darker than I'd like to see, e.g., "960000" for red, "005900" for green, and "005555" for cyan. 
 * Setting brightness = 40.0 gives a pretty good approximation to 'blue' ("3b3bff") with more vibrant colors along the boundary of the polygon, e.g., "c00000" for red, "006e00" for green, and "006a6a" for cyan.


---

Comment by novoselt created at 2015-07-27 20:11:30

I greatly like the idea of "the i-th rainbow color" without specifying the total number, it is indeed mighty inconvenient when all colors change on adding one more line to the plot...


---

Comment by paulmasson created at 2016-07-17 02:05:36

Close as duplicate when #12962 is completed


---

Comment by paulmasson created at 2016-07-17 02:05:36

Changing status from new to needs_info.


---

Comment by paulmasson created at 2016-08-12 20:17:08

Changing status from needs_info to positive_review.


---

Comment by tscrim created at 2016-08-12 22:48:17

For future reference, it is better to have someone else set it to a positive review to make sure they agree it is a duplicate.


---

Comment by paulmasson created at 2016-08-12 23:10:11

Already had a second person, but a third is even better: #12962#comment:30


---

Comment by embray created at 2016-08-30 13:32:25

Resolution: wontfix


---

Comment by embray created at 2016-08-30 13:32:25

Determined to be invalid/duplicate/wontfix (closing as "wontfix" as a catch-all resolution).
