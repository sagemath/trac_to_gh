# Issue 7196: SageNB: Reorganize the JS/Java/CSS/HTML "data" directory

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2009-10-12 17:16:48

Assignee: boothby

CC:  timdumol was

Reorganize `sagenb/data` around packages.


---

Attachment

SageNB data/ reorg part A: Shuffle files and directories.  Apply this patch first.


---

Comment by mpatel created at 2009-10-12 17:38:44

SageNB data/ reorg part B: Fix broken paths. Apply this patch second.


---

Comment by mpatel created at 2009-10-12 17:40:49

Changing status from new to needs_review.


---

Attachment

I made the change in two parts, since the shuffle slowed Mercurial significantly.


---

Comment by was created at 2009-10-15 01:14:00

You didn't mention it, but one must *MANUALLY* move data/java/jmol to data/jmol after applying this patch, since jmol isn't under revision control, and the path to jmol was changed in twist.py.


---

Comment by was created at 2009-10-15 01:24:39

positive review, and merged into sagenb-0.3.1, which has been posted here:

 http://sage.math.washington.edu/home/wstein/patches/sagenb/


---

Comment by was created at 2009-10-15 01:24:39

Resolution: fixed


---

Attachment

Update MANIFEST.in.
