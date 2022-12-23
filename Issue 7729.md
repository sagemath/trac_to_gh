# Issue 7729: Iwahori Hecke algebras

archive/issues_007729.json:
```json
{
    "body": "Assignee: bump\n\nKeywords: Iwahori Hecke Algebra\n\nThe attached patch implements Iwahori Hecke algebras. Given a Cartan Type, the Iwahori Hecke algebra is a deformation of the group algebra over the Weyl group. It has generators in bijection with the simple reflections of the Weyl group that satisfy simple quadratic relations of the form (T_i-q1)*(T_i-q2) = 0. Often we default q2=-1, q1=q in which case the relation is of the form T_i^2=(q-1)T_i+q. The generators also satisfy the braid relations.  \n\n\n```\nsage: R.<q>=PolynomialRing(QQ)\nsage: H = IwahoriHeckeAlgebra(\"A3\",q)\nsage: [T1,T2,T3]=H.algebra_generators()\nsage: T1*(T2+T3)*T1\nT1*T2*T1 + (q-1)*T3*T1 + q*T3\n```\n\n\nThis code is very tested for type A and is almost certainly correct for Weyl groups of finite type. I have not tried it for any affine Weyl groups.\n\nThe following issues remain.\n\n* It may require some revision in order to follow Sage's coercion model. David Roe suggested that the _coerce_impl method should be removed.\n\n* The get_action method is a kludge to avoid the crash reported in #7725. That crash is fixed by David Roe's patch in #7718, but this patch does not work with the patch in #7718.\n\nFor some further discussion of this topic see\nhttp://groups.google.com/group/sage-combinat-devel/browse_thread/thread/78fc23f23cafe705?hl=en\n\nIt is well tested for type A and is probably correct for all Cartan Types of finite type. I have not tried it with\n\nIssue created by migration from https://trac.sagemath.org/ticket/7729\n\n",
    "created_at": "2009-12-18T01:36:46Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "title": "Iwahori Hecke algebras",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7729",
    "user": "bump"
}
```
Assignee: bump

Keywords: Iwahori Hecke Algebra

The attached patch implements Iwahori Hecke algebras. Given a Cartan Type, the Iwahori Hecke algebra is a deformation of the group algebra over the Weyl group. It has generators in bijection with the simple reflections of the Weyl group that satisfy simple quadratic relations of the form (T_i-q1)*(T_i-q2) = 0. Often we default q2=-1, q1=q in which case the relation is of the form T_i^2=(q-1)T_i+q. The generators also satisfy the braid relations.  


```
sage: R.<q>=PolynomialRing(QQ)
sage: H = IwahoriHeckeAlgebra("A3",q)
sage: [T1,T2,T3]=H.algebra_generators()
sage: T1*(T2+T3)*T1
T1*T2*T1 + (q-1)*T3*T1 + q*T3
```


This code is very tested for type A and is almost certainly correct for Weyl groups of finite type. I have not tried it for any affine Weyl groups.

The following issues remain.

* It may require some revision in order to follow Sage's coercion model. David Roe suggested that the _coerce_impl method should be removed.

* The get_action method is a kludge to avoid the crash reported in #7725. That crash is fixed by David Roe's patch in #7718, but this patch does not work with the patch in #7718.

For some further discussion of this topic see
http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/78fc23f23cafe705?hl=en

It is well tested for type A and is probably correct for all Cartan Types of finite type. I have not tried it with

Issue created by migration from https://trac.sagemath.org/ticket/7729





---

archive/issue_comments_066405.json:
```json
{
    "body": "I posted a new version. This version works either before or after the patch in #7718.",
    "created_at": "2009-12-18T16:26:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7729#issuecomment-66405",
    "user": "bump"
}
```

I posted a new version. This version works either before or after the patch in #7718.



---

archive/issue_comments_066406.json:
```json
{
    "body": "Changing component from algebra to combinatorics.",
    "created_at": "2009-12-18T17:29:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7729#issuecomment-66406",
    "user": "bump"
}
```

Changing component from algebra to combinatorics.



---

archive/issue_comments_066407.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2009-12-19T00:14:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7729#issuecomment-66407",
    "user": "nthiery"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_066408.json:
```json
{
    "body": "Hi Dan!\n\nThanks much for implementing this very useful feature!\n\nDo you mind renaming it into IwahoriHeckeAlgebraT or TBasis, so that we can\nlater use IwahoriHeckeAlgebra for the abstract Iwahori Hecke algebra with its other bases?\n\nOther than that, the code looks good, except for the duplication of the CombinatorialFreeModule code. Do you mind if I refactor it to use the category framework and CombinatorialFreeModule?\nI am not sure when I'll be able to do that though, so maybe it's best to first get this patch\ninto Sage. Unless you are tempted by the adventure.\n\nI don't expect particular problems with affine weyl groups or other coxeter groups.\n\nAh one thing: please make the algebra generators into a family indexed by the index set of the Dynkin diagram (so that T[1], ... ) will do what we expect.",
    "created_at": "2009-12-19T00:14:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7729#issuecomment-66408",
    "user": "nthiery"
}
```

Hi Dan!

Thanks much for implementing this very useful feature!

Do you mind renaming it into IwahoriHeckeAlgebraT or TBasis, so that we can
later use IwahoriHeckeAlgebra for the abstract Iwahori Hecke algebra with its other bases?

Other than that, the code looks good, except for the duplication of the CombinatorialFreeModule code. Do you mind if I refactor it to use the category framework and CombinatorialFreeModule?
I am not sure when I'll be able to do that though, so maybe it's best to first get this patch
into Sage. Unless you are tempted by the adventure.

I don't expect particular problems with affine weyl groups or other coxeter groups.

Ah one thing: please make the algebra generators into a family indexed by the index set of the Dynkin diagram (so that T[1], ... ) will do what we expect.



---

archive/issue_comments_066409.json:
```json
{
    "body": "I've revised it so that it works with affine Weyl groups.\n\nI don't mind renaming it IwahoriHeckeAlgebraT but it seems to\nme that perhaps other presentations can be handled within this\nframework. I think I should leave the refactoring to the\ncategory framework to you.\n\nI will make the algebra generators into a family. When I've\ndone that I will change the status back to needs review.",
    "created_at": "2009-12-19T00:23:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7729#issuecomment-66409",
    "user": "bump"
}
```

I've revised it so that it works with affine Weyl groups.

I don't mind renaming it IwahoriHeckeAlgebraT but it seems to
me that perhaps other presentations can be handled within this
framework. I think I should leave the refactoring to the
category framework to you.

I will make the algebra generators into a family. When I've
done that I will change the status back to needs review.



---

archive/issue_comments_066410.json:
```json
{
    "body": "I've addressed two out of three of Nicolas' requests, and his\nmessage indicates that the refactoring issue can be postponed.\n\n* The name is now `IwahoriHeckeAlgebraT`\n\n* `self.algebra_generators()` now returns a finite family.\n\nI've changed the status back to needs review.\n\nNicolas wrote:\n\n> Do you mind renaming it into IwahoriHeckeAlgebraT or TBasis, so that we can later > use IwahoriHeckeAlgebra? for the abstract Iwahori Hecke algebra with its other bases?\n\nwhat other bases do we need? There is the Bernstein Zelevinsky presentation.",
    "created_at": "2009-12-19T01:10:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7729#issuecomment-66410",
    "user": "bump"
}
```

I've addressed two out of three of Nicolas' requests, and his
message indicates that the refactoring issue can be postponed.

* The name is now `IwahoriHeckeAlgebraT`

* `self.algebra_generators()` now returns a finite family.

I've changed the status back to needs review.

Nicolas wrote:

> Do you mind renaming it into IwahoriHeckeAlgebraT or TBasis, so that we can later > use IwahoriHeckeAlgebra? for the abstract Iwahori Hecke algebra with its other bases?

what other bases do we need? There is the Bernstein Zelevinsky presentation.



---

archive/issue_comments_066411.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-19T01:10:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7729#issuecomment-66411",
    "user": "bump"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066412.json:
```json
{
    "body": "I posted a revised version. With this version, the base ring can be either a field\ncontaining q1 and q2, or a LaurentPolynomialRing. The previous version did not\nwork with LaurentPolynomialRings.\n\nAlso, methods were added to\ncompute inverses of basis elements, a common task. \n\nFinally, there is a bug fix in\nsage.categories.pushout (import PolynomialRing when needed).",
    "created_at": "2010-01-02T22:59:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7729#issuecomment-66412",
    "user": "bump"
}
```

I posted a revised version. With this version, the base ring can be either a field
containing q1 and q2, or a LaurentPolynomialRing. The previous version did not
work with LaurentPolynomialRings.

Also, methods were added to
compute inverses of basis elements, a common task. 

Finally, there is a bug fix in
sage.categories.pushout (import PolynomialRing when needed).



---

archive/issue_comments_066413.json:
```json
{
    "body": "Attachment\n\nIwahori Hecke algebra patch, including revisions from",
    "created_at": "2010-01-06T04:48:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7729#issuecomment-66413",
    "user": "bump"
}
```

Attachment

Iwahori Hecke algebra patch, including revisions from



---

archive/issue_comments_066414.json:
```json
{
    "body": "I qfolded two patches from the trac server and re uploaded the patch.\n\n\n```\ntrac_7729-iwahori-hecke-fixdoctests-nt.patch\ntrac_7729-iwahori-hecke-reviewer-nt.patch\n```\n",
    "created_at": "2010-01-06T04:51:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7729#issuecomment-66414",
    "user": "bump"
}
```

I qfolded two patches from the trac server and re uploaded the patch.


```
trac_7729-iwahori-hecke-fixdoctests-nt.patch
trac_7729-iwahori-hecke-reviewer-nt.patch
```




---

archive/issue_comments_066415.json:
```json
{
    "body": "IwahoriHeckeAlgebraT now takes a Coxeter group + moved method to ModulesWithBasis. Replaces the previous patch.",
    "created_at": "2010-01-06T15:47:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7729#issuecomment-66415",
    "user": "nthiery"
}
```

IwahoriHeckeAlgebraT now takes a Coxeter group + moved method to ModulesWithBasis. Replaces the previous patch.



---

archive/issue_comments_066416.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-01-06T15:48:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7729#issuecomment-66416",
    "user": "nthiery"
}
```

