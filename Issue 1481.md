# Issue 1481: showing a matrix plot blows up

Issue created by migration from https://trac.sagemath.org/ticket/1481

Original creator: jason

Original creation time: 2007-12-12 19:51:52

Assignee: was

CC:  kcrisman


```
sage: m=matrix(ZZ,1,[16]); m
[16]
sage: matrix_plot(m^10).show()
---------------------------------------------------------------------------
<type 'exceptions.OverflowError'>         Traceback (most recent call last)

/home/grout/.sage/<ipython console> in <module>()

/home/grout/sage/local/lib/python2.5/site-packages/sage/plot/plot.py in show(self, xmin, xmax, ymin, ymax, figsize, filename, dpi, axes, axes_label, frame, fontsize, **args)
    654         if filename is None:
    655             filename = sage.misc.misc.tmp_filename() + '.png'
--> 656         self.save(filename, xmin, xmax, ymin, ymax, figsize, dpi=dpi, axes=axes,frame=frame, fontsize=fontsize)
    657         os.system('%s %s 2>/dev/null 1>/dev/null &'%(sage.misc.viewer.browser(), filename))
    658

/home/grout/sage/local/lib/python2.5/site-packages/sage/plot/plot.py in save(self, filename, xmin, xmax, ymin, ymax, figsize, figure, sub, savenow, dpi, axes, axes_label, fontsize, frame, verify)
    766             if isinstance(g, GraphicPrimitive_MatrixPlot):
    767                 matrixplot = True
--> 768             g._render_on_subplot(subplot)
    769
    770         #adjust the xy limits and draw the axes:

/home/grout/sage/local/lib/python2.5/site-packages/sage/plot/plot.py in _render_on_subplot(self, subplot)
   1102             print "The possible color maps include: %s"%possibilities
   1103             raise RuntimeError, "Color map %s not known"%cmap
-> 1104         subplot.imshow(self.xy_data_array, cmap=cmap, interpolation='nearest')
   1105
   1106 # Below is the base class that is used to make 'field plots'.

/home/grout/sage/local/lib/python2.5/site-packages/matplotlib/axes.py in imshow(self, X, cmap, norm, aspect, interpolation, alpha, vmin, vmax, origin, extent, shape, filternorm, filterrad, imlim, **kwargs)
   4053                        filterrad=filterrad, **kwargs)
   4054
-> 4055         im.set_data(X)
   4056         im.set_alpha(alpha)
   4057         self._set_artist_props(im)

/home/grout/sage/local/lib/python2.5/site-packages/matplotlib/image.py in set_data(self, A, shape)
    224             or X.shape[2] > 4
    225             or X.shape[2] < 3):
--> 226             cm.ScalarMappable.set_array(self, X)
    227         else:
    228             self._A = X

/home/grout/sage/local/lib/python2.5/site-packages/matplotlib/cm.py in set_array(self, A)
     65             self._A = A.astype(nx.Float32)
     66         else:
---> 67             self._A = A.astype(nx.Int16)
     68
     69     def get_array(self):

/home/grout/sage/local/lib/python2.5/site-packages/numpy/core/ma.py in astype(self, tc)
   1148     def astype (self, tc):
   1149         "return self as array of given type."
-> 1150         d = self._data.astype(tc)
   1151         return array(d, mask=self._mask)
   1152

<type 'exceptions.OverflowError'>: long int too large to convert to int
```



---

Comment by jason created at 2007-12-12 19:52:01

Changing component from algebraic geometry to linear algebra.


---

Comment by jason created at 2008-01-19 07:22:03

This seems to work in 2.9.3:


```
sage: m=matrix(ZZ,1,[16]); m
[16]
sage: matrix_plot(m^100).show()
sage: 
```


I do get this warning:


```
sage: matrix_plot(m^1000).show()
Warning: invalid value encountered in multiply
```


but the image shows up (a giant black square, just like it should).


---

Comment by jason created at 2008-01-19 07:22:03

Resolution: fixed


---

Comment by mabshoff created at 2008-01-19 07:26:34

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-01-19 07:26:34

Resolution changed from fixed to 


---

Comment by mabshoff created at 2008-01-19 07:26:34

Ok, but we should still add a doctest to catch this behavior. It can be `#long`, but I will reopen this for now until the doctest is added [which is standard requirement to close bugs these days :)]

Cheers,

Michael


---

Comment by jason created at 2008-01-28 17:50:19

Thanks for reopening this.  The following code displays the wrong plot:


```
a=matrix(2,[16^1000,0,0,-16^1000]);
matrix_plot(a)
```


What should be displayed is the same as the plot:


```
a=matrix(2,[16,0,0,-16]);
matrix_plot(a)
```


So the matrix plot has gone from blowing up to just being wrong.  Whether this is worse or better is left as an exercise for the reader.


---

Comment by jason created at 2008-01-28 18:51:18

I think this problem is a matplotlib problem and has to do with not dealing with inf or -inf in the matrix.  We could send vmin and vmax parameters to the imshow command to scale the matrix manually if we see an infinity in the matrix, or we could raise an exception, or we could report the bug back up to matplotlib (if it is indeed a matplotlib issue).


---

Attachment

this should completely deal with the dense case.


---

Comment by jason created at 2010-12-22 08:14:46

Changing status from new to needs_review.


---

Comment by jason created at 2010-12-22 08:15:07

Changing component from linear algebra to graphics.


---

Comment by jason created at 2011-01-11 16:51:23

Whoever referees this patch should make sure it works well with the norm, vmin, and vmax parameters in matrix_plot


---

Comment by jason created at 2011-01-11 16:54:31

On the surface, it doesn't appear that the patch works with norm, vmin, and vmax, probably because the patch was written before we added those parameters.


---

Comment by kcrisman created at 2011-03-12 04:31:02

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2011-03-12 04:31:02

Does not apply to 4.7.alpha1 in any case.  Needs work - though, impressively, only one hunk failed. Not bad for a patch over a year old.


---

Comment by dsm created at 2012-05-25 21:22:16

The original patch doesn't seem to work at the moment (the numpy array created has dtype=object, so the integers stay as integers instead of becoming floats, so there are no infs to work around).  I have a variant which works, and modified it to handle vmin and vmax, but I'm not sure what to do with norm: should the norm be applied before or after the vmin/vmax?
