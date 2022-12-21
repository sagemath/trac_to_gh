# Issue 8320: Make HTML doc headers and footers more compact

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-02-21 19:59:15

Assignee: mvngu

We can use Sphinx's [html_short_title setting](http://sphinx.pocoo.org/config.html#confval-html_short_title) to [try to] keep links from overflowing the header and footer.

For example, instead of "Sage Reference Manual v4.3.3," we can use "Reference v4.3.3."


---

Comment by mpatel created at 2010-02-21 21:43:09

HTML short titles for selected docs.  sage repo.


---

Attachment

The patch adds shorter HTML titles, which appear in Sphinx headers and footers, for selected docs: the developer's guide, Bordeaux lectures, numerical primer, and reference manual.  The others' titles overflow only with very large font sizes.  But feel free to make adjustments, e.g., for consistency.


---

Comment by mpatel created at 2010-02-21 21:57:54

Changing priority from minor to trivial.


---

Comment by mpatel created at 2010-02-21 21:57:54

Changing status from new to needs_review.


---

Attachment

apply on top of previous patch


---

Comment by mvngu created at 2010-02-26 04:48:44

The reviewer patch [trac_8320-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8320/trac_8320-reviewer.patch) shortens the HTML title of these documents:

 * A Tour of Sage
 * Sage Installation Guide
 
I also changed the short title of the reference manual from "Reference" to "Sage Reference" as an attempt to be consistent with these short titles:

 * Sage Tutorial
 * Sage Constructions
 * Sage Tour
 
Only my patch needs review by anyone but me.


---

Comment by mpatel created at 2010-02-26 20:20:43

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-02 22:19:42

Resolution: fixed


---

Comment by mvngu created at 2010-03-02 22:19:42

Merged in this order:

 1. [trac_8320-html_short_title.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8320/trac_8320-html_short_title.patch)
 1. [trac_8320-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8320/trac_8320-reviewer.patch)
