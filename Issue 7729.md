# Issue 7729: Iwahori Hecke algebras

Issue created by migration from https://trac.sagemath.org/ticket/7729

Original creator: bump

Original creation time: 2009-12-18 01:36:46

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


---

Comment by bump created at 2009-12-18 16:26:02

I posted a new version. This version works either before or after the patch in #7718.


---

Comment by bump created at 2009-12-18 17:29:47

Changing component from algebra to combinatorics.


---

Comment by nthiery created at 2009-12-19 00:14:23

Changing status from new to needs_work.


---

Comment by nthiery created at 2009-12-19 00:14:23

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

Comment by bump created at 2009-12-19 00:23:57

I've revised it so that it works with affine Weyl groups.

I don't mind renaming it IwahoriHeckeAlgebraT but it seems to
me that perhaps other presentations can be handled within this
framework. I think I should leave the refactoring to the
category framework to you.

I will make the algebra generators into a family. When I've
done that I will change the status back to needs review.


---

Comment by bump created at 2009-12-19 01:10:19

I've addressed two out of three of Nicolas' requests, and his
message indicates that the refactoring issue can be postponed.

* The name is now `IwahoriHeckeAlgebraT`

* `self.algebra_generators()` now returns a finite family.

I've changed the status back to needs review.

Nicolas wrote:

> Do you mind renaming it into IwahoriHeckeAlgebraT or TBasis, so that we can later > use IwahoriHeckeAlgebra? for the abstract Iwahori Hecke algebra with its other bases?

what other bases do we need? There is the Bernstein Zelevinsky presentation.


---

Comment by bump created at 2009-12-19 01:10:19

Changing status from needs_work to needs_review.


---

Comment by bump created at 2010-01-02 22:59:58

I posted a revised version. With this version, the base ring can be either a field
containing q1 and q2, or a LaurentPolynomialRing. The previous version did not
work with LaurentPolynomialRings.

Also, methods were added to
compute inverses of basis elements, a common task. 

Finally, there is a bug fix in
sage.categories.pushout (import PolynomialRing when needed).


---

Attachment

Iwahori Hecke algebra patch, including revisions from


---

Comment by bump created at 2010-01-06 04:51:55

I qfolded two patches from the trac server and re uploaded the patch.


```
trac_7729-iwahori-hecke-fixdoctests-nt.patch
trac_7729-iwahori-hecke-reviewer-nt.patch
```



---

Comment by nthiery created at 2010-01-06 15:47:20

IwahoriHeckeAlgebraT now takes a Coxeter group + moved method to ModulesWithBasis. Replaces the previous patch.


---

Attachment


---

Attachment


---

Comment by bump created at 2010-01-06 18:15:57

I made minor revisions to the docstring and reposted the patch as
trac_7729_iwahori-hecke-algebra-2.patch.


---

Comment by bump created at 2010-01-07 13:51:48

The patch trac_7729_iwahori_hecke_algebra_3.patch implements Anne Schilling's
comments from:

http://groups.google.com/group/sage-combinat-devel/msg/e2abca2135c73e33?hl=en

It also adds Nicolas as an author, and fixes the copyright year.

Dan


---

Attachment

Implements Iwahori Hecke algebras


---

Comment by aschilling created at 2010-01-07 19:57:57

This patch implements the much desired Iwahori Hecke algebras in sage. It is very well documented with explanations on usage and references to the literature. All methods have doctests and all tests pass. In particular, I tested several special cases (like the nilCoxeter case q_1=q_2=0) and everything seemed to work fine.


---

Comment by aschilling created at 2010-01-07 19:57:57

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-13 09:35:49

Resolution: fixed
