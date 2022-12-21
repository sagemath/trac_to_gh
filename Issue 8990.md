# Issue 8990: update MPIR 1.2.2 license information as requested by upstream

Issue created by migration from Trac.

Original creator: GeorgSWeber

Original creation time: 2010-05-18 21:46:52

Assignee: tbd

As description, let me just post the diff of the new SPKG.txt of the new mpir-1.2.2.p1.spkg (with respect to the SPKG.txt of mpir-1.2.2.p0.spkg) that I'll upload in a minute:

```
--- a/SPKG.txt  Tue Jan 05 20:49:53 2010 +0000
+++ b/SPKG.txt  Tue May 18 23:35:30 2010 +0200
`@``@` -4,13 +4,14 `@``@`
 
 MPIR is an open source multiprecision integer library derived from
 version 4.2.1 of the GMP (GNU Multi Precision) project (which was
-licensed LGPL v2+).
+licensed LGPL v2+). Note MPIR 1.2.2 is overall LGPL v3+ due to the
+inclusion of an LGPL v3 file (mpf/set_str.c).
 
 See http://www.mpir.org
 
 == License ==
 
- * LGPL V2+
+ * LGPL V3+
 
 == SPKG Maintainers ==
 
`@``@` -26,6 +27,20 `@``@`
 
 == Changelog == 
 
+=== mpir-1.2.2.p1 (Georg S. Weber, May 18th 2010) ===
+ * Update the License information (e.g. above), as kindly requested
+   on the MPIR project homepage (see "http://www.mpir.org/past.html"):
+   "... Note MPIR 1.2.2 is overall LGPL v3+ due to us accidentally including
+    an LGPL v3 file (mpf/set_str.c). Please distribute this version of the
+    library under the terms of this license! ..."
+   (According to "http://trac.mpir.org/mpir_trac/ticket/71", this LGPL v3 file
+   stems from (patches for) GMP 4.2.4 in the year 2008.)
+   Also copied two new files "gpl-3.0.txt" and "lgpl-3.0.txt" under src/, taken
+   from the updated mpir-1.2.2 "vanilla" tarball downloaded under the link:
+       http://www.mpir.org/mpir-1.2.2.tar.gz
+   According to private communication with Bill Hart (MPIR upstream), this
+   addition of two files was the only change done to the tarball itself.
+
 === mpir-1.2.2.p0 (David Kirkby, January 5th 2010) ===
  * 7849. Included two header files so MPIR builds with Sun
   studio if configured with  --enable-cxx and the newer
```



---

Comment by GeorgSWeber created at 2010-05-18 21:59:21

The link to the new spkg is:

http://sage.math.washington.edu/home/weberg/spkg/mpir-1.2.2.p1.spkg


---

Comment by GeorgSWeber created at 2010-05-18 21:59:21

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-05-19 05:47:51

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-05-19 05:47:51

The changes are OK by me. The update spkg contains the following changes:

 * State in the file SPKG.txt that MPIR 1.2.2 is overall LGPLv3+ licensed.
 * Place a copy of the GPLv3 and LGPLv3 licenses under `src/`.


---

Comment by mhansen created at 2010-05-19 05:57:11

We should also really just upgrade to 2.0: #8664


---

Comment by mvngu created at 2010-05-19 07:52:07

Resolution: fixed


---

Comment by GeorgSWeber created at 2010-05-19 09:46:41

Replying to [comment:3 mhansen]:
> We should also really just upgrade to 2.0: #8664

See my comment(s) there.
