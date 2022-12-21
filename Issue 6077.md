# Issue 6077: simplicial complex method for polytopes

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2009-05-18 22:06:08

Assignee: mhampton

CC:  jhpalmieri

Keywords: polytopes, simplicial

This just adds a simplicial complex method for the polytope class, which requires lrs to compute a triangulation.


---

Attachment

adds a simplicial_complex method to polytopes


---

Comment by jhpalmieri created at 2009-05-19 03:21:53

Mostly good, but needs a few fixes.  I'm attaching a referee's patch which does the following:

 - removes the 'verbose' argument, since it's not used

 - inserts a warning about this possibly failing if the dimension is larger than 3

 - inserts '# optional' flags on the doctests so that they don't fail on machines without lrs installed

mhampton's patch gets a positive review from me; only my patch needs to be reviewed.  With my patch, all tests pass on sage.math (without lrs installed).  With lrs installed, sage -t -optional passes on this file.  (But someone else should probably double-check this.)


---

Comment by jhpalmieri created at 2009-05-19 03:22:24

apply on top of other patch


---

Attachment


---

Attachment

Thanks for looking at this.  Let me apologize for being somewhat confused about it - I have code in development for doing triangulations with lrs, but currently Sage doesn't use this.  So the warning about possibly not working in high dimensions is good, but I can also delete the check for lrs until I merge that code in.

Anyway, I have added a new patch "6077_v2.patch" which does not depend on the others and should account for the above comments and corrections.


---

Comment by jhpalmieri created at 2009-05-19 21:46:07

Looks good to me. Passes all tests (without lrs installed, which shouldn't be relevant anymore).


---

Comment by mabshoff created at 2009-05-21 01:41:00

Resolution: fixed


---

Comment by mabshoff created at 2009-05-21 01:41:00

Merged 6077_v2.patch only in Sage 4.0.rc0. In case that was not intended please let me know.

Cheers,

Michael
