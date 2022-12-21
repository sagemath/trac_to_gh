# Issue 6485: [with patch, needs review] broken links from website index to tutorial, constructions, etc.

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2009-07-08 17:32:50

Assignee: tba

Build the HTML documentation, including the website, and navigate to `$SAGE_ROOT/devel/sage/doc/output/html/en/index.html`.  Clicking on a link to an  individual document yields a directory listing, instead of the expected index page.


---

Attachment

This ticket looks like a duplicate of #5550 to me. Since mpatel's already uploaded a patch here, I suggest we close #5550 as a duplicate and keep this one open.


---

Comment by davidloeffler created at 2009-07-13 19:20:07

Works for me.


---

Comment by mvngu created at 2009-07-18 21:17:22

The patch fixes the index.html linking problem, but only for the page

SAGE_ROOT/devel/sage/doc/output/html/en/index.html

There's also a "website" which can be built using

sage -docbuild website html

and the same problem is still with the page

SAGE_ROOT/devel/sage/doc/output/html/en/website/index.html

But I doubt we need "website" at all. Its purpose is to link to the other 8 standard documents. This is already achieved with

SAGE_ROOT/devel/sage/doc/output/html/en/index.html

So I'm closing this ticket as fixing the linking problem in the page 

SAGE_ROOT/devel/sage/doc/output/html/en/index.html

Feel free to open another ticket to fix or delete the "website" page.


---

Comment by mvngu created at 2009-07-18 21:17:22

Resolution: fixed


---

Comment by mpatel created at 2009-07-19 05:10:38

I think `sage -docbuild website html` builds the top-level `index.html` in `website/` and just copies the output up one directory level.  (We could delete the original afterward.)  Perhaps I should have put "web site" in the summary instead of "website."  I apologize, if I'm mistaken.
