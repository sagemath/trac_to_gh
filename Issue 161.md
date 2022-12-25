# Issue 161: segfaults not picked up in doctests

archive/issues_000161.json:
```json
{
    "body": "Assignee: @williamstein\n\n`sage -t` does not pick up segfaults in doctests. For example this code currently causes a segmentation fault:\n\n\n```\nsage: x = 3**10000000\nsage: bits = 31699256\nsage: R = RealField(bits)\nsage: y = x._mpfr_(R)\nsage: z = y.log()\n```\n\n\nIf this appears in a doctest, then the test framework continues without comment, and prints \"All tests passed!\" at the end.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/161\n\n",
    "created_at": "2006-10-29T21:55:51Z",
    "labels": [
        "component: user interface",
        "critical",
        "bug"
    ],
    "title": "segfaults not picked up in doctests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/161",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: @williamstein

`sage -t` does not pick up segfaults in doctests. For example this code currently causes a segmentation fault:


```
sage: x = 3**10000000
sage: bits = 31699256
sage: R = RealField(bits)
sage: y = x._mpfr_(R)
sage: z = y.log()
```


If this appears in a doctest, then the test framework continues without comment, and prints "All tests passed!" at the end.


Issue created by migration from https://trac.sagemath.org/ticket/161





---

archive/issue_comments_000716.json:
```json
{
    "body": "I fixed this (and generally beefed up robustness of doctests to such things).\nThis will be in SAGE-1.5:\n\n\n```\nsha:~/s/local/bin was$ hg export 92\n# HG changeset patch\n# User William Stein <wstein@gmail.com>\n# Date 1162797238 28800\n# Node ID c89bcbe0a11a94137dc3581a75c9158cd39b44fb\n# Parent  edcb018e5a26dc2ae56cc87efdf891c56c09b94d\nBeefed up the doctesting in various ways to address Trac bug #161 (doctest silently failing on seg fault).\n\ndiff -r edcb018e5a26 -r c89bcbe0a11a sage-doctest\n--- a/sage-doctest      Fri Nov 03 06:54:40 2006 -0800\n+++ b/sage-doctest      Sun Nov 05 23:13:58 2006 -0800\n@@ -301,6 +301,9 @@ def test_file(file):\n         if 'Failed' in s or 'Error' in s:\n             delete_tmpfiles()\n             sys.exit(1)\n+        elif e != 0:\n+            print \"A mysterious error (perphaps a memory error?) occured, which may have crashed doctest.\"\n+            sys.exit(1)\n         else:\n             delete_tmpfiles()\n             sys.exit(0)\ndiff -r edcb018e5a26 -r c89bcbe0a11a sage-doctest_tex\n--- a/sage-doctest_tex  Fri Nov 03 06:54:40 2006 -0800\n+++ b/sage-doctest_tex  Sun Nov 05 23:13:58 2006 -0800\n@@ -155,7 +155,7 @@ def no_escapes(x):\n         k = j + x[j:].find(chr(109))\n         x = x[:j] + x[k+1:]\n \n-def test_session(S, verbose=False):\n+def test_session(S, verbose):\n     global E\n     \n     if verbose:\n@@ -195,7 +195,7 @@ def test_session(S, verbose=False):\n             i += 1\n             \n             \n-def test_file(file, start, stop):\n+def test_file(file, start, stop, verbose):\n     global ERRORS\n     name = os.path.basename(file)\n     name = name[:name.find(\".\")]\n@@ -205,7 +205,7 @@ def test_file(file, start, stop):\n \n         sessions = extract_python_doc(file)\n     else:\n-        print \"Skipping %s, unknown file type\"%file\n+        print \"Skipping %s; unknown file type\"%file\n         return 0\n     i = 0\n     for S in sessions:\n@@ -213,7 +213,7 @@ def test_file(file, start, stop):\n         try:\n             if i >= start:\n                 print \"Example %s (line %s)\"%(i,S[0][0])                        \n-                test_session(S, verbose=False)\n+                test_session(S, verbose=verbose)\n         except pexpect.TIMEOUT:\n             print \"Example %s (line %s)\"%(i,S[0][0])                        \n             print \"TIMEOUT!!\"\n@@ -233,15 +233,21 @@ def test_file(file, start, stop):\n         if stop != 0 and i > stop:\n             break\n     return 0\n-                \n+\n if __name__ ==  '__main__':\n     import os, sys\n     print ''\n     if len(sys.argv) == 1:\n-        print \"Usage: %s <filename.tex> [start number] [stop number]\"%(sys.argv[0])\n-        print \"Test the documentation in a latex file using SAGE.\"\n+        print \"Usage: %s [--verbose or -v] <filename.tex> [start number] [stop number]\"%(sys.argv[0])\n+        print \"Test the documentation in a .tex or .sage file using SAGE (via a pseudo-tty).\"\n         sys.exit(1)\n     else:\n+        verbose = False\n+        for i in range(1, len(sys.argv)):\n+            if sys.argv[i] in ['--verbose', '-verbose', '-v']:\n+                verbose = True\n+                del sys.argv[i]\n+                break\n         file = sys.argv[1]\n         start = 0\n         stop  = 0\n@@ -250,9 +256,21 @@ if __name__ ==  '__main__':\n         if len(sys.argv) > 3:\n             stop = int(sys.argv[3])\n         initialize_sage()\n-        if test_file(file, start, stop):\n+        if test_file(file, start, stop, verbose=verbose):\n             sys.exit(1)\n         if len(ERRORS) > 0:\n             print ERRORS\n             sys.exit(1)\n+        e = E.terminate(0)\n+        if e:\n+            print \" ** Unclean exit -- possibly a memory error or segmentation fault occured. ** \"\n+            sys.exit(1)\n+        try:\n+            # Hack to get around stupid pointless error message.\n+            def foo():\n+                pass\n+            E.__del__ = foo\n+            del E\n+        except:\n+            pass\n         sys.exit(0)\ndiff -r edcb018e5a26 -r c89bcbe0a11a sage-test\n--- a/sage-test Fri Nov 03 06:54:40 2006 -0800\n+++ b/sage-test Sun Nov 05 23:13:58 2006 -0800\n@@ -79,8 +79,8 @@ def test_file(F):\n             F = file        \n \n     base, ext = os.path.splitext(F)\n-    if use_sage_only or ext in ['.sage']:\n-        return test(F, 'doctest_tex')\n+    if use_sage_only or ext == '.sage':\n+        return test(F, 'doctest_tex ' + opts)\n     elif ext in ['.py', '.pyx', '.tex']:\n         return test(F, 'doctest '+opts)\n     elif os.path.isdir(F) and not (F[:1] == '.') \\\n\n```\n",
    "created_at": "2006-11-06T07:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/161#issuecomment-716",
    "user": "https://github.com/williamstein"
}
```

I fixed this (and generally beefed up robustness of doctests to such things).
This will be in SAGE-1.5:


```
sha:~/s/local/bin was$ hg export 92
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1162797238 28800
# Node ID c89bcbe0a11a94137dc3581a75c9158cd39b44fb
# Parent  edcb018e5a26dc2ae56cc87efdf891c56c09b94d
Beefed up the doctesting in various ways to address Trac bug #161 (doctest silently failing on seg fault).

