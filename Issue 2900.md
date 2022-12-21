# Issue 2900: matplotlib bug in imshow (probably fixed in new version)

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-04-12 16:22:28

Assignee: mabshoff

CC:  jhpalmieri jason

Sage's current version of matplotlib has a bug, as reported by Fabio Tonti (http://groups.google.com/group/sage-support/browse_thread/thread/a41e9ab2b158c41e#):

```
sage: from pylab import *
sage: imshow([This is the Trac macro ** that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#-macro) called with arguments (0,0,0))
sage: savefig('foo.png')
Traceback (most recent call last):
...
NameError: global name 'npy' is not defined 
```

It looks like this bug has been fixed in 0.91.2 (although I haven't actually tried it); we should upgrade.


---

Comment by mabshoff created at 2008-12-02 02:32:23

This still fails with Sage 3.2.1.rc1 (which ships with matplotlib 0.98.3):

```
sage: savefig('foo.png')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/scratch/mabshoff/release-cycle/sage-3.2.1.final/<ipython console> in <module>()

/scratch/mabshoff/release-cycle/sage-3.2.1.final/local/lib/python2.5/site-packages/matplotlib/pyplot.pyc in savefig(*args, **kwargs)
    340 def savefig(*args, **kwargs):
    341     fig = gcf()
--> 342     return fig.savefig(*args, **kwargs)
    343 if Figure.savefig.__doc__ is not None:
    344     savefig.__doc__ = dedent(Figure.savefig.__doc__)

/scratch/mabshoff/release-cycle/sage-3.2.1.final/local/lib/python2.5/site-packages/matplotlib/figure.pyc in savefig(self, *args, **kwargs)
    962                 patch.set_alpha(0.0)
    963 
--> 964         self.canvas.print_figure(*args, **kwargs)
    965 
    966         if transparent:

/scratch/mabshoff/release-cycle/sage-3.2.1.final/local/lib/python2.5/site-packages/matplotlib/backend_bases.pyc in print_figure(self, filename, dpi, facecolor, edgecolor, orientation, format, **kwargs)
   1308                 edgecolor=edgecolor,
   1309                 orientation=orientation,
-> 1310                 **kwargs)
   1311         finally:
   1312             self.figure.dpi = origDPI

/scratch/mabshoff/release-cycle/sage-3.2.1.final/local/lib/python2.5/site-packages/matplotlib/backends/backend_agg.pyc in print_png(self, filename_or_obj, *args, **kwargs)
    303 
    304     def print_png(self, filename_or_obj, *args, **kwargs):
--> 305         FigureCanvasAgg.draw(self)
    306         renderer = self.get_renderer()
    307         original_dpi = renderer.dpi

/scratch/mabshoff/release-cycle/sage-3.2.1.final/local/lib/python2.5/site-packages/matplotlib/backends/backend_agg.pyc in draw(self)
    259 
    260         self.renderer = self.get_renderer()
--> 261         self.figure.draw(self.renderer)
    262 
    263     def get_renderer(self):

/scratch/mabshoff/release-cycle/sage-3.2.1.final/local/lib/python2.5/site-packages/matplotlib/figure.pyc in draw(self, renderer)
    757 
    758         # render the axes
--> 759         for a in self.axes: a.draw(renderer)
    760 
    761         # render the figure text

/scratch/mabshoff/release-cycle/sage-3.2.1.final/local/lib/python2.5/site-packages/matplotlib/axes.pyc in draw(self, renderer, inframe)
   1463         if len(self.images)<=1 or renderer.option_image_nocomposite():
   1464             for im in self.images:
-> 1465                 im.draw(renderer)
   1466         else:
   1467             # make a composite image blending alpha

/scratch/mabshoff/release-cycle/sage-3.2.1.final/local/lib/python2.5/site-packages/matplotlib/image.pyc in draw(self, renderer, *args, **kwargs)
    234             self.axes.get_yscale() != 'linear'):
    235             warnings.warn("Images are not supported on non-linear axes.")
--> 236         im = self.make_image(renderer.get_image_magnification())
    237         l, b, widthDisplay, heightDisplay = self.axes.bbox.bounds
    238         renderer.draw_image(round(l), round(b), im, self.axes.bbox.frozen(),

/scratch/mabshoff/release-cycle/sage-3.2.1.final/local/lib/python2.5/site-packages/matplotlib/image.pyc in make_image(self, magnification)
    185                 else:
    186                     x = self._rgbacache
--> 187                 im = _image.fromarray(x[yslice,xslice], 0)
    188                 if len(self._A.shape) == 2:
    189                     im.is_grayscale = self.cmap.is_gray()

ValueError: Array must be rank 2 or 3 of doubles
sage: 
Exiting SAGE (CPU time 0m1.32s, Wall time 0m43.85s).
```


Cheers,

Michael


---

Comment by kcrisman created at 2009-09-15 17:30:53

To release manager:
This is now fixed, given #5448 (and perhaps long before that):

```
sage: from pylab import *
sage: imshow([This is the Trac macro ** that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#-macro) called with arguments (0,0,0))
<matplotlib.image.AxesImage object at 0xa50f190>
sage: savefig('foo.png')
```

foo.png is attached.


---

Attachment


---

Comment by kcrisman created at 2009-09-29 14:40:39

Depends on #7059


---

Attachment

The patch verifies this is fixed, and uses the new (better) syntax from #7059.


---

Comment by jason created at 2009-09-29 20:31:29

Thanks for making a doctest patch.


---

Comment by mhansen created at 2009-10-15 05:23:42

Resolution: fixed
