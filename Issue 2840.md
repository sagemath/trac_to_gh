# Issue 2840: notebook -- remove ALL unused javascript from js.py and DOCUMENT every single function

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-07 07:46:41

Assignee: boothby




---

Attachment


---

Comment by was created at 2008-04-07 08:04:08

This patch depends on #2825, which depends on others.  

If you just want to get something that works asap, apply this bundle *against sage-3.0-alpha*:

http://sage.math.washington.edu/home/was/patches/sage-2840.hg


---

Comment by was created at 2008-04-07 08:50:59

Bugs introduced by this patch:  
  * If you tab complete and their is a unique completion, the cursor doesn't get put at the right position.  
  * The left margin of the active an inactive and evaluated cells seems different, which is annoying an inconsistent.


---

Comment by was created at 2008-04-07 08:51:46

Bugs introduced by this patch:
   * Type `function_name([tab]` and the cursor jumps to the next cell instead of staying put.


---

Comment by boothby created at 2008-04-07 17:45:42

I'm giving this a positive review, though I haven't tested it yet.  My justification for this is that  (1) we need this patch badly, and (2) if any bugs are introduced by this, they will be easy to fix.


---

Comment by was created at 2008-04-07 17:52:38

Another bug introduced by this patch:
   * Sometimes the line count in js.py overestimates.  This is clearly documented, but it is more annoying now given that the code depends 100% on it.  We should fix this to always give exactly the right answer.


---

Comment by mabshoff created at 2008-04-07 18:31:05

Ok, applying against my tree has some rejects:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.0.alpha3/devel/sage$ patch -p1 --dry-run < trac_2840.patch
patching file sage/server/notebook/cell.py
patching file sage/server/notebook/config.py
patching file sage/server/notebook/css.py
patching file sage/server/notebook/js.py
Hunk #6 FAILED at 294.
Hunk #22 FAILED at 1895.
Hunk #23 succeeded at 1917 (offset -1 lines).
Hunk #24 succeeded at 1957 (offset -1 lines).
Hunk #25 succeeded at 2001 (offset -1 lines).
Hunk #26 succeeded at 2039 (offset -1 lines).
Hunk #27 succeeded at 2099 (offset -1 lines).
Hunk #28 succeeded at 2308 (offset -1 lines).
Hunk #29 succeeded at 2328 (offset -1 lines).
Hunk #30 succeeded at 2348 (offset -1 lines).
Hunk #31 succeeded at 2420 (offset -1 lines).
Hunk #32 succeeded at 2448 (offset -1 lines).
Hunk #33 succeeded at 2496 (offset -1 lines).
Hunk #34 succeeded at 2524 (offset -1 lines).
Hunk #35 succeeded at 2571 (offset -1 lines).
Hunk #36 succeeded at 2585 (offset -1 lines).
Hunk #37 succeeded at 2666 (offset -1 lines).
Hunk #38 succeeded at 2693 (offset -1 lines).
Hunk #39 succeeded at 2709 (offset -1 lines).
Hunk #40 succeeded at 2724 (offset -1 lines).
Hunk #41 succeeded at 2738 (offset -1 lines).
Hunk #42 succeeded at 2753 (offset -1 lines).
Hunk #43 succeeded at 2989 (offset -1 lines).
Hunk #44 succeeded at 3006 (offset -1 lines).
Hunk #45 succeeded at 3042 (offset -1 lines).
Hunk #46 succeeded at 3089 (offset -1 lines).
Hunk #47 succeeded at 3110 (offset -1 lines).
Hunk #48 succeeded at 3139 (offset -1 lines).
Hunk #49 succeeded at 3156 (offset -1 lines).
Hunk #50 succeeded at 3174 (offset -1 lines).
Hunk #51 succeeded at 3224 (offset -1 lines).
Hunk #52 succeeded at 3297 (offset -1 lines).
Hunk #53 succeeded at 3327 (offset -1 lines).
Hunk #54 succeeded at 3370 (offset -1 lines).
Hunk #55 succeeded at 3498 (offset -1 lines).
Hunk #56 succeeded at 3529 (offset -1 lines).
Hunk #57 succeeded at 3619 (offset -1 lines).
Hunk #58 succeeded at 3635 (offset -1 lines).
2 out of 58 hunks FAILED -- saving rejects to file sage/server/notebook/js.py.rej
patching file sage/server/notebook/keyboards.py
patching file sage/server/notebook/notebook.py
Hunk #1 succeeded at 1060 (offset 68 lines).
Hunk #2 succeeded at 1186 (offset 68 lines).
Hunk #3 succeeded at 1807 (offset 68 lines).
Hunk #4 succeeded at 2000 (offset 68 lines).
Hunk #5 succeeded at 2042 (offset 68 lines).
patching file sage/server/notebook/tutorial.py
patching file sage/server/notebook/twist.py
patching file sage/server/notebook/worksheet.py
Hunk #2 succeeded at 875 (offset -1 lines).
Hunk #3 succeeded at 941 (offset -1 lines).
```

I did apply #2826, so that is either the problem or I am missing some commits. I would prefer to get a rebased patch and not unbundle a 400 kb bundle ;)

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-07 19:45:41

version of was' patch that I merged


---

Attachment

Patch for the two hunks that I merged manually


---

Comment by mabshoff created at 2008-04-07 19:46:41

The diff between the final merged version and he one provided by was as a reference


---

Attachment

Merged trac_2840-good-hunks.patch and trac_2840-manually_merged-hunks.patch in Sage 3.0.alpha3.


---

Comment by mabshoff created at 2008-04-07 19:47:15

Resolution: fixed
