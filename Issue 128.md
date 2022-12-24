# Issue 128: possible clash for EllipticCurve(j-invariant) signature

archive/issues_000128.json:
```json
{
    "body": "Assignee: was\n\nCC:  cremona jdemeyer\n\nSince Elliptic curves should probably have some things in common, one would probably at some point want signatures of the type\n\nEllipticCurve(f) and EllipticCurve(f,h)\n\nto define curves with models y^2=f(x) and y^2+h(x)*y=f(x).\nThis would clash with EllipticCurve(j-invariant) that exists now.\n\nExample:\n\nEllipticCurve(x^3-x)\n\nShould this create an elliptic curve over Q[x] with j-invariant x^3-x or should it create an elliptic curve over Q with equation y<sup>2=x</sup>3-x?\n\nMagma did go with the first for a while but decided to stick with the latter later.\n\nIssue created by migration from https://trac.sagemath.org/ticket/128\n\n",
    "created_at": "2006-10-14T05:31:06Z",
    "labels": [
        "algebraic geometry",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "possible clash for EllipticCurve(j-invariant) signature",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/128",
    "user": "nbruin"
}
```
Assignee: was

CC:  cremona jdemeyer

Since Elliptic curves should probably have some things in common, one would probably at some point want signatures of the type

EllipticCurve(f) and EllipticCurve(f,h)

to define curves with models y^2=f(x) and y^2+h(x)*y=f(x).
This would clash with EllipticCurve(j-invariant) that exists now.

Example:

EllipticCurve(x^3-x)

Should this create an elliptic curve over Q[x] with j-invariant x^3-x or should it create an elliptic curve over Q with equation y<sup>2=x</sup>3-x?

Magma did go with the first for a while but decided to stick with the latter later.

Issue created by migration from https://trac.sagemath.org/ticket/128





---

archive/issue_comments_000577.json:
```json
{
    "body": "Is this still an issue? I have added John to the CC field since he is the resident expert ;).\n\nJohn: Do you have an opinion on this? Feel free to ignore this if you have more pressing things to tend to.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-12T12:56:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-577",
    "user": "mabshoff"
}
```

Is this still an issue? I have added John to the CC field since he is the resident expert ;).

John: Do you have an opinion on this? Feel free to ignore this if you have more pressing things to tend to.

Cheers,

Michael



---

archive/issue_comments_000578.json:
```json
{
    "body": "It is still an issue in the sense that nothing has changed:\n\n```\nsage: R.<x>=QQ[]\nsage: E=EllipticCurve(x^3+1)\nsage: E\nElliptic Curve defined by y^2  = x^3 + (-3*x^6+5178*x^3+5181)*x + (-2*x^9+6906*x^6-5958150*x^3-5965058) over Fraction Field of Univariate Polynomial Ring in x over Rational Field\nsage: E.j_invariant()\nx^3 + 1\n```\n\n\nPersonally I would *not* want the EllipticCurve() function to do something totally different if passed one thing which happened to be a polynomial (or a pair of polynomials) -- but then I just don't think of elliptic curves as being defined by polynomials.\n\nNote that this *does* work:\n\n```\nsage: H.genus()\n1\nsage: R.<x>=QQ[]\nsage: H=HyperellipticCurve(x^3+1)\nsage: H\nHyperelliptic Curve over Rational Field defined by y^2 = x^3 + 1\nsage: H.genus()\n1\nsage: H.hyperelliptic_polynomials()\n(x^3 + 1, 0)\n```\n\nand the HyperellipticCurve() function *only* takes a polynomial (or two) as inputs, something which I would not suggest changing.\n\nHence it might be reasonable to proceed as follows.  Keep the existing facility for defining a HyperellipticCurve of genus 1 out of two polynomials, and define a new constructor EllipticCurve() which takes a HyperellipticCurve H (of genus 1 of course) as input.  This would require that the first of H.hyperelliptic_polynomials() was monic and degree 3, and that the second had degree at most 1, otherwise an exception would be raised.\n\nIf this was implemented then at least this would work:\n\n```\nE=EllipticCurve(HyperellipticCurve(x^3+1,x+1))\n```\n\nand result in the elliptic curve y<sup>2+x*y+y=x</sup>3+1.\n\nIs Nils receiving this?  Does he have an opinion?",
    "created_at": "2008-04-12T13:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-578",
    "user": "cremona"
}
```

