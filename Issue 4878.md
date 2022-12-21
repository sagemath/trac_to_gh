# Issue 4878: [with patch; needs review] Add a density_plot() function

Issue created by migration from Trac.

Original creator: abergeron

Original creation time: 2008-12-25 05:49:42

Assignee: abergeron

As was requested a long time ago (in september!), I did the density_plot() function.

I've added as copyright-holders all the copyright-holders from contour_plot since over 80% of density_plot file is copy and paste from that.




---

Attachment

Applies to 3.2.2 cleanly and passes sage -t. The docstrings look fine.

I tried

```
sage: density_plot(sin(x^2 + y^2)*cos(x)*sin(y), (-4, 4), (-4, 4), cmap='winter', plot_points=100)

sage: contour_plot(sin(x^2 + y^2)*cos(x)*sin(y), (-4, 4), (-4, 4), cmap='winter', plot_points=100, contours=40)
```

and noticed that they look very similar (modulo scaling). However, there are some plotting artifacts contour_plot leaves at the "corners" where cos(x)=0 and sin(y)=0. density_plot seems to avoid these problems. Nice patch.

BTW, where can one find the list of "legal" values of cmap? For example, _allowed_options gives this:


```
    cmap           The colormap, one of (autumn, bone, cool, copper,
                       gray, hot, hsv, jet, pink, prism, spring, summer, winter)
```


But this is incomplete, since Oranges, Blues, etc also work. For example, try


```
sage: x,y = var('x,y')
sage: density_plot(sin(x^2 + y^2)*exp((x^2+y^2)/10), (-4, 4), (-4, 4), cmap='Greens')
```

I'm happy giving this a positive review but am wondering about this one small issue with the output of _allowed_options. Can the author please comment on this?


---

Attachment

Fix some problems with original patch, incremental


---

Comment by abergeron created at 2008-12-27 23:21:24

Changing status from new to assigned.


---

Comment by abergeron created at 2008-12-27 23:21:24

The thing about cmap options is that every time we update matplotlib new colormap names become available.  The docstrings are just a fixed list and we do not update them every time we update matplotlib.

I've just opened a ticket at #4884 to fix colormap handling that includes a fix for this issue and another patch that uses the new function to do the cmap handling.

This means that this ticket depends on #4884 now.

I've also fixed a couple of small problems with the code and docs.


---

Comment by was created at 2008-12-29 06:15:46

> The thing about cmap options is that every time we update matplotlib 
> new colormap names become available. The docstrings are just a fixed 
> list and we do not update them every time we update matplotlib. 

At a bare minimum, the docstring should explain precisely what one needs to type to get a list of all valid colormaps.  This could be included in a docstring, so that when matplotlib changes the colormap options, the docstring will suddenly break, and we will know to fix it.

Incidentally, right now one way to get a list of valid colormaps is to just make a mistake with the cmap option, and a list of all valid options is displayed.

```
sage: var('x,y')
sage: z = contour_plot(cos(x^2+y^2), (-4, 4), (-4, 4),cmap='foobar')  
sage: z.save('a.png')                                               
```

verbose 0 (63: contour_plot.py, _render_on_subplot) The possible color maps include: Spectral, summer, pink_r, Set1, Set2, Set3, Dark2, prism, PuOr_r, PuBuGn_r, RdPu, gist_ncar_r, Dark2_r, YlGnBu, RdYlBu, hot_r, gist_rainbow_r, gist_stern, cool_r, cool, gray, copper_r, Greens_r, GnBu, gist_ncar, spring_r, gist_rainbow, gist_heat_r, summer_r, OrRd_r, bone, gist_stern_r, RdYlGn, Pastel2_r, spring, Accent, YlOrRd_r, Set2_r, PuBu, RdGy_r, spectral, flag_r, jet_r, RdPu_r, gist_yarg, BuGn, Paired_r, hsv_r, YlOrRd, Greens, PRGn, gist_heat, spectral_r, Paired, hsv, Oranges_r, prism_r, Pastel2, Pastel1_r, Pastel1, gray_r, PuRd_r, Spectral_r, BuPu, YlGnBu_r, copper, gist_earth_r, Set3_r, OrRd, PuBu_r, winter_r, RdBu, jet, bone_r, gist_earth, Oranges, RdYlGn_r, PiYG, YlGn, binary_r, gist_gray_r, gist_gray, flag, RdBu_r, BrBG, Reds, GnBu_r, BrBG_r, Reds_r, RdGy, PuRd, Accent_r, Blues, Greys, autumn, PRGn_r, Greys_r, pink, binary, winter, gist_yarg_r, RdYlBu_r, hot, YlOrBr, BuPu_r, Purples_r, PiYG_r, YlGn_r, Blues_r, YlOrBr_r, Purples, autumn_r, BuGn_r, Set1_r, PuOr, PuBuGn
}}}


