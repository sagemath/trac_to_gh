# Issue 9664: Graphical representation of fans

Issue created by migration from https://trac.sagemath.org/ticket/9664

Original creator: vbraun

Original creation time: 2010-08-01 20:15:07

Assignee: mhampton

CC:  novoselt

There should be some graphical representation of rational polyhedral fans in low dimensions.


---

Comment by novoselt created at 2010-09-10 03:08:25

I like how the output looks, but I was designing a more flexible system (making all objects plottable, preferably both for 2d and 3d cases, with uniform parameter handling and easy way to adjust default parameters). Do you mind if I make another patch for this ticket using some of your code?


---

Comment by novoselt created at 2010-09-10 03:08:25

Changing status from new to needs_info.


---

Comment by vbraun created at 2010-09-10 08:54:54

I already had a working implementation of 3d plots, so let me attach my improved patch. I also changed the name `graph` to `plot` since otherwise a user might expect some graph-theoretic output. My working plan was to write 2d and 3d cases separately, and once we are happy with the output we can try to merge the functions. Although similar, there are often minor variations to make it look good, and there is a danger that your code ends up riddled with if/then clauses.


---

Comment by vbraun created at 2010-09-10 08:54:54

Changing status from needs_info to needs_work.


---

Comment by vbraun created at 2010-09-10 08:55:10

graphics for 2-d fans


---

Attachment

Hi Volker! So, here is my plan/proposal:
 1. Make all "toric objects" plottable in a consistent way with options trickling down from complicated objects to simpler ones.
 1. Gather all these options in a single file, say `sage.geometry.toric_plot` and use this module to store default options with users being able to see all options, change them globally and reset to originals. The same options also can be passed to each individual object.
 1. It is totally fine to have different internal functions for 2d and 3d plots, but when possible options should have the same name/meaning.
 1. I like your round 2-d fans, but I think there should be 3 ways to plot fans (and other things): in the disk of given radius, in the box with given sides (i.e. xyz-dimensions), and in the polytope determined by rays, i.e. rays are drawn to primitive generators, and cones are drawn between primitive generators. Reason - I think that round plots are pretty (so people should use them and I propose this as default), boxed plots are common (so people may want to use them despite of round ones being prettier), and "generator plot" seems to be very natural from the point of view of CPR-Fano toric varieties and I think this should be the default for them.
 1. I think that rays should be a little longer than cones, so that arrows "stick out", and the length of these rays does not have to correlate with primitive generators (but it would be nice to mark the generators with red dots, or some other way to clearly distinguish them from other lattice points).
 1. What is the purpose of white strips surrounding rays in your functions? (I agree that it looks pretty ;-))

Here are the options I think toric objects should have (each consequent one accepts parameters for previous ones):
 1. `ToricLatticeElement` (plots a point):
  * `point_color`
  * `point_size`
  * `point_label`
  * `point_label_shift` (so that it is not right on top of the point)
 1. `ToricLattice` (plots all points within the given region):
  * `plot_type` (one of "round", "box", "generators")
  * `radius` (for "round", can also be given for "box" as all six bounds)
  * `xyzmin/max` (six parameters)
 1. `IntegralRayCollection`:
  * `ray_color`
  * `ray_thickness`
  * `ray_extension` (how much longer should rays be compared to the size based on other parameters, to make "arrows sticking out")
  * `ray_label`
  * `ray_label_shift`
  * `generator_color` (for the lattice point corresponding to generator)
  * `generator_size`
  * `plot_lattice` (True/False to include lattice points or not)
 1. `Cone`
  * `cone_color`
  * `cone_alpha`
  * `cone_label`
  * maybe something to determine label position, but it seems that it can be position quite well between rays without necessity to shift it further
  * `plot_rays` (True/False)
  * `ray_label` can be given as a list of separate labels for each ray (just indexing them may be not very good, e.g. for toric varieties it may make sense to stick coordinate names next to rays)
 1. `Fan`
  * `plot_cones` (True/False)
  * `cone_label` can be given as a list of separate labels for each cone

