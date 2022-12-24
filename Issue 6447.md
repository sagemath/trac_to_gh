# Issue 6447: Add a <canvas> renderer for 3D plotting

archive/issues_006447.json:
```json
{
    "body": "Assignee: was\n\nCC:  saliola wdj\n\nThis feature would add another backend to 3D plotting, in addition to Jmol and Tachyon, that would render the plot using the new HTML5 <canvas> element, which supports drawing arbitrary shapes to a section of a web page.\n\nThe idea was initially suggested in [this thread](http://groups.google.com/group/sage-devel/browse_thread/thread/9e0ca32eb97d5757/d47d88b28d292512) on sage-devel.\n\nAlthough JavaScript is significantly slower than Java, a canvas backend is feasible and might provide a nice, compatible, alternative.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6447\n\n",
    "created_at": "2009-06-29T18:43:12Z",
    "labels": [
        "graphics",
        "minor",
        "enhancement"
    ],
    "title": "Add a <canvas> renderer for 3D plotting",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6447",
    "user": "wcauchois"
}
```
Assignee: was

CC:  saliola wdj

This feature would add another backend to 3D plotting, in addition to Jmol and Tachyon, that would render the plot using the new HTML5 <canvas> element, which supports drawing arbitrary shapes to a section of a web page.

The idea was initially suggested in [this thread](http://groups.google.com/group/sage-devel/browse_thread/thread/9e0ca32eb97d5757/d47d88b28d292512) on sage-devel.

Although JavaScript is significantly slower than Java, a canvas backend is feasible and might provide a nice, compatible, alternative.

Issue created by migration from https://trac.sagemath.org/ticket/6447





---

archive/issue_comments_051801.json:
```json
{
    "body": "The attached patch implements the feature as described, although it currently only renders in wireframe.\n\nTry it out for yourself:\n\n```\nx, y = var('x y')\nplot3d(sin(pi*(x^2+y^2))/2,(x,-1,1),(y,-1,1), viewer='canvas3d', plot_points=(20, 20))\n```\n\n\nA couple of issues need to be addressed:\n\n* Doctests. As well as documentation to make this feature visible to an end-user.\n* Solid polygons. Here we run into problems like depth-testing and shading. I'm sure there are JavaScript libraries available for 3D rendering using canvas. Could we plug one of these in?\n* I am somewhat unsatisfied with the mechanism for rotating the model. Currently, the X and Y position of the mouse are used to rotate the model about the Y and X axes. But this can result in unexpected rotations, due to the inadequacy of Euler angles (wherein one rotation configuration can be represented in multiple ways). I'm aware of a better method for user interaction with a 3D viewer called [Arcball](http://rainwarrior.thenoos.net/dragon/arcball.html), but that looks too complicated to do in JavaScript.",
    "created_at": "2009-06-29T18:55:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51801",
    "user": "wcauchois"
}
```

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

archive/issue_comments_051802.json:
```json
{
    "body": "This is cool!\n\nNote that it works with parametric_plot3d as well.\n\nThe rotations do seem kind of jerky, as you pointed out, at least on a macbook running 10.4.11 and inside camino. Still, thanks for working on this - I think this will be *very* useful at some point.",
    "created_at": "2009-06-29T20:50:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51802",
    "user": "wdj"
}
```

This is cool!

Note that it works with parametric_plot3d as well.

The rotations do seem kind of jerky, as you pointed out, at least on a macbook running 10.4.11 and inside camino. Still, thanks for working on this - I think this will be *very* useful at some point.



---

archive/issue_comments_051803.json:
```json
{
    "body": "I second wdj's \"this is cool\"!\n\nI don't know about JS libraries for solid polygons, but I used LiveGraphics3D (which made Java applets out of Mathematica code) for a long time, and it used a pretty naive algorithm for determining which polygon was in front, and some things just looked bad. I suspect that getting a good algorithm for doing that sort of thing well is difficult...but would be awesome to have!",
    "created_at": "2009-06-29T23:50:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51803",
    "user": "ddrake"
}
```

I second wdj's "this is cool"!

I don't know about JS libraries for solid polygons, but I used LiveGraphics3D (which made Java applets out of Mathematica code) for a long time, and it used a pretty naive algorithm for determining which polygon was in front, and some things just looked bad. I suspect that getting a good algorithm for doing that sort of thing well is difficult...but would be awesome to have!



---

archive/issue_comments_051804.json:
```json
{
    "body": "Very cool!",
    "created_at": "2009-06-30T02:25:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51804",
    "user": "robertwb"
}
```

Very cool!



---

archive/issue_comments_051805.json:
```json
{
    "body": "Very nice!  Worked very smoothly for me.",
    "created_at": "2009-06-30T06:37:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51805",
    "user": "rbeezer"
}
```

Very nice!  Worked very smoothly for me.



---

archive/issue_comments_051806.json:
```json
{
    "body": "Comments:\n\n(1) I don't think you should worry too much about wireframe versus solid polygons yet.   This is javascript/canvas, after all.  I think it would be much better to focus on rendering a wider range of objects, e.g., make it so \n\n```\nicosahedron(color='red', viewer='canvas3d') + sphere(viewer='canvas3d')\n```\n\nworks. \n\n(2) I notice that you're \"I'm sure there are JavaScript? libraries available for 3D rendering using canvas. Could we plug one of these in?\"  I tried googling for some of those words, and the first thing that pops up is:\n   http://www.nihilogic.dk/labs/canvas3dtexture_0.2/\nIf you turn off the texture in that link and render some of the models (select from the list on the right), you'll see that indeed you are right, there are now 3d canvas javascript libraries. \n\nWilliam",
    "created_at": "2009-06-30T13:32:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51806",
    "user": "was"
}
```

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

archive/issue_comments_051807.json:
```json
{
    "body": "I added much smoother trackball rotation, and fixed several bugs. Now could anyone take a look at this?",
    "created_at": "2009-07-15T02:29:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51807",
    "user": "wcauchois"
}
```

I added much smoother trackball rotation, and fixed several bugs. Now could anyone take a look at this?



---

archive/issue_comments_051808.json:
```json
{
    "body": "The patch applies cleanly to sage-4.1 and is working very well (FF3, Ubuntu 8.10, amd64). So from me it gets a positive review.\n\nCan people with different systems/browsers give this a try?",
    "created_at": "2009-07-15T07:45:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51808",
    "user": "saliola"
}
```

The patch applies cleanly to sage-4.1 and is working very well (FF3, Ubuntu 8.10, amd64). So from me it gets a positive review.

Can people with different systems/browsers give this a try?



---

archive/issue_comments_051809.json:
```json
{
    "body": "Yes, the patch applied fine but then I got this (amd64, ubuntu 9.04):\n\n\n```\nwdj@hera:~/sagefiles/sage-4.1.rc0$ ./sage -t  \"devel/sage/sage/plot/plot3d/implicit_plot3d.py\"\nsage -t  \"devel/sage/sage/plot/plot3d/implicit_plot3d.py\"\n*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n*** *** Error: TIMED OUT! *** ***\n*** *** Error: TIMED OUT! *** ***\n         [360.1 s]\nexit code: 1024\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  \"devel/sage/sage/plot/plot3d/implicit_plot3d.py\"\n```\n\nIt seems related but I'm not sure.",
    "created_at": "2009-07-15T19:15:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51809",
    "user": "wdj"
}
```

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

archive/issue_comments_051810.json:
```json
{
    "body": "Same thing on an intel macbook running 10.4.11. I'm inclined to label this \"needs work\" but am not sure what the problem is.",
    "created_at": "2009-07-15T19:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51810",
    "user": "wdj"
}
```

Same thing on an intel macbook running 10.4.11. I'm inclined to label this "needs work" but am not sure what the problem is.



---

archive/issue_comments_051811.json:
```json
{
    "body": "Replying to [comment:10 wdj]:\n\nIt can't seem to finish the test on line 45 of implicit_plot3d.py. Its an issue that only shows up during doctesting mode. I've been looking into this, and I think I can have a patch to fix it by later tonight. Thanks for catching this!",
    "created_at": "2009-07-15T21:23:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51811",
    "user": "wcauchois"
}
```

Replying to [comment:10 wdj]:

It can't seem to finish the test on line 45 of implicit_plot3d.py. Its an issue that only shows up during doctesting mode. I've been looking into this, and I think I can have a patch to fix it by later tonight. Thanks for catching this!



---

archive/issue_comments_051812.json:
```json
{
    "body": "based on sage 4.1",
    "created_at": "2009-07-16T02:26:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51812",
    "user": "wcauchois"
}
```

based on sage 4.1



---

archive/issue_comments_051813.json:
```json
{
    "body": "Attachment [trac_6447-canvas3d.patch](tarball://root/attachments/some-uuid/ticket6447/trac_6447-canvas3d.patch) by wcauchois created at 2009-07-16 02:26:50",
    "created_at": "2009-07-16T02:26:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51813",
    "user": "wcauchois"
}
```

Attachment [trac_6447-canvas3d.patch](tarball://root/attachments/some-uuid/ticket6447/trac_6447-canvas3d.patch) by wcauchois created at 2009-07-16 02:26:50



---

archive/issue_comments_051814.json:
```json
{
    "body": "With the new patch, the doctests pass for me on a x86_64 machine running 2.6.23-gentoo-r6.",
    "created_at": "2009-07-16T11:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51814",
    "user": "saliola"
}
```

With the new patch, the doctests pass for me on a x86_64 machine running 2.6.23-gentoo-r6.



---

archive/issue_comments_051815.json:
```json
{
    "body": "Same here, on an amd64 ubuntu 9.04 machine. Applies fine and passes sage -testall.\n\nI would give this a positive review but I am unsure of the requirements for examples in the docstrings for plotting functions. If this did not return a plot but a number (say) then it would be necessary to have an example illustrating the new method. (There are example docstrings but none that return a plot.) Does anyone know what the standard is here?",
    "created_at": "2009-07-16T14:11:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51815",
    "user": "wdj"
}
```

Same here, on an amd64 ubuntu 9.04 machine. Applies fine and passes sage -testall.

I would give this a positive review but I am unsure of the requirements for examples in the docstrings for plotting functions. If this did not return a plot but a number (say) then it would be necessary to have an example illustrating the new method. (There are example docstrings but none that return a plot.) Does anyone know what the standard is here?



---

archive/issue_comments_051816.json:
```json
{
    "body": "Replying to [comment:15 wdj]:\n> Same here, on an amd64 ubuntu 9.04 machine. Applies fine and passes sage -testall.\n> \n> I would give this a positive review but I am unsure of the requirements for examples in the docstrings for plotting functions. If this did not return a plot but a number (say) then it would be necessary to have an example illustrating the new method. (There are example docstrings but none that return a plot.) Does anyone know what the standard is here?\n\nI can add an example to the documentation for show(), but other than that I can't think of any place where more documentation would be appropriate.",
    "created_at": "2009-07-16T17:42:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51816",
    "user": "wcauchois"
}
```

Replying to [comment:15 wdj]:
> Same here, on an amd64 ubuntu 9.04 machine. Applies fine and passes sage -testall.
> 
> I would give this a positive review but I am unsure of the requirements for examples in the docstrings for plotting functions. If this did not return a plot but a number (say) then it would be necessary to have an example illustrating the new method. (There are example docstrings but none that return a plot.) Does anyone know what the standard is here?

I can add an example to the documentation for show(), but other than that I can't think of any place where more documentation would be appropriate.



---

archive/issue_comments_051817.json:
```json
{
    "body": "Attachment [trac_6447~all.patch](tarball://root/attachments/some-uuid/ticket6447/trac_6447~all.patch) by wcauchois created at 2009-07-16 18:05:18\n\napply only this patch to sage 4.1",
    "created_at": "2009-07-16T18:05:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51817",
    "user": "wcauchois"
}
```

Attachment [trac_6447~all.patch](tarball://root/attachments/some-uuid/ticket6447/trac_6447~all.patch) by wcauchois created at 2009-07-16 18:05:18

apply only this patch to sage 4.1



---

archive/issue_comments_051818.json:
```json
{
    "body": "Ok, just did it.\n\nI also had to reorder the elements of the set in a doctest for texture_set(). I have found that unrelated changes to the codebase can cause the elements to assume a different order than what is expected. Obviously order doesn't matter with sets, but the doctesting system counts it as a failure. I think a more permanent solution could be achieved by defining a better __hash__ for Texture_class, since from my experiments that is how the internal element order is determined. For now, though, I've been modifying the offending doctest by hand.",
    "created_at": "2009-07-16T18:22:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51818",
    "user": "wcauchois"
}
```

Ok, just did it.

I also had to reorder the elements of the set in a doctest for texture_set(). I have found that unrelated changes to the codebase can cause the elements to assume a different order than what is expected. Obviously order doesn't matter with sets, but the doctesting system counts it as a failure. I think a more permanent solution could be achieved by defining a better __hash__ for Texture_class, since from my experiments that is how the internal element order is determined. For now, though, I've been modifying the offending doctest by hand.



---

archive/issue_comments_051819.json:
```json
{
    "body": "I wonder how #6307 will affect this ticket. I think moving the canvas3d lib into a separate JS file would be great. Does that mean we should rebase this patch on sage-4.1.1-alpha0?",
    "created_at": "2009-07-16T21:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51819",
    "user": "wcauchois"
}
```

I wonder how #6307 will affect this ticket. I think moving the canvas3d lib into a separate JS file would be great. Does that mean we should rebase this patch on sage-4.1.1-alpha0?



---

archive/issue_comments_051820.json:
```json
{
    "body": "Damn. I think I screwed up on applying the doctest somehow because I got a boatload of failures. \nCan you rebase and then tell me where to access sage-4.1.1-alpha0?",
    "created_at": "2009-07-16T21:32:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51820",
    "user": "wdj"
}
```

Damn. I think I screwed up on applying the doctest somehow because I got a boatload of failures. 
Can you rebase and then tell me where to access sage-4.1.1-alpha0?



---

archive/issue_comments_051821.json:
```json
{
    "body": "I don't know anything about sage-4.1.1.alpha0, except that #6307 was merged into it yesterday. I'm going to mark this [needs rebase] until I can find a development version of Sage with the changes from #6307 and move the canvas3d lib into a separate JS file. And then we can get this into Sage!",
    "created_at": "2009-07-17T16:53:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51821",
    "user": "wcauchois"
}
```

I don't know anything about sage-4.1.1.alpha0, except that #6307 was merged into it yesterday. I'm going to mark this [needs rebase] until I can find a development version of Sage with the changes from #6307 and move the canvas3d lib into a separate JS file. And then we can get this into Sage!



---

archive/issue_comments_051822.json:
```json
{
    "body": "based on sage 4.1.1.alpha1",
    "created_at": "2009-07-28T16:06:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51822",
    "user": "wcauchois"
}
```

based on sage 4.1.1.alpha1



---

archive/issue_comments_051823.json:
```json
{
    "body": "Attachment [trac_6447~rebase.patch](tarball://root/attachments/some-uuid/ticket6447/trac_6447~rebase.patch) by wcauchois created at 2009-07-28 16:11:36\n\nI attached a self-contained patch where I've moved the JavaScript code into a separate file, in keeping with the changes made in #6307. Its based on Sage 4.1.1.alpha1. Can someone re-review this?",
    "created_at": "2009-07-28T16:11:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51823",
    "user": "wcauchois"
}
```

Attachment [trac_6447~rebase.patch](tarball://root/attachments/some-uuid/ticket6447/trac_6447~rebase.patch) by wcauchois created at 2009-07-28 16:11:36

I attached a self-contained patch where I've moved the JavaScript code into a separate file, in keeping with the changes made in #6307. Its based on Sage 4.1.1.alpha1. Can someone re-review this?



---

archive/issue_comments_051824.json:
```json
{
    "body": "This applies fine to 4.1.1.a1 and pases sage -testall (amd64, ubuntu 9.04) except for the already reported failures at \n\n\n```\n\n        sage -t  \"devel/sage/sage/misc/abstract_method.py\"\n        sage -t  \"devel/sage/sage/misc/lazy_attribute.py\"\n```\n\n\nAgain, a positive test from me.",
    "created_at": "2009-07-28T22:31:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51824",
    "user": "wdj"
}
```

This applies fine to 4.1.1.a1 and pases sage -testall (amd64, ubuntu 9.04) except for the already reported failures at 


```

        sage -t  "devel/sage/sage/misc/abstract_method.py"
        sage -t  "devel/sage/sage/misc/lazy_attribute.py"
