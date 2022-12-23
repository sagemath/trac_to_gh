# Issue 4525: [with patch, needs review] LLL-reduction of elliptic curve bases (with resulting speed enhancement to integral_points())

Issue created by migration from https://trac.sagemath.org/ticket/4525

Original creator: cremona

Original creation time: 2008-11-14 17:36:47

Assignee: was

CC:  tnagel mardaus

Keywords: elliptic curve

The integral_points() function for elliptic curves can be speeded up if the Mordell-Weil basis used is first LLL-reduced, since this increases the minimal eigenvalue of the height-pairing matrix.  The patch achieves this.  For example, before:

```
sage: E = EllipticCurve([0, 1, 1, -2, 42])
sage: E.gens()
[(-4 : 1 : 1), (-3 : 5 : 1), (-11/4 : 43/8 : 1), (-2 : 6 : 1)]
sage: time len(E.integral_points())
CPU times: user 42.67 s, sys: 0.48 s, total: 43.15 s
Wall time: 43.50 s
24
```

and after:

```
sage: E = EllipticCurve([0, 1, 1, -2, 42])
sage: E.gens()
[(-4 : 1 : 1), (-3 : 5 : 1), (-11/4 : 43/8 : 1), (-2 : 6 : 1)]
sage: time len(E.integral_points())
CPU times: user 8.18 s, sys: 0.12 s, total: 8.29 s
Wall time: 8.37 s
24
```

(i.e. speedup by a factor of 5) and for a rank 5 example I had a speedup factor of 50.

I implemented the LLL-reduction via pari's lllgram function, in a separate function lll_reduce() since it will be useful elsewhere.  There is a case for applying it whenever we compute generators (since, for example, mwrank does not LLL-reduce its generators, because the mwrank code has no access to a floating point LLL routine!) but I have not done that -- many doctest would need changing as generators would change.

The doctests include a long one on a curve of rank 24, which adds 2m to the -long doctest time.  If that is too long it could be deleted.


---

Attachment


---

Comment by malb created at 2008-11-15 11:27:30

> I implemented the LLL-reduction via pari's lllgram function

Is there any particular reason you are not using Sage's fpLLL based LLL reduction? It is (supposed to be) much faster, but maybe the speed of the LLL is negligible for your application? Just curious.


---

Comment by cremona created at 2008-11-15 12:46:29

Replying to [comment:1 malb]:
> > I implemented the LLL-reduction via pari's lllgram function
> 
> Is there any particular reason you are not using Sage's fpLLL based LLL reduction? It is (supposed to be) much faster, but maybe the speed of the LLL is negligible for your application? Just curious.
> 
Unless I am mistaken, fpLLL only works on *integer* matrices, where the input is a basis for the lattice.  The same is true of NTL's LLL code.  What we need here is LLL on a lattice given only the real (floating point) gram matrix;  there is no underlying integer lattice.

It's the same reason why reduced_basis() for number fields uses pari, and also why mwrank does not LLL-reduce its bases in the first place!


---

Comment by malb created at 2008-11-15 12:56:51

Replying to [comment:2 cremona]:
> Unless I am mistaken, fpLLL only works on *integer* matrices, where the input is a basis for the lattice.  The same is true of NTL's LLL code.  What we need here is LLL on a lattice given only the real (floating point) gram matrix;  there is no underlying integer lattice.
> 
> It's the same reason why reduced_basis() for number fields uses pari, and also why mwrank does not LLL-reduce its bases in the first place!

You are 100% right. Sorry for the noise, I should have checked.


---

Attachment

The second patch 10903.patch implements another speedup, in the function integral_points_with_bounded_mw_coefficients(), which I have moved outside the integral_points() function (mainly for ease of testing).  We still loop through all relevant linear combinations as real points, but instead of computing each linear combo from scratch we do so in a more incremental way, since most of the time we get the next combo by adding a single point.

Apply after the previous patch.  Timings:

rank 3 [0,0,1,-7,6] : old 0.33s, new 0.16s

rank 4 [0,0,1,-7,36]: old 15.4s, new 4.24s

rank 5 [0,0,1,-79,342]: old 273s, new 64s

