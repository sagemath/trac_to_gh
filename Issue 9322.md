# Issue 9322: bug in simon_two_descent for elliptic curves

Issue created by migration from https://trac.sagemath.org/ticket/9322

Original creator: cremona

Original creation time: 2010-06-24 03:00:39

Assignee: AlexGhitza

CC:  wuthrich jeremywest

[NB This is a different bug from the one on #5153]

Chris Wuthrich reports:

```
sage: K.<w> = NumberField(x^2-x-232)
sage: E = EllipticCurve([2-w,18+3*w,209+9*w,2581+175*w,852-55*w])
sage: E.local_data()
[]
sage: E.simon_two_descent(verbose=2)
booom.
```


The same example runs fine in gp using the same version of the script ell.gp that Sage has (in version 4.4.4) and the same version of gp.


---

Comment by cremona created at 2010-06-24 03:02:59


```

john@ubuntu%sage -gp
                  GP/PARI CALCULATOR Version 2.3.5 (released)
...

? bnf=bnfinit(y^2-y-232);
? w=Mod(y,y^2-y-232)
%8 = Mod(y, y^2 - y - 232)
? e=ellinit([2-w,18+3*w,209+9*w,2581+175*w,852-55*w]);
? bnfellrank(bnf,e)
courbe elliptique : Y^2 = x^3 + Mod(9*y + 308, y^2 - y - 232)*x^2 + Mod(1200*y + 27936, y^2 - y - 232)*x + Mod(57968*y + 1054096, y^2 - y - 232)
points triviaux sur la courbe = [[1, 1, 0]]
#S(E/K)[2]    = 4
#E(K)/2E(K)  >= 1
#III(E/K)[2] <= 4
rang(E/K)    >= 0
listpointsmwr = []
%10 = [0, 2, []]
```



---

Comment by jeremywest created at 2010-07-01 06:32:20

Changing status from new to needs_work.


---

Comment by jeremywest created at 2010-07-01 06:32:20

I also noticed this same problem, although it seems to be nearly ubiquitous for number fields. I found it for several quadratic and cubic extensions as well as for a degree seven extension. For one I got an index out of bounds error which I believe originates because gp does not hand back the results expected by the sage script. For the rest I found that the sage script was attempting to coerce a point from one curve to another and it reports that the point does not lie on the curve.

Unfortunately, I don't currently have access to sage so I am unable to report line numbers. The problem occurs in sage/schemes/elliptic_curves/gp_simon.py near the bottom of the only function defined.


---

Comment by jeremywest created at 2010-07-01 06:32:20

Changing component from algebra to elliptic curves.


---

Comment by cremona created at 2011-03-25 04:47:29

With 4.7.alpha1 this works fine:

```
sage: K.<w> = NumberField(x^2-x-232)                                   
sage: E = EllipticCurve([2-w,18+3*w,209+9*w,2581+175*w,852-55*w])      
sage: E.local_data()                                                   
[]
sage: E.simon_two_descent()                                      
(0, 2, [])
```

but after #11005 (which updates to a newer version of Simon's GP scripts) we run into an infinite loop:

```
 **** Warning: doubling the real precision in nfsign_s **** 76
 **** Warning: doubling the real precision in nfsign_s **** 152
 **** Warning: doubling the real precision in nfsign_s **** 76
 **** Warning: doubling the real precision in nfsign_s **** 152
 **** Warning: doubling the real precision in nfsign_s **** 76
```

which I will test on a stand-alone gp and report upstream.


---

Comment by cremona created at 2011-03-25 04:47:29

Changing keywords from "" to "Simon".


---

Comment by cremona created at 2011-03-25 04:47:29

Changing status from needs_work to needs_info.


---

Comment by cremona created at 2011-03-25 04:54:02

Changing status from needs_info to needs_work.


---

Comment by cremona created at 2011-03-25 04:54:02

Running under gp directly:

```
? K = bnfinit(y^2 - y - 232);
? a = Mod(y,K.pol);
? bnfellrank(K, [-a + 2,3*a + 18,9*a + 209,175*a + 2581,-55*a + 852])
courbe elliptique : Y^2 = x^3 + Mod(9*y + 308, y^2 - y - 232)*x^2 + Mod(1200*y + 27936, y^2 - y - 232)*x + Mod(57968*y + 1054096, y^2 - y - 232)
points triviaux sur la courbe = [[1, 1, 0]]
#S(E/K)[2]    = 4
#E(K)/2E(K)  >= 2
#III(E/K)[2] <= 2
rang(E/K)    >= 1
 III devrait etre un carre, donc 
#E(K)/2E(K)  = 4
#III(E/K)[2] = 1
rang(E/K)    = 2
listpointsmwr = [[Mod(-35/4*y - 186, y^2 - y - 232), Mod(-21/8*y - 37, y^2 - y - 232)]]
%71 = [2, 2, [[Mod(-35/16*y - 93/2, y^2 - y - 232), Mod(-1727/64*y - 2531/8, y^2 - y - 232)]]]
```

we get instant success.  Also with the gp2c-compiled version.  So it is *not* an upstream problem,and one which should be solvable within Sage.


---

Comment by zimmerma created at 2011-09-14 15:59:09

I've been struggling with that bug for a few hours, and have made only little progress.
With Sage 4.7.1 and Pari 2.4.3 (development), I've noticed that Pari 2.4.3 and the version of Pari within Sage differ at `bbnf = bnfinit(rnfeq[1],1)` in `ell.gp`, where
`rnfep[1] = x^6 + 625*x^5 + 135916*x^4 + 14984560*x^3 + 914453072*x^2 + 29502178560*x + 392635160576`.

Pari 2.4.3 returns `bbnf: [Mat(2), Mat([0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, ...` whereas
Pari within Sage returns `bbnf: [Mat(2), Mat([0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, ...`

However I don't know if `bnfinit` should be deterministic...

Paul


---

Comment by zimmerma created at 2011-09-15 15:25:59

is there a way to get the output of the print commands from the ell.gp script
when it is called from within Sage? Even with a large value of DEBUGLEVEL_ell, the output
of those print statements does not appear in the Sage session, thus it is difficult to debug.

Paul


---

Comment by cremona created at 2011-09-15 15:50:57

Replying to [comment:6 zimmerma]:
> is there a way to get the output of the print commands from the ell.gp script
> when it is called from within Sage? Even with a large value of DEBUGLEVEL_ell, the output
> of those print statements does not appear in the Sage session, thus it is difficult to debug.
> 
> Paul

You can get a whole gp session logged to a file by setting gp=Gp(logfile=foobar.txt').  But the code in gp-simon.py creates its own gp instance without using the logfile option.  In the short term, edit line 38 of sage/sage/schemes/elliptic_curves/gp-simon.py to add the logfile option.  A better long-term solution would be to have a logfile parameter to the two-descent function itself and pass that on.

By the way, there are new version of Simon's scripts which in Sage Days in March (6 months ago!) I got working in a better way, using gp2c to convert to C code.  There was some reason which I now cannot remember why there was a delay in getting this merged, and after 6 months I fear that the patches we made then would no longer work.  Damn.  Anyway, I strongly suggest if you have problem cases that you run the curves directly through ell.gp (outside Sage) using the newest version of ell.gp from Simon's web page, since you may be seeing a problem which has already been fixed.


---

Comment by zimmerma created at 2011-09-16 10:18:42

thank you John for your advice. After trying it, I figured out that with Sage 4.7.1 on my laptop
in fact the example in the description actually works, but takes about 2.5 minutes, during which
top reports that the gp process takes 100% of the cpu time, while evaluating the command

```
ans=bnfellrank(K, [-a + 2,3*a + 18,9*a + 209,175*a + 2581,-55*a + 852]);;
```

Can someone else confirm? Maybe a problem in the Sage-gp interface?
What should we do with that ticket?

Paul


---

Comment by zimmerma created at 2011-09-16 10:18:42

Changing status from needs_work to needs_info.


---

Comment by zimmerma created at 2011-09-16 14:56:50

Changing keywords from "Simon" to "Simon ecc2011".


---

Comment by zimmerma created at 2011-09-16 14:56:50

ok, I found where the problem comes from. In the file `ellQ.gp` which is also loaded by the
`gp_simon.py` file, the global constants `LIM1, LIM3, LIMTRIV` have different values than
in `ell.gp`, respectively 5, 50, 50 instead of 2, 4, 2.

The slow behaviour can be reproduced with `sage -gp` if one reads both `ell.gp`
*and* `ellQ.gp`. If one only reads `ell.gp`, it is fast. Apparently `ellQ.gp` is not
needed for this computation.

Moreover the default values in Sage are again different: 5, 50, 10.

With 5, 5, 10 it takes only 1.45s (wall clock time) on my laptop.
With 5, 10, 10 it takes 2.19s.
With 5, 20, 10 it takes 11.63s.

Note that those values should be modified both in `ell_number_field.py` and in
`gp_simon.py` (the former function is critical in this example).

One should also share the default values for `lim1, lim3, limtriv` between the
`simon_two_descent` functions in `ell_number_field.py` and `gp_simon.py`.

Paul


---

Comment by cremona created at 2011-09-26 09:14:10

In the other ticket on this we changed Simon's scripts so that the use of these "environment variables" for passing configuration parameters was replaced by actual parameters to the functions (with default values).  So this problem should go away then.  We also persuaded Simon not to have the same function name for different functions in his various script files (he even had the same name for two different an incompatible versions of functions to do the same thing!).


---

Comment by chapoton created at 2013-09-21 12:28:36

Changing keywords from "Simon ecc2011" to "simon_two_descent ecc2011".


---

Comment by pbruin created at 2014-02-11 20:00:49

After applying #11005 (upgrade Simon's script to the latest version), rather than running for a long time, this example now gives an error similar to #15483:

```
sage: K.<w> = NumberField(x^2-x-232)
sage: E = EllipticCurve([2-w,18+3*w,209+9*w,2581+175*w,852-55*w])
sage: E.local_data()
[]
sage: E.simon_two_descent()
Traceback (most recent call last):
...
RuntimeError: 
  ***   at top-level: ans=bnfellrank(K,[-a+2,3
  ***                     ^--------------------
  ***   in function bnfellrank: ...eqtheta,rnfeq,bbnf];rang=
  ***   bnfell2descent_gen(b
  ***   ^--------------------
  ***   in function bnfell2descent_gen: ...und,r=nfsqrt(nf,norm(zc))
  ***   [1];if(DEBUGLEVEL_el
  ***   ^--------------------
  ***   array index (1) out of allowed range [none].
An error occurred while running Simon's 2-descent program
```

With the fix I just made at #15483, it again gives the correct result, but after a long time.


---

Comment by pbruin created at 2014-02-12 16:55:29

In principle it is not a bug if Sage uses different default values than Simon's script for the various parameters (`lim1`, `lim3`, `limtriv` and the more technical `maxprob` and `limbigprime`).  The defaults should be sensible, of course.  I guess we should find out if there is a good reason to use different defaults, and if so, what settings would be reasonable.


---

Comment by mmasdeu created at 2014-03-25 18:14:59

Is there a good reason to not use the default values that pari is using? What is troubling is that an example that runs fast in pari does take forever in Sage. So I would put the defaults to None, and then pass different defaults when the curve is over QQ or over a number field (according to DS's scripts).

One exception to this: the parameter `limbigprime` should be set to 0, to avoid the use of probabilistic (and thus not provably true) prime testing.


---

Comment by pbruin created at 2014-03-25 19:41:15

Replying to [comment:17 mmasdeu]:
> So I would put the defaults to None, and then pass different defaults when the curve is over QQ or over a number field (according to DS's scripts).
> 
> One exception to this: the parameter `limbigprime` should be set to 0, to avoid the use of probabilistic (and thus not provably true) prime testing.
Agree with all of this.


---

Comment by mmasdeu created at 2014-03-26 13:35:53

I have implemented the above suggestions. However, it seems that the using limbigprime=0 raises errors (I found them when using gp directly) and so I have currently set it to 30 (DS's default).

When simon_two_descent() is called with default arguments, the infinite-order points change (this is expected). I have checked that the answer is still correct (in particular, the rank bounds are the same), and changed the doctests (which affected four files in total).

Now the doctests pass for everything in the schemes/elliptic_curves folder, but I haven't run all the others.
----
New commits:


---

Comment by mmasdeu created at 2014-03-26 13:35:53

Changing status from needs_info to needs_review.


---

Comment by pbruin created at 2014-03-26 14:15:29

Changing status from needs_review to needs_work.


---

Comment by pbruin created at 2014-03-26 14:15:29

Merged with development branch.  There are some doctest failures, one of which seems to be non-trivial (reported rank changing from 1 to 0).


---

Comment by pbruin created at 2014-03-26 14:20:43

The failing example is the new doctest from #16009 in `gp_simon.py`; it now returns `(0, 0, [])`.

```
sage: F.<a> = QuadraticField(29)
sage: x = QQ['x'].gen()
sage: K.<b> = F.extension(x^2-1/2*a+1/2)
sage: E = EllipticCurve(K,[1, 0, 5/2*a + 27/2, 0, 0])
sage: E.simon_two_descent(lim1=2, limtriv=3)
(1, 1, [((-369/50*a - 1987/50)*b + 539/50*a + 2897/50 : (-27193/250*a - 146439/250)*b + 39683/250*a + 213709/250 : 1)])
```

This is reproducible inside `gp` (2.5.x) with the current version of Simon's script (as included in Sage since #11005):

```
K = bnfinit(y^4 + y^2 - 7);
a = Mod(y, K.pol);
E = [1, 0, 5*a^2 + 16, 0, 0];
LIM1 = 2;
LIMTRIV = 3;
bnfellrank(K, E)
```

This returns `[0, 0, []]`.


---

Comment by git created at 2014-03-27 14:19:20

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by pbruin created at 2014-03-27 14:22:36

Merged #16009 and indirectly #16022, and fixed the two remaining doctest failures.  No other unexpected things, so I think this can safely be regarded as a reviewer patch.


---

Comment by pbruin created at 2014-03-27 14:22:36

Changing status from needs_work to positive_review.


---

Comment by git created at 2014-03-28 18:43:18

Changing status from positive_review to needs_review.


---

Comment by git created at 2014-03-28 18:43:18

Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:


---

Comment by git created at 2014-03-28 18:49:36

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by pbruin created at 2014-03-28 18:53:27

While looking at #10745 I noticed that the default `limtriv` over *Q* in Simon's script `ellQ.gp` changed from 50 to 3 in the latest version, so I changed the default setting in `ell_rational_field.py` and `gp_simon.py` accordingly.  Still qualifies as a reviewer patch, I guess.


---

Comment by pbruin created at 2014-03-28 18:53:27

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-03-31 14:57:12

Resolution: fixed
