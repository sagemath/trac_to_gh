# Issue 3416: Weierstrass form for cubics [with patch, with negative review]

archive/issues_003416.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @novoselt\n\nKeywords: nagell, weierstrass, cubic, elliptic curves\n\nThis code still needs a bit of polishing and testing, but it's nearly ready to go. I am marking this with a negative review since it's not quite release ready, but people can check it out.\n\nThis includes code for finding the transformation maps.\n\n-Bobby\n\nIssue created by migration from https://trac.sagemath.org/ticket/3416\n\n",
    "created_at": "2008-06-13T16:19:39Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.12",
    "title": "Weierstrass form for cubics [with patch, with negative review]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3416",
    "user": "https://github.com/bobmoretti"
}
```
Assignee: @williamstein

CC:  @novoselt

Keywords: nagell, weierstrass, cubic, elliptic curves

This code still needs a bit of polishing and testing, but it's nearly ready to go. I am marking this with a negative review since it's not quite release ready, but people can check it out.

This includes code for finding the transformation maps.

-Bobby

Issue created by migration from https://trac.sagemath.org/ticket/3416





---

archive/issue_comments_023901.json:
```json
{
    "body": "Attachment [weier.patch](tarball://root/attachments/some-uuid/ticket3416/weier.patch) by @wdjoyner created at 2008-06-13 17:04:27\n\nSince y^2 = quartic is also genus 1, I'm curious if there is a corresponding function planned to compute the Weierstrass form of a quartic hyperelliptic.",
    "created_at": "2008-06-13T17:04:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23901",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [weier.patch](tarball://root/attachments/some-uuid/ticket3416/weier.patch) by @wdjoyner created at 2008-06-13 17:04:27

Since y^2 = quartic is also genus 1, I'm curious if there is a corresponding function planned to compute the Weierstrass form of a quartic hyperelliptic.



---

archive/issue_comments_023902.json:
```json
{
    "body": "You can't give your own code a negative review :-).  I changed it to \"not ready for review\".",
    "created_at": "2008-06-13T22:21:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23902",
    "user": "https://github.com/williamstein"
}
```

You can't give your own code a negative review :-).  I changed it to "not ready for review".



---

archive/issue_comments_023903.json:
```json
{
    "body": "Changing keywords from \"nagell, weierstrass, cubic, elliptic curves\" to \"nagell, weierstrass, cubic, elliptic curves, editor_wstein\".",
    "created_at": "2008-06-20T05:04:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23903",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "nagell, weierstrass, cubic, elliptic curves" to "nagell, weierstrass, cubic, elliptic curves, editor_wstein".



---

archive/issue_comments_023904.json:
```json
{
    "body": "Attachment [Weierstrass.sage](tarball://root/attachments/some-uuid/ticket3416/Weierstrass.sage) by @syazdani77 created at 2009-04-30 22:06:58\n\nAlgorithm 7.4.10 of GTM 138",
    "created_at": "2009-04-30T22:06:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23904",
    "user": "https://github.com/syazdani77"
}
```

Attachment [Weierstrass.sage](tarball://root/attachments/some-uuid/ticket3416/Weierstrass.sage) by @syazdani77 created at 2009-04-30 22:06:58

Algorithm 7.4.10 of GTM 138



---

archive/issue_comments_023905.json:
```json
{
    "body": "I believe the formulas used here are incorrect. I'm not sure, but they appear similar to the erroneous formula's from Cohen's book. I'm currently working on an implementation that uses different formulas. I expect that to be done within two weeks.\n\nOne of my colleagues is working on y<sup>2</sup> = quartic, which I will implement for him. I expect this to be done within a couple of weeks. During Sage Days 23 plans were made for other curves too, but I'm not sure anyone is working on those.",
    "created_at": "2010-07-13T23:29:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23905",
    "user": "https://trac.sagemath.org/admin/accounts/users/Niels"
}
```

I believe the formulas used here are incorrect. I'm not sure, but they appear similar to the erroneous formula's from Cohen's book. I'm currently working on an implementation that uses different formulas. I expect that to be done within two weeks.

One of my colleagues is working on y<sup>2</sup> = quartic, which I will implement for him. I expect this to be done within a couple of weeks. During Sage Days 23 plans were made for other curves too, but I'm not sure anyone is working on those.



---

archive/issue_comments_023906.json:
```json
{
    "body": "Replying to [comment:5 Niels]:\n> I believe the formulas used here are incorrect. I'm not sure, but they appear similar to the erroneous formula's \n> from Cohen's book. I'm currently working on an implementation that uses different formulas.\n>  I expect that to be done within two weeks.\n\nYes, they are definitely the wrong formulas in Cohen's book.\n\n -- William",
    "created_at": "2010-07-13T23:32:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23906",
    "user": "https://github.com/williamstein"
}
```

Replying to [comment:5 Niels]:
> I believe the formulas used here are incorrect. I'm not sure, but they appear similar to the erroneous formula's 
> from Cohen's book. I'm currently working on an implementation that uses different formulas.
>  I expect that to be done within two weeks.

Yes, they are definitely the wrong formulas in Cohen's book.

 -- William



---

archive/issue_comments_023907.json:
```json
{
    "body": "Henri Cohen writes (2010-08-12):\n\n```\nConcerning the formulas for a general cubic in my first book, the situation is precisely the following:\n\n1) They were directly copied from an APECS script written by Ian Connell.\n\n2) The final Weirstrass equation is correct, as is the transformation from\nthe cubic coordinates to the Weierstrass ones. On the other hand, the reverse\ntransformation has a mistake, which I never took time to find, should be easy\n(it may be the other way round).\n\n3) This is in my errata sheets. In my more recent books, I indicate that there is indeed a\nmistake, and explain the algorithm (well-known of course), in less detail with no explicit\nformulas, so that a student should be able to reconstruct them.\n```\n\nThis suggests that very minor corrections are all that is required.",
    "created_at": "2010-08-13T09:03:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23907",
    "user": "https://github.com/JohnCremona"
}
```

Henri Cohen writes (2010-08-12):

```
Concerning the formulas for a general cubic in my first book, the situation is precisely the following:

1) They were directly copied from an APECS script written by Ian Connell.

2) The final Weirstrass equation is correct, as is the transformation from
the cubic coordinates to the Weierstrass ones. On the other hand, the reverse
transformation has a mistake, which I never took time to find, should be easy
(it may be the other way round).

3) This is in my errata sheets. In my more recent books, I indicate that there is indeed a
mistake, and explain the algorithm (well-known of course), in less detail with no explicit
formulas, so that a student should be able to reconstruct them.
```

This suggests that very minor corrections are all that is required.



---

archive/issue_comments_023908.json:
```json
{
    "body": "I have found that the descriptions in:\n\nCassels, J. W. S. Lectures on elliptic curves. London Mathematical Society Student Texts, 24. Cambridge University Press, Cambridge, 1991.\n\ngive excellent recipes for writing down isomorphisms from cubics, y!^2=quartic and intersections of two quadrics in P!^2 with a rational point to their Jacobians in weierstrass form.\n\nThe alternative method of writing down maps of degrees 3, 2, 4 (respectively) to their Jacobians using invariant theory (see Tom Fisher et al.) often results in nicer models, because there are less arbitrary choices to be made.",
    "created_at": "2010-08-13T23:29:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23908",
    "user": "https://github.com/nbruin"
}
```

I have found that the descriptions in:

Cassels, J. W. S. Lectures on elliptic curves. London Mathematical Society Student Texts, 24. Cambridge University Press, Cambridge, 1991.

give excellent recipes for writing down isomorphisms from cubics, y!^2=quartic and intersections of two quadrics in P!^2 with a rational point to their Jacobians in weierstrass form.

The alternative method of writing down maps of degrees 3, 2, 4 (respectively) to their Jacobians using invariant theory (see Tom Fisher et al.) often results in nicer models, because there are less arbitrary choices to be made.



---

archive/issue_comments_023909.json:
```json
{
    "body": "Replying to [comment:8 nbruin]:\n> I have found that the descriptions in:\n> \n> Cassels, J. W. S. Lectures on elliptic curves. London Mathematical Society Student Texts, 24. Cambridge University Press, Cambridge, 1991.\n> \n> give excellent recipes for writing down isomorphisms from cubics, y!^2=quartic and intersections of two quadrics in P!^2 with a rational point to their Jacobians in weierstrass form.\n> \n> The alternative method of writing down maps of degrees 3, 2, 4 (respectively) to their Jacobians using invariant theory (see Tom Fisher et al.) often results in nicer models, because there are less arbitrary choices to be made.\n\nSure, and it would be great to have all these genus one modes in Sage!\n\n(you can call me) al",
    "created_at": "2010-08-14T11:34:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23909",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:8 nbruin]:
> I have found that the descriptions in:
> 
> Cassels, J. W. S. Lectures on elliptic curves. London Mathematical Society Student Texts, 24. Cambridge University Press, Cambridge, 1991.
> 
> give excellent recipes for writing down isomorphisms from cubics, y!^2=quartic and intersections of two quadrics in P!^2 with a rational point to their Jacobians in weierstrass form.
> 
> The alternative method of writing down maps of degrees 3, 2, 4 (respectively) to their Jacobians using invariant theory (see Tom Fisher et al.) often results in nicer models, because there are less arbitrary choices to be made.

Sure, and it would be great to have all these genus one modes in Sage!

(you can call me) al



---

archive/issue_comments_023910.json:
```json
{
    "body": "Replying to [comment:8 nbruin]:\n> I have found that the descriptions in:\n> \n> Cassels, J. W. S. Lectures on elliptic curves. London Mathematical Society Student Texts, 24. Cambridge University Press, Cambridge, 1991.\n> \n> give excellent recipes for writing down isomorphisms from cubics, y!^2=quartic and intersections of two quadrics in P!^2 with a rational point to their Jacobians in weierstrass form.\n> \n> The alternative method of writing down maps of degrees 3, 2, 4 (respectively) to their Jacobians using invariant theory (see Tom Fisher et al.) often results in nicer models, because there are less arbitrary choices to be made.\n\n\nThanks for the advice. I will browse through the suggested literature to find the most convenient way of implementing cubic to Weierstrass. I plan to finish this before the end of August.\n\nIf I have more time I will try some quartics and see whether I can get the nicer formulas using J-invariants.",
    "created_at": "2010-08-15T09:22:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23910",
    "user": "https://trac.sagemath.org/admin/accounts/users/Niels"
}
```

Replying to [comment:8 nbruin]:
> I have found that the descriptions in:
> 
> Cassels, J. W. S. Lectures on elliptic curves. London Mathematical Society Student Texts, 24. Cambridge University Press, Cambridge, 1991.
> 
> give excellent recipes for writing down isomorphisms from cubics, y!^2=quartic and intersections of two quadrics in P!^2 with a rational point to their Jacobians in weierstrass form.
> 
> The alternative method of writing down maps of degrees 3, 2, 4 (respectively) to their Jacobians using invariant theory (see Tom Fisher et al.) often results in nicer models, because there are less arbitrary choices to be made.


Thanks for the advice. I will browse through the suggested literature to find the most convenient way of implementing cubic to Weierstrass. I plan to finish this before the end of August.

If I have more time I will try some quartics and see whether I can get the nicer formulas using J-invariants.



---

archive/issue_comments_023911.json:
```json
{
    "body": "Attachment [14532.patch](tarball://root/attachments/some-uuid/ticket3416/14532.patch) by Niels created at 2010-10-24 13:50:05",
    "created_at": "2010-10-24T13:50:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23911",
    "user": "https://trac.sagemath.org/admin/accounts/users/Niels"
}
```

