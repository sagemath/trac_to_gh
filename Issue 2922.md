# Issue 2922: scale function for plot_vector_field

Issue created by migration from https://trac.sagemath.org/ticket/2922

Original creator: schilly

Original creation time: 2008-04-14 21:28:18

Assignee: was

CC:  jason novoselt

When plotting a vector field, it is useful to be able to scale the length of the arrows. This is similar to [mma:ScaleFunction](http://reference.wolfram.com/mathematica/VectorFieldPlots/ref/ScaleFunction.html). 

e.g.:
 * an upper therehold: `lambda x: min(1,x)`
 * logarithmic: `lambda x: log(1+x)`

where x is the positive absolute length of the vector and each coordinate is divided by that - or some generalization of that.


---

Comment by kcrisman created at 2009-09-29 20:49:57

This would be good.  There are two options for this.

1. Rewrite the matplotlib scale to take either a number or a callable function, and somehow make the Sage interface to this make scaling do what one would expect (the mpl scale does NOT behave as expected, as it essentially makes its own adhoc function similar to ones above).

2. Get at the underlying matplotlib object for each and every arrow in the Quiver and adjust the length. 

I'm not sure how the second one could even happen.  But the first one requires some non-trivial changes to matplotlib.quiver (since currently scale is an attribute only), and probably should be sent upstream if done.


---

Comment by jason created at 2009-09-29 21:41:31

So basically you want to give a function that gives the length of a vector?  That sounds reasonable.

Since Sage is actually the thing that generates the vectors, and matplotlib just plots them, I think scaling the vectors in Sage to each have the length you want is the correct thing to do here, before passing them to matplotlib.

plot_vector_field((-y,-x), (x,0,1),(y,0,1), norm=f)

where f is a function defined to take f(v,w), where v is the vector, w is the point in space (as a vector).

so your examples would be:

f=lambda v,w: min(1,v.norm())

f=lambda v,w: log(1+v.norm())

We could then adjust the scale parameter of the quiver plot so that the arrows would plot exactly the length you wanted (I believe units='x', scale=1 should do the job).


---

Comment by kcrisman created at 2009-09-30 00:16:59

Well, yeah, you can use the same thing you do in plot_slope_field to get the norm (in fact, numpy has this nice absolute() function that mpl uses).  But it looked to me like it might not be possible to get around the auto-scaling that mpl does (see matplotlib.quiver??), since ordinarily scale=1 is definitely _not_ what one wants.  I will look to see if units='x' would actually get around that.


---

Comment by jason created at 2009-09-30 00:53:48

The scale argument says the ratio of length to units, where units are specified in the units parameter.  Usually the units are not in terms of data coordinates, I believe.  So what you want is to make the units equal to data coordinates (i.e., 'x' or 'y'), instead of a function of the plot size, like 'width' and 'height' are.


---

Comment by jason created at 2009-09-30 01:28:59

After playing with this a bit more, I decided that, while what matplotlib has makes sense, it isn't what we want.  I just sent a message to the matplotlib-users mailing list.


---

Comment by jason created at 2009-10-01 04:09:43

Eric Firing just committed the change to the matplotlib quiver function that allows us to scale arrows easily.  See http://www.nabble.com/scaling-arrows-in-quiver-tt25673613.html#a25673613

Now we just need to update the matplotlib spkg and wrap it (the new scale_units function).  This might wait a while until the next release of matplotlib comes out, unless someone wants to update the spkg before then.


---

Comment by jason created at 2009-10-01 04:13:42

(his commit is here: http://github.com/astraw/matplotlib/commit/b24fa7c6aef0db82ae4c9108c86abf3ddd871e34 )


---

Comment by edrex created at 2009-10-19 19:57:35

I'd like to be able to pass the scale kwarg to quiver, is that what we're talking about doing?


---

Comment by jason created at 2009-10-20 15:03:27

Replying to [comment:8 edrex]:
> I'd like to be able to pass the scale kwarg to quiver, is that what we're talking about doing?

yes.


---

Comment by kcrisman created at 2011-04-17 00:24:01

See also #11208, which is also about quivers.

Is this ready to wrap?  We've definitely updated mpl since a year and a half ago.


---

Comment by jason created at 2011-04-17 00:42:55

Replying to [comment:10 kcrisman]:

> Is this ready to wrap?  We've definitely updated mpl since a year and a half ago.

Yes, it should be ready to wrap now.


---

Comment by benjaminfjones created at 2012-09-30 21:33:20

Just a note, this ticket would provide a nice solution to the issue raised at http://ask.sagemath.org/question/1816/visualize-vector-field-with-singularities.


---

Comment by kcrisman created at 2020-06-19 19:40:40

Another thing requested somewhat often is that all have the same length, similar to slope field but with arrows.  #11208 is still relevant here.  (We may also be able to remove the hack there if we haven't already.)


---

Comment by kcrisman created at 2022-07-28 15:35:35

Another note: Apparently `VectorField.plot()` from the Sage manifolds project has some of the things discussed here.
