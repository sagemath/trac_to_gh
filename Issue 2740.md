# Issue 2740: Downloading and uploading folders of worksheets

Issue created by migration from https://trac.sagemath.org/ticket/2740

Original creator: jason

Original creation time: 2008-03-31 15:54:01

Assignee: boothby

To ease migration between, for example, vmware images, it would be nice to be able to download and upload entire folders of worksheets, instead of just one at a time.  Or even beyond that, download/upload everything related to your notebook account.


---

Comment by jason created at 2008-11-14 05:04:05

we already have the checkboxes, so maybe just another menu option that would take the checked worksheets and make a zip of all the corresponding sws files.  Just a zip of all the sws files should do; maybe call it a snb for a sage note book?  The upload code then just double checks for sws files when it unzips and imports each one.


---

Attachment

This should be fixed to be non-blocking, possibly even with feedback (as it might be slow).


---

Attachment

allows downloading of checked worksheets only


---

Comment by was created at 2009-04-20 02:11:08

REFEREE REPORT:

I love this!

1. I think this should go in even without the non-blocking option.   It can be an option in the notebook command to turn this on, with it off by default.   Then on public servers people keep it off, but for their own servers (the vast majority), it is on.

2. The upload screen says: "Upload worksheet (an sws or txt file) to the Sage Notebook".  It should also say that one can upload a zip archive.

3. It would be nice if the filename of the sws could be included in the worksheet name, optionally.  My students always seem to name their sws filename right, but often forgot to actually rename their worksheets.  This causes me a *massive* amount of work to track down.


---

Comment by was created at 2009-04-28 23:35:40

I'm changing this to a positive review, because 1-3 above are just minor nitpicks, and can all easily be fixed/polished later.


---

Comment by mabshoff created at 2009-04-30 07:29:05

Merged both patches in Sage 3.4.2.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-30 07:29:05

Resolution: fixed
