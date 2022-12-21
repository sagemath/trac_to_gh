# Issue 9484: add demos for implicit_plot3d that show how to do CSG (constructive solid geometry)

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2010-07-12 17:34:19

Assignee: cwitty

See http://groups.google.com/group/sage-support/browse_thread/thread/e05229d90733c78d for an example of how to do CSG (intersections and unions of solid objects) with implicit_plot3d; I think the given example:

```
sage: var('x,y,z')
(x, y, z)
sage: implicit_plot3d(max_symbolic(min_symbolic(x*x+y*y-1, x*x+z*z-2), x-1.8, y-1.8, z-1.8, -x-1.8, -y-1.8, -z-1.8), (x, -2, 2), (y, -2, 2), (z, -2, 2), smooth=False)
```

(along with some explanation) should be added to the implicit_plot3d docstring.


---

Attachment

I picked a slightly different example.


---

Comment by cwitty created at 2010-07-18 02:54:05

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-08-05 20:46:24

Probably depends on #9482 and #9483.


---

Comment by kcrisman created at 2010-08-06 01:27:37

After #9483, I go from error message to no error message with this example as expected.  Can't test the actual view for some reason :(


---

Comment by cwitty created at 2010-08-06 02:45:40

I apologize for not marking the dependency in my comment.

By the way, you could see a version of the plot by adding a viewer='tachyon' keyword argument to the implicit_plot3d call.


---

Comment by kcrisman created at 2010-08-06 14:18:32

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2010-08-06 14:18:32

This looks fine, except probably one should put commands like `implicit_plot3d` in double ticks like ```implicit_plot3d```, or in that case you might even be able to use `:meth:` or something like that.  Very interesting example!
