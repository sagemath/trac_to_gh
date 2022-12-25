# Issue 8164: automatic rainbow coloring of multiple plot lines

archive/issues_008164.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  wcauchois @kcrisman @alauve @paulmasson\n\nRight now, `plot([x,x^2,log(x)], (x,0,1), fill=True)` does a great job of selecting different colors for the fills.  It would be fantastic if `plot([x,x^2,log(x)], (x,0,1))` also picked a different color for each of the lines.\n\nIt would also be nice if `plot([x,x^2,log(x)], (x,0,1), color=<list of colors>)` worked well, just cycling through the list for each plot.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8164\n\n",
    "created_at": "2010-02-03T05:28:45Z",
    "labels": [
        "component: graphics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "automatic rainbow coloring of multiple plot lines",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8164",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

CC:  wcauchois @kcrisman @alauve @paulmasson

Right now, `plot([x,x^2,log(x)], (x,0,1), fill=True)` does a great job of selecting different colors for the fills.  It would be fantastic if `plot([x,x^2,log(x)], (x,0,1))` also picked a different color for each of the lines.

It would also be nice if `plot([x,x^2,log(x)], (x,0,1), color=<list of colors>)` worked well, just cycling through the list for each plot.

Issue created by migration from https://trac.sagemath.org/ticket/8164





---

archive/issue_comments_071701.json:
```json
{
    "body": "I strongly disagree.   The default should be monochromatic - maybe even black, but we haven't done that, so stick with blue for now.   But the multiple colors can be very distracting, and also difficult for some people to see.\n\nHowever, I *do* agree that it should be super-easy to do what you suggest.  Maybe even 'colors=True' or something like that.",
    "created_at": "2010-02-03T15:37:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8164#issuecomment-71701",
    "user": "https://github.com/kcrisman"
}
```

I strongly disagree.   The default should be monochromatic - maybe even black, but we haven't done that, so stick with blue for now.   But the multiple colors can be very distracting, and also difficult for some people to see.

However, I *do* agree that it should be super-easy to do what you suggest.  Maybe even 'colors=True' or something like that.



---

archive/issue_comments_071702.json:
```json
{
    "body": "I'd love to hear why you have that preference.\n\nWe can just extend `plot([x,x^2,log(x)], (x,0,1), color=<list of colors>)` to do something like `plot([x,x^2,log(x)], (x,0,1), color=colors.rainbow(3))`, or even `plot([x,x^2,log(x)], (x,0,1), color=colors.rainbow)`.",
    "created_at": "2010-02-03T18:33:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8164#issuecomment-71702",
    "user": "https://github.com/jasongrout"
}
```

I'd love to hear why you have that preference.

We can just extend `plot([x,x^2,log(x)], (x,0,1), color=<list of colors>)` to do something like `plot([x,x^2,log(x)], (x,0,1), color=colors.rainbow(3))`, or even `plot([x,x^2,log(x)], (x,0,1), color=colors.rainbow)`.



---

archive/issue_comments_071703.json:
```json
{
    "body": "From [this sage-support thread](http://groups.google.com/group/sage-support/browse_thread/thread/797289bc476b089a):\n\n```\n\n> >> Try something like:\n> \n> >> colors=rainbow(len([0,1,..3]))\n> >> sum(plot(derivative((f(x), a) , (x,0,2*pi), color =\n> >> colors[i],label=\"Plot %d\"%i) for i,a in enumerate([0,1,..3]))\n> \n> >> Make each curve an individual plot, and then sum them together.\n> \n> > Though for years I've wanted to do\n> \n> > plot([f,g,h],(x,0,1),color=['red','blue','green'])\n> \n> > Don't know how hard it would be to send color to list and check if it\n> > had the right length... \u00a0probably not?\n> \n> Almost surely it's not hard. \u00a0My guess is that it would involve maybe\n> one or two lines of code change, right at the start where it detects if\n> you have multiple functions and calls plot for each function.\n> \n> That's around line 3216 of plot/plot.py, right after this comment:\n> \n> \u00a0 \u00a0 \u00a0#check to see if funcs is a list of functions that will\n> \u00a0 \u00a0 \u00a0#be all plotted together.\n> \n```",
    "created_at": "2011-10-28T17:57:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8164#issuecomment-71703",
    "user": "https://github.com/kcrisman"
}
```

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

archive/issue_comments_071704.json:
```json
{
    "body": "Also, #6894 turned out to be a dup.\n\n```\nExample: plot([lambda x: x,lambda x: -x], (-5,5)) should plot x->x and x->-x in two different colors.\n```",
    "created_at": "2011-10-28T17:58:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8164#issuecomment-71704",
    "user": "https://github.com/kcrisman"
}
```

Also, #6894 turned out to be a dup.

```
Example: plot([lambda x: x,lambda x: -x], (-5,5)) should plot x->x and x->-x in two different colors.
```



---

archive/issue_comments_071705.json:
```json
{
    "body": "I actually think that auto-rainbow is cool. It should be very easy to get monochromatic and in particular black-and-white plots, e.g. for inclusion into stuff that will be printed in B&W, but as a default during interactive work I think it would be nice to automatically have different colors and legend.\n\nRegarding difficulty of seeing - perhaps it should not be just rainbow but, say, 50% rainbow plus 50% black, so that all colors remain high-contrast with background. I used plain rainbows a couple weeks ago (https://sage.math.ualberta.ca:8073/home/pub/5/) and I think that green does not look that great, especially when using a projector.\n\nMaybe it would be a good idea also to make the legend background lighter by default. Maybe even white to match the usual background color of the plot itself...",
    "created_at": "2011-11-21T04:15:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8164#issuecomment-71705",
    "user": "https://github.com/novoselt"
}
```

I actually think that auto-rainbow is cool. It should be very easy to get monochromatic and in particular black-and-white plots, e.g. for inclusion into stuff that will be printed in B&W, but as a default during interactive work I think it would be nice to automatically have different colors and legend.

Regarding difficulty of seeing - perhaps it should not be just rainbow but, say, 50% rainbow plus 50% black, so that all colors remain high-contrast with background. I used plain rainbows a couple weeks ago (https://sage.math.ualberta.ca:8073/home/pub/5/) and I think that green does not look that great, especially when using a projector.

Maybe it would be a good idea also to make the legend background lighter by default. Maybe even white to match the usual background color of the plot itself...



---

archive/issue_comments_071706.json:
```json
{
    "body": "See http://sage.maa.org/home/pub/140/ for what we have to do now.  I still think that having all the same color is better for accessibility and non-confusion reasons, but it should be very easy, and of course having the list of colors (like `rainbow(5)`) would be very very good as pointed out in the description.",
    "created_at": "2012-07-11T00:50:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8164#issuecomment-71706",
    "user": "https://github.com/kcrisman"
}
```

See http://sage.maa.org/home/pub/140/ for what we have to do now.  I still think that having all the same color is better for accessibility and non-confusion reasons, but it should be very easy, and of course having the list of colors (like `rainbow(5)`) would be very very good as pointed out in the description.



---

archive/issue_events_019556.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8164#event-19556"
}
```



---

archive/issue_comments_071707.json:
```json
{
    "body": "Here's a very interesting article from HackerNews about choosing colors procedurally: http://devmag.org.za/2012/07/29/how-to-choose-colours-procedurally-algorithms/.  The Golden Ratio method looks particularly interesting.  See also http://martin.ankerl.com/2009/12/09/how-to-create-random-colors-programmatically/ and the HackerNews comment thread: https://news.ycombinator.com/item?id=6309989 (where someone mentions that Mathematica uses the GoldenRatio method too.)",
    "created_at": "2013-09-02T17:33:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8164#issuecomment-71707",
    "user": "https://github.com/jasongrout"
}
```

Here's a very interesting article from HackerNews about choosing colors procedurally: http://devmag.org.za/2012/07/29/how-to-choose-colours-procedurally-algorithms/.  The Golden Ratio method looks particularly interesting.  See also http://martin.ankerl.com/2009/12/09/how-to-create-random-colors-programmatically/ and the HackerNews comment thread: https://news.ycombinator.com/item?id=6309989 (where someone mentions that Mathematica uses the GoldenRatio method too.)



---

archive/issue_events_019557.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8164#event-19557"
}
```



---

archive/issue_events_019558.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8164#event-19558"
}
```



---

archive/issue_events_019559.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8164#event-19559"
}
```



---

archive/issue_events_019560.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8164#event-19560"
}
```



---

archive/issue_events_019561.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8164#event-19561"
}
```



---

archive/issue_events_019562.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8164#event-19562"
}
```



