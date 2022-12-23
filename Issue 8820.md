# Issue 8820: elliptic_exponential broken for curves over number fields

Issue created by migration from https://trac.sagemath.org/ticket/8820

Original creator: robertwb

Original creation time: 2010-04-29 09:03:18

Assignee: cremona

CC:  jdemeyer rwb


```
sage: E = EllipticCurve('37a')
sage: K.<a> = QuadraticField(-5)
sage: L = E.change_ring(K).period_lattice(K.places()[0])
sage: L.elliptic_exponential(CDF(.1,.1))
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "/usr/local/sage/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/period_lattice.py", line 1390, in elliptic_exponential
    pxy = E.pari_curve(prec+5).ellztopoint(w)
  File "gen.pyx", line 9234, in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:44342)
PariError: bad argument for an elliptic curve related function (43)
```


Perhaps Pari doesn't support curve not over Q? 


---

Comment by robertwb created at 2010-04-29 09:13:30

Changing type from defect to enhancement.


---

Comment by robertwb created at 2010-04-29 09:13:30

Actually, this makes sense because I'm not giving Pari the embedding to use.


---

Comment by cremona created at 2010-04-29 09:35:33

Rats, I thought I had implemented this properly.  The elliptic log does have examples over number fields with complex embeddings!  This should be a lot easier...

The period lattice has an embedding into CC (or RR) stored with it.  That should be used to create a pari elliptic curve defined over RR or CC, there the pari function would work.

I would much prefer to have our own Weierstrass functions implemented, but that's the situation right now.

Note that this will involve some of the same code as #8815.


---

Comment by cremona created at 2010-08-27 09:47:16

I am working on this right now.


---

Comment by cremona created at 2010-08-29 14:35:46

applies to 4.5.3.alpha2


---

Comment by cremona created at 2010-08-29 14:38:36

Changing status from new to needs_review.


---

Attachment

The patch implements this.  I left the old code (using ellztopoint) for curves over QQ though the new code (using ellwp) works fine too, since the the output of many doctests would have changed (in insignificant bits), especially in heegner.py.

I also documented a couple of functions in period_lattice.py which were not, so that file now has 100% coverage.


---

Comment by wuthrich created at 2010-09-23 19:14:17

I get doctest failures, like the typical case below. It should be considered numerical noise, but somehow it is not a very good example then. I think a point (1,1) would give a more convincing example.


```
File "/local/pmzcw/prog/sage-4.5/devel/sage-test/sage/schemes/elliptic_curves/period_lattice.py", line 1424:
    sage: Li[0].elliptic_exponential(zi[0])
Expected:
    (2.17701177381006e-16 + 2.21973923391111e-16*I : 1.11022302462516e-16 - 2.21990394816407e-16*I : 1.00000000000000)
Got:
    (2.17818031662168e-16 + 2.22022549601564e-16*I : 1.11022302462516e-16 - 2.22044604925031e-16*I : 1.00000000000000)
```


The lines that fail are 1424, 1426, 1428, 1440, 1450, 1452.


---

Comment by wuthrich created at 2010-09-23 19:14:17

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2010-09-23 21:06:19

Replying to [comment:5 wuthrich]:
> I get doctest failures, like the typical case below. It should be considered numerical noise, but somehow it is not a very good example then. I think a point (1,1) would give a more convincing example.
> 
> {{{
> File "/local/pmzcw/prog/sage-4.5/devel/sage-test/sage/schemes/elliptic_curves/period_lattice.py", line 1424:
>     sage: Li[0].elliptic_exponential(zi[0])
> Expected:
>     (2.17701177381006e-16 + 2.21973923391111e-16*I : 1.11022302462516e-16 - 2.21990394816407e-16*I : 1.00000000000000)
> Got:
>     (2.17818031662168e-16 + 2.22022549601564e-16*I : 1.11022302462516e-16 - 2.22044604925031e-16*I : 1.00000000000000)
> }}}
> 
> The lines that fail are 1424, 1426, 1428, 1440, 1450, 1452.

Which version is that?  The patch says 4.5!


---

Comment by cremona created at 2010-09-23 21:07:15

Replying to [comment:6 cremona]:


> Which version is that?  The patch says 4.5!

Sorry, I meant "path".


---

Comment by wuthrich created at 2010-09-24 18:16:33

It is 4.5.3 on my office computer. 

Not that I believe that it matters. It is just numerical noise. Both results are correct with an error 2.e-16. My question is whether we should change it to 2.2.... e-16, while we could take as an example a point (1,1) where 1.000000... would be a better illustration of the computations.

Am I too picky ?

Chris.


---

Comment by cremona created at 2010-09-24 19:28:58

