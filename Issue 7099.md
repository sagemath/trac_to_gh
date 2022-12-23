# Issue 7099: serious incomplete gamma function precision bugs

Issue created by migration from https://trac.sagemath.org/ticket/7099

Original creator: was

Original creation time: 2009-10-02 18:58:08

Assignee: jkantor

CC:  kcrisman


```
sage: C = ComplexField(1000)
sage: C(2+I).gamma_inc(C(3+I))
0.1215156446645086956511068454478419198494520969688892364501953125000000\
000000000000000000000000000000000000000000000000000000000000000000000000\
000000000000000000000000000000000000000000000000000000000000000000000000\
000000000000000000000000000000000000000000000000000000000000000000000000\
00000000000000 +
0.1015339090798260332775427433604775728781532961875200271606445312500000\
000000000000000000000000000000000000000000000000000000000000000000000000\
000000000000000000000000000000000000000000000000000000000000000000000000\
000000000000000000000000000000000000000000000000000000000000000000000000\
00000000000000*I
```


What's with all the zeros?   Same bad behavior for higher precision and any other random input.  This is undoubtedly the typical mistake of not setting the pari precision correctly, etc., etc. 


---

Comment by kcrisman created at 2011-08-19 14:11:33

Correct.  Here's the problem, I think.

```

sage: C = ComplexField(1000)
sage: c = C(2+I)
sage: c
2.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 + 1.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000*I
sage: d = c.real()
sage: d
2.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
sage: d._pari_()
2.00000000000000
```

So here is the problem, right in the change to Pari from the RealField.


---

Comment by pbruin created at 2014-05-03 23:25:14

