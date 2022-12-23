# Issue 216: optional_packages misparses

Issue created by migration from https://trac.sagemath.org/ticket/216

Original creator: nbruin

Original creation time: 2007-01-25 03:42:56

Assignee: boothby

The command optional_packages() raises an exception when run from the notebook:

```
File "/sage/local/lib/python2.5/site-packages/sage/misc/package.py", line 77, in optional_packages
    i = X.index('INSTALLED:')
ValueError: list.index(x): x not in list
```




---

Comment by was created at 2007-01-25 14:40:35

This was much more likely actually a problem with you maybe not having
a valid network connection, or the package list download getting corrupted (?).

I've made the code more robust for sage > 1.8.2.1


```
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1169735785 28800
# Node ID 9839fc0f4341de039cb16097a9d1b70f89a2ba9b
# Parent  5b7c4027bc1e4f035ae4d8be69efc256721258a3
trac #216 -- make optional_packages() command more robust.

diff -r 5b7c4027bc1e -r 9839fc0f4341 sage/misc/package.py
--- a/sage/misc/package.py      Thu Jan 25 06:25:41 2007 -0800
+++ b/sage/misc/package.py      Thu Jan 25 06:36:25 2007 -0800
@@ -73,9 +73,16 @@ def optional_packages():
         upgrade -- upgrade to latest version of core packages
                    (optional packages are not automatically upgraded).
     """
-    X = os.popen('sage -optional').read().split('\n')
-    i = X.index('INSTALLED:')
-    j = X.index('NOT INSTALLED:')
+    R = os.popen('sage -optional').read()
+    X = R.split('\n')
+    try:
+        i = X.index('INSTALLED:')
+        j = X.index('NOT INSTALLED:')
+    except ValueError, msg:
+        print R
+        print "Optional package list (shown above) appears to be currently not available or corrupted (network error?)."
+        return [], []
+    
     installed = []
     for k in X[i+1:]:
         if k == '':
```



---

Comment by was created at 2007-01-25 14:40:35

Resolution: fixed
