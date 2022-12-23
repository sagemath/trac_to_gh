# Issue 7902: scipy-0.7.p3: misbuilt silently, due to missing perl modules

Issue created by migration from https://trac.sagemath.org/ticket/7902

Original creator: tornaria

Original creation time: 2010-01-12 04:58:09

Assignee: GeorgSWeber

This is similar to #5517.

The error reported by scipy-0.7.p3 is:

```
Can't locate File/Copy.pm in @INC (@INC contains: /etc/perl /usr/local/lib/perl/5.10.0 /usr/local/share/perl/5.10.0 /usr/lib/perl5 /usr/share/perl5 /usr/lib/perl/5.10 /usr/share/perl/5.10 /usr/local/lib/site_perl .) at ./copy_patches.pl line 2.
```

However, the `spkg-install` here is actually a shell script which calls the perl script (`copy_patches.pl`), _but it doesn't check the exit status_. Therefore, even though the perl script is aborted, the spkg-install continues without a real warning.


---

Comment by tornaria created at 2010-01-12 05:38:40

Updated spkg at http://sage.math.washington.edu/home/tornaria/spkg/scipy-0.7.p4.spkg.
Here's the complete diff for reference:

```
diff -r 51b50077f1c9 -r a5fb4ead3bf9 SPKG.txt
--- a/SPKG.txt  Wed Nov 11 21:59:39 2009 -0800
+++ b/SPKG.txt  Tue Jan 12 03:08:14 2010 -0200
@@ -7,6 +7,9 @@
 
 == Changelog ==
 
+=== scipy-0.7.0.p4 (Gonzalo Tornaria; 12 Jan 2010) ===
+ * Fixed #7902 by replacing copy_patches.pl by copy_patches.sh
+
 === scipy-0.7.0.p3 (Mike Hansen; 12 Nov 2009) ===
  * Fixed #6825 by adding a patch to scipy/stats/mstats_basic.py
 
diff -r 51b50077f1c9 -r a5fb4ead3bf9 copy_patches.pl
--- a/copy_patches.pl   Wed Nov 11 21:59:39 2009 -0800
+++ /dev/null   Thu Jan 01 00:00:00 1970 +0000
@@ -1,21 +0,0 @@
-#!/usr/bin/env perl
-use File::Copy;
-
-$ver_string = `sage_fortran --version`;
-if ($ver_string =~ m/G95/)
-{
-    print "Using g95";
-    copy("patches/setup.py.integrate", "src/scipy/integrate/setup.py");
-    copy("patches/setup.py.optimize","src/scipy/optimize/setup.py");
-    copy("patches/setup.py.special","src/scipy/special/setup.py");
-    copy("patches/setup.py.interpolate","src/scipy/interpolate/setup.py");
-    copy("patches/setup.py.odr", "src/scipy/odr/setup.py");
-    copy("patches/setup.py.stats", "src/scipy/stats/setup.py");
-}
-
-# The following patch (optimize.py) is a temporary fix already included upstream.
-copy("patches/optimize.py","src/scipy/optimize/optimize.py");
-
-
-# Fix an incorrect assert
-copy("patches/mstats_basic.py","src/scipy/stats/mstats_basic.py");
diff -r 51b50077f1c9 -r a5fb4ead3bf9 copy_patches.sh
--- /dev/null   Thu Jan 01 00:00:00 1970 +0000
+++ b/copy_patches.sh   Tue Jan 12 03:08:14 2010 -0200
@@ -0,0 +1,23 @@
+#!/usr/bin/env bash
+
+# abort on error --- the spkg-install will catch it
+set -e
+
+VER_STRING="`sage_fortran --version`" 
+case "$VER_STRING" in 
+    G95*) 
+        echo "Using g95" 
+        cp "patches/setup.py.integrate"  "src/scipy/integrate/setup.py"
+        cp "patches/setup.py.optimize" "src/scipy/optimize/setup.py"
+        cp "patches/setup.py.special" "src/scipy/special/setup.py"
+        cp "patches/setup.py.interpolate" "src/scipy/interpolate/setup.py"
+        cp "patches/setup.py.odr"  "src/scipy/odr/setup.py"
+        cp "patches/setup.py.stats"  "src/scipy/stats/setup.py"
+        ;; 
+esac 
+
+# The following patch (optimize.py) is a temporary fix already included upstream.
+cp "patches/optimize.py" "src/scipy/optimize/optimize.py"
+
+# Fix an incorrect assert
+cp "patches/mstats_basic.py" "src/scipy/stats/mstats_basic.py"
diff -r 51b50077f1c9 -r a5fb4ead3bf9 spkg-install
--- a/spkg-install      Wed Nov 11 21:59:39 2009 -0800
+++ b/spkg-install      Tue Jan 12 03:08:14 2010 -0200
@@ -1,9 +1,16 @@
 #!/bin/sh
 
+if [ "$SAGE_LOCAL" = "" ]; then 
+    echo "SAGE_LOCAL undefined ... exiting"; 
+    echo "Maybe run 'sage -sh'?" 
+    exit 1 
+fi 
 
-
-
-./copy_patches.pl
+./copy_patches.sh
+if [ $? -ne 0 ]; then
+    echo "Error patching scipy"
+    exit 1
+fi 
 
 # These flags confuse numpy's distutils.   In particular,
 # if they are set empty bad things happen.
@@ -36,11 +43,6 @@
 
 cd src/
 
-if [ $? -ne 0 ]; then
-    echo "Error patching setup.py"
-    exit 1
-fi 
-
 # Build 
 python setup.py build
 if [ $? -ne 0 ]; then
```



---

Comment by tornaria created at 2010-01-12 05:38:40

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-03-06 23:49:23

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-06 23:49:23

What a subtle bug. Thank you for tracking this down. The updated package [scipy-0.7.p4.spkg](http://sage.math.washington.edu/home/tornaria/spkg/scipy-0.7.p4.spkg) works as claimed.


---

Comment by mhansen created at 2010-03-07 00:11:20

Resolution: fixed