with presumably even better factors for larger examples.  (I still have not completed a rank 8 example, but one day I will!).

By the way, for that rank 5 example I had to find the gens first with "proof=False" and then manually use E._set_rank() and E._set_gens().  We might want to add the proof flag to integral points, just to apply to the MW basis part of the computation.

PS Since I moved the function it is not so easy to see what has changed, sorry.  Basically the old lines 4228-4242 are replaced by the new lines 4491-4526.


---

Attachment


---

Comment by cremona created at 2008-11-22 17:17:05

Changing type from enhancement to defect.


---

Comment by cremona created at 2008-11-22 17:17:05

New patch 10984.patch fixes a bug whereby integral points of the form P+T where P is integral and with small x, and T is torsion, were missed.  Example:  in vanilla 3.2:

```
sage: E = EllipticCurve([0,0,0,-1131^2,0])
sage: [P[0] for P in E.integral_points()]
[-1131, -117, 0, 1131, 1392]
```

misses x=10933.  After the patch:

```
sage: E = EllipticCurve([0,0,0,-1131^2,0])
sage: [P[0] for P in E.integral_points()]
[-1131, -117, 0, 1131, 1392, 10933]
```


The funny thing is that I only ran this curve to check a claim made in "	Solving the Diophantine equation y2=x(x2−n2)" by Konstantinos Draziotis, Dimitrios Poulakis which just appeared in Volume 129, Issue 1, Pages 102-121 (January 2009) of the Journal of Number theory;  in that paper they miss x=1392!

I guess this should have been a new ticket, but all three patches affect the same function and no-one has reviewed them yet anyway...


---

Attachment

this should replace the patch right above this one, which wouldn't apply cleanly for me.


---

Comment by was created at 2008-11-23 08:23:08

> The funny thing is that I only ran this curve to check a claim made in " Solving 
> the Diophantine equation y2=x(x2−n2)" by Konstantinos Draziotis, Dimitrios Poulakis
> which just appeared in Volume 129, Issue 1, Pages 102-121 (January 2009) of 
> the Journal of Number theory; in that paper they miss x=1392! 

That's an extremely bizarre coincidence!!!!!!!  What did those guys use to get the wrong answer?  Magma finds 1392.


---

Comment by was created at 2008-11-23 08:25:22

fix some numerical noise issues (part of refereeing)


---

Attachment

OK, this looks good, but it introduces a *BUG*:
We have in sage-3.2 released:

```
was@sage:~/www/talks$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.2, Release Date: 2008-11-20                         |
| Type notebook() for the GUI, and license() for information.        |
sage: EllipticCurve('91b1').integral_points()
[(-1 : 3 : 1), (1 : 0 : 1), (3 : 4 : 1)]
```


However, after applying these patches, I get:

```
EllipticCurve('91b1').integral_points()
Traceback (click to the left for traceback)
...
ValueError: No point with x-coordinate 0 on Elliptic Curve defined by
y^2 + y = x^3 + x^2 - 7*x + 5 over Rational Field
```


I found with the following handy script, which anybody who ever works on the integral points code should always consider running:

```
for e in cremona_curves([1..100]):
    t = cputime(); i = len(e.integral_points()); t = cputime(t)
    t2 = magma.cputime(); j = len(magma(e).IntegralPoints()); t2 = magma.cputime(t2)
    print e.cremona_label(), i, j, t, t2
    assert i == j
```


Also, the curve 112a2 also gives the same error.


** One weird thing I noticed using the script is that for the elliptic curve 102b5, magma takes 3.88 seconds to find all the integral points, and sage takes 0.004
102b5 0 0 0.004 3.88.


---

Comment by mabshoff created at 2008-11-23 09:26:01

Hi guys,

no need to add anyone's email address to the CC field. In case someone has a trac id it is sufficient to add it to the CC field, i.e. the address cannot be harvested by spammers in that case. 

Cheers,

Michael


---

Comment by cremona created at 2008-11-23 10:45:52

Sorry about my 3rd patch being based wrongly.  I'll look into the new bug (thanks for finding it).  I'm a bit embarrassed -- when we first released this code we tested it very thoroughly, but I have not repeated those tests after making changes.  As William says, we should do this every time.