A probably related bug was just reported on [sage-support](https://groups.google.com/forum/#!topic/sage-support/RrveCpPgoKU):

```
sage: numerical_approx(gamma(9, 10^(-3))-gamma(9), digits=40)
0.000000000000000
```

The correct answer is approximately -1.1101115655 * 10<sup>-28</sup>.


---

Comment by pbruin created at 2014-05-04 00:07:31

Changing status from new to needs_info.


---

Comment by pbruin created at 2014-05-04 00:07:31

Here is a somewhat rough fix.  It doesn't take into account the precisions of both input parameters separately, but uses the precision of the desired parent in `Function_gamma_inc`, and the precision of the parent of the first argument in `ComplexNumber.gamma_inc()` et al.  Maybe an expert on this can say whether this behaviour is consistent with other special functions in Sage?

(Note that the relatively low precision in the new doctest is because of cancellation.)


---

Comment by git created at 2014-05-04 00:16:36

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by jdemeyer created at 2014-05-04 09:10:43

I'm wondering if this a bug in the `gamma` function or in symbolic functions in general...


---

Comment by jdemeyer created at 2014-05-04 09:13:57

Isn't this the only and actual bug? That the following doesn't depend on the `prec` parameter.

```
sage: numerical_approx(gamma(9,10^-3), prec=1024)                                    
40320.0000000000
```



---

Comment by jdemeyer created at 2014-05-04 09:17:28

I don't know whether the change to `src/sage/functions/other.py` is right (I'm not saying it is wrong, just don't know), but the adding of the precision arguments is obviously needed.


---

Comment by git created at 2014-05-04 13:14:24

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by pbruin created at 2014-05-04 13:19:13

Setting priority to critical because the bug leads to mathematically incorrect answers.

The original bug is already solved by passing the correct precision to PARI's `incgam()`.

The bug in comment:5 should be solved by the additional changes to `Function_gamma_inc._evalf_()`.


---

Comment by pbruin created at 2014-05-04 13:19:13

Changing status from needs_info to needs_review.


---

Comment by pbruin created at 2014-05-04 13:19:13

Changing priority from major to critical.


---

Comment by jdemeyer created at 2014-05-04 19:11:55

Replying to [comment:12 pbruin]:
> The bug in comment:5 should be solved by the additional changes to `Function_gamma_inc._evalf_()`.
I think it is better not to confuse these 2 different bugs.


---

Comment by dimpase created at 2014-05-04 19:40:48

Replying to [comment:9 jdemeyer]:
> Isn't this the only and actual bug? That the following doesn't depend on the `prec` parameter.
> {{{
> sage: numerical_approx(gamma(9,10^-3), prec=1024)                                    
> 40320.0000000000
> }}}

is `prec` parameter mentioned in the doc on `gamma`? It doesn't, IMHO. 
Are there other transcendentals for which this parameter does work?


---

Comment by rws created at 2014-05-05 06:40:59

"`TestsPassed 6.2.rc2`" http://patchbot.sagemath.org/ticket/7099/


---

Comment by kcrisman created at 2014-05-05 17:14:02

> > Isn't this the only and actual bug? That the following doesn't depend on the `prec` parameter.
> > {{{
> > sage: numerical_approx(gamma(9,10^-3), prec=1024)                                    
> > 40320.0000000000
> > }}}
> 
> is `prec` parameter mentioned in the doc on `gamma`? It doesn't, IMHO. 
> Are there other transcendentals for which this parameter does work?
I was pretty sure we were deprecating the `prec` keyword **inside** such functions.  But this is apparently a keyword of `numerical_approx`, which is different.  In which case it should just pass the precision on correctly somewhere else.


---

Comment by rws created at 2014-08-10 09:53:54

With #16697 the output is as expected:

```
sage: C = ComplexField(1000)
sage: gamma_inc(C(2+I),C(3+I))
0.121515644664508695525971545977439666159749344176962379708992904126499444842886620664991650378432544392118359044438541514683402245033018771644222346410367471459456844674335147722343580581945662693850674590491020834632434082710800093315646442975240326569517738365018117780134100101636704042869033248174 + 0.101533909079826033296475736021224621546966200987295663190553587086145836461236284668967411665020429964946098113930918849948956425984499549094441904693395768367238320065064071027383069839637218088862214571990869510941211277488169032567679631037683814516738122300220474252081775895835843619616213883517*I
```

This is because I changed the default to mpmath for the gamma functions. The ticket is still relevant for `C(2+I).gamma_inc(C(3+I))` however.


---

Comment by rws created at 2014-08-10 13:25:30

Patchbot was happy at 6.2beta2 so I guess it's still good. The changes look straightforward, anyway.


---

Comment by rws created at 2014-08-10 13:25:30

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-08-10 23:01:05

On the Arando buildbot:

```
sage -t --long src/sage/rings/complex_mpc.pyx
**********************************************************************
File "src/sage/rings/complex_mpc.pyx", line 2241, in sage.rings.complex_mpc.MPComplexNumber.gamma_inc
Failed example:
    (1+i).gamma_inc(2 + 3*i)
Expected:
    0.0020969149 - 0.059981914*I
Got:
    0.0020969148 - 0.059981914*I
**********************************************************************
1 item had failures:
   1 of   5 in sage.rings.complex_mpc.MPComplexNumber.gamma_inc
    [375 tests, 1 failure, 0.27 s]
sage -t --long src/sage/rings/complex_number.pyx
**********************************************************************
File "src/sage/rings/complex_number.pyx", line 2023, in sage.rings.complex_number.ComplexNumber.gamma_inc
Failed example:
    (1+i).gamma_inc(2 + 3*i)
Expected:
    0.0020969149 - 0.059981914*I
Got:
    0.0020969148 - 0.059981914*I
**********************************************************************
1 item had failures:
   1 of   8 in sage.rings.complex_number.ComplexNumber.gamma_inc
    [378 tests, 1 failure, 3.12 s]
```



---

Comment by vbraun created at 2014-08-10 23:01:05

Changing status from positive_review to needs_work.


---

Comment by git created at 2014-08-11 09:27:55

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by pbruin created at 2014-08-11 09:29:24

I'm assuming this fix does not absolutely require another review round...


---

Comment by pbruin created at 2014-08-11 09:29:24

Changing status from needs_work to positive_review.


---

Comment by vbraun created at 2014-08-11 15:01:31

Resolution: fixed