---

archive/issue_comments_071708.json:
```json
{
    "body": "It may turn out that this is part of #12962 but it would be nice to have some discussion of this.",
    "created_at": "2015-07-25T01:48:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8164#issuecomment-71708",
    "user": "https://github.com/kcrisman"
}
```

It may turn out that this is part of #12962 but it would be nice to have some discussion of this.



---

archive/issue_comments_071709.json:
```json
{
    "body": "My two cents, regarding making multi-color curves the default...\n\nPerhaps, \"Mathematica and Maple do it,\" is not a convincing enough argument for most (though I think it is), but what about, \"because that's what a novice user needs\"? Anyhow, this was the impetus for creating #12962, as I was not getting what I expected. I certainly wouldn't expect my (pre-)calculus student to figure out dictionaries and plot-addition to help them distinguish one function from the next.\n\nRegarding B&W readability, yes, this could be a problem with `rainbow()`... and I notice that Mathematica chooses very dark shades for their default colors. However, there is an additional problem with `rainbow()`: sometimes your second function would be plotted with cyan, sometimes your fourth function would be (depending on how many are plotted, in total). For a novice trying to learn the different behavior of assorted functions, this hardly seems like a good idea. \n\nRegarding alternatives to `rainbow()`, I really like the golden-ratio idea (and it solves my 'additional problem' above). We should start from 'blue' as this is Sage's preferred plot color. Try: \n\n```\nh = golden_ratio_conjugate = 0.618033988749895\ngraphics_array([circle((.2,.2),.5,facecolor=Color((.666666+i*h)%1,1,.45,space='hsl'),fill=True,edgecolor='white') for i in range(10)]).show(axes=False,figsize=7)\n```\nand notice that the first ten entries are identical to those here:\n\n```\nh = golden_ratio_conjugate = 0.618033988749895\ngraphics_array([circle((.2,.2),.5,facecolor=Color((.666666+i*h)%1,1,.45, space='hsl'),fill=True,edgecolor='white') for i in range(15)]).show(axes=False,figsize=10)\n```\n\nI've implemented the following function in #12962, in case anybody wants to pull that branch and have a look.\n\n```\ndef rainbow_color(i):\n    # note: 'blue' has hue-saturation-lightness values (2/3, 1, 1/2).\n    h = golden_ratio_conjugate = 0.618033988749895\n    return Color((0.666666666666+i*h) % 1, 1, 0.4, space='hsl')\n```",
    "created_at": "2015-07-25T04:15:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8164#issuecomment-71709",
    "user": "https://github.com/alauve"
}
```

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

archive/issue_comments_071710.json:
```json
{
    "body": "This website for [seaborn](http://stanford.edu/~mwaskom/software/seaborn/tutorial/color_palettes.html#palette-tutorial) has an interesting discourse on the color palette that should be chosen for visualization. We can take some hints from that.",
    "created_at": "2015-07-26T03:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8164#issuecomment-71710",
    "user": "https://github.com/ppurka"
}
```

This website for [seaborn](http://stanford.edu/~mwaskom/software/seaborn/tutorial/color_palettes.html#palette-tutorial) has an interesting discourse on the color palette that should be chosen for visualization. We can take some hints from that.



---

archive/issue_comments_071711.json:
```json
{
    "body": "The website [seaborn](http://stanford.edu/~mwaskom/software/seaborn/tutorial/color_palettes.html) suggests we use a \"qualitative\" color palette, so the [Preiss/Ankerl](http://martin.ankerl.com/2009/12/09/how-to-create-random-colors-programmatically/) idea of using the *golden ratio* is fine. (I actually prefer it to what seaborn does, as the latter would result in the first plot in a list of seven being colored differently than the first plot in a list of six.)\n\nDo we have access to seaborn in Sage? Its attempt to adjust for human perception of hue seems like a good idea. It draws \"hue polygons\" as a function of brightness, then intersects a given hue's ray with the polygon ([HUSL](http://www.husl-colors.org/)). (If not, one could port over Boronine's [python code](https://github.com/husl-colors/husl-python), on which seaborn is based.)\n\n**Proposed algorithm:**\n\n```\nstep 1: pick a hue using golden_ratio()\nstep 2: adjust hue using husl()\n```\n\nNote that brightness-level isn't mentioned in the algorithm. We should agree on a level to use, independent of hue. If I understand Boronine's discussion (and [HSL sliders demo](http://www.husl-colors.org/)) correctly, there is only one hue-polygon that contains the color 'blue' (brightness = 32.3).\n* We might choose brightness = 32.3, to respect Sage's default plot color. However, the hues along the boundary of the polygon are quite a bit darker than I'd like to see, e.g., \"960000\" for red, \"005900\" for green, and \"005555\" for cyan. \n* Setting brightness = 40.0 gives a pretty good approximation to 'blue' (\"3b3bff\") with more vibrant colors along the boundary of the polygon, e.g., \"c00000\" for red, \"006e00\" for green, and \"006a6a\" for cyan.",
    "created_at": "2015-07-27T19:45:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8164#issuecomment-71711",
    "user": "https://github.com/alauve"
}
```

The website [seaborn](http://stanford.edu/~mwaskom/software/seaborn/tutorial/color_palettes.html) suggests we use a "qualitative" color palette, so the [Preiss/Ankerl](http://martin.ankerl.com/2009/12/09/how-to-create-random-colors-programmatically/) idea of using the *golden ratio* is fine. (I actually prefer it to what seaborn does, as the latter would result in the first plot in a list of seven being colored differently than the first plot in a list of six.)

Do we have access to seaborn in Sage? Its attempt to adjust for human perception of hue seems like a good idea. It draws "hue polygons" as a function of brightness, then intersects a given hue's ray with the polygon ([HUSL](http://www.husl-colors.org/)). (If not, one could port over Boronine's [python code](https://github.com/husl-colors/husl-python), on which seaborn is based.)

**Proposed algorithm:**

```
step 1: pick a hue using golden_ratio()
step 2: adjust hue using husl()
```

Note that brightness-level isn't mentioned in the algorithm. We should agree on a level to use, independent of hue. If I understand Boronine's discussion (and [HSL sliders demo](http://www.husl-colors.org/)) correctly, there is only one hue-polygon that contains the color 'blue' (brightness = 32.3).
* We might choose brightness = 32.3, to respect Sage's default plot color. However, the hues along the boundary of the polygon are quite a bit darker than I'd like to see, e.g., "960000" for red, "005900" for green, and "005555" for cyan. 
* Setting brightness = 40.0 gives a pretty good approximation to 'blue' ("3b3bff") with more vibrant colors along the boundary of the polygon, e.g., "c00000" for red, "006e00" for green, and "006a6a" for cyan.



---

archive/issue_comments_071712.json:
```json
{
    "body": "I greatly like the idea of \"the i-th rainbow color\" without specifying the total number, it is indeed mighty inconvenient when all colors change on adding one more line to the plot...",
    "created_at": "2015-07-27T20:11:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8164#issuecomment-71712",
    "user": "https://github.com/novoselt"
}
```

I greatly like the idea of "the i-th rainbow color" without specifying the total number, it is indeed mighty inconvenient when all colors change on adding one more line to the plot...



---

archive/issue_comments_071713.json:
```json
{
    "body": "Close as duplicate when #12962 is completed",
    "created_at": "2016-07-17T02:05:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8164#issuecomment-71713",
    "user": "https://github.com/paulmasson"
}
```

Close as duplicate when #12962 is completed



---

archive/issue_comments_071714.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2016-07-17T02:05:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8164#issuecomment-71714",
    "user": "https://github.com/paulmasson"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_071715.json:
```json
{
    "body": "Changing status from needs_info to positive_review.",
    "created_at": "2016-08-12T20:17:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8164#issuecomment-71715",
    "user": "https://github.com/paulmasson"
}
```

Changing status from needs_info to positive_review.



---

archive/issue_events_019563.json:
```json
{
    "actor": "https://github.com/paulmasson",
    "created_at": "2016-08-12T20:17:08Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8164#event-19563"
}
```



---

archive/issue_events_019564.json:
```json
{
    "actor": "https://github.com/paulmasson",
    "created_at": "2016-08-12T20:17:08Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8164#event-19564"
}
```



---

archive/issue_comments_071716.json:
```json
{
    "body": "For future reference, it is better to have someone else set it to a positive review to make sure they agree it is a duplicate.",
    "created_at": "2016-08-12T22:48:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8164#issuecomment-71716",
    "user": "https://github.com/tscrim"
}
```

For future reference, it is better to have someone else set it to a positive review to make sure they agree it is a duplicate.



---

archive/issue_comments_071717.json:
```json
{
    "body": "Already had a second person, but a third is even better: #12962#comment:30",
    "created_at": "2016-08-12T23:10:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8164#issuecomment-71717",
    "user": "https://github.com/paulmasson"
}
```

Already had a second person, but a third is even better: #12962#comment:30



---

archive/issue_comments_071718.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2016-08-30T13:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8164#issuecomment-71718",
    "user": "https://github.com/embray"
}
```

Resolution: wontfix



---

archive/issue_events_019565.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2016-08-30T13:32:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8164#event-19565"
}
```



---

archive/issue_comments_071719.json:
```json
{
    "body": "Determined to be invalid/duplicate/wontfix (closing as \"wontfix\" as a catch-all resolution).",
    "created_at": "2016-08-30T13:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8164#issuecomment-71719",
    "user": "https://github.com/embray"
}
```

Determined to be invalid/duplicate/wontfix (closing as "wontfix" as a catch-all resolution).
