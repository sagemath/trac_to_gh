# Issue 2476: 3d plotting -- easy to fix bug?

Issue created by migration from https://trac.sagemath.org/ticket/2476

Original creator: was

Original creation time: 2008-03-11 23:11:43

Assignee: was


```
sage: g = Graph({1:[1,2]}, loops=True)
sage: g.plot3d()
---------------------------------------------------------------------------
<type 'exceptions.ZeroDivisionError'>     Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/site-packages/IPython/Prompts.py in __call__(self, arg)
    521 
    522             # and now call a possibly user-defined print mechanism
--> 523             manipulated_val = self.display(arg)
    524             
    525             # user display hooks can change the variable to be stored in

/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/site-packages/IPython/Prompts.py in _display(self, arg)
    545         """
    546 
--> 547         return self.shell.hooks.result_display(arg)
    548 
    549     # Assign the default display method:

/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/site-packages/IPython/hooks.py in __call__(self, *args, **kw)
    132             #print "prio",prio,"cmd",cmd #dbg
    133             try:
--> 134                 ret = cmd(*args, **kw)
    135                 return ret
    136             except ipapi.TryNext, exc:

/Users/was/build/sage-2.10.3.rc3/local/lib/python2.5/site-packages/IPython/hooks.py in result_display(self, arg)
    160     
    161     if self.rc.pprint:
--> 162         out = pformat(arg)
    163         if '\n' in out:
    164             # So that multi-line strings line up with the left column of

/Users/was/build/sage-2.10.3.rc3/local/lib/python/pprint.py in pformat(self, object)
    109     def pformat(self, object):
    110         sio = _StringIO()
--> 111         self._format(object, sio, 0, 0, {}, 0)
    112         return sio.getvalue()
    113 

/Users/was/build/sage-2.10.3.rc3/local/lib/python/pprint.py in _format(self, object, stream, indent, allowance, context, level)
    127             self._readable = False
    128             return
--> 129         rep = self._repr(object, context, level - 1)
    130         typ = _type(object)
    131         sepLines = _len(rep) > (self._width - 1 - indent - allowance)

/Users/was/build/sage-2.10.3.rc3/local/lib/python/pprint.py in _repr(self, object, context, level)
    193     def _repr(self, object, context, level):
    194         repr, readable, recursive = self.format(object, context.copy(),
--> 195                                                 self._depth, level)
    196         if not readable:
    197             self._readable = False

/Users/was/build/sage-2.10.3.rc3/local/lib/python/pprint.py in format(self, object, context, maxlevels, level)
    205         and whether the object represents a recursive construct.
    206         """
--> 207         return _safe_repr(object, context, maxlevels, level)
    208 
    209 

/Users/was/build/sage-2.10.3.rc3/local/lib/python/pprint.py in _safe_repr(object, context, maxlevels, level)
    290         return format % _commajoin(components), readable, recursive
    291 
--> 292     rep = repr(object)
    293     return rep, (rep and not rep.startswith('<')), False
    294 

/Users/was/base.pyx in sage.plot.plot3d.base.Graphics3d.__repr__()

/Users/was/base.pyx in sage.plot.plot3d.base.Graphics3d.show()

/Users/was/base.pyx in sage.plot.plot3d.base.Graphics3d.export_jmol()

/Users/was/base.pyx in sage.plot.plot3d.base.TransformGroup.jmol_repr()

/Users/was/base.pyx in sage.plot.plot3d.base.TransformGroup.jmol_repr()

/Users/was/base.pyx in sage.plot.plot3d.base.Graphics3dGroup.jmol_repr()

/Users/was/base.pyx in sage.plot.plot3d.base.TransformGroup.jmol_repr()

/Users/was/shapes.pyx in sage.plot.plot3d.shapes.Cylinder.jmol_repr()

<type 'exceptions.ZeroDivisionError'>: float division

```



---

Comment by mhansen created at 2009-06-04 21:26:30

This ticket is now invalid:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: sage: g = Graph({1:[1,2]}, loops=True)
sage: sage: g.plot3d()
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
| Sage Version 4.0.1.rc1, Release Date: 2009-06-04                   |
| Type notebook() for the GUI, and license() for information.        |
/home/mhansen/.sage/temp/sage.math.washington.edu/21917/_home_mhansen__sage_init_sage_0.py in <module>()

/scratch/mhansen/release/4.0.1/rc1/sage-4.0.1.rc1/local/lib/python2.5/site-packages/sage/graphs/graph.pyc in plot3d(self, bgcolor, vertex_colors, vertex_size, edge_colors, edge_size, edge_size2, pos3d, iterations, color_by_label, engine, **kwds)
   6617         """
   6618         if self.has_multiple_edges() or self.has_loops():
-> 6619             raise NotImplementedError("3D plotting of multiple edges or loops not implemented.")
   6620         if engine == 'jmol':
   6621             from sage.plot.plot3d.all import sphere, line3d, arrow3d

NotImplementedError: 3D plotting of multiple edges or loops not implemented.
```



---

Comment by mhansen created at 2009-06-04 21:26:30

Resolution: invalid