```


Again, a positive test from me.



---

archive/issue_comments_051825.json:
```json
{
    "body": "Quick questions:\n* Should the default view angle for the new viewer match that for tachyon and jmol?\n* Is it possible to enable axes?",
    "created_at": "2009-08-07T01:41:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51825",
    "user": "mpatel"
}
```

Quick questions:
* Should the default view angle for the new viewer match that for tachyon and jmol?
* Is it possible to enable axes?



---

archive/issue_comments_051826.json:
```json
{
    "body": "Replying to [comment:23 mpatel]:\n> Quick questions:\n>  * Should the default view angle for the new viewer match that for tachyon and jmol?\n\nThat's a good idea. I found a tuple called \"orientation\" in Graphics3d.export_jmol, so I think I can copy the values from that.\n\n>  * Is it possible to enable axes?\n\nAxes are not currently implemented, although they can be. I think all that's necessary is to add support for arrow3d.",
    "created_at": "2009-08-12T00:10:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51826",
    "user": "wcauchois"
}
```

Replying to [comment:23 mpatel]:
> Quick questions:
>  * Should the default view angle for the new viewer match that for tachyon and jmol?

That's a good idea. I found a tuple called "orientation" in Graphics3d.export_jmol, so I think I can copy the values from that.

>  * Is it possible to enable axes?

Axes are not currently implemented, although they can be. I think all that's necessary is to add support for arrow3d.



---

archive/issue_comments_051827.json:
```json
{
    "body": "I think that axes are, perhaps, more important, since they give a sense of scale of a plot's \"landscape.\"\n\nBut I'm happy to defer to D. Joyner on reviewing this ticket. \n\nAnother question, possibly very naive:  Would it be less taxing on the browser to use \"quads\" instead of triangles as mesh elements, at least in some circumstances?",
    "created_at": "2009-08-17T06:57:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51827",
    "user": "mpatel"
}
```

I think that axes are, perhaps, more important, since they give a sense of scale of a plot's "landscape."

But I'm happy to defer to D. Joyner on reviewing this ticket. 

Another question, possibly very naive:  Would it be less taxing on the browser to use "quads" instead of triangles as mesh elements, at least in some circumstances?



---

archive/issue_comments_051828.json:
```json
{
    "body": "Replying to [comment:25 mpatel]:\n> I think that axes are, perhaps, more important, since they give a sense of scale of a plot's \"landscape.\"\n> \n> But I'm happy to defer to D. Joyner on reviewing this ticket. \n> \n> Another question, possibly very naive:  Would it be less taxing on the browser to use \"quads\" instead of triangles as mesh elements, at least in some circumstances?  \n\n\nWhen I gave this my positive review, I'm not saying that this patch is in it's final form. I'm sure that there are lots of improvements possible. But as a patch implementing an important new idea, it is excellent I think. The problem with me changing \"neds\" to \"positive\" is that I do not know javascript. William Stein said he would look this code over. But if someone else wants to (eg, mpatel) then I'm sure William won't mind:-)",
    "created_at": "2009-08-17T10:11:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51828",
    "user": "wdj"
}
```

Replying to [comment:25 mpatel]:
> I think that axes are, perhaps, more important, since they give a sense of scale of a plot's "landscape."
> 
> But I'm happy to defer to D. Joyner on reviewing this ticket. 
> 
> Another question, possibly very naive:  Would it be less taxing on the browser to use "quads" instead of triangles as mesh elements, at least in some circumstances?  


When I gave this my positive review, I'm not saying that this patch is in it's final form. I'm sure that there are lots of improvements possible. But as a patch implementing an important new idea, it is excellent I think. The problem with me changing "neds" to "positive" is that I do not know javascript. William Stein said he would look this code over. But if someone else wants to (eg, mpatel) then I'm sure William won't mind:-)



---

archive/issue_comments_051829.json:
```json
{
    "body": "wdj -- this looks good to me.  It doesn't have axes and \"everything\", but neither does tachyon.  But it provides new and *very* valuable functionality.",
    "created_at": "2009-08-29T05:58:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51829",
    "user": "was"
}
```

wdj -- this looks good to me.  It doesn't have axes and "everything", but neither does tachyon.  But it provides new and *very* valuable functionality.



---

archive/issue_comments_051830.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-30T07:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51830",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_051831.json:
```json
{
    "body": "Merged `trac_6447~rebase.patch`.",
    "created_at": "2009-08-30T07:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6447",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6447#issuecomment-51831",
    "user": "mvngu"
}
```

Merged `trac_6447~rebase.patch`.
