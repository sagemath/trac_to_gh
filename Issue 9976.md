# Issue 9976: Implement complex multiplication for points of CM elliptic curves

archive/issues_009976.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nCC:  @jdemeyer @JohnCremona @yyyyx4\n\nKeywords: CM\n\nIt would be great if we could do\n\n```\nsage: E = EllipticCurve([0,0,0,3,0]) # curve with CM by Q[I]\nsage: (1 + I) * P([1,2])\n```\n\nThis wouldn't be very hard for CM elliptic curves over QQ, since the necessary functionality is there in PARI's `ellpow`; see #6327. CM elliptic curves over number fields might be a bit harder. \n\nIssue created by migration from https://trac.sagemath.org/ticket/9977\n\n",
    "created_at": "2010-09-23T12:11:05Z",
    "labels": [
        "elliptic curves",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Implement complex multiplication for points of CM elliptic curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9976",
    "user": "@loefflerd"
}
```
Assignee: @JohnCremona

CC:  @jdemeyer @JohnCremona @yyyyx4

Keywords: CM

It would be great if we could do

```
sage: E = EllipticCurve([0,0,0,3,0]) # curve with CM by Q[I]
sage: (1 + I) * P([1,2])
```

This wouldn't be very hard for CM elliptic curves over QQ, since the necessary functionality is there in PARI's `ellpow`; see #6327. CM elliptic curves over number fields might be a bit harder. 

Issue created by migration from https://trac.sagemath.org/ticket/9977





---

archive/issue_comments_100286.json:
```json
{
    "body": "Agreed!  See also #7368.",
    "created_at": "2010-09-23T16:29:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9976#issuecomment-100286",
    "user": "@JohnCremona"
}
```

Agreed!  See also #7368.



---

archive/issue_comments_100287.json:
```json
{
    "body": "If we can do Q, then we can do number fields simply by adapting the PARI code.  I already have the proof-of-concept code for this.\n\nI have an important mathematical question though: given an elliptic curve E, how can we see whether it has CM and if yes, for which discriminant?",
    "created_at": "2010-09-23T16:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9976#issuecomment-100287",
    "user": "@jdemeyer"
}
```

If we can do Q, then we can do number fields simply by adapting the PARI code.  I already have the proof-of-concept code for this.

I have an important mathematical question though: given an elliptic curve E, how can we see whether it has CM and if yes, for which discriminant?



---

archive/issue_comments_100288.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-09-23T16:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9976#issuecomment-100288",
    "user": "@jdemeyer"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_100289.json:
```json
{
    "body": "Changing keywords from \"CM\" to \"CM elliptic curve\".",
    "created_at": "2010-09-23T16:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9976#issuecomment-100289",
    "user": "@jdemeyer"
}
```

Changing keywords from "CM" to "CM elliptic curve".



---

archive/issue_comments_100290.json:
```json
{
    "body": "There are now methods `has_cm` and `cm_discriminant` available.",
    "created_at": "2013-09-21T12:18:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9976#issuecomment-100290",
    "user": "@fchapoton"
}
```

There are now methods `has_cm` and `cm_discriminant` available.



---

archive/issue_comments_100291.json:
```json
{
    "body": "The new code for isogenies should make it easy to implement endomorphisms for CM curves.  Then this sort of thing would be easy.  So I would say that the next step should be to implement endomorphism rings, as structures which know they are rings and also know how to act on points.",
    "created_at": "2013-09-21T14:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9976#issuecomment-100291",
    "user": "@JohnCremona"
}
```

The new code for isogenies should make it easy to implement endomorphisms for CM curves.  Then this sort of thing would be easy.  So I would say that the next step should be to implement endomorphism rings, as structures which know they are rings and also know how to act on points.



---

archive/issue_comments_100292.json:
```json
{
    "body": "Note that although some elliptic curves defined over Q are CM curves, the additional endomorphisms are not themselves defined over Q.  One needs to distinguish, for an elliptic curve E defined over a field k,  between End_k(E) (the ring of endomorphisms defined over k itself) and End(E) (the possibly larger ring of endomorphisms defined over an algebraic closure).  In the case where char(k)=0 and E has CM by the order of discriminant D<0, the endomorphisms are defined over k(sqrt(D)) which may be a quadratic extension of k.  This is always the case when k=Q.\n\nIn the original example, (1+I)*P will not be a rational point on the original curve.",
    "created_at": "2018-04-13T09:02:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9976",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9976#issuecomment-100292",
    "user": "@JohnCremona"
}
```

Note that although some elliptic curves defined over Q are CM curves, the additional endomorphisms are not themselves defined over Q.  One needs to distinguish, for an elliptic curve E defined over a field k,  between End_k(E) (the ring of endomorphisms defined over k itself) and End(E) (the possibly larger ring of endomorphisms defined over an algebraic closure).  In the case where char(k)=0 and E has CM by the order of discriminant D<0, the endomorphisms are defined over k(sqrt(D)) which may be a quadratic extension of k.  This is always the case when k=Q.

In the original example, (1+I)*P will not be a rational point on the original curve.
