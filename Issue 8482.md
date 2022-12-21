# Issue 8482: Add a link from the static help embedded in the notebook to the corresponding live documentation page

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2010-03-08 21:50:17

Assignee: was

CC:  sage-combinat

Keywords: notebook, live documentation

Task: in the static documentation that appears embedded in the
notebook upon, say,

        sage: sage.categories.primer?

add a link to the corresponding live documentation page
(e.g. http://localhost:8000/doc/live/reference/sage/categories/primer.html)

This would be very handy, and make a strong advertisement for the live
documentation (a really cool feature that I had never stumbled upon
until Mike hinted me about it; and apparently, no one at Sage 20 knew
about it either).



---

Comment by nthiery created at 2010-03-08 22:11:40

The thread where this came up: http://groups.google.com/group/sage-devel/t/ab13aaf3dbe17a19.


---

Comment by kini created at 2013-03-27 22:44:00

Changing status from new to needs_review.


---

Comment by kini created at 2013-03-27 22:44:00

Pull request: https://github.com/sagemath/sagenb/issues/146


---

Comment by kini created at 2013-03-27 22:44:08

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2013-03-28 13:59:12

Keshav, I still don't understand why this should be positive review if we haven't actually merged a sagenb with it in it.  We would never do that with Maxima or Pari.  I have changed this to "reported upstream, developers acknowledge bug".


---

Comment by kcrisman created at 2013-03-28 13:59:12

Changing status from positive_review to needs_info.


---

Comment by kini created at 2013-03-28 14:13:04

Ah, fair enough. You're right, I wasn't thinking.


---

Comment by embray created at 2018-08-10 09:51:28

This would still be nice to have, not just for the classic SageNB, but also in the Jupyter kernel (if possible), or at least links to doc.sagemath.org if a local copy of the docs is not available.
