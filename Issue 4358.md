# Issue 4358: Sage spawn too many gp processes

archive/issues_004358.json:
```json
{
    "body": "Assignee: was\n\nCC:  cremona jdemeyer\n\nThis:\n\n\n```\nsage: EllipticCurve('37a').sha().an_numerical()\n```\n\n\nspawn a new gp process every time it is computed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4358\n\n",
    "created_at": "2008-10-24T05:17:34Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "Sage spawn too many gp processes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4358",
    "user": "anakha"
}
```
Assignee: was

CC:  cremona jdemeyer

This:


```
sage: EllipticCurve('37a').sha().an_numerical()
```


spawn a new gp process every time it is computed.

Issue created by migration from https://trac.sagemath.org/ticket/4358





---

archive/issue_comments_032014.json:
```json
{
    "body": "I think this might be in the Dokchitser call (line 94 of elliptic_curves/sha_tate.py)",
    "created_at": "2008-10-31T16:57:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4358#issuecomment-32014",
    "user": "cremona"
}
```

I think this might be in the Dokchitser call (line 94 of elliptic_curves/sha_tate.py)



---

archive/issue_comments_032015.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T02:43:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4358#issuecomment-32015",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_032016.json:
```json
{
    "body": "Why is this a bug? `gp` starts up very quickly, so it doesn't need to be \"fixed\".",
    "created_at": "2013-08-13T16:00:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4358#issuecomment-32016",
    "user": "jdemeyer"
}
```

Why is this a bug? `gp` starts up very quickly, so it doesn't need to be "fixed".



---

archive/issue_comments_032017.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-08-13T16:00:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4358#issuecomment-32017",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_032018.json:
```json
{
    "body": "Tim Dokchitser's `gp` script `computel.gp`, which is used internally by `an_numerical`, uses global variables, which is a good reason to use a different `gp` instance for every call.\n\nI first suspected an unnecessary line of code in `Lseries_ell.dokchitser()`, but this was not the cause:\n\n```diff\n--- a/sage/schemes/elliptic_curves/lseries_ell.py\n+++ b/sage/schemes/elliptic_curves/lseries_ell.py\n@@ -132,7 +132,6 @@\n                        eps = self.__E.root_number(),\n                        poles = [],\n                        prec = prec)\n-        gp = L.gp()\n         s = 'e = ellinit(%s);'%list(self.__E.minimal_model().a_invariants())\n         s += 'a(k) = ellak(e, k);'\n         L.init_coeffs('a(k)', 1, pari_precode = s,\n```\n\nThis line just starts the `gp` instance a bit sooner than necessary, so I don't think a patch is needed.",
    "created_at": "2013-08-13T20:10:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4358#issuecomment-32018",
    "user": "pbruin"
}
```

Tim Dokchitser's `gp` script `computel.gp`, which is used internally by `an_numerical`, uses global variables, which is a good reason to use a different `gp` instance for every call.

I first suspected an unnecessary line of code in `Lseries_ell.dokchitser()`, but this was not the cause:

```diff
--- a/sage/schemes/elliptic_curves/lseries_ell.py
+++ b/sage/schemes/elliptic_curves/lseries_ell.py
@@ -132,7 +132,6 @@
                        eps = self.__E.root_number(),
                        poles = [],
                        prec = prec)
-        gp = L.gp()
         s = 'e = ellinit(%s);'%list(self.__E.minimal_model().a_invariants())
         s += 'a(k) = ellak(e, k);'
         L.init_coeffs('a(k)', 1, pari_precode = s,
```

This line just starts the `gp` instance a bit sooner than necessary, so I don't think a patch is needed.



---

archive/issue_comments_032019.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-08-13T20:10:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4358#issuecomment-32019",
    "user": "pbruin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_032020.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2013-08-16T11:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4358",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4358#issuecomment-32020",
    "user": "jdemeyer"
}
```

Resolution: wontfix
