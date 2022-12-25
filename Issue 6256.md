# Issue 6256: bug in symbolic arithmetic with exp

archive/issues_006256.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @jasongrout\n\n\n```\nsage: var('kappa')\nkappa\nsage: x = sqrt(kappa)\nsage: F = exp(x)\nsage: F\ne^sqrt(kappa)\nsage: F/F\ne^(2*sqrt(kappa))\nsage: 1/F\ne^(-sqrt(kappa))\nsage: (1/F) * F\ne^(2*sqrt(kappa))\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6256\n\n",
    "created_at": "2009-06-10T08:48:57Z",
    "labels": [
        "component: symbolics",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "bug in symbolic arithmetic with exp",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6256",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

CC:  @jasongrout


```
sage: var('kappa')
kappa
sage: x = sqrt(kappa)
sage: F = exp(x)
sage: F
e^sqrt(kappa)
sage: F/F
e^(2*sqrt(kappa))
sage: 1/F
e^(-sqrt(kappa))
sage: (1/F) * F
e^(2*sqrt(kappa))
```


Issue created by migration from https://trac.sagemath.org/ticket/6256





---

archive/issue_comments_049874.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-13T22:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6256#issuecomment-49874",
    "user": "https://github.com/burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_049875.json:
```json
{
    "body": "Here is the fix for pynac:\n\n```\ndiff --git a/ginac/mul.cpp b/ginac/mul.cpp\n--- a/ginac/mul.cpp\n+++ b/ginac/mul.cpp\n@@ -1167,7 +1167,7 @@\n        if (cmpval != 0) {\n                return cmpval;\n        }\n-       if (seq.size() == 1 && overall_coeff.is_equal(_ex_1))\n+       if (seq.size() == 1 && overall_coeff.is_equal(_ex1))\n                return 0;\n        return 1;\n }\n```\n\n\nI'll post an updated spkg later together with a fix for #6244.",
    "created_at": "2009-06-13T22:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6256#issuecomment-49875",
    "user": "https://github.com/burcin"
}
```

Here is the fix for pynac:

```
diff --git a/ginac/mul.cpp b/ginac/mul.cpp
--- a/ginac/mul.cpp
+++ b/ginac/mul.cpp
@@ -1167,7 +1167,7 @@
        if (cmpval != 0) {
                return cmpval;
        }
-       if (seq.size() == 1 && overall_coeff.is_equal(_ex_1))
+       if (seq.size() == 1 && overall_coeff.is_equal(_ex1))
                return 0;
        return 1;
 }
```


I'll post an updated spkg later together with a fix for #6244.



---

archive/issue_comments_049876.json:
```json
{
    "body": "Attachment [trac_6256-pynac_mul_compare_tests.patch](tarball://root/attachments/some-uuid/ticket6256/trac_6256-pynac_mul_compare_tests.patch) by @burcin created at 2009-06-14 20:51:47\n\ndoctests",
    "created_at": "2009-06-14T20:51:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6256#issuecomment-49876",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_6256-pynac_mul_compare_tests.patch](tarball://root/attachments/some-uuid/ticket6256/trac_6256-pynac_mul_compare_tests.patch) by @burcin created at 2009-06-14 20:51:47

doctests



---

archive/issue_comments_049877.json:
```json
{
    "body": "New pynac package fixes this:\n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.8.p0.spkg\n\nIt also contains fixes for #6244 and #6211, so doctests should be run with patches from those tickets applied.\n\n\nJason, can you review this?",
    "created_at": "2009-06-14T20:59:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6256#issuecomment-49877",
    "user": "https://github.com/burcin"
}
```

New pynac package fixes this:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.8.p0.spkg

It also contains fixes for #6244 and #6211, so doctests should be run with patches from those tickets applied.


Jason, can you review this?



---

archive/issue_comments_049878.json:
```json
{
    "body": "Fine by me, works with new spkg.",
    "created_at": "2009-06-14T21:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6256#issuecomment-49878",
    "user": "https://github.com/ncalexan"
}
```

Fine by me, works with new spkg.



---

archive/issue_comments_049879.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-14T21:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6256#issuecomment-49879",
    "user": "https://github.com/ncalexan"
}
```

Resolution: fixed



---

archive/issue_events_006500.json:
```json
{
    "actor": "https://github.com/ncalexan",
    "created_at": "2009-06-14T21:36:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6256",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6256#event-6500"
}
```