Replying to [comment:8 wuthrich]:
> It is 4.5.3 on my office computer. 
> 
> Not that I believe that it matters. It is just numerical noise. Both results are correct with an error 2.e-16. My question is whether we should change it to 2.2.... e-16, while we could take as an example a point (1,1) where 1.000000... would be a better illustration of the computations.
> 
> Am I too picky ?

No, not at all -- using points which do not have 0 as a coordinate is a good idea!  But I was confused since the test which fails does not appear to exist on my 4.6.alpha1.

> 
> Chris.


---

Comment by cremona created at 2010-09-24 19:31:58

Replying to [comment:9 cremona]:
> Replying to [comment:8 wuthrich]:
> > It is 4.5.3 on my office computer. 
> > 
> > Not that I believe that it matters. It is just numerical noise. Both results are correct with an error 2.e-16. My question is whether we should change it to 2.2.... e-16, while we could take as an example a point (1,1) where 1.000000... would be a better illustration of the computations.
> > 
> > Am I too picky ?
> 
> No, not at all -- using points which do not have 0 as a coordinate is a good idea!  But I was confused since the test which fails does not appear to exist on my 4.6.alpha1.

Sorry, I am being completely stupid -- of course the failing test is in the patch and I was looking at unpatched files!  But now I find that the patch does not apply to 4.6.alpha1 so I will have to rebase it.  When I do that I will try to use better examples.

> 
> > 
> > Chris.


---

Comment by cremona created at 2010-09-24 20:04:30

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-09-24 20:04:30

Please try the rebased patch.  I changes the point (0,0) to (-1,-1) in the bad example, but that was enough since the approximate imaginary parts were not exactly 0 -- which I got around by taking real parts where necessary.  A little crude, but it avoids the fuzz.


---

Comment by jdemeyer created at 2010-09-25 17:20:30

John: I suppose you mean rebased to 4.6.alpha1 unless you have some super-secret pre-release version of sage-4.6.alpha2 :-)

Also: you should use "PARI" instead of "Pari".


---

Comment by cremona created at 2010-09-25 17:43:25

Replying to [comment:12 jdemeyer]:
> John: I suppose you mean rebased to 4.6.alpha1 unless you have some super-secret pre-release version of sage-4.6.alpha2 :-)
> 
> Also: you should use "PARI" instead of "Pari".

yes, alpha1


---

Comment by cremona created at 2010-09-26 16:46:21

Replying to [comment:13 cremona]:
> Replying to [comment:12 jdemeyer]:
> > John: I suppose you mean rebased to 4.6.alpha1 unless you have some super-secret pre-release version of sage-4.6.alpha2 :-)
> > 
> > Also: you should use "PARI" instead of "Pari".
> 
> yes, alpha1

I have now fixed all the offending "Pari" and "pari" in the patch, and all the files in  elliptic_curves!


---

Attachment

applies to 4.6.alpha1


---

Comment by jdemeyer created at 2010-09-26 18:04:23

John, I have rebased your patch such that it can be applied after the positively-reviewed #9931 (there were several conflicts).  I also made some very small changes to the docstring of the `cardinality` function in `ell_finite_field.py`


---

Comment by cremona created at 2010-09-26 20:56:14

Replying to [comment:15 jdemeyer]:
> John, I have rebased your patch such that it can be applied after the positively-reviewed #9931 (there were several conflicts).  I also made some very small changes to the docstring of the `cardinality` function in `ell_finite_field.py`

OK, I'm not sure what the issues were there but the new patch applies fine after #9931;  I am currently testing it.  Meanwhile:  the latest patch's header is

```
...
# User Jeroen Demeyer <jdemeyer@cage.ugent.be>
...
[mq]: 8820_rebase_after_9931
```

and I think protocol would leave me as author (and have a better one-line description) ;)


---

Comment by cremona created at 2010-09-26 20:56:14

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2010-09-26 21:12:30

Replying to [comment:16 cremona]:
> # User Jeroen Demeyer <jdemeyer`@`cage.ugent.be>
> ...
> [mq]: 8820_rebase_after_9931
> }}}
> and I think protocol would leave me as author (and have a better one-line description) ;)

OK, I just copy-pasted the header from your patch.


---

Comment by jdemeyer created at 2010-09-26 21:12:44

John's patch rebased to be applied on top of #9931 (and some small additional changes)


---

Comment by cremona created at 2010-09-26 21:42:19

Changing status from needs_work to positive_review.


---

Attachment

Replying to [comment:17 jdemeyer]:
> Replying to [comment:16 cremona]:
> > # User Jeroen Demeyer <jdemeyer`@`cage.ugent.be>
> > ...
> > [mq]: 8820_rebase_after_9931
> > }}}
> > and I think protocol would leave me as author (and have a better one-line description) ;)
> 
> OK, I just copy-pasted the header from your patch.

