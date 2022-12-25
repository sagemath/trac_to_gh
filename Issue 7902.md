# Issue 7902: scipy-0.7.p3: misbuilt silently, due to missing perl modules

archive/issues_007902.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nThis is similar to #5517.\n\nThe error reported by scipy-0.7.p3 is:\n\n```\nCan't locate File/Copy.pm in @INC (@INC contains: /etc/perl /usr/local/lib/perl/5.10.0 /usr/local/share/perl/5.10.0 /usr/lib/perl5 /usr/share/perl5 /usr/lib/perl/5.10 /usr/share/perl/5.10 /usr/local/lib/site_perl .) at ./copy_patches.pl line 2.\n```\n\nHowever, the `spkg-install` here is actually a shell script which calls the perl script (`copy_patches.pl`), *but it doesn't check the exit status*. Therefore, even though the perl script is aborted, the spkg-install continues without a real warning.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7902\n\n",
    "created_at": "2010-01-12T04:58:09Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "scipy-0.7.p3: misbuilt silently, due to missing perl modules",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7902",
    "user": "https://github.com/tornaria"
}
```
Assignee: GeorgSWeber

This is similar to #5517.

The error reported by scipy-0.7.p3 is:

```
Can't locate File/Copy.pm in @INC (@INC contains: /etc/perl /usr/local/lib/perl/5.10.0 /usr/local/share/perl/5.10.0 /usr/lib/perl5 /usr/share/perl5 /usr/lib/perl/5.10 /usr/share/perl/5.10 /usr/local/lib/site_perl .) at ./copy_patches.pl line 2.
```

However, the `spkg-install` here is actually a shell script which calls the perl script (`copy_patches.pl`), *but it doesn't check the exit status*. Therefore, even though the perl script is aborted, the spkg-install continues without a real warning.

Issue created by migration from https://trac.sagemath.org/ticket/7902





---

archive/issue_comments_068602.json:
```json
{
    "body": "Updated spkg at http://sage.math.washington.edu/home/tornaria/spkg/scipy-0.7.p4.spkg.\nHere's the complete diff for reference:\n\n```\ndiff -r 51b50077f1c9 -r a5fb4ead3bf9 SPKG.txt\n--- a/SPKG.txt  Wed Nov 11 21:59:39 2009 -0800\n+++ b/SPKG.txt  Tue Jan 12 03:08:14 2010 -0200\n@@ -7,6 +7,9 @@\n \n == Changelog ==\n \n+=== scipy-0.7.0.p4 (Gonzalo Tornaria; 12 Jan 2010) ===\n+ * Fixed #7902 by replacing copy_patches.pl by copy_patches.sh\n+\n === scipy-0.7.0.p3 (Mike Hansen; 12 Nov 2009) ===\n  * Fixed #6825 by adding a patch to scipy/stats/mstats_basic.py\n \ndiff -r 51b50077f1c9 -r a5fb4ead3bf9 copy_patches.pl\n--- a/copy_patches.pl   Wed Nov 11 21:59:39 2009 -0800\n+++ /dev/null   Thu Jan 01 00:00:00 1970 +0000\n@@ -1,21 +0,0 @@\n-#!/usr/bin/env perl\n-use File::Copy;\n-\n-$ver_string = `sage_fortran --version`;\n-if ($ver_string =~ m/G95/)\n-{\n-    print \"Using g95\";\n-    copy(\"patches/setup.py.integrate\", \"src/scipy/integrate/setup.py\");\n-    copy(\"patches/setup.py.optimize\",\"src/scipy/optimize/setup.py\");\n-    copy(\"patches/setup.py.special\",\"src/scipy/special/setup.py\");\n-    copy(\"patches/setup.py.interpolate\",\"src/scipy/interpolate/setup.py\");\n-    copy(\"patches/setup.py.odr\", \"src/scipy/odr/setup.py\");\n-    copy(\"patches/setup.py.stats\", \"src/scipy/stats/setup.py\");\n-}\n-\n-# The following patch (optimize.py) is a temporary fix already included upstream.\n-copy(\"patches/optimize.py\",\"src/scipy/optimize/optimize.py\");\n-\n-\n-# Fix an incorrect assert\n-copy(\"patches/mstats_basic.py\",\"src/scipy/stats/mstats_basic.py\");\ndiff -r 51b50077f1c9 -r a5fb4ead3bf9 copy_patches.sh\n--- /dev/null   Thu Jan 01 00:00:00 1970 +0000\n+++ b/copy_patches.sh   Tue Jan 12 03:08:14 2010 -0200\n@@ -0,0 +1,23 @@\n+#!/usr/bin/env bash\n+\n+# abort on error --- the spkg-install will catch it\n+set -e\n+\n+VER_STRING=\"`sage_fortran --version`\" \n+case \"$VER_STRING\" in \n+    G95*) \n+        echo \"Using g95\" \n+        cp \"patches/setup.py.integrate\"  \"src/scipy/integrate/setup.py\"\n+        cp \"patches/setup.py.optimize\" \"src/scipy/optimize/setup.py\"\n+        cp \"patches/setup.py.special\" \"src/scipy/special/setup.py\"\n+        cp \"patches/setup.py.interpolate\" \"src/scipy/interpolate/setup.py\"\n+        cp \"patches/setup.py.odr\"  \"src/scipy/odr/setup.py\"\n+        cp \"patches/setup.py.stats\"  \"src/scipy/stats/setup.py\"\n+        ;; \n+esac \n+\n+# The following patch (optimize.py) is a temporary fix already included upstream.\n+cp \"patches/optimize.py\" \"src/scipy/optimize/optimize.py\"\n+\n+# Fix an incorrect assert\n+cp \"patches/mstats_basic.py\" \"src/scipy/stats/mstats_basic.py\"\ndiff -r 51b50077f1c9 -r a5fb4ead3bf9 spkg-install\n--- a/spkg-install      Wed Nov 11 21:59:39 2009 -0800\n+++ b/spkg-install      Tue Jan 12 03:08:14 2010 -0200\n@@ -1,9 +1,16 @@\n #!/bin/sh\n \n+if [ \"$SAGE_LOCAL\" = \"\" ]; then \n+    echo \"SAGE_LOCAL undefined ... exiting\"; \n+    echo \"Maybe run 'sage -sh'?\" \n+    exit 1 \n+fi \n \n-\n-\n-./copy_patches.pl\n+./copy_patches.sh\n+if [ $? -ne 0 ]; then\n+    echo \"Error patching scipy\"\n+    exit 1\n+fi \n \n # These flags confuse numpy's distutils.   In particular,\n # if they are set empty bad things happen.\n@@ -36,11 +43,6 @@\n \n cd src/\n \n-if [ $? -ne 0 ]; then\n-    echo \"Error patching setup.py\"\n-    exit 1\n-fi \n-\n # Build \n python setup.py build\n if [ $? -ne 0 ]; then\n```\n",
    "created_at": "2010-01-12T05:38:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7902#issuecomment-68602",
    "user": "https://github.com/tornaria"
}
```

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

archive/issue_comments_068603.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-12T05:38:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7902#issuecomment-68603",
    "user": "https://github.com/tornaria"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068604.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-06T23:49:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7902#issuecomment-68604",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068605.json:
```json
{
    "body": "What a subtle bug. Thank you for tracking this down. The updated package [scipy-0.7.p4.spkg](http://sage.math.washington.edu/home/tornaria/spkg/scipy-0.7.p4.spkg) works as claimed.",
    "created_at": "2010-03-06T23:49:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7902#issuecomment-68605",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

What a subtle bug. Thank you for tracking this down. The updated package [scipy-0.7.p4.spkg](http://sage.math.washington.edu/home/tornaria/spkg/scipy-0.7.p4.spkg) works as claimed.



---

archive/issue_comments_068606.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-07T00:11:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7902#issuecomment-68606",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
