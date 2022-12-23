# Issue 2741: Implement mesh lines in 3d plots

Issue created by migration from https://trac.sagemath.org/ticket/2741

Original creator: jason

Original creation time: 2008-03-31 18:19:49

Assignee: was

CC:  timothyclemans

> >  Is there an easy way to get mesh lines in a plot3d surface?

This is not implemented.  I wish you would implement it  :-) 

Robert Bradshaw might have some useful advise.

> > Sometimes
> >  it is hard to visualize the plot (especially when it is printed) without
> >  the mesh lines.
> >
> >  If that is easy, what about the possibility of doing some of things that
> >  Mma does with different types of meshes?  For reference, see:
> >
> >  http://reference.wolfram.com/mathematica/ref/Mesh.html
> >
> >  http://reference.wolfram.com/mathematica/ref/MeshFunctions.html
> >
> >  http://reference.wolfram.com/mathematica/ref/MeshShading.html
> >
> >  http://reference.wolfram.com/mathematica/ref/MeshStyle.html
> >


---

Comment by jason created at 2008-03-31 18:34:40

Well, he already answered my question in the source.

In sage/sage/plot/plot3d/index_set.pyx, starting at line 658 (in 2.10.4):

```
        # If we wanted to turn on display of the mesh lines or dots
        # we would uncomment thse.  This should be determined by
        # render_params, probably. 
        #s += '\npmesh %s mesh\n'%name
        #s += '\npmesh %s dots\n'%name
```


Uncommenting the appropriate line does indeed give a mesh in JMOL.  So now the question is how to expose this to the user.  And how to extend it to do nontrivial mesh functions.


---

Attachment


---

Comment by TimothyClemans created at 2008-04-30 05:39:41

fixes doctest failures


---

Attachment

Impressive plots with mesh lines! There were two doctest failures I fixed them and uploaded a patch.


---

Comment by mabshoff created at 2008-04-30 05:47:27

Timothy's patch looks good to me. Somebody didn't doctest his own patch ;)

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-30 05:47:48

Merger in Sage 3.0.1.alpha1


---

Comment by mabshoff created at 2008-04-30 05:47:48

Resolution: fixed
