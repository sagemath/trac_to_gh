# Issue 6384: elliptic curve -- isogeny function seems completely totally broken in first example I try

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-21 23:44:06

Assignee: tbd

CC:  shumow@gmail.com kohel cremona

First the docstring for E.isogeny? has a typo

```
(defaul:None)
```

Note the missing t.

Next, I tried taking the elliptic curve 11a and one 5-torsion point P on it and trying to make the isogeny `E --> E/<P>`.  It seems that the result is a *total disaster in every imaginable way*.


```
sage: E = EllipticCurve('11a'); P = E.torsion_subgroup().gens()[0]; P
(5 : 5 : 1)
sage: phi = E.isogeny([P]); phi
Isogeny of degree 1 from Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field to Elliptic Curve defined by y^2 + y = x^3 - x^2 - 560*x - 4277 over Rational Field
sage: phi.codomain().conductor()
530575705
sage: phi.codomain().conductor().factor()
5 * 11 * 1531 * 6301
```


Note that: 

  * the two curves are not isogenous, since their conductors are different

  * the degree of the isogeny is reported to be 1, but it should be 5.

 


---

Comment by shumow created at 2009-06-22 16:36:31

The problem is where you do:

> sage: phi = E.isogeny([P]); phi

That is not the correct way to specify a kernel.  You are trying to specify the generator, and expecting the isogeny function to determine this.  (We could, at some point modify this to be the case in some sense.)  However, the correct way to specify an isogeny with a kernel list is to specify the whole kernel.  So, what you would need to do is this:

> sage: phi = E.isogeny([E(0), P, 2*P, 3*P, 4*P]); phi

You have a good point about the typo in the docstring.




Replying to [ticket:6384 was]:
> First the docstring for E.isogeny? has a typo
> {{{
> (defaul:None)
> }}}
> Note the missing t.
> 
> Next, I tried taking the elliptic curve 11a and one 5-torsion point P on it and trying to make the isogeny `E --> E/<P>`.  It seems that the result is a *total disaster in every imaginable way*.
> 
> {{{
> sage: E = EllipticCurve('11a'); P = E.torsion_subgroup().gens()[0]; P
> (5 : 5 : 1)
> sage: phi = E.isogeny([P]); phi
> Isogeny of degree 1 from Elliptic Curve defined by y^2 + y = x^3 - x^2 - 10*x - 20 over Rational Field to Elliptic Curve defined by y^2 + y = x^3 - x^2 - 560*x - 4277 over Rational Field
> sage: phi.codomain().conductor()
> 530575705
> sage: phi.codomain().conductor().factor()
> 5 * 11 * 1531 * 6301
> }}}
> 
> Note that: 
> 
>   * the two curves are not isogenous, since their conductors are different
> 
>   * the degree of the isogeny is reported to be 1, but it should be 5.
> 
>


---

Comment by shumow created at 2009-06-22 16:36:31

Changing assignee from tbd to shumow.


---

Comment by was created at 2009-06-22 16:44:47

I've changed the description of this ticket to: " isogeny function is not robust -- it doesn't check validity of its input". 

The first easy fix is that you must check that the input list of points is a subgroup and raise an error if it isn't. 

An enhancement can be opened as a separate ticket that would allow for generators instead.  Of course, a better solution is to just create a "finite subgroups of elliptic curves class". 

 -- William


---

Comment by wuthrich created at 2009-06-25 17:16:25

I would change the input to be as now, but if a list of points is given, the kernel is understood to be the subgroup *GENERATED* by these points.

I guess one needs to check the following:

* If a list of points is given that they are torsion.

* If a polynomial of degree n is given that it divides the division_polynomial(2*n+1). Also the polynomial should be squarefree, i.e. define a reduced scheme.

Am I right ?

Why is the kernel_polynomial a multivariable polynomial ?

Also as an enhancement we could have simply an integer to get the multiplication by n as an isogeny. And for curves over QQ, a codomain=label (and the degree can be read off the isogeny_class matrix).


---

Comment by wuthrich created at 2009-06-26 17:00:50

OK. I will work on it and post a patch within the next week.
Chris.


---

