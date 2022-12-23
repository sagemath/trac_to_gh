# Issue 6997: minor typo in Constructions documentation

Issue created by migration from https://trac.sagemath.org/ticket/6997

Original creator: mvngu

Original creation time: 2009-09-22 22:22:55

Assignee: tba

CC:  mariah.lenox@gmail.com wdj

Mariah Lenox reports a typo in the Construction Guide at this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/b370c14dea509a7c) thread:

```
A minor typo in the Constructions documentation.  The
Constructions documentation says to send corrections
to sage-devel.

# HG changeset patch
# User Mariah Lenox <mariah.le...@gmail.com>
# Date 1253652415 14400
# Node ID bd65499b09ca9c88108908a609648850433dda8a
# Parent  40fe66e6c2b07677706fd983a6be6f3eb86060c5
user: Mariah Lenox <mariah.le...@gmail.com>
branch 'default'
changed doc/en/constructions/interface_issues.rst

diff -r 40fe66e6c2b0 -r bd65499b09ca doc/en/constructions/
interface_issues.rst
--- a/doc/en/constructions/interface_issues.rst Mon Sep 21 09:59:54
2009 -0400
+++ b/doc/en/constructions/interface_issues.rst Tue Sep 22 16:46:55
2009 -0400
@@ -549,7 +549,7 @@
 some of the GAP databases have to be added separately, and
 Singular. Adding Singular was not easy, due to the difficulty of
 compiling Singular from source. Version 0.9 was released in
-November. This version when through 34 releases! As of version
+November. This version went through 34 releases! As of version
 0.9.34 (definitely by version 0.10.0), Maxima and clisp were
 included with Sage. Version 0.10.0 was released January 12, 2006.
 The release of Sage 1.0 was made early February, 2006. As of
@@ -559,4 +559,4 @@
 such as assistance in compiling on various OS's. Generally code
 authors are acknowledged in the AUTHOR section of the Python
 docstring of their file and the credits section of the Sage
-website.
\ No newline at end of file
+website. 
```



---

Attachment


---

Comment by mvngu created at 2009-09-23 00:20:27

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 09:40:17

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
