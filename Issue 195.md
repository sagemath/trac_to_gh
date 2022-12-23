# Issue 195: Can't compile spyx files with hyphens in names

archive/issues_000195.json:
```json
{
    "body": "Assignee: was\n\nThe syntax\n   attach \"filename.spyx\"\nfails when filename contains a hyphen.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/195\n\n",
    "created_at": "2007-01-17T20:27:37Z",
    "labels": [
        "packages: standard",
        "minor",
        "bug"
    ],
    "title": "Can't compile spyx files with hyphens in names",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/195",
    "user": "kedlaya"
}
```
Assignee: was

The syntax
   attach "filename.spyx"
fails when filename contains a hyphen.


Issue created by migration from https://trac.sagemath.org/ticket/195





---

archive/issue_comments_000889.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-19T10:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/195",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/195#issuecomment-889",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_000890.json:
```json
{
    "body": "fixed\n\n\n```\n# HG changeset patch\n# User William Stein <wstein@gmail.com>\n# Date 1169203338 28800\n# Node ID 08b37570702281f7b6208e4df5871cc07c19250b\n# Parent  405159b758a0c2d6c4b4e0836e25ae1753fb88d8\nTrac #195 -- fix bug that Kiran Kedlaya reported that spyx files with funny filenames don't work.\n\ndiff -r 405159b758a0 -r 08b375707022 sage/misc/sagex.py\n--- a/sage/misc/sagex.py        Fri Jan 19 02:31:01 2007 -0800\n+++ b/sage/misc/sagex.py        Fri Jan 19 02:42:18 2007 -0800\n@@ -106,7 +106,8 @@ def sagex(filename, verbose=False, compi\n     if filename[-5:] != '.spyx':\n         print \"File (=%s) must have extension .spyx\"%filename\n \n-    base = os.path.split(os.path.splitext(filename)[0])[1]\n+    clean_filename = sanitize(filename)\n+    base = os.path.split(os.path.splitext(clean_filename)[0])[1]\n \n     build_dir = '%s/%s'%(SPYX_TMP, base)\n     if os.path.exists(build_dir):\n@@ -151,8 +152,8 @@ def sagex(filename, verbose=False, compi\n     # increment the sequence number so will use a different one next time.\n     sequence_number[base] += 1\n \n-    additional_source_files = \",\".join([\"'\"+os.path.abspath(os.curdir)+\"/\"+filename+\"'\" \\\n-                                        for filename in additional_source_files])\n+    additional_source_files = \",\".join([\"'\"+os.path.abspath(os.curdir)+\"/\"+fname+\"'\" \\\n+                                        for fname in additional_source_files])\n     \n     pyx = '%s/%s.pyx'%(build_dir, name)\n     open(pyx,'w').write(F)\n@@ -334,3 +335,23 @@ def f(%s):\n                                          create_local_c_file=False)\n     return d['f']\n     \n+\n+\n+def sanitize(f):\n+    \"\"\"\n+    Given a filename f, replace it by a filename that is a valid Python\n+    module name.\n+\n+    This means that the characters are all alphanumeric or _'s and\n+    doesn't begin with a numeral.\n+    \"\"\"\n+    s = ''\n+    if f[0].isdigit():\n+        s += '_'\n+    for a in f:\n+        if a.isalnum():\n+            s += a\n+        else:\n+            s += '_'\n+    return s\n+\n```\n",
    "created_at": "2007-01-19T10:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/195",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/195#issuecomment-890",
    "user": "was"
}
```

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

