# Issue 3416: Weierstrass form for cubics [with patch, with negative review]

Issue created by migration from Trac.

Original creator: moretti

Original creation time: 2008-06-13 16:19:39

Assignee: was

CC:  novoselt

Keywords: nagell, weierstrass, cubic, elliptic curves

This code still needs a bit of polishing and testing, but it's nearly ready to go. I am marking this with a negative review since it's not quite release ready, but people can check it out.

This includes code for finding the transformation maps.

-Bobby


---

Attachment

Since y^2 = quartic is also genus 1, I'm curious if there is a corresponding function planned to compute the Weierstrass form of a quartic hyperelliptic.


---

Comment by was created at 2008-06-13 22:21:41

You can't give your own code a negative review :-).  I changed it to "not ready for review".


---

Comment by craigcitro created at 2008-06-20 05:04:45

Changing keywords from "nagell, weierstrass, cubic, elliptic curves" to "nagell, weierstrass, cubic, elliptic curves, editor_wstein".


---

Attachment

Algorithm 7.4.10 of GTM 138


---

Comment by Niels created at 2010-07-13 23:29:25

I believe the formulas used here are incorrect. I'm not sure, but they appear similar to the erroneous formula's from Cohen's book. I'm currently working on an implementation that uses different formulas. I expect that to be done within two weeks.

One of my colleagues is working on y<sup>2</sup> = quartic, which I will implement for him. I expect this to be done within a couple of weeks. During Sage Days 23 plans were made for other curves too, but I'm not sure anyone is working on those.


---

Comment by was created at 2010-07-13 23:32:58

Replying to [comment:5 Niels]:
> I believe the formulas used here are incorrect. I'm not sure, but they appear similar to the erroneous formula's 
> from Cohen's book. I'm currently working on an implementation that uses different formulas.
>  I expect that to be done within two weeks.

Yes, they are definitely the wrong formulas in Cohen's book.

 -- William


---

Comment by cremona created at 2010-08-13 09:03:54

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

Comment by nbruin created at 2010-08-13 23:29:28

I have found that the descriptions in:

Cassels, J. W. S. Lectures on elliptic curves. London Mathematical Society Student Texts, 24. Cambridge University Press, Cambridge, 1991.

give excellent recipes for writing down isomorphisms from cubics, y!^2=quartic and intersections of two quadrics in P!^2 with a rational point to their Jacobians in weierstrass form.

The alternative method of writing down maps of degrees 3, 2, 4 (respectively) to their Jacobians using invariant theory (see Tom Fisher et al.) often results in nicer models, because there are less arbitrary choices to be made.


---

Comment by cremona created at 2010-08-14 11:34:39

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

Comment by Niels created at 2010-08-15 09:22:33

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

Attachment


---

Comment by Niels created at 2010-10-24 13:56:58

Changing status from needs_work to needs_review.


---

Attachment

Here is my first ever Sage patch: 14532.patch. It creates an elliptic curve from any homogeneous cubic. The cubic is transformed to Weierstrass, and birational maps between the equations are given. The case y<sup>2</sup> = quartic is not covered.

The patch is based upon Sage 4.4.4.

The used transformations are from Section 4.4 of the course notes: "G1CRPC: Rational Points on Curves", which I uploaded as cnotes.pdf.

Please review my patch, and provide extensive feedback.


---

Comment by cremona created at 2010-10-24 19:22:55

Just a couple of quick comments, as I have not yet had a chance to look at the patch properly or try it out.  First:  I'm not sure we really want my old lecture notes attached to this ticket!  There is nothing you are using there that is not in standard other sources.  But if they are there, they should be attributed ;)

Secondly, you absolutely cannot have print statements giving part of the output as a side-effect.  Better to return a tuple consisting of the elliptic curve and the morphisms.  This will break backwards compatibility, since the Magma version does not so this (though he underlying Magma function surely does), but it could be controlled by an extra parameter which defaults to False.


