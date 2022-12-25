# Issue 159: bessel function bug

archive/issues_000159.json:
```json
{
    "body": "Assignee: @wdjoyner\n\nKeywords: bessel functions\n\nInconsistent behaviour:\n\n\n```\nsage: bessel_J(2,5.135,\"maxima\")\n0.00021138927993558099\nsage: bessel_J(2,5.136,\"maxima\")\n-0.00012828753895466338\nsage: bessel_J(2,5.135)\n0.0056034700919736996\nsage: bessel_J(2,5.136)\n0.0055939359540343476\nsage: bessel_J(2,5.136,\"pari\")\n0.0055939359540343476\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/159\n\n",
    "created_at": "2006-10-28T16:22:30Z",
    "labels": [
        "component: numerical",
        "bug"
    ],
    "title": "bessel function bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/159",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: @wdjoyner

Keywords: bessel functions

Inconsistent behaviour:


```
sage: bessel_J(2,5.135,"maxima")
0.00021138927993558099
sage: bessel_J(2,5.136,"maxima")
-0.00012828753895466338
sage: bessel_J(2,5.135)
0.0056034700919736996
sage: bessel_J(2,5.136)
0.0055939359540343476
sage: bessel_J(2,5.136,"pari")
0.0055939359540343476
```



Issue created by migration from https://trac.sagemath.org/ticket/159





---

archive/issue_comments_000709.json:
```json
{
    "body": "According to the docs (that wdj wrote) PARI and Maxima define the bessel_J function differently.  I added something about this to the documentation.\n\n\n```\n# HG changeset patch\n# User William Stein <wstein@gmail.com>\n# Date 1168648166 28800\n# Node ID 4ee645ba1eb61c95dbc383f05e8ea09da8682b7a\n# Parent  c7164849d131e768a44b8c02da9bde74bed9f801\naddressed ticket #159 -- inconsistent bessel_j by documenting behavior.\n\ndiff -r c7164849d131 -r 4ee645ba1eb6 sage/functions/special.py\n--- a/sage/functions/special.py Fri Jan 12 16:17:20 2007 -0800\n+++ b/sage/functions/special.py Fri Jan 12 16:29:26 2007 -0800\n@@ -419,9 +419,12 @@ def bessel_I(nu,z,alg = \"pari\",prec=53):\n         \n def bessel_J(nu,z,alg=\"pari\",prec=53):\n     r\"\"\"\n-    Implements the \"J-Bessel function\", or\n+    Return value of the \"J-Bessel function\", or\n     \"Bessel function, 1st kind\", with\n     index (or \"order\") nu and argument z.\n+\n+    WARNING: The pari and maxima definitions of ``the'' J-Bessel\n+    function are different (see below).\n \n     \\begin{verbatim}\n     Defn:\n@@ -459,6 +462,12 @@ def bessel_J(nu,z,alg=\"pari\",prec=53):\n         0.719622018527510801\n         sage: bessel_J(0,1)    # last few digits are random\n         0.765197686557966605\n+\n+    We illustrate that the pari and maxima definitions differ:\n+        sage: bessel_J(3,10,\"maxima\")   # last few digits are random\n+        0.0583793793051869\n+        sage: bessel_J(3,10,\"pari\")     # last few digits are random\n+        0.0000129283516457158\n \n     \"\"\"\n     if alg==\"pari\":\n```\n",
    "created_at": "2007-01-13T00:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/159#issuecomment-709",
    "user": "https://github.com/williamstein"
}
```

According to the docs (that wdj wrote) PARI and Maxima define the bessel_J function differently.  I added something about this to the documentation.


```
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1168648166 28800
# Node ID 4ee645ba1eb61c95dbc383f05e8ea09da8682b7a
# Parent  c7164849d131e768a44b8c02da9bde74bed9f801
addressed ticket #159 -- inconsistent bessel_j by documenting behavior.

diff -r c7164849d131 -r 4ee645ba1eb6 sage/functions/special.py
--- a/sage/functions/special.py Fri Jan 12 16:17:20 2007 -0800
+++ b/sage/functions/special.py Fri Jan 12 16:29:26 2007 -0800
@@ -419,9 +419,12 @@ def bessel_I(nu,z,alg = "pari",prec=53):
         
 def bessel_J(nu,z,alg="pari",prec=53):
     r"""
-    Implements the "J-Bessel function", or
+    Return value of the "J-Bessel function", or
     "Bessel function, 1st kind", with
     index (or "order") nu and argument z.
+
+    WARNING: The pari and maxima definitions of ``the'' J-Bessel
+    function are different (see below).
 
     \begin{verbatim}
     Defn:
@@ -459,6 +462,12 @@ def bessel_J(nu,z,alg="pari",prec=53):
         0.719622018527510801
         sage: bessel_J(0,1)    # last few digits are random
         0.765197686557966605
+
+    We illustrate that the pari and maxima definitions differ:
+        sage: bessel_J(3,10,"maxima")   # last few digits are random
+        0.0583793793051869
+        sage: bessel_J(3,10,"pari")     # last few digits are random
+        0.0000129283516457158
 
     """
     if alg=="pari":
```




---

archive/issue_events_000165.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-01-13T00:30:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/159",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/159#event-165"
}
```



---

archive/issue_comments_000710.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-13T00:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/159#issuecomment-710",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
