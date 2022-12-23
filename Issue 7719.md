# Issue 7719: Improvements to complex AGM

Issue created by migration from https://trac.sagemath.org/ticket/7719

Original creator: cremona

Original creation time: 2009-12-17 10:29:09

Assignee: AlexGhitza

CC:  robertwb

Keywords: complex agm

This is related to #6021 but also of independent interest.

As of 4.3 we use pari to compute the complex agm (i.e. a.agm(b) where a, b are complex).  Now the complex agm is multi-valued, and for the application to periods of elliptic curves it does matter which value is used (see upcoming paper by John Cremona and Thotsaphon Thongjunthug).  The pari-computed value is not this "optimal" value.  So I have implemented a native Sage version, replacing the existing code in sage/rings/complex_number.pyx.

Much to my surprise, the new code is in some cases 50 times faster than calling the pari library -- despite the fact that I have not yet cython-optimised the code!

```
sage: CC = ComplexField(200)
sage: a = CC(-0.95,-0.65)                
sage: b = CC(0.683,0.747)                
sage: %timeit t = a.agm(b, algorithm="pari")
100 loops, best of 3: 7.04 ms per loop
sage:  %timeit t = a.agm(b, algorithm="principal")
10000 loops, best of 3: 136 mus per loop
sage:  %timeit t = a.agm(b, algorithm="optimal")  
10000 loops, best of 3: 146 mus per loop
```

Here "mus" means microseconds (this was run on a computer for which displaying greek "mu" causes an error).  "pari" is the old way calling the pari library function;  "principal" is a native implementation of essentially the same; "optimal" is the native implementation returning the so-called optimal value.

Some details:  AGM(a,b) is the common limit of two sequences `a_n,b_n` under the iteration `(a,b) -> ((a+b)/2, sqrt(a*b))` and the issue is which square root to take.  The complete story is a wonderful but quite long one (which started with Gauss).  Essentially, the "principal" algorithm always takes the principal branch of the square root (with positive real part);  pari does the same after an initial step where AGM(a,b) is replaced by a*AGM(1/b/a);  the optimal sequence (which gives the largest limit) is the one for which the sign is always chosen so that sqrt(a*b) is closest to (a+b)/2.  Note that the optimal sequence is preserved under scaling, so gives AGM(z*a,z*b)=z*AGM(a,b), but this is not true of the principal sequence.

I have a patch, but before posting it I'll ask for some help optimising it cythonically.


---

Attachment

Applies to 4.3.rc0.  Preliminary version


---

Comment by cremona created at 2009-12-17 11:53:04

The first patch is not yet ready for review (there are some doctest failures in from elliptic curve period computations which will be fixed later).  I have put it here so that I can ask for help making the code more efficient as it's in a cython file, if possible.


---

Comment by was created at 2009-12-18 05:56:52

Watch out.  The following is a much more accurate reflection of how fast PARI is at this computation (and even then there is still a tiny bit of overhead):

```
sage: timeit('pari("agm(-0.95-0.65*I,0.683+0.747*I)")')
625 loops, best of 3: 33.2 µs per loop
```

versus

```
sage: CC = ComplexField(200)
sage: a = CC(-0.95,-0.65)                
sage: b = CC(0.683,0.747) 
sage: z = pari(a)
sage: timeit('z.agm(b)')
625 loops, best of 3: 309 µs per loop
```


To avoid overhead from caching:

```
sage: time z = pari("for(i=1,10^5,agm(-0.95-I*0.65,0.683+I*0.747))")
CPU times: user 2.49 s, sys: 0.00 s, total: 2.49 s
Wall time: 2.49 s
```

which is about 25 microseconds. 

Conclusions:

  (1) How did you come up with an algorithm="pari" that takes 7ms?  That's really long.

  (2) What we do in Sage should hopefully take at most 25 microseconds in just order to be competitive to PARI. 

Here's some more to worry about.  Magma evidently does not even have a *complex* AGM.  However, it has a real AGM, and it is an order of magnitude faster than PARI's:


```
age: time z = pari("for(i=1,10^5,agm(-0.95,0.683))")
CPU times: user 2.07 s, sys: 0.00 s, total: 2.07 s
Wall time: 2.07 s
sage: magma.eval("time for n in [1..10^5] do z := AGM(0.95,0.683); end for;")
'Time: 0.170'
sage: 2.07/0.170
12.1764705882353
```