---

Comment by Niels created at 2010-10-25 06:53:28

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

Comment by cremona created at 2010-11-20 17:39:22

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2010-11-20 17:39:22

I tried to define the morphism properly, which should work, but it doesn't since in defining the morphism Sage checks that the polynomials used a homogeneous of the same degree (see line 458 of schemes.generic.morphism.py), but the degree function is not defined for elements of the coordinate ring.  This can be fixed:  although in general QuotientRingElement s have no degree, in this situation (where the quotient is by a homogeneous ideal) the degree is well-defined.


---

Comment by cremona created at 2010-11-20 18:48:29

See #10297 for a separate report on this (and, soon, a patch).


---

Comment by cremona created at 2010-11-20 19:06:34

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

Comment by Niels created at 2011-03-28 14:55:06

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

Attachment

patch_2011_04_26


---

Comment by Niels created at 2011-04-26 08:17:36

I now have the morphisms as optional output, which defaults to False. The output uses print statements, because I still cannot find a better form for the general non-homogeneous morphisms. I tried using strings instead, but adding a polynomial to a string did not work.

I hope this solution is okay for now. If anyone has a better suggestion for the representation, I will be happy to update my patch, or repatch it.


---

Comment by Niels created at 2011-04-26 08:17:36

Changing status from needs_work to needs_review.


---

Comment by Niels created at 2011-04-27 08:34:49

Changing status from needs_review to needs_work.


---

Comment by Niels created at 2011-04-27 08:34:49

I am writing my own documentation about the transformation from cubic to Weierstrass. I will upload it within the next few days.

I think I spotted a minor error in my patch. When P is not a flex, the program finds a second point P2 using the chord and tangent method. However, if P2 is a flex, I think the program will return an error. This is a simple fix, which will be up soon.


---

Attachment

patch_2011_04_27 with the fix for when P2 is a flex


---

Comment by Niels created at 2011-04-29 08:22:53

I'm sorry, I spotted another error when P2 is a flex. I'm fixing this today. I expect the new patch to be up today, and also the documentation. The documentation makes me confident that the new patch will be error-free.


---

Comment by Niels created at 2011-04-29 09:42:05

patch_2011_04_29 with additional fix


---

Attachment

The documentation is also up now. Comments on the documentation are welcome.

Please review my patch (trac_3416_elliptic_curve_from_cubic3.patch), and suggest any improvements it may need. The documentation describes how the patch works.


---

Comment by Niels created at 2011-04-29 10:41:38

Changing status from needs_work to needs_review.


---

Comment by Niels created at 2011-05-02 20:25:42

Documentation of patch3, including the source code - updated 2011_05_02


---

Comment by mstreng created at 2011-07-04 21:56:20

Changing component from number theory to elliptic curves.


---

Attachment

Did I understand correctly that one should apply trac_3416_elliptic_curve_from_cubic3.patch only?


---

Comment by Niels created at 2011-07-06 07:09:12

Replying to [comment:23 mstreng]:
> Did I understand correctly that one should apply trac_3416_elliptic_curve_from_cubic3.patch only?
> 
Yes, number 3 only, I guess I should have removed the other patches. Thanks for pointing this out.


---

Comment by mstreng created at 2011-07-06 09:28:07

You can't remove patches (unless you have special rights on the trac server). But whenever you upload a patch, you can help reviewers and release managers by writting (preferably both in comments and in the ticket description) which patches to apply and in which order. If you follow a [certain syntax](http://wiki.sagemath.org/buildbot) in the comments, then an additional bonus is that your patches will get automatically tested by the buildbot.

I almost gave you a negative review because of the following, but it seems that this is not something introduced by you, but just an error that was already there:

The documentation of `EllipticCurve_from_cubic` says that P should be a tuple, but the function only accepts lists (e.g. `[-1,0,1]`), not tuples (e.g. `(-1,0,1)`). Well, I guess I need to work harder for a review.


