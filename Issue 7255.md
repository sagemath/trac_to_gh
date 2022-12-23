# Issue 7255: sagenb notebook: reset() causes the worksheet to stop working.  fix this.

Issue created by migration from https://trac.sagemath.org/ticket/7255

Original creator: was

Original creation time: 2009-10-20 19:28:49

Assignee: boothby




---

Comment by was created at 2009-10-20 22:10:25

patch to sagenb repo to fix this problem


---

Attachment

Reset doesn't touch _ names, so the fix is easy -- just use `import sagenb.notebook.interact as _interact_` then everywhere in code refer to `_interact_` instead of `sagenb.notebook.interact`.  This is better on many levels.


---

Comment by was created at 2009-10-20 22:11:26

Changing status from new to needs_review.


---

Comment by mhampton created at 2009-10-20 22:46:20

I'm getting these errors when applying the patch - what directory should this be done from?

applying /Users/mh/sagestuff/trac_sagenb_7255.patch
unable to find 'sagenb/data/sage/js/notebook_lib.js' for patching
1 out of 1 hunks FAILED -- saving rejects to file sagenb/data/sage/js/notebook_lib.js.rej
unable to find 'sagenb/notebook/interact.py' for patching
5 out of 5 hunks FAILED -- saving rejects to file sagenb/notebook/interact.py.rej
unable to find 'sagenb/notebook/worksheet.py' for patching
2 out of 2 hunks FAILED -- saving rejects to file sagenb/notebook/worksheet.py.rej
abort: patch failed to apply


---

Comment by mhampton created at 2009-10-21 02:02:11

OK, this seems to fix the problem.  I had some troubles with the patch at first but I think they are my fault.  Patch should be installed in 

spkg/build/sagenb-0.3.3/src/ 

and then

sage -python setup.py install

After doing this and doing sage -b, I got some strange errors about certain libraries, for example:

___gmpz_tdiv_r_2exp referenced from libmpfr expected to be defined in /Volumes/E/sage-4.1.2.rc0/local/lib/libgmp.3.dylib

My sage install originally was in /Volumes/E/sage-4.1.2.rc0, and then I upgraded and renamed it.  I think this can be ignored as a quirk of my setup, I've been doing quite a bit of cloning and some patch reviews on it, so I am going ahead and giving this a positive review.


---

Comment by was created at 2009-10-24 06:17:52

Resolution: fixed