---

Comment by cremona created at 2009-12-18 09:13:29

Replying to [comment:2 was]:
> Watch out.  The following is a much more accurate reflection of how fast PARI is at this computation (and even then there is still a tiny bit of overhead):
> {{{
> sage: timeit('pari("agm(-0.95-0.65*I,0.683+0.747*I)")')
> 625 loops, best of 3: 33.2 µs per loop
> }}}
> versus
> {{{
> sage: CC = ComplexField(200)
> sage: a = CC(-0.95,-0.65)                
> sage: b = CC(0.683,0.747) 
> sage: z = pari(a)
> sage: timeit('z.agm(b)')
> 625 loops, best of 3: 309 µs per loop
> }}}

If you instead do timeit('a.agm(b)') you'll see a vast slow-down.   So the difference in speed is mainly coming from conversion to pari.  That is still worth avoiding if we can write a fast native version.

> 
> To avoid overhead from caching:
> {{{
> sage: time z = pari("for(i=1,10^5,agm(-0.95-I*0.65,0.683+I*0.747))")
> CPU times: user 2.49 s, sys: 0.00 s, total: 2.49 s
> Wall time: 2.49 s
> }}}
> which is about 25 microseconds. 
> 
> Conclusions:
> 
>   (1) How did you come up with an algorithm="pari" that takes 7ms?  That's really long.

I didn't come up with anything!  That code just calls the version of agm we have in Sage already which is two lines, calling pari after conversion.

> 
>   (2) What we do in Sage should hopefully take at most 25 microseconds in just order to be competitive to PARI. 

Agreed.  But as I said on sage-devel, what's very important for me is to get the correct ("optimal") value of the function.  I hope that will not mean having two versions of the function, one very fast but producing a value which is useless for me (as with the existing pari function) and a slower one I actually use.

By the way, this is not likely to be a function which is called many times over and over.

> 
> Here's some more to worry about.  Magma evidently does not even have a *complex* AGM.  However, it has a real AGM, and it is an order of magnitude faster than PARI's:
> 
> {{{
> age: time z = pari("for(i=1,10^5,agm(-0.95,0.683))")
> CPU times: user 2.07 s, sys: 0.00 s, total: 2.07 s
> Wall time: 2.07 s
> sage: magma.eval("time for n in [1..10^5] do z := AGM(0.95,0.683); end for;")
> 'Time: 0.170'
> sage: 2.07/0.170
> 12.1764705882353
> }}}
> 

Good point -- that's what we have to try to beat/match!


---

Comment by robertwb created at 2009-12-18 21:21:14

I'm not so sure switching the default from principle to optimal is the best thing to do, at least not without further investigation/justification.


---

Comment by cremona created at 2009-12-18 21:31:29

Replying to [comment:4 robertwb]:

I don't mind, as long as I can use the optimal one.  There's nowhere in Sage where the other version is used (except places in alliptic_curves/period_lattice.py where the optimal version _should_ be used).


---

Comment by robertwb created at 2009-12-19 00:02:51

That justification to switch is fine for me (I just wanted to raise the issue). 

On another note, see #7739


---

Attachment


---

Comment by robertwb created at 2009-12-19 09:31:35

The speed disparity between AGM over CC and over CDF was bugging me, so I decided to code the arbitrary-precision case directly against mpfr tonight. Made me wish we had mpc ;), or even better if sage/cython could unroll CC arithmetic like this already (though there are several other optimizations)

In any case, now we have


```
sage: a = CC(-0.95,-0.65)
sage: b = CC(0.683,0.747)
sage: %timeit a.agm(b, algorithm="optimal")
10000 loops, best of 3: 37.9 µs per loop
sage: %timeit aa.agm(bb)
10000 loops, best of 3: 35.2 µs per loop
```


The difference may be due to pari's stack-based rather than heap-based memory management. Note, we're getting closer to optimal with this algorithm as good chunk of the time is due to just taking the square roots:


```
sage: %timeit [a.sqrt() for k in range(6)]
10000 loops, best of 3: 25.9 µs per loop
```



---

Comment by cremona created at 2009-12-19 09:56:47

