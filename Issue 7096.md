# Issue 7096: bug in dual isogeny computation

archive/issues_007096.json:
```json
{
    "body": "Assignee: davidloeffler\n\nCC:  shumow@gmail.com\n\nKeywords: elliptic curve isogeny\n\n\n```\nsage: p = 1019\nsage: F = GF(p)\nsage: E = EllipticCurve(F,[1,-1,0,1,1])\nsage: psi = E.division_polynomial(7).factor()[3][0]\nsage: phi = E.isogeny(kernel=psi)\nsage: assert phi.degree()==7\nsage: phi.dual()\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/home/jec/.sage/temp/selmer/14232/_home_jec__sage_init_sage_0.py in <module>()\n\n/home/jec/sage-4.1.2.rc0/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_curve_isogeny.pyc in dual(self)\n   2998\n   2999         phi_hat.set_pre_isomorphism(pre_isom)\n-> 3000         phi_hat.set_post_isomorphism(post_isom)\n   3001\n   3002         self.__dual = phi_hat\n\n/home/jec/sage-4.1.2.rc0/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_curve_isogeny.pyc in set_post_isomorphism(self, postWI)\n   2627\n   2628         if (self.__E2 != WIdom):\n-> 2629             raise ValueError, \"Invalid parameter: isomorphism must have domain curve equal to this isogenies'codomain.\"\n   2630\n   2631         if (None == self.__post_isomorphism):\n\nValueError: Invalid parameter: isomorphism must have domain curve equal to this isogenies' codomain.\n```\n\n\nThis looks like something which should be easy to fix.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7096\n\n",
    "created_at": "2009-10-02T15:05:02Z",
    "labels": [
        "elliptic curves",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "bug in dual isogeny computation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7096",
    "user": "cremona"
}
```
Assignee: davidloeffler

CC:  shumow@gmail.com

Keywords: elliptic curve isogeny


```
sage: p = 1019
sage: F = GF(p)
sage: E = EllipticCurve(F,[1,-1,0,1,1])
sage: psi = E.division_polynomial(7).factor()[3][0]
sage: phi = E.isogeny(kernel=psi)
sage: assert phi.degree()==7
sage: phi.dual()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/jec/.sage/temp/selmer/14232/_home_jec__sage_init_sage_0.py in <module>()

/home/jec/sage-4.1.2.rc0/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_curve_isogeny.pyc in dual(self)
   2998
   2999         phi_hat.set_pre_isomorphism(pre_isom)
-> 3000         phi_hat.set_post_isomorphism(post_isom)
   3001
   3002         self.__dual = phi_hat

/home/jec/sage-4.1.2.rc0/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_curve_isogeny.pyc in set_post_isomorphism(self, postWI)
   2627
   2628         if (self.__E2 != WIdom):
-> 2629             raise ValueError, "Invalid parameter: isomorphism must have domain curve equal to this isogenies'codomain."
   2630
   2631         if (None == self.__post_isomorphism):

