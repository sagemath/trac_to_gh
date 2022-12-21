# Issue 2646: create plot_vector_field3d function

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-03-22 15:58:11

Assignee: was

CC:  kcrisman rbeezer

Here is an initial version.


```
def plot_vector_field3d(vec, xrange, yrange, zrange, plot_points=5, **kwds):
    xvar, xmin, xmax = xrange
    yvar, ymin, ymax = yrange
    zvar, zmin, zmax = zrange
    ff = SR(vec[0])._fast_float_(xvar, yvar, zvar)
    gg = SR(vec[1])._fast_float_(xvar, yvar, zvar)
    hh = SR(vec[2])._fast_float_(xvar, yvar, zvar)
    xpoints = [xmin..xmax, step=float(xmax-xmin)/(plot_points-1)][0:plot_points]
    ypoints = [ymin..ymax, step=float(ymax-ymin)/(plot_points-1)][0:plot_points]
    zpoints = [zmin..zmax, step=float(zmax-zmin)/(plot_points-1)][0:plot_points]
    points = [(i,j,k) for i in xpoints for j in ypoints for k in zpoints]
    vectors = [(ff(i,j,k), gg(i,j,k), hh(i,j,k)) for i,j,k in points]
    max_len = max([math.sqrt(i^2+j^2+k^2) for i,j,k in vectors])
    scaled_vectors = [(i/max_len, j/max_len, k/max_len) for i,j,k in vectors] 
    return sum([arrow3d( point, (point[0]+vector[0], point[1]+vector[1], point[2]+vector[2]), **kwds) for point,vector in zip(points, scaled_vectors)])
```


It is used similar to the plot_vector_field function:


```
sage: var('x y z')
sage: plot_vector_field3d((sin(x),cos(y), x*z), (x,0,3), (y,0,3), (z,0,3), plot_points=6)
```




---

Comment by robertwb created at 2008-03-22 18:01:52

Looks good, but it would be much faster to use the line3d function, which produces a native arrow rather than triangulating one. For example: 


```
line3d([(0,0,0), (1,2,3)], thickness=2, arrow_head=True)
```


perhaps the arrow3d command should be updated to use this when a thickness (as opposed to a radius) is specified.


---

Comment by jason created at 2009-03-12 07:45:09

See also: http://sagenb.org/home/pub/216/

That code appears to be better.


---

Comment by jason created at 2009-04-23 20:17:31

I rewrote my code above too.  Now I just plot the vector, since #5450 makes sure that plotting a vector actually plots line3d:


```
def plot_vector_field3d(vec, xrange, yrange, zrange, plot_points=[5,5,5], **kwds):
    xvar, xmin, xmax = xrange
    yvar, ymin, ymax = yrange
    zvar, zmin, zmax = zrange
    if not isinstance(plot_points, (list, tuple)):
        plot_points = [plot_points]*3
    ff, gg, hh = fast_float(vec, xvar, yvar, zvar)
    xpoints = [xmin..xmax, step=float(xmax-xmin)/(plot_points[0]-1)][0:plot_points[0]]
    ypoints = [ymin..ymax, step=float(ymax-ymin)/(plot_points[1]-1)][0:plot_points[1]]
    zpoints = [zmin..zmax, step=float(zmax-zmin)/(plot_points[2]-1)][0:plot_points[2]]
    points = [vector((i,j,k)) for i in xpoints for j in ypoints for k in zpoints]
    vectors = [vector((ff(*point), gg(*point), hh(*point))) for point in points]
    # scale the vectors
    max_len = max(v.norm() for v in vectors)
    scaled_vectors = [v/max_len for v in vectors] 
    return sum([plot(v,**kwds).translate(p) for v,p in zip(scaled_vectors, points)])
```



---

Comment by jason created at 2009-04-23 20:23:43

Here's another version that offers the option of centering the arrows on the point.


```
def plot_vector_field3d(vec, xrange, yrange, zrange, plot_points=[5,5,5], center_arrows=False,**kwds):
    xvar, xmin, xmax = xrange
    yvar, ymin, ymax = yrange
    zvar, zmin, zmax = zrange
    if not isinstance(plot_points, (list, tuple)):
        plot_points = [plot_points]*3
    ff, gg, hh = fast_float(vec, xvar, yvar, zvar)
    xpoints = [xmin..xmax, step=float(xmax-xmin)/(plot_points[0]-1)][0:plot_points[0]]
    ypoints = [ymin..ymax, step=float(ymax-ymin)/(plot_points[1]-1)][0:plot_points[1]]
    zpoints = [zmin..zmax, step=float(zmax-zmin)/(plot_points[2]-1)][0:plot_points[2]]
    points = [vector((i,j,k)) for i in xpoints for j in ypoints for k in zpoints]
    vectors = [vector((ff(*point), gg(*point), hh(*point))) for point in points]
    # scale the vectors
    max_len = max(v.norm() for v in vectors)
    scaled_vectors = [v/max_len for v in vectors]
    if center_arrows:
        return sum([plot(v,**kwds).translate(p-v/2) for v,p in zip(scaled_vectors, points)])
    else:
        return sum([plot(v,**kwds).translate(p) for v,p in zip(scaled_vectors, points)])
```


