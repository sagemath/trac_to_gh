# Issue 2604: plotting constant functions throws an error

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-03-19 19:47:42

Assignee: was


```
sage: plot(1,(x,-1,1))
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/grout/sage/devel/sage-main/sage/plot/<ipython console> in <module>()

/home/grout/sage/local/lib/python2.5/site-packages/IPython/Prompts.py in __call__(self, arg)
    521 
    522             # and now call a possibly user-defined print mechanism
--> 523             manipulated_val = self.display(arg)
    524             
    525             # user display hooks can change the variable to be stored in

/home/grout/sage/local/lib/python2.5/site-packages/IPython/Prompts.py in _display(self, arg)
    545         """
    546 
--> 547         return self.shell.hooks.result_display(arg)
    548 
    549     # Assign the default display method:

/home/grout/sage/local/lib/python2.5/site-packages/IPython/hooks.py in __call__(self, *args, **kw)
    132             #print "prio",prio,"cmd",cmd #dbg
    133             try:
--> 134                 ret = cmd(*args, **kw)
    135                 return ret
    136             except ipapi.TryNext, exc:

/home/grout/sage/local/lib/python2.5/site-packages/IPython/hooks.py in result_display(self, arg)
    160     
    161     if self.rc.pprint:
--> 162         out = pformat(arg)
    163         if '\n' in out:
    164             # So that multi-line strings line up with the left column of

/home/grout/sage/local/lib/python2.5/pprint.py in pformat(self, object)
    109     def pformat(self, object):
    110         sio = _StringIO()
--> 111         self._format(object, sio, 0, 0, {}, 0)
    112         return sio.getvalue()
    113 

/home/grout/sage/local/lib/python2.5/pprint.py in _format(self, object, stream, indent, allowance, context, level)
    127             self._readable = False
    128             return
--> 129         rep = self._repr(object, context, level - 1)
    130         typ = _type(object)
    131         sepLines = _len(rep) > (self._width - 1 - indent - allowance)

/home/grout/sage/local/lib/python2.5/pprint.py in _repr(self, object, context, level)
    193     def _repr(self, object, context, level):
    194         repr, readable, recursive = self.format(object, context.copy(),
--> 195                                                 self._depth, level)
    196         if not readable:
    197             self._readable = False

/home/grout/sage/local/lib/python2.5/pprint.py in format(self, object, context, maxlevels, level)
    205         and whether the object represents a recursive construct.
    206         """
--> 207         return _safe_repr(object, context, maxlevels, level)
    208 
    209 

/home/grout/sage/local/lib/python2.5/pprint.py in _safe_repr(object, context, maxlevels, level)
    290         return format % _commajoin(components), readable, recursive
    291 
--> 292     rep = repr(object)
    293     return rep, (rep and not rep.startswith('<')), False
    294 

/home/grout/sage/devel/sage-main/sage/plot/base.pyx in sage.plot.plot3d.base.Graphics3d.__repr__()

/home/grout/sage/devel/sage-main/sage/plot/base.pyx in sage.plot.plot3d.base.Graphics3d.show()

/home/grout/sage/devel/sage-main/sage/plot/base.pyx in sage.plot.plot3d.base.Graphics3d._prepare_for_jmol()

/home/grout/sage/devel/sage-main/sage/plot/base.pyx in sage.plot.plot3d.base.Graphics3d._box_for_aspect_ratio()

/home/grout/sage/devel/sage-main/sage/plot/base.pyx in sage.plot.plot3d.base.Graphics3d._safe_bounding_box()

/home/grout/sage/devel/sage-main/sage/plot/base.pyx in sage.plot.plot3d.base.TransformGroup.bounding_box()

/home/grout/sage/devel/sage-main/sage/plot/base.pyx in sage.plot.plot3d.base.TransformGroup.get_transformation()

/home/grout/sage/devel/sage-main/sage/plot/transform.pyx in sage.plot.plot3d.transform.Transformation.__init__()

/home/grout/sage/local/lib/python2.5/site-packages/sage/matrix/constructor.py in matrix(arg0, arg1, arg2, arg3, sparse)
    454         sparse = False
    455 
--> 456     return matrix_space.MatrixSpace(ring, nrows, ncols, sparse=sparse)(entries)
    457 
    458 

/home/grout/sage/local/lib/python2.5/site-packages/sage/matrix/matrix_space.py in __call__(self, entries, coerce, copy, rows)
    352             return self(entries.matrix(), copy=False)
    353 
--> 354         return self.matrix(entries, copy=copy, coerce=coerce, rows=rows)
    355 
    356     def change_ring(self, R):

/home/grout/sage/local/lib/python2.5/site-packages/sage/matrix/matrix_space.py in matrix(self, x, coerce, copy, rows)
    965                 x = new_x
    966             
--> 967         return self.__matrix_class(self, entries=x, copy=copy, coerce=coerce) 
    968      
    969     def matrix_space(self, nrows=None, ncols=None, sparse=False):

/home/grout/sage/devel/sage-main/sage/plot/matrix_real_double_dense.pyx in sage.matrix.matrix_real_double_dense.Matrix_real_double_dense.__init__()

<type 'exceptions.TypeError'>: float() argument must be a string or a number
```




---

Comment by mabshoff created at 2008-04-08 12:49:56

Resolution: duplicate


---

Comment by mabshoff created at 2008-04-08 12:49:56

This is a duplicate of #2409.

Cheers,

Michael
