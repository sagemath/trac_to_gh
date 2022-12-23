# Issue 9483: implicit_plot3d fails on symbolic inputs that can't be automatically differentiated

Issue created by migration from https://trac.sagemath.org/ticket/9483

Original creator: cwitty

Original creation time: 2010-07-12 17:21:32

Assignee: cwitty

Here's an example:

```
sage: implicit_plot3d(max_symbolic(min_symbolic(x*x+y*y-1, x*x+z*z-2), x-1.8, y-1.8, z-1.8, -x-1.8, -y-1.8, -z-1.8), (x, -2, 2), (y, -2, 2), (z, -2, 2))
```

... VERY long traceback, ending:

```
/home/cwitty/sage/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in fast_callable(ex, etb)
   1363 
   1364     """
-> 1365     return FastCallableConverter(ex, etb)()
   1366 
   1367 class RingConverter(Converter):

/home/cwitty/sage/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in __call__(self, ex)
    216             return self.relation(ex, operator)
    217         elif isinstance(operator, FDerivativeOperator):
--> 218             return self.derivative(ex, operator)
    219         else:
    220             return self.composition(ex, operator)

/home/cwitty/sage/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.pyc in derivative(self, ex, operator)
    349             NotImplementedError: derivative
    350         """        
--> 351         raise NotImplementedError, "derivative"
    352 
    353     def arithmetic(self, ex, operator):

NotImplementedError: derivative
```




---

Comment by cwitty created at 2010-07-18 02:52:46

Changing status from new to needs_review.


---

Attachment

This patch fixes the error; all doctests pass.


---

Comment by kcrisman created at 2010-08-05 20:44:48

I'd like to review this but for some reason it doesn't apply for the `implicit_plot3d` part.  I can't figure out where the lines 230-232 in the patch come from - the file doesn't seem to have been changed in quite some time, according to hg, and 4.5.2.rc1 doesn't have this. 

By the way, I am *very* curious about *why* this fixes it!  Does smooth require differentiating?


---

Comment by kcrisman created at 2010-08-05 20:46:29

Or does this depend on #9482, as I now realize?


---

Comment by kcrisman created at 2010-08-06 01:02:38

Okay, one issue is that this depends on some other ticket which may or may not get reviewed.

And I think I see why this fix works, sort of - when smooth is True, MarchingCubesTriangles calls the gradient, though presumably smooth was already False - this seems weird to me.  But why not make the change at

```

    def __init__(self, f, xrange, yrange, zrange,
                 contour=0, plot_points="automatic",
                 region=None, smooth=True, gradient=None, vertex_color=None,
                 **kwds):
```

?  I guess someone could still pass in 'smooth', though it seems like then this should be deprecated as an option - or we should have prominent TODO to add it.  But also

```

        if smooth and gradient is None:
```

it seems like we should just get rid of this whole thing, since smooth will never be True.

Anyway, because I don't quite understand those things, I'm putting `needs_info`, but it seems good overall - and I apologize for any ignorance on my part.  

On the plus side, it does get rid of the traceback as advertised!  For some reason I don't have 3d plotting on the computer I'm checking this one (old Java?), but that's still pretty good.


---

Comment by kcrisman created at 2010-08-06 01:02:38

Changing status from needs_review to needs_info.


---

Comment by cwitty created at 2010-08-06 02:40:15

When I first wrote the code, I had the idea to create a direct-to-tachyon backend that would use vertex normals to create much nicer-looking plots with smaller numbers of plot_points, and laid the groundwork for this backend with the gradient and smooth arguments.  But I abandoned the code without writing this backend (and leaving many other parts of the code unfinished).

When William Cauchois took over and finished the code (thank you, William!), he only wrote an `IndexFaceSet` backend, that can't (currently) make use of vertex normals.  So the gradient code is currently useless.

It would make me sad, but I wouldn't object if the gradient code were removed altogether.  I do think it basically works, though, and it's still open for somebody to write a direct-to-tachyon backend, or to extend `IndexFaceSet` to support vertex normals...


---

Comment by kcrisman created at 2010-08-06 14:12:52

Changing status from needs_info to needs_work.


---

Comment by kcrisman created at 2010-08-06 14:12:52

I totally don't think we should get rid of good code, but I think that if this is what is going on, before we get a positive review here there should be some additional comments near where the `smooth` parameter first shows up that says approximately what you do here - what the parameter is for, where one would extend it, etc.  The `IndexFaceSet` file has one tiny TODO that mentions this, which is also not too helpful.

Otherwise this works (my work computer apparently has good enough Java, and I don't know why I didn't think of using tachyon last night), though I'm still mystified why having it in the `options` dict didn't work but this does.


---

Comment by kcrisman created at 2011-06-14 03:31:48

Changing status from needs_work to positive_review.


---

Comment by kcrisman created at 2011-06-14 03:31:48

I'm taking care of adding that content.  It's really silly this took so long, but I didn't know whether Carl would do that.   It's just some comments, so positive review!  It still applies :)


---

Comment by kcrisman created at 2011-06-14 03:33:03

apply only this file


---

Comment by jdemeyer created at 2011-06-15 20:13:06

Resolution: fixed


---

Attachment
