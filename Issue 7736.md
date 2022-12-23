# Issue 7736: factor returns a reducible factor,

Issue created by migration from https://trac.sagemath.org/ticket/7736

Original creator: syazdani

Original creation time: 2009-12-18 20:22:06

Assignee: tbd

CC:  wuthrich was

Here is a result that confuses me (appologies for not having a simpler example for this):

```
sage: E = EllipticCurve('1728z');
sage: Et = E.mod5family();
sage: f=Et.discriminant().numerator().factor()[0][0];
sage: K.<alpha> = NumberField(f);
sage: f.change_ring(K).factor()[1][0].is_irreducible()
False
```

Here f turns out to be a degree 12 polynomial, and when you factor it over K, you get a linear factor and a degree 11 factor. However, degree 11 factor in this case is not irreducible. In fact, if you continue with

```
sage: g = f.change_ring(K).factor()[1][0];
sage: g.factor()
```

you get a linear factor and a degree 10 factor, where both are irreducible.


---

Comment by was created at 2009-12-18 23:11:20

Ultimately factorization over number fields are done by PARI.  Looking at g.factor?? you see that the factorization is ultimately handled by PARI after some manipulations to account for denominators in the defining polynomial for the number field.  So it's likely that the bug is actually in PARI.   But we'll see.  If I were debugging this I would put some print statements in the factor function to see exactly what is passed off to pari and see if pari is buggy.  If so, report upstream, after trying the latest svn version.

William


---

Comment by was created at 2009-12-19 04:35:22

This might be the same as #7097?


---

Comment by cremona created at 2010-02-11 15:59:07

Changing assignee from tbd to cremona.


---

Comment by cremona created at 2010-02-11 15:59:07

It may well be that the short-term fix I put in at #7097 is not yet good enough.  [It is short-term since the latest version of pari have fixed some bugs which arose for non-monic polynomials, which is why the patch  I put in at #7097 made sure that pari was only called to factor monic ones.]

I just had a possibly worse example, and found this ticket while looking to see if I should open a new one:

```
sage: E = EllipticCurve('4900a2')
sage: f = E.division_polynomial(9)
sage: K3.<z> = CyclotomicField(3)
sage: ff = f.change_ring(K3)
sage: ff.degree()
40
sage: [g.degree() for g,e in ff.factor()]
[1, 3, 9, 40]
```

I factor a degree 40 polynomial and the returned factors have degrees 1,3,9,40!
Even if I make the polynomial monic (above it has leading coefficient 9) it is no better:

```
sage: x = f.parent().gen()
sage: g = 9^39 * f(x/9)
sage: all([c.is_integral() for c in g.coefficients()])
True
sage: [h.degree() for h,e in g.change_ring(K3).factor()]
[1, 3, 9, 40]
```



---

Comment by mhansen created at 2010-03-06 06:24:38

There's an SPKG for the new PARI at #8453 which fixes John's problem, but not the one reported in the summary.


---

Comment by cremona created at 2010-06-26 21:10:44

The following script confirms that all is well using either nffactor() or factornf() in 

```

                   GP/PARI CALCULATOR Version 2.4.3 (development svn-12471)
                  i686 running linux (ix86/GMP-4.2.2 kernel) 32-bit version
                   compiled: Jun 25 2010, gcc-4.2.4 (Ubuntu 4.2.4-1ubuntu4)
                        (readline v5.2 enabled, extended help enabled)
```

(latest svn pari version as of 2010-06-26):

```

f = t^12 + 4811804/1884237*t^11 + 501578/1884237*t^10 + 649220/50874399*t^9 + 14465/50874399*t^8 - 12232/152623197*t^7 - 52756/1373608773*t^6 - 8536/4120826319*t^5 - 605/12362478957*t^4 - 220/333786931839*t^3 - 22/1001360795517*t^2 - 4/1001360795517*t - 1/27036741478959

fm = t^12 + 69044128098228*t^11 + 194586025985656552389748914*t^10 + 252206133278375846620611910363960279620*t^9 + 151927551892320463602482158314423242534005837551135*t^8 - 1157840316800177898179502977396915725886340880517554037247717144*t^7 - 15001507175768040071414348254147174918292469313307008195125210400587831506052*t^6 - 21875124557509546030610056365629827329300918240857885825522849089306079707691831828411736*t^5 - 13972837118332351426055337318528492766817006355033884326778630955066105801586929451124705565427318065*t^4 - 5087945924524636104869811628561988778476675586778609071619493774225875340654682413166396849224980548949885496220*t^3 - 4585382620676520885033637329085293361766727857705544672584084201955286189767281537555363181449203944664777829514827546801166*t^2 - 22540691726789566284791090059861226369539881229945431559159210204846754832348501703584277353410422860328945842151249543476507386971939308*t - 5642841249760365128848452030124057197006418321418963437144886094595692736999089907821045425216157097104588947199646188372804628704737026803780620559

d =  27036741478959
subst(fm,t,t*d) == f*d^12

F = nfinit(fm);
fmfac = nffactor(F,subst(fm,t,x));
matsize(fmfac) == [3,2]
vector(3,j,poldegree(fmfac[j,1])) == [1,1,10] 


ffac = nffactor(F,subst(f,t,x));
matsize(ffac) == [3,2]
vector(3,j,poldegree(ffac[j,1])) == [1,1,10]

allocatemem()
allocatemem()
allocatemem()
fmfac2 = factornf(subst(fm,t,x),fm)
matsize(fmfac2) == [3,2]
vector(3,j,poldegree(fmfac2[j,1])) == [1,1,10]

ffac2 = factornf(subst(f,t,x),fm);
matsize(ffac2) == [3,2]
vector(3,j,poldegree(ffac2[j,1])) == [1,1,10] 
```


Explanation:  fm is f made monic and integral which is required for construction of number fields.  We check that both f and fm factor correctly over the number field defined by f (which we have to construct using fm): factors have degrees 1,1,10.  Note that we have to change variables before factoring, otherwise we get an error;  and that the factornf functions require more than the default memory allocation.

This is good news since right now a few feet from me William and Robert B are spending the day making this version of pari into an new spkg (see #9343).


---

Comment by cremona created at 2010-06-26 21:10:44

Changing keywords from "" to "number field pari".


---

Comment by was created at 2010-06-27 06:34:22

I have now checked that the work at #9343 completely fixes this bug.  So when that goes in, this can be changed.


---

Comment by jdemeyer created at 2010-09-08 08:26:26

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2010-09-08 08:26:32

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-10 10:49:55

Resolution: duplicate


---

Comment by mpatel created at 2010-09-10 10:49:55

I assume this is still fixed by #9343.  If not, please reopen this.


---

Comment by cremona created at 2010-09-11 16:19:19

Replying to [comment:10 mpatel]:
> I assume this is still fixed by #9343.  If not, please reopen this.

It is still fixed:  all the examples in this ticket work fine with 4.6.alpha0.
