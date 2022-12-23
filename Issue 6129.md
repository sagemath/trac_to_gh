# Issue 6129: Ammend docstring in ode.pyx

archive/issues_006129.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: ode docstring\n\n\n```\n# HG changeset patch\n# User Anthony David <adavid@adavid.com.au>\n# Date 1243305447 -36000\n# Node ID 894f488ddccd3411fdd0736b455f27e2d8272099\n# Parent  958178a11b9e809788f1eda0cc29107c456a1bbe\nammend EXAMPLE comment in sage/gsl/ode.pyx to match doctest function g_1\n\ndiff -r 958178a11b9e -r 894f488ddccd sage/gsl/ode.pyx\n--- a/sage/gsl/ode.pyx\tMon May 25 00:46:38 2009 +1000\n+++ b/sage/gsl/ode.pyx\tTue May 26 12:37:27 2009 +1000\n@@ -213,7 +213,7 @@\n \n          Lets try a system\n \n-         y_0'=y_2*y_3\n+         y_0'=y_1*y_2\n          y_1'=-y_0*y_2\n          y_2'=-.51*y_0*y_1\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6129\n\n",
    "created_at": "2009-05-26T02:15:06Z",
    "labels": [
        "documentation",
        "trivial",
        "enhancement"
    ],
    "title": "Ammend docstring in ode.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6129",
    "user": "adavid"
}
```
Assignee: somebody

Keywords: ode docstring


```
# HG changeset patch
# User Anthony David <adavid@adavid.com.au>
# Date 1243305447 -36000
# Node ID 894f488ddccd3411fdd0736b455f27e2d8272099
# Parent  958178a11b9e809788f1eda0cc29107c456a1bbe
ammend EXAMPLE comment in sage/gsl/ode.pyx to match doctest function g_1

diff -r 958178a11b9e -r 894f488ddccd sage/gsl/ode.pyx
--- a/sage/gsl/ode.pyx	Mon May 25 00:46:38 2009 +1000
+++ b/sage/gsl/ode.pyx	Tue May 26 12:37:27 2009 +1000
@@ -213,7 +213,7 @@
 
          Lets try a system
 
-         y_0'=y_2*y_3
+         y_0'=y_1*y_2
          y_1'=-y_0*y_2
          y_2'=-.51*y_0*y_1
```


Issue created by migration from https://trac.sagemath.org/ticket/6129





---

archive/issue_comments_048963.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-05-28T07:22:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6129#issuecomment-48963",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_048964.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-05-28T07:31:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6129#issuecomment-48964",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_048965.json:
```json
{
    "body": "Merged trac_6129.patch in 4.0.rc1.",
    "created_at": "2009-05-28T07:31:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6129#issuecomment-48965",
    "user": "mhansen"
}
```

Merged trac_6129.patch in 4.0.rc1.



---

archive/issue_comments_048966.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-28T07:31:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6129#issuecomment-48966",
    "user": "mhansen"
}
```

Resolution: fixed