ValueError: Invalid parameter: isomorphism must have domain curve equal to this isogenies' codomain.
```


This looks like something which should be easy to fix.

Issue created by migration from https://trac.sagemath.org/ticket/7096





---

archive/issue_comments_058697.json:
```json
{
    "body": "Remove assignee davidloeffler.",
    "created_at": "2009-10-09T09:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7096#issuecomment-58697",
    "user": "davidloeffler"
}
```

Remove assignee davidloeffler.



---

archive/issue_comments_058698.json:
```json
{
    "body": "While looking at the code of `{dual()`, I found a second bug in this\n\n\n```\nE = EllipticCurve(GF(7),[1,-1,1,-3,3])\nphi = E.isogeny(E([1,0]))\nphi.dual()\n```\n\n\ngives a ZeroDivisionError. Only separable isogenies are implented, so one can not possibly take the dual of this separable isogeny of degree 7 in chracteristic 7. A quick check should be introduced here.",
    "created_at": "2009-10-09T09:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7096#issuecomment-58698",
    "user": "wuthrich"
}
```

While looking at the code of `{dual()`, I found a second bug in this


```
E = EllipticCurve(GF(7),[1,-1,1,-3,3])
phi = E.isogeny(E([1,0]))
phi.dual()
```


gives a ZeroDivisionError. Only separable isogenies are implented, so one can not possibly take the dual of this separable isogeny of degree 7 in chracteristic 7. A quick check should be introduced here.



---

archive/issue_comments_058699.json:
```json
{
    "body": "Yet another, bigger problem with dual() : Say E -> E' is an isogeny of degree d, then all the algorithm does is creating an isogeny E' -> E of degree d. This does not guarantee that it is the dual; it could be the dual composed with an automorphism, like [-1]. This probably happens quite often as it uses `WeierstrassIsomorphism(E,E')`. This returns one of the isomorphisms without any control of it, hence often the sign will be wrong.\n\nThe function dual definitely needs a lot of work.\n\nNow, the actual bug reported in this ticket is not in dual but occurs as\n\n```\nE1 = EllipticCurve(GF(1013),[1,-1,0,288,19])\nE2 = EllipticCurve(GF(1013),[7,970,0,363,464])\nEllipticCurveIsogeny(E1,None,E2,7)\n```\n",
    "created_at": "2009-10-09T10:45:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7096#issuecomment-58699",
    "user": "wuthrich"
}
```

Yet another, bigger problem with dual() : Say E -> E' is an isogeny of degree d, then all the algorithm does is creating an isogeny E' -> E of degree d. This does not guarantee that it is the dual; it could be the dual composed with an automorphism, like [-1]. This probably happens quite often as it uses `WeierstrassIsomorphism(E,E')`. This returns one of the isomorphisms without any control of it, hence often the sign will be wrong.

The function dual definitely needs a lot of work.

Now, the actual bug reported in this ticket is not in dual but occurs as

```
E1 = EllipticCurve(GF(1013),[1,-1,0,288,19])
E2 = EllipticCurve(GF(1013),[7,970,0,363,464])
EllipticCurveIsogeny(E1,None,E2,7)
```




---

archive/issue_comments_058700.json:
```json
{
    "body": "Of course the field in the previous lines should be 1019. The output is\n\n\n```\nIsogeny of degree 7 from Elliptic Curve defined by y^2 + x*y = x^3 + 1018*x^2 + 288*x + 19 over Finite Field of size 1019 to Elliptic Curve defined by y^2 + 7*x*y + 850*y = x^3 + 970*x^2 + 445*x + 202 over Finite Field of size 1019\n```\n\n\nwhich has visibly the wrong, but an isomorphic codomain.\nAfter 1 hour of chasing through the code, I was not able to find the error. I include the author as CC in the hope that he might have an idea.",
    "created_at": "2009-10-09T11:52:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7096#issuecomment-58700",
    "user": "wuthrich"
}
```

Of course the field in the previous lines should be 1019. The output is


```
Isogeny of degree 7 from Elliptic Curve defined by y^2 + x*y = x^3 + 1018*x^2 + 288*x + 19 over Finite Field of size 1019 to Elliptic Curve defined by y^2 + 7*x*y + 850*y = x^3 + 970*x^2 + 445*x + 202 over Finite Field of size 1019
```


which has visibly the wrong, but an isomorphic codomain.
After 1 hour of chasing through the code, I was not able to find the error. I include the author as CC in the hope that he might have an idea.



---

archive/issue_comments_058701.json:
```json
{
    "body": "Attachment [trac_7096.patch](tarball://root/attachments/some-uuid/ticket7096/trac_7096.patch) by wuthrich created at 2009-10-17 23:10:34\n\napplies to 4.1.2. after trac #6886. this is only a provisional patch.",
    "created_at": "2009-10-17T23:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7096#issuecomment-58701",
    "user": "wuthrich"
}
```

Attachment [trac_7096.patch](tarball://root/attachments/some-uuid/ticket7096/trac_7096.patch) by wuthrich created at 2009-10-17 23:10:34

applies to 4.1.2. after trac #6886. this is only a provisional patch.



---

archive/issue_comments_058702.json:
```json
{
    "body": "I worked on the bugs for isogenies and I found two. They should be corrected with the above patch. But I have to do some more work and test it carefully, before it is ready for a review.",
    "created_at": "2009-10-17T23:13:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7096#issuecomment-58702",
    "user": "wuthrich"
}
```

I worked on the bugs for isogenies and I found two. They should be corrected with the above patch. But I have to do some more work and test it carefully, before it is ready for a review.



---

archive/issue_comments_058703.json:
```json
{
    "body": "I started implementing some more related to this ticket. Especially the `formal()` for isogeny. Then there are two ideas how to compute the dual.\n\n* I can take the implementation as it is now. This yields **a** isogeny of the correct degree\n  in the opposite direction. Then I can compute the leading term of the composition in the \n  formal expansion (or simply check to what multiple the differential is pulled-back to). This \n  gives me the `WeierstrassIsomorphism` to use. I am not 100 % sure if this will work in\n  all cases. Say the elliptic curve is defined over a finite field and has a cyclic isogeny of\n  degree *n<sup>2</sup>* to itself. It is certain that our current implementation gives back a cyclic \n  isogeny and not just *[n]*. I fear one could find counterexamples... I have to do some \n  testings.\n* Otherwise, I will try to implement the full computation of the dual via the formal group. I \n  believe that there is an algorithm with running time *O(n)* for an isogeny of prime degree \n  *n*. Though I have not checked this in details. It would only involve to compute the first \n  *2n* coefficients in *[n]* and the `division_polynomial` in the formal expansion. The \n  one example I have computed so far by hand was a failure :(. One obstacle here will be the \n  fact that `.reversion()` is only defined for power-series with coefficients in **Q**.\n\n\u00e0 suivre.",
    "created_at": "2009-10-23T09:08:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7096#issuecomment-58703",
    "user": "wuthrich"
}
```

I started implementing some more related to this ticket. Especially the `formal()` for isogeny. Then there are two ideas how to compute the dual.

* I can take the implementation as it is now. This yields **a** isogeny of the correct degree
  in the opposite direction. Then I can compute the leading term of the composition in the 
  formal expansion (or simply check to what multiple the differential is pulled-back to). This 
  gives me the `WeierstrassIsomorphism` to use. I am not 100 % sure if this will work in
  all cases. Say the elliptic curve is defined over a finite field and has a cyclic isogeny of
  degree *n<sup>2</sup>* to itself. It is certain that our current implementation gives back a cyclic 
  isogeny and not just *[n]*. I fear one could find counterexamples... I have to do some 
  testings.
* Otherwise, I will try to implement the full computation of the dual via the formal group. I 
  believe that there is an algorithm with running time *O(n)* for an isogeny of prime degree 
  *n*. Though I have not checked this in details. It would only involve to compute the first 
  *2n* coefficients in *[n]* and the `division_polynomial` in the formal expansion. The 
  one example I have computed so far by hand was a failure :(. One obstacle here will be the 
  fact that `.reversion()` is only defined for power-series with coefficients in **Q**.

à suivre.



---

archive/issue_comments_058704.json:
```json
{
    "body": "I found another issue with isogenies.\n\n\n```\nE = EllipticCurve('11a1')\nE2 = EllipticCurve('11a2')\nE2.isogeny(None,codomain=E1,degree=5)\n```\n\n\nfails with \n\n\n```\nValueError: Codomain parameter must be isomorphic to computed codomain isogeny\n```\n\n\nwhile `E.isogeny(None,codomain=E2,degree=5)` works fine. The reason is that the algorithm for computing the kernel polynomial in `compute_isogeny_starks` is only valid for **normalised** isogenies. \n\nStark's algorithm is implemented in ell_curve_isogeny.py from scratch and so it contains the computation of the formal expansion of the Weierstrass p function. I wonder if we should add as another possible algorithm to do the same sort of computation, but using the already existing code for formal groups instead. ....",
    "created_at": "2009-10-23T23:47:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7096#issuecomment-58704",
    "user": "wuthrich"
}
```

I found another issue with isogenies.


```
E = EllipticCurve('11a1')
E2 = EllipticCurve('11a2')
E2.isogeny(None,codomain=E1,degree=5)
```


fails with 


```
ValueError: Codomain parameter must be isomorphic to computed codomain isogeny
```


while `E.isogeny(None,codomain=E2,degree=5)` works fine. The reason is that the algorithm for computing the kernel polynomial in `compute_isogeny_starks` is only valid for **normalised** isogenies. 

Stark's algorithm is implemented in ell_curve_isogeny.py from scratch and so it contains the computation of the formal expansion of the Weierstrass p function. I wonder if we should add as another possible algorithm to do the same sort of computation, but using the already existing code for formal groups instead. ....



---

archive/issue_comments_058705.json:
```json
{
    "body": "Yet another bug with `dual`. I have to chase that. It does not look like being related to the previously reported bugs.\n\n\n```\nk = GF(103)\nE = EllipticCurve(k,[1,0,0,1,-1])\nP = E(60,85)\nphi = E.isogeny(P)\nphi.dual()\n```\n\n\ngives\n\n\n```\nIndexError: list index out of range\n```\n\n\nin  line 3789.\n\n(I keep on adding these bugs here and I try to resolve as many as I can with the patch for this. Only then I will open new tickets for the remaining ones)",
    "created_at": "2009-10-24T17:29:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7096#issuecomment-58705",
    "user": "wuthrich"
}
```

Yet another bug with `dual`. I have to chase that. It does not look like being related to the previously reported bugs.


```
k = GF(103)
E = EllipticCurve(k,[1,0,0,1,-1])
P = E(60,85)
phi = E.isogeny(P)
phi.dual()
```


gives


```
IndexError: list index out of range
```


in  line 3789.

(I keep on adding these bugs here and I try to resolve as many as I can with the patch for this. Only then I will open new tickets for the remaining ones)



---

archive/issue_comments_058706.json:
```json
{
    "body": "Thanks for your work on this.  Perhaps we should make dual raise a NotImplementedError since it fails in so many different ways?\n\nI think that when Dan Shumow implemented all the isogeny stuff he was mainly interested in certain kinds of isogenies (over finite fields?) so did not test as much in other situations.  Just guessing.  [For example, he added the model parameter on my request, over Q only;  I would have made that the default over Q.]",
    "created_at": "2009-10-24T19:19:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7096#issuecomment-58706",
    "user": "cremona"
}
```

Thanks for your work on this.  Perhaps we should make dual raise a NotImplementedError since it fails in so many different ways?

I think that when Dan Shumow implemented all the isogeny stuff he was mainly interested in certain kinds of isogenies (over finite fields?) so did not test as much in other situations.  Just guessing.  [For example, he added the model parameter on my request, over Q only;  I would have made that the default over Q.]



---

archive/issue_comments_058707.json:
```json
{
    "body": "The problem is that most errors go back to problems for the `EllipticCurveIsogeny` constructor itself. So they can be recreated without `dual`. Of course, I don't want `isogeny()` to raise a `NotImplementedError`. But I will include warnings in the documentation...",
    "created_at": "2009-10-24T20:22:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7096#issuecomment-58707",
    "user": "wuthrich"
}
```

The problem is that most errors go back to problems for the `EllipticCurveIsogeny` constructor itself. So they can be recreated without `dual`. Of course, I don't want `isogeny()` to raise a `NotImplementedError`. But I will include warnings in the documentation...



---

archive/issue_comments_058708.json:
```json
{
    "body": "Attachment [trac_7096_2.patch](tarball://root/attachments/some-uuid/ticket7096/trac_7096_2.patch) by wuthrich created at 2009-10-29 13:37:28\n\nAnother preliminary version. Replaces the previous patch.",
    "created_at": "2009-10-29T13:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7096#issuecomment-58708",
    "user": "wuthrich"
}
```

Attachment [trac_7096_2.patch](tarball://root/attachments/some-uuid/ticket7096/trac_7096_2.patch) by wuthrich created at 2009-10-29 13:37:28

Another preliminary version. Replaces the previous patch.



---

archive/issue_comments_058709.json:
```json
{
    "body": "OK. Here we go. That is a patch for this ticket that I would like to be reviewed.\n\nI explain all the changes it introduces as it is quite a long and complicated patch. (I like the fact that the initial comment on the ticket was *\"This looks like something which should be easy to fix.\"* while it took me a month of quite hard work.)\n\n* I moved the computation of the weierstrass p-function into a seperate file ell_wp.py.\n  I also completely clean it. It used to contain a lot of functions on power series that\n  are already implemented in sage. There is an option now to call the pari version.\n* I added a `weierstrass_p` to ell_field.py.\n* Having redone all the weierstrass_p with laurent and power series rather than with \n  polynomials, also got rid of the `IndexError` mentioned above.\n* The dual is now correct and not just up to an automorphism.\n* When trying to give an isogeny with a codomain, it now checks if the algorithm fails\n  (typically because there is no cyclic normalized isogeny of this degree). This eliminates a\n  bad bug that was known in the code.\n* We can now take duals of non-normalized isogenies\n* There is a new function `formal` that computes the formal expansion of the isogeny.\n* This `formal` can be used to check if the isogeny is normalized; this simplifies and\n  corrects the previous code (which is still there but deprecated).\n* I included a check to forbid `dual` of isogenies of degree divisible by the \n  charactersitic.\n* I updated a lot of the documentation of isogenies.\n* And I also changed the starting documentation of ell_generic.py to clarify what we mean by\n  an elliptic curve in sage.\n \nThere is still a lot that should be done about isogenies for elliptic curves. I hope this patch corrects and clarifies what is possible right now. For further things that one could wish for in sage concerning isogenies and endomorphisms I opened ticket #7368 as a follow up.\n\nNote that this ticket also includes the correction asked for in #7307.",
    "created_at": "2009-11-01T14:28:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7096#issuecomment-58709",
    "user": "wuthrich"
}
```

OK. Here we go. That is a patch for this ticket that I would like to be reviewed.

I explain all the changes it introduces as it is quite a long and complicated patch. (I like the fact that the initial comment on the ticket was *"This looks like something which should be easy to fix."* while it took me a month of quite hard work.)

* I moved the computation of the weierstrass p-function into a seperate file ell_wp.py.
  I also completely clean it. It used to contain a lot of functions on power series that
  are already implemented in sage. There is an option now to call the pari version.
* I added a `weierstrass_p` to ell_field.py.
* Having redone all the weierstrass_p with laurent and power series rather than with 
  polynomials, also got rid of the `IndexError` mentioned above.
* The dual is now correct and not just up to an automorphism.
* When trying to give an isogeny with a codomain, it now checks if the algorithm fails
  (typically because there is no cyclic normalized isogeny of this degree). This eliminates a
  bad bug that was known in the code.
* We can now take duals of non-normalized isogenies
* There is a new function `formal` that computes the formal expansion of the isogeny.
* This `formal` can be used to check if the isogeny is normalized; this simplifies and
  corrects the previous code (which is still there but deprecated).
* I included a check to forbid `dual` of isogenies of degree divisible by the 
  charactersitic.
* I updated a lot of the documentation of isogenies.
* And I also changed the starting documentation of ell_generic.py to clarify what we mean by
  an elliptic curve in sage.
 
There is still a lot that should be done about isogenies for elliptic curves. I hope this patch corrects and clarifies what is possible right now. For further things that one could wish for in sage concerning isogenies and endomorphisms I opened ticket #7368 as a follow up.

Note that this ticket also includes the correction asked for in #7307.



---

archive/issue_comments_058710.json:
```json
{
    "body": "Attachment [trac_7096_3.patch](tarball://root/attachments/some-uuid/ticket7096/trac_7096_3.patch) by wuthrich created at 2009-11-01 14:29:56\n\npatch for this ticket exported against 4.2.alpha1. (in particular after #6886). This patch should be reviewed while the previously submitted should be ignored.",
    "created_at": "2009-11-01T14:29:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7096#issuecomment-58710",
    "user": "wuthrich"
}
```

Attachment [trac_7096_3.patch](tarball://root/attachments/some-uuid/ticket7096/trac_7096_3.patch) by wuthrich created at 2009-11-01 14:29:56

patch for this ticket exported against 4.2.alpha1. (in particular after #6886). This patch should be reviewed while the previously submitted should be ignored.



---

archive/issue_comments_058711.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-01T14:30:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7096#issuecomment-58711",
    "user": "wuthrich"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_058712.json:
```json
{
    "body": "Sorry I saw that the patch does not include the new file ell_wp.py.",
    "created_at": "2009-11-01T14:33:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7096#issuecomment-58712",
    "user": "wuthrich"
}
```

Sorry I saw that the patch does not include the new file ell_wp.py.



---

archive/issue_comments_058713.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-01T14:33:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7096#issuecomment-58713",
    "user": "wuthrich"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_058714.json:
```json
{
    "body": "You have done a great job, and I look forward to studying it in detail.  Unfortunately other work prevents me from doing so for quite a while, so although I was the one who posted this (complete with under-estimation of the work involved) I would be very happy if someone else interested reviews it first.",
    "created_at": "2009-11-01T15:06:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7096#issuecomment-58714",
    "user": "cremona"
}
```

You have done a great job, and I look forward to studying it in detail.  Unfortunately other work prevents me from doing so for quite a while, so although I was the one who posted this (complete with under-estimation of the work involved) I would be very happy if someone else interested reviews it first.



---

archive/issue_comments_058715.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-01T15:06:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7096#issuecomment-58715",
    "user": "cremona"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_058716.json:
```json
{
    "body": "After writing the above I went ahead anyway and read the patch -- when ell_wp.py is added too I'll try test to test it as well.",
    "created_at": "2009-11-01T15:15:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7096#issuecomment-58716",
    "user": "cremona"
}
```

After writing the above I went ahead anyway and read the patch -- when ell_wp.py is added too I'll try test to test it as well.



---

archive/issue_comments_058717.json:
```json
{
    "body": "Attachment [trac_7096_4.patch](tarball://root/attachments/some-uuid/ticket7096/trac_7096_4.patch) by wuthrich created at 2009-11-01 15:19:43\n\nReplaces all previous patches.",
    "created_at": "2009-11-01T15:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7096#issuecomment-58717",
    "user": "wuthrich"
}
```

Attachment [trac_7096_4.patch](tarball://root/attachments/some-uuid/ticket7096/trac_7096_4.patch) by wuthrich created at 2009-11-01 15:19:43

Replaces all previous patches.



---

archive/issue_comments_058718.json:
```json
{
    "body": "Ok that was easy. now it should be review-able.",
    "created_at": "2009-11-01T15:23:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7096#issuecomment-58718",
    "user": "wuthrich"
}
```

Ok that was easy. now it should be review-able.



---

archive/issue_comments_058719.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-01T17:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7096#issuecomment-58719",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058720.json:
```json
{
    "body": "OK, I relented and have reviewed the patch.  It is great.  It applies fine to 4.2 and builds and tests ok.  (Even better, my not-yet-complete patch for #6887 applied OK on top of this, so a large piece of work which uses isogenies a lot still works fine;  that is a very good test, I think).  I also built and read through the documentation, which is good -- better than before in several respects.  I may have spotted a typo or too but did not note them down so will not delay things by hunting them down.\n\nPositive review: and gives me a spur to finish #6887.",
    "created_at": "2009-11-01T17:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7096#issuecomment-58720",
    "user": "cremona"
}
```

OK, I relented and have reviewed the patch.  It is great.  It applies fine to 4.2 and builds and tests ok.  (Even better, my not-yet-complete patch for #6887 applied OK on top of this, so a large piece of work which uses isogenies a lot still works fine;  that is a very good test, I think).  I also built and read through the documentation, which is good -- better than before in several respects.  I may have spotted a typo or too but did not note them down so will not delay things by hunting them down.

Positive review: and gives me a spur to finish #6887.



---

archive/issue_comments_058721.json:
```json
{
    "body": "That was quick ! Thanks a lot.\n\nChris.",
    "created_at": "2009-11-01T17:37:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7096#issuecomment-58721",
    "user": "wuthrich"
}
```

That was quick ! Thanks a lot.

Chris.



---

archive/issue_comments_058722.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-02T04:49:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7096",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7096#issuecomment-58722",
    "user": "mhansen"
}
```

Resolution: fixed