---

Comment by mstreng created at 2011-07-06 10:19:55


```
sage -t -long devel/sage/sage/schemes/elliptic_curves/constructor.py
**********************************************************************
Error: TAB character found.
```

You can't use TAB characters in python. Please replace it by the appropriate number of spaces. You can probably set up your editor so that it never uses TAB characters (and uses spaces instead).

I'll read your code and give you a few suggestions for the next version.


---

Comment by mstreng created at 2011-07-06 10:19:55

Changing status from needs_review to needs_work.


---

Comment by mstreng created at 2011-07-06 11:02:37

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

Comment by mstreng created at 2011-07-06 11:04:13

Replying to [comment:25 mstreng]:
> I almost gave you a negative review because of the following, but it seems that this is not something introduced by you, but just an error that was already there:
> 
> The documentation of `EllipticCurve_from_cubic` says that P should be a tuple, but the function only accepts lists (e.g. `[-1,0,1]`), not tuples (e.g. `(-1,0,1)`). Well, I guess I need to work harder for a review.

Never mind this comment: it does accept tuples, it just does not accept `(-1,0,1)`, only `(-1,1,0)`.


---

Comment by mstreng created at 2011-07-06 11:16:24

ps. `are_projectively_equivalent` needs documentation including tests. Even though it is not available to the user, it must make sense to developers who want to edit your code.


---

Comment by cremona created at 2011-07-06 11:26:16

I very strongly agree that outputting the map as strings is not acceptable, and makes using this output impossible.  I said as much in an earlier review, and the response was that the author could not work out how to return maps.

In a spirit of cooperation and so that this can eventually be finished, let's try to carry out Marco's suggestion to construct a hom properly.  I seem to remember that when I tried this last it failed for some rather silly reason, but we really should be able to get this to work!


---

Comment by nbruin created at 2011-07-06 17:13:15

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

Comment by mstreng created at 2011-07-06 17:44:29

