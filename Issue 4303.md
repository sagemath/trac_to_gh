# Issue 4303: Plotting: points(list_of_points, rgbcolor=c) gives strangely colored results with exactly 3 points.

Issue created by migration from https://trac.sagemath.org/ticket/4303

Original creator: jbandlow

Original creation time: 2008-10-15 17:33:34

Assignee: was

Keywords: plotting

From the docstring for point2d, the following works fine:

sage: p = point(((0.5, 0.5), (1, 2), (0.5, 0.9), (-1,-1)), rgbcolor=hue(1), pointsize=30); p.show()

However

sage: p = point(((0.5, 0.5), (1, 2), (0.5, 0.9)), rgbcolor=hue(1), pointsize=30); p.show()

gives one purple(?) point and two blue points.  This seems to happen if and only if the number of points specified is exactly three, regardless of the specified color.




---

Comment by mhampton created at 2008-10-15 18:38:30

I wonder if this is related to the apparent special casing of 3 or fewer points in GraphicPrimitiveFactory_from_point_list (code below, from sage/plot/plot.py).  That was the best lead I can find with the time I have, hope it helps.


```
class GraphicPrimitiveFactory_from_point_list(GraphicPrimitiveFactory):
    def __call__(self, points, coerce=True, **kwds):
        try:
            return points.plot(**kwds)
        except AttributeError:
            pass
        options = dict(self.options)
        for k, v in kwds.iteritems():
            options[k] = v

        if not isinstance(points, (list,tuple)) or \
           (isinstance(points,(list,tuple)) and len(points) <= 3 \
            and len(points) > 0 \
            and not isinstance(points[0], (list,tuple))):
            try:
                points = [[float(z) for z in points]]
            except TypeError:
                pass

        try:
            if len(points) > 0 and len(points[0]) == 3:
                return self._graphic3d()(points, coerce=coerce, **kwds)
        except (AttributeError, TypeError):
            pass
        xdata = []
        ydata = []
        if coerce:
            xdata = [float(z[0]) for z in points]
            ydata = [float(z[1]) for z in points]            
        else:
            xdata = [z[0] for z in points]
            ydata = [z[1] for z in points]            

        return self._from_xdata_ydata(xdata, ydata, True, options=options)
```



---

Comment by mhansen created at 2008-10-15 19:12:47

This is a duplicate of #2076.


---

Comment by mhansen created at 2008-10-15 19:12:47

Resolution: duplicate
