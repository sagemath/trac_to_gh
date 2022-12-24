# Issue 9776: include more rings in random testing

archive/issues_009776.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  tscrim slelievre @kliem\n\nKeywords: random testing, rings\n\np-adics should be included, perhaps at \"level 0\"?\n\nThe following \"level 1\" rings are not included in `sage.rings.tests`:\n\n* power series rings\n\n* Laurent series rings\n\n* multivariate power series rings (implemented in #1956)\n\n* infinite polynomial rings\n\nAlso, it's not clear that \"level n\" testing occurs for `n > 1`; e.g. multivariate polynomial ring in 3 variables over Laurent series ring over finite field of size 29, etc.\n\nQuotient rings are also not included, but should be.  There are probably more to be included than this list indicates.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9777\n\n",
    "created_at": "2010-08-21T19:47:56Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.5",
    "title": "include more rings in random testing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9776",
    "user": "niles"
}
```
Assignee: AlexGhitza

CC:  tscrim slelievre @kliem

Keywords: random testing, rings

p-adics should be included, perhaps at "level 0"?

The following "level 1" rings are not included in `sage.rings.tests`:

* power series rings

* Laurent series rings

* multivariate power series rings (implemented in #1956)

* infinite polynomial rings

Also, it's not clear that "level n" testing occurs for `n > 1`; e.g. multivariate polynomial ring in 3 variables over Laurent series ring over finite field of size 29, etc.

Quotient rings are also not included, but should be.  There are probably more to be included than this list indicates.

Issue created by migration from https://trac.sagemath.org/ticket/9777





---

archive/issue_comments_095936.json:
```json
{
    "body": "Here is a branch.\n\nBut is this still pertinent ?\n----\nNew commits:",
    "created_at": "2021-08-11T14:34:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9776#issuecomment-95936",
    "user": "chapoton"
}
```

Here is a branch.

But is this still pertinent ?
----
New commits:



---

archive/issue_comments_095937.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2021-08-11T14:34:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9776#issuecomment-95937",
    "user": "chapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_095938.json:
```json
{
    "body": "any opinion on the pertinence ?",
    "created_at": "2021-08-19T16:06:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9776#issuecomment-95938",
    "user": "chapoton"
}
```

any opinion on the pertinence ?



---

archive/issue_comments_095939.json:
```json
{
    "body": "Is this doctest checking the right function?\n\n\n```patch\n+\n+def padic_field():\n+    \"\"\"\n+    Return a random p-adic field modulo n with p at most 10000\n+    and precision between 10 and 100.\n+\n+    EXAMPLES::\n+\n+        sage: import sage.rings.tests\n+        sage: sage.rings.tests.integer_mod_ring()\n+        Ring of integers modulo 30029\n+    \"\"\"\n+    from sage.all import ZZ, Qp\n+    prec = ZZ.random_element(x=10, y=100)\n+    p = ZZ.random_element(x=2, y=10**4 - 30).next_prime()\n+    return Qp(p, prec)\n+\n+\n```\n\n\nIn any case, it would be nice to avoid adding *new* tests that require a specific random seed. We're pretty close to making all testing random testing.",
    "created_at": "2021-08-19T23:34:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9776#issuecomment-95939",
    "user": "mjo"
}
```

Is this doctest checking the right function?


```patch
+
+def padic_field():
+    """
+    Return a random p-adic field modulo n with p at most 10000
+    and precision between 10 and 100.
+
+    EXAMPLES::
+
+        sage: import sage.rings.tests
+        sage: sage.rings.tests.integer_mod_ring()
+        Ring of integers modulo 30029
+    """
+    from sage.all import ZZ, Qp
+    prec = ZZ.random_element(x=10, y=100)
+    p = ZZ.random_element(x=2, y=10**4 - 30).next_prime()
+    return Qp(p, prec)
+
+
```


In any case, it would be nice to avoid adding *new* tests that require a specific random seed. We're pretty close to making all testing random testing.



---

archive/issue_comments_095940.json:
```json
{
    "body": "I am not sure how useful this is for catching bugs as we do (or at least should do) good test coverage within the individual files/rings themselves. However, I would follow `@`mjo's recommendation as I don't have a strong opinion on this.",
    "created_at": "2021-08-20T00:03:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9776#issuecomment-95940",
    "user": "tscrim"
}
```

I am not sure how useful this is for catching bugs as we do (or at least should do) good test coverage within the individual files/rings themselves. However, I would follow `@`mjo's recommendation as I don't have a strong opinion on this.



---

archive/issue_comments_095941.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2021-08-20T12:20:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9776#issuecomment-95941",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_095942.json:
```json
{
    "body": "ok, should be better now",
    "created_at": "2021-08-20T12:21:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9776#issuecomment-95942",
    "user": "chapoton"
}
```

ok, should be better now



---

archive/issue_comments_095943.json:
```json
{
    "body": "Thanks! Many of these tests can probably be removed later on, but it's nice to have this old ticket fixed in the meantime, especially in the likely event that we all forget about it for another decade.",
    "created_at": "2021-08-23T00:18:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9776#issuecomment-95943",
    "user": "mjo"
}
```

Thanks! Many of these tests can probably be removed later on, but it's nice to have this old ticket fixed in the meantime, especially in the likely event that we all forget about it for another decade.



---

archive/issue_comments_095944.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-08-23T00:18:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9776#issuecomment-95944",
    "user": "mjo"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095945.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2021-08-29T09:39:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9776#issuecomment-95945",
    "user": "vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_095946.json:
```json
{
    "body": "Merge conflict",
    "created_at": "2021-08-29T09:39:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9776#issuecomment-95946",
    "user": "vbraun"
}
```

Merge conflict



---

archive/issue_comments_095947.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2021-09-01T06:12:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9776#issuecomment-95947",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_095948.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2021-09-01T06:13:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9776#issuecomment-95948",
    "user": "chapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_095949.json:
```json
{
    "body": "indeed a serious merge conflict. Needs another round of review, please",
    "created_at": "2021-09-01T06:13:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9776#issuecomment-95949",
    "user": "chapoton"
}
```

indeed a serious merge conflict. Needs another round of review, please



---

archive/issue_comments_095950.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-09-02T15:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9776#issuecomment-95950",
    "user": "mjo"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095951.json:
```json
{
    "body": "Still OK.",
    "created_at": "2021-09-02T15:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9776#issuecomment-95951",
    "user": "mjo"
}
```

Still OK.



---

archive/issue_comments_095952.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2021-09-07T20:52:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9776#issuecomment-95952",
    "user": "vbraun"
}
```

Resolution: fixed
