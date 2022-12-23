# Issue 6096: [with patch, needs review] Fix subtle bug in partition refinement

Issue created by migration from https://trac.sagemath.org/ticket/6096

Original creator: rlm

Original creation time: 2009-05-20 21:31:46

Assignee: rlm

CC:  sage-combinat

This patch includes a module which gives an extremely simple example of using the `partn_ref` module, which exposed the bug, whose fix is:


```
diff -r feb2d962bf2b -r f5d696c216ff sage/groups/perm_gps/partn_ref/double_coset.pyx
--- a/sage/groups/perm_gps/partn_ref/double_coset.pyx	Mon May 18 12:46:23 2009 -0700
+++ b/sage/groups/perm_gps/partn_ref/double_coset.pyx	Wed May 20 14:59:09 2009 -0700
@@ -540,7 +540,7 @@
         if not possible:
             possible = 1
             i = current_ps.depth
-            current_ps.depth = min(first_kids_are_same-1, current_kids_are_same-1)
+            current_ps.depth = current_kids_are_same-1
             if i == current_kids_are_same:
                 continue # main loop
             if index_in_fp_and_mcr < len_of_fp_and_mcr - 1:
```



---

Attachment

The module `refinement_list` was written by Nicolas Borie, and I just cleaned it up a bit. He and Nicolas Thiery found the bug and reported it to me. The fix was mine.


---

Comment by ekirkman created at 2009-05-21 20:39:11

Good explanation of one-line fix at Allegro.  Patch resolves issue and new doctest module is included.  No doctest failures on 4.0alpha0.


---

Comment by mabshoff created at 2009-05-22 13:33:12

Merged in Sage 4.0.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-22 13:33:12

Resolution: fixed
