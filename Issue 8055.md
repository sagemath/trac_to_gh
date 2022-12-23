# Issue 8055: Add the jCarousel plug-in and set up a Sage showcase for the login page

Issue created by migration from https://trac.sagemath.org/ticket/8055

Original creator: mpatel

Original creation time: 2010-01-25 13:51:51

Assignee: was

CC:  schilly mvngu timdumol chapoton

Let's showcase the many cool features of Sage on the Notebook login page!

For this we can use a carousel plug-in for jQuery.  Some searches and several experiments indicate that [jCarousel](http://sorgalla.com/projects/jcarousel/) is both featureful and relatively easy-to-use.

Note: We can use the carousel in other ways, too, e.g., for slideshows.


---

Comment by mpatel created at 2010-01-25 13:55:17

Add jCarousel and use it on the login page.  sagenb repo.


---

Comment by mpatel created at 2010-01-25 14:21:44

Changing status from new to needs_review.


---

Attachment

Note: This depends on the SageNB 0.7 spkg at #8051.

The patch puts an auto-scrolling image carousel on the login page.  I've used several images from sagemath.org as an example.  [Here's a mockup.](http://boxen.math.washington.edu/home/mpatel/trac/8055/login_showcase.html)  But we could

 * Add screenshots.
 * Include links to more documentation, published worksheets, etc.
 * Make it customizable.
 * Get the server to generate images, etc.
 * Insert any HTML that fits in the space.


---

Comment by mpatel created at 2010-01-25 14:28:15

How should we allow server admins to use their own images and markup?  In a special directory under `DOT_SAGE/sage_notebook.sagenb`?


---

Comment by mpatel created at 2010-01-25 15:54:08

#3525 is related.


---

Comment by mpatel created at 2010-01-26 17:32:23

Changing status from needs_review to needs_work.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Changing status from needs_work to needs_review.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.


---

Comment by chapoton created at 2020-09-02 07:48:10

Resolution: invalid
