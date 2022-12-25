# Issue 175: ceil or something is broken

archive/issues_000175.json:
```json
{
    "body": "Assignee: somebody\n\n```\nsage: ceil(10^16 * 1.0)\n 10000000000000000\n\nsage: ceil(10^17 * 1.0)\n 3125000000000000\n```\n\nright.......\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/175\n\n",
    "created_at": "2006-12-02T17:01:48Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "title": "ceil or something is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/175",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: somebody

```
sage: ceil(10^16 * 1.0)
 10000000000000000

sage: ceil(10^17 * 1.0)
 3125000000000000
```

right.......


Issue created by migration from https://trac.sagemath.org/ticket/175





---

archive/issue_events_000328.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-01-25T19:37:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/175",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/175#event-328"
}
```



---

archive/issue_comments_000810.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-25T19:37:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/175",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/175#issuecomment-810",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_000811.json:
```json
{
    "body": "Fixed.\n\nThis was a potentially terrible bug.  I'm glad you found it!!\n\n```\n# HG changeset patch\n# User William Stein <wstein@gmail.com>\n# Date 1169753572 28800\n# Node ID 7b1e4c3ea615683c3062256c16e72327c037117c\n# Parent  0652688d22a71a106562e9e3c10508365d663512\nTrac #175 -- fix ceil problem (really integer_part)\n\ndiff -r 0652688d22a7 -r 7b1e4c3ea615 sage/rings/real_mpfr.pyx\n--- a/sage/rings/real_mpfr.pyx  Thu Jan 25 11:27:04 2007 -0800\n+++ b/sage/rings/real_mpfr.pyx  Thu Jan 25 11:32:52 2007 -0800\n@@ -745,11 +745,20 @@ cdef class RealNumber(sage.structure.ele\n         EXAMPLE:\n             sage: a = 119.41212\n             sage: a.integer_part()\n-            119             \n+            119\n+\n+        A big number with no decimal point:\n+            sage: a = RR(10^17); a\n+            100000000000000000\n+            sage: a.integer_part()\n+            100000000000000000\n         \"\"\"\n         s = self.str(base=32, no_sci=True)\n         i = s.find(\".\")\n-        return Integer(s[:i], base=32)\n+        if i != -1:\n+            return Integer(s[:i], base=32)\n+        else:\n+            return Integer(s, base=32)\n \n     ########################\n     #   Basic Arithmetic\n@@ -981,6 +990,11 @@ cdef class RealNumber(sage.structure.ele\n             2\n             sage: (2.01).ceil()\n             3\n+\n+            sage: ceil(10^16 * 1.0)\n+            10000000000000000\n+            sage: ceil(10^17 * 1.0)\n+            100000000000000000\n         \"\"\"\n         cdef RealNumber x\n         x = self._new()\n```",
    "created_at": "2007-01-25T19:37:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/175",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/175#issuecomment-811",
    "user": "https://github.com/williamstein"
}
```

Fixed.

This was a potentially terrible bug.  I'm glad you found it!!

```
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1169753572 28800
# Node ID 7b1e4c3ea615683c3062256c16e72327c037117c
# Parent  0652688d22a71a106562e9e3c10508365d663512
Trac #175 -- fix ceil problem (really integer_part)

diff -r 0652688d22a7 -r 7b1e4c3ea615 sage/rings/real_mpfr.pyx
--- a/sage/rings/real_mpfr.pyx  Thu Jan 25 11:27:04 2007 -0800
+++ b/sage/rings/real_mpfr.pyx  Thu Jan 25 11:32:52 2007 -0800
@@ -745,11 +745,20 @@ cdef class RealNumber(sage.structure.ele
         EXAMPLE:
             sage: a = 119.41212
             sage: a.integer_part()
-            119             
+            119
+
+        A big number with no decimal point:
+            sage: a = RR(10^17); a
+            100000000000000000
+            sage: a.integer_part()
+            100000000000000000
         """
         s = self.str(base=32, no_sci=True)
         i = s.find(".")
-        return Integer(s[:i], base=32)
+        if i != -1:
+            return Integer(s[:i], base=32)
+        else:
+            return Integer(s, base=32)
 
     ########################
     #   Basic Arithmetic
@@ -981,6 +990,11 @@ cdef class RealNumber(sage.structure.ele
             2
             sage: (2.01).ceil()
             3
+
+            sage: ceil(10^16 * 1.0)
+            10000000000000000
+            sage: ceil(10^17 * 1.0)
+            100000000000000000
         """
         cdef RealNumber x
         x = self._new()
```
