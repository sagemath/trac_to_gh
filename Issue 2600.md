# Issue 2600: vector plot throws error when function contains a float

Issue created by migration from https://trac.sagemath.org/ticket/2600

Original creator: jason

Original creation time: 2008-03-19 18:59:44

Assignee: was


```
sage: var('y')
y
sage: plot_vector_field((lambda x,y: .01*x,x+y), (-10,10), (-10,10))
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/home/grout/<ipython console> in <module>()

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

/home/grout/sage_object.pyx in sage.structure.sage_object.SageObject.__repr__()

/home/grout/sage/local/lib/python2.5/site-packages/sage/plot/plot.py in _repr_(self)
    736         """
    737         if SHOW_DEFAULT:
--> 738             self.show()
    739             return ''
    740         else:

/home/grout/sage/local/lib/python2.5/site-packages/sage/plot/plot.py in show(self, xmin, xmax, ymin, ymax, figsize, filename, dpi, axes, axes_labels, frame, fontsize, aspect_ratio)
   1250         self.save(filename, xmin, xmax, ymin, ymax, figsize, dpi=dpi, axes=axes,
   1251                   frame=frame, fontsize=fontsize,
-> 1252                   aspect_ratio=aspect_ratio)
   1253         os.system('%s %s 2>/dev/null 1>/dev/null &'%(sage.misc.viewer.browser(), filename))
   1254 

/home/grout/sage/local/lib/python2.5/site-packages/sage/plot/plot.py in save(self, filename, xmin, xmax, ymin, ymax, figsize, figure, sub, savenow, dpi, axes, axes_labels, fontsize, frame, verify, aspect_ratio)
   1462             else:
   1463                 raise ValueError, "file extension must be either 'png', 'ps, 'eps', 'pdf, 'svg' or 'sobj'"
-> 1464             canvas.print_figure(filename, dpi=dpi)
   1465 
   1466 ################## Graphics Primitives ################

/home/grout/sage/local/lib/python2.5/site-packages/matplotlib/backend_bases.py in print_figure(self, filename, dpi, facecolor, edgecolor, orientation, format, **kwargs)
   1200             self.figure.set_edgecolor(origedgecolor)
   1201             self.figure.set_canvas(self)
-> 1202             self.figure.canvas.draw()
   1203             
   1204         return result

/home/grout/sage/local/lib/python2.5/site-packages/matplotlib/backends/backend_agg.py in draw(self)
    378 
    379         self.renderer = self.get_renderer()
--> 380         self.figure.draw(self.renderer)
    381 
    382     def get_renderer(self):

/home/grout/sage/local/lib/python2.5/site-packages/matplotlib/figure.py in draw(self, renderer)
    610 
    611         # render the axes
--> 612         for a in self.axes: a.draw(renderer)
    613 
    614         # render the figure text

/home/grout/sage/local/lib/python2.5/site-packages/matplotlib/axes.py in draw(self, renderer, inframe)
   1342 
   1343         for zorder, i, a in dsu:
-> 1344             a.draw(renderer)
   1345 
   1346         self.transData.thaw()  # release the lazy objects

/home/grout/sage/local/lib/python2.5/site-packages/matplotlib/quiver.py in draw(self, renderer)
    334         self._init()
    335         if self._new_UV:
--> 336             verts = self._make_verts(self.U, self.V)
    337             # Using nan internally here is the easiest
    338             # way to support masked inputs; it doesn't

/home/grout/sage/local/lib/python2.5/site-packages/matplotlib/quiver.py in _make_verts(self, U, V)
    389         # a masked array with one element converts it to
    390         # an ndarray.
--> 391         theta = npy.angle(ma.asarray(uv[..., npy.newaxis]).filled(0))
    392         xy = (X+Y*1j) * npy.exp(1j*theta)*self.width
    393         xy = xy[:,:,npy.newaxis]

/home/grout/sage/local/lib/python2.5/site-packages/numpy/lib/function_base.py in angle(z, deg)
    694         zimag = 0
    695         zreal = z
--> 696     return arctan2(zimag, zreal) * fact
    697 
    698 def unwrap(p, discont=pi, axis=-1):

<type 'exceptions.AttributeError'>: 'int' object has no attribute 'arctan2'
```




---

Attachment

The attached patch fixes the bug and adds a doctest for it.  Tests pass in plot.py .


---

Comment by jason created at 2008-03-25 21:48:37

looks good to me.  Thanks!


---

Comment by mabshoff created at 2008-03-26 00:02:34

Resolution: fixed


---

Comment by mabshoff created at 2008-03-26 00:02:34

Merged in Sage 2.11.alpha2