In 3-d cases there may be some sense in being able to specify options differently for 2-d and 3-d cones, but that should be more clear in the process. Also, instead of drawing points corresponding to generators, maybe it is better to draw vectors, as in your implementation. But I still would like to see rays continuing "to infinity", i.e. beyond shaded regions for cones.

Thoughtscomments?


---

Comment by vbraun created at 2010-09-25 21:46:01

The reason for the white strips in the 2-d fan is that, otherwise, a complete fan is just a full disk. And I was too lazy to figure out the coordinates for the polyhedral region that is the "cake slice with some in the middle removed".

Just some thoughts:
  * I think its potentially confusing if the arrow is not ending at the generating lattice point. If you can't live without longer rays, how about having an arrow in the middle of the ray: `--->---`
  * `cone_label` already encompasses `ray_label`s.
  * The label positions should be chosen automatically in a reasonable way, no need for `_shift` options. You don't have to make everything configurable, if someone really, really wants to customize the heck out of the plot then he can take apart the returned graphics object.
  * In the 3-d case the `X.fan().plot() + X.Delta_polar().show3d()` combination basically gives you your type-III plot.

What would be really interesting is to have some visualization in the 4-d case, like a "orange peel" plot of the 3-d surface polyhedra with induced triangulation.


---

Comment by novoselt created at 2010-10-04 19:43:20

OK, here is my version, a little different from the above description but it is easier to look at plots and documentation than to explain it here. So I will just highlight some features.

Basically, the patch adds a "constructor" for toric plots and lattices/cones/fans set up this constructor and then call relevant commands. The hope is that one can easily use this constructor to create plots for some combinations, e.g. superimposed fan and its subdivision, split fan for fibrations and so on. As a simple example of modifying existing plots toric varieties replace default ray labels with coordinate names. (And old `plot3d` is finally gone from CPR-Fano varieties.)

Any plotting function here takes any parameters without trying to determine what is right and what is wrong. If something is wrong, it is likely to appear when the plot is actually plotted, but otherwise it makes life simpler both for user and for programmer. There are only two places where all options should be exposed: dictionary of default values and documentation of `toric_plotter.options` function.

In addition to passing parameters to plotting functions it is also possible to modify global options (e.g. if one want to have black and white plots, or does not like the defaults in some other way).

I did not find it practical to have separate functions for different dimensions, so there are some places with if/else based on dimension. Personally, I think that all these places are bugs of the current Sage plotting system - why point sizes have different meaning for 2-d and 3-d, why arrows behave differently, why text fields take different options? Bugs! On the bright side, toric objects should behave uniformly for 1,2,3-d (no attempts to go higher yet).

I found `toric_varieties.Cube_deformation(4)` to be an excellent reason to have "round" plotting mode as default and invite you to check it as well. "sigma_3" labels in 3-d may not look too great, so we may consider changing it, but then again when you can rotate the plot it does not seem to me that they are difficult to interpret. I am also considering using `wall_color="rainbow"` as default. Check it out - I think it is pretty and not too tacky with `wall_alpha=0.4`! Terminology like "walls" also may be not perfect, but it seems to me that it is convenient to have clear distinction - for plotting purposes cones of different dimension are really different.

Finally, I switched the author on this ticket to myself, but you are given credit in the authors section of the new module since I have used your patch to learn some things about plotting in Sage as well as an inspiration for the round mode, hope it is OK!


---

Comment by novoselt created at 2010-10-04 19:43:20

Changing status from needs_work to needs_review.


---

Comment by novoselt created at 2010-10-04 20:31:25

I rebased the patch to remove dependence from lattice morphisms. The only dependency was because of including new modules into documentation. I hope that this patch is more ripe on the one hand, and it would be convenient to have it while working on fan morphisms on the other.


---

Comment by vbraun created at 2010-10-05 18:58:14

Its very pretty!

Some thoughts: 
  * I would be in favor of `wall_color="rainbow"` being the default, too.
  * Maybe lower the threshold where the lattice is no longer shown by default; I find `toric_varieties.BCdlOG_base().plot()` already not very enlightening.
  * it would be nice if `toric_variety.plot.__doc__` would have a link to `:meth:toric_plotter.options`.

