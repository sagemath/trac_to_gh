# Issue 9728: Moving the Linear transformations interact from wiki into the library.

Issue created by migration from https://trac.sagemath.org/ticket/9728

Original creator: punchagan

Original creation time: 2010-08-11 21:33:05

Assignee: itolkov, jason

CC:  mhampton nishanth.amuluru@gmail.com

This code moves the interact example for linear transformations from the wiki to the library. 


---

Attachment


---

Comment by punchagan created at 2010-08-12 04:45:30

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-09-21 20:06:58

Does this conflict with #9623?  It would be great to get that in first, then this and #9729.


---

Comment by samhop created at 2010-11-07 07:16:23

So far as I can tell, this doesn't conflict with 9623. At very least, they don't attempt to implement overlapping interacts.


---

Attachment

adds capability for user to set the matrix defining the transformation


---

Comment by pang created at 2010-11-18 09:46:53

I want to propose some changes to this interact:

 * Adding a 2x3 transformation (affine, I guess) does not fit with plotting vectors, IMHO. I'd stick to linear transformations and possibly add a second interact for affine transformations.
 * Use input_grid instead of input_box for the matrix.
 * Why plot two concentric circles? It is useful to communicate that the aspect_ratio is 1, but if the axes are present, I don't think it's necessary.
 * Why not plot the unit sphere, and its image under A, instead? Using the same colors as with the vectors, this makes the idea more clear.

So how about using the following code instead:

```
@interact 
def linear_transformation(
    theta = slider(0, 2*pi, .1), 
    r     = slider(0.1,  2, .1, default=1),
    A     = input_grid(2, 2, default = [[1,-1],[-1,1/2]],
                             to_value=matrix)):
    """An interact which illustrates ...
    """
    v=vector([r*cos(theta), r*sin(theta)]) 
    w = A*v

    unit_sphere = circle((0,0), radius = 1, rgbcolor = (1,0,0))
    var('t')
    image_of_sphere = parametric_plot(A*vector([sin(t),cos(t)]), 
                         (t, 0, 2*pi), rgbcolor=(0,0,1))
    
    html("$v = %s,; %s w=%s$"%(v.n(4),latex(A),w.n(4)))     
    show(v.plot(rgbcolor=(1,0,0)) +
         w.plot(rgbcolor=(0,0,1)) +
         unit_sphere + image_of_sphere,
         aspect_ratio=1)
```



---

Attachment


---

Comment by kcrisman created at 2011-06-13 18:13:29

Based on pang's comments, apparently this is 'needs work'.


---

Comment by kcrisman created at 2011-06-13 18:13:29

Changing status from needs_review to needs_work.