Replying to [comment:31 nbruin]:
> If you are implementing your algorithm "bare bones" (internally, you just work with polynomials and you don't use any of the scheme machinery and your input consists of a homogeneous poly rather than a plane curve) there could be some value of also making your output available "bare bones", i.e., just return the list [a1,a2,a3,a4,a6] and a list of polynomials describing the map.
> 
> There is a cost to using schemes, ambient spaces etc., so there may be a benefit in having the raw functionality available in a form that avoids it. Once you have a routine that does the heavy lifting, it's straightforward to write a wrapper that provides an interface in scheme language.

I like this idea. So Niels's code could simply output three lists: the [a1,a2,a3,a4,a6] and 2 lists of 3 polynomials each. Outputting instead of printing should be an easy enough change.

And then a new member function of `ProjectiveCurve_generic` could call it (or an analogous "`y^2`=quartic" function) and convert the output to an `EllipticCurve...` and two `SchemeMorphism...` objects.


---

Comment by mstreng created at 2011-07-06 18:02:33

Replying to [comment:32 mstreng]:
> And then a new member function of `ProjectiveCurve_generic` could call it (or an analogous "`y^2`=quartic" function) and convert the output to an `EllipticCurve...` and two `SchemeMorphism...` objects.

(ps. this part is for a later ticket, of course)


---

Comment by Niels created at 2011-07-06 19:27:40

Thank you all for the comments. I will have another go at making this patch work.


---

Comment by cremona created at 2012-12-02 12:11:31

This has arisen once again on sage-nt: is anyone interested in making this work at last?


---

Comment by vbraun created at 2012-12-02 14:00:49

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

Comment by cremona created at 2012-12-02 14:28:57

Sure --without any points you can easily write down a W. equation for the Jacobian of the plane cubic.  Even if the cubic has no rational points, such as the famous `3x<sup>3+4y</sup>3+5z^3=0`.  But that is not usual what people want, and should have a different name (such as "Jacobian").


---

Comment by novoselt created at 2012-12-02 15:03:29

And what is done by Maple in
http://www.maplesoft.com/support/help/Maple/view.aspx?path=algcurves/Weierstrassform
?

It does return the maps in both directions without using any points.


---

Comment by cremona created at 2012-12-02 15:44:18

Replying to [comment:38 novoselt]:
> And what is done by Maple in
> http://www.maplesoft.com/support/help/Maple/view.aspx?path=algcurves/Weierstrassform
> ?
> 
> It does return the maps in both directions without using any points.

I have no idea.  The definition there is wrong:  an elliptic curve is not just a genus 1 curve, it is a genus one curve with a specified point.  Perhaps Maple tries to find a point (it does say that the function can be speeded up by providing one), and perhaps if there is no rational point it uses something generic, or a point defined over an extension.  Without a notion of field of definition, you could do anything.   Note that Magma's function does not require a point to be specified;  if none is given it tries to find one, uses it if it finds one and otherwise raises a run-time error.

Someone with Maple could try the Selmer curve (of my previous post) to see what it does.


---

Comment by vbraun created at 2012-12-02 15:45:12

I think Maple does the same as #13458: it returns a rational multi-covering. This you can also get without a point.

Currently I don't like the way the transformation is returned in this ticket. A bunch of text, really? Can't we return concatenated maps or something that can be accessed programmatically? Or, failing that, a custom python object that can be queried for the defining polynomials.

The good news is that we seem to have all relevant algorithms implemented, we just need to settle on an interface. My suggestion would be

A constructor function EllipticCurve_from_curve(equation, point=None, proof=False)
If proof=False then just the Weierstrass form is returned using whatever algorithm is fastest (probably ignoring the given point).
If proof=True and no point is given, a pair (E,f) of elliptic curve and rational covering map from the curve to the Weierstrass form is returned.
If proof=True and a point is given, then a pair (E,f) is returned such that f is an isomorphism.
Make EllipticCurve_from_cubic an alias for EllipticCurve_from_curve. The latter will also handle e.g. y^2=quartic(x) e.g., so it shouldn't mention cubic.


---

Comment by vbraun created at 2013-02-12 11:57:12

Does anybody have an objection to my suggestion of implementing a constructor function `EllipticCurve_from_curve(equation, point=None, proof=False)`, or perhaps `certificate=False`, that by default returns the Weierstrass form of the Jacobian and otherwise a morphism? I can work over this ticket but it would be nice if we can agree on the interface first.


---

Comment by mstreng created at 2013-02-12 12:09:57

Replying to [comment:41 vbraun]:
> Does anybody have an objection to my suggestion

No objection, but a few comments:

 * Don't call it "proof", since your proposal always gives provenly correct output. I'm not a fan of "certificate" either. How about "morphism" or "morphisms"?
 * In the case of an isomorphism, could you also return its inverse?
 * When a point is provided, I would prefer the default to be to output the isomorphisms too, as most applications will need them.

Anyway, thanks for picking this up again!


---

Comment by cremona created at 2013-02-12 12:42:49

Thanks from me too.  Is the plan as follows:  input is a smooth plane cubic, possibly with a rational point.  If there is a point given then the output includes a Weierstrass model birational to the input curve, in fact  isomorphic to it, with a linear projective change of coordinates if the point was a flex and a more complicated (quadratic) map on `P^2` inducing the isomorphism otherwise;  while if there is no point given then the curve returned is the Jacobian.  In the latter case one could also return a map from the input curve to the Jacobian, namely the associated 3-covering map of degree 9.  And no attempt is made to find rational points if none are given.

That seems reasonable to me, provided that the documentation makes it clear how different the output will be in the two cases (point supplied or not).


---

Comment by nbruin created at 2013-02-12 18:51:44

Replying to [comment:43 cremona]:
> If there is a point given then the output includes a Weierstrass model birational to the input curve, in fact  isomorphic to it
[...]
> In the latter case one could also return a map from the input curve to the Jacobian, namely the associated 3-covering map of degree 9.  And no attempt is made to find rational points if none are given.

Since the two cases are distinct (in one case the cubic is birational over the base field to the returned curve, in the other case not necessarily) I think we cannot treat those cases silently as the same. At the very least it needs an option. I would prefer a different routine for the latter. `Jacobian` comes to mind.


---

Comment by vbraun created at 2013-02-12 19:34:54

So how about

```
def EllipticCurve_from_cubic_and_point(F, P, morphism=False):
   ...

def EllipticCurve_from_Jacobian(F, morphism=False):
   ...
```



---

Comment by cremona created at 2013-02-12 19:44:10

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

Comment by mstreng created at 2013-02-12 19:51:41

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

Comment by was created at 2013-02-12 19:59:32

I think it should 

   EllipticCurve_from_cubic(F, P=None, morphism=False)

and initially give an error if you don't specify P.  In many cases (in practice -- in general this is the world's most exciting open problem), one can *find* P, and that could be implemented.  