You write "Chamber: 3d cone plotting not implemented yet", did you have something particular in mind? A 3D printer? ;-) Seriously, I guess we want a `chamber_label` option. Anything else? I also think that, in 3d plots, the generating cones and not the 2-cones should be labeled by default. But we don't have to implement that right now.


---

Comment by novoselt created at 2010-10-06 02:46:14

Replying to [comment:8 vbraun]:
> Its very pretty!

Thank you ;-)

> Some thoughts: 
>   * I would be in favor of `wall_color="rainbow"` being the default, too.
Done.
>   * Maybe lower the threshold where the lattice is no longer shown by default; I find `toric_varieties.BCdlOG_base().plot()` already not very enlightening.
Done, now it is radius <= 3 for 3-d plots, I kept 5 for 2-d.
>   * it would be nice if `toric_variety.plot.__doc__` would have a link to `:meth:toric_plotter.options`.
I am not quite sure what you mean. The plot method of toric varieties does have a link to options function, although it was not rendered properly in the interactive help - looks like it was because of "NOTE" after "EXAMPLES". I have changed the order and now everything looks OK to me.

I made two more changes: `label_list` now does put an index on a single label, if this index was passed by the user. The point is that 2-d cones of fans are now marked as "sigma_4" rather than just "sigma". I also use `show_lattice=True` as default for `lattice.plot()` independent of the size: I was playing with plots of lattices and sublattices and got a bit surprised when they have miraculously disappeared.

> You write "Chamber: 3d cone plotting not implemented yet", did you have something particular in mind? A 3D printer? ;-) Seriously, I guess we want a `chamber_label` option. Anything else? I also think that, in 3d plots, the generating cones and not the 2-cones should be labeled by default. But we don't have to implement that right now.

Didn't think of 3D printers and actually didn't think much about 3-d cones until writing the documentation, so it has no reflection in the code yet. What I would like to have are "translucent caps" on them, i.e. the piece of the bounding sphere that is cut out by the cone. It seems to me that the only option is to use polygons in the same way I draw sectors in 3-d and it is not completely trivial (but not terribly hard as well). In "generators" mode it would be quite easy and natural for CPR-Fanos, but again I just didn't work on it yet.


---

Comment by novoselt created at 2010-10-06 02:46:56

Apply this patch only.


---

Attachment

Great! I don't think the cone caps are a priority; I'm not even sure whether they woudl be more confusing than helpful. Colored fog might be useful to show the 3-d cones, but then I don't think that the tachyon interface covers that. 

In other words, I think we should merge this patch now :-)

Release manager: merge `trac_9664_add_toric_potter.patch` only.


---

Comment by vbraun created at 2010-10-06 09:18:00

Changing status from needs_review to positive_review.


---

Comment by mhampton created at 2010-10-06 11:53:42

Tachyon does have a fog command, but its undocumented, and more importantly doesn't seem to work correctly from what I have tested.

I've tried to visualize higher-dimensional fans some, and one thing that might help is to "explode" the fan a bit - i.e. move the cones out a bit from their center, so they are easier to see.  One of my attempts from a couple of years ago is at [http://sage.math.washington.edu/home/mhampton/gf5_14fade.mp4](http://sage.math.washington.edu/home/mhampton/gf5_14fade.mp4) - 39 MB.  I would do a number of things differently now though.


---

Comment by novoselt created at 2010-10-06 14:31:14

Looks pretty, but I cannot say that it really helps me to understand the structure of the fan which seems to be not extremely complicated. I am also more concerned about jmol plots since I didn't master Tachyon to any extent.

For 3-d fans I think current plots will be quite clear if we add labels for 3-d cones and  hide names of their facets. Then "missing" 3-cones will be easy to detect. Of course, one of the reasons I have not think of it earlier is that mostly I work with complete fans and there is no confusion anyway.

For 4-d I am more in favor of "orange peel" as Volker has suggested. As I understand he means taking the intersection of a 4-d fan with a 3-d sphere and then plotting some kind of a projection from this sphere to R<sup>3</sup>. Another option is the dual graph, I wrote such code for a 3-d polyhedral complex in 5-d and it was useful. For non-full dimensional cones one can also just plot them in the basis of the subspace.


---

Comment by mpatel created at 2010-10-08 22:31:09

Resolution: fixed
