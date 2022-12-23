# Issue 130: problem with multiline history recall in IPython

Issue created by migration from https://trac.sagemath.org/ticket/130

Original creator: nbruin

Original creation time: 2006-10-14 05:44:23

Assignee: was

If you type a loop at the sage prompt:

----------------------------------
sage: for i in range(1,3):
   ...:     print i
   ...:
1
2
----------------------------------

and then do an "arrow up" key, it seems like the loop is recalled. However, it seems only the first line is actually still there:

-----------------------------------------
sage: for i in range(1,3):
    print i
   ....:     print "done"
   ....:
done
done
-----------------------------------------


---

Comment by was created at 2007-01-12 23:23:06

In straight Ipython this problems doesn't happen.  In sage it does.  Tricky.  

PLAN:
   1. disable bits of how sage customizes ipython until find the problem.


---

Comment by was created at 2007-01-19 09:38:07

Fixed

```
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1169199334 28800
# Node ID e89f3913fa979d38a32cbcbef9b4d0af56c5de16
# Parent  cbda6c27c46e6e36c6c192550b172f79189ce974
Fix trac bug #130 -- multiline editing in Ipython/sage was broken.

diff -r cbda6c27c46e -r e89f3913fa97 sage/misc/interpreter.py
--- a/sage/misc/interpreter.py  Fri Jan 19 01:19:31 2007 -0800
+++ b/sage/misc/interpreter.py  Fri Jan 19 01:35:34 2007 -0800
@@ -152,7 +152,15 @@ def do_prefilter_paste(line, continuatio
 def do_prefilter_paste(line, continuation):
     """
     Alternate prefilter for input.
-    """
+
+    INPUT:
+        line -- a single line; must *not* have any newlines in it
+        continuation -- whether the input line is really part
+                     of the previous line, because of open parens or backslash.
+    """
+    if '\n' in line:
+        raise RuntimeError, "bug in function that calls do_prefilter_paste -- there can be no newlines in the input"
+    
     global attached
 
     # This is so it's OK to have lots of blank space at the
@@ -366,23 +374,34 @@ def process_file(name):
     return name2
     
 
-def sage_prefilter(self, line, continuation):
-    """
-    Alternate prefilter for input.
+def sage_prefilter(self, block, continuation):
+    """
+    SAGE's prefilter for input.  Given a string block (usually a
+    line), return the preparsed version of it.  
+
+    INPUT:
+        block -- string (usually a single line, but not always)
+        continuation -- whether or not this line is a continuation.
     """
     try:
-        line2 = do_prefilter_paste(line, continuation)
+        block2 = ''
+        for L in block.split('\n'):
+            M = do_prefilter_paste(L, continuation)
+            # The L[:len(L)-len(L.lstrip())]  business here preserves
+            # the whitespace at the beginning of L.
+            if block2 != '':
+                block2 += '\n'
+            block2 += L[:len(L)-len(L.lstrip())] + M 
 
     except None:
         
         print "WARNING: An error occured in the SAGE parser while"
-        print "parsing the following line:"
-        print line
+        print "parsing the following block:"
+        print block
         print "Please report this as a bug (include the output of typing '%hist')."
-        line2 = line
-        
-    from IPython.iplib import InteractiveShell
-    return InteractiveShell._prefilter(self, line2, continuation)
+        block2 = block
+        
+    return InteractiveShell._prefilter(self, block2, continuation)
 
```



---

Comment by was created at 2007-01-19 09:38:07

Resolution: fixed