Comment by wuthrich created at 2009-07-03 12:30:39

Moreover there is the following bug in the doctest:


```
sage: E = EllipticCurve(GF(31),[1,0,0,1,2])
sage: phi = E.isogeny([14,27,4,1])
sage: phi.degree()
7
sage: E.division_polynomial(7).factor()
(7) * (x^24 + 2*x^23  + ... +  15*x + 22)
```


in other words there can not be an isogeny of degree 7 defined over the ground field. The given polynomial is a factor of the 3-division polynomial. But it can not define an isogeny of degree 3 as the kernel would have 6 elements.


---

Comment by wuthrich created at 2009-07-03 16:32:55

Changing component from algebra to number theory.


---

Comment by wuthrich created at 2009-07-03 16:32:55

Changing keywords from "" to "elliptic curves, isogeny,".


---

Comment by wuthrich created at 2009-07-03 16:39:12

The patch was exported agains 4.1.alpha3.

In the end it took my quite a lot of work to correct this due to the (unnecessary) complexity of this file. I changed

* one can now give a single point or a list of points as the kernel argument. The isogeny has kernel generated by these points.
* it checks now if the points are torsion points and, when a polynomial is given, that it divides the correct division polynomial.
* and i changed the documentation slightly.


---

Comment by shumow created at 2009-07-16 06:56:01

So, over all, thanks for the thorough once over here.


Sorry I didn't look at this lately.  I have been very busy.  I work full time and I am finishing my master's thesis (which I wrote this class to do research for.)


I changed this to "needs work", not because it is necessarily bad, but because I want to discuss it more.


1)  I don't think you should remove the algorithm parameter, which defaults to none.  First off I was planning on adding another algorithm which is similar to the kohel from kernel polynomial variant, and that is the main reason why I had the parameter.  That, or someone smarter than me can come along and add a new algorithm, and add the parameter to make it easier to select the new version (or specify the old version for backward compatibility.)

2)  I am fine with taking the input as a point (or a pair of points) to specify the generators of the kernel.  However, I do not think that this should replace the kernel list way of doing things.  First off, it unnecessarily breaks backwards compatibility.  Second off, there was a very good reason that I did not initially do the solution that you have here, generating the list of input points from generators is quite slow.  Specifically, as you have it coded here, you end up doing n**2 work inflating the kernel list.  Now, if someone knows the list of points in the kernel, (or knows that the kernel is cyclic) they have no choice but to allow the init to run a quadratic complexity algorithm, when it would have otherwise been linear.  This actually becomes the slowest part of the isogeny computation.  I see no reason to not have this new way of doing input work alongside the old way.

3) When changing this to work side by side with the old way, obviously not all of the examples should be changed, as we still want to exercise the old way of doing things.


I think that your general modification here is good, however, I would like to switch this to work along side the old way of doing things.  By detecting the type of the input.  If you prefer I make the change, that is fine, but it will need to wait until I file my ms thesis, so after next week.


---

Comment by wuthrich created at 2009-07-20 15:38:52

Hi.

I agree that we may want to discuss this further ... and maybe eventually ask sage-nt for a vote on what should be done.

1) Currently the parameter 'algorithm' is of no use at all. As you can not force the algorithm to be 'kohel' when a list of point is given. So this option - in the current version - is totally obsolete and I am against carrying it around for nothing. If someone really wants to force things, he can always import the function and work directly with them. A user who wants to create an isogeny will never want to choose this. If ever you implement further algorithms, we can add it again without problem.

I agree that this "breaks" backward compatibility. But it is really nowhere used in sage and I do not think that any user apart from the two of us even noticed that it existed. I personally consider it a design error and not an option that we must keep compatible with. But other people may think differently about this.

2) The same goes for the compatibility issue here. We should not carry a wrong initial design with us for the rest of all times, if no one has ever used it.

On the other hand I agree with your speed arguement. I may be wrong, but I think no one will ever want to use this function with n as large as it would matter. In characteristic 0, the typical degree is hardly ever bigger than 10. Over finite fields, I would think that the usual way of using this function for large n would be through 'kohel', but I might be wrong. Anyway, I think that we should not worry about the eventual slow down. In most cases the subgroup is not computed previously to the use of this function. 