Attachment [14532.patch](tarball://root/attachments/some-uuid/ticket3416/14532.patch) by Niels created at 2010-10-24 13:50:05



---

archive/issue_comments_023912.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-10-24T13:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23912",
    "user": "https://trac.sagemath.org/admin/accounts/users/Niels"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_023913.json:
```json
{
    "body": "Attachment [cnotes.pdf](tarball://root/attachments/some-uuid/ticket3416/cnotes.pdf) by Niels created at 2010-10-24 13:56:58\n\nHere is my first ever Sage patch: 14532.patch. It creates an elliptic curve from any homogeneous cubic. The cubic is transformed to Weierstrass, and birational maps between the equations are given. The case y<sup>2</sup> = quartic is not covered.\n\nThe patch is based upon Sage 4.4.4.\n\nThe used transformations are from Section 4.4 of the course notes: \"G1CRPC: Rational Points on Curves\", which I uploaded as cnotes.pdf.\n\nPlease review my patch, and provide extensive feedback.",
    "created_at": "2010-10-24T13:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23913",
    "user": "https://trac.sagemath.org/admin/accounts/users/Niels"
}
```

Attachment [cnotes.pdf](tarball://root/attachments/some-uuid/ticket3416/cnotes.pdf) by Niels created at 2010-10-24 13:56:58

Here is my first ever Sage patch: 14532.patch. It creates an elliptic curve from any homogeneous cubic. The cubic is transformed to Weierstrass, and birational maps between the equations are given. The case y<sup>2</sup> = quartic is not covered.

The patch is based upon Sage 4.4.4.

The used transformations are from Section 4.4 of the course notes: "G1CRPC: Rational Points on Curves", which I uploaded as cnotes.pdf.

Please review my patch, and provide extensive feedback.



---

archive/issue_comments_023914.json:
```json
{
    "body": "Just a couple of quick comments, as I have not yet had a chance to look at the patch properly or try it out.  First:  I'm not sure we really want my old lecture notes attached to this ticket!  There is nothing you are using there that is not in standard other sources.  But if they are there, they should be attributed ;)\n\nSecondly, you absolutely cannot have print statements giving part of the output as a side-effect.  Better to return a tuple consisting of the elliptic curve and the morphisms.  This will break backwards compatibility, since the Magma version does not so this (though he underlying Magma function surely does), but it could be controlled by an extra parameter which defaults to False.",
    "created_at": "2010-10-24T19:22:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23914",
    "user": "https://github.com/JohnCremona"
}
```

Just a couple of quick comments, as I have not yet had a chance to look at the patch properly or try it out.  First:  I'm not sure we really want my old lecture notes attached to this ticket!  There is nothing you are using there that is not in standard other sources.  But if they are there, they should be attributed ;)

Secondly, you absolutely cannot have print statements giving part of the output as a side-effect.  Better to return a tuple consisting of the elliptic curve and the morphisms.  This will break backwards compatibility, since the Magma version does not so this (though he underlying Magma function surely does), but it could be controlled by an extra parameter which defaults to False.



---

archive/issue_comments_023915.json:
```json
{
    "body": "Replying to [comment:13 cremona]:\n> I'm not sure we really want my old lecture notes attached to this ticket!  There is nothing you are using there that is not in standard other sources.  But if they are there, they should be attributed ;)\n\nThe problem is that most of the standard other sources contain incorrect formulas. These lecture notes are the first source I found with correct formulas. The main reason for including them is that it may help people in reviewing the patch. If anyone finds the same transformations in a standard source, please let me know.\n \n> Secondly, you absolutely cannot have print statements giving part of the output as a side-effect.  Better to return a tuple consisting of the elliptic curve and the morphisms.  This will break backwards compatibility, since the Magma version does not so this (though he underlying Magma function surely does), but it could be controlled by an extra parameter which defaults to False.\n\nOk, I can change that. Is there nice a way to represent such a morphism in Sage? I have difficulty expressing a transformation like the following as a single morphism (just an example from the top of my head):\n\nx -> x<sup>2</sup> - y\n\ny -> x<sup>2</sup> + y\n\nz -> z<sup>2</sup>\n\nThen multiply with 6/(x<sup>2</sup> z)",
    "created_at": "2010-10-25T06:53:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23915",
    "user": "https://trac.sagemath.org/admin/accounts/users/Niels"
}
```

Replying to [comment:13 cremona]:
> I'm not sure we really want my old lecture notes attached to this ticket!  There is nothing you are using there that is not in standard other sources.  But if they are there, they should be attributed ;)

The problem is that most of the standard other sources contain incorrect formulas. These lecture notes are the first source I found with correct formulas. The main reason for including them is that it may help people in reviewing the patch. If anyone finds the same transformations in a standard source, please let me know.
 
> Secondly, you absolutely cannot have print statements giving part of the output as a side-effect.  Better to return a tuple consisting of the elliptic curve and the morphisms.  This will break backwards compatibility, since the Magma version does not so this (though he underlying Magma function surely does), but it could be controlled by an extra parameter which defaults to False.

Ok, I can change that. Is there nice a way to represent such a morphism in Sage? I have difficulty expressing a transformation like the following as a single morphism (just an example from the top of my head):

x -> x<sup>2</sup> - y

y -> x<sup>2</sup> + y

z -> z<sup>2</sup>

Then multiply with 6/(x<sup>2</sup> z)



---

archive/issue_comments_023916.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-20T17:39:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23916",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_023917.json:
```json
{
    "body": "I tried to define the morphism properly, which should work, but it doesn't since in defining the morphism Sage checks that the polynomials used a homogeneous of the same degree (see line 458 of schemes.generic.morphism.py), but the degree function is not defined for elements of the coordinate ring.  This can be fixed:  although in general QuotientRingElement s have no degree, in this situation (where the quotient is by a homogeneous ideal) the degree is well-defined.",
    "created_at": "2010-11-20T17:39:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23917",
    "user": "https://github.com/JohnCremona"
}
```

I tried to define the morphism properly, which should work, but it doesn't since in defining the morphism Sage checks that the polynomials used a homogeneous of the same degree (see line 458 of schemes.generic.morphism.py), but the degree function is not defined for elements of the coordinate ring.  This can be fixed:  although in general QuotientRingElement s have no degree, in this situation (where the quotient is by a homogeneous ideal) the degree is well-defined.



---

archive/issue_comments_023918.json:
```json
{
    "body": "See #10297 for a separate report on this (and, soon, a patch).",
    "created_at": "2010-11-20T18:48:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23918",
    "user": "https://github.com/JohnCremona"
}
```

See #10297 for a separate report on this (and, soon, a patch).



---

archive/issue_comments_023919.json:
```json
{
    "body": "Replying to [comment:16 cremona]:\n> See #10297 for a separate report on this (and, soon, a patch).\n\nThe patch is there, so please review it!  The example I used there is one of the examples from the patch here.\n\nReplacing the curve E used there with\n\n```\n\nsage: E=EllipticCurve([0,0,0,0,-6400/3])\nsage: H=C.Hom(E)\nsage: f = H([zbar,xbar-ybar,-(xbar+ybar)/80])\nsage: f\nScheme morphism:\n  From: Projective Curve over Rational Field defined by x^3 + y^3 + 60*z^3\n  To:   Elliptic Curve defined by y^2 = x^3 - 6400/3 over Rational Field\n  Defn: Defined on coordinates by sending (x : y : z) to\n        (zbar : xbar - ybar : -1/80*xbar - 1/80*ybar)\n```\n\nsuccessfully defines the morphism.  I recommend that the function here just returns the morphism, since one can recover E from\n\n```\nsage: f.codomain()\nElliptic Curve defined by y^2 = x^3 - 6400/3 over Rational Field\n```\n\n\nThis will not be the end of the story, as I now cannot apply f to a point on C to get a point on E, but that's because of another difficulty like the one at #10297, so should be fixed separately.",
    "created_at": "2010-11-20T19:06:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23919",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:16 cremona]:
> See #10297 for a separate report on this (and, soon, a patch).

The patch is there, so please review it!  The example I used there is one of the examples from the patch here.

Replacing the curve E used there with

```

sage: E=EllipticCurve([0,0,0,0,-6400/3])
sage: H=C.Hom(E)
sage: f = H([zbar,xbar-ybar,-(xbar+ybar)/80])
sage: f
Scheme morphism:
  From: Projective Curve over Rational Field defined by x^3 + y^3 + 60*z^3
  To:   Elliptic Curve defined by y^2 = x^3 - 6400/3 over Rational Field
  Defn: Defined on coordinates by sending (x : y : z) to
        (zbar : xbar - ybar : -1/80*xbar - 1/80*ybar)
```

successfully defines the morphism.  I recommend that the function here just returns the morphism, since one can recover E from

```
sage: f.codomain()
Elliptic Curve defined by y^2 = x^3 - 6400/3 over Rational Field
```


This will not be the end of the story, as I now cannot apply f to a point on C to get a point on E, but that's because of another difficulty like the one at #10297, so should be fixed separately.



---

archive/issue_comments_023920.json:
```json
{
    "body": "Replying to [comment:17 cremona]:\n> Replying to [comment:16 cremona]:\n> > See #10297 for a separate report on this (and, soon, a patch).\n> \n> The patch is there, so please review it!  The example I used there is one of the examples from the patch here.\n> \n> Replacing the curve E used there with\n> {{{\n> \n> sage: E=EllipticCurve([0,0,0,0,-6400/3])\n> sage: H=C.Hom(E)\n> sage: f = H([zbar,xbar-ybar,-(xbar+ybar)/80])\n> sage: f\n> Scheme morphism:\n>   From: Projective Curve over Rational Field defined by x<sup>3</sup> + y<sup>3</sup> + 60*z<sup>3</sup>\n>   To:   Elliptic Curve defined by y<sup>2</sup> = x<sup>3</sup> - 6400/3 over Rational Field\n>   Defn: Defined on coordinates by sending (x : y : z) to\n>         (zbar : xbar - ybar : -1/80*xbar - 1/80*ybar)\n> }}}\n> successfully defines the morphism.  I recommend that the function here just returns the morphism, since one can recover E from\n> {{{\n> sage: f.codomain()\n> Elliptic Curve defined by y<sup>2</sup> = x<sup>3</sup> - 6400/3 over Rational Field\n> }}}\n> \n> This will not be the end of the story, as I now cannot apply f to a point on C to get a point on E, but that's because of another difficulty like the one at #10297, so should be fixed separately.\n\nThe example you give almost works. However, the map f sending (x : y : z) to (zbar : xbar - ybar : -1/80*xbar - 1/80*ybar) is the inverse of the map we are looking for. The map f is from the Elliptic Curve defined by y<sup>2</sup> = x<sup>3</sup> - 6400/3 to the Curve defined by x<sup>3</sup> + y<sup>3</sup> + 60*z<sup>3</sup>, not the other way around.\n\nI would like to include both the map f and its inverse f<sup>-1</sup> as (optional) output. Also, it would be nice to include the projective scaling necessary after the rational transformation. Unfortunately, the map f<sup>-1</sup> from \"x<sup>3</sup> + y<sup>3</sup> + 60*z<sup>3</sup>\" to \"y<sup>2</sup> - x<sup>3</sup> + 6400/3\" is not homogeneous:\n\nx -> 1/2*y - 40\n\ny -> -1/2*y - 40\n\nz -> x\n\nThen multiply the equation with 1/60.\n\nThe map f is homogeneous, but I'm not sure I can get a homogeneous f<sup>-1</sup> from there.\n\nI suggest that I include the morphisms as an optional tuple of strings. Does anyone have a better suggestion?",
    "created_at": "2011-03-28T14:55:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23920",
    "user": "https://trac.sagemath.org/admin/accounts/users/Niels"
}
```

Replying to [comment:17 cremona]:
> Replying to [comment:16 cremona]:
> > See #10297 for a separate report on this (and, soon, a patch).
> 
> The patch is there, so please review it!  The example I used there is one of the examples from the patch here.
> 
> Replacing the curve E used there with
> {{{
> 
> sage: E=EllipticCurve([0,0,0,0,-6400/3])
> sage: H=C.Hom(E)
> sage: f = H([zbar,xbar-ybar,-(xbar+ybar)/80])
> sage: f
> Scheme morphism:
>   From: Projective Curve over Rational Field defined by x<sup>3</sup> + y<sup>3</sup> + 60*z<sup>3</sup>
>   To:   Elliptic Curve defined by y<sup>2</sup> = x<sup>3</sup> - 6400/3 over Rational Field
>   Defn: Defined on coordinates by sending (x : y : z) to
>         (zbar : xbar - ybar : -1/80*xbar - 1/80*ybar)
> }}}
> successfully defines the morphism.  I recommend that the function here just returns the morphism, since one can recover E from
> {{{
> sage: f.codomain()
> Elliptic Curve defined by y<sup>2</sup> = x<sup>3</sup> - 6400/3 over Rational Field
> }}}
> 
> This will not be the end of the story, as I now cannot apply f to a point on C to get a point on E, but that's because of another difficulty like the one at #10297, so should be fixed separately.

The example you give almost works. However, the map f sending (x : y : z) to (zbar : xbar - ybar : -1/80*xbar - 1/80*ybar) is the inverse of the map we are looking for. The map f is from the Elliptic Curve defined by y<sup>2</sup> = x<sup>3</sup> - 6400/3 to the Curve defined by x<sup>3</sup> + y<sup>3</sup> + 60*z<sup>3</sup>, not the other way around.

I would like to include both the map f and its inverse f<sup>-1</sup> as (optional) output. Also, it would be nice to include the projective scaling necessary after the rational transformation. Unfortunately, the map f<sup>-1</sup> from "x<sup>3</sup> + y<sup>3</sup> + 60*z<sup>3</sup>" to "y<sup>2</sup> - x<sup>3</sup> + 6400/3" is not homogeneous:

x -> 1/2*y - 40

y -> -1/2*y - 40

z -> x

Then multiply the equation with 1/60.

The map f is homogeneous, but I'm not sure I can get a homogeneous f<sup>-1</sup> from there.

I suggest that I include the morphisms as an optional tuple of strings. Does anyone have a better suggestion?



---

archive/issue_comments_023921.json:
```json
{
    "body": "Attachment [trac_3416_elliptic_curve_from_cubic.patch](tarball://root/attachments/some-uuid/ticket3416/trac_3416_elliptic_curve_from_cubic.patch) by Niels created at 2011-04-26 08:09:53\n\npatch_2011_04_26",
    "created_at": "2011-04-26T08:09:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23921",
    "user": "https://trac.sagemath.org/admin/accounts/users/Niels"
}
```

Attachment [trac_3416_elliptic_curve_from_cubic.patch](tarball://root/attachments/some-uuid/ticket3416/trac_3416_elliptic_curve_from_cubic.patch) by Niels created at 2011-04-26 08:09:53

patch_2011_04_26



---

archive/issue_comments_023922.json:
```json
{
    "body": "I now have the morphisms as optional output, which defaults to False. The output uses print statements, because I still cannot find a better form for the general non-homogeneous morphisms. I tried using strings instead, but adding a polynomial to a string did not work.\n\nI hope this solution is okay for now. If anyone has a better suggestion for the representation, I will be happy to update my patch, or repatch it.",
    "created_at": "2011-04-26T08:17:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23922",
    "user": "https://trac.sagemath.org/admin/accounts/users/Niels"
}
```

I now have the morphisms as optional output, which defaults to False. The output uses print statements, because I still cannot find a better form for the general non-homogeneous morphisms. I tried using strings instead, but adding a polynomial to a string did not work.

I hope this solution is okay for now. If anyone has a better suggestion for the representation, I will be happy to update my patch, or repatch it.



---

archive/issue_comments_023923.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-04-26T08:17:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23923",
    "user": "https://trac.sagemath.org/admin/accounts/users/Niels"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_023924.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-04-27T08:34:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23924",
    "user": "https://trac.sagemath.org/admin/accounts/users/Niels"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_023925.json:
```json
{
    "body": "I am writing my own documentation about the transformation from cubic to Weierstrass. I will upload it within the next few days.\n\nI think I spotted a minor error in my patch. When P is not a flex, the program finds a second point P2 using the chord and tangent method. However, if P2 is a flex, I think the program will return an error. This is a simple fix, which will be up soon.",
    "created_at": "2011-04-27T08:34:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23925",
    "user": "https://trac.sagemath.org/admin/accounts/users/Niels"
}
```

I am writing my own documentation about the transformation from cubic to Weierstrass. I will upload it within the next few days.

I think I spotted a minor error in my patch. When P is not a flex, the program finds a second point P2 using the chord and tangent method. However, if P2 is a flex, I think the program will return an error. This is a simple fix, which will be up soon.



---

archive/issue_comments_023926.json:
```json
{
    "body": "Attachment [trac_3416_elliptic_curve_from_cubic2.patch](tarball://root/attachments/some-uuid/ticket3416/trac_3416_elliptic_curve_from_cubic2.patch) by Niels created at 2011-04-27 09:47:44\n\npatch_2011_04_27 with the fix for when P2 is a flex",
    "created_at": "2011-04-27T09:47:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23926",
    "user": "https://trac.sagemath.org/admin/accounts/users/Niels"
}
```

Attachment [trac_3416_elliptic_curve_from_cubic2.patch](tarball://root/attachments/some-uuid/ticket3416/trac_3416_elliptic_curve_from_cubic2.patch) by Niels created at 2011-04-27 09:47:44

patch_2011_04_27 with the fix for when P2 is a flex



---

archive/issue_comments_023927.json:
```json
{
    "body": "I'm sorry, I spotted another error when P2 is a flex. I'm fixing this today. I expect the new patch to be up today, and also the documentation. The documentation makes me confident that the new patch will be error-free.",
    "created_at": "2011-04-29T08:22:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23927",
    "user": "https://trac.sagemath.org/admin/accounts/users/Niels"
}
```

I'm sorry, I spotted another error when P2 is a flex. I'm fixing this today. I expect the new patch to be up today, and also the documentation. The documentation makes me confident that the new patch will be error-free.



---

archive/issue_comments_023928.json:
```json
{
    "body": "patch_2011_04_29 with additional fix",
    "created_at": "2011-04-29T09:42:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23928",
    "user": "https://trac.sagemath.org/admin/accounts/users/Niels"
}
```

patch_2011_04_29 with additional fix



---

archive/issue_comments_023929.json:
```json
{
    "body": "Attachment [trac_3416_elliptic_curve_from_cubic3.patch](tarball://root/attachments/some-uuid/ticket3416/trac_3416_elliptic_curve_from_cubic3.patch) by Niels created at 2011-04-29 10:41:38\n\nThe documentation is also up now. Comments on the documentation are welcome.\n\nPlease review my patch (trac_3416_elliptic_curve_from_cubic3.patch), and suggest any improvements it may need. The documentation describes how the patch works.",
    "created_at": "2011-04-29T10:41:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23929",
    "user": "https://trac.sagemath.org/admin/accounts/users/Niels"
}
```

Attachment [trac_3416_elliptic_curve_from_cubic3.patch](tarball://root/attachments/some-uuid/ticket3416/trac_3416_elliptic_curve_from_cubic3.patch) by Niels created at 2011-04-29 10:41:38

The documentation is also up now. Comments on the documentation are welcome.

Please review my patch (trac_3416_elliptic_curve_from_cubic3.patch), and suggest any improvements it may need. The documentation describes how the patch works.



---

archive/issue_comments_023930.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-04-29T10:41:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23930",
    "user": "https://trac.sagemath.org/admin/accounts/users/Niels"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_023931.json:
```json
{
    "body": "Documentation of patch3, including the source code - updated 2011_05_02",
    "created_at": "2011-05-02T20:25:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23931",
    "user": "https://trac.sagemath.org/admin/accounts/users/Niels"
}
```

Documentation of patch3, including the source code - updated 2011_05_02



---

archive/issue_comments_023932.json:
```json
{
    "body": "Changing component from number theory to elliptic curves.",
    "created_at": "2011-07-04T21:56:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23932",
    "user": "https://github.com/mstreng"
}
```

Changing component from number theory to elliptic curves.



---

archive/issue_comments_023933.json:
```json
{
    "body": "Attachment [cubic_to_weierstrass_documentation.pdf](tarball://root/attachments/some-uuid/ticket3416/cubic_to_weierstrass_documentation.pdf) by @mstreng created at 2011-07-04 21:56:20\n\nDid I understand correctly that one should apply trac_3416_elliptic_curve_from_cubic3.patch only?",
    "created_at": "2011-07-04T21:56:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23933",
    "user": "https://github.com/mstreng"
}
```

Attachment [cubic_to_weierstrass_documentation.pdf](tarball://root/attachments/some-uuid/ticket3416/cubic_to_weierstrass_documentation.pdf) by @mstreng created at 2011-07-04 21:56:20

Did I understand correctly that one should apply trac_3416_elliptic_curve_from_cubic3.patch only?



---

archive/issue_comments_023934.json:
```json
{
    "body": "Replying to [comment:23 mstreng]:\n> Did I understand correctly that one should apply trac_3416_elliptic_curve_from_cubic3.patch only?\n> \nYes, number 3 only, I guess I should have removed the other patches. Thanks for pointing this out.",
    "created_at": "2011-07-06T07:09:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23934",
    "user": "https://trac.sagemath.org/admin/accounts/users/Niels"
}
```

Replying to [comment:23 mstreng]:
> Did I understand correctly that one should apply trac_3416_elliptic_curve_from_cubic3.patch only?
> 
Yes, number 3 only, I guess I should have removed the other patches. Thanks for pointing this out.



---

archive/issue_comments_023935.json:
```json
{
    "body": "You can't remove patches (unless you have special rights on the trac server). But whenever you upload a patch, you can help reviewers and release managers by writting (preferably both in comments and in the ticket description) which patches to apply and in which order. If you follow a [certain syntax](http://wiki.sagemath.org/buildbot) in the comments, then an additional bonus is that your patches will get automatically tested by the buildbot.\n\nI almost gave you a negative review because of the following, but it seems that this is not something introduced by you, but just an error that was already there:\n\nThe documentation of `EllipticCurve_from_cubic` says that P should be a tuple, but the function only accepts lists (e.g. `[-1,0,1]`), not tuples (e.g. `(-1,0,1)`). Well, I guess I need to work harder for a review.",
    "created_at": "2011-07-06T09:28:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23935",
    "user": "https://github.com/mstreng"
}
```

You can't remove patches (unless you have special rights on the trac server). But whenever you upload a patch, you can help reviewers and release managers by writting (preferably both in comments and in the ticket description) which patches to apply and in which order. If you follow a [certain syntax](http://wiki.sagemath.org/buildbot) in the comments, then an additional bonus is that your patches will get automatically tested by the buildbot.

I almost gave you a negative review because of the following, but it seems that this is not something introduced by you, but just an error that was already there:

The documentation of `EllipticCurve_from_cubic` says that P should be a tuple, but the function only accepts lists (e.g. `[-1,0,1]`), not tuples (e.g. `(-1,0,1)`). Well, I guess I need to work harder for a review.



---

archive/issue_comments_023936.json:
```json
{
    "body": "\n```\nsage -t -long devel/sage/sage/schemes/elliptic_curves/constructor.py\n**********************************************************************\nError: TAB character found.\n```\n\nYou can't use TAB characters in python. Please replace it by the appropriate number of spaces. You can probably set up your editor so that it never uses TAB characters (and uses spaces instead).\n\nI'll read your code and give you a few suggestions for the next version.",
    "created_at": "2011-07-06T10:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23936",
    "user": "https://github.com/mstreng"
}
```


```
sage -t -long devel/sage/sage/schemes/elliptic_curves/constructor.py
**********************************************************************
Error: TAB character found.
```

You can't use TAB characters in python. Please replace it by the appropriate number of spaces. You can probably set up your editor so that it never uses TAB characters (and uses spaces instead).

I'll read your code and give you a few suggestions for the next version.



---

archive/issue_comments_023937.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-07-06T10:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23937",
    "user": "https://github.com/mstreng"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_023938.json:
```json
{
    "body": "Ok, here are some more comments, and a few cases where your code does not work:\n\nMost importantly: I don't like the output strings, I would definitely prefer actual `SchemeMorphism_on_points_projective_space` objects. This makes the method much more useful (as you can just evaluate these in points to transfer points between the curves). It also makes your patch much easier to review (as reviewers don't need to manually copy printed strings to test correctness of your output). I don't think this change is a lot of work: you can just feed your polynomials to E.hom, and you can find an example in the parametrization function [here](http://trac.sagemath.org/sage_trac/attachment/ticket/727/trac_727_conics_without_number_fields.patch). I'm afraid it would require accepting an actual plane projective curve as input `f` instead of a polynomial. For backwards compatibility, you can change polynomials into curves when you get them as input.\n\nAnyway, here are some comments on the code as it is:\n\nIf you stick with printing: in the description of the ``equivalence`` parameter: replace \"given\" by \"*printed*\" to make clear that it is only printed, not really given as a Sage object. The \"*\"'s around \"printed\" make it italic for emphasis.\n\nI would have called the \"equivalence\" parameter \"transformation\" instead.\n\nIn all your examples:\n\n```\nsage: var(\"x y z\")\n(x, y, z)\nsage: R.<x,y,z>=QQ[]\nsage: f=R(x^3+y^3+z^3)\n```\n\nThe second input overwrites the x, y, and z of the first input, so the first two lines (one input and one output) can (and hence should) be removed. Also, `x<sup>3+y</sup>3+z^3` is already in R, so remove \"R(\" and \")\".\n\nI don't understand the purpose of the \"Then multiply the equation with\". The three substitutions already give a map in projective space, right?\n\nYour function seems to require the variable names to be \"x,y,z\", this is not right:\n\n```\nsage: Q.<a,b,c>=QQ[]\nsage: EllipticCurve_from_cubic(a^3+b^3+60*c^3, [1,-1,0], equivalence=True)\n\u2026\nKeyError: 'y'\n```\n\n\nThere are cases that your code cannot handle:\n\n```\nsage: P.<x,y,z> = QQ[]\nsage: EllipticCurve_from_cubic(x^3+y^3+z^3, [-1,1,0])\nElliptic Curve defined by y^2 + 2*x*y + 1/3*y = x^3 - x^2 - 1/3*x - 1/27 over Rational Field\nsage: EllipticCurve_from_cubic(x^3+y^3+z^3, [-1,0,1])\n\u2026\nZeroDivisionError: \n```\n",
    "created_at": "2011-07-06T11:02:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23938",
    "user": "https://github.com/mstreng"
}
```

Ok, here are some more comments, and a few cases where your code does not work:

Most importantly: I don't like the output strings, I would definitely prefer actual `SchemeMorphism_on_points_projective_space` objects. This makes the method much more useful (as you can just evaluate these in points to transfer points between the curves). It also makes your patch much easier to review (as reviewers don't need to manually copy printed strings to test correctness of your output). I don't think this change is a lot of work: you can just feed your polynomials to E.hom, and you can find an example in the parametrization function [here](http://trac.sagemath.org/sage_trac/attachment/ticket/727/trac_727_conics_without_number_fields.patch). I'm afraid it would require accepting an actual plane projective curve as input `f` instead of a polynomial. For backwards compatibility, you can change polynomials into curves when you get them as input.

Anyway, here are some comments on the code as it is:

If you stick with printing: in the description of the ``equivalence`` parameter: replace "given" by "*printed*" to make clear that it is only printed, not really given as a Sage object. The "*"'s around "printed" make it italic for emphasis.

I would have called the "equivalence" parameter "transformation" instead.

In all your examples:

```
sage: var("x y z")
(x, y, z)
sage: R.<x,y,z>=QQ[]
sage: f=R(x^3+y^3+z^3)
```

The second input overwrites the x, y, and z of the first input, so the first two lines (one input and one output) can (and hence should) be removed. Also, `x<sup>3+y</sup>3+z^3` is already in R, so remove "R(" and ")".

I don't understand the purpose of the "Then multiply the equation with". The three substitutions already give a map in projective space, right?

Your function seems to require the variable names to be "x,y,z", this is not right:

```
sage: Q.<a,b,c>=QQ[]
sage: EllipticCurve_from_cubic(a^3+b^3+60*c^3, [1,-1,0], equivalence=True)
…
KeyError: 'y'
```


There are cases that your code cannot handle:

```
sage: P.<x,y,z> = QQ[]
sage: EllipticCurve_from_cubic(x^3+y^3+z^3, [-1,1,0])
Elliptic Curve defined by y^2 + 2*x*y + 1/3*y = x^3 - x^2 - 1/3*x - 1/27 over Rational Field
sage: EllipticCurve_from_cubic(x^3+y^3+z^3, [-1,0,1])
…
ZeroDivisionError: 
```




---

archive/issue_comments_023939.json:
```json
{
    "body": "Replying to [comment:25 mstreng]:\n> I almost gave you a negative review because of the following, but it seems that this is not something introduced by you, but just an error that was already there:\n> \n> The documentation of `EllipticCurve_from_cubic` says that P should be a tuple, but the function only accepts lists (e.g. `[-1,0,1]`), not tuples (e.g. `(-1,0,1)`). Well, I guess I need to work harder for a review.\n\nNever mind this comment: it does accept tuples, it just does not accept `(-1,0,1)`, only `(-1,1,0)`.",
    "created_at": "2011-07-06T11:04:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23939",
    "user": "https://github.com/mstreng"
}
```

Replying to [comment:25 mstreng]:
> I almost gave you a negative review because of the following, but it seems that this is not something introduced by you, but just an error that was already there:
> 
> The documentation of `EllipticCurve_from_cubic` says that P should be a tuple, but the function only accepts lists (e.g. `[-1,0,1]`), not tuples (e.g. `(-1,0,1)`). Well, I guess I need to work harder for a review.

Never mind this comment: it does accept tuples, it just does not accept `(-1,0,1)`, only `(-1,1,0)`.



---

archive/issue_comments_023940.json:
```json
{
    "body": "ps. `are_projectively_equivalent` needs documentation including tests. Even though it is not available to the user, it must make sense to developers who want to edit your code.",
    "created_at": "2011-07-06T11:16:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23940",
    "user": "https://github.com/mstreng"
}
```

ps. `are_projectively_equivalent` needs documentation including tests. Even though it is not available to the user, it must make sense to developers who want to edit your code.



---

archive/issue_comments_023941.json:
```json
{
    "body": "I very strongly agree that outputting the map as strings is not acceptable, and makes using this output impossible.  I said as much in an earlier review, and the response was that the author could not work out how to return maps.\n\nIn a spirit of cooperation and so that this can eventually be finished, let's try to carry out Marco's suggestion to construct a hom properly.  I seem to remember that when I tried this last it failed for some rather silly reason, but we really should be able to get this to work!",
    "created_at": "2011-07-06T11:26:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23941",
    "user": "https://github.com/JohnCremona"
}
```

I very strongly agree that outputting the map as strings is not acceptable, and makes using this output impossible.  I said as much in an earlier review, and the response was that the author could not work out how to return maps.

In a spirit of cooperation and so that this can eventually be finished, let's try to carry out Marco's suggestion to construct a hom properly.  I seem to remember that when I tried this last it failed for some rather silly reason, but we really should be able to get this to work!



---

archive/issue_comments_023942.json:
```json
{
    "body": "Nice work! Haven't tested it, but I did scan over the patch. Some remarks:\n\n- Your examples are misleading. You call `var(\"x y z\")` and then construct a polynomial ring. The call to `var` is irrelevant and should be removed.\n\n- Line 578. Why don't you take R=parent(F)? In fact, why do you define R at all? I don't think you use it.\n\n- Line 587. Don't use chord-tangent to determine if a point is a flex, but see if the hessian (determinant of the matrix of double derivatives of F) vanishes at P. That allows you to get rid of \"chord_and_tangent\" and of \"are_projectively_equivalent\" (for which you should a library routine instead of writing your own, if you really need it elsewhere. Sage's projective spaces and their points should be able to do this for you.\n\nFor the interfacing with magma:\n\nI think you can be a little more elegant here. Consider the following example\n\n```\nR.<x,y,z>=QQ[]\nf=x^3+y^3+z^3\nP=(0,1,-1)\n```\n\nYou can now do (and this should apply generally):\n\n```\nP2_magma=f.parent().magma().Proj()\nC_magma=P2.Curve(f)\nE_magma,mp_magma=C.EllipticCurve(C_magma(P),nvals=Integer(2))\nE_magma.aInvariants().sage()\n```\n\nTo extract the map, one would hope to be able to do\n\n```\nmp.DefiningPolynomials().sage()\n```\n\nand the fact that this fails is not really the fault of the code here. The proper solution would be to extend the coercion system to the magma interface, but that doesn't sound very appealing.\n\nIn any case, I don't think you should be hard-coding the Rationals as a base ring here and you should not be calling MinimalModel either, because you don't do that in the sage version.\n\n---------------------------------------------------------\n\nFinally, for the transformation: Yes, return a morphism or failing that, a list of 3 homogeneous polynomials in the parent of F that would be the appropriate input for the \"hom\" constructor.\n\nIf you are implementing your algorithm \"bare bones\" (internally, you just work with polynomials and you don't use any of the scheme machinery and your input consists of a homogeneous poly rather than a plane curve) there could be some value of also making your output available \"bare bones\", i.e., just return the list [a1,a2,a3,a4,a6] and a list of polynomials describing the map.\n\nThere is a cost to using schemes, ambient spaces etc., so there may be a benefit in having the raw functionality available in a form that avoids it. Once you have a routine that does the heavy lifting, it's straightforward to write a wrapper that provides an interface in scheme language.\n\n(there is also a benefit in using scheme language, so if you choose to write your code in terms of such higher level constructs, it makes little sense to wrap it to provide a \"raw\" interface as well)",
    "created_at": "2011-07-06T17:13:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23942",
    "user": "https://github.com/nbruin"
}
```

Nice work! Haven't tested it, but I did scan over the patch. Some remarks:

- Your examples are misleading. You call `var("x y z")` and then construct a polynomial ring. The call to `var` is irrelevant and should be removed.

- Line 578. Why don't you take R=parent(F)? In fact, why do you define R at all? I don't think you use it.

- Line 587. Don't use chord-tangent to determine if a point is a flex, but see if the hessian (determinant of the matrix of double derivatives of F) vanishes at P. That allows you to get rid of "chord_and_tangent" and of "are_projectively_equivalent" (for which you should a library routine instead of writing your own, if you really need it elsewhere. Sage's projective spaces and their points should be able to do this for you.

For the interfacing with magma:

I think you can be a little more elegant here. Consider the following example

```
R.<x,y,z>=QQ[]
f=x^3+y^3+z^3
P=(0,1,-1)
```

You can now do (and this should apply generally):

```
P2_magma=f.parent().magma().Proj()
C_magma=P2.Curve(f)
E_magma,mp_magma=C.EllipticCurve(C_magma(P),nvals=Integer(2))
E_magma.aInvariants().sage()
```

To extract the map, one would hope to be able to do

```
mp.DefiningPolynomials().sage()
```

and the fact that this fails is not really the fault of the code here. The proper solution would be to extend the coercion system to the magma interface, but that doesn't sound very appealing.

In any case, I don't think you should be hard-coding the Rationals as a base ring here and you should not be calling MinimalModel either, because you don't do that in the sage version.

---------------------------------------------------------

Finally, for the transformation: Yes, return a morphism or failing that, a list of 3 homogeneous polynomials in the parent of F that would be the appropriate input for the "hom" constructor.

If you are implementing your algorithm "bare bones" (internally, you just work with polynomials and you don't use any of the scheme machinery and your input consists of a homogeneous poly rather than a plane curve) there could be some value of also making your output available "bare bones", i.e., just return the list [a1,a2,a3,a4,a6] and a list of polynomials describing the map.

There is a cost to using schemes, ambient spaces etc., so there may be a benefit in having the raw functionality available in a form that avoids it. Once you have a routine that does the heavy lifting, it's straightforward to write a wrapper that provides an interface in scheme language.

(there is also a benefit in using scheme language, so if you choose to write your code in terms of such higher level constructs, it makes little sense to wrap it to provide a "raw" interface as well)



---

archive/issue_comments_023943.json:
```json
{
    "body": "Replying to [comment:31 nbruin]:\n> If you are implementing your algorithm \"bare bones\" (internally, you just work with polynomials and you don't use any of the scheme machinery and your input consists of a homogeneous poly rather than a plane curve) there could be some value of also making your output available \"bare bones\", i.e., just return the list [a1,a2,a3,a4,a6] and a list of polynomials describing the map.\n> \n> There is a cost to using schemes, ambient spaces etc., so there may be a benefit in having the raw functionality available in a form that avoids it. Once you have a routine that does the heavy lifting, it's straightforward to write a wrapper that provides an interface in scheme language.\n\nI like this idea. So Niels's code could simply output three lists: the [a1,a2,a3,a4,a6] and 2 lists of 3 polynomials each. Outputting instead of printing should be an easy enough change.\n\nAnd then a new member function of `ProjectiveCurve_generic` could call it (or an analogous \"`y^2`=quartic\" function) and convert the output to an `EllipticCurve...` and two `SchemeMorphism...` objects.",
    "created_at": "2011-07-06T17:44:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23943",
    "user": "https://github.com/mstreng"
}
```

Replying to [comment:31 nbruin]:
> If you are implementing your algorithm "bare bones" (internally, you just work with polynomials and you don't use any of the scheme machinery and your input consists of a homogeneous poly rather than a plane curve) there could be some value of also making your output available "bare bones", i.e., just return the list [a1,a2,a3,a4,a6] and a list of polynomials describing the map.
> 
> There is a cost to using schemes, ambient spaces etc., so there may be a benefit in having the raw functionality available in a form that avoids it. Once you have a routine that does the heavy lifting, it's straightforward to write a wrapper that provides an interface in scheme language.

I like this idea. So Niels's code could simply output three lists: the [a1,a2,a3,a4,a6] and 2 lists of 3 polynomials each. Outputting instead of printing should be an easy enough change.

And then a new member function of `ProjectiveCurve_generic` could call it (or an analogous "`y^2`=quartic" function) and convert the output to an `EllipticCurve...` and two `SchemeMorphism...` objects.



---

archive/issue_comments_023944.json:
```json
{
    "body": "Replying to [comment:32 mstreng]:\n> And then a new member function of `ProjectiveCurve_generic` could call it (or an analogous \"`y^2`=quartic\" function) and convert the output to an `EllipticCurve...` and two `SchemeMorphism...` objects.\n\n(ps. this part is for a later ticket, of course)",
    "created_at": "2011-07-06T18:02:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23944",
    "user": "https://github.com/mstreng"
}
```

Replying to [comment:32 mstreng]:
> And then a new member function of `ProjectiveCurve_generic` could call it (or an analogous "`y^2`=quartic" function) and convert the output to an `EllipticCurve...` and two `SchemeMorphism...` objects.

(ps. this part is for a later ticket, of course)



---

archive/issue_comments_023945.json:
```json
{
    "body": "Thank you all for the comments. I will have another go at making this patch work.",
    "created_at": "2011-07-06T19:27:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23945",
    "user": "https://trac.sagemath.org/admin/accounts/users/Niels"
}
```

Thank you all for the comments. I will have another go at making this patch work.



---

archive/issue_comments_023946.json:
```json
{
    "body": "This has arisen once again on sage-nt: is anyone interested in making this work at last?",
    "created_at": "2012-12-02T12:11:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23946",
    "user": "https://github.com/JohnCremona"
}
```

This has arisen once again on sage-nt: is anyone interested in making this work at last?



---

archive/issue_comments_023947.json:
```json
{
    "body": "There is also the pointless version #13084, #13458. The way I see it, it has the advantage that you don't have to specify a point to get the Weierstrass form. The price to pay is that you don't get an explicit isomorphism with the Weierstrass cubic.\n\nActually, the Magma `aInvariants` function that the current code calls\n\n```\n    cmd = 'aInvariants(MinimalModel(EllipticCurve(Curve(Scheme(P, %s)),P!%s)));'%(F, P) \n    s = magma.eval(cmd) \n    return EllipticCurve(rings.RationalField(), eval(s)) \n```\n\nimplements the same algorithm as #13084, see http://magma.maths.usyd.edu.au/magma/handbook/text/1379. Which is why it doesn't return a morphism. \n\nI'm not entirely sure how to merge the two approaches but it seems that you should only require a point if you actually need the isomorphism to the Weierstrass model.",
    "created_at": "2012-12-02T14:00:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23947",
    "user": "https://github.com/vbraun"
}
```

There is also the pointless version #13084, #13458. The way I see it, it has the advantage that you don't have to specify a point to get the Weierstrass form. The price to pay is that you don't get an explicit isomorphism with the Weierstrass cubic.

Actually, the Magma `aInvariants` function that the current code calls

```
    cmd = 'aInvariants(MinimalModel(EllipticCurve(Curve(Scheme(P, %s)),P!%s)));'%(F, P) 
    s = magma.eval(cmd) 
    return EllipticCurve(rings.RationalField(), eval(s)) 
```

implements the same algorithm as #13084, see http://magma.maths.usyd.edu.au/magma/handbook/text/1379. Which is why it doesn't return a morphism. 

I'm not entirely sure how to merge the two approaches but it seems that you should only require a point if you actually need the isomorphism to the Weierstrass model.



---

archive/issue_comments_023948.json:
```json
{
    "body": "Sure --without any points you can easily write down a W. equation for the Jacobian of the plane cubic.  Even if the cubic has no rational points, such as the famous `3x<sup>3+4y</sup>3+5z^3=0`.  But that is not usual what people want, and should have a different name (such as \"Jacobian\").",
    "created_at": "2012-12-02T14:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23948",
    "user": "https://github.com/JohnCremona"
}
```

Sure --without any points you can easily write down a W. equation for the Jacobian of the plane cubic.  Even if the cubic has no rational points, such as the famous `3x<sup>3+4y</sup>3+5z^3=0`.  But that is not usual what people want, and should have a different name (such as "Jacobian").



---

archive/issue_comments_023949.json:
```json
{
    "body": "And what is done by Maple in\nhttp://www.maplesoft.com/support/help/Maple/view.aspx?path=algcurves/Weierstrassform\n?\n\nIt does return the maps in both directions without using any points.",
    "created_at": "2012-12-02T15:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23949",
    "user": "https://github.com/novoselt"
}
```

And what is done by Maple in
http://www.maplesoft.com/support/help/Maple/view.aspx?path=algcurves/Weierstrassform
?

It does return the maps in both directions without using any points.



---

archive/issue_comments_023950.json:
```json
{
    "body": "Replying to [comment:38 novoselt]:\n> And what is done by Maple in\n> http://www.maplesoft.com/support/help/Maple/view.aspx?path=algcurves/Weierstrassform\n> ?\n> \n> It does return the maps in both directions without using any points.\n\nI have no idea.  The definition there is wrong:  an elliptic curve is not just a genus 1 curve, it is a genus one curve with a specified point.  Perhaps Maple tries to find a point (it does say that the function can be speeded up by providing one), and perhaps if there is no rational point it uses something generic, or a point defined over an extension.  Without a notion of field of definition, you could do anything.   Note that Magma's function does not require a point to be specified;  if none is given it tries to find one, uses it if it finds one and otherwise raises a run-time error.\n\nSomeone with Maple could try the Selmer curve (of my previous post) to see what it does.",
    "created_at": "2012-12-02T15:44:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23950",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:38 novoselt]:
> And what is done by Maple in
> http://www.maplesoft.com/support/help/Maple/view.aspx?path=algcurves/Weierstrassform
> ?
> 
> It does return the maps in both directions without using any points.

I have no idea.  The definition there is wrong:  an elliptic curve is not just a genus 1 curve, it is a genus one curve with a specified point.  Perhaps Maple tries to find a point (it does say that the function can be speeded up by providing one), and perhaps if there is no rational point it uses something generic, or a point defined over an extension.  Without a notion of field of definition, you could do anything.   Note that Magma's function does not require a point to be specified;  if none is given it tries to find one, uses it if it finds one and otherwise raises a run-time error.

Someone with Maple could try the Selmer curve (of my previous post) to see what it does.



---

archive/issue_comments_023951.json:
```json
{
    "body": "I think Maple does the same as #13458: it returns a rational multi-covering. This you can also get without a point.\n\nCurrently I don't like the way the transformation is returned in this ticket. A bunch of text, really? Can't we return concatenated maps or something that can be accessed programmatically? Or, failing that, a custom python object that can be queried for the defining polynomials.\n\nThe good news is that we seem to have all relevant algorithms implemented, we just need to settle on an interface. My suggestion would be\n\nA constructor function EllipticCurve_from_curve(equation, point=None, proof=False)\nIf proof=False then just the Weierstrass form is returned using whatever algorithm is fastest (probably ignoring the given point).\nIf proof=True and no point is given, a pair (E,f) of elliptic curve and rational covering map from the curve to the Weierstrass form is returned.\nIf proof=True and a point is given, then a pair (E,f) is returned such that f is an isomorphism.\nMake EllipticCurve_from_cubic an alias for EllipticCurve_from_curve. The latter will also handle e.g. y^2=quartic(x) e.g., so it shouldn't mention cubic.",
    "created_at": "2012-12-02T15:45:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23951",
    "user": "https://github.com/vbraun"
}
```

I think Maple does the same as #13458: it returns a rational multi-covering. This you can also get without a point.

Currently I don't like the way the transformation is returned in this ticket. A bunch of text, really? Can't we return concatenated maps or something that can be accessed programmatically? Or, failing that, a custom python object that can be queried for the defining polynomials.

The good news is that we seem to have all relevant algorithms implemented, we just need to settle on an interface. My suggestion would be

A constructor function EllipticCurve_from_curve(equation, point=None, proof=False)
If proof=False then just the Weierstrass form is returned using whatever algorithm is fastest (probably ignoring the given point).
If proof=True and no point is given, a pair (E,f) of elliptic curve and rational covering map from the curve to the Weierstrass form is returned.
If proof=True and a point is given, then a pair (E,f) is returned such that f is an isomorphism.
Make EllipticCurve_from_cubic an alias for EllipticCurve_from_curve. The latter will also handle e.g. y^2=quartic(x) e.g., so it shouldn't mention cubic.



---

archive/issue_comments_023952.json:
```json
{
    "body": "Does anybody have an objection to my suggestion of implementing a constructor function `EllipticCurve_from_curve(equation, point=None, proof=False)`, or perhaps `certificate=False`, that by default returns the Weierstrass form of the Jacobian and otherwise a morphism? I can work over this ticket but it would be nice if we can agree on the interface first.",
    "created_at": "2013-02-12T11:57:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23952",
    "user": "https://github.com/vbraun"
}
```

Does anybody have an objection to my suggestion of implementing a constructor function `EllipticCurve_from_curve(equation, point=None, proof=False)`, or perhaps `certificate=False`, that by default returns the Weierstrass form of the Jacobian and otherwise a morphism? I can work over this ticket but it would be nice if we can agree on the interface first.



---

archive/issue_comments_023953.json:
```json
{
    "body": "Replying to [comment:41 vbraun]:\n> Does anybody have an objection to my suggestion\n\nNo objection, but a few comments:\n\n* Don't call it \"proof\", since your proposal always gives provenly correct output. I'm not a fan of \"certificate\" either. How about \"morphism\" or \"morphisms\"?\n* In the case of an isomorphism, could you also return its inverse?\n* When a point is provided, I would prefer the default to be to output the isomorphisms too, as most applications will need them.\n\nAnyway, thanks for picking this up again!",
    "created_at": "2013-02-12T12:09:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23953",
    "user": "https://github.com/mstreng"
}
```

Replying to [comment:41 vbraun]:
> Does anybody have an objection to my suggestion

No objection, but a few comments:

* Don't call it "proof", since your proposal always gives provenly correct output. I'm not a fan of "certificate" either. How about "morphism" or "morphisms"?
* In the case of an isomorphism, could you also return its inverse?
* When a point is provided, I would prefer the default to be to output the isomorphisms too, as most applications will need them.

Anyway, thanks for picking this up again!



---

archive/issue_comments_023954.json:
```json
{
    "body": "Thanks from me too.  Is the plan as follows:  input is a smooth plane cubic, possibly with a rational point.  If there is a point given then the output includes a Weierstrass model birational to the input curve, in fact  isomorphic to it, with a linear projective change of coordinates if the point was a flex and a more complicated (quadratic) map on `P^2` inducing the isomorphism otherwise;  while if there is no point given then the curve returned is the Jacobian.  In the latter case one could also return a map from the input curve to the Jacobian, namely the associated 3-covering map of degree 9.  And no attempt is made to find rational points if none are given.\n\nThat seems reasonable to me, provided that the documentation makes it clear how different the output will be in the two cases (point supplied or not).",
    "created_at": "2013-02-12T12:42:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23954",
    "user": "https://github.com/JohnCremona"
}
```

Thanks from me too.  Is the plan as follows:  input is a smooth plane cubic, possibly with a rational point.  If there is a point given then the output includes a Weierstrass model birational to the input curve, in fact  isomorphic to it, with a linear projective change of coordinates if the point was a flex and a more complicated (quadratic) map on `P^2` inducing the isomorphism otherwise;  while if there is no point given then the curve returned is the Jacobian.  In the latter case one could also return a map from the input curve to the Jacobian, namely the associated 3-covering map of degree 9.  And no attempt is made to find rational points if none are given.

That seems reasonable to me, provided that the documentation makes it clear how different the output will be in the two cases (point supplied or not).



---

archive/issue_comments_023955.json:
```json
{
    "body": "Replying to [comment:43 cremona]:\n> If there is a point given then the output includes a Weierstrass model birational to the input curve, in fact  isomorphic to it\n[...]\n> In the latter case one could also return a map from the input curve to the Jacobian, namely the associated 3-covering map of degree 9.  And no attempt is made to find rational points if none are given.\n\nSince the two cases are distinct (in one case the cubic is birational over the base field to the returned curve, in the other case not necessarily) I think we cannot treat those cases silently as the same. At the very least it needs an option. I would prefer a different routine for the latter. `Jacobian` comes to mind.",
    "created_at": "2013-02-12T18:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23955",
    "user": "https://github.com/nbruin"
}
```

Replying to [comment:43 cremona]:
> If there is a point given then the output includes a Weierstrass model birational to the input curve, in fact  isomorphic to it
[...]
> In the latter case one could also return a map from the input curve to the Jacobian, namely the associated 3-covering map of degree 9.  And no attempt is made to find rational points if none are given.

Since the two cases are distinct (in one case the cubic is birational over the base field to the returned curve, in the other case not necessarily) I think we cannot treat those cases silently as the same. At the very least it needs an option. I would prefer a different routine for the latter. `Jacobian` comes to mind.



---

archive/issue_comments_023956.json:
```json
{
    "body": "So how about\n\n```\ndef EllipticCurve_from_cubic_and_point(F, P, morphism=False):\n   ...\n\ndef EllipticCurve_from_Jacobian(F, morphism=False):\n   ...\n```\n",
    "created_at": "2013-02-12T19:34:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23956",
    "user": "https://github.com/vbraun"
}
```

So how about

```
def EllipticCurve_from_cubic_and_point(F, P, morphism=False):
   ...

def EllipticCurve_from_Jacobian(F, morphism=False):
   ...
```




---

archive/issue_comments_023957.json:
```json
{
    "body": "Replying to [comment:45 vbraun]:\n> So how about\n> {{{\n> def EllipticCurve_from_cubic_and_point(F, P, morphism=False):\n>    ...\n> \n> def EllipticCurve_from_Jacobian(F, morphism=False):\n>    ...\n> }}}\nThe latter is not right -- it's the Jacobian elliptic curve which is returned!  We could call it just Jacobian() and raise a NotImplemented error if the genus is >1?\n\nThe first is fine though rather long.",
    "created_at": "2013-02-12T19:44:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23957",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:45 vbraun]:
> So how about
> {{{
> def EllipticCurve_from_cubic_and_point(F, P, morphism=False):
>    ...
> 
> def EllipticCurve_from_Jacobian(F, morphism=False):
>    ...
> }}}
The latter is not right -- it's the Jacobian elliptic curve which is returned!  We could call it just Jacobian() and raise a NotImplemented error if the genus is >1?

The first is fine though rather long.



---

archive/issue_comments_023958.json:
```json
{
    "body": "Replying to [comment:45 vbraun]:\n> {{{\n> def EllipticCurve_from_cubic_and_point(F, P, morphism=False):\n> }}}\n\nI think the name is a bit long, and I prefer \"True\" as the default. And can't we add this functionality to the existing constructor `EllipticCurve` instead of creating a new function?\n\n> {{{\n> def EllipticCurve_from_Jacobian(F, morphism=False):\n> }}}\n\n-1: the name sounds like the Jacobian is the input, while actually it is the output. Perhaps `EllipticCurveJacobian`, or add this functionality to the existing constructor `Jacobian`?",
    "created_at": "2013-02-12T19:51:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23958",
    "user": "https://github.com/mstreng"
}
```

Replying to [comment:45 vbraun]:
> {{{
> def EllipticCurve_from_cubic_and_point(F, P, morphism=False):
> }}}

I think the name is a bit long, and I prefer "True" as the default. And can't we add this functionality to the existing constructor `EllipticCurve` instead of creating a new function?

> {{{
> def EllipticCurve_from_Jacobian(F, morphism=False):
> }}}

-1: the name sounds like the Jacobian is the input, while actually it is the output. Perhaps `EllipticCurveJacobian`, or add this functionality to the existing constructor `Jacobian`?



---

archive/issue_comments_023959.json:
```json
{
    "body": "I think it should \n\n   EllipticCurve_from_cubic(F, P=None, morphism=False)\n\nand initially give an error if you don't specify P.  In many cases (in practice -- in general this is the world's most exciting open problem), one can *find* P, and that could be implemented.  \n\nIf you take a cubic F, take *any* random rational point P on F, and compute the corresponding elliptic curve, then put it in the unique minimal Weierstrass form with a_1,a_2,a_3 tiny, then the result does not depend on P.",
    "created_at": "2013-02-12T19:59:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23959",
    "user": "https://github.com/williamstein"
}
```

I think it should 

   EllipticCurve_from_cubic(F, P=None, morphism=False)

and initially give an error if you don't specify P.  In many cases (in practice -- in general this is the world's most exciting open problem), one can *find* P, and that could be implemented.  

If you take a cubic F, take *any* random rational point P on F, and compute the corresponding elliptic curve, then put it in the unique minimal Weierstrass form with a_1,a_2,a_3 tiny, then the result does not depend on P.



---

archive/issue_comments_023960.json:
```json
{
    "body": "We should reorganize the constructor around a tab-completable `elliptic_curve.<something>` hierarchy just like `matrix.<tab>` and `groups.<tab>`. But thats for another ticket.\n\nSo I take it we should go with\n\n```\ndef EllipticCurve_Jacobian(F, morphism=False):\n    ...\n```\n\nwhich would eventually become `elliptic_curve.Jacobian(...)`.",
    "created_at": "2013-02-12T20:09:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23960",
    "user": "https://github.com/vbraun"
}
```

We should reorganize the constructor around a tab-completable `elliptic_curve.<something>` hierarchy just like `matrix.<tab>` and `groups.<tab>`. But thats for another ticket.

So I take it we should go with

```
def EllipticCurve_Jacobian(F, morphism=False):
    ...
```

which would eventually become `elliptic_curve.Jacobian(...)`.



---

archive/issue_comments_023961.json:
```json
{
    "body": "I'm not thrilled about EllipticCurve_Jacobian for a few reasons:\n\n1. Introducing a new function into the global namespace just to deprecate it later is just very, very annoying to users.  Please don't do that.  \n\n2. Why not just \"EllipticCurve(...)\".  It is not ambiguous.  We have EllipticCurve_from_blah in some cases in order to resolve ambiguity, e.g., c4c6 and j.  But there is no ambiguity if a cubic polynomial is given.\n\n3. I would prefer adding a global Jacobian function than EllipticCurve_Jacobian.  E.g., something like\n\n```\n    def Jacobian(C, **kwds):\n        try:\n            return C.jacobian(**kwds)\n        except AttributeError:\n            if its a cubic... call your code above.\n```\n\n\nThere are genus 2 Jacobians, etc., for which typing Jacobian(C) (or Jac(C)) would be convenient. \n\nMaybe include Jacobian(matrix) for calculus students :-)\n\nWilliam",
    "created_at": "2013-02-12T20:42:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23961",
    "user": "https://github.com/williamstein"
}
```

I'm not thrilled about EllipticCurve_Jacobian for a few reasons:

1. Introducing a new function into the global namespace just to deprecate it later is just very, very annoying to users.  Please don't do that.  

2. Why not just "EllipticCurve(...)".  It is not ambiguous.  We have EllipticCurve_from_blah in some cases in order to resolve ambiguity, e.g., c4c6 and j.  But there is no ambiguity if a cubic polynomial is given.

3. I would prefer adding a global Jacobian function than EllipticCurve_Jacobian.  E.g., something like

```
    def Jacobian(C, **kwds):
        try:
            return C.jacobian(**kwds)
        except AttributeError:
            if its a cubic... call your code above.
```


There are genus 2 Jacobians, etc., for which typing Jacobian(C) (or Jac(C)) would be convenient. 

Maybe include Jacobian(matrix) for calculus students :-)

William



---

archive/issue_comments_023962.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-02-14T18:14:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23962",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_023963.json:
```json
{
    "body": "For the patchbot:\n\napply trac_3416_elliptic_curve_from_cubic_vb.patch, trac_3416_jacobians.patch",
    "created_at": "2013-02-14T18:16:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23963",
    "user": "https://github.com/vbraun"
}
```

For the patchbot:

apply trac_3416_elliptic_curve_from_cubic_vb.patch, trac_3416_jacobians.patch



---

archive/issue_comments_023964.json:
```json
{
    "body": "You have done a really nice job wit hthis.  I am in the middle of reading the code and will test it as soon as I can.",
    "created_at": "2013-02-15T13:48:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23964",
    "user": "https://github.com/JohnCremona"
}
```

You have done a really nice job wit hthis.  I am in the middle of reading the code and will test it as soon as I can.



---

archive/issue_comments_023965.json:
```json
{
    "body": "I like this code, and the patches apply cleanly to 5.7.rc0 even without the dependencies applied, but doctesting fails without the dependencies.  I would like someone else to review the dependencies since I want to be able to finish reviewing this one!",
    "created_at": "2013-02-17T20:32:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23965",
    "user": "https://github.com/JohnCremona"
}
```

I like this code, and the patches apply cleanly to 5.7.rc0 even without the dependencies applied, but doctesting fails without the dependencies.  I would like someone else to review the dependencies since I want to be able to finish reviewing this one!



---

archive/issue_comments_023966.json:
```json
{
    "body": "Tiniest nitpick. In the documentation:\n\n```\nA genus one curve is a torus with a complex coordinate system\n```\n\nThat's only true in characteristic 0 via the Lefschetz principle (for instance, for a genus one curve over `QQ(t)` or `CC(t)` this is a decidedly painful description) and simply untrue in positive characteristic. Yet, the code here should still work without a problem for most of these. I'd say just leave this sentence out. The rest seems fine without it.",
    "created_at": "2013-02-17T21:24:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23966",
    "user": "https://github.com/nbruin"
}
```

Tiniest nitpick. In the documentation:

```
A genus one curve is a torus with a complex coordinate system
```

That's only true in characteristic 0 via the Lefschetz principle (for instance, for a genus one curve over `QQ(t)` or `CC(t)` this is a decidedly painful description) and simply untrue in positive characteristic. Yet, the code here should still work without a problem for most of these. I'd say just leave this sentence out. The rest seems fine without it.



---

archive/issue_comments_023967.json:
```json
{
    "body": "This was just my attempt to give a one-paragraph introduction of what the Jacobian is; I'm aware (and do say) that it is not 100% mathematically waterproof. How about I add a sentence that I'm just talking about CC here. I think we should at least give some idea of what a genus-one curve is thats understandable to somebody who is not a algebraic geometer or number theorist...",
    "created_at": "2013-02-17T21:45:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23967",
    "user": "https://github.com/vbraun"
}
```

This was just my attempt to give a one-paragraph introduction of what the Jacobian is; I'm aware (and do say) that it is not 100% mathematically waterproof. How about I add a sentence that I'm just talking about CC here. I think we should at least give some idea of what a genus-one curve is thats understandable to somebody who is not a algebraic geometer or number theorist...



---

archive/issue_comments_023968.json:
```json
{
    "body": "Replying to [comment:56 vbraun]:\n> This was just my attempt to give a one-paragraph introduction of what the Jacobian is; I'm aware (and do say) that it is not 100% mathematically waterproof. How about I add a sentence that I'm just talking about CC here. I think we should at least give some idea of what a genus-one curve is thats understandable to somebody who is not a algebraic geometer or number theorist...\n\nAnd then proceed to describe what an elliptic curve is in terms of line bundles :-). Including `CC` here is indeed a solution, but this code is only interesting if you consider curves over base fields *different from* `CC`.\n\nI don't think you're ever going to get a useful 1-paragraph description that's helpful for anybody who doesn't already know what a genus 1 curve is and what their Jacobians are, so I wouldn't bother and just take the terms as self-evident (and include a literature reference).\n\n(It's a slightly simplified *description* of what the module does, by the way. Not a *version*.",
    "created_at": "2013-02-17T22:24:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23968",
    "user": "https://github.com/nbruin"
}
```

Replying to [comment:56 vbraun]:
> This was just my attempt to give a one-paragraph introduction of what the Jacobian is; I'm aware (and do say) that it is not 100% mathematically waterproof. How about I add a sentence that I'm just talking about CC here. I think we should at least give some idea of what a genus-one curve is thats understandable to somebody who is not a algebraic geometer or number theorist...

And then proceed to describe what an elliptic curve is in terms of line bundles :-). Including `CC` here is indeed a solution, but this code is only interesting if you consider curves over base fields *different from* `CC`.

I don't think you're ever going to get a useful 1-paragraph description that's helpful for anybody who doesn't already know what a genus 1 curve is and what their Jacobians are, so I wouldn't bother and just take the terms as self-evident (and include a literature reference).

(It's a slightly simplified *description* of what the module does, by the way. Not a *version*.



---

archive/issue_comments_023969.json:
```json
{
    "body": "I agree with Nils regarding the documentation -- no textbook needed!",
    "created_at": "2013-02-17T22:31:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23969",
    "user": "https://github.com/JohnCremona"
}
```

I agree with Nils regarding the documentation -- no textbook needed!



---

archive/issue_comments_023970.json:
```json
{
    "body": "Thanks for all the work! I have not looked at it in detail, but do have a few comments:\n\n* The following worked without the patch (using Magma), but gives a `ZeroDivisionError` with the patch: (see also [comment:27 here])\n> {{{\n> sage: P.<x,y,z> = QQ[]\n> sage: EllipticCurve_from_cubic(x<sup>3+y</sup>3+z^3, [-1,0,1])\n> \u2026\n> ZeroDivisionError: \n> }}}\n\n  That is because the code this patch is built on is incomplete (it misses a few such cases).\n\n* There is a backwards incompatibility in `EllipticCurve_from_cubic`. Input:\n  {{{\n  sage: P.<X,Y,Z> = QQ[]                               \n  sage: EllipticCurve_from_cubic(X<sup>3+Y</sup>3+Z^3, [1,-1,0])\n  }}}\n  Output: an elliptic curve without the patch, a morphism with the patch\n\n* Why not add a \"morphism\" parameter to `EllipticCurve` too? That way, `EllipticCurve_from_cubic` is not needed at all. This will make the global namespace smaller (leading to smaller startup times and less confusion on which function to use when). And as an added bonus, it allows a smooth deprecation of `EllipticCurve_from_cubic`, rather than the backwards incompatibility mentioned above.\n\n* When I do\n  {{{\n  sage: Jacobian?\n  }}}\n  I get \n  {{{\n  ...\n  Source File:    /scratch/tsg250/sage-5.5.rc0/devel/sage/sage/misc/lazy_import.so\n  ...\n       * A polynomial, see \"Jacobian_of_equation()\" for details.\n    \n       * A curve, see \"Jacobian_of_curve()\" for details.\n  }}}\n  But \"`Jacobian_of_equation?`\" and \"`Jacobian_of_curve?`\" don't work, because they are not in the global namespace. And it takes some effort to find out that\n  {{{\n  sage: sage.schemes.elliptic_curves.jacobian.Jacobian_of_curve?\n  }}}\n  works, unless someone first tells me that `Jacobian_of_curve` is in `sage.schemes.elliptic_curves.jacobian`.",
    "created_at": "2013-02-18T10:09:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23970",
    "user": "https://github.com/mstreng"
}
```

Thanks for all the work! I have not looked at it in detail, but do have a few comments:

* The following worked without the patch (using Magma), but gives a `ZeroDivisionError` with the patch: (see also [comment:27 here])
> {{{
> sage: P.<x,y,z> = QQ[]
> sage: EllipticCurve_from_cubic(x<sup>3+y</sup>3+z^3, [-1,0,1])
> …
> ZeroDivisionError: 
> }}}

  That is because the code this patch is built on is incomplete (it misses a few such cases).

* There is a backwards incompatibility in `EllipticCurve_from_cubic`. Input:
  {{{
  sage: P.<X,Y,Z> = QQ[]                               
  sage: EllipticCurve_from_cubic(X<sup>3+Y</sup>3+Z^3, [1,-1,0])
  }}}
  Output: an elliptic curve without the patch, a morphism with the patch

* Why not add a "morphism" parameter to `EllipticCurve` too? That way, `EllipticCurve_from_cubic` is not needed at all. This will make the global namespace smaller (leading to smaller startup times and less confusion on which function to use when). And as an added bonus, it allows a smooth deprecation of `EllipticCurve_from_cubic`, rather than the backwards incompatibility mentioned above.

* When I do
  {{{
  sage: Jacobian?
  }}}
  I get 
  {{{
  ...
  Source File:    /scratch/tsg250/sage-5.5.rc0/devel/sage/sage/misc/lazy_import.so
  ...
       * A polynomial, see "Jacobian_of_equation()" for details.
    
       * A curve, see "Jacobian_of_curve()" for details.
  }}}
  But "`Jacobian_of_equation?`" and "`Jacobian_of_curve?`" don't work, because they are not in the global namespace. And it takes some effort to find out that
  {{{
  sage: sage.schemes.elliptic_curves.jacobian.Jacobian_of_curve?
  }}}
  works, unless someone first tells me that `Jacobian_of_curve` is in `sage.schemes.elliptic_curves.jacobian`.



---

archive/issue_comments_023971.json:
```json
{
    "body": "The old `EllipticCurve_from_cubic` just computed the Jacobian using Magma. So, strictly speaking, we replace the wrong output with the correct output. Its intentionally backwards incompatible.\n\nI don't particularly like adding extra keyword arguments to `EllipticCurve` that only make sense in very special circumstances. If you want to reduce the number of global symbols, which I'm all in favor of, then one should combine the constructors into a class `EllipticCurve.from_foobar()` to disambiguate.\n\nThat'll also fix your last problem that the HTML hyperlinks don't translate particularly well into the text-mode help.",
    "created_at": "2013-02-18T14:08:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23971",
    "user": "https://github.com/vbraun"
}
```

The old `EllipticCurve_from_cubic` just computed the Jacobian using Magma. So, strictly speaking, we replace the wrong output with the correct output. Its intentionally backwards incompatible.

I don't particularly like adding extra keyword arguments to `EllipticCurve` that only make sense in very special circumstances. If you want to reduce the number of global symbols, which I'm all in favor of, then one should combine the constructors into a class `EllipticCurve.from_foobar()` to disambiguate.

That'll also fix your last problem that the HTML hyperlinks don't translate particularly well into the text-mode help.



---

archive/issue_comments_023972.json:
```json
{
    "body": "Replying to [comment:60 vbraun]:\n> I don't particularly like adding extra keyword arguments to `EllipticCurve` that only make sense in very special circumstances. If you want to reduce the number of global symbols, which I'm all in favor of, then one should combine the constructors into a class `EllipticCurve.from_foobar()` to disambiguate.\n\nWhether an (iso)morphism should be returned as well applies to more than very special circumstances. When creating an elliptic curve from a given algebraic curve plus rational point it's always relevant. In fact, keeping track of the transformations involved really does cost extra work, especially if you want the inverse as well. I doubt someone's going to bother to write a faster version that doesn't track the morphism, but as a general user interface it makes sense.\n\nRoutines are usually named after the thing they produce, so from `EllipticCurve_from_cubic` one expects an elliptic curve. `Isomorphism_from_cubic_curve_to_jacobian` would produce a morphism. Unless you claim `EllipticCurve_from_cubic` is only an internal routine, in which case it can return anything it likes.\n\nI don't quite know how to return extra optional information. We could return a tuple with as a second value the morphism so that we get the extremely magmaesque\n\n```\nE,phi = EllipticCurve_from_cubic(x^3+y^3+z^3,[1,0,-1],morphism=True)\n```\n\nbut that does mean the return type changes significantly upon supplying a keyword argument. Mandating\n\n```\nE, = EllipticCurve_from_cubic(x^3+y^3+z^3,[1,0,-1],morphism=False)\n```\n\nseems a no-go.\n\nI like the idea of returning morphisms to package up all relevant information. I did so quite a bit in Magma. I've noticed that this wasn't picked up by other users/authors, though, and that a few interface routines grew that picked apart the morphisms and returned domain and codomain separately. Perhaps that provides you with a data point of how successful morphism-based return values are in practice. It seems the majority of the mathematicians prefer to concentrate on the dots rather than the arrows ...",
    "created_at": "2013-02-18T17:06:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23972",
    "user": "https://github.com/nbruin"
}
```

Replying to [comment:60 vbraun]:
> I don't particularly like adding extra keyword arguments to `EllipticCurve` that only make sense in very special circumstances. If you want to reduce the number of global symbols, which I'm all in favor of, then one should combine the constructors into a class `EllipticCurve.from_foobar()` to disambiguate.

Whether an (iso)morphism should be returned as well applies to more than very special circumstances. When creating an elliptic curve from a given algebraic curve plus rational point it's always relevant. In fact, keeping track of the transformations involved really does cost extra work, especially if you want the inverse as well. I doubt someone's going to bother to write a faster version that doesn't track the morphism, but as a general user interface it makes sense.

Routines are usually named after the thing they produce, so from `EllipticCurve_from_cubic` one expects an elliptic curve. `Isomorphism_from_cubic_curve_to_jacobian` would produce a morphism. Unless you claim `EllipticCurve_from_cubic` is only an internal routine, in which case it can return anything it likes.

I don't quite know how to return extra optional information. We could return a tuple with as a second value the morphism so that we get the extremely magmaesque

```
E,phi = EllipticCurve_from_cubic(x^3+y^3+z^3,[1,0,-1],morphism=True)
```

but that does mean the return type changes significantly upon supplying a keyword argument. Mandating

```
E, = EllipticCurve_from_cubic(x^3+y^3+z^3,[1,0,-1],morphism=False)
```

seems a no-go.

I like the idea of returning morphisms to package up all relevant information. I did so quite a bit in Magma. I've noticed that this wasn't picked up by other users/authors, though, and that a few interface routines grew that picked apart the morphisms and returned domain and codomain separately. Perhaps that provides you with a data point of how successful morphism-based return values are in practice. It seems the majority of the mathematicians prefer to concentrate on the dots rather than the arrows ...



---

archive/issue_comments_023973.json:
```json
{
    "body": "Another possibility (which is easy in Python) is to enhance objects with extra structure. For example,\n\n\n```\nsage: K.<a,b> = NumberField([x^2+1,x^3-2]); K\nNumber Field in a with defining polynomial x^2 + 1 over its base field\nsage: L.<c> = K.absolute_field(); L\nNumber Field in c with defining polynomial x^6 + 3*x^4 + 4*x^3 + 3*x^2 - 12*x + 5\nsage: L.structure()\n(Isomorphism map:\n  From: Number Field in c with defining polynomial x^6 + 3*x^4 + 4*x^3 + 3*x^2 - 12*x + 5\n  To:   Number Field in a with defining polynomial x^2 + 1 over its base field, Isomorphism map:\n  From: Number Field in a with defining polynomial x^2 + 1 over its base field\n  To:   Number Field in c with defining polynomial x^6 + 3*x^4 + 4*x^3 + 3*x^2 - 12*x + 5)\n```\n\n\nIn our case, we could do:\n\n```\nsage: E = EllipticCurve_from_cubic(x^3+y^3+z^3, [1,0,-1])\nsage: E.extra_defining_data()\n{'cubic':x^3+y^3+z^3, 'morphism':..., 'point':[1,0,-1]}\n```\n\n\nIf the morphism gets computed, it's there; if it doesn't get computed, it isn't.\nWhether or not it gets computed can be determined as you suggest\n\n```\nE = EllipticCurve_from_cubic(x^3+y^3+z^3, [1,0,-1], morphism=False)\n```\n\nBUT the input does not impact the return type -- you get an elliptic curve no matter what.\n\nI not sure I agree with the assertion that people/algorithms will always compute the morphism.  There are alternative algorithms for computing the jacobian of a genus 1 curve that give the Jacobian without giving the morphism -- one involves computing the a_p and doing a search for curves with those a_p, and another involves \"Fermionic Fock Spaces\" (I think). \n\nTo me the above proposal fits better with how one thinks in mathematics; when you construct one object from another, you might as well remember you did so, and take advantage of it. \n\nAnother possibility would be to add a \"jacobian_structure()\" method to elliptic curves, which usually returns the identity map E-->E, but in the above case, returns a morphism X-->E.  More generally, it could return a simply transitive group-object, i.e., a map E x X --> X, but that's getting complicated.",
    "created_at": "2013-02-18T17:38:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23973",
    "user": "https://github.com/williamstein"
}
```

Another possibility (which is easy in Python) is to enhance objects with extra structure. For example,


```
sage: K.<a,b> = NumberField([x^2+1,x^3-2]); K
Number Field in a with defining polynomial x^2 + 1 over its base field
sage: L.<c> = K.absolute_field(); L
Number Field in c with defining polynomial x^6 + 3*x^4 + 4*x^3 + 3*x^2 - 12*x + 5
sage: L.structure()
(Isomorphism map:
  From: Number Field in c with defining polynomial x^6 + 3*x^4 + 4*x^3 + 3*x^2 - 12*x + 5
  To:   Number Field in a with defining polynomial x^2 + 1 over its base field, Isomorphism map:
  From: Number Field in a with defining polynomial x^2 + 1 over its base field
  To:   Number Field in c with defining polynomial x^6 + 3*x^4 + 4*x^3 + 3*x^2 - 12*x + 5)
```


In our case, we could do:

```
sage: E = EllipticCurve_from_cubic(x^3+y^3+z^3, [1,0,-1])
sage: E.extra_defining_data()
{'cubic':x^3+y^3+z^3, 'morphism':..., 'point':[1,0,-1]}
```


If the morphism gets computed, it's there; if it doesn't get computed, it isn't.
Whether or not it gets computed can be determined as you suggest

```
E = EllipticCurve_from_cubic(x^3+y^3+z^3, [1,0,-1], morphism=False)
```

BUT the input does not impact the return type -- you get an elliptic curve no matter what.

I not sure I agree with the assertion that people/algorithms will always compute the morphism.  There are alternative algorithms for computing the jacobian of a genus 1 curve that give the Jacobian without giving the morphism -- one involves computing the a_p and doing a search for curves with those a_p, and another involves "Fermionic Fock Spaces" (I think). 

To me the above proposal fits better with how one thinks in mathematics; when you construct one object from another, you might as well remember you did so, and take advantage of it. 

Another possibility would be to add a "jacobian_structure()" method to elliptic curves, which usually returns the identity map E-->E, but in the above case, returns a morphism X-->E.  More generally, it could return a simply transitive group-object, i.e., a map E x X --> X, but that's getting complicated.



---

archive/issue_comments_023974.json:
```json
{
    "body": "I just want to point out that this is all more complicated and less discoverable than just returning the morphism. Even if the function is not called `Morphism_from_cubic_to_elliptic_curve` I think we are smart enough to guess what the result means. \n\nFor the record, this is the current state:\n* `EllipticCurve(x<sup>3+y</sup>3+z^3, [1,-1,0])` returns elliptic curve\n* `EllipticCurve_from_cubic(x<sup>3+y</sup>3+z^3, [1,-1,0])` returns morphism\n* `EllipticCurve_from_cubic(x<sup>3+y</sup>3+z^3, [1,-1,0], morphism=True)` returns morphism\n* `EllipticCurve_from_cubic(x<sup>3+y</sup>3+z^3, [1,-1,0], morphism=False)` returns elliptic curve\n* `Jacobian(x<sup>3+y</sup>3+z^3)` returns elliptic curve\n* `Jacobian(x<sup>3+y</sup>3+z^3, morphism=False)` returns elliptic curve\n* `Jacobian(x<sup>3+y</sup>3+z^3, morphism=True)` returns morphism (but not isomorphism)\n\nWe can always tack on defining data to the elliptic curve in another ticket, so imho the only discussion that is relevant to this ticket is whether `morphism` should default to true or false.",
    "created_at": "2013-02-18T18:23:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23974",
    "user": "https://github.com/vbraun"
}
```

I just want to point out that this is all more complicated and less discoverable than just returning the morphism. Even if the function is not called `Morphism_from_cubic_to_elliptic_curve` I think we are smart enough to guess what the result means. 

For the record, this is the current state:
* `EllipticCurve(x<sup>3+y</sup>3+z^3, [1,-1,0])` returns elliptic curve
* `EllipticCurve_from_cubic(x<sup>3+y</sup>3+z^3, [1,-1,0])` returns morphism
* `EllipticCurve_from_cubic(x<sup>3+y</sup>3+z^3, [1,-1,0], morphism=True)` returns morphism
* `EllipticCurve_from_cubic(x<sup>3+y</sup>3+z^3, [1,-1,0], morphism=False)` returns elliptic curve
* `Jacobian(x<sup>3+y</sup>3+z^3)` returns elliptic curve
* `Jacobian(x<sup>3+y</sup>3+z^3, morphism=False)` returns elliptic curve
* `Jacobian(x<sup>3+y</sup>3+z^3, morphism=True)` returns morphism (but not isomorphism)

We can always tack on defining data to the elliptic curve in another ticket, so imho the only discussion that is relevant to this ticket is whether `morphism` should default to true or false.



---

archive/issue_comments_023975.json:
```json
{
    "body": "Replying to [comment:62 was]:\n> Another possibility (which is easy in Python) is to enhance objects with extra structure. For example,\n> \n> {{{\n> sage: K.<a,b> = NumberField([x<sup>2+1,x</sup>3-2]); K\n> Number Field in a with defining polynomial x^2 + 1 over its base field\n> sage: L.<c> = K.absolute_field(); L\n> Number Field in c with defining polynomial x^6 + 3*x^4 + 4*x^3 + 3*x^2 - 12*x + 5\n> sage: L.structure()\n> (Isomorphism map:\n>   From: Number Field in c with defining polynomial x^6 + 3*x^4 + 4*x^3 + 3*x^2 - 12*x + 5\n>   To:   Number Field in a with defining polynomial x^2 + 1 over its base field, Isomorphism map:\n>   From: Number Field in a with defining polynomial x^2 + 1 over its base field\n>   To:   Number Field in c with defining polynomial x^6 + 3*x^4 + 4*x^3 + 3*x^2 - 12*x + 5)\n> }}}\nAren't elliptic curves parents as well? That means they're unique. That makes it difficult to hang such information off them, because it means that all this structure information must be part of the constructor input.\n\nThe natural implementation of a lot of these constructors would be via a factory function that will punt to `EllipticCurve([a1,a2,a3,a4,a6])` to actually create the elliptic curve, so at the moment of \"unique instantiation\" the extra data isn't naturally available.\n\nYou can't go scribbling into fields on this elliptic curve because you risk overwriting information another constructor has already put there and which might still be relied upon elsewhere in the code.\n\nI'm starting to doubt that having unique parents is such a good design decision. Making one of the most complex objects in your system immutable complicates a lot of things.",
    "created_at": "2013-02-18T18:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23975",
    "user": "https://github.com/nbruin"
}
```

Replying to [comment:62 was]:
> Another possibility (which is easy in Python) is to enhance objects with extra structure. For example,
> 
> {{{
> sage: K.<a,b> = NumberField([x<sup>2+1,x</sup>3-2]); K
> Number Field in a with defining polynomial x^2 + 1 over its base field
> sage: L.<c> = K.absolute_field(); L
> Number Field in c with defining polynomial x^6 + 3*x^4 + 4*x^3 + 3*x^2 - 12*x + 5
> sage: L.structure()
> (Isomorphism map:
>   From: Number Field in c with defining polynomial x^6 + 3*x^4 + 4*x^3 + 3*x^2 - 12*x + 5
>   To:   Number Field in a with defining polynomial x^2 + 1 over its base field, Isomorphism map:
>   From: Number Field in a with defining polynomial x^2 + 1 over its base field
>   To:   Number Field in c with defining polynomial x^6 + 3*x^4 + 4*x^3 + 3*x^2 - 12*x + 5)
> }}}
Aren't elliptic curves parents as well? That means they're unique. That makes it difficult to hang such information off them, because it means that all this structure information must be part of the constructor input.

The natural implementation of a lot of these constructors would be via a factory function that will punt to `EllipticCurve([a1,a2,a3,a4,a6])` to actually create the elliptic curve, so at the moment of "unique instantiation" the extra data isn't naturally available.

You can't go scribbling into fields on this elliptic curve because you risk overwriting information another constructor has already put there and which might still be relied upon elsewhere in the code.

I'm starting to doubt that having unique parents is such a good design decision. Making one of the most complex objects in your system immutable complicates a lot of things.



---

archive/issue_comments_023976.json:
```json
{
    "body": "Totally OT, but elliptic curves currently don't even attempt to be unique:\n\n```\nsage: EllipticCurve('37b2') is EllipticCurve('37b2')\nFalse\n```\n",
    "created_at": "2013-02-18T19:09:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23976",
    "user": "https://github.com/vbraun"
}
```

Totally OT, but elliptic curves currently don't even attempt to be unique:

```
sage: EllipticCurve('37b2') is EllipticCurve('37b2')
False
```




---

archive/issue_comments_023977.json:
```json
{
    "body": "Replying to [comment:65 vbraun]:\n> Totally OT, but elliptic curves currently don't even attempt to be unique.\n\nOK! perhaps elliptic curves provide a way out of the quagmire of uniqueness of parents:\n\n\n```\nsage: E=EllipticCurve([1,2,3,4,3])\nsage: E([0,1,0])\n(0 : 1 : 0)\nsage: P=E([0,1,0])\nsage: P.parent()\nAbelian group of points on Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 4*x + 3 over Rational Field\n```\n\nIt seems elliptic curves are parents: `E.parent()` gives an error and `E.category()` does not (although it returns a rather questionable \"Category of sets\", but who cares), but the example above suggest they don't actually occur as parents of elements. I guess they do occur as domains and codomains of maps, though (see `E.multiplication_by_m_isogeny(2)`). If those get trapped in the coercion framework, something might choke on uniqueness assumptions.",
    "created_at": "2013-02-18T21:14:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23977",
    "user": "https://github.com/nbruin"
}
```

Replying to [comment:65 vbraun]:
> Totally OT, but elliptic curves currently don't even attempt to be unique.

OK! perhaps elliptic curves provide a way out of the quagmire of uniqueness of parents:


```
sage: E=EllipticCurve([1,2,3,4,3])
sage: E([0,1,0])
(0 : 1 : 0)
sage: P=E([0,1,0])
sage: P.parent()
Abelian group of points on Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 4*x + 3 over Rational Field
```

It seems elliptic curves are parents: `E.parent()` gives an error and `E.category()` does not (although it returns a rather questionable "Category of sets", but who cares), but the example above suggest they don't actually occur as parents of elements. I guess they do occur as domains and codomains of maps, though (see `E.multiplication_by_m_isogeny(2)`). If those get trapped in the coercion framework, something might choke on uniqueness assumptions.



---

archive/issue_comments_023978.json:
```json
{
    "body": "Replying to [comment:62 was]:\n\n> I not sure I agree with the assertion that people/algorithms will always compute the morphism.  There are alternative algorithms for computing the jacobian of a genus 1 curve that give the Jacobian without giving the morphism -- one involves computing the a_p and doing a search for curves with those a_p, and another involves \"Fermionic Fock Spaces\" (I think). \n> \n\nA basic (plane cubic) --> (Jacobian elliptic curve) function could be very much simpler, you just compute the classical S, T invariants as in Salmon and these are the c4,c6 (up to constant factors) of the Jacobian.\n\nMy guess is that most of the use this function will get will be from people who want to find rational points on the elliptic curve and map them back to \"their\" cubic, so we should make this easy and not requiring a PhD to understand.",
    "created_at": "2013-02-19T08:51:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23978",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:62 was]:

> I not sure I agree with the assertion that people/algorithms will always compute the morphism.  There are alternative algorithms for computing the jacobian of a genus 1 curve that give the Jacobian without giving the morphism -- one involves computing the a_p and doing a search for curves with those a_p, and another involves "Fermionic Fock Spaces" (I think). 
> 

A basic (plane cubic) --> (Jacobian elliptic curve) function could be very much simpler, you just compute the classical S, T invariants as in Salmon and these are the c4,c6 (up to constant factors) of the Jacobian.

My guess is that most of the use this function will get will be from people who want to find rational points on the elliptic curve and map them back to "their" cubic, so we should make this easy and not requiring a PhD to understand.



---

archive/issue_comments_023979.json:
```json
{
    "body": "Replying to [comment:67 cremona]:\n> A basic (plane cubic) --> (Jacobian elliptic curve) function could be very much simpler, you just compute the classical S, T invariants as in Salmon and these are the c4,c6 (up to constant factors) of the Jacobian.\n\nThis is precisely what `Jacobian()` does, for the record.",
    "created_at": "2013-02-19T15:07:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23979",
    "user": "https://github.com/vbraun"
}
```

Replying to [comment:67 cremona]:
> A basic (plane cubic) --> (Jacobian elliptic curve) function could be very much simpler, you just compute the classical S, T invariants as in Salmon and these are the c4,c6 (up to constant factors) of the Jacobian.

This is precisely what `Jacobian()` does, for the record.



---

archive/issue_comments_023980.json:
```json
{
    "body": "Attachment [trac_3416_jacobians.patch](tarball://root/attachments/some-uuid/ticket3416/trac_3416_jacobians.patch) by @vbraun created at 2013-02-24 03:01:30\n\nImproved patch",
    "created_at": "2013-02-24T03:01:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23980",
    "user": "https://github.com/vbraun"
}
```

Attachment [trac_3416_jacobians.patch](tarball://root/attachments/some-uuid/ticket3416/trac_3416_jacobians.patch) by @vbraun created at 2013-02-24 03:01:30

Improved patch



---

archive/issue_comments_023981.json:
```json
{
    "body": "The last patch fixes Miguel's `ZeroDivisionError` and sanitizes the code that was responsible for coordinate choices for the Weierstrass form.\n\nI've also removed any attempt at explaining what a genus-one curve is in the jacobian module.",
    "created_at": "2013-02-24T03:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23981",
    "user": "https://github.com/vbraun"
}
```

The last patch fixes Miguel's `ZeroDivisionError` and sanitizes the code that was responsible for coordinate choices for the Weierstrass form.

I've also removed any attempt at explaining what a genus-one curve is in the jacobian module.



---

archive/issue_comments_023982.json:
```json
{
    "body": "Attachment [trac_3416_elliptic_curve_from_cubic_vb.patch](tarball://root/attachments/some-uuid/ticket3416/trac_3416_elliptic_curve_from_cubic_vb.patch) by @vbraun created at 2013-05-17 17:34:14\n\nUpdated patch",
    "created_at": "2013-05-17T17:34:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23982",
    "user": "https://github.com/vbraun"
}
```

Attachment [trac_3416_elliptic_curve_from_cubic_vb.patch](tarball://root/attachments/some-uuid/ticket3416/trac_3416_elliptic_curve_from_cubic_vb.patch) by @vbraun created at 2013-05-17 17:34:14

Updated patch



---

archive/issue_comments_023983.json:
```json
{
    "body": "Patch updated for sage-5.10.beta3",
    "created_at": "2013-05-17T17:34:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23983",
    "user": "https://github.com/vbraun"
}
```

Patch updated for sage-5.10.beta3



---

archive/issue_comments_023984.json:
```json
{
    "body": "The three patches apply fine to 5.11.beta3;  doing some testing now.",
    "created_at": "2013-06-26T13:33:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23984",
    "user": "https://github.com/JohnCremona"
}
```

The three patches apply fine to 5.11.beta3;  doing some testing now.



---

archive/issue_comments_023985.json:
```json
{
    "body": "I get doctest failures in jacobian.py.   Al else in the elliptic_curves directory pass.\n\nSecondly,  in are_projectively_equivalent(P, Q) the function and exit with True as soon as the condition ratio[0]*p == ratio[1]*q holds, so those two lines should be replaced by\n\n```\nelse return ratio[0]*p == ratio[1]*q: \n```\n\nbut I don't know why the function does not just \n\n```\nreturn Matrix([P,Q]).rank() < 2 \n```\n\n?",
    "created_at": "2013-06-26T13:43:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23985",
    "user": "https://github.com/JohnCremona"
}
```

I get doctest failures in jacobian.py.   Al else in the elliptic_curves directory pass.

Secondly,  in are_projectively_equivalent(P, Q) the function and exit with True as soon as the condition ratio[0]*p == ratio[1]*q holds, so those two lines should be replaced by

```
else return ratio[0]*p == ratio[1]*q: 
```

but I don't know why the function does not just 

```
return Matrix([P,Q]).rank() < 2 
```

?



---

archive/issue_comments_023986.json:
```json
{
    "body": "Which doctest is failing? They all pass on my machine (also sage-5.11.beta3)\n\nI don't have a strong preference on how `are_projectively_equivalent()` should implement the check, I just kept that from the previous patch. Constructing a matrix and computing its rank incurs some overhead but that doesn't really matter here, so the matrix version should be used.",
    "created_at": "2013-06-26T14:44:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23986",
    "user": "https://github.com/vbraun"
}
```

Which doctest is failing? They all pass on my machine (also sage-5.11.beta3)

I don't have a strong preference on how `are_projectively_equivalent()` should implement the check, I just kept that from the previous patch. Constructing a matrix and computing its rank incurs some overhead but that doesn't really matter here, so the matrix version should be used.



---

archive/issue_comments_023987.json:
```json
{
    "body": "Sorry, I had assumed that the problem would be reproducible.  This is with 5.11.beta3 on which I had done nothing at all before adding the three patches:\n\n```\njec@fermat%../../sage -t sage/schemes/elliptic_curves/jacobian.py \nRunning doctests with ID 2013-06-26-17-52-06-6d628e14.\nDoctesting 1 file.\nsage -t sage/schemes/elliptic_curves/jacobian.py\n**********************************************************************\nFile \"sage/schemes/elliptic_curves/jacobian.py\", line 94, in sage.schemes.elliptic_curves.jacobian.Jacobian\nFailed example:\n    Jacobian(C, morphism=True)\nException raised:\n    Traceback (most recent call last):\n      File \"/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/doctest/forker.py\", line 486, in _run\n        self.execute(example, compiled, test.globs)\n      File \"/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/doctest/forker.py\", line 845, in execute\n        exec compiled in globs\n      File \"<doctest sage.schemes.elliptic_curves.jacobian.Jacobian[7]>\", line 1, in <module>\n        Jacobian(C, morphism=True)\n      File \"lazy_import.pyx\", line 313, in sage.misc.lazy_import.LazyImport.__call__ (sage/misc/lazy_import.c:2475)\n      File \"/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/schemes/elliptic_curves/jacobian.py\", line 120, in Jacobian\n        return Jacobian_of_curve(X, morphism=morphism, **kwds)\n      File \"/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/schemes/elliptic_curves/jacobian.py\", line 151, in Jacobian_of_curve\n        return Jacobian_of_equation(eqn, curve=curve)\n      File \"/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/schemes/elliptic_curves/jacobian.py\", line 235, in Jacobian_of_equation\n        X, Y, Z = WeierstrassForm(polynomial, variables=variables, transformation=True)\n    TypeError: WeierstrassForm() got an unexpected keyword argument 'transformation'\n**********************************************************************\nFile \"sage/schemes/elliptic_curves/jacobian.py\", line 192, in sage.schemes.elliptic_curves.jacobian.Jacobian_of_equation\nFailed example:\n    h = Jacobian(f, curve=Curve(f));  h\nException raised:\n    Traceback (most recent call last):\n      File \"/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/doctest/forker.py\", line 486, in _run\n        self.execute(example, compiled, test.globs)\n      File \"/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/doctest/forker.py\", line 845, in execute\n        exec compiled in globs\n      File \"<doctest sage.schemes.elliptic_curves.jacobian.Jacobian_of_equation[4]>\", line 1, in <module>\n        h = Jacobian(f, curve=Curve(f));  h\n      File \"lazy_import.pyx\", line 313, in sage.misc.lazy_import.LazyImport.__call__ (sage/misc/lazy_import.c:2475)\n      File \"/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/schemes/elliptic_curves/jacobian.py\", line 116, in Jacobian\n        return Jacobian_of_equation(X, **kwds)\n      File \"/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/schemes/elliptic_curves/jacobian.py\", line 235, in Jacobian_of_equation\n        X, Y, Z = WeierstrassForm(polynomial, variables=variables, transformation=True)\n    TypeError: WeierstrassForm() got an unexpected keyword argument 'transformation'\n**********************************************************************\nFile \"sage/schemes/elliptic_curves/jacobian.py\", line 200, in sage.schemes.elliptic_curves.jacobian.Jacobian_of_equation\nFailed example:\n    h([1,-1,0])\nException raised:\n    Traceback (most recent call last):\n      File \"/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/doctest/forker.py\", line 486, in _run\n        self.execute(example, compiled, test.globs)\n      File \"/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/doctest/forker.py\", line 845, in execute\n        exec compiled in globs\n      File \"<doctest sage.schemes.elliptic_curves.jacobian.Jacobian_of_equation[5]>\", line 1, in <module>\n        h([Integer(1),-Integer(1),Integer(0)])\n    NameError: name 'h' is not defined\n**********************************************************************\nFile \"sage/schemes/elliptic_curves/jacobian.py\", line 206, in sage.schemes.elliptic_curves.jacobian.Jacobian_of_equation\nFailed example:\n    E = h.codomain()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/doctest/forker.py\", line 486, in _run\n        self.execute(example, compiled, test.globs)\n      File \"/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/doctest/forker.py\", line 845, in execute\n        exec compiled in globs\n      File \"<doctest sage.schemes.elliptic_curves.jacobian.Jacobian_of_equation[6]>\", line 1, in <module>\n        E = h.codomain()\n    NameError: name 'h' is not defined\n**********************************************************************\nFile \"sage/schemes/elliptic_curves/jacobian.py\", line 207, in sage.schemes.elliptic_curves.jacobian.Jacobian_of_equation\nFailed example:\n    E.defining_polynomial()(h.defining_polynomials()).factor()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/doctest/forker.py\", line 486, in _run\n        self.execute(example, compiled, test.globs)\n      File \"/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/doctest/forker.py\", line 845, in execute\n        exec compiled in globs\n      File \"<doctest sage.schemes.elliptic_curves.jacobian.Jacobian_of_equation[7]>\", line 1, in <module>\n        E.defining_polynomial()(h.defining_polynomials()).factor()\n    NameError: name 'E' is not defined\n**********************************************************************\n2 items had failures:\n   1 of   9 in sage.schemes.elliptic_curves.jacobian.Jacobian\n   4 of  13 in sage.schemes.elliptic_curves.jacobian.Jacobian_of_equation\n    [39 tests, 5 failures, 2.61 s]\n----------------------------------------------------------------------\nsage -t sage/schemes/elliptic_curves/jacobian.py  # 5 doctests failed\n```\n\n\nNote that\n\n```\nsage: search_def(\"WeierstrassForm\")\nschemes/toric/weierstrass.py:355:def WeierstrassForm(polynomial, variables=None):\nschemes/toric/weierstrass.py:614:def WeierstrassForm_P2(polynomial, variables=None):\nschemes/toric/weierstrass.py:814:def WeierstrassForm_P1xP1(biquadric, variables=None):\nschemes/toric/weierstrass.py:952:def WeierstrassForm_P2_112(polynomial, variables=None):\n```\n\nIs there a missing dependency?",
    "created_at": "2013-06-26T16:56:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23987",
    "user": "https://github.com/JohnCremona"
}
```

Sorry, I had assumed that the problem would be reproducible.  This is with 5.11.beta3 on which I had done nothing at all before adding the three patches:

```
jec@fermat%../../sage -t sage/schemes/elliptic_curves/jacobian.py 
Running doctests with ID 2013-06-26-17-52-06-6d628e14.
Doctesting 1 file.
sage -t sage/schemes/elliptic_curves/jacobian.py
**********************************************************************
File "sage/schemes/elliptic_curves/jacobian.py", line 94, in sage.schemes.elliptic_curves.jacobian.Jacobian
Failed example:
    Jacobian(C, morphism=True)
Exception raised:
    Traceback (most recent call last):
      File "/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/doctest/forker.py", line 486, in _run
        self.execute(example, compiled, test.globs)
      File "/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/doctest/forker.py", line 845, in execute
        exec compiled in globs
      File "<doctest sage.schemes.elliptic_curves.jacobian.Jacobian[7]>", line 1, in <module>
        Jacobian(C, morphism=True)
      File "lazy_import.pyx", line 313, in sage.misc.lazy_import.LazyImport.__call__ (sage/misc/lazy_import.c:2475)
      File "/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/schemes/elliptic_curves/jacobian.py", line 120, in Jacobian
        return Jacobian_of_curve(X, morphism=morphism, **kwds)
      File "/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/schemes/elliptic_curves/jacobian.py", line 151, in Jacobian_of_curve
        return Jacobian_of_equation(eqn, curve=curve)
      File "/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/schemes/elliptic_curves/jacobian.py", line 235, in Jacobian_of_equation
        X, Y, Z = WeierstrassForm(polynomial, variables=variables, transformation=True)
    TypeError: WeierstrassForm() got an unexpected keyword argument 'transformation'
**********************************************************************
File "sage/schemes/elliptic_curves/jacobian.py", line 192, in sage.schemes.elliptic_curves.jacobian.Jacobian_of_equation
Failed example:
    h = Jacobian(f, curve=Curve(f));  h
Exception raised:
    Traceback (most recent call last):
      File "/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/doctest/forker.py", line 486, in _run
        self.execute(example, compiled, test.globs)
      File "/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/doctest/forker.py", line 845, in execute
        exec compiled in globs
      File "<doctest sage.schemes.elliptic_curves.jacobian.Jacobian_of_equation[4]>", line 1, in <module>
        h = Jacobian(f, curve=Curve(f));  h
      File "lazy_import.pyx", line 313, in sage.misc.lazy_import.LazyImport.__call__ (sage/misc/lazy_import.c:2475)
      File "/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/schemes/elliptic_curves/jacobian.py", line 116, in Jacobian
        return Jacobian_of_equation(X, **kwds)
      File "/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/schemes/elliptic_curves/jacobian.py", line 235, in Jacobian_of_equation
        X, Y, Z = WeierstrassForm(polynomial, variables=variables, transformation=True)
    TypeError: WeierstrassForm() got an unexpected keyword argument 'transformation'
**********************************************************************
File "sage/schemes/elliptic_curves/jacobian.py", line 200, in sage.schemes.elliptic_curves.jacobian.Jacobian_of_equation
Failed example:
    h([1,-1,0])
Exception raised:
    Traceback (most recent call last):
      File "/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/doctest/forker.py", line 486, in _run
        self.execute(example, compiled, test.globs)
      File "/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/doctest/forker.py", line 845, in execute
        exec compiled in globs
      File "<doctest sage.schemes.elliptic_curves.jacobian.Jacobian_of_equation[5]>", line 1, in <module>
        h([Integer(1),-Integer(1),Integer(0)])
    NameError: name 'h' is not defined
**********************************************************************
File "sage/schemes/elliptic_curves/jacobian.py", line 206, in sage.schemes.elliptic_curves.jacobian.Jacobian_of_equation
Failed example:
    E = h.codomain()
Exception raised:
    Traceback (most recent call last):
      File "/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/doctest/forker.py", line 486, in _run
        self.execute(example, compiled, test.globs)
      File "/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/doctest/forker.py", line 845, in execute
        exec compiled in globs
      File "<doctest sage.schemes.elliptic_curves.jacobian.Jacobian_of_equation[6]>", line 1, in <module>
        E = h.codomain()
    NameError: name 'h' is not defined
**********************************************************************
File "sage/schemes/elliptic_curves/jacobian.py", line 207, in sage.schemes.elliptic_curves.jacobian.Jacobian_of_equation
Failed example:
    E.defining_polynomial()(h.defining_polynomials()).factor()
Exception raised:
    Traceback (most recent call last):
      File "/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/doctest/forker.py", line 486, in _run
        self.execute(example, compiled, test.globs)
      File "/home/jec/sage-5.11.beta3/local/lib/python2.7/site-packages/sage/doctest/forker.py", line 845, in execute
        exec compiled in globs
      File "<doctest sage.schemes.elliptic_curves.jacobian.Jacobian_of_equation[7]>", line 1, in <module>
        E.defining_polynomial()(h.defining_polynomials()).factor()
    NameError: name 'E' is not defined
**********************************************************************
2 items had failures:
   1 of   9 in sage.schemes.elliptic_curves.jacobian.Jacobian
   4 of  13 in sage.schemes.elliptic_curves.jacobian.Jacobian_of_equation
    [39 tests, 5 failures, 2.61 s]
----------------------------------------------------------------------
sage -t sage/schemes/elliptic_curves/jacobian.py  # 5 doctests failed
```


Note that

```
sage: search_def("WeierstrassForm")
schemes/toric/weierstrass.py:355:def WeierstrassForm(polynomial, variables=None):
schemes/toric/weierstrass.py:614:def WeierstrassForm_P2(polynomial, variables=None):
schemes/toric/weierstrass.py:814:def WeierstrassForm_P1xP1(biquadric, variables=None):
schemes/toric/weierstrass.py:952:def WeierstrassForm_P2_112(polynomial, variables=None):
```

Is there a missing dependency?



---

archive/issue_comments_023988.json:
```json
{
    "body": "The `transformation` keyword argument is from #13458, which is listed as a dependency",
    "created_at": "2013-06-26T17:01:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23988",
    "user": "https://github.com/vbraun"
}
```

The `transformation` keyword argument is from #13458, which is listed as a dependency



---

archive/issue_comments_023989.json:
```json
{
    "body": "Attachment [trac_3416_fixes.patch](tarball://root/attachments/some-uuid/ticket3416/trac_3416_fixes.patch) by @vbraun created at 2013-06-26 17:04:32\n\nUpdated patch",
    "created_at": "2013-06-26T17:04:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23989",
    "user": "https://github.com/vbraun"
}
```

Attachment [trac_3416_fixes.patch](tarball://root/attachments/some-uuid/ticket3416/trac_3416_fixes.patch) by @vbraun created at 2013-06-26 17:04:32

Updated patch



---

archive/issue_comments_023990.json:
```json
{
    "body": "I've switched `are_projectively_equvalent` to the matrix version in the updated patch.",
    "created_at": "2013-06-26T17:05:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23990",
    "user": "https://github.com/vbraun"
}
```

I've switched `are_projectively_equvalent` to the matrix version in the updated patch.



---

archive/issue_comments_023991.json:
```json
{
    "body": "Replying to [comment:75 vbraun]:\n> The `transformation` keyword argument is from #13458, which is listed as a dependency\nVery sorry: I'm sure when I looked all three had the line through (I cannot see the colours very well).\nTesting again, with your new revision...",
    "created_at": "2013-06-26T17:09:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23991",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:75 vbraun]:
> The `transformation` keyword argument is from #13458, which is listed as a dependency
Very sorry: I'm sure when I looked all three had the line through (I cannot see the colours very well).
Testing again, with your new revision...



---

archive/issue_comments_023992.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-06-26T17:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23992",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_023993.json:
```json
{
    "body": "I'm now happy to give this a positive review -- at last!  Thanks to Volker for the hard work which gives a lot more than this ticket originally promised.\n\nI do not feel qualified to positively review #13458 though, so I hope this is not being inconsistent of me.",
    "created_at": "2013-06-26T17:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23993",
    "user": "https://github.com/JohnCremona"
}
```

I'm now happy to give this a positive review -- at last!  Thanks to Volker for the hard work which gives a lot more than this ticket originally promised.

I do not feel qualified to positively review #13458 though, so I hope this is not being inconsistent of me.



---

archive/issue_comments_023994.json:
```json
{
    "body": "Sorry, there are some issues with these patches:\n\nMost importantly, the doctests for `Jacobian_magma_from_plane_curve` don't actually use the function `Jacobian_magma_from_plane_curve`. So the function which is \"useful for doctesting\" doesn't seem to be used in any doctest.\n\nThen some details: I would replace\n\n```\nsage: x,y,z=PolynomialRing(QQ,3,'xyz').gens()\n```\n\nby\n\n```\nsage: R.<x,y,z> = PolynomialRing(QQ,3)\n```\n\nor\n\n```\nsage: R.<x,y,z> = QQ[]\n```\n\n\nAnd also replace\n\n```\nsage: f = x**5 + 1184*x**3 + 1846*x**2 + 956*x + 560\n```\n\nby\n\n```\nsage: f = x^5 + 1184*x^3 + 1846*x^2 + 956*x + 560\n```\n",
    "created_at": "2013-08-13T13:17:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23994",
    "user": "https://github.com/jdemeyer"
}
```

Sorry, there are some issues with these patches:

Most importantly, the doctests for `Jacobian_magma_from_plane_curve` don't actually use the function `Jacobian_magma_from_plane_curve`. So the function which is "useful for doctesting" doesn't seem to be used in any doctest.

Then some details: I would replace

```
sage: x,y,z=PolynomialRing(QQ,3,'xyz').gens()
```

by

```
sage: R.<x,y,z> = PolynomialRing(QQ,3)
```

or

```
sage: R.<x,y,z> = QQ[]
```


And also replace

```
sage: f = x**5 + 1184*x**3 + 1846*x**2 + 956*x + 560
```

by

```
sage: f = x^5 + 1184*x^3 + 1846*x^2 + 956*x + 560
```




---

archive/issue_comments_023995.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2013-08-13T13:17:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23995",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_023996.json:
```json
{
    "body": "I didn't write the `Jacobian_magma_...` functions, for the record. I just moved it out of `constructor.py` into a less visible location. I don't think that beautifying them makes any sense, the docstring is pretty clear that you shouldn't base your work on it. If anything, it should be removed altogether. Though IMHO that is not particularly urgent. \n\nThe attached patch changes the function call so that it is doctested.",
    "created_at": "2013-08-13T13:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23996",
    "user": "https://github.com/vbraun"
}
```

I didn't write the `Jacobian_magma_...` functions, for the record. I just moved it out of `constructor.py` into a less visible location. I don't think that beautifying them makes any sense, the docstring is pretty clear that you shouldn't base your work on it. If anything, it should be removed altogether. Though IMHO that is not particularly urgent. 

The attached patch changes the function call so that it is doctested.



---

archive/issue_comments_023997.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-08-13T13:41:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23997",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_023998.json:
```json
{
    "body": "Can any of the \"official\" reviewers of this ticket please check that these doctests pass with magma with\n\n```\n./sage -t --optional=sage,magma devel/sage/sage/schemes/elliptic_curves\n```\n",
    "created_at": "2013-08-13T13:45:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23998",
    "user": "https://github.com/jdemeyer"
}
```

Can any of the "official" reviewers of this ticket please check that these doctests pass with magma with

```
./sage -t --optional=sage,magma devel/sage/sage/schemes/elliptic_curves
```




---

archive/issue_comments_023999.json:
```json
{
    "body": "Replying to [comment:83 jdemeyer]:\n> Can any of the \"official\" reviewers of this ticket please check that these doctests pass with magma with\n> {{{\n> ./sage -t --optional=sage,magma devel/sage/sage/schemes/elliptic_curves\n> }}}\n\nI just did, and there are some problems, which I am now fixing.\n\nI note that the dependent #13458 is marged as having been merged, but only in 5.12.beta0 which is in the future for most of us!\n\nJohn",
    "created_at": "2013-08-13T13:47:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-23999",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:83 jdemeyer]:
> Can any of the "official" reviewers of this ticket please check that these doctests pass with magma with
> {{{
> ./sage -t --optional=sage,magma devel/sage/sage/schemes/elliptic_curves
> }}}

I just did, and there are some problems, which I am now fixing.

I note that the dependent #13458 is marged as having been merged, but only in 5.12.beta0 which is in the future for most of us!

John



---

archive/issue_comments_024000.json:
```json
{
    "body": "Am I doing something stupid here?  I have 5.11.rc0 with the patches from #13458 and this ticket applied.  Now\n\n```\nsage: R.<x,y,z> = QQ[]\nsage: f = x^3+y^3+60*z^3                            \nsage: from sage.schemes.elliptic_curves.jacobian import Jacobian_magma_equation\nsage: E = Jacobian_magma_equation(f)\n(...)\nNameError: global name 'SR' is not defined\n```\n\ndespite\n\n```\nsage: SR\nSymbolic Ring\n```\n\nThe relevant line works fine by itself:\n\n```\nsage: cmd = \"P<%s,%s,%s> := ProjectivePlane(RationalField());\"%SR(f).variables()\nsage: cmd\n'P<x,y,z> := ProjectivePlane(RationalField());'\n```\n",
    "created_at": "2013-08-13T14:12:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-24000",
    "user": "https://github.com/JohnCremona"
}
```

Am I doing something stupid here?  I have 5.11.rc0 with the patches from #13458 and this ticket applied.  Now

```
sage: R.<x,y,z> = QQ[]
sage: f = x^3+y^3+60*z^3                            
sage: from sage.schemes.elliptic_curves.jacobian import Jacobian_magma_equation
sage: E = Jacobian_magma_equation(f)
(...)
NameError: global name 'SR' is not defined
```

despite

```
sage: SR
Symbolic Ring
```

The relevant line works fine by itself:

```
sage: cmd = "P<%s,%s,%s> := ProjectivePlane(RationalField());"%SR(f).variables()
sage: cmd
'P<x,y,z> := ProjectivePlane(RationalField());'
```




---

archive/issue_comments_024001.json:
```json
{
    "body": "I've added the missing import, should work now.",
    "created_at": "2013-08-13T14:20:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-24001",
    "user": "https://github.com/vbraun"
}
```

I've added the missing import, should work now.



---

archive/issue_comments_024002.json:
```json
{
    "body": "Replying to [comment:86 vbraun]:\n> I've added the missing import, should work now.\nThat's odd as I would not have expected it to be necessary to import SR for a doctest.\n\nAnyway, that function is still wrong since 2 lines later it refers to P which I presume is a point on the curve, but there is no parameter P.  Shall we just delete this completely redundant function?\n\nThe next function `Jacobian_magma_from_plane_curve` needs a minor fix in the last line since rings is not imported.  It's fine with\n\n```\n    from sage.rings.all import QQ\n    return EllipticCurve(QQ, eval(s))\n```\n",
    "created_at": "2013-08-13T14:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-24002",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:86 vbraun]:
> I've added the missing import, should work now.
That's odd as I would not have expected it to be necessary to import SR for a doctest.

Anyway, that function is still wrong since 2 lines later it refers to P which I presume is a point on the curve, but there is no parameter P.  Shall we just delete this completely redundant function?

The next function `Jacobian_magma_from_plane_curve` needs a minor fix in the last line since rings is not imported.  It's fine with

```
    from sage.rings.all import QQ
    return EllipticCurve(QQ, eval(s))
```




---

archive/issue_comments_024003.json:
```json
{
    "body": "Attachment [trac_3416_magma.patch](tarball://root/attachments/some-uuid/ticket3416/trac_3416_magma.patch) by @vbraun created at 2013-08-13 14:57:00\n\nUpdated patch",
    "created_at": "2013-08-13T14:57:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-24003",
    "user": "https://github.com/vbraun"
}
```

Attachment [trac_3416_magma.patch](tarball://root/attachments/some-uuid/ticket3416/trac_3416_magma.patch) by @vbraun created at 2013-08-13 14:57:00

Updated patch



---

archive/issue_comments_024004.json:
```json
{
    "body": "Updated patch removes both `Jacobian_magma_...` functions since they don't really add anything useful.",
    "created_at": "2013-08-13T14:59:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-24004",
    "user": "https://github.com/vbraun"
}
```

Updated patch removes both `Jacobian_magma_...` functions since they don't really add anything useful.



---

archive/issue_comments_024005.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-08-13T15:25:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-24005",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_024006.json:
```json
{
    "body": "Replying to [comment:88 vbraun]:\n> Updated patch removes both `Jacobian_magma_...` functions since they don't really add anything useful.\n\nNow the optional tests certainly pass!  Back to positive review, and I hope that Jeroen is happy.",
    "created_at": "2013-08-13T15:25:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-24006",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:88 vbraun]:
> Updated patch removes both `Jacobian_magma_...` functions since they don't really add anything useful.

Now the optional tests certainly pass!  Back to positive review, and I hope that Jeroen is happy.



---

archive/issue_comments_024007.json:
```json
{
    "body": "Replying to [comment:89 cremona]:\n> Replying to [comment:88 vbraun]:\n> > Updated patch removes both `Jacobian_magma_...` functions since they don't really add anything useful.\n> \n> Now the optional tests certainly pass!\nObviously :-)\n\n> I hope that Jeroen is happy.\nSure!",
    "created_at": "2013-08-13T15:28:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-24007",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:89 cremona]:
> Replying to [comment:88 vbraun]:
> > Updated patch removes both `Jacobian_magma_...` functions since they don't really add anything useful.
> 
> Now the optional tests certainly pass!
Obviously :-)

> I hope that Jeroen is happy.
Sure!



---

archive/issue_comments_024008.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-08-20T12:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-24008",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_003632.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-20T12:58:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3416#event-3632"
}
```



---

archive/issue_comments_024009.json:
```json
{
    "body": "See #15340 for a follow-up.",
    "created_at": "2013-10-28T19:54:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3416#issuecomment-24009",
    "user": "https://github.com/vbraun"
}
```

See #15340 for a follow-up.
