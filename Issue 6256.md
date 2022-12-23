# Issue 6256: bug in symbolic arithmetic with exp

archive/issues_006256.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  jason\n\n\n```\nsage: var('kappa')\nkappa\nsage: x = sqrt(kappa)\nsage: F = exp(x)\nsage: F\ne^sqrt(kappa)\nsage: F/F\ne^(2*sqrt(kappa))\nsage: 1/F\ne^(-sqrt(kappa))\nsage: (1/F) * F\ne^(2*sqrt(kappa))\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6256\n\n",
    "created_at": "2009-06-10T08:48:57Z",
    "labels": [
        "symbolics",
        "blocker",
        "bug"
    ],
    "title": "bug in symbolic arithmetic with exp",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6256",
    "user": "burcin"
}
```
Assignee: burcin

CC:  jason


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

archive/issue_comments_049970.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-13T22:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6256#issuecomment-49970",
    "user": "burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_049971.json:
```json
{
    "body": "Here is the fix for pynac:\n\n```\ndiff --git a/ginac/mul.cpp b/ginac/mul.cpp\n--- a/ginac/mul.cpp\n+++ b/ginac/mul.cpp\n@@ -1167,7 +1167,7 @@\n        if (cmpval != 0) {\n                return cmpval;\n        }\n-       if (seq.size() == 1 && overall_coeff.is_equal(_ex_1))\n+       if (seq.size() == 1 && overall_coeff.is_equal(_ex1))\n                return 0;\n        return 1;\n }\n```\n\n\nI'll post an updated spkg later together with a fix for #6244.",
    "created_at": "2009-06-13T22:23:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6256#issuecomment-49971",
    "user": "burcin"
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

archive/issue_comments_049972.json:
```json
{
    "body": "Attachment\n\ndoctests",
    "created_at": "2009-06-14T20:51:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6256#issuecomment-49972",
    "user": "burcin"
}
```

Attachment

doctests



---

archive/issue_comments_049973.json:
```json
{
    "body": "New pynac package fixes this:\n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.8.p0.spkg\n\nIt also contains fixes for #6244 and #6211, so doctests should be run with patches from those tickets applied.\n\n\nJason, can you review this?",
    "created_at": "2009-06-14T20:59:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6256#issuecomment-49973",
    "user": "burcin"
}
```

New pynac package fixes this:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.8.p0.spkg

It also contains fixes for #6244 and #6211, so doctests should be run with patches from those tickets applied.


Jason, can you review this?



---

archive/issue_comments_049974.json:
```json
{
    "body": "Fine by me, works with new spkg.",
    "created_at": "2009-06-14T21:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6256#issuecomment-49974",
    "user": "ncalexan"
}
```

Fine by me, works with new spkg.



---

archive/issue_comments_049975.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-14T21:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6256",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6256#issuecomment-49975",
    "user": "ncalexan"
}
```

Resolution: fixed
