# Issue 6625: manually removing executable bits doesn't work

Issue created by migration from https://trac.sagemath.org/ticket/6625

Original creator: mvngu

Original creation time: 2009-07-26 06:50:31

Assignee: cwitty

This is a follow up to #3687. Apparently, the issue of executable bits pop up again after they had been manually removed. That is, manually remove the executable bits of sage-banner, sage-gdb-commands, sage-maxima.lisp, and sage-verify-pyc. Then create a source distribution and you see those executable bits restored:

```
[mvngu@sage bin]$ pwd
/home/mvngu/release/sage-4.1.1.alpha1/local/bin
[mvngu@sage bin]$ hg st
M sage-README-osx.txt
M sage-banner
M sage-gdb-commands
M sage-maxima.lisp
M sage-verify-pyc
```

Somewhere a script called by the command

```
sage -sdist <version-number>
```

is restoring those executable bits.


---

Attachment

The `sage-make_devel_packages` explicitly set the x bit on all `sage-*` files.


---

Comment by wjp created at 2010-01-19 02:18:05

Changing status from new to needs_review.


---

Attachment

rebased against Sage 4.3.1.rc1; apply to SAGE_LOCAL/bin


---

Comment by mvngu created at 2010-01-19 17:28:33

The attachment [scripts_6625_no_x_bit.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6625/scripts_6625_no_x_bit.patch) fails to apply against Sage 4.3.1.rc1:

```
[mvngu@mod bin]$ pwd
/dev/shm/mvngu/sage-4.3.1.rc1/local/bin
[mvngu@mod bin]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6625/scripts_6625_no_x_bit.patch
adding scripts_6625_no_x_bit.patch to series file
[mvngu@mod bin]$ hg qpush
applying scripts_6625_no_x_bit.patch
patching file sage-make_devel_packages
Hunk #1 FAILED at 135
1 out of 1 hunks FAILED -- saving rejects to file sage-make_devel_packages.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh scripts_6625_no_x_bit.patch
[mvngu@mod bin]$ cat sage-make_devel_packages.rej 
--- sage-make_devel_packages
+++ sage-make_devel_packages
@@ -136,6 +136,8 @@
 rm -rf $SCRIPTS
 mkdir $SCRIPTS
 chmod +x sage-*
+chmod -x sage-README-osx.txt sage-banner sage-gdb-commands
+chmod -x sage-maxima.lisp sage-verify-pyc
 chmod +x dsage_*
 rm sage-*~
```

The failure results from #7975, which removes dsage from Sage and the patches on #7975 have been merged in Sage 4.3.1.rc1. The guilty line from [scripts_6625_no_x_bit.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6625/scripts_6625_no_x_bit.patch) is:

```
139	141	chmod +x dsage_*
```

Essentially the patch looks good. I have rebased it against Sage 4.3.1.rc1, so only my rebase [trac_6625-no-x-bit.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6625/trac_6625-no-x-bit.patch) needs reviewing.


---

Comment by wjp created at 2010-01-19 17:37:19

Changing status from needs_review to positive_review.


---

Comment by wjp created at 2010-01-19 17:37:19

Thanks. The rebase looks good to me.


---

Comment by mvngu created at 2010-01-24 02:22:34

Resolution: fixed


---

Comment by mvngu created at 2010-01-24 02:22:34

Merged [trac_6625-no-x-bit.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6625/trac_6625-no-x-bit.patch) in the script repository.
