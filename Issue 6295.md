# Issue 6295: [with patch, needs review] build runs sphinx-build even on failure

Issue created by migration from https://trac.sagemath.org/ticket/6295

Original creator: burcin

Original creation time: 2009-06-15 09:52:30

Assignee: burcin

CC:  craigcitro

The build process runs sphinx-build even if a package fails to install. This hides the real error message from the spkg build.

This patch to spkg/install fixes the problem:


```
--- install.old 2009-06-12 08:46:55.000000000 +0200
+++ install     2009-06-15 11:47:02.000000000 +0200
@@ -357,6 +357,11 @@
 
 time make -f standard/deps $1
 
+if [ $? -ne 0 ]; then
+       echo "Error building Sage."
+       exit 1
+fi
+
 #Build the documentation
 rm -rf "$SAGE_ROOT"/devel/sage-main/doc/output/doctrees
 rm -rf "$SAGE_ROOT"/devel/sage-main/doc/en/reference/sage/*
```



---

Comment by craigcitro created at 2009-06-18 00:03:04

Resolution: fixed


---

Comment by craigcitro created at 2009-06-18 00:03:04

Yep, this is a great idea. There's no hg repository there, but I've added the changes.
