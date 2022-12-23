# Issue 555: c_lib SConscript doesn't always copy new libcsage.dylib on a sage -b

Issue created by migration from https://trac.sagemath.org/ticket/555

Original creator: craigcitro

Original creation time: 2007-09-01 18:18:47

Assignee: craigcitro

If you have two branches, and you edit libcsage.dylib in one, then sage -b to the other, it doesn't (always? ever?) copy over the appropriate libcsage.dylib to /sage/local/lib.


---

Comment by craigcitro created at 2007-09-02 17:13:21

I'm pretty sure this is fixed. Basically, the problem is that scons doesn't want to look at a remote file (in our case $SAGE_ROOT/local/lib/libcsage.dylib) and see if it's up to date. The fix: just force it to copy the file over every time. Not the most elegant, but it works.

hg bundle is attached.


---

Comment by was created at 2007-09-03 03:02:08

I can't apply this patch no matter what I try...


---

Attachment


---

Attachment

patch for same hg bundle below


---

Attachment


---

Attachment

Attached two new bundles, total_trac_555.hg and total_trac_555_localbin.hg. The first is against the main sage repo, and the second is for $SAGE_ROOT/local/bin, as you might guess from the name. These take you from a clean 2.8.3 install to a version with a fully working c_lib recompilation on branch switch setup, with very few spurious copies. 

Let me know if people run into trouble; if you want to test it, do the following: make a new branch (called, say, foo) and apply the hg bundle, and then clone that (maybe call that bar). Then switch back and forth between foo and bar, and make sure that you see libcsage.dylib getting copied (along with a bunch of include files) every time you switch branches.


---

Comment by was created at 2007-09-03 21:15:21

I've pushed this all into the official repo.


---

Comment by was created at 2007-09-03 21:15:21

Resolution: fixed
