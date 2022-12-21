# Issue 9384: descend_to method for elliptic curves

Issue created by migration from Trac.

Original creator: ebeyerstedt

Original creation time: 2010-06-29 22:24:01

Assignee: cremona

CC:  adeines cremona jeremywest

Keywords: descend, subfield, isomorphic, elliptic curve

Given a subfield K and an elliptic curve E defined over a field L, this function determines whether there exists an elliptic curve over K which is isomorphic over L to E. If one exists, it finds it.


---

Comment by ebeyerstedt created at 2010-06-29 23:46:50

This has been implemented in the patch. Please review.


---

Comment by ebeyerstedt created at 2010-06-29 23:46:50

Changing status from new to needs_review.


---

Comment by ebeyerstedt created at 2010-06-30 02:26:32

Note: This function does not yet work when j = 0, 1728.


---

Attachment


---

Comment by ebeyerstedt created at 2010-06-30 03:46:54

The update handles the cases for j=0,1728.


---

Comment by aly.deines created at 2010-06-30 04:35:19

Changing status from needs_review to needs_work.


---

Comment by aly.deines created at 2010-06-30 04:35:19

The code for handling j=0,1728 needs to be cleaned up a little. Also, this function currently does not properly handle the following case

F.<b> = QuadraticField(23)
K.<a> = F.extension(x^3+5)
E = EllipticCurve(j = 1728*b).change_ring(K)
E.descend_to(F)

It returns none when it should descend to the subfield F.


---

Comment by cremona created at 2010-06-30 11:33:52

It looks to me as though the curve returned is (sometimes) a twist of the original, rather than isomorphic -- but I have been flying all night so am not reliable!

You can check if there is an embedding of K in self.base_ring() like this:

```
sage: X = polygen(QQ)
sage: K.<a> = NumberField(X^4 - X^3 + 2*X^2 + X + 1)
sage: QQ.embeddings(K)
[Ring Coercion morphism:
  From: Rational Field
  To:   Number Field in a with defining polynomial x^4 - x^3 + 2*x^2 + x + 1]
```



---

Comment by ebeyerstedt created at 2010-07-02 05:14:48

This new patch should work in general. It uses the newly implemented preimage function for number field homomorphisms. Be sure to apply the patch from #9403 first.


---

Comment by ebeyerstedt created at 2010-07-02 05:14:48

Changing status from needs_work to needs_review.


---

Attachment

Replaces previous patch.


---

Comment by aly.deines created at 2010-07-02 19:57:16

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-07-27 00:51:24

Resolution: fixed


---

Comment by mpatel created at 2010-07-27 04:35:32

I'm entering a guess for the Reviewer(s) field.  Please correct me if I'm wrong.


---

Comment by cremona created at 2014-06-07 17:07:50

See follow-up ticket at #16456 where it is explained why the implementation here is deficient and needs fixing.