For both 1) and 2), I asked William Stein and David Kohel whether they would agree with changing this in Barcelona.

Chris.


---

Comment by davidloeffler created at 2009-07-20 19:50:08

Changing component from number theory to elliptic curves.


---

Comment by wuthrich created at 2009-08-20 12:09:47

I am updating here the patch. It is now based on sage-4.1.1 plus trac ticket #6672 .

Since nothing seems to happen with this patch and I continue to insist that it should go in as it is, I allow myself to switch back to 'needs review'. If any reviewer is against it for the reasons mentioned eralier, then I would propose that this ticket goes in (as it fixes some serious bugs) and that the changes are made later to it. I recall the main changes :

 * one can now give a single point or a list of points as the kernel argument. The isogeny has kernel generated by these points. 
 * it checks now if the points are torsion points and, when a polynomial is given, that it divides the correct division polynomial.
 * and it changes the documentation slightly.


---

Attachment

exported against 4.1.1 + patch #6672


---

Comment by cremona created at 2009-08-21 20:44:55

These are all things I wanted to change myself, after trying out the isogeny code, but I had not realised that it had been done.

I'll do a proper review within a day or so, promise.


---

Comment by shumow created at 2009-08-22 01:19:53

I agree that this fixes some issues, and is important.  However, as I said before, I do not think that we should totally replace being able to specify the full list of points in the kernel.  Rather, I think specifying the generators should work *in addition to* the full list of kernel points.  Using Velu's algorithm here is mainly for pedagogical reasons anyway, as specifying the kernel polynomial is computationally much simpler and easy.  And as using Velu's algorithm requires the input be the full list of points, I think this is a reasonable input.

I propose that we open new bugs for (1) the documentation issues that you fix and (2) an enhancement for being able to specify generators in addition to the full list of kernel points.

Overall, The fixes in this patch are good, there are just many fixes in a patch that don't really fix *this bug*


---

Comment by cremona created at 2009-08-22 11:56:35

I have just read through the above discussions.  I think that by far the most common way people will create isgenies from kernels will be either from a kernel polynomial (in which case there definitely should be a check, as Chris implemented, that the polynomial given does define a valid subgroup), or by giving a point generating a cyclic kernel.  So I'm with Chris on this one.  It is very easy to convert a pint P of order n to a list of points in the subgroup generated by P, just use list(multiples(P,n))  --multiples() returned an iterator.    It will be very rare for non-cyclic isogenies to be needed, with the single exception of the multiplication-by-m map which we can already create using the division_polynomial(m).

I don't think that backward compatibility is an important issue here, though I can see that it might be for Dan, since the isogeny code is so new, to the extent that I still consider it to be "beta" code, as I have not had a chance to use it much.

Dan, I cannot imagine it to be at all common for a user to have the points of a subgroup but not know the generator(s), so I think your comment about the complexity here is not a very serious one.

I will now spend some time testing the patch;  if I don't find any problems I'll give this a positive review.


---

Comment by cremona created at 2009-08-23 13:47:48

Here's the positive review.  I tried out the curve on a whole lot of examples.

If there is still disagreement we could try for a vote on sage-devel or sage-nt!


---

Comment by mvngu created at 2009-08-24 00:57:37

Possible typo in the patch that touches `sage/schemes/elliptic_curves/ell_curve_isogeny.py`:

```
4036	    - ``E2``        - an elliptic curve in short wWeierstrass form. 
```

It should be "Weierstrass" instead of "wWeierstrass".


---

Attachment

reviewer patch; apply after previous one


---

Comment by mvngu created at 2009-08-24 04:53:13

The patch `trac_6384-reviewer.patch` fixes the reported typo. It should be applied after `trac_6384.patch`.


---

Comment by mvngu created at 2009-08-24 05:20:16

Resolution: fixed


---

Comment by mvngu created at 2009-08-24 05:20:48

Merged both patches.


---

Comment by cremona created at 2009-09-04 08:59:41

See #6886 for an undesirable side-effect of the checking introduced here!