It is still an issue in the sense that nothing has changed:

```
sage: R.<x>=QQ[]
sage: E=EllipticCurve(x^3+1)
sage: E
Elliptic Curve defined by y^2  = x^3 + (-3*x^6+5178*x^3+5181)*x + (-2*x^9+6906*x^6-5958150*x^3-5965058) over Fraction Field of Univariate Polynomial Ring in x over Rational Field
sage: E.j_invariant()
x^3 + 1
```


Personally I would *not* want the EllipticCurve() function to do something totally different if passed one thing which happened to be a polynomial (or a pair of polynomials) -- but then I just don't think of elliptic curves as being defined by polynomials.

Note that this *does* work:

```
sage: H.genus()
1
sage: R.<x>=QQ[]
sage: H=HyperellipticCurve(x^3+1)
sage: H
Hyperelliptic Curve over Rational Field defined by y^2 = x^3 + 1
sage: H.genus()
1
sage: H.hyperelliptic_polynomials()
(x^3 + 1, 0)
```

and the HyperellipticCurve() function *only* takes a polynomial (or two) as inputs, something which I would not suggest changing.

Hence it might be reasonable to proceed as follows.  Keep the existing facility for defining a HyperellipticCurve of genus 1 out of two polynomials, and define a new constructor EllipticCurve() which takes a HyperellipticCurve H (of genus 1 of course) as input.  This would require that the first of H.hyperelliptic_polynomials() was monic and degree 3, and that the second had degree at most 1, otherwise an exception would be raised.

If this was implemented then at least this would work:

```
E=EllipticCurve(HyperellipticCurve(x^3+1,x+1))
```

and result in the elliptic curve y<sup>2+x*y+y=x</sup>3+1.

Is Nils receiving this?  Does he have an opinion?



---

archive/issue_comments_000579.json:
```json
{
    "body": "First of all, sorry for the typo in the original report. I meant \"in common with hyperelliptic curves\". Subsequent commentary is consistent with that. The idea is that \"elliptic curves in Weierstrass form\" can be viewed as a subcategory of \"double covers of `P^1`\" that hyperelliptic curves in computer algebra seem to symbolize, and hence that everything that works for hyperelliptic curves should work for elliptic curves as well.\n\nI do think of (models of) elliptic curves as being defined by polynomials, so for me the proposed signatures EllipticCurve(f) and EllipticCurve(f,h) feel very natural. Sage itself agrees:\n\n```\nsage: EllipticCurve(1)\nElliptic Curve defined by y^2  = x^3 + 5181*x - 5965058 over Rational Field\n```\n\nThe way the curve is printed seems to indicate that the curve is indeed defined by a polynomial (apart from the \"`y^2=`\" bit).\n\nThe signature EllipticCurve(HyperellipticCurve(..)) should indeed work at some point as well, which makes me think that the design decisions made here should be looked at in the broader setting of how algebraic geometry constructions will work in sage. Ultimately, sage is going to have to be able to have functions of the type\n\nmake_elliptic_curve_from(cubic, rational point)\nmake_elliptic_curve_from(singular plane quartic, rational point)\nmake_elliptic_curve_from(genus 1 curve, degree 1 divisor)\ngive_jacobian_as_elliptic_curve(genus 1 curve)\n\nMost of these (and also the make_elliptic_curve(hyperelliptic curve) signature) should be able to return a birational map. Since those maps are not canonical to neither the curve nor the elliptic curve, we can't really handle those maps via the coercion system, so the magmatic solution of returning the map as a second value seems most natural to me.\n\nI'm not sure if some of those should be overloaded into the EllipticCurve constructor (I would like that, because it's what I'm used to in magma. Constructors in sage seem to be very lenient in what they accept as input anyway)\n\nThe relevance for this report:\n\nIf the EllipticCurve constructor is going to be rather liberal in what it accepts for input, then I think people will expect it can take defining polynomials as well, and they won't expect an elliptic curve that happens to have a j-invariant equal to that polynomial as a return value.\n\nI agree with John that EllipticCurve(<ring element>) should behave differently depending on the type of ring that is put in. Given that in most cases the j-invariant does -not- determine uniquely an elliptic curve over the ring the j-invariant lives in, I think that the section map of\n\n<elliptic curves> -> <j-invariants>\n\nshould not be used as a valid default constructor for EllipticCurve. Instead have a function elliptic_curve_from_j_invariant, or some more palatable name. However, that's just my opinion. David Kohel's opinion would be interesting here as well.",
    "created_at": "2008-04-14T18:15:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-579",
    "user": "nbruin"
}
```

