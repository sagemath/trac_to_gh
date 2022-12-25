# Issue 8990: update MPIR 1.2.2 license information as requested by upstream

archive/issues_008990.json:
```json
{
    "body": "Assignee: tbd\n\nAs description, let me just post the diff of the new SPKG.txt of the new mpir-1.2.2.p1.spkg (with respect to the SPKG.txt of mpir-1.2.2.p0.spkg) that I'll upload in a minute:\n\n```\n--- a/SPKG.txt  Tue Jan 05 20:49:53 2010 +0000\n+++ b/SPKG.txt  Tue May 18 23:35:30 2010 +0200\n@@ -4,13 +4,14 @@\n \n MPIR is an open source multiprecision integer library derived from\n version 4.2.1 of the GMP (GNU Multi Precision) project (which was\n-licensed LGPL v2+).\n+licensed LGPL v2+). Note MPIR 1.2.2 is overall LGPL v3+ due to the\n+inclusion of an LGPL v3 file (mpf/set_str.c).\n \n See http://www.mpir.org\n \n == License ==\n \n- * LGPL V2+\n+ * LGPL V3+\n \n == SPKG Maintainers ==\n \n@@ -26,6 +27,20 @@\n \n == Changelog == \n \n+=== mpir-1.2.2.p1 (Georg S. Weber, May 18th 2010) ===\n+ * Update the License information (e.g. above), as kindly requested\n+   on the MPIR project homepage (see \"http://www.mpir.org/past.html\"):\n+   \"... Note MPIR 1.2.2 is overall LGPL v3+ due to us accidentally including\n+    an LGPL v3 file (mpf/set_str.c). Please distribute this version of the\n+    library under the terms of this license! ...\"\n+   (According to \"http://trac.mpir.org/mpir_trac/ticket/71\", this LGPL v3 file\n+   stems from (patches for) GMP 4.2.4 in the year 2008.)\n+   Also copied two new files \"gpl-3.0.txt\" and \"lgpl-3.0.txt\" under src/, taken\n+   from the updated mpir-1.2.2 \"vanilla\" tarball downloaded under the link:\n+       http://www.mpir.org/mpir-1.2.2.tar.gz\n+   According to private communication with Bill Hart (MPIR upstream), this\n+   addition of two files was the only change done to the tarball itself.\n+\n === mpir-1.2.2.p0 (David Kirkby, January 5th 2010) ===\n  * 7849. Included two header files so MPIR builds with Sun\n   studio if configured with  --enable-cxx and the newer\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/8990\n\n",
    "created_at": "2010-05-18T21:46:52Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "update MPIR 1.2.2 license information as requested by upstream",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8990",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```
Assignee: tbd

As description, let me just post the diff of the new SPKG.txt of the new mpir-1.2.2.p1.spkg (with respect to the SPKG.txt of mpir-1.2.2.p0.spkg) that I'll upload in a minute:

```
--- a/SPKG.txt  Tue Jan 05 20:49:53 2010 +0000
+++ b/SPKG.txt  Tue May 18 23:35:30 2010 +0200
@@ -4,13 +4,14 @@
 
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
 
@@ -26,6 +27,20 @@
 
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

Issue created by migration from https://trac.sagemath.org/ticket/8990





---

archive/issue_comments_082974.json:
```json
{
    "body": "The link to the new spkg is:\n\nhttp://sage.math.washington.edu/home/weberg/spkg/mpir-1.2.2.p1.spkg",
    "created_at": "2010-05-18T21:59:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8990#issuecomment-82974",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

The link to the new spkg is:

http://sage.math.washington.edu/home/weberg/spkg/mpir-1.2.2.p1.spkg



---

archive/issue_comments_082975.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-18T21:59:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8990#issuecomment-82975",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082976.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-19T05:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8990#issuecomment-82976",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082977.json:
```json
{
    "body": "The changes are OK by me. The update spkg contains the following changes:\n\n* State in the file SPKG.txt that MPIR 1.2.2 is overall LGPLv3+ licensed.\n* Place a copy of the GPLv3 and LGPLv3 licenses under `src/`.",
    "created_at": "2010-05-19T05:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8990#issuecomment-82977",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The changes are OK by me. The update spkg contains the following changes:

* State in the file SPKG.txt that MPIR 1.2.2 is overall LGPLv3+ licensed.
* Place a copy of the GPLv3 and LGPLv3 licenses under `src/`.



---

archive/issue_comments_082978.json:
```json
{
    "body": "We should also really just upgrade to 2.0: #8664",
    "created_at": "2010-05-19T05:57:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8990#issuecomment-82978",
    "user": "https://github.com/mwhansen"
}
```

We should also really just upgrade to 2.0: #8664



---

archive/issue_comments_082979.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-19T07:52:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8990#issuecomment-82979",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_022003.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-05-19T07:52:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8990",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8990#event-22003"
}
```



---

archive/issue_comments_082980.json:
```json
{
    "body": "Replying to [comment:3 mhansen]:\n> We should also really just upgrade to 2.0: #8664\n\n\nSee my comment(s) there.",
    "created_at": "2010-05-19T09:46:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8990",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8990#issuecomment-82980",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Replying to [comment:3 mhansen]:
> We should also really just upgrade to 2.0: #8664


See my comment(s) there.
