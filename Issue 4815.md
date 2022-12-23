# Issue 4815: list_plot3d is broken (segfaults, zero division errors)

Issue created by migration from https://trac.sagemath.org/ticket/4815

Original creator: was

Original creation time: 2008-12-16 16:37:42

Assignee: was

In sage-3.2.1 the following segfaults.  Fortunately, in sage-3.2.2.alpha2 it gives only a traceback (as given below):

```
sage: sage: X = list_plot3d([(1,1,1), (1,2,3), (1,2,5), (1,1,1)])
sage: sage: X.show(viewer='tachyon')
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)

/Users/was/build/sage-3.2.2.alpha2/<ipython console> in <module>()

/Users/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/plot/plot3d/base.so in sage.plot.plot3d.base.Graphics3d.show (sage/plot/plot3d/base.c:8436)()

/Users/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/plot/plot3d/base.so in sage.plot.plot3d.base.Graphics3d._prepare_for_tachyon (sage/plot/plot3d/base.c:5912)()

/Users/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/plot/plot3d/base.so in sage.plot.plot3d.base.Graphics3d._box_for_aspect_ratio (sage/plot/plot3d/base.c:6124)()

/Users/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/plot/plot3d/base.so in sage.plot.plot3d.base.Graphics3d._safe_bounding_box (sage/plot/plot3d/base.c:2743)()

/Users/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_surface.so in sage.plot.plot3d.parametric_surface.ParametricSurface.bounding_box (sage/plot/plot3d/parametric_surface.c:2133)()

/Users/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_surface.so in sage.plot.plot3d.parametric_surface.ParametricSurface.triangulate (sage/plot/plot3d/parametric_surface.c:2612)()

/Users/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_surface.so in sage.plot.plot3d.parametric_surface.triangulate (sage/plot/plot3d/parametric_surface.c:2551)()

/Users/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_surface.so in sage.plot.plot3d.parametric_surface.ParametricSurface.eval_grid (sage/plot/plot3d/parametric_surface.c:4108)()

/Users/was/build/sage-3.2.2.alpha2/local/lib/python2.5/site-packages/sage/plot/plot3d/list_plot3d.pyc in g(x, y)
    210         from parametric_surface import ParametricSurface
    211         def g(x,y):
--> 212             i=round( (x-xmin)/(xmax-xmin)*(num_points-1) )
    213             j=round( (y-ymin)/(ymax-ymin)*(num_points-1) )
    214             z=vals[int(j),int(i)]

ZeroDivisionError: float division
```


list_plot3d is supposed to work on *any* input, so this is a bug. 


---

Comment by was created at 2008-12-16 16:39:12

This is a dup of #4752.


---

Comment by was created at 2008-12-16 16:39:12

Resolution: duplicate


---

Comment by was created at 2008-12-16 16:48:52

I am re-opening this, since interestingly it isn't the same bug as is exposed by #4752's example.


---

Comment by was created at 2008-12-16 16:48:52

Changing status from closed to reopened.


---

Comment by was created at 2008-12-16 16:48:52

Resolution changed from duplicate to 


---

Comment by mabshoff created at 2009-02-15 07:16:40

Changing priority from major to blocker.


---

Comment by mabshoff created at 2009-02-15 07:16:40

Ok, this ticket was hiding in the dupe milestone and given it rather grisly nature of segfaulting Sage I am making it a blocker against 3.3.

Cheers,

Michael


---

Comment by mhansen created at 2009-02-19 11:28:28

The patch at #4752 keeps this from segfaulting, etc


```
sage: version()
'Sage Version 3.3.rc1, Release Date: 2009-02-16'
sage: sage: sage: X = list_plot3d([(1,1,1), (1,2,3), (1,2,5), (1,1,1)])
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/mhansen/.sage/temp/sage.math.washington.edu/28849/_home_mhansen__sage_init_sage_0.py in <module>()

/home/mhansen/sage-3.3.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/plot/plot3d/list_plot3d.pyc in list_plot3d(v, interpolation_type, texture, point_list, **kwds)
    189             return line3d(v, **kwds)
    190         elif isinstance(v[0],tuple) or point_list==True and len(v[0]) == 3:
--> 191             return list_plot3d_tuples(v,interpolation_type,texture=texture, **kwds)
    192         else:
    193             return list_plot3d_array_of_arrays(v, interpolation_type,texture, **kwds)

/home/mhansen/sage-3.3.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/plot/plot3d/list_plot3d.pyc in list_plot3d_tuples(v, interpolation_type, texture, **kwds)
    248             if x[i]==x[j] and y[i]==y[j]:
    249                 if z[i]!=z[j]:
--> 250                     raise ValueError, "Two points with same x,y coordinates and different z coordinates were given. Interpolation cannot handle this."
    251                 elif z[i]==z[j]:
    252                     drop_list.append(j)

ValueError: Two points with same x,y coordinates and different z coordinates were given. Interpolation cannot handle this.
```



---

Comment by mabshoff created at 2009-02-20 07:43:51

Ok, closing as fixed by #4752. Thanks Mike.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 07:43:51

Resolution: fixed