About the email addresses:  we ordinary mortals do not have a list of trac account names, so it can be impossible to add people in the way Michael recommends!  If that happens to me again, I'll add a comment asking for such-and-such a person to be added (if i don't know their trac a/c name) and hope that Michael picks it up ;)


---

Comment by mabshoff created at 2008-11-23 10:52:13

Replying to [comment:11 cremona]:
> Sorry about my 3rd patch being based wrongly.  I'll look into the new bug (thanks for finding it).  I'm a bit embarrassed -- when we first released this code we tested it very thoroughly, but I have not repeated those tests after making changes.  As William says, we should do this every time.

Yes, I would certainly welcome optional and long tests comparing the output from Sage's implementation to Magma's. We could even introduce a new category  "#very long ?" in case those tests would burn more than 10 minutes of CPU time. The more automated regression testing there is the better we will be off. Sage 3.2.1 will contain a feature --only-optional where one can test only the Magma related doctests for example. 

> About the email addresses:  we ordinary mortals do not have a list of trac account names, so it can be impossible to add people in the way Michael recommends!  If that happens to me again, I'll add a comment asking for such-and-such a person to be added (if i don't know their trac a/c name) and hope that Michael picks it up ;)

Maybe we should make a list in the wiki mapping real names to trac accounts?

Cheers,

Michael


---

Attachment

Replaces ALL earlier patches combined


---

Comment by cremona created at 2008-11-23 15:58:20

The new patch trac-4525-combined.patch  replaces all earlier ones by combining them, and also fixes the bug William found (fix due to Tobias) with an associated doctest.  I checked all was well for curves in the database up to conductor about 170.

The patch is based on 3.2 (since I have not yet built any 3.2.1s).  Tested on 32- and 64-bit linux.

Remarks on testing (especially against Magma):  (1) unless you have a very recent version of Magma the Magma output may sometimes be wrong (from x-coordinates repeated to crashes).  (2) For small examples like this most of the time is spent finding the MW basis.  For better time comparisons you should (a) use the optional database, which includes generators, in Sage and (b) precompute the generators in Magma medfore asking for the integral points.  I did this before the initial release of the code, and one day I'll do it again.


---

Comment by was created at 2008-11-23 19:45:24

John -- idle thought -- how hard would it be for you to have a fairly compressed cache included as part of mwrank that would make it so all mwrank data is precomputed for curves of conductor up to some bound?  That would make mwrank instant on say all curves of conductor up to 10,000 or 100,000 or something, depending on how compressed you could make this...  Could be interesting.


---

Comment by was created at 2008-11-23 20:33:48

I strongly recommend adding this as a doctest.  It takes 11 seconds without database_cremona, and about 2.5 seconds with, so should be marked #long, probably:

sage: [len(e.integral_points(both_signs=False)) for e in cremona_curves([1..100])]  # long
[2, 0, 2, 3, 2, 1, 3, 0, 2, 4, 2, 4, 3, 0, 0, 1, 2, 1, 2, 0, 2, 1, 0, 1, 3, 3, 1, 1, 4, 2, 3, 2, 0, 0, 5, 3, 2, 2, 1, 1, 1, 0, 1, 3, 0, 1, 0, 1, 1, 3, 6, 1, 2, 2, 2, 0, 0, 2, 3, 1, 2, 2, 1, 1, 0, 3, 2, 1, 0, 1, 0, 1, 3, 3, 1, 1, 5, 1, 0, 1, 1, 0, 1, 2, 0, 2, 0, 1, 1, 3, 1, 2, 2, 4, 4, 2, 1, 0, 0, 5, 1, 0, 1, 2, 0, 2, 2, 0, 0, 0, 1, 0, 3, 1, 5, 1, 2, 4, 1, 0, 1, 0, 1, 0, 1, 0, 2, 2, 0, 0, 1, 0, 1, 1, 4, 1, 0, 1, 1, 0, 4, 2, 0, 1, 1, 2, 3, 1, 1, 1, 1, 6, 2, 1, 1, 0, 2, 0, 6, 2, 0, 4, 2, 2, 0, 0, 1, 2, 0, 2, 1, 0, 3, 1, 2, 1, 4, 6, 3, 2, 1, 0, 2, 2, 0, 0, 5, 4, 1, 0, 0, 1, 0, 2, 2, 0, 0, 2, 3, 1, 3, 1, 1, 0, 1, 0, 0, 1, 2, 2, 0, 2, 0, 0, 1, 2, 0, 0, 4, 1, 0, 1, 1, 0, 1, 2, 0, 1, 4, 3, 1, 2, 2, 1, 1, 1, 1, 6, 3, 3, 3, 3, 1, 1, 1, 1, 1, 0, 7, 3, 0, 1, 3, 2, 1, 0, 3, 2, 1, 0, 2, 2, 6, 0, 0, 6, 2, 2, 3, 4, 6, 5, 1, 0, 6, 1, 0, 3, 1, 1, 2, 3, 1, 2, 1, 1, 0, 1, 0, 1, 0, 5, 5, 2, 2, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1]

