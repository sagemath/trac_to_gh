# Issue 5249: implicit_plot3d functionality (isosurfaces, 3d contour plots, etc.)

Issue created by migration from https://trac.sagemath.org/ticket/5249

Original creator: jason

Original creation time: 2009-02-12 20:33:35

Assignee: was

CC:  cwitty wcauchois alexghitza

This is code from Carl Witty, which (almost) implements an implicit_plot3d command to plot isosurfaces of a 3d function.  Carl, would it be fair to say the code is inspired by Jmol's code for generating and displaying isosurfaces?


---

Attachment


---

Comment by jason created at 2009-02-12 20:39:18

(I should say the code is posted here with Carl's permission).

Here are a list of things that he thinks need to be done in order to have it be ready to be reviewed for inclusion in Sage in the shortest amount of time (the rest of this post is quoting Carl's email):

This is the least that I think is necessary to release the code.
Probably (4) (add docstrings and doctests) is by far the most work.

1) remove all mention of colors from the docstring (probably move the
current docstring text into the function body as comments, so it isn't
lost)

2) test NaNs in the function output, or remove the text about NaNs in
the docstring

3) test the following (or, in some cases, remove the text from the docstring):

 * using the standard Sage 3d transforms to move the result around in 3D space
 * explicitly specifying a gradient function
 * using a triple for plot_points, to have separate X,Y,Z resolution
 * using different plot ranges in the different directions

For non-cubical voxels, (either of the last two tests) be sure to test
with tachyon to make sure the gradients are right (make sure that
specular-reflection highlights look correct).  Draw a sphere using the
sphere primitive, and another sphere using implicit_plot3d, and make
sure that the highlights look similar, even when you use very
non-cubical voxels.

4) add docstrings and doctests (you hopefully wouldn't be able to get
it into sage in its current almost-doctestless state, anyway)

5) fix this:

Currently, we forbid giving variable names in the plot ranges.
Probably we should either require them or make them optional.

6) If the following two bugs/potential bugs aren't fixed, then tickets
should be opened against them so they aren't lost:

For surface normals (for smooth rendering in tachyon), it tries to
differentiate the function to find the gradient.  This seems to work
for SR functions, but not for polynomials; it's probably easy to fix,
but I didn't look into it at all.

There's at least one bug that I think is there (but haven't verified):
I think that if an implicit surface is given a transform that squishes
or skews it, then the surface normals will be wrong.  (We transform
the surface normal by the transformation matrix; I seem to recall that
you're supposed to transform surface normals according to the inverse
of the transpose of the transformation matrix.)  (Only the tachyon
renderer uses the surface normals, and only in smooth=True mode.)


---

Comment by jason created at 2009-02-12 20:40:26

Also, here is another thing that could be changed/enhanced:

> Carl Witty wrote:
>> >>        hole - If hole is given, it must be a python callable.
>> >>            Segments of the surface where hole(x,y,z) returns a number >0
>> >>            will be omitted.  (Note that returning a Python boolean
>> >>            is acceptable, since as a number, True == 1 and False == 0.)
>> >>
> >
> > I'm curious why you chose to implement a "hole" parameter instead of MMA's
> > (opposite) RegionFunction parameter (see the ContourPlot3D docs).

1) I hadn't even looked at the ContourPlot3D docs until I was mostly
done with the implementation.

2) I was probably influenced by the JVXL-format mention of NaN's
making holes in the surfaces; so I was thinking about how to replicate
this effect, and punch holes.

If whoever works on the code next wants to invert the "hole" into
"regionfunction", that would be fine with me.

Note the somewhat unusual specification of "hole", checking for >0
instead of for True.  I did this to perhaps make it easier to use a
fast_float function for the hole.  (I didn't do much thinking about
it, though.)


---

Comment by jason created at 2009-02-12 20:42:09

I hope to be able to finish this soon (i.e., in the next couple of weeks at the latest).  If anyone wants to work on it before the end of February 2009, please (1) feel free to do so! and (2) post a note on the ticket here so that we do not duplicate work.