I think the only other thing that the function in the worksheet linked above does is provide an option to make the arrows thicker (based on the scaling, I believe).


---

Comment by jason created at 2009-10-29 04:03:14

Even shorter, now that we have a better plotting base:


```
def plot_vector_field3d(vec, xrange, yrange, zrange, plot_points=[5,5,5], center_arrows=False,**kwds):
    from sage.plot.misc import setup_for_eval_on_grid
    (ff,gg,hh), ranges = setup_for_eval_on_grid(vec, [xrange, yrange, zrange], plot_points)
    xpoints, ypoints, zpoints = [srange(*r, include_endpoint=True) for r in ranges]
    points = [vector((i,j,k)) for i in xpoints for j in ypoints for k in zpoints]
    vectors = [vector((ff(*point), gg(*point), hh(*point))) for point in points]

    max_len = max(v.norm() for v in vectors)
    scaled_vectors = [v/max_len for v in vectors]

    if center_arrows:
        return sum([plot(v,**kwds).translate(p-v/2) for v,p in zip(scaled_vectors, points)])
    else:
        return sum([plot(v,**kwds).translate(p) for v,p in zip(scaled_vectors, points)])
```



---

Comment by jason created at 2009-10-29 04:31:56

Okay, now with coloring based on the norm, using matplotlib colormaps:


```
def plot_vector_field3d(vec, xrange, yrange, zrange, plot_points=[5,5,5], cmap='jet', center_arrows=False,**kwds):
    from matplotlib.cm import get_cmap
    from sage.plot.misc import setup_for_eval_on_grid
    (ff,gg,hh), ranges = setup_for_eval_on_grid(vec, [xrange, yrange, zrange], plot_points)
    xpoints, ypoints, zpoints = [srange(*r, include_endpoint=True) for r in ranges]
    points = [vector((i,j,k)) for i in xpoints for j in ypoints for k in zpoints]
    vectors = [vector((ff(*point), gg(*point), hh(*point))) for point in points]
    
    cm=get_cmap(cmap)

    max_len = max(v.norm() for v in vectors)
    scaled_vectors = [v/max_len for v in vectors]
    
    if center_arrows:
        return sum([plot(v,color=cm(v.norm()),**kwds).translate(p-v/2) for v,p in zip(scaled_vectors, points)])
    else:
        return sum([plot(v,color=cm(v.norm()),**kwds).translate(p) for v,p in zip(scaled_vectors, points)])
```



---

Comment by jason created at 2009-10-29 04:47:54

One more try, so that colors can take a single matplotlib color specifier, a list of color specifiers, or a name of a matplotlib cmap.


```
def plot_vector_field3d(vec, xrange, yrange, zrange, plot_points=[5,5,5], colors='jet', center_arrows=False,**kwds):
    from matplotlib.cm import get_cmap
    from matplotlib.colors import ListedColormap
    from sage.plot.misc import setup_for_eval_on_grid
    (ff,gg,hh), ranges = setup_for_eval_on_grid(vec, [xrange, yrange, zrange], plot_points)
    xpoints, ypoints, zpoints = [srange(*r, include_endpoint=True) for r in ranges]
    points = [vector((i,j,k)) for i in xpoints for j in ypoints for k in zpoints]
    vectors = [vector((ff(*point), gg(*point), hh(*point))) for point in points]
    
    try:
        cm=get_cmap(colors)
        assert(cm is not None)
    except:
        if not isinstance(colors, (list, tuple)):
            colors=[colors]
        cm=ListedColormap(colors)
                
    max_len = max(v.norm() for v in vectors)
    scaled_vectors = [v/max_len for v in vectors]
    
    if center_arrows:
        return sum([plot(v,color=cm(v.norm()),**kwds).translate(p-v/2) for v,p in zip(scaled_vectors, points)])
    else:
        return sum([plot(v,color=cm(v.norm()),**kwds).translate(p) for v,p in zip(scaled_vectors, points)])
```



---

Comment by jason created at 2009-10-29 04:48:01

Changing status from new to needs_work.


---

Attachment

Finally, a patch!


---

Comment by jason created at 2009-10-29 06:29:00

Changing status from needs_work to needs_review.


---

Comment by mhampton created at 2009-10-29 19:02:06

Changing status from needs_review to positive_review.


---

Comment by mhampton created at 2009-10-29 19:02:06

Very nice, positive review.  This is great timing since I am about to teach vector fields in a week or two.


---

Comment by mhansen created at 2009-10-31 05:18:14

Resolution: fixed
