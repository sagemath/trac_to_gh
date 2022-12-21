# Issue 7506: NotebookObject documentation is out of date

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2009-11-21 02:46:12

Assignee: boothby

CC:  jhpalmieri

Keywords: notebook, documentation, server

From Chris Wuthrich on sage-edu:
"From my perspective the biggest problem was that I did not allocate
enough resources to the virtual server the notebook was running on.
I was a bit disappointed with the documentation for setting up a
server etc. For instance the docstring of the notebook still contains
lines like
  nb = load('./sage/sage_notebook/nb.sobj')
which do not seem to apply any longer. "

So at least that needs to be cleaned up in notebook_object.py.


---

Attachment

This updates the notebook_object.py documentation and removes the warnings on build.


---

Comment by timdumol created at 2010-01-19 22:01:08

Adds `notebook_object` to the reference manual


---

Attachment

Related: #4574.


---

Comment by mpatel created at 2010-01-24 20:02:20

Several formatting tweaks.  ``sagenb`` repo.  Replaces previous.


---

Comment by mpatel created at 2010-01-24 20:20:21

Changing status from new to needs_review.


---

Attachment

Hi Dan, Jason, and Karl-Dieter -- Could you look at the patch and make/recommend improvements here or at [StartingTheNotebook](http://wiki.sagemath.org/StartingTheNotebook)?

Also, should the latter have a link to [JustEnoughSageServer](http://wiki.sagemath.org/DanDrake/JustEnoughSageServer)?


---

Comment by mpatel created at 2010-01-24 20:21:53

V2 just makes formatting changes.


---

Comment by mpatel created at 2010-01-24 20:26:09

A mock-up of V2 is [here](http://sage.math.washington.edu/home/mpatel/trac/7506/notebook_object.html).


---

Comment by ddrake created at 2010-01-25 04:08:16

Replying to [comment:2 mpatel]:
> Hi Dan, Jason, and Karl-Dieter -- Could you look at the patch and make/recommend improvements here or at [StartingTheNotebook](http://wiki.sagemath.org/StartingTheNotebook)?

The patch looks good. 
 
> Also, should the latter have a link to [JustEnoughSageServer](http://wiki.sagemath.org/DanDrake/JustEnoughSageServer)?

Sure, although that's a bit out of date now...it's still pretty useful, though. I'm planning on updating that page later this spring after Ubuntu Lucid is out.


---

Comment by mpatel created at 2010-02-06 16:30:23

Changing component from notebook to documentation.


---

Comment by mpatel created at 2010-02-06 16:31:54

Requesting an assist, if time permits.


---

Comment by jhpalmieri created at 2010-02-07 21:42:14

Given this documentation, should the file sagenb.notebook.notebook_object be added to the Sage reference manual?


---

Comment by jhpalmieri created at 2010-02-07 21:51:58

The patch looks good.  Here's an accompanying patch for the Sage library: for the notebook, the docs here seem like the ones people will want first, so I put it first in the reference manual.

(I feel like I'm missing something: this isn't already in the reference manual, is it?  I looked, but I didn't see it.)


---

Attachment

patch for the sage repo


---

Comment by jhpalmieri created at 2010-02-07 21:53:18

I'm willing to give the main patch a positive review.  If the patch for the ref manual is okay, the whole thing can get a positive review.


---

Comment by mpatel created at 2010-02-09 03:04:55

We should have added a note about [attachment:trac_7506-sage_core_lib-notebook-obj-ref.patch], which also adds `notebook_object` to the reference manual.  I'm not sure why it's missing the usual Mercurial header.

If Tim doesn't mind, I suggest that the release manager merge

 * [attachment:trac_7506-ref-manual.patch] into the sage repo.
 * [attachment:trac_7506-notebook_object-documentation.2.patch] into the sagenb repo.


---

Comment by mpatel created at 2010-02-09 03:04:55

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-02-09 04:06:00

Oops, I missed that patch -- I saw "replaces previous" on the next patch and immediately ignored everything above it.  The two Sage library patches are the same, so it's fine with me if Tim gets credit (I don't care either way about the attribution -- I just want to make sure this gets added to the reference manual).


---

Comment by mpatel created at 2010-02-11 15:03:29

Resolution: fixed