---

Comment by cwitty created at 2009-02-12 22:11:59

> Carl, would it be fair to say the code is inspired by Jmol's code for 
> generating and displaying isosurfaces? 

Definitely.  Plus, some of the non-code chunks (some nice ASCII art, and the triangle-generation table) are directly copied from the Jmol source.  (All such instances are nicely commented, and the file copyright explains the situation.)

Let me get one more item into the permanent record here:

There is support that is mostly implemented, but doesn't quite work, for producing colored plots (where the color at each point comes from a separate function, producing either scalar or RGB values).  This is documented as working, but it doesn't.

As I mentioned above, one possibility would be to just remove the bits about color from the documentation.  But another would be to actually fix the color support.

For Jmol, I think this just involves feeding colors into the
JVXLRunLenthEncoder in self.colors (using the same
self.fraction_as_character() call as for the edge data), then changing
some text in the JVXL header and appending the text from self.colors
after the edge data.  (The JVXLRunLengthEncoder has never been tested;
alternatively, you can just replace it with a StringIO, and that
should work -- the run length encoding is optional.)

For tachyon, at first I thought that it wouldn't be possible to get
nice colors -- the documentation doesn't mention any triangle
primitive that lets you do smooth-shaded colors.  But I found the
undocumented VCSTRI in the tachyon source, that looks like exactly
what you would want.


---

Comment by cwitty created at 2009-02-21 19:18:00

1) There's a bug in the module_list entry, so that the patch won't build unless you have a system numpy installed; this (from Jason) explains how to fix it:

"
This looks like a typical problem with the path to include the numpy arrayobject.h.  I think the extension section for this Cython module in devel/sage/sage/module_list.py should have:

include_dirs = numpy_include_dirs

added to it (search for that text to see examples of extension modules with this include directive)
"

2) It sounds like William's student William Cauchois may start working on this, so I count three people (Alex Ghitza, Jason Grout, and William Cauchois) who might do some work on this patch whenever they get around to it.  You should probably coordinate with each other somehow, possibly by posting a note on this ticket when you actually do start working on it.


---

Comment by wcauchois created at 2009-02-28 09:34:51

Hi, I just started working on this issue!

One thing I noticed is that the automated testing framework tests instances of Graphics3d by invoking the obj() method, which returns a representation in Wavefront OBJ format -- however, ImplicitSurface does not support this feature yet. So do you think we should add this feature (presumably by building off of MarchingCubesTachyon)? Or should we, for example, invoke export_jmol() inside of a stub obj_repr() method just to make the automated tests actually test something?

I've attached a patch with some minor fixes which ensures the code will build and pass the doctests trivially -- obj_repr() is defined to return the empty string, for now.


---

Comment by jason created at 2009-02-28 09:56:29

Are you absolutely sure that it is the Wavefront obj format?  My guess is that it's actually supposed to return a Python pickled object, which usually has extension .obj.

As for exactly what to do, we should probably support some sort of saving so that things are consistent.  In other words, if c is an implicit plot, then c.save() should work.  Again, pickling is the thing to look up for this.


---

Comment by was created at 2009-02-28 16:27:55

> supposed to return a Python pickled object, which usually has extension .obj. 

Actually the extension is ".sobj"


---

Comment by wcauchois created at 2009-02-28 20:10:29

I'm sure its the Wavefront OBJ format; look at this output, from ParametricSurface.obj():

```
g obj_1
usemtl texture16
v 1 1 0
v 1 0.996757 0.0804666
v 1 0.98705 0.160411
v 1 0.970942 0.239316
v 1 0.948536 0.316668
...
```



---

Comment by wcauchois created at 2009-03-09 23:50:38