diff -r edcb018e5a26 -r c89bcbe0a11a sage-doctest
--- a/sage-doctest      Fri Nov 03 06:54:40 2006 -0800
+++ b/sage-doctest      Sun Nov 05 23:13:58 2006 -0800
@@ -301,6 +301,9 @@ def test_file(file):
         if 'Failed' in s or 'Error' in s:
             delete_tmpfiles()
             sys.exit(1)
+        elif e != 0:
+            print "A mysterious error (perphaps a memory error?) occured, which may have crashed doctest."
+            sys.exit(1)
         else:
             delete_tmpfiles()
             sys.exit(0)
diff -r edcb018e5a26 -r c89bcbe0a11a sage-doctest_tex
--- a/sage-doctest_tex  Fri Nov 03 06:54:40 2006 -0800
+++ b/sage-doctest_tex  Sun Nov 05 23:13:58 2006 -0800
@@ -155,7 +155,7 @@ def no_escapes(x):
         k = j + x[j:].find(chr(109))
         x = x[:j] + x[k+1:]
 
-def test_session(S, verbose=False):
+def test_session(S, verbose):
     global E
     
     if verbose:
@@ -195,7 +195,7 @@ def test_session(S, verbose=False):
             i += 1
             
             
-def test_file(file, start, stop):
+def test_file(file, start, stop, verbose):
     global ERRORS
     name = os.path.basename(file)
     name = name[:name.find(".")]
