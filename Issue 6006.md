# Issue 6006: Bring plot/point.py to 100% coverage

Issue created by migration from https://trac.sagemath.org/ticket/6006

Original creator: kcrisman

Original creation time: 2009-05-08 05:09:27

Assignee: tba

Bring plot/point.py to 100% coverage.


---

Comment by kcrisman created at 2009-05-08 05:13:20

Changing assignee from tba to kcrisman.


---

Comment by kcrisman created at 2009-05-08 05:13:20

Changing status from new to assigned.


---

Attachment

This patch also actually implements the height option for the plot3d method of the Point class that the old doctest was actually using through a 3D graphics object.


---

Comment by kcrisman created at 2009-05-08 05:15:41

I should also point out that I could not find a way to test for _allowed_options for the keywords in Point.plot3d, so I put something about that in the TODO but also pointed it out in the documentation, lest one confuse pointsize and size (et al.).


---

Comment by kcrisman created at 2009-05-08 16:46:10

See [http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43](http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43) for explanation of why there is no loads(dumps()) test.


---

Comment by mvngu created at 2009-05-13 04:36:33

On line 43, the constructor for `Point(GraphicPrimitive_xydata)` is

```
43	    def __init__(self, xdata, ydata, options)
```

Currently with Sphinx, any docstring of `__init__` will not be shown in the documentation for `Point(GraphicPrimitive_xydata)`. The situation is the same for every class. So one issue to fix is to copy the examples in `__init__(self, xdata, ydata, options)` and paste them within the docstring for `Point(GraphicPrimitive_xydata)` after line 32. Another issue is, the constructor arguments `xdata, ydata, options` on line 43 are not documented in the docstring for `Point(GraphicPrimitive_xydata)`. Constructor arguments must be documented to explain what they are, and how to properly use them.


---

Comment by kcrisman created at 2009-05-13 13:35:19

I was not aware of this.  I would be happy to improve this, and copying examples is easy.  However, could you point me to a file with a correctly documented set of constructor arguments?  I am uncertain how to proceed with that, particularly because I modeled my own documentation after other examples in plot/; the xdata and ydata, for instance, come from the function getxydata or something like that, which is called when a point (as opposed to Point) is made.   Also, what _should_ be in the docstring for __init__, if not what is currently there?  Thanks for any ideas or model files to look at!


---

Comment by mabshoff created at 2009-05-13 17:18:20

Replying to [comment:4 mvngu]:
}
> Currently with Sphinx, any docstring of `__init__` will not be shown in the documentation for `Point(GraphicPrimitive_xydata)`. The situation is the same for every class. So one issue to fix is to copy the examples in `__init__(self, xdata, ydata, options)` and paste them within the docstring for `Point(GraphicPrimitive_xydata)` after line 32.

No, do not do this. It will be fixed in the future. This is still "needs work" due to the other issue.

Cheers,

Michael


---

Attachment


---

Comment by mvngu created at 2009-05-15 07:20:01

reviewer patch


---

Attachment

Positive review! Apply patches in the following order:
 1. `trac_6006.patch`
 1. `trac_6006-fix.patch`
 1. `trac_6006-reviewer.patch` -- this fixes two trivial typos introduced in `trac_6006.patch`


---

Comment by mabshoff created at 2009-05-15 07:54:47

Merged all three patches in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-15 07:54:47

Resolution: fixed