I believe the output numbers are right.  Two of them disagree with magma (that 92 example), but in those two cases magma is wrong, as you mention above.

Positive review (but please add the above doctest).


---

Attachment

Replace previous one with this


---

Comment by cremona created at 2008-11-23 21:11:38

Replying to [comment:15 was]:
> I strongly recommend adding this as a doctest.  It takes 11 seconds without database_cremona, and about 2.5 seconds with, so should be marked #long, probably:
> 
> sage: [len(e.integral_points(both_signs=False)) for e in cremona_curves([1..100])]  # long
> [2, 0, 2, 3, 2, 1, 3, 0, 2, 4, 2, 4, 3, 0, 0, 1, 2, 1, 2, 0, 2, 1, 0, 1, 3, 3, 1, 1, 4, 2, 3, 2, 0, 0, 5, 3, 2, 2, 1, 1, 1, 0, 1, 3, 0, 1, 0, 1, 1, 3, 6, 1, 2, 2, 2, 0, 0, 2, 3, 1, 2, 2, 1, 1, 0, 3, 2, 1, 0, 1, 0, 1, 3, 3, 1, 1, 5, 1, 0, 1, 1, 0, 1, 2, 0, 2, 0, 1, 1, 3, 1, 2, 2, 4, 4, 2, 1, 0, 0, 5, 1, 0, 1, 2, 0, 2, 2, 0, 0, 0, 1, 0, 3, 1, 5, 1, 2, 4, 1, 0, 1, 0, 1, 0, 1, 0, 2, 2, 0, 0, 1, 0, 1, 1, 4, 1, 0, 1, 1, 0, 4, 2, 0, 1, 1, 2, 3, 1, 1, 1, 1, 6, 2, 1, 1, 0, 2, 0, 6, 2, 0, 4, 2, 2, 0, 0, 1, 2, 0, 2, 1, 0, 3, 1, 2, 1, 4, 6, 3, 2, 1, 0, 2, 2, 0, 0, 5, 4, 1, 0, 0, 1, 0, 2, 2, 0, 0, 2, 3, 1, 3, 1, 1, 0, 1, 0, 0, 1, 2, 2, 0, 2, 0, 0, 1, 2, 0, 0, 4, 1, 0, 1, 1, 0, 1, 2, 0, 1, 4, 3, 1, 2, 2, 1, 1, 1, 1, 6, 3, 3, 3, 3, 1, 1, 1, 1, 1, 0, 7, 3, 0, 1, 3, 2, 1, 0, 3, 2, 1, 0, 2, 2, 6, 0, 0, 6, 2, 2, 3, 4, 6, 5, 1, 0, 6, 1, 0, 3, 1, 1, 2, 3, 1, 2, 1, 1, 0, 1, 0, 1, 0, 5, 5, 2, 2, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1]
> 
> I believe the output numbers are right.  Two of them disagree with magma (that 92 example), but in those two cases magma is wrong, as you mention above.
> 
> Positive review (but please add the above doctest).

Done in trac-4525-combined-2.patch which *replaces* trac-4525-combined.patch .


---

Comment by mabshoff created at 2008-11-23 23:50:49

Merged trac-4525-combined-2.patch in Sage 3.2.1.alpha1


---

Comment by mabshoff created at 2008-11-23 23:50:49

Resolution: fixed
