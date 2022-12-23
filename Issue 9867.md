# Issue 9867: Improve plot3d documentation

Issue created by migration from https://trac.sagemath.org/ticket/9868

Original creator: kcrisman

Original creation time: 2010-09-07 16:13:55

Assignee: jason, was

CC:  jason

The highest-level ResT files for 3d plotting are ... not so informative.  See for instance [this](http://www.sagemath.org/doc/reference/sage/plot/plot3d/examples.html) page.

This ticket would make the top-level 3d plotting page look as nice as [this](http://www.sagemath.org/doc/reference/sage/plot/plot.html) one, with lots of discussion about options - and in particular putting text on a 3D plot, since [this](http://groups.google.com/group/sage-support/browse_thread/thread/46b1fef4c02dc650/c25cdb155dcccc56?show_docid=c25cdb155dcccc56&pli=1) thread mentioned it.



---

Comment by jason created at 2010-09-07 16:16:52

As a different ticket, we should make text work with 2d or 3d plots, like most other plotting functions do.


---

Comment by kcrisman created at 2010-09-07 16:19:36

Replying to [comment:1 jason]:
> As a different ticket, we should make text work with 2d or 3d plots, like most other plotting functions do.
Can you clarify what you mean by that?  Do you mean a `.3d()` method (or whatever it's called)?  Or do you mean like how `point` or `line` know whether there are two or three coordinates?


---

Comment by jason created at 2010-09-07 16:24:39

Make text() behave like point() or line().
