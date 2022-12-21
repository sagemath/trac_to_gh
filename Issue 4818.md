# Issue 4818: bug in list_plot3d -- invalid index?

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-17 06:54:47

Assignee: was


```
sage: v = list_plot3d([(1,2,3)]).show(viewer="tachyon")
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/home/wstein/<ipython console> in <module>()

/home/wstein/sage/local/lib/python2.5/site-packages/sage/plot/plot3d/list_plot3d.pyc in list_plot3d(v, interpolation_type, texture, point_list, **kwds)
    124             return Graphics3d()
    125         elif isinstance(v[0],tuple) or point_list==True and len(v[0]) == 3:
--> 126             return list_plot3d_tuples(v,interpolation_type,texture=texture, **kwds)
    127         else:
    128             return list_plot3d_array_of_arrays(v, interpolation_type,texture, **kwds)

/home/wstein/sage/local/lib/python2.5/site-packages/sage/plot/plot3d/list_plot3d.pyc in list_plot3d_tuples(v, interpolation_type, texture, **kwds)
    222     if interpolation_type == 'nn'  or interpolation_type =='default':
    223 
--> 224         T=delaunay.Triangulation(x,y)
    225         f=T.nn_interpolator(z)
    226         f.default_value=0.0

/home/wstein/sage/local/lib/python2.5/site-packages/delaunay/triangulate.pyc in __init__(self, x, y)
     66             self.triangle_neighbors = delaunay(self.x, self.y)
     67 
---> 68         self.hull = self._compute_convex_hull()
     69 
     70     def _compute_convex_hull(self):

/home/wstein/sage/local/lib/python2.5/site-packages/delaunay/triangulate.pyc in _compute_convex_hull(self)
     77 
     78         edges = {}
---> 79         edges.update(dict(zip(self.triangle_nodes[border[:,0]][:,1],
     80                               self.triangle_nodes[border[:,0]][:,2])))
     81         edges.update(dict(zip(self.triangle_nodes[border[:,1]][:,2],

IndexError: invalid index

```



---

Comment by was created at 2009-01-22 13:42:52

The attached patch fixes the reported bug by special casing the case of 1 or 2 input points by plotting a point or a line instead of a surface.  (Note that there are other bugs in list_plot3d that this patch doesn't fix.)


---

Attachment

This does what it is supposed and has very sensible behaviour for the case of one or two points.


---

Comment by robertwb created at 2009-01-23 03:53:35

+1 from me too. I need to get quicker at reviewing these things...


---

Comment by mabshoff created at 2009-01-23 09:39:49

Merged in Sage 3.3.alpha1

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-23 09:39:49

Resolution: fixed