---

Comment by abergeron created at 2008-12-29 06:38:51

I am not sure what you mean with this comment.

The proposed patch add a mention to the docstring saying that you have to type cmap_help() to get detailed info on colormaps.  This function contains a list of all defined colormaps in the installed matplotlib version.  The list is automatically fetched just like the current error code for cmap does right now.

Is this what you want?  If not, what do you want?


---

Comment by wdj created at 2008-12-29 11:52:14

Arnaud: I think you have addressed William's complaint in your second patch. (I was basically arguing the same thing, though maybe not so clearly.) You describe cmap as one of the options to density_plot and "Type "cmap_hlp() for more information". The patch 4884 (which has a positive review) impliments that.

With the second patch, I think this is an excellent addition. Both patches to be applied together with that in #4884.

Positive review. Thanks Arnaud!


---

Comment by abergeron created at 2008-12-29 20:45:50

Since there is heavy discussion at #4884, I will wait until that settles before updating the patch here to conform with whatever interface (and documentation) will be decided upon.


---

Comment by abergeron created at 2008-12-30 01:52:19

#4884 is settled.  Since there is no change of interface, back to positive.


---

Comment by mabshoff created at 2009-01-12 01:54:27

Merged both patches in Sage 3.3.alpha0


---

Comment by mabshoff created at 2009-01-12 01:54:27

Resolution: fixed


---

Comment by mvngu created at 2009-02-07 04:10:00

Is it possible for someone to attach an image or two to this ticket? I'm looking for an image of a plot resulting from using the function `density_plot()`. What I have in mind is something along the line of the images attached to #2770 and #4976. Such images should serve as a high-level summary of what a (new) plotting function can do. And having such images mean that they can be referred to from a release tour note on the Sage wiki. I don't always have the latest alpha on my work machine, only the latest stable version.


---

Attachment

example image for mvngu


---

Comment by mvngu created at 2009-02-20 04:44:46

Thanks, Arnaud, for attaching that sample image. Just out of curiosity, what code did you use to produce that plot?


---

Attachment

another sample plot in black and white


---

Comment by mvngu created at 2009-02-20 04:52:23

The image `trac_4878-sample-plot-bw.png` is another sample plot showcasing the new function `density_plot()`. The image is in gray scale.


---

Comment by mabshoff created at 2009-02-20 05:39:52

Hi Minh,

any reason you don't want to attach those snapshots to a wiki page directly? It doesn't matter too much, but that is what we do for all the interact examples, too and that way it would be all on one host.

Cheers,

Michael


---

Comment by abergeron created at 2009-02-20 07:07:07

`@`mvngu:

This code: 


```
sage: density_plot(sin(x^2 + y^2)*cos(x)*sin(y), (-4, 4), (-4, 4), cmap='jet', plot_points=100)
```


from the examples.


---

Comment by mvngu created at 2009-02-23 04:41:34

Replying to [comment:12 mabshoff]:
> Hi Minh,
> 
> any reason you don't want to attach those snapshots to a wiki page directly? 
> It doesn't matter too much, but that is what we do for all the interact examples, 
> too and that way it would be all on one host.
Previously, I didn't know how to attach a file to a wiki page. But don't worry, I sort of know it now. The images I referred to are now attached to the release tour wiki.


---

Comment by mvngu created at 2009-02-23 04:43:01

Replying to [comment:13 abergeron]:
> `@`mvngu:
> 
> This code: 
> 
> {{{
> sage: density_plot(sin(x^2 + y^2)*cos(x)*sin(y), (-4, 4), (-4, 4), cmap='jet', plot_points=100)
> }}}
> 
> from the examples.
Greatly appreciated, Arnaud. And the plot looks damn cool :-)
