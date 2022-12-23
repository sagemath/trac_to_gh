# Issue 6664: [with patch, needs review] Skip nested classes in docs by Sphinx v0.6.x

Issue created by migration from https://trac.sagemath.org/ticket/6664

Original creator: mpatel

Original creation time: 2009-08-02 09:39:43

Assignee: tba

Sphinx complains about nested classes when building the reference manual.

This just tweaks #6419 so that it works with Sphinx v0.6.x's `autodoc` extension.  See [comment:#6586:10 this comment] at #6586 for more.


---

Attachment

"Depends" on #6586.


---

Comment by jhpalmieri created at 2009-08-23 18:09:50

This suppresses the private methods (`__init__`, etc.).  I'm not sure this is a good idea.  Before the transition to Sphinx, these were included in the reference manual, and then they weren't post-Sphinx, I think mainly because the default was to not include them.  I think they should be included.


---

Comment by mpatel created at 2009-08-23 18:39:57

Sounds good.  I should have understood and [remembered](http://groups.google.com/group/sage-devel/browse_thread/thread/80a99dc2c2836a7b/ad3407f7714349bf).  How about a docbuild option to select between "developer" and "user" documentation?  Or is this not a meaningful distinction?  Are there any private methods we should always suppress?   Of course, we can just close this ticket (or mark it as invalid).


---

Comment by jhpalmieri created at 2009-08-23 21:22:24

I think that having different versions of the reference manual was discussed at some point, but without definite outcomes or guidelines.  Maybe it should be discussed on sage-devel?

At the moment, though, including private methods is a bit problematic.  First, `__weakref__` appears sort of at random, and then some classes get all sorts of weird extra methods, maybe inherited from another class?  See the `Matrix` class in `SAGE_ROOT/devel/sage/doc/output/html/en/reference/sage/matrix/matrix0.html`, for example; there is an entry for `__delitem__`, and the entry for `__init__` is wrong: it looks generic rather than the one which is actually in the file.  Maybe this has to do with it being Cython rather than Python.

Is it better to exclude all private methods, or to include them at the price of having all sorts of extra crap in addition?  I say we continue to exclude them until we can figure out how to fix this.  So let's keep this patch for now.  I'll give it a positive review.

Does this really depend on #6586, or can it be merged now?


---

Comment by mpatel created at 2009-08-24 04:50:58

Replying to [comment:4 jhpalmieri]:
> Does this really depend on #6586, or can it be merged now?
It's not dependent, according to `du -s`.  I tested this with and without the patch, with Sphinx 0.5.1.


---

Comment by mvngu created at 2009-08-29 11:40:20

Resolution: fixed
