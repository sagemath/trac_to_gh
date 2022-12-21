# Issue 9019: Full doctest coverage for sage.categories.map

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2010-05-22 17:34:21

Assignee: nthiery

Keywords: doctest map composition

Apart from full doctest coverage for sage.categories.map, the patch provides the following:

1. Test for injectivity and surjectivity of `MatrixMorphism`:

```
sage: V1 = QQ^2
sage: V2 = QQ^3
sage: phi = V1.hom(Matrix([[1,2],[3,4],[5,6]]),V2)
sage: phi.is_injective()
True
sage: phi.is_surjective()
False
sage: psi = V2.hom(Matrix([[1,2,3],[4,5,6]]),V1)
sage: psi.is_injective()
False
sage: psi.is_surjective()
True
```


2. Composition of a `RingHomomorphism_im_gens` with another ring homomorphism (this used to return a `FormalCompositeMap`, which is not very efficient):

```
sage: R.<x,y> = QQ[]
sage: S.<a,b> = QQ[]
sage: f = R.hom([a+b,a-b])
sage: g = S.hom(Frac(S))
sage: g*f
Ring morphism:
  From: Multivariate Polynomial Ring in x, y over Rational Field
  To:   Fraction Field of Multivariate Polynomial Ring in a, b over Rational Field
  Defn: x |--> a + b
        y |--> a - b
sage: h = S.hom([x+y,x-y])
sage: h*f
Ring endomorphism of Multivariate Polynomial Ring in x, y over Rational Field
  Defn: x |--> 2*x
        y |--> 2*y
```


3. Comparison of `FormalCompositeMap`s:

```
sage: R.<x,y> = QQ[]
sage: S.<a,b> = QQ[]
sage: f = R.hom([a+b,a-b])
sage: g = S.hom([x+y,x-y])
sage: from sage.categories.map import FormalCompositeMap
sage: H = Hom(R,R,Rings())
sage: m = FormalCompositeMap(H,f,g)
sage: m == loads(dumps(m))  # this used to be False!
True
```




---

Attachment

is_injective/is_surjective for MatrixMorphism, cmp for FormalCompositeMap, more efficient composition of ring homomorphisms, full doctest coverage for sage.categories.map


---

Comment by SimonKing created at 2010-05-22 17:37:23

Changing status from new to needs_review.


---

Attachment

Looks good, positive review, modulo approval of my tiny referee patch that adds an actual example for Map.section()


---

Comment by SimonKing created at 2010-05-25 07:27:12

Changing status from needs_review to positive_review.


---

Comment by SimonKing created at 2010-05-25 07:27:12

Replying to [comment:2 robertwb]:
> Looks good, positive review, modulo approval of my tiny referee patch that adds an actual example for Map.section()

Dear Robert,

Thank you for the review and the example!

I don't know if I am in the position to approve your example, but it works for me, so that I take this as a positive review.

If nobody opposes, I'll insert your name as a reviewer and mark the ticket accordingly.

Cheers,

Simon


---

Comment by mhansen created at 2010-06-05 21:59:26

Resolution: fixed