If you take a cubic F, take *any* random rational point P on F, and compute the corresponding elliptic curve, then put it in the unique minimal Weierstrass form with a_1,a_2,a_3 tiny, then the result does not depend on P.


---

Comment by vbraun created at 2013-02-12 20:09:47

We should reorganize the constructor around a tab-completable `elliptic_curve.<something>` hierarchy just like `matrix.<tab>` and `groups.<tab>`. But thats for another ticket.

So I take it we should go with

```
def EllipticCurve_Jacobian(F, morphism=False):
    ...
```

which would eventually become `elliptic_curve.Jacobian(...)`.


---

Comment by was created at 2013-02-12 20:42:35

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

Comment by vbraun created at 2013-02-14 18:14:41

Changing status from needs_work to needs_review.


---

Comment by vbraun created at 2013-02-14 18:16:27

For the patchbot:

apply trac_3416_elliptic_curve_from_cubic_vb.patch, trac_3416_jacobians.patch


---

Comment by cremona created at 2013-02-15 13:48:24

You have done a really nice job wit hthis.  I am in the middle of reading the code and will test it as soon as I can.


---

Comment by cremona created at 2013-02-17 20:32:47

I like this code, and the patches apply cleanly to 5.7.rc0 even without the dependencies applied, but doctesting fails without the dependencies.  I would like someone else to review the dependencies since I want to be able to finish reviewing this one!


---

Comment by nbruin created at 2013-02-17 21:24:47

Tiniest nitpick. In the documentation:

```
A genus one curve is a torus with a complex coordinate system
```

That's only true in characteristic 0 via the Lefschetz principle (for instance, for a genus one curve over `QQ(t)` or `CC(t)` this is a decidedly painful description) and simply untrue in positive characteristic. Yet, the code here should still work without a problem for most of these. I'd say just leave this sentence out. The rest seems fine without it.


---

Comment by vbraun created at 2013-02-17 21:45:01

This was just my attempt to give a one-paragraph introduction of what the Jacobian is; I'm aware (and do say) that it is not 100% mathematically waterproof. How about I add a sentence that I'm just talking about CC here. I think we should at least give some idea of what a genus-one curve is thats understandable to somebody who is not a algebraic geometer or number theorist...


---

Comment by nbruin created at 2013-02-17 22:24:17

Replying to [comment:56 vbraun]:
> This was just my attempt to give a one-paragraph introduction of what the Jacobian is; I'm aware (and do say) that it is not 100% mathematically waterproof. How about I add a sentence that I'm just talking about CC here. I think we should at least give some idea of what a genus-one curve is thats understandable to somebody who is not a algebraic geometer or number theorist...

