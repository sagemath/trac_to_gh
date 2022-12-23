# Issue 7367: Add SageNB modules to the reference manual

Issue created by migration from https://trac.sagemath.org/ticket/7367

Original creator: mpatel

Original creation time: 2009-11-01 13:35:58

Assignee: tbd

CC:  timdumol

Currently, the [reference manual's](http://www.sagemath.org/doc/reference/index.html) [Notebook section](http://www.sagemath.org/doc/reference/notebook.html) documents the old Sage notebook.

We should update this section with docstrings from the recently separated [SageNB](http://nb.sagemath.org/).


---

Attachment

Add SageNB modules to reference manual.  Apply to sage repo.


---

Comment by mpatel created at 2009-11-01 14:03:26

I've commented out the "Interfaces" section, for now.

I think `sagenb.misc.sphinxify`'s docstrings need just a bit of tweaking.


---

Comment by mpatel created at 2009-11-01 14:10:43

Replying to [comment:1 mpatel]:
> I think `sagenb.misc.sphinxify`'s docstrings need just a bit of tweaking.

Of course, we can comment it out, too, temporarily.  I didn't mean to pile on more work.


---

Comment by mpatel created at 2009-11-01 14:10:50

Changing status from new to needs_review.


---

Comment by timdumol created at 2009-11-03 20:48:05

Replying to [comment:2 mpatel]:
> Replying to [comment:1 mpatel]:
> > I think `sagenb.misc.sphinxify`'s docstrings need just a bit of tweaking.
> 
> Of course, we can comment it out, too, temporarily.  I didn't mean to pile on more work.

Docstring fixes are up at http://trac.sagemath.org/sage_trac/ticket/7384


---

Comment by timdumol created at 2009-11-03 21:32:53

Everything looks good, but why is the miscellaneous section named "Documentation"? Shouldn't it be named "Miscellaneous functions", or "Introspection", or the like? The name "Documentation" is confusing, at least for me.


---

Comment by mpatel created at 2009-11-04 04:36:04

"Documentation" is indeed confusing.  I think my motive was to identify and group the [mostly] help-related modules.  Since `support` falls under "Online Help" and "Miscellaneous," the forthcoming patch simply puts them all under the latter.


---

Attachment

Less confusing subheading.  Really skip interface modules.  Apply only this patch to sage repo.


---

Comment by mpatel created at 2009-11-12 01:44:32

Feel free to bump the milestone to 4.3.


---

Comment by was created at 2009-11-12 02:12:53

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-11-12 02:12:53

Looks good to me too.


---

Comment by mhansen created at 2009-11-12 07:30:39

Resolution: fixed
