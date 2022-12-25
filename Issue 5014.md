# Issue 5014: matrix rank should call echelon_form over *fraction field*

archive/issues_005014.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @orlitzky\n\n\n```\n\nOn Sun, Jan 18, 2009 at 6:49 AM, Paul Zimmermann <Paul.Zimmermann@loria.fr> wrote:\n>       Hi,\n>\n> I hit the following:\n>\n> sage: P.<x> = PolynomialRing(GF(17))\n> sage: m = Matrix(P,2,2)\n> sage: m.randomize(); m\n>\n> [ 6*x^2 + 8*x + 12 10*x^2 + 4*x + 11]\n> [8*x^2 + 12*x + 15  8*x^2 + 9*x + 16]\n> sage: m.rank()\n> ...\n> NotImplementedError: echelon form over Univariate Polynomial Ring in x over Finite Field of size 17 not yet implemented\n>\n> Isn't that provided by either GP or Linbox?\n\nYes, by gp.  I have no idea if it is in Linbox.\n\nsage: gp(m).matrank()\n2\nsage: pari(m).matrank()\nboom -- matrank not wrapped\n\nSomebody *could* implement this by wrapping pari's matrank then doing the conversion and calling it.  Of course, much better would be to do:\n\nsage: m.change_ring(m.base_ring().fraction_field()).rank()\n2\n\nwhich already works. \n\nI am puzzled that rank doesn't first change base to the fraction field, *then* call echelon form -- it's stupid that it tries to call echelon form over the same base ring, since that is often much harder (e.g., it is Hermite form over ZZ).\n\nWilliam\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5014\n\n",
    "created_at": "2009-01-18T14:59:32Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "matrix rank should call echelon_form over *fraction field*",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5014",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  @orlitzky


```

On Sun, Jan 18, 2009 at 6:49 AM, Paul Zimmermann <Paul.Zimmermann@loria.fr> wrote:
>       Hi,
>
> I hit the following:
>
> sage: P.<x> = PolynomialRing(GF(17))
> sage: m = Matrix(P,2,2)
> sage: m.randomize(); m
>
> [ 6*x^2 + 8*x + 12 10*x^2 + 4*x + 11]
> [8*x^2 + 12*x + 15  8*x^2 + 9*x + 16]
> sage: m.rank()
> ...
> NotImplementedError: echelon form over Univariate Polynomial Ring in x over Finite Field of size 17 not yet implemented
>
> Isn't that provided by either GP or Linbox?

Yes, by gp.  I have no idea if it is in Linbox.

sage: gp(m).matrank()
2
sage: pari(m).matrank()
boom -- matrank not wrapped

Somebody *could* implement this by wrapping pari's matrank then doing the conversion and calling it.  Of course, much better would be to do:

sage: m.change_ring(m.base_ring().fraction_field()).rank()
2

which already works. 

I am puzzled that rank doesn't first change base to the fraction field, *then* call echelon form -- it's stupid that it tries to call echelon form over the same base ring, since that is often much harder (e.g., it is Hermite form over ZZ).

William
```


Issue created by migration from https://trac.sagemath.org/ticket/5014





---

archive/issue_comments_038137.json:
```json
{
    "body": "See #3211 for a related ticket, sort of.",
    "created_at": "2009-01-21T08:27:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5014#issuecomment-38137",
    "user": "https://github.com/jasongrout"
}
```

See #3211 for a related ticket, sort of.



---

archive/issue_comments_038138.json:
```json
{
    "body": "This seems to work now:\n\n\n```\n\nsage: version()\n'Sage Version 4.6.2, Release Date: 2011-02-25'\nsage: P.<x> = PolynomialRing(GF(17))\nsage: m = Matrix(P,2,2)\nsage: m.randomize()\nsage: m\n[     15*x^2 + 16*x  9*x^2 + 12*x + 12]\n[13*x^2 + 16*x + 16   4*x^2 + 5*x + 12]\nsage: m.rank()\n2\n```\n",
    "created_at": "2011-05-23T13:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5014#issuecomment-38138",
    "user": "https://trac.sagemath.org/admin/accounts/users/dsm"
}
```

This seems to work now:


```

sage: version()
'Sage Version 4.6.2, Release Date: 2011-02-25'
sage: P.<x> = PolynomialRing(GF(17))
sage: m = Matrix(P,2,2)
sage: m.randomize()
sage: m
[     15*x^2 + 16*x  9*x^2 + 12*x + 12]
[13*x^2 + 16*x + 16   4*x^2 + 5*x + 12]
sage: m.rank()
2
```




---

archive/issue_comments_038139.json:
```json
{
    "body": "Attachment [sage-trac_5014.patch](tarball://root/attachments/some-uuid/ticket5014/sage-trac_5014.patch) by @orlitzky created at 2012-01-08 00:07:14\n\nAdd a doctest computing the rank of one of these matrices.",
    "created_at": "2012-01-08T00:07:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5014#issuecomment-38139",
    "user": "https://github.com/orlitzky"
}
```

Attachment [sage-trac_5014.patch](tarball://root/attachments/some-uuid/ticket5014/sage-trac_5014.patch) by @orlitzky created at 2012-01-08 00:07:14

Add a doctest computing the rank of one of these matrices.



---

archive/issue_comments_038140.json:
```json
{
    "body": "This works now; I've added a doctest using the example in the description.",
    "created_at": "2012-01-08T00:10:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5014#issuecomment-38140",
    "user": "https://github.com/orlitzky"
}
```

This works now; I've added a doctest using the example in the description.



---

archive/issue_comments_038141.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-01-08T00:10:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5014#issuecomment-38141",
    "user": "https://github.com/orlitzky"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_038142.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-01-11T05:16:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5014#issuecomment-38142",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_011581.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-01-11T11:05:37Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5014",
    "milestone": "sage-5.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5014#event-11581"
}
```



---

archive/issue_events_011582.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-01-21T23:39:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5014",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5014#event-11582"
}
```



---

archive/issue_comments_038143.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-01-21T23:39:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5014",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5014#issuecomment-38143",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