Attachment



---

archive/issue_comments_066417.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-01-06T18:14:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7729#issuecomment-66417",
    "user": "bump"
}
```

Attachment



---

archive/issue_comments_066418.json:
```json
{
    "body": "I made minor revisions to the docstring and reposted the patch as\ntrac_7729_iwahori-hecke-algebra-2.patch.",
    "created_at": "2010-01-06T18:15:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7729#issuecomment-66418",
    "user": "bump"
}
```

I made minor revisions to the docstring and reposted the patch as
trac_7729_iwahori-hecke-algebra-2.patch.



---

archive/issue_comments_066419.json:
```json
{
    "body": "The patch trac_7729_iwahori_hecke_algebra_3.patch implements Anne Schilling's\ncomments from:\n\nhttp://groups.google.com/group/sage-combinat-devel/msg/e2abca2135c73e33?hl=en\n\nIt also adds Nicolas as an author, and fixes the copyright year.\n\nDan",
    "created_at": "2010-01-07T13:51:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7729#issuecomment-66419",
    "user": "bump"
}
```

The patch trac_7729_iwahori_hecke_algebra_3.patch implements Anne Schilling's
comments from:

http://groups.google.com/group/sage-combinat-devel/msg/e2abca2135c73e33?hl=en

It also adds Nicolas as an author, and fixes the copyright year.

Dan



---

archive/issue_comments_066420.json:
```json
{
    "body": "Attachment\n\nImplements Iwahori Hecke algebras",
    "created_at": "2010-01-07T14:05:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7729#issuecomment-66420",
    "user": "bump"
}
```

Attachment

Implements Iwahori Hecke algebras



---

archive/issue_comments_066421.json:
```json
{
    "body": "This patch implements the much desired Iwahori Hecke algebras in sage. It is very well documented with explanations on usage and references to the literature. All methods have doctests and all tests pass. In particular, I tested several special cases (like the nilCoxeter case q_1=q_2=0) and everything seemed to work fine.",
    "created_at": "2010-01-07T19:57:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7729#issuecomment-66421",
    "user": "aschilling"
}
```

This patch implements the much desired Iwahori Hecke algebras in sage. It is very well documented with explanations on usage and references to the literature. All methods have doctests and all tests pass. In particular, I tested several special cases (like the nilCoxeter case q_1=q_2=0) and everything seemed to work fine.



---

archive/issue_comments_066422.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-07T19:57:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7729#issuecomment-66422",
    "user": "aschilling"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066423.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-13T09:35:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7729#issuecomment-66423",
    "user": "rlm"
}
```

Resolution: fixed
