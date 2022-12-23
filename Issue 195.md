# Issue 195: Can't compile spyx files with hyphens in names

Issue created by migration from https://trac.sagemath.org/ticket/195

Original creator: kedlaya

Original creation time: 2007-01-17 20:27:37

Assignee: was

The syntax
   attach "filename.spyx"
fails when filename contains a hyphen.



---

Comment by was created at 2007-01-19 10:45:07

Resolution: fixed


---

Comment by was created at 2007-01-19 10:45:07

fixed


```
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1169203338 28800
# Node ID 08b37570702281f7b6208e4df5871cc07c19250b
# Parent  405159b758a0c2d6c4b4e0836e25ae1753fb88d8
Trac #195 -- fix bug that Kiran Kedlaya reported that spyx files with funny filenames don't work.

diff -r 405159b758a0 -r 08b375707022 sage/misc/sagex.py
--- a/sage/misc/sagex.py        Fri Jan 19 02:31:01 2007 -0800
+++ b/sage/misc/sagex.py        Fri Jan 19 02:42:18 2007 -0800
@@ -106,7 +106,8 @@ def sagex(filename, verbose=False, compi
     if filename[-5:] != '.spyx':
         print "File (=%s) must have extension .spyx"%filename
 
-    base = os.path.split(os.path.splitext(filename)[0])[1]
+    clean_filename = sanitize(filename)
+    base = os.path.split(os.path.splitext(clean_filename)[0])[1]
 
     build_dir = '%s/%s'%(SPYX_TMP, base)
     if os.path.exists(build_dir):
@@ -151,8 +152,8 @@ def sagex(filename, verbose=False, compi
     # increment the sequence number so will use a different one next time.
     sequence_number[base] += 1
 
-    additional_source_files = ",".join(["'"+os.path.abspath(os.curdir)+"/"+filename+"'" \
-                                        for filename in additional_source_files])
+    additional_source_files = ",".join(["'"+os.path.abspath(os.curdir)+"/"+fname+"'" \
+                                        for fname in additional_source_files])
     
     pyx = '%s/%s.pyx'%(build_dir, name)
     open(pyx,'w').write(F)
@@ -334,3 +335,23 @@ def f(%s):
                                          create_local_c_file=False)
     return d['f']
     
+
+
+def sanitize(f):
+    """
+    Given a filename f, replace it by a filename that is a valid Python
+    module name.
+
+    This means that the characters are all alphanumeric or _'s and
+    doesn't begin with a numeral.
+    """
+    s = ''
+    if f[0].isdigit():
+        s += '_'
+    for a in f:
+        if a.isalnum():
+            s += a
+        else:
+            s += '_'
+    return s
+
```