First of all, sorry for the typo in the original report. I meant "in common with hyperelliptic curves". Subsequent commentary is consistent with that. The idea is that "elliptic curves in Weierstrass form" can be viewed as a subcategory of "double covers of `P^1`" that hyperelliptic curves in computer algebra seem to symbolize, and hence that everything that works for hyperelliptic curves should work for elliptic curves as well.

I do think of (models of) elliptic curves as being defined by polynomials, so for me the proposed signatures EllipticCurve(f) and EllipticCurve(f,h) feel very natural. Sage itself agrees:

```
sage: EllipticCurve(1)
Elliptic Curve defined by y^2  = x^3 + 5181*x - 5965058 over Rational Field
```

The way the curve is printed seems to indicate that the curve is indeed defined by a polynomial (apart from the "`y^2=`" bit).

The signature EllipticCurve(HyperellipticCurve(..)) should indeed work at some point as well, which makes me think that the design decisions made here should be looked at in the broader setting of how algebraic geometry constructions will work in sage. Ultimately, sage is going to have to be able to have functions of the type

make_elliptic_curve_from(cubic, rational point)
make_elliptic_curve_from(singular plane quartic, rational point)
make_elliptic_curve_from(genus 1 curve, degree 1 divisor)
give_jacobian_as_elliptic_curve(genus 1 curve)

Most of these (and also the make_elliptic_curve(hyperelliptic curve) signature) should be able to return a birational map. Since those maps are not canonical to neither the curve nor the elliptic curve, we can't really handle those maps via the coercion system, so the magmatic solution of returning the map as a second value seems most natural to me.

I'm not sure if some of those should be overloaded into the EllipticCurve constructor (I would like that, because it's what I'm used to in magma. Constructors in sage seem to be very lenient in what they accept as input anyway)

The relevance for this report:

If the EllipticCurve constructor is going to be rather liberal in what it accepts for input, then I think people will expect it can take defining polynomials as well, and they won't expect an elliptic curve that happens to have a j-invariant equal to that polynomial as a return value.

I agree with John that EllipticCurve(<ring element>) should behave differently depending on the type of ring that is put in. Given that in most cases the j-invariant does -not- determine uniquely an elliptic curve over the ring the j-invariant lives in, I think that the section map of

<elliptic curves> -> <j-invariants>

should not be used as a valid default constructor for EllipticCurve. Instead have a function elliptic_curve_from_j_invariant, or some more palatable name. However, that's just my opinion. David Kohel's opinion would be interesting here as well.



---

archive/issue_comments_000580.json:
```json
{
    "body": "Sorry about yet another typo. I agree with John and hence think that EllipticCurve(<ring element>) should *NOT* behave differently based on the ring type. Would\n`EllipticCurve(j=1728)`\ndo the trick for people? Is it even acceptable to have a constructor that is happy with no unnamed parameters?",
    "created_at": "2008-04-14T23:21:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-580",
    "user": "nbruin"
}
```

Sorry about yet another typo. I agree with John and hence think that EllipticCurve(<ring element>) should *NOT* behave differently based on the ring type. Would
`EllipticCurve(j=1728)`
do the trick for people? Is it even acceptable to have a constructor that is happy with no unnamed parameters?



---

archive/issue_comments_000581.json:
```json
{
    "body": "Having thought about it, I now agree with Nils:   sine there is not a unique E.C. with given j-invariant, having a constructor of E from j -- which necessarily therefore makes an arbitray choice -- is not very sensible.\n\nSo we should instead have a function called something like EllipticCurve_from_j(j) which does the same as the current EllipticCurve(j), and this frees up a role for a 1-parameter constructor where the parameter is a polynomial.  But it still makes constructing a curve from a pair of polynomials problematical (since currently EllipticCurve(a,b) is the same as EllipticCurve([0,0,0,a,b]).\n\nNile is also quite right that in due course we should have a lot more ways of constructing E.C.s from other things.",
    "created_at": "2008-04-15T13:55:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-581",
    "user": "cremona"
}
```

