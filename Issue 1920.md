# Issue 1920: 3d graphics -- constant plot3d's

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-25 05:59:46

Assignee: was

CC:  mhansen cwitty jason

This works:

```
var('x,y')
plot3d(0, (x,-1,1), (y,-1,1))
```


This doesn't:

```
plot3d(0, (-1,1), (-1,1))
```


It seems completely reasonable that we fix the above so it does.


---

Comment by mabshoff created at 2008-08-27 01:03:03

This is still an issue with all the plot fixes in Sage 3.1.2.alpha1:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.2.alpha0, Release Date: 2008-08-22                |
| Type notebook() for the GUI, and license() for information.        |
sage: plot3d(0, (-1,1), (-1,1))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/<ipython console> in <module>()

/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/local/lib/python2.5/site-packages/IPython/Prompts.py in __call__(self, arg)
    533 
    534             # and now call a possibly user-defined print mechanism
--> 535             manipulated_val = self.display(arg)
    536             
    537             # user display hooks can change the variable to be stored in

/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/local/lib/python2.5/site-packages/IPython/Prompts.py in _display(self, arg)
    559             return IPython.generics.result_display(arg)
    560         except TryNext:            
--> 561             return self.shell.hooks.result_display(arg)
    562 
    563     # Assign the default display method:

/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/local/lib/python2.5/site-packages/IPython/hooks.py in __call__(self, *args, **kw)
    132             #print "prio",prio,"cmd",cmd #dbg
    133             try:
--> 134                 ret = cmd(*args, **kw)
    135                 return ret
    136             except ipapi.TryNext, exc:

/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/local/lib/python2.5/site-packages/IPython/hooks.py in result_display(self, arg)
    160     
    161     if self.rc.pprint:
--> 162         out = pformat(arg)
    163         if '\n' in out:
    164             # So that multi-line strings line up with the left column of

/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/local/lib/python2.5/pprint.py in pformat(self, object)
    109     def pformat(self, object):
    110         sio = _StringIO()
--> 111         self._format(object, sio, 0, 0, {}, 0)
    112         return sio.getvalue()
    113 

/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/local/lib/python2.5/pprint.py in _format(self, object, stream, indent, allowance, context, level)
    127             self._readable = False
    128             return
--> 129         rep = self._repr(object, context, level - 1)
    130         typ = _type(object)
    131         sepLines = _len(rep) > (self._width - 1 - indent - allowance)

/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/local/lib/python2.5/pprint.py in _repr(self, object, context, level)
    193     def _repr(self, object, context, level):
    194         repr, readable, recursive = self.format(object, context.copy(),
--> 195                                                 self._depth, level)
    196         if not readable:
    197             self._readable = False

/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/local/lib/python2.5/pprint.py in format(self, object, context, maxlevels, level)
    205         and whether the object represents a recursive construct.
    206         """
--> 207         return _safe_repr(object, context, maxlevels, level)
    208 
    209 

/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/local/lib/python2.5/pprint.py in _safe_repr(object, context, maxlevels, level)
    290         return format % _commajoin(components), readable, recursive
    291 
--> 292     rep = repr(object)
    293     return rep, (rep and not rep.startswith('<')), False
    294 

/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/base.pyx in sage.plot.plot3d.base.Graphics3d.__repr__ (sage/plot/plot3d/base.c:1819)()

/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/base.pyx in sage.plot.plot3d.base.Graphics3d.show (sage/plot/plot3d/base.c:8472)()

/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/base.pyx in sage.plot.plot3d.base.Graphics3d._prepare_for_jmol (sage/plot/plot3d/base.c:5321)()

/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/base.pyx in sage.plot.plot3d.base.Graphics3d._box_for_aspect_ratio (sage/plot/plot3d/base.c:5756)()

/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/base.pyx in sage.plot.plot3d.base.Graphics3d._safe_bounding_box (sage/plot/plot3d/base.c:2561)()

/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/parametric_surface.pyx in sage.plot.plot3d.parametric_surface.ParametricSurface.bounding_box (sage/plot/plot3d/parametric_surface.c:2096)()

/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/parametric_surface.pyx in sage.plot.plot3d.parametric_surface.ParametricSurface.triangulate (sage/plot/plot3d/parametric_surface.c:2555)()

/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/parametric_surface.pyx in sage.plot.plot3d.parametric_surface.triangulate (sage/plot/plot3d/parametric_surface.c:2497)()

/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1/parametric_surface.pyx in sage.plot.plot3d.parametric_surface.ParametricSurface.eval_grid (sage/plot/plot3d/parametric_surface.c:3916)()

TypeError: 'sage.rings.integer.Integer' object is not callable
sage: 
Exiting SAGE (CPU time 0m1.16s, Wall time 0m27.83s).
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha1$ 
```


Cheers,

Michael


---

Comment by AlexGhitza created at 2009-01-22 18:27:42

Changing type from defect to enhancement.


---

Comment by kcrisman created at 2010-07-27 17:30:47

Do we still want this?  We've been spending a lot of time making sure people declare their variables.  On the other hand, for a constant function this may not be an issue :)


---

Comment by jason created at 2010-07-27 23:37:51

Yes, it seems to make sense to make this work, doesn't it? (a constant function should take any number of parameters and return the constant, right?).  Hopefully my recent (in-progress) revamping of fast_callable will take care of this.  It's probably even easier just to fix this.


---

Comment by kcrisman created at 2012-07-07 03:53:11

This does, in fact, now work.

```
sage: plot3d(pi, (-1,1), (-1,1))
```

I can't figure out quite which upgrade did it, though I found several possible suspects.


---

Attachment

Apply [attachment:trac_1920-verify.patch].  I couldn't find a better place to add this... and if someone knows that this is already tested, please let me know.  I did a grep through the Sage library for plotting the 0 function, but of course if it is more like my test, then one could never find it.


---

Comment by kcrisman created at 2012-07-07 03:55:00

Changing status from new to needs_review.


---

Comment by ppurka created at 2012-11-16 09:16:01

This should have been merged long ago.


---

Comment by ppurka created at 2012-11-16 09:16:01

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-12-18 11:17:16

Resolution: fixed
