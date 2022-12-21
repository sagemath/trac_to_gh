# Issue 35: sage notebook load and DOS files

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-09-12 23:29:11

Assignee: somebody

*SAGE notebook load doesn't deal with DOS format files correctly,
  but python import does.



---

Comment by was created at 2007-01-19 11:13:27

Fixed.


```
# HG changeset patch
# User William Stein <wstein`@`gmail.com>
# Date 1169205070 28800
# Node ID 21687c50ad918c8af09e6338ea5835c19a43f819
# Parent  4c0bbf3706fad3a37607129c520366de1b20e452
fixed trac #35 -- laoding dos file didn't work.  (change split('\n') to splitlines())

diff -r 4c0bbf3706fa -r 21687c50ad91 sage/misc/preparser.py
--- a/sage/misc/preparser.py    Fri Jan 19 03:07:12 2007 -0800
+++ b/sage/misc/preparser.py    Fri Jan 19 03:11:10 2007 -0800
`@``@` -385,7 +385,7 `@``@` def preparse_file(contents, attached={},
     loaded_files = []
 
     F = []
-    A = contents.split('\n')
+    A = contents.splitlines()
     i = 0
     while i < len(A):
         L = A[i].rstrip()
```



---

Comment by was created at 2007-01-19 11:13:27

Resolution: fixed