Having thought about it, I now agree with Nils:   sine there is not a unique E.C. with given j-invariant, having a constructor of E from j -- which necessarily therefore makes an arbitray choice -- is not very sensible.

So we should instead have a function called something like EllipticCurve_from_j(j) which does the same as the current EllipticCurve(j), and this frees up a role for a 1-parameter constructor where the parameter is a polynomial.  But it still makes constructing a curve from a pair of polynomials problematical (since currently EllipticCurve(a,b) is the same as EllipticCurve([0,0,0,a,b]).

Nile is also quite right that in due course we should have a lot more ways of constructing E.C.s from other things.



---

archive/issue_comments_000582.json:
```json
{
    "body": "See the related #5673",
    "created_at": "2009-04-09T15:53:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-582",
    "user": "cremona"
}
```

See the related #5673



---

archive/issue_comments_000583.json:
```json
{
    "body": "I think this ticket should be closed. The issue is solved by #5673.",
    "created_at": "2009-04-21T15:20:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-583",
    "user": "wuthrich"
}
```

I think this ticket should be closed. The issue is solved by #5673.



---

archive/issue_comments_000584.json:
```json
{
    "body": "We still do not have a constructor from a monic cubic in one variable (or a cubic and a linear).  That would be quite easy, though it would have to have a new name (e.g. elliptic_curve_from_polynomials(f,g)) since otherwise it would conflict with other constructors using EllipticCurve().   \n\nSpeaking personally I would be happy to close this though!",
    "created_at": "2009-04-21T15:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-584",
    "user": "cremona"
}
```

We still do not have a constructor from a monic cubic in one variable (or a cubic and a linear).  That would be quite easy, though it would have to have a new name (e.g. elliptic_curve_from_polynomials(f,g)) since otherwise it would conflict with other constructors using EllipticCurve().   

Speaking personally I would be happy to close this though!



---

archive/issue_comments_000585.json:
```json
{
    "body": "Attachment [trac_128-ec-constructor.patch](tarball://root/attachments/some-uuid/ticket128/trac_128-ec-constructor.patch) by cremona created at 2009-12-13 22:59:11\n\nApplies to 4.3.rc0",
    "created_at": "2009-12-13T22:59:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-585",
    "user": "cremona"
}
```

Attachment [trac_128-ec-constructor.patch](tarball://root/attachments/some-uuid/ticket128/trac_128-ec-constructor.patch) by cremona created at 2009-12-13 22:59:11

Applies to 4.3.rc0



---

archive/issue_comments_000586.json:
```json
{
    "body": "Changing component from algebraic geometry to elliptic curves.",
    "created_at": "2009-12-13T23:02:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-586",
    "user": "cremona"
}
```

Changing component from algebraic geometry to elliptic curves.



---

archive/issue_comments_000587.json:
```json
{
    "body": "This ticket was opened 3 years ago and never settled.  I hope the attached patch will allow it to be put to rest.  Certainly there will be ways of tricking this (very flexible) constructor but everything that used to work still does, and there are now more ways of constructing Elliptic Curves!\n\nI hope that Nils and/or others will enjoy taking the opportunity to close a 3-digit ticket.",
    "created_at": "2009-12-13T23:02:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-587",
    "user": "cremona"
}
```

This ticket was opened 3 years ago and never settled.  I hope the attached patch will allow it to be put to rest.  Certainly there will be ways of tricking this (very flexible) constructor but everything that used to work still does, and there are now more ways of constructing Elliptic Curves!

I hope that Nils and/or others will enjoy taking the opportunity to close a 3-digit ticket.



---

archive/issue_comments_000588.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-13T23:02:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-588",
    "user": "cremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_000589.json:
```json
{
    "body": "The following behaviour is (sort of) documented, but is really painful:\n\n```\nsage: Q.<y,x>=QQ[]\nsage: EllipticCurve(y^2-x^3+1)\nNotImplementedError\nsage: EllipticCurve(x^3+1)\nNotImplementedError\n```\n\nbut:\n\n```\nsage: Q.<x,y>=QQ[]\nsage: EllipticCurve(y^2-x^3+1)\nElliptic Curve defined by y^2 = x^3 - 1 over Rational Field\nsage: EllipticCurve(x^3+1)\nElliptic Curve defined by y^2 = x^3 + 1 over Rational Field\n```\n\nI understand that the heart of this patch is not concerned with this behaviour, but the patch does change something about bivariate parents too (lines 280, 282). In particular, there seems to be code there concerned with swapping `x` and `y` so perhaps John could address this as well?\n\nIncidentally, `HyperellipticCurve(x^3+1)` in the above example simply does not work, because it insists on univariate polynomials. \n\nOther weird stuff:\n\n```\nsage: var(\"x,y,u,v\")\n(x, y, u, v)\nsage: EllipticCurve(y^2-x^3+1)\nElliptic Curve defined by y^2 = x^3 - 1 over Rational Field\nsage: EllipticCurve(v^2-u^3+1)\nTypeError\n```\n\nbut I guess that's what you get for using the symbolic ring.",
    "created_at": "2009-12-15T01:19:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-589",
    "user": "nbruin"
}
```

The following behaviour is (sort of) documented, but is really painful:

```
sage: Q.<y,x>=QQ[]
sage: EllipticCurve(y^2-x^3+1)
NotImplementedError
sage: EllipticCurve(x^3+1)
NotImplementedError
```

but:

```
sage: Q.<x,y>=QQ[]
sage: EllipticCurve(y^2-x^3+1)
Elliptic Curve defined by y^2 = x^3 - 1 over Rational Field
sage: EllipticCurve(x^3+1)
Elliptic Curve defined by y^2 = x^3 + 1 over Rational Field
```

I understand that the heart of this patch is not concerned with this behaviour, but the patch does change something about bivariate parents too (lines 280, 282). In particular, there seems to be code there concerned with swapping `x` and `y` so perhaps John could address this as well?

Incidentally, `HyperellipticCurve(x^3+1)` in the above example simply does not work, because it insists on univariate polynomials. 

Other weird stuff:

```
sage: var("x,y,u,v")
(x, y, u, v)
sage: EllipticCurve(y^2-x^3+1)
Elliptic Curve defined by y^2 = x^3 - 1 over Rational Field
sage: EllipticCurve(v^2-u^3+1)
TypeError
```

but I guess that's what you get for using the symbolic ring.



---

archive/issue_comments_000590.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-15T01:19:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-590",
    "user": "nbruin"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_000591.json:
```json
{
    "body": "Oh dear.  Well, this will not be a priority for me, so if anyone else would like to try then please do!  \n\nI guess we need to determine in a more general way how many variables there are, whatever their names.  As long as you don't want EllipticCurve(x<sup>2-(y</sup>3+1)) to be valid input....",
    "created_at": "2009-12-15T09:12:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-591",
    "user": "cremona"
}
```

Oh dear.  Well, this will not be a priority for me, so if anyone else would like to try then please do!  

I guess we need to determine in a more general way how many variables there are, whatever their names.  As long as you don't want EllipticCurve(x<sup>2-(y</sup>3+1)) to be valid input....



---

archive/issue_comments_000592.json:
```json
{
    "body": "I realised that when I looked at the code I noticed something that I think is really not a good idea:\n\n```\n        sage: R.<x,y> = QQ[] \n \tsage: EllipticCurve( x^3+1 ) \n \tElliptic Curve defined by y^2 = x^3 + 1 over Rational Field\n```\n\nIn this case, the variety defined by `x^3+1` has a very clear affine interpretation: 3 vertical lines. This is not an elliptic curve and should not be accepted as valid input. It was only later that I realized that it's this patch that introduces this use pattern. It shouldn't.",
    "created_at": "2010-02-09T19:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-592",
    "user": "nbruin"
}
```

I realised that when I looked at the code I noticed something that I think is really not a good idea:

```
        sage: R.<x,y> = QQ[] 
 	sage: EllipticCurve( x^3+1 ) 
 	Elliptic Curve defined by y^2 = x^3 + 1 over Rational Field
```

In this case, the variety defined by `x^3+1` has a very clear affine interpretation: 3 vertical lines. This is not an elliptic curve and should not be accepted as valid input. It was only later that I realized that it's this patch that introduces this use pattern. It shouldn't.



---

archive/issue_comments_000593.json:
```json
{
    "body": "I agree with, Nils!  Since you introduced the ticket in the first place, would you like to resolve as dontfix?  We have already changed things so that to construct a curve with given j-invariant you have to say \"j=...\"  explicitly.",
    "created_at": "2010-02-09T20:24:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-593",
    "user": "cremona"
}
```

I agree with, Nils!  Since you introduced the ticket in the first place, would you like to resolve as dontfix?  We have already changed things so that to construct a curve with given j-invariant you have to say "j=..."  explicitly.



---

archive/issue_comments_000594.json:
```json
{
    "body": "Cremona may be agreeing with me but I don't think I agree with him. The other example\n\n```\n        sage: R.<x> = QQ[] \n \tsage: EllipticCurve( x^3+1 ) \n \tElliptic Curve defined by y^2 = x^3 + 1 over Rational Field\n```\n\nmakes perfect sense to me and the present patch does fix that too. It matters whether a univariate or a bivariate polynomial gets put in. Perhaps this should go on another ticket, but a good start is here already and we'll never get such a nice ticket number (8192 is already gone).\n\nIt is nice to recognise when a bivariate polynomial obviously defines a weierstrass normal form, but then you may as well just look at general cubics with a rational flex.",
    "created_at": "2010-02-09T21:32:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-594",
    "user": "nbruin"
}
```

Cremona may be agreeing with me but I don't think I agree with him. The other example

```
        sage: R.<x> = QQ[] 
 	sage: EllipticCurve( x^3+1 ) 
 	Elliptic Curve defined by y^2 = x^3 + 1 over Rational Field
```

makes perfect sense to me and the present patch does fix that too. It matters whether a univariate or a bivariate polynomial gets put in. Perhaps this should go on another ticket, but a good start is here already and we'll never get such a nice ticket number (8192 is already gone).

It is nice to recognise when a bivariate polynomial obviously defines a weierstrass normal form, but then you may as well just look at general cubics with a rational flex.



---

archive/issue_comments_000595.json:
```json
{
    "body": "I advocate for a new ticket, since with current Sage `EllipticCurve(x^3-x)` reports a\ndeprecate warning, thus the description of this ticket is out of date.\n\nThe new ticket should clearly state which enhancements are wanted.\n\nPaul",
    "created_at": "2011-09-15T15:51:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-595",
    "user": "zimmerma"
}
```

I advocate for a new ticket, since with current Sage `EllipticCurve(x^3-x)` reports a
deprecate warning, thus the description of this ticket is out of date.

The new ticket should clearly state which enhancements are wanted.

Paul



---

archive/issue_comments_000596.json:
```json
{
    "body": "Yes, we might as well close it. By the time the deprecation has turned into an error for the current behaviour of\n`EllipticCurve(x^3+1)`\nwe can consider letting it produce the elliptic curve `y<sup>2=x</sup>3+1`.\nIncidentally, the call\n`EllipticCurve(x^3+1,x)`\nalready produces an error, so in principle this is available to produce `y<sup>2+x*y=x</sup>3+1`",
    "created_at": "2011-09-15T20:26:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-596",
    "user": "nbruin"
}
```

Yes, we might as well close it. By the time the deprecation has turned into an error for the current behaviour of
`EllipticCurve(x^3+1)`
we can consider letting it produce the elliptic curve `y<sup>2=x</sup>3+1`.
Incidentally, the call
`EllipticCurve(x^3+1,x)`
already produces an error, so in principle this is available to produce `y<sup>2+x*y=x</sup>3+1`



---

archive/issue_comments_000597.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-01-29T20:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-597",
    "user": "kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_000598.json:
```json
{
    "body": "So... please someone put as 'positive review', then.  I've filled in the reviewer blank :)",
    "created_at": "2013-01-29T20:28:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-598",
    "user": "kcrisman"
}
```

So... please someone put as 'positive review', then.  I've filled in the reviewer blank :)



---

archive/issue_comments_000599.json:
```json
{
    "body": "Any particular reason to delete me as author?  And have you checked that the 3-year-old patch still works?  And still gives some better behaviour, even if not perfect?",
    "created_at": "2013-01-30T09:06:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-599",
    "user": "cremona"
}
```

Any particular reason to delete me as author?  And have you checked that the 3-year-old patch still works?  And still gives some better behaviour, even if not perfect?



---

archive/issue_comments_000600.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-01-30T09:17:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-600",
    "user": "zimmerma"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_000601.json:
```json
{
    "body": "John, with Sage 5.6 we now get an error:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: R.<x>=QQ[]          \nsage: EllipticCurve(x^3+1)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n| Sage Version 5.6, Release Date: 2013-01-21                         |\n| Type \"notebook()\" for the browser-based notebook interface.        |\n| Type \"help()\" for help.                                            |\n/users/caramel/zimmerma/<ipython console> in <module>()\n\n/localdisk/tmp/sage-5.6/local/lib/python2.7/site-packages/sage/schemes/elliptic_curves/constructor.pyc in EllipticCurve(x, y, j, minimal_twist)\n    351 \n    352     if rings.is_RingElement(x) and y is None:\n--> 353         raise TypeError, \"invalid input to EllipticCurve constructor\"\n    354 \n    355     if not isinstance(x, (list, tuple)):\n\nTypeError: invalid input to EllipticCurve constructor\n```\n\nthus the original problem in the ticket description is solved. I thus propose to close that ticket, while leaving you as author.\n\nPaul",
    "created_at": "2013-01-30T09:17:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-601",
    "user": "zimmerma"
}
```

John, with Sage 5.6 we now get an error:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: R.<x>=QQ[]          
sage: EllipticCurve(x^3+1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 5.6, Release Date: 2013-01-21                         |
| Type "notebook()" for the browser-based notebook interface.        |
| Type "help()" for help.                                            |
/users/caramel/zimmerma/<ipython console> in <module>()

/localdisk/tmp/sage-5.6/local/lib/python2.7/site-packages/sage/schemes/elliptic_curves/constructor.pyc in EllipticCurve(x, y, j, minimal_twist)
    351 
    352     if rings.is_RingElement(x) and y is None:
--> 353         raise TypeError, "invalid input to EllipticCurve constructor"
    354 
    355     if not isinstance(x, (list, tuple)):

TypeError: invalid input to EllipticCurve constructor
```

thus the original problem in the ticket description is solved. I thus propose to close that ticket, while leaving you as author.

Paul



---

archive/issue_comments_000602.json:
```json
{
    "body": "That's fair enough -- so \"positive review\" is *not* appropriate, surely, as we want the ticket to be closed without the patch being applied?",
    "created_at": "2013-01-30T09:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-602",
    "user": "cremona"
}
```

That's fair enough -- so "positive review" is *not* appropriate, surely, as we want the ticket to be closed without the patch being applied?



---

archive/issue_comments_000603.json:
```json
{
    "body": "John, I understand I gave a \"positive review\" to the \"sage-duplicate/invalid/wontfix\" status,\nwhich implies of course the patch should not be applied.\n\nJeroen, how should we proceed?\n\nPaul",
    "created_at": "2013-01-30T09:37:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-603",
    "user": "zimmerma"
}
```

John, I understand I gave a "positive review" to the "sage-duplicate/invalid/wontfix" status,
which implies of course the patch should not be applied.

Jeroen, how should we proceed?

Paul



---

archive/issue_comments_000604.json:
```json
{
    "body": "> John, I understand I gave a \"positive review\" to the \"sage-duplicate/invalid/wontfix\" status,\n> which implies of course the patch should not be applied.\nCorrect.\n> Jeroen, how should we proceed?\nI'm sure he'll weigh in; I was just following his usual method for such cases, which was to remove the author(s) (since no patch was applied, so nothing was written) and to put the people who confirmed that we won't do it as reviewers.",
    "created_at": "2013-01-30T13:05:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-604",
    "user": "kcrisman"
}
```

> John, I understand I gave a "positive review" to the "sage-duplicate/invalid/wontfix" status,
> which implies of course the patch should not be applied.
Correct.
> Jeroen, how should we proceed?
I'm sure he'll weigh in; I was just following his usual method for such cases, which was to remove the author(s) (since no patch was applied, so nothing was written) and to put the people who confirmed that we won't do it as reviewers.



---

archive/issue_comments_000605.json:
```json
{
    "body": "Exactly.  Set the ticket to positive_review and milestone to sage-duplicate/invalid/wontfix.  That's it.",
    "created_at": "2013-01-30T13:07:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-605",
    "user": "jdemeyer"
}
```

Exactly.  Set the ticket to positive_review and milestone to sage-duplicate/invalid/wontfix.  That's it.



---

archive/issue_comments_000606.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-01-31T20:37:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/128#issuecomment-606",
    "user": "jdemeyer"
}
```

Resolution: worksforme
