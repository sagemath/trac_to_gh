# Issue 8315: Reference manual layout: toggles, sidebar links

Issue created by migration from https://trac.sagemath.org/ticket/8315

Original creator: mpatel

Original creation time: 2010-02-20 21:02:10

Assignee: mvngu

CC:  hivert jhpalmieri nthiery klee

JavaScript additions to `layout.html` that transform a reference manual HTML page on display.

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/a34a80097ad47805/2e57eb60d7f9881d?#2e57eb60d7f9881d) for some background.


---

Comment by mpatel created at 2010-02-21 06:53:42

Reference manual toggles and sidebar links.  sage repo.


---

Attachment

I've attached a first take.  Remarks:

 * I haven't tested this extensively.
 * The sticky sidebar doesn't work in the live docs.
 * All of the transformations are done in the browser when it renders the page.
 * Feel free to change the colors or suggest other changes!


---

Comment by mpatel created at 2010-02-21 07:13:01

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-02-21 07:13:34

Oops!  Time for a break.


---

Comment by mpatel created at 2010-02-21 19:50:36

To do:

 * Disable or fix the sticky sidebar in the live docs.
 * Add hide / show / toggle controls for "all."
 * Add a color, etc., for attributes (e.g., aliases), data, exceptions, modules, i.e., the other `autodocumenters`.
 * Fix uniform over-indentation in live docs.
 * Make (sub)section headings toggle (sub)section display.  We can use this in the other docs.
 * Add "larger" and "smaller" font size controls.
 * When it's necessary, extend the main content to match the sidebar in length.

Most of these are straightforward to implement, I think.


---

Comment by mpatel created at 2010-06-23 01:16:08

Changing status from needs_review to needs_info.


---

Comment by mpatel created at 2010-06-23 01:16:08

I'm changing this to "needs info" until I can determine which improvements to make.


---

Comment by mpatel created at 2010-07-14 22:48:54

[Here](http://sage.math.washington.edu/home/mpatel/projects/sage_doc/reference/index.html) is the Sage 4.5.rc1 HTML reference manual built with the patch above.  See, for example, [2D Plotting](http://sage.math.washington.edu/home/mpatel/projects/sage_doc/reference/sage/plot/plot.html).  Comments are welcome!


---

Comment by nthiery created at 2010-07-15 01:36:14

Wow, I haven't tried it intensively, but for what I saw, it's going to be a great improvement in usability of the doc! Thanks!


---

Comment by nthiery created at 2010-07-15 01:37:17

Oh, by the way: would it be hard to add a pointer to the corresponding live documentation, when available?


---

Comment by mpatel created at 2010-07-15 05:02:03

Replying to [comment:7 nthiery]:
> Oh, by the way: would it be hard to add a pointer to the corresponding live documentation, when available?
Good idea!  This should be straightforward.  It may be better to include the link in just the "fast static" documentation.  In this case, we have the server address and port number, so we can insert an analogous "Go live!" link on the fly.

Of course, this only works if the server is still running and works best when the user is logged into the server.  I'm not aware of an easy way for a page to check whether a link is valid before deciding whether to display it or hide it.

For the "offline" docs (e.g., those accessed via `file:///`), perhaps we could prompt for a working server address (and save it in a cookie) or direct the user to `sagenb.org`?


---

Comment by mkoeppe created at 2022-10-26 05:15:16

Changing status from needs_info to needs_review.


---

Comment by mkoeppe created at 2022-10-26 05:15:16

likely outdated


---

Comment by klee created at 2022-10-26 05:27:03

Changing status from needs_review to positive_review.


---

Comment by klee created at 2022-10-26 05:27:03

I agree. We moved to furo.


---

Comment by mkoeppe created at 2022-11-14 19:36:43

Resolution: invalid