And then proceed to describe what an elliptic curve is in terms of line bundles :-). Including `CC` here is indeed a solution, but this code is only interesting if you consider curves over base fields _different from_ `CC`.

I don't think you're ever going to get a useful 1-paragraph description that's helpful for anybody who doesn't already know what a genus 1 curve is and what their Jacobians are, so I wouldn't bother and just take the terms as self-evident (and include a literature reference).

(It's a slightly simplified _description_ of what the module does, by the way. Not a _version_.


---

Comment by cremona created at 2013-02-17 22:31:53

I agree with Nils regarding the documentation -- no textbook needed!


---

Comment by mstreng created at 2013-02-18 10:09:06

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

Comment by vbraun created at 2013-02-18 14:08:09

The old `EllipticCurve_from_cubic` just computed the Jacobian using Magma. So, strictly speaking, we replace the wrong output with the correct output. Its intentionally backwards incompatible.

I don't particularly like adding extra keyword arguments to `EllipticCurve` that only make sense in very special circumstances. If you want to reduce the number of global symbols, which I'm all in favor of, then one should combine the constructors into a class `EllipticCurve.from_foobar()` to disambiguate.

That'll also fix your last problem that the HTML hyperlinks don't translate particularly well into the text-mode help.


---

Comment by nbruin created at 2013-02-18 17:06:20

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

Comment by was created at 2013-02-18 17:38:12

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

Comment by vbraun created at 2013-02-18 18:23:25

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

Comment by nbruin created at 2013-02-18 18:26:11

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

Comment by vbraun created at 2013-02-18 19:09:53

Totally OT, but elliptic curves currently don't even attempt to be unique:

```
sage: EllipticCurve('37b2') is EllipticCurve('37b2')
False
```



---

Comment by nbruin created at 2013-02-18 21:14:15

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

Comment by cremona created at 2013-02-19 08:51:08

Replying to [comment:62 was]:

> I not sure I agree with the assertion that people/algorithms will always compute the morphism.  There are alternative algorithms for computing the jacobian of a genus 1 curve that give the Jacobian without giving the morphism -- one involves computing the a_p and doing a search for curves with those a_p, and another involves "Fermionic Fock Spaces" (I think). 
> 

A basic (plane cubic) --> (Jacobian elliptic curve) function could be very much simpler, you just compute the classical S, T invariants as in Salmon and these are the c4,c6 (up to constant factors) of the Jacobian.

My guess is that most of the use this function will get will be from people who want to find rational points on the elliptic curve and map them back to "their" cubic, so we should make this easy and not requiring a PhD to understand.


---

Comment by vbraun created at 2013-02-19 15:07:07

Replying to [comment:67 cremona]:
> A basic (plane cubic) --> (Jacobian elliptic curve) function could be very much simpler, you just compute the classical S, T invariants as in Salmon and these are the c4,c6 (up to constant factors) of the Jacobian.

This is precisely what `Jacobian()` does, for the record.


---

Attachment

Improved patch


---

Comment by vbraun created at 2013-02-24 03:15:26

The last patch fixes Miguel's `ZeroDivisionError` and sanitizes the code that was responsible for coordinate choices for the Weierstrass form.

I've also removed any attempt at explaining what a genus-one curve is in the jacobian module.


---

Attachment

Updated patch


---

Comment by vbraun created at 2013-05-17 17:34:32

Patch updated for sage-5.10.beta3


---

Comment by cremona created at 2013-06-26 13:33:54

The three patches apply fine to 5.11.beta3;  doing some testing now.


---

Comment by cremona created at 2013-06-26 13:43:30

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

Comment by vbraun created at 2013-06-26 14:44:02

Which doctest is failing? They all pass on my machine (also sage-5.11.beta3)

I don't have a strong preference on how `are_projectively_equivalent()` should implement the check, I just kept that from the previous patch. Constructing a matrix and computing its rank incurs some overhead but that doesn't really matter here, so the matrix version should be used.


---

Comment by cremona created at 2013-06-26 16:56:33

Sorry, I had assumed that the problem would be reproducible.  This is with 5.11.beta3 on which I had done nothing at all before adding the three patches:

```
jec`@`fermat%../../sage -t sage/schemes/elliptic_curves/jacobian.py 
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

Comment by vbraun created at 2013-06-26 17:01:22

The `transformation` keyword argument is from #13458, which is listed as a dependency


---

Attachment

Updated patch


---

Comment by vbraun created at 2013-06-26 17:05:19

I've switched `are_projectively_equvalent` to the matrix version in the updated patch.


---

Comment by cremona created at 2013-06-26 17:09:42

Replying to [comment:75 vbraun]:
> The `transformation` keyword argument is from #13458, which is listed as a dependency
Very sorry: I'm sure when I looked all three had the line through (I cannot see the colours very well).
Testing again, with your new revision...


---

Comment by cremona created at 2013-06-26 17:21:13

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2013-06-26 17:21:13

I'm now happy to give this a positive review -- at last!  Thanks to Volker for the hard work which gives a lot more than this ticket originally promised.

I do not feel qualified to positively review #13458 though, so I hope this is not being inconsistent of me.


---

Comment by jdemeyer created at 2013-08-13 13:17:28

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

Comment by jdemeyer created at 2013-08-13 13:17:28

Changing status from positive_review to needs_work.


---

Comment by vbraun created at 2013-08-13 13:40:19

I didn't write the `Jacobian_magma_...` functions, for the record. I just moved it out of `constructor.py` into a less visible location. I don't think that beautifying them makes any sense, the docstring is pretty clear that you shouldn't base your work on it. If anything, it should be removed altogether. Though IMHO that is not particularly urgent. 

The attached patch changes the function call so that it is doctested.


---

Comment by vbraun created at 2013-08-13 13:41:38

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2013-08-13 13:45:46

Can any of the "official" reviewers of this ticket please check that these doctests pass with magma with

```
./sage -t --optional=sage,magma devel/sage/sage/schemes/elliptic_curves
```



---

Comment by cremona created at 2013-08-13 13:47:06

Replying to [comment:83 jdemeyer]:
> Can any of the "official" reviewers of this ticket please check that these doctests pass with magma with
> {{{
> ./sage -t --optional=sage,magma devel/sage/sage/schemes/elliptic_curves
> }}}

I just did, and there are some problems, which I am now fixing.

I note that the dependent #13458 is marged as having been merged, but only in 5.12.beta0 which is in the future for most of us!

John


---

Comment by cremona created at 2013-08-13 14:12:10

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

Comment by vbraun created at 2013-08-13 14:20:13

I've added the missing import, should work now.


---

Comment by cremona created at 2013-08-13 14:43:09

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

Attachment

Updated patch


---

Comment by vbraun created at 2013-08-13 14:59:21

Updated patch removes both `Jacobian_magma_...` functions since they don't really add anything useful.


---

Comment by cremona created at 2013-08-13 15:25:26

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2013-08-13 15:25:26

Replying to [comment:88 vbraun]:
> Updated patch removes both `Jacobian_magma_...` functions since they don't really add anything useful.

Now the optional tests certainly pass!  Back to positive review, and I hope that Jeroen is happy.


---

Comment by jdemeyer created at 2013-08-13 15:28:50

Replying to [comment:89 cremona]:
> Replying to [comment:88 vbraun]:
> > Updated patch removes both `Jacobian_magma_...` functions since they don't really add anything useful.
> 
> Now the optional tests certainly pass!
Obviously :-)

> I hope that Jeroen is happy.
Sure!


---

Comment by jdemeyer created at 2013-08-20 12:58:04

Resolution: fixed


---

Comment by vbraun created at 2013-10-28 19:54:29

See #15340 for a follow-up.