@@ -205,7 +205,7 @@ def test_file(file, start, stop):
 
         sessions = extract_python_doc(file)
     else:
-        print "Skipping %s, unknown file type"%file
+        print "Skipping %s; unknown file type"%file
         return 0
     i = 0
     for S in sessions:
@@ -213,7 +213,7 @@ def test_file(file, start, stop):
         try:
             if i >= start:
                 print "Example %s (line %s)"%(i,S[0][0])                        
-                test_session(S, verbose=False)
+                test_session(S, verbose=verbose)
         except pexpect.TIMEOUT:
             print "Example %s (line %s)"%(i,S[0][0])                        
             print "TIMEOUT!!"
@@ -233,15 +233,21 @@ def test_file(file, start, stop):
         if stop != 0 and i > stop:
             break
     return 0
-                
+
 if __name__ ==  '__main__':
     import os, sys
     print ''
     if len(sys.argv) == 1:
-        print "Usage: %s <filename.tex> [start number] [stop number]"%(sys.argv[0])
-        print "Test the documentation in a latex file using SAGE."
+        print "Usage: %s [--verbose or -v] <filename.tex> [start number] [stop number]"%(sys.argv[0])
+        print "Test the documentation in a .tex or .sage file using SAGE (via a pseudo-tty)."
         sys.exit(1)
     else:
+        verbose = False
+        for i in range(1, len(sys.argv)):
+            if sys.argv[i] in ['--verbose', '-verbose', '-v']:
+                verbose = True
+                del sys.argv[i]
+                break
         file = sys.argv[1]
         start = 0
         stop  = 0
@@ -250,9 +256,21 @@ if __name__ ==  '__main__':
         if len(sys.argv) > 3:
             stop = int(sys.argv[3])
         initialize_sage()
-        if test_file(file, start, stop):
+        if test_file(file, start, stop, verbose=verbose):
             sys.exit(1)
         if len(ERRORS) > 0:
             print ERRORS
             sys.exit(1)
+        e = E.terminate(0)
+        if e:
+            print " ** Unclean exit -- possibly a memory error or segmentation fault occured. ** "
+            sys.exit(1)
+        try:
+            # Hack to get around stupid pointless error message.
+            def foo():
+                pass
+            E.__del__ = foo
+            del E
+        except:
+            pass
         sys.exit(0)
diff -r edcb018e5a26 -r c89bcbe0a11a sage-test
--- a/sage-test Fri Nov 03 06:54:40 2006 -0800
+++ b/sage-test Sun Nov 05 23:13:58 2006 -0800
@@ -79,8 +79,8 @@ def test_file(F):
             F = file        
 
     base, ext = os.path.splitext(F)
-    if use_sage_only or ext in ['.sage']:
-        return test(F, 'doctest_tex')
+    if use_sage_only or ext == '.sage':
+        return test(F, 'doctest_tex ' + opts)
     elif ext in ['.py', '.pyx', '.tex']:
         return test(F, 'doctest '+opts)
     elif os.path.isdir(F) and not (F[:1] == '.') \

```




---

archive/issue_comments_000717.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2006-11-06T07:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/161",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/161#issuecomment-717",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000167.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2006-11-06T07:41:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/161",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/161#event-167"
}
```