Fantastic piece of work!  I am so pleased that I asked for help doing this -- the results are even better than I hoped.   Later today I'll do a proper review.  Thanks, Robert.


---

Comment by cremona created at 2009-12-19 12:52:52

Changing status from new to needs_work.


---

Comment by cremona created at 2009-12-19 12:52:52

Robert: in line 1508 you set required_prec to self.prec -2.  In my code I used the precision-2 when testing relative error based on nothing more than trial and error (this way it converged while with the same precision it did not), since I am hopeless at working this kind of thing out properly.

Before merging this, I'll need to fix some doctests in the elliptic curve code -- but before that there's some more work to be done, since the new cmp_abs() does not work on my 32-bit machine (and my 64-bit machine has crashed...):

```
sage -t  "devel/sage-cagm/sage/rings/complex_number.pyx"    
**********************************************************************
File "/home/john/sage-4.3.rc0/devel/sage-cagm/sage/rings/complex_number.pyx", line 2190:
    sage: cmp_abs(CC(5), CC(1))
Expected:
    1
Got:
    -1
**********************************************************************
File "/home/john/sage-4.3.rc0/devel/sage-cagm/sage/rings/complex_number.pyx", line 2192:
    sage: cmp_abs(CC(5), CC(4))
Expected:
    1
Got:
    -1
**********************************************************************
File "/home/john/sage-4.3.rc0/devel/sage-cagm/sage/rings/complex_number.pyx", line 2194:
    sage: cmp_abs(CC(5), CC(5))
Expected:
    0
Got:
    -1
**********************************************************************
File "/home/john/sage-4.3.rc0/devel/sage-cagm/sage/rings/complex_number.pyx", line 2200:
    sage: cmp_abs(CC(-100), CC(1))
Expected:
    1
Got:
    -1
**********************************************************************
File "/home/john/sage-4.3.rc0/devel/sage-cagm/sage/rings/complex_number.pyx", line 2202:
    sage: cmp_abs(CC(-100), CC(100))
Expected:
    0
Got:
    -1
**********************************************************************
File "/home/john/sage-4.3.rc0/devel/sage-cagm/sage/rings/complex_number.pyx", line 2206:
    sage: cmp_abs(CC(1,1), CC(1))
Expected:
    1
Got:
    -1
**********************************************************************
1 items had failures:
   6 of  19 in __main__.example_79
***Test Failed*** 6 failures.
```



---

Comment by ylchapuy created at 2009-12-19 14:06:34

The failures comes from line 2225 where b.__im is used instead of b.__re .

There is also a problem line 1513 where we should test for [ComplexNumber](ComplexNumber) instead of real.


---

Comment by cremona created at 2009-12-19 14:11:07

Well spotted -- I will fix those two things in a 3rd patch, and at the same time fix the related doctest issues.  Later today.

Sounds like ylchapuy will be needed for a final review of this one -- thanks.


---

Attachment

Replaces previous patch


---

Comment by cremona created at 2009-12-19 18:56:04

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2009-12-19 18:56:04

This was harder than expected.  After applying the two changes suggested by ylchapuy I found that the code looped on some inputs (e.g. the new test, which arose from testing period_lattice.py).  This led to finding some other bugs in that cmp_abs function (in cases where a or b is zero only), and after fixing that I found that the max_exp function returns something like -2^31 when z=0 which then causes overflow (and the infinite loop) when the difference d is exactly 0 in the agm code (which does happen).  Hence the extra test for that condition (which seemed simpler than changing max_exp).

Some minor doctest fixes in the elliptic_curve directory  were needed (all numerical fuzz).

The bugfix patch also contains Robert's original changes (sorry) and then my actual bugfixes, so only the first and third should be applied.

Anyone else like to review this?  Otherwise I'll OK Robert's code (as adjusted here), but someone needs to check (I did check on 64-bit as well as 32-bit).


---

Comment by robertwb created at 2009-12-19 19:03:20

Thanks. Sorry my code had so many issues--I wrote it pretty quickly and should have tested it more, but wanted to get what I had up. I'll take a look again.


---

Comment by cremona created at 2009-12-19 21:01:37

Replying to [comment:14 robertwb]:
> Thanks. Sorry my code had so many issues--I wrote it pretty quickly and should have tested it more, but wanted to get what I had up. I'll take a look again. 

No apology needed.  This way I read it a lot more carefully than I might have done if everything had worked!


