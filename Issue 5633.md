# Issue 5633: [with patch, needs review] add pix to the documentation

Issue created by migration from https://trac.sagemath.org/ticket/5633

Original creator: jhpalmieri

Original creation time: 2009-03-29 16:08:57

Assignee: tba

The documentation has been missing a few pictures, and this patch restores them.


---

Comment by jhpalmieri created at 2009-03-29 16:14:49

Changing assignee from tba to jhpalmieri.


---

Comment by jhpalmieri created at 2009-03-29 16:14:49

Changing status from new to assigned.


---

Comment by jhpalmieri created at 2009-03-29 23:01:36

To summarize: these files are added:

sage/doc/en/a_tour_of_sage/eigen_plot.png
sage/doc/en/a_tour_of_sage/sin_plot.png
sage/doc/en/bordeaux_2008/birch.png
sage/doc/en/bordeaux_2008/modpcurve.png

You can test this by viewing the documentation (html or pdf version) as is, then apply the patch, rebuild, and view the new documentation.  The pictures should appear in the second version.


---

Comment by mabshoff created at 2009-04-06 00:33:56

This patch will need to be accomplished by a patch that adds those file to MANIFEST.in. Otherwise the repo will be broken for a fresh build.

Cheers,

Michael


---

Comment by jhpalmieri created at 2009-04-06 03:55:19

I've added a line adding all .png files in the doc directory; is that okay?


---

Comment by jhpalmieri created at 2009-04-06 03:57:19

(Oops -- if this patch is too big, delete it: the link in the summary points to the new patch.)


---

Comment by mabshoff created at 2009-04-06 04:26:28

The patch is fine, it isn't too large and we just don't want spkgs attached here.

I am not happy with the MANIFEST.in changes since if one does build the documentation using pngs instead of jsmath you end up with a boatload of crap in the spkg. You should add the four files explicitly to MANIFEST.in - this is the only true and optimal patch IMHO.

Cheers,

Michael


---

Comment by jhpalmieri created at 2009-04-06 05:12:19

Okay.  Note that this means that if someone decides to add pictures to the tutorial, for example (people requested this a long time ago for the plotting section), then they'll have to add those individually, too. It might get to be a little tedious after a while...


---

Attachment


---

Comment by mabshoff created at 2009-04-06 05:22:11

Replying to [comment:8 jhpalmieri]:
> Okay.  Note that this means that if someone decides to add pictures to the tutorial, for example (people requested this a long time ago for the plotting section), then they'll have to add those individually, too. It might get to be a little tedious after a while...

Well, you can recursively include png images below a certain directory for example, but I will catch any issue with pics being added to the documentation, but not in MANIFEST.in. I will review this patch shortly.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-06 05:30:26

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-06 05:32:54

Resolution: fixed


---

Comment by mabshoff created at 2009-04-06 05:32:54

Merged in Sage 3.4.1.rc1.

Cheers,

Michael
