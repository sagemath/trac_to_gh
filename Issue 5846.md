# Issue 5846: small bug in caching the precision for p-adic L-series

archive/issues_005846.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: p-adic L-series\n\nWhen looking up cached values of the p-adic L-series of an elliptic curve, there is a problem with the precision (as a powe-series in T) :\n\n\n```\nsage: E = EllipticCurve('389a')\nsage: p = 3\nsage: L = E.padic_lseries(p)\nsage: L.series(3)\nO(3^5) + O(3^2)*T + (2 + 2*3 + O(3^2))*T^2 + (2 + O(3))*T^3 + (1 + 3 + O(3^2))*T^4 + O(T^5)\nsage: L.series(3,prec=6)\nO(3^5) + O(3^2)*T + (2 + 2*3 + O(3^2))*T^2 + (2 + O(3))*T^3 + (1 + 3 + O(3^2))*T^4 + O(T^5)\n```\n\n\nThe attached patch changes the inequality sign in question.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5846\n\n",
    "created_at": "2009-04-21T14:27:11Z",
    "labels": [
        "number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "small bug in caching the precision for p-adic L-series",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5846",
    "user": "@categorie"
}
```
Assignee: @williamstein

Keywords: p-adic L-series

When looking up cached values of the p-adic L-series of an elliptic curve, there is a problem with the precision (as a powe-series in T) :


```
sage: E = EllipticCurve('389a')
sage: p = 3
sage: L = E.padic_lseries(p)
sage: L.series(3)
O(3^5) + O(3^2)*T + (2 + 2*3 + O(3^2))*T^2 + (2 + O(3))*T^3 + (1 + 3 + O(3^2))*T^4 + O(T^5)
sage: L.series(3,prec=6)
O(3^5) + O(3^2)*T + (2 + 2*3 + O(3^2))*T^2 + (2 + O(3))*T^3 + (1 + 3 + O(3^2))*T^4 + O(T^5)
```


The attached patch changes the inequality sign in question.

Issue created by migration from https://trac.sagemath.org/ticket/5846





---

archive/issue_comments_045984.json:
```json
{
    "body": "Attachment [trac_5846_prec.patch](tarball://root/attachments/some-uuid/ticket5846/trac_5846_prec.patch) by @categorie created at 2009-04-21 15:04:45",
    "created_at": "2009-04-21T15:04:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5846#issuecomment-45984",
    "user": "@categorie"
}
```

Attachment [trac_5846_prec.patch](tarball://root/attachments/some-uuid/ticket5846/trac_5846_prec.patch) by @categorie created at 2009-04-21 15:04:45



---

archive/issue_comments_045985.json:
```json
{
    "body": "One slight nitpick: The trac number in the patch is missing.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-21T22:17:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5846#issuecomment-45985",
    "user": "mabshoff"
}
```

One slight nitpick: The trac number in the patch is missing.

Cheers,

Michael



---

archive/issue_comments_045986.json:
```json
{
    "body": "And this is not going into 3.4.1 since it is basically done, so better luck in 3.4.2 :)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-21T22:37:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5846#issuecomment-45986",
    "user": "mabshoff"
}
```

And this is not going into 3.4.1 since it is basically done, so better luck in 3.4.2 :)

Cheers,

Michael



---

archive/issue_comments_045987.json:
```json
{
    "body": "to apply after the first patch",
    "created_at": "2009-04-22T10:38:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5846#issuecomment-45987",
    "user": "@categorie"
}
```

to apply after the first patch



---

archive/issue_comments_045988.json:
```json
{
    "body": "Attachment [trac_5846_prec_2.patch](tarball://root/attachments/some-uuid/ticket5846/trac_5846_prec_2.patch) by @categorie created at 2009-04-22 10:39:03\n\nI added the forgotten trac number in the doctest.\n\nChris.",
    "created_at": "2009-04-22T10:39:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5846#issuecomment-45988",
    "user": "@categorie"
}
```

Attachment [trac_5846_prec_2.patch](tarball://root/attachments/some-uuid/ticket5846/trac_5846_prec_2.patch) by @categorie created at 2009-04-22 10:39:03

I added the forgotten trac number in the doctest.

Chris.



---

archive/issue_comments_045989.json:
```json
{
    "body": "Attachment [trac_5846_combined.patch](tarball://root/attachments/some-uuid/ticket5846/trac_5846_combined.patch) by GeorgSWeber created at 2009-04-28 19:56:44\n\napply only this one",
    "created_at": "2009-04-28T19:56:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5846#issuecomment-45989",
    "user": "GeorgSWeber"
}
```

Attachment [trac_5846_combined.patch](tarball://root/attachments/some-uuid/ticket5846/trac_5846_combined.patch) by GeorgSWeber created at 2009-04-28 19:56:44

apply only this one



---

archive/issue_comments_045990.json:
```json
{
    "body": "The first two hunks of the first patch didn't apply to sage-3.4.2.alpha0, but they contained only whitespace beautification. Probably this had already been adressed. I merged the remaining two hunks with the \"real\" patch and the the second patch. Ready to go.",
    "created_at": "2009-04-28T20:00:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5846#issuecomment-45990",
    "user": "GeorgSWeber"
}
```

The first two hunks of the first patch didn't apply to sage-3.4.2.alpha0, but they contained only whitespace beautification. Probably this had already been adressed. I merged the remaining two hunks with the "real" patch and the the second patch. Ready to go.



---

archive/issue_comments_045991.json:
```json
{
    "body": "Merged  trac_5846_combined.patch in Sage 3.4.2.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-29T23:38:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5846#issuecomment-45991",
    "user": "mabshoff"
}
```

Merged  trac_5846_combined.patch in Sage 3.4.2.rc0.

Cheers,

Michael



---

archive/issue_comments_045992.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-29T23:38:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5846#issuecomment-45992",
    "user": "mabshoff"
}
```

Resolution: fixed
