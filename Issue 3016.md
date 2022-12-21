# Issue 3016: [with patch, needs discussion ] javascript code editor spkg

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-04-24 08:51:55

Assignee: boothby

Edit Area is one of several javascript code editors.  Here is a simple (*very* simple) spkg which installs the necessary files in sage/data/extcode/notebook/javascript/edit_area/ and also a patch to enable the functionality.

The patch currently only enables the toggle switch (between new editor and old functionality) for the first cell (the input_cell_0 cell).  That should be enough to evaluate it, though.


---

Attachment


---

Attachment

Hi Jason,

instead of an spkg it would be customary to add the code directly to the extcode repo. What is the license of the code? The notebook code is supposed to be BSD since other projects might be able to pick it up that way.

If you want discussion of something like this you should mention it on sage-devel since trac is certainly the wrong place to discuss this and few people will find the ticket without it being mentioned on sage-devel.

Cheers,

Michael


---

Comment by jason created at 2008-04-24 18:10:31

I mentioned it in the thread where it was brought up in sage-devel.  I'll make another post too so that it's more visible.  As explained in the SPKG.txt file, the license is LGPL and Apache (dual-licensed).  I know that it would be customary to add the code directly, but since it was likely to be controversial (I just picked an editor and threw it in so we could at least play with it easily), I opted for the "optional package" route, at least for now.  I wrote the patch to notebook.py so that it would automatically take advantage of the package if it was there, but not change things if it wasn't.

Also, the spkg is barely minimally functional; it breaks everything too.  When the editor is clicked, nothing from the sage behavior works (tab completion, etc.).  Again, I just put it in there so people would have something they could start and play with.

Thanks for the pointers, though.

Jason


---

Comment by craigcitro created at 2008-06-20 04:51:18

Resolution: invalid


---

Comment by craigcitro created at 2008-06-20 04:51:18

This should be brought up as a thread on sage-devel.
