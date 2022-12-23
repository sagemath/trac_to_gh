# Issue 9956: Parametric Surfaces don't load well

Issue created by migration from https://trac.sagemath.org/ticket/9957

Original creator: kcrisman

Original creation time: 2010-09-20 19:32:42

Assignee: jason, was

See [this ask.sagemath.org](http://ask.sagemath.org/question/136/importing-saved-3d-plot) discussion for background.  Basically,

```
sage: var('x,y')
(x, y)
sage: f(x,y)=x^2+y^2
sage: p=plot3d(f,(-5,5),(-5,5))
sage: p # works fine
sage: p.save('test.sobj')
sage: q = load('test.sobj')
sage: q
ERROR: An unexpected error occurred while tokenizing input
```



---

Comment by kcrisman created at 2010-09-20 19:43:17

This can be traced down to the fact that in `parametric_surface.pyx` 

```
    def get_grid(self, ds):
        """
        TEST::

            sage: from sage.plot.plot3d.parametric_surface import ParametricSurface
            sage: def f(x,y): return x+y,x-y,x*y
            sage: P = ParametricSurface(f)
            sage: P.get_grid(.1)
            Traceback (most recent call last):
            ...
            NotImplementedError: You must override the get_grid method.
        """
        if self.render_grid is None:
            raise NotImplementedError, "You must override the get_grid method."
        return self.render_grid
```

which is called from `triangulate` when you try to view the plot.  For some reason the `render_grid` attribute isn't set in `q`, but in `p` it is.  I don't know how to access these attributes, unfortunately...


---

Comment by nbruin created at 2014-10-11 20:57:58

Pickling is simply not implemented for this class:

```
sage: p.__reduce_ex__(2)
(<function copy_reg.__newobj__>,
 (sage.plot.plot3d.parametric_surface.ParametricSurface,),
 None,
 None,
 None)
```

as you can see, no construction parameters are provided at all. So this object just gets pickled as an empty `ParametricSurface` object.