(By the way, I was wrong about the way the automated testing works; it does the sensible thing, and tests every output format. All that's necessary is a stub obj_repr() method to keep it from complaining.)

I"ve attached a patch with what I have so far:
 * Added docstrings and tests to most of the major functions (in the new ReST format), with a few notable exceptions. MarchingCubes.process_slice and related methods are inherently stateful, and thus hard to test -- although they are indirectly tested by render_implicit and implicit_plot3d.
 * Removed all mention of colors from the docstring for implicit_plot3d.
 * Added support for explicitly specifying plot variables via extract_vars_ranges_and_adapt.
 * Added defaults for plot_points, render_params, and texture (the latter two in MarchingCubes.__init__).

I did find a bug which is that MarchingCubesJVXL cannot handle heterogeneous plot ranges; try the last example under TESTS with show(viewer='tachyon') and then show(viewer='jmol').

Also, we need many more examples!

I will see what I can do.


---

Comment by jason created at 2009-03-12 22:53:12

what is the status of work on this ticket? I might have some time next week to work on something, and I'd like to see this get in.


---

Attachment

I updated trac5249.patch. Apply it on top of implicit-surfaces.patch.

I added 28 examples to the docstring for implicit_plot3d. I also attached many-more-examples.tar, which contains a simple script I used to format the examples. It can output the examples in a Sage notebook format, so if you want to see the examples, you should check it out.

Jason: Here's the status. I've done much of the work that Carl described in his original email. Currently, the major thing left to do is fixing bugs.

Aside from the two bugs Carl mentioned, which are still outstanding, there is one critical bug that I discovered. If you specify different X, Y or Z ranges, then Jmol rendering is radically wrong (although Tachyon is unaffected). For example, try this:


```
var('x,y,z')
implicit_plot3d(x^2+y^2+z^2-4,(-2,0),(-2,2),(-2,2)).show(viewer='jmol')
```


Good luck, I hope you can make some headway!


---

Comment by mvngu created at 2009-03-23 07:45:16

I applied the above patches against Sage 3.4 in the following order:
 1. implicit-surface.patch
 1. trac5249-minorfixes.patch
 1. trac5249.patch
But 2 hunks failed:

```
sage: hg_sage.apply("/home/mvngu/patch/5249/implicit-surface.patch")
cd "/home/mvngu/scratch/sage-3.4/devel/sage" && hg status
cd "/home/mvngu/scratch/sage-3.4/devel/sage" && hg status
cd "/home/mvngu/scratch/sage-3.4/devel/sage" && hg import   "/home/mvngu/patch/5249/implicit-surface.patch"
applying /home/mvngu/patch/5249/implicit-surface.patch
sage: hg_sage.apply("/home/mvngu/patch/5249/trac")
/home/mvngu/patch/5249/trac5249-minorfixes.patch
/home/mvngu/patch/5249/trac5249.patch
sage: hg_sage.apply("/home/mvngu/patch/5249/trac5249-minorfixes.patch")
cd "/home/mvngu/scratch/sage-3.4/devel/sage" && hg status
cd "/home/mvngu/scratch/sage-3.4/devel/sage" && hg status
cd "/home/mvngu/scratch/sage-3.4/devel/sage" && hg import   "/home/mvngu/patch/5249/trac5249-minorfixes.patch"
applying /home/mvngu/patch/5249/trac5249-minorfixes.patch
sage: hg_sage.apply("/home/mvngu/patch/5249/trac5249.patch")
cd "/home/mvngu/scratch/sage-3.4/devel/sage" && hg status
cd "/home/mvngu/scratch/sage-3.4/devel/sage" && hg status
cd "/home/mvngu/scratch/sage-3.4/devel/sage" && hg import   "/home/mvngu/patch/5249/trac5249.patch"
applying /home/mvngu/patch/5249/trac5249.patch
patching file module_list.py
Hunk #1 FAILED at 772
1 out of 1 hunks FAILED -- saving rejects to file module_list.py.rej
patching file sage/plot/plot3d/implicit_surface.pyx
Hunk #1 succeeded at 1150 with fuzz 2 (offset 5 lines).
Hunk #2 FAILED at 1227
Hunk #3 FAILED at 1248
2 out of 3 hunks FAILED -- saving rejects to file sage/plot/plot3d/implicit_surface.pyx.rej
patching file sage/plot/plot3d/implicit_surface.pyx
Hunk #14 succeeded at 1323 with fuzz 1 (offset 0 lines).
abort: patch failed to apply
```



---

Comment by wcauchois created at 2009-04-02 23:09:40

Replying to [comment:14 mvngu]:
> I applied the above patches against Sage 3.4 in the following order:
>  1. implicit-surface.patch
>  1. trac5249-minorfixes.patch
>  1. trac5249.patch

I incorporated the changes from trac5249-minorfixes.patch into trac5249.patch, so the two were never meant to be applied together. William has deleted trac5249-minorfixes.patch from the ticket, so it should now be clear that in order to import implicit plot functionality, you should apply the patches in this order:
 1. implicit-surface.patch
 1. trac5249.patch


---

Comment by wcauchois created at 2009-04-02 23:18:00

Has anyone else noticed that some of the plots, when rendered using the Jmol backend, look very bumpy? The Tachyon renderings of the same plots, however, are fine. William thought the surface normals might be incorrect, but actually, if you zoom in on the model, you can perceive jagged edges in some cases. Is this a bug or a feature? Does anyone know what the problem might be?

To see what I mean, try this code:

```
var('x,y,z')
P = implicit_plot3d((x^2 + y^2 - 1) * ( x^2 + z^2 - 1) - 1, (x, -3, 3), (y, -3, 3), (z, -3, 3))
P.show(viewer='jmol')
# P.show(viewer='tachyon') # uncomment this
```



---

Comment by cwitty created at 2009-04-03 03:40:54

_Has anyone else noticed that some of the plots, when rendered using the Jmol backend, look very bumpy?_

Yes.  I saw this problem when drawing spheres, and made a random change to "fix" it.  Search for "Make mysterious correction for Z edges" in the code.  This may be a different problem with a similar symptom; or it may be the same problem, and my previous change was horribly wrong.  (But it did appear to fix the problem in the spheres I was drawing.)


---

Comment by wcauchois created at 2009-04-07 04:37:01

Replying to [comment:17 cwitty]:
> Yes.  I saw this problem when drawing spheres, and made a random change to "fix" it.  Search for "Make mysterious correction for Z edges" in the code.  This may be a different problem with a similar symptom; or it may be the same problem, and my previous change was horribly wrong.  (But it did appear to fix the problem in the spheres I was drawing.)

Interesting. I took a look at some plots sans your correction, and it looks like it might be the same species of bug -- the plots have a kind of ripple distortion, radiating outward from a pole. Your change was not wrong, however, or at least its removal did not affect any other bugs.

Is there anyone more knowledgeable about marching cubes and JVXL who is willing to work on this bug? I will do what I can. I'd like to see implicit_plot3d in Sage in the near future!


---

Comment by wcauchois created at 2009-04-15 01:01:52

After thoroughly examining the code, I've come to believe that the jaggedness in the Jmol plots is due to a limitation of the JVXL file format. The interpolation values along the edges must be rounded to fit into a byte (actually, less than a byte -- there are 90 possible values), and I think that this loss of precision accounts for the incorrect plots. If that's the case, then MarchingCubesJVXL might be unsalvageable.

William suggested I write a backend for Jmol rendering that eschews the JVXL format in favor of a polygonal representation, and I think that would be the best course of action. Even if we lose some efficiency, we gain a measure of control. In fact, I would like to unify the Tachyon and Jmol backends by using IndexFaceSet. I could refactor MarchingCubesTachyon to make this happen. Another advantage of IndexFaceSet is that it gives us a number of features for free -- such as transparency, and mesh=True.

Carl, does this sound like a good plan?


---

Comment by jason created at 2009-04-15 01:39:13

I strongly suggest that you bounce this off of the author of JMOL.  It sounds like you've done a fair amount of research; they might have some ideas to address this issue as well.


---

Comment by cwitty created at 2009-04-15 05:43:48

I'm a little dubious about the rounding being the problem.  If you have plot_points=(20,20,20), and you have this plot zoomed to fill a 600x600 window, then the quantization error is about 600/(20*90) = 1/3 pixel.  The jaggedness I've seen seems a lot more than 1/3 pixel...

But killing off MarchingCubesJVXL in favor of something using `IndexFaceSet` does seem like a good idea (although it's a little sad, since we've both spent hours on MarchingCubesJVXL... oh well).  It will presumably fix the problem no matter what the problem is, since `IndexFaceSet` does seem to work OK with jmol in general, and the tachyon implicit_plot3d plots are not jagged.


---

Comment by wcauchois created at 2009-04-15 23:41:02

jason: That's a great idea. I posted a message to the jmol-users mailing list. I'll let you all know if I get any useful replies.

cwitty: I'll be sorry if I have to abandon MarchingCubesJVXL, but I think there are a number of advantages to an IndexFaceSet based approach. I just want to get this thing working well!


---

Comment by wcauchois created at 2009-04-24 03:00:52

Here's a status update:

I posted to the jmol-users mailing list and Robert Hanson, who wrote most of the isosurface code in Jmol, helped me find the problem with our JVXL files. Apparently the JVXL specification is wrong. Where the spec says

```
for (int x = voxelCountX; --x >= 0;) {
 for (int y = voxelCountY; --y >= 0;) {
   for (int z = voxelCountZ; --z >= 0;) {
```

to demonstrate the order for visiting voxels (on page 7), it should be

```
for (int x = 0; x < voxelCountX; x++) {
 for (int y = 0; y < voxelCountY; y++) {
   for (int z = 0; z < voxelCountZ; z++) {
```

-- that is to say, the order is reversed. A quick fix for this is to reverse the order of the edge data stored in self.bitmap in MarchingCubesJVXL. I tried it and it worked.

Anyhow, I also wrote a backend based on IndexFaceSet, and that works fine, and I've attached the patch. I think the IndexFaceSet backend should be the default for both Jmol and Tachyon, since it offers a number of features -- including mesh=True, transparency, and methods to manipulate the mesh programmatically. As long as MarchingCubesJVXL is working, shall we keep support for JVXL as a feature?

There is one outstanding issue with the IndexFaceSet backend, which is that the scale for the Jmol plots is incorrect. If you try to graph something, you can see that the figure will be larger than its bounding box by a factor of about 3. I believe the bounding box is correct, so the problem must be with the transformation matrix we are given through render_params or the way we apply that transformation. On line 317 of plot3d/base.pyx, in _prepare_for_jmol, I noticed that it applies some scaling factor "s" (=3). Do we have to account for that somehow? Does anyone have any insight into this issue?

So basically the major things left to do are to fix that bug, and add doctests for everything. I will continue to work on this.


---

Comment by jason created at 2009-04-24 03:36:52

Robert Bradshaw might be a good person to ask that _prepare_for_jmol question.


---

Comment by jason created at 2009-04-24 03:40:15

Is there any reason why mesh and transparency can't work with jvxl files?  JVXL and the pmesh both give ways to specify a surface to jmol; I don't see why you shouldn't be able to specify mesh=True and transparency options when passing a jvxl file.  If not, can we request it?  Do you know the size difference between a (zipped) pmesh command file to jmol and the equivalent (zipped) jvxl command file?

Thanks for all of your work on this!


---

Comment by robertwb created at 2009-04-24 03:44:10

I have no idea what the factor of 3 is about--William Stein wrote the _prepare_for_jmol functions--but I would guess it's something to do with trying to center the object in the middle 1/3 of the viewable area. I believe the bounding box functionality method on IndexFaceSet is correct, but it would be good to have some doctests asserting this.


---

Comment by jason created at 2009-04-24 04:24:30

If I understand things correctly, page 2 of http://chemapps.stolaf.edu/jmol/docs/misc/JVXL-format.pdf shows several jvxl surfaces that are transparent.  So why is transparency an issue with jvxl format?


---

Comment by wcauchois created at 2009-04-24 07:56:26

I'm sorry I wasn't clear. I'm pretty sure transparency is possible for JVXL files, we just haven't implemented it yet. I don't know how mesh=True works though. So I guess those points don't really count for the IFS based implementation.

I will try to get the difference in size between a pmesh file and a JVXL file for you. But I can tell you now that the main advantage of JVXL is size, since efficient compression of isosurfaces was one of its primary design goals.


---

Comment by wcauchois created at 2009-04-26 23:17:11

I fixed the scaling issue for Jmol plots. The bug was due to render_params.transform being applied twice -- once in MarchingCubes, and once in IndexFaceSet.jmol_repr.


---

Comment by wcauchois created at 2009-04-29 23:30:16

I would like to rename the "hole" parameter so that it is consistent with me and Jason's work on #5514, which implements exclusions for parametric 3D plots. Is everybody OK with the term "region"? So the user provides a "region" parameter which returns True for all points that should be included. Note that this is an inversion of the logic for "hole", which returns False for all points that should be included. We currently use "region_function" in #5514, but I would like to change that as well to the more concise "region".


---

Comment by cwitty created at 2009-04-29 23:49:31

Definitely it should use the same name as #5514.  I'm fine with changing the name and inverting the meaning of True/False.

I have a slight preference for region_function over region, for two reasons: 1) to match Mathematica; and 2) because we do require a function.  (If region=(x<sup>2</sup>+y<sup>2</sup>+z<sup>2</sup><1) worked, then "region" would probably be better than "region_function".  And of course, it wouldn't be hard to make that work.)


---

Comment by jason created at 2009-04-30 00:07:33

+1 on calling it "region" (and then followed by a patch or two that make it more general than a function :).

and +1 on inverting the "hole" meaning.


---

Comment by wcauchois created at 2009-05-01 07:43:34

So I think this patch is ready for review! Apply trac5249.patch.

Test coverage is up to 100%, and I renamed the "hole" parameter to "region". This implementation uses only the IndexFaceSet based backend, but it is fully functional. I would like to get this into Sage, and then we can work on integrating MarchingCubesJVXL again. Robert Bradshaw had a good suggestion, which was that we should make ImplicitSurface more generic so that it can accept a user-specified array of voxels and triangulate that. I can open a ticket to address these potential features.


---

Comment by was created at 2009-05-05 20:58:44

this applies cleanly against 3.4.2


---

Attachment


---

Comment by mabshoff created at 2009-05-13 17:11:42

Two remarks, both of which should be addressed via followup tickets:

 * lots of docstrings of non-underscore methods consist only of tests, but no description what the function does
 * the new functionality has not been added to the reference manual, so it is hard to be aware that the functionality exists

Also: Is the following correct?

 * credit for authorship: Bill Cauchois, Carl Witty, Jason Grout
 * credit for review: William Stein



Cheers,

Michael


---

Comment by mabshoff created at 2009-05-13 17:39:26

Resolution: fixed


---

Comment by mabshoff created at 2009-05-13 17:39:26

Merged trac_5249-flat.patch only in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by jason created at 2009-05-13 21:17:31

I don't think I wrote any actual code on this patch (unless someone remembers something that I didn't).  Carl Witty single-handedly wrote the initial patch (which I posted), and then Bill took it from there.  I think it would be fair to put me in as a reviewer, though.  Good job, guys!


---

Comment by mabshoff created at 2009-05-14 05:15:21

Replying to [comment:38 jason]:
> I don't think I wrote any actual code on this patch (unless someone remembers something that I didn't).  Carl Witty single-handedly wrote the initial patch (which I posted), and then Bill took it from there.  I think it would be fair to put me in as a reviewer, though.  Good job, guys!

Ok, credits fixed accordingly.

Cheers,

Michael