---

Comment by robertwb created at 2009-12-19 21:40:21

I found another case where it enters into an infinite loop. It's just messy when the required precision is so close to the rounding error, and we're doing many real operations here. Other than that, positive review to the changes you made. 

The solution, it seems, is to require at least half the desired precision on the penultimate iteration. Patch coming up.


---

Comment by robertwb created at 2009-12-19 22:41:41

apply first and this only


---

Attachment

After I coded up the previous suggestion, I felt the best way was to simply run the whole thing with a bit of extra precision. This way the last couple bits in the final iteration will actually be correct for that step, not just as correct as they could be due to rounding limitations. I also fixed a bug with a.agm(-a) and added some more tests. 

I folded it into the above patch, so apply trac_7719-agm.patch and 7719-bugfix2.patch. I'm positively reviewing cremona's changes--he needs to look at mine.


---

Comment by cremona created at 2009-12-19 23:20:27

I'll look at it tomorrow as its too late now in th UK.

About a.agm(-a):  it should be put into the specification that a.agm(b) requires a and b nonzero and also a not equal to plus or minus b.  We could either throw an error if any of those hold, or return zero.  (In applications these conditions will not hold anyway).

If you could add that to your next patch that would be helpful!  thanks


---

Comment by robertwb created at 2009-12-20 10:03:01

apply first and this only


---

Attachment

I think returning zero is the right thing to do for these degenerate cases--after all the AGM as a limit of the arithmetic and geometric means does exist. I've updated the patch.


---

Attachment

apply on top of bugfix3


---

Comment by ylchapuy created at 2009-12-20 11:39:58

This seems good to me and I can't think of other degenerate cases.

I added a last patch with a slight improvement, it avoids an add in the loop.
It really isn't critical but why not do it?


---

Comment by cremona created at 2009-12-20 12:12:00

Thanks -- ingeneous.

About Robert's latest:  luckily he did what I intended which was to deal with the special cases (a,-a), (a,0) and (0,b) while leaving alone the case (a,a) where the limit is (of course) a.  I described that last case as degenerate above since in my application it would be, but as far as the AGM itself is concerned it is clear that the correct value when a=b is a!  (Note, though, that the 'principal' version will not return a when a=b and Re(a)<0.)

Secondly, the better precision handling now means that I can revert the doctest changes for ell_rational_field and period_lattice.  Which probably means that I should not have changed them in the first place...

I'll merge all our patches into a single one for the final review.


---

Attachment

Replaces all previous


---

Comment by cremona created at 2009-12-20 12:47:06

The new patch trac_7719-cagm.patch replaces all previous, for ease of application -- and also makes clear that just one file is touched (rings/complex_number.pyx) though testers should also test schemes/elliptic_curves/{period_lattice,ell_number_field,ell_rational_field}.py since these all use the code.

I made this using the "fold" system in mercurial queues, which worked fine, though the end result is that I'm the only user listed in the patch.  If anyone knows how to get back in the credit for Robert Miller, and also ylchapuy, please do since the last thing I want to do is take credit for Robert's fantastic work on this.


---

Comment by robertwb created at 2010-01-07 10:32:02

That's why I avoid the fold command for tickets with multiple authors... (BTW, I'm Bradshaw, not Miller.)


---

Comment by cremona created at 2010-01-07 10:41:03

Replying to [comment:23 robertwb]:
> That's why I avoid the fold command for tickets with multiple authors... (BTW, I'm Bradshaw, not Miller.)
Very sorry -- I seem to have made things worse with my first apology!  I do know which of you is which, honest.


---

Comment by robertwb created at 2010-01-07 10:48:46

Don't worry, it's not a big deal (I know you know us both).


---

Comment by cremona created at 2010-01-21 16:24:42

I only just noticed that this was not merged into 4.3.1!  A pity since the similar patch for RDF/CDF is in (#7739).

Can a non-author please test again and (hopefully) give a positive review?


---

Comment by rishi created at 2010-01-21 19:02:37

Works good. The algorithm is exactly the definition so it was easy to follow the code. And I found out (for my knowlege) that swapping is faster than mpfr_set if you do not care about the other value.


---

Comment by rishi created at 2010-01-21 19:02:37

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-01-22 20:15:55

Resolution: fixed
