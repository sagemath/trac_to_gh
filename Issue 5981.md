# Issue 5981: Sage 3.4.2: prime_pi() broken on 32 bit

archive/issues_005981.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis patch fixes the problem:\n\n```\ndiff -r 8713e0a599f3 sage/functions/prime_pi.pyx\n--- a/sage/functions/prime_pi.pyx\tSun May 03 23:10:56 2009 -0700\n+++ b/sage/functions/prime_pi.pyx\tMon May 04 12:44:03 2009 -0400\n@@ -171,7 +171,7 @@\n             raise ValueError, \"mem_mult must be positive\"\n         if x < 2:\n             return 0\n-        if x > Integer(2**40):\n+        if x > 1099511627776L:\n             raise NotImplementedError, \"computation of prime_pi() greater 2**40 not implemented\"\n         x += x & 1\n         # m_max is the current sieving value, for prime counting - this value is sqrt(x)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5981\n\n",
    "created_at": "2009-05-04T16:45:52Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "Sage 3.4.2: prime_pi() broken on 32 bit",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5981",
    "user": "mabshoff"
}
```
Assignee: mabshoff

This patch fixes the problem:

```
diff -r 8713e0a599f3 sage/functions/prime_pi.pyx
--- a/sage/functions/prime_pi.pyx	Sun May 03 23:10:56 2009 -0700
+++ b/sage/functions/prime_pi.pyx	Mon May 04 12:44:03 2009 -0400
@@ -171,7 +171,7 @@
             raise ValueError, "mem_mult must be positive"
         if x < 2:
             return 0
-        if x > Integer(2**40):
+        if x > 1099511627776L:
             raise NotImplementedError, "computation of prime_pi() greater 2**40 not implemented"
         x += x & 1
         # m_max is the current sieving value, for prime counting - this value is sqrt(x)
```


Issue created by migration from https://trac.sagemath.org/ticket/5981





---

archive/issue_comments_047496.json:
```json
{
    "body": "Attachment [trac_5981.patch](tarball://root/attachments/some-uuid/ticket5981/trac_5981.patch) by mabshoff created at 2009-05-04 16:59:12",
    "created_at": "2009-05-04T16:59:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5981#issuecomment-47496",
    "user": "mabshoff"
}
```

Attachment [trac_5981.patch](tarball://root/attachments/some-uuid/ticket5981/trac_5981.patch) by mabshoff created at 2009-05-04 16:59:12



---

archive/issue_comments_047497.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-04T17:00:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5981#issuecomment-47497",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_047498.json:
```json
{
    "body": "Positive review :)\n\n\n```\n\n ./sage -t  \"devel/sage/sage/functions/prime_pi.pyx\"\nsage -t  \"devel/sage/sage/functions/prime_pi.pyx\"\n     [48.1 s]\n\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 48.1 seconds\n\n\nJaap\n\n\n```\n",
    "created_at": "2009-05-04T17:08:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5981#issuecomment-47498",
    "user": "@jaapspies"
}
```

Positive review :)


```

 ./sage -t  "devel/sage/sage/functions/prime_pi.pyx"
sage -t  "devel/sage/sage/functions/prime_pi.pyx"
     [48.1 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 48.1 seconds


Jaap


```




---

archive/issue_comments_047499.json:
```json
{
    "body": "Merged in Sage 3.4.2.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-05T04:20:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5981#issuecomment-47499",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.2.

Cheers,

Michael



---

archive/issue_comments_047500.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-05T04:20:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5981#issuecomment-47500",
    "user": "mabshoff"
}
```

Resolution: fixed