Thanks -- I added your name as reviewer and marked the ticket Positive Review.  If you want, you can add your name as author (and mine as reviewer) -- I appreciate your attention to detail.

Release manager:  apply only the last patch 8820_rebase_after_9931.patch, after the patch at #9931.


---

Comment by jdemeyer created at 2010-09-26 22:05:35

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2010-09-26 22:05:35

I'm sorry John, but I did not review your patch, I just made a few small comments.  In any case, I think it is strange for the author of a patch to set his ticket to positive_review (no offense though).  I can probably review your patch later (not tonight).


---

Comment by jdemeyer created at 2010-09-26 22:05:43

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-09-26 22:14:19

Replying to [comment:19 jdemeyer]:
> I'm sorry John, but I did not review your patch, I just made a few small comments.  In any case, I think it is strange for the author of a patch to set his ticket to positive_review (no offense though).  I can probably review your patch later (not tonight).

No problem -- I misunderstood, and also forgot that the original doctest failures were not from you but from Chris Wuthrich.

Of course I would not positively review my own work!  I have now added Chris to the list of reviewers, and hope that he'll be able to take another look at it.  Needs review!


---

Comment by jdemeyer created at 2010-09-30 09:18:38

A few comments:

 * I think the help for `elliptic_exponential` (lines 1379--1385) is not so well written.  I would write something like

```
OUTPUT:

- If ``to_curve`` is False, a 2-tuple of real or complex numbers
representing the point `(x,y) = (\wp(z),\wp'(z))` where `\wp` denotes the Weierstrass
`\wp`-function with respect to this lattice.

- If ``to_curve`` is True, the point `(x-b_2/12,y-(a_1(x-b_2/12)-a_3)/2)`
as a point in `E(\RR)` or `E(\CC)`, with `(x,y) = (\wp(z),\wp'(z))` as above.

If the lattice is real...
```


 * The comment

```
       # the next lines compute [P(w), P'(w)] when flag=1
       # or [x:y:1] in E(C) when flag=2
```

 seems to refer to old code.

 * Is there a good reason to distinguish between QQ and general number fields?  The number-field code seems simpler, so you could consider removing the special-case code for QQ.

 * lines 1503 and 1530: `C(t.real().python(),t.imag().python())` can be simplified as `C(t)`.

 * it doesn't work for the point at infinity (and there should be a doctest for that case anyway):

```
sage: E = EllipticCurve([1,1,1,-8,6])
sage: L = E.period_lattice()
sage: L.elliptic_exponential(0)
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)

/usr/local/src/pari/src/<ipython console> in <module>()

/usr/local/src/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/period_lattice.pyc in elliptic_exponential(self, z, to_curve)
   1476         if self.coordinates(z) == self.coordinates(z, rounding='round'):
   1477             if to_curve:
-> 1478                 return E.change_ring(C)(0)
   1479             return (C('+infinity'),C('+infinity'))
   1480

UnboundLocalError: local variable 'E' referenced before assignment
```



---

Comment by jdemeyer created at 2010-09-30 09:18:38

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2010-09-30 09:35:20

Also, there is trouble with points which are very close to the point af infinity:

```
sage: K.<a> = QuadraticField(-1)
sage: E = EllipticCurve([0,0,0,a,0])
sage: L = E.period_lattice(K.complex_embeddings()[0])
sage: L.elliptic_exponential(1e-100)
---------------------------------------------------------------------------
PariError                                 Traceback (most recent call last)

/home/jdemeyer/<ipython console> in <module>()

/usr/local/src/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/period_lattice.pyc in elliptic_exponential(self, z, to_curve)
   1527         # the same precision as the input.
   1528
-> 1529         x,y = pari(self.basis(prec=prec)).ellwp(w,flag=1)
   1530         x,y = [C(t) for t in (x,y)]
   1531

/usr/local/src/sage-4.6.alpha1/local/lib/python2.6/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:45047)()

