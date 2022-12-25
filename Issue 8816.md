# Issue 8816: Bug in CPS_height_bound

archive/issues_008816.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nThe documentation states that \n\n\n```\n        Return the Cremona-Prickett-Siksek height bound. This is a\n        floating point number B such that if P is a rational point on\n        the curve, then `|h(P) - \\hat{h}(P)| \\leq B`, where `h(P)` is        the naive logarithmic height of `P` and `\\hat{h}(P)` is the\n        canonical height.\n```\n\n\nBut\n\n\n```\n            sage: E = EllipticCurve(\"5077a\")\n            sage: E.CPS_height_bound()\n            0.0\n```\n\n\nClearly that can't be correct as the naive height is not exactly equal to the canonical height. Either the documentation is incorrect, or the function broken for higher rank curves (in which case we should raise an error of some sort.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/8816\n\n",
    "created_at": "2010-04-29T05:59:24Z",
    "labels": [
        "component: elliptic curves",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "Bug in CPS_height_bound",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8816",
    "user": "https://github.com/robertwb"
}
```
Assignee: @JohnCremona

The documentation states that 


```
        Return the Cremona-Prickett-Siksek height bound. This is a
        floating point number B such that if P is a rational point on
        the curve, then `|h(P) - \hat{h}(P)| \leq B`, where `h(P)` is        the naive logarithmic height of `P` and `\hat{h}(P)` is the
        canonical height.
```


But


```
            sage: E = EllipticCurve("5077a")
            sage: E.CPS_height_bound()
            0.0
```


Clearly that can't be correct as the naive height is not exactly equal to the canonical height. Either the documentation is incorrect, or the function broken for higher rank curves (in which case we should raise an error of some sort.)

Issue created by migration from https://trac.sagemath.org/ticket/8816





---

archive/issue_comments_080785.json:
```json
{
    "body": "It is the documentation which is wrong.  Although the difference h(P) - \\hat{h}(P)  is bounded above and below, this function returns the upper bound (since that is the one most used), i.e. it returns B such that h(P) <= \\hat{h}(P) + B.\n\nIn the example, the generators are (1,0), (2,0), (0,-3).  Naive heights are therefore 0, log(2)=0.693 and 0.  The canonical heights are 0.6682, 0.767, 0.99.  This is consistent with B=0 as that just says that h(P) is no more than \\hat{h}(P).\n\nNote that Magma agrees with the bound of 0 for this curve (which is not that surprising since I wrote the Magma code  as well as the C++ code used here!).  Magma calls it the SiksekBound, despite the paper which it is based on having 3 authors!  The paper does give the lower bound too, and over number fields, so if that is ever needed it could be implemented.\n\nAt #8799 I am working through the documentation for this and other mwrank/eclib related functions, and had already noticed that the documentation for the height bounds was wrong in this respect.  I may fix this one at the same time -- in which case I will come back here and cross-reference.\n\nI have taken the liberty of correcting teh title and description on this ticket!  (Rank is irrelevant here).",
    "created_at": "2010-04-29T09:25:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8816#issuecomment-80785",
    "user": "https://github.com/JohnCremona"
}
```

It is the documentation which is wrong.  Although the difference h(P) - \hat{h}(P)  is bounded above and below, this function returns the upper bound (since that is the one most used), i.e. it returns B such that h(P) <= \hat{h}(P) + B.

In the example, the generators are (1,0), (2,0), (0,-3).  Naive heights are therefore 0, log(2)=0.693 and 0.  The canonical heights are 0.6682, 0.767, 0.99.  This is consistent with B=0 as that just says that h(P) is no more than \hat{h}(P).

Note that Magma agrees with the bound of 0 for this curve (which is not that surprising since I wrote the Magma code  as well as the C++ code used here!).  Magma calls it the SiksekBound, despite the paper which it is based on having 3 authors!  The paper does give the lower bound too, and over number fields, so if that is ever needed it could be implemented.

At #8799 I am working through the documentation for this and other mwrank/eclib related functions, and had already noticed that the documentation for the height bounds was wrong in this respect.  I may fix this one at the same time -- in which case I will come back here and cross-reference.

I have taken the liberty of correcting teh title and description on this ticket!  (Rank is irrelevant here).



---

archive/issue_comments_080786.json:
```json
{
    "body": "Attachment [8816-cps-doc.patch](tarball://root/attachments/some-uuid/ticket8816/8816-cps-doc.patch) by @robertwb created at 2010-04-29 18:09:51",
    "created_at": "2010-04-29T18:09:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8816#issuecomment-80786",
    "user": "https://github.com/robertwb"
}
```

Attachment [8816-cps-doc.patch](tarball://root/attachments/some-uuid/ticket8816/8816-cps-doc.patch) by @robertwb created at 2010-04-29 18:09:51



---

archive/issue_comments_080787.json:
```json
{
    "body": "Ah, OK, that makes more sense. I suspected rank, as the first example I tried (and was surprised by) was 389a (which also has integral generators). \n\nI have implemented some of this (e.g. the computation of alpha) in my min-height stuff, and am hoping to get a ticket up for that soon.",
    "created_at": "2010-04-29T18:12:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8816#issuecomment-80787",
    "user": "https://github.com/robertwb"
}
```

Ah, OK, that makes more sense. I suspected rank, as the first example I tried (and was surprised by) was 389a (which also has integral generators). 

I have implemented some of this (e.g. the computation of alpha) in my min-height stuff, and am hoping to get a ticket up for that soon.



---

archive/issue_comments_080788.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-29T18:12:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8816#issuecomment-80788",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080789.json:
```json
{
    "body": "Replying to [comment:2 robertwb]:\n> Ah, OK, that makes more sense. I suspected rank, as the first example I tried (and was surprised by) was 389a (which also has integral generators). \n> \n> I have implemented some of this (e.g. the computation of alpha) in my min-height stuff, and am hoping to get a ticket up for that soon. \n\nGood!  I'll be waiting...",
    "created_at": "2010-04-29T19:03:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8816#issuecomment-80789",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:2 robertwb]:
> Ah, OK, that makes more sense. I suspected rank, as the first example I tried (and was surprised by) was 389a (which also has integral generators). 
> 
> I have implemented some of this (e.g. the computation of alpha) in my min-height stuff, and am hoping to get a ticket up for that soon. 

Good!  I'll be waiting...



---

archive/issue_comments_080790.json:
```json
{
    "body": "Positive review.  (All the patch does is make a minor correction to a docstring.)",
    "created_at": "2010-04-30T20:38:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8816#issuecomment-80790",
    "user": "https://github.com/JohnCremona"
}
```

Positive review.  (All the patch does is make a minor correction to a docstring.)



---

archive/issue_comments_080791.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-30T20:38:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8816#issuecomment-80791",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008981.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-05-08T21:54:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8816",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8816#event-8981"
}
```



---

archive/issue_comments_080792.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-08T21:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8816#issuecomment-80792",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
