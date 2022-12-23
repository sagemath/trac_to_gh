# Issue 6447: Add a <canvas> renderer for 3D plotting

Issue created by migration from https://trac.sagemath.org/ticket/6447

Original creator: wcauchois

Original creation time: 2009-06-29 18:43:12

Assignee: was

CC:  saliola wdj

This feature would add another backend to 3D plotting, in addition to Jmol and Tachyon, that would render the plot using the new HTML5 <canvas> element, which supports drawing arbitrary shapes to a section of a web page.

The idea was initially suggested in [this thread](http://groups.google.com/group/sage-devel/browse_thread/thread/9e0ca32eb97d5757/d47d88b28d292512) on sage-devel.

Although JavaScript is significantly slower than Java, a canvas backend is feasible and might provide a nice, compatible, alternative.


---

Comment by wcauchois created at 2009-06-29 18:55:41

The attached patch implements the feature as described, although it currently only renders in wireframe.

Try it out for yourself:

```
x, y = var('x y')
plot3d(sin(pi*(x^2+y^2))/2,(x,-1,1),(y,-1,1), viewer='canvas3d', plot_points=(20, 20))
```


A couple of issues need to be addressed:

 * Doctests. As well as documentation to make this feature visible to an end-user.
 * Solid polygons. Here we run into problems like depth-testing and shading. I'm sure there are JavaScript libraries available for 3D rendering using canvas. Could we plug one of these in?
 * I am somewhat unsatisfied with the mechanism for rotating the model. Currently, the X and Y position of the mouse are used to rotate the model about the Y and X axes. But this can result in unexpected rotations, due to the inadequacy of Euler angles (wherein one rotation configuration can be represented in multiple ways). I'm aware of a better method for user interaction with a 3D viewer called [Arcball](http://rainwarrior.thenoos.net/dragon/arcball.html), but that looks too complicated to do in JavaScript.


---

Comment by wdj created at 2009-06-29 20:50:54

This is cool!

Note that it works with parametric_plot3d as well.

The rotations do seem kind of jerky, as you pointed out, at least on a macbook running 10.4.11 and inside camino. Still, thanks for working on this - I think this will be *very* useful at some point.


---

Comment by ddrake created at 2009-06-29 23:50:16

I second wdj's "this is cool"!

I don't know about JS libraries for solid polygons, but I used LiveGraphics3D (which made Java applets out of Mathematica code) for a long time, and it used a pretty naive algorithm for determining which polygon was in front, and some things just looked bad. I suspect that getting a good algorithm for doing that sort of thing well is difficult...but would be awesome to have!


---

Comment by robertwb created at 2009-06-30 02:25:57

Very cool!


---

Comment by rbeezer created at 2009-06-30 06:37:40

Very nice!  Worked very smoothly for me.


---

Comment by was created at 2009-06-30 13:32:22

Comments:

(1) I don't think you should worry too much about wireframe versus solid polygons yet.   This is javascript/canvas, after all.  I think it would be much better to focus on rendering a wider range of objects, e.g., make it so 

```
icosahedron(color='red', viewer='canvas3d') + sphere(viewer='canvas3d')
```

works. 

(2) I notice that you're "I'm sure there are JavaScript? libraries available for 3D rendering using canvas. Could we plug one of these in?"  I tried googling for some of those words, and the first thing that pops up is:
   http://www.nihilogic.dk/labs/canvas3dtexture_0.2/
If you turn off the texture in that link and render some of the models (select from the list on the right), you'll see that indeed you are right, there are now 3d canvas javascript libraries. 

William


---

Comment by wcauchois created at 2009-07-15 02:29:42

I added much smoother trackball rotation, and fixed several bugs. Now could anyone take a look at this?


---

Comment by saliola created at 2009-07-15 07:45:15

The patch applies cleanly to sage-4.1 and is working very well (FF3, Ubuntu 8.10, amd64). So from me it gets a positive review.

Can people with different systems/browsers give this a try?


---

Comment by wdj created at 2009-07-15 19:15:39

Yes, the patch applied fine but then I got this (amd64, ubuntu 9.04):


```
wdj@hera:~/sagefiles/sage-4.1.rc0$ ./sage -t  "devel/sage/sage/plot/plot3d/implicit_plot3d.py"
sage -t  "devel/sage/sage/plot/plot3d/implicit_plot3d.py"
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
*** *** Error: TIMED OUT! *** ***
         [360.1 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/plot/plot3d/implicit_plot3d.py"
```

It seems related but I'm not sure.


---

Comment by wdj created at 2009-07-15 19:54:48

Same thing on an intel macbook running 10.4.11. I'm inclined to label this "needs work" but am not sure what the problem is.


---

Comment by wcauchois created at 2009-07-15 21:23:43

Replying to [comment:10 wdj]:

It can't seem to finish the test on line 45 of implicit_plot3d.py. Its an issue that only shows up during doctesting mode. I've been looking into this, and I think I can have a patch to fix it by later tonight. Thanks for catching this!


---

Comment by wcauchois created at 2009-07-16 02:26:35

based on sage 4.1


---

Attachment


---

Comment by saliola created at 2009-07-16 11:17:01

With the new patch, the doctests pass for me on a x86_64 machine running 2.6.23-gentoo-r6.


---

Comment by wdj created at 2009-07-16 14:11:07

Same here, on an amd64 ubuntu 9.04 machine. Applies fine and passes sage -testall.

I would give this a positive review but I am unsure of the requirements for examples in the docstrings for plotting functions. If this did not return a plot but a number (say) then it would be necessary to have an example illustrating the new method. (There are example docstrings but none that return a plot.) Does anyone know what the standard is here?


---

Comment by wcauchois created at 2009-07-16 17:42:52

Replying to [comment:15 wdj]:
> Same here, on an amd64 ubuntu 9.04 machine. Applies fine and passes sage -testall.
> 
> I would give this a positive review but I am unsure of the requirements for examples in the docstrings for plotting functions. If this did not return a plot but a number (say) then it would be necessary to have an example illustrating the new method. (There are example docstrings but none that return a plot.) Does anyone know what the standard is here?

I can add an example to the documentation for show(), but other than that I can't think of any place where more documentation would be appropriate.


---

Attachment

apply only this patch to sage 4.1


---

Comment by wcauchois created at 2009-07-16 18:22:05

Ok, just did it.

I also had to reorder the elements of the set in a doctest for texture_set(). I have found that unrelated changes to the codebase can cause the elements to assume a different order than what is expected. Obviously order doesn't matter with sets, but the doctesting system counts it as a failure. I think a more permanent solution could be achieved by defining a better __hash__ for Texture_class, since from my experiments that is how the internal element order is determined. For now, though, I've been modifying the offending doctest by hand.


---

Comment by wcauchois created at 2009-07-16 21:16:45

I wonder how #6307 will affect this ticket. I think moving the canvas3d lib into a separate JS file would be great. Does that mean we should rebase this patch on sage-4.1.1-alpha0?


---

Comment by wdj created at 2009-07-16 21:32:48

Damn. I think I screwed up on applying the doctest somehow because I got a boatload of failures. 
Can you rebase and then tell me where to access sage-4.1.1-alpha0?


---

Comment by wcauchois created at 2009-07-17 16:53:42

I don't know anything about sage-4.1.1.alpha0, except that #6307 was merged into it yesterday. I'm going to mark this [needs rebase] until I can find a development version of Sage with the changes from #6307 and move the canvas3d lib into a separate JS file. And then we can get this into Sage!


---

Comment by wcauchois created at 2009-07-28 16:06:49

based on sage 4.1.1.alpha1


---

Attachment

I attached a self-contained patch where I've moved the JavaScript code into a separate file, in keeping with the changes made in #6307. Its based on Sage 4.1.1.alpha1. Can someone re-review this?


---

Comment by wdj created at 2009-07-28 22:31:40

This applies fine to 4.1.1.a1 and pases sage -testall (amd64, ubuntu 9.04) except for the already reported failures at 


```

        sage -t  "devel/sage/sage/misc/abstract_method.py"
        sage -t  "devel/sage/sage/misc/lazy_attribute.py"
```


Again, a positive test from me.


---

Comment by mpatel created at 2009-08-07 01:41:58

Quick questions:
 * Should the default view angle for the new viewer match that for tachyon and jmol?
 * Is it possible to enable axes?


---

Comment by wcauchois created at 2009-08-12 00:10:37

Replying to [comment:23 mpatel]:
> Quick questions:
>  * Should the default view angle for the new viewer match that for tachyon and jmol?

That's a good idea. I found a tuple called "orientation" in Graphics3d.export_jmol, so I think I can copy the values from that.

>  * Is it possible to enable axes?

Axes are not currently implemented, although they can be. I think all that's necessary is to add support for arrow3d.


---

Comment by mpatel created at 2009-08-17 06:57:22

I think that axes are, perhaps, more important, since they give a sense of scale of a plot's "landscape."

But I'm happy to defer to D. Joyner on reviewing this ticket. 

Another question, possibly very naive:  Would it be less taxing on the browser to use "quads" instead of triangles as mesh elements, at least in some circumstances?


---

Comment by wdj created at 2009-08-17 10:11:13

Replying to [comment:25 mpatel]:
> I think that axes are, perhaps, more important, since they give a sense of scale of a plot's "landscape."
> 
> But I'm happy to defer to D. Joyner on reviewing this ticket. 
> 
> Another question, possibly very naive:  Would it be less taxing on the browser to use "quads" instead of triangles as mesh elements, at least in some circumstances?  


When I gave this my positive review, I'm not saying that this patch is in it's final form. I'm sure that there are lots of improvements possible. But as a patch implementing an important new idea, it is excellent I think. The problem with me changing "neds" to "positive" is that I do not know javascript. William Stein said he would look this code over. But if someone else wants to (eg, mpatel) then I'm sure William won't mind:-)


---

Comment by was created at 2009-08-29 05:58:24

wdj -- this looks good to me.  It doesn't have axes and "everything", but neither does tachyon.  But it provides new and *very* valuable functionality.


---

Comment by mvngu created at 2009-08-30 07:26:00

Resolution: fixed


---

Comment by mvngu created at 2009-08-30 07:26:00

Merged `trac_6447~rebase.patch`.