PariError: division by zero (27)
```



---

Comment by cremona created at 2010-09-30 10:41:41

Thanks for the comments, I will revise the patch accordingly.  The very last point (evaluation when z is very small but not zero) will not be easy though.  I think that I left in the special code for QQ since it was faster, but I may be mixing this up with the (harder!) elliptic logarithm.


---

Comment by jdemeyer created at 2010-09-30 15:06:30

Replying to [comment:25 cremona]:
> Thanks for the comments, I will revise the patch accordingly.  The very last point (evaluation when z is very small but not zero) will not be easy though.

You could use `try:`/`except PariError:` for this.  The only problem is that currently, you cannot easily check in Python whether a PariError is a division by zero or something else.


---

Comment by cremona created at 2010-09-30 16:43:32

It's ok, I have fixed it and the only reason I have not yet upadted the patch is that I am getting lots of failures in heegner.py -- not for the first time.  Several of the doctests there are not very well designed, so I may complain to Robert Bradshaw if I cannot fix them all!


---

Comment by cremona created at 2010-10-03 12:15:32

8820_rebase_after_9931-new.patch adresses the doctest failures in heegner.py.  I did this quite carefully (even refining a little the code which does the modular parametrization).  I took account where sensible of Chris's remark that it is better in approximate doctests not to have numbers which are approximately zero;  but when the output is an approximate integral Heegner point one cannot easily change the point.  I hope reviewer(s) do not object to the various ways I found  around this -- with very little use of ... and none (I think) of #random.

Note that these Heegner examples are often going to be problematical since in many cases the point computed is approximately (0:1:0), i.e. the z in CC is approximately a period.  In such examples it might be better just to output E.period_lattice().coordinates(z) rather than E.elliptic_exponential(z).  However, I have adjusted the test for being integral (i.e. for z to b in the period lattice) in a way that I hope is a reasonable compromise:   namely that the coordinates w.r.t. the lattice basis should be approximately integral in the sense that their fractional part is at most `2^(0.8*prec)`.


---

Comment by cremona created at 2010-10-03 12:15:32

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2010-10-03 15:57:11

Replying to [comment:28 cremona]:
> However, I have adjusted the test for being integral (i.e. for z to b in the period lattice) in a way that I hope is a reasonable compromise:   namely that the coordinates w.r.t. the lattice basis should be approximately integral in the sense that their fractional part is at most `2^(0.8*prec)`.

I like this solution. The `elliptic_exponential()` code looks fine to me.  However, I would like somebody else to review the heegner stuff.

One small suggestion: the doctest for `elliptic_exponential()` is quite long, so I would separate it in an `EXAMPLES` part and a `TESTS` part.


---

Comment by jdemeyer created at 2010-10-03 16:02:04

Replying to [comment:28 cremona]:
> I took account where sensible of Chris's remark that it is better in approximate doctests not to have numbers which are approximately zero

Well, my *personal opinion* on this differs a bit.  I think we should remember that doctests not only serve as tests, but also as documentation.  I think it is always a difficult excercise to balance these two.  For me personally, the balance always goes in favour of documentation.  When needed, one can still add true tests in a `TESTS` section of a doctest.


---

Comment by cremona created at 2010-10-03 16:19:56

Replying to [comment:30 jdemeyer]:
> Replying to [comment:28 cremona]:
> > I took account where sensible of Chris's remark that it is better in approximate doctests not to have numbers which are approximately zero
> 
> Well, my *personal opinion* on this differs a bit.  I think we should remember that doctests not only serve as tests, but also as documentation.  I think it is always a difficult excercise to balance these two.  For me personally, the balance always goes in favour of documentation.  When needed, one can still add true tests in a `TESTS` section of a doctest.

Fair enough.  In the heegner file, which I did not write any of, I did not want to re-think documentation/tests from scratch, although that might be a good idea;  I just wanted to get things to work!  (And I would not have had to do anything, I think, if I had not followed the suggestion to eliminate the specific QQ code from elliptic_exponential.)


---

Comment by was created at 2010-10-04 23:56:48

I give all the changes to heegner.py in the patch "8820_rebase_after_9931-new.patch" a positive review.


---

Comment by robertwb created at 2010-10-05 04:40:52

You beat me to it :). Looks fine by me too.


---

Comment by jdemeyer created at 2010-10-05 07:23:29

There is a doctest failure on a 32-bit machine:

```
sage -t -long "devel/sage/sage/schemes/elliptic_curves/heegner.py"
**********************************************************************
File "/Users/jdemeyer/sage-4.6.alpha2/devel/sage/sage/schemes/elliptic_curves/heegner.py", line 3048:
    sage: P = E.heegner_point(-19); y = P._trace_numerical_conductor_1(); [c.real() for c in y]
Expected:
    [-1.26165722088693e-16, -1.00000000000000, 1.00000000000000]
Got:
    [-1.26126537554300e-16, -1.00000000000000, 1.00000000000000]
**********************************************************************
```


When this is fixed (just write -1.261...), this ticket can finally gets its positive_review.


---

Comment by cremona created at 2010-10-05 08:26:26

replaces previous


---

Attachment

Thanks to all, and apologies for missing that one.  I have changed the patch as suggested and just tested it on a 32-bit machine as well as a 64-bit.

That failing test is exactly the kind of thing it would be nice to avoid altogether in doctests, since the "true" value of the x-coordinate is 0, so all nonzero digits, and the sign, are completely spurious.

Jeroen, if you are happy with this now could you mark it as "positive review"?  Thanks.

Release manager: only the last patch is to be applied.


---

Comment by jdemeyer created at 2010-10-05 20:41:37

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-10-06 03:17:56

Resolution: fixed
