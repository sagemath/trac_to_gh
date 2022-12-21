# Issue 4376: Implement conversion of power series over more rings (e.g. GF(p)) to pari

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-10-28 09:44:11

Assignee: was

CC:  salmanhb@gmail.com davidloeffler niles jdemeyer

Keywords: power series pari

salmanhb`@`gmail.com would like to be able to do linear algebra over `GF(p)[This is the Trac macro *X* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#X-macro)` using pari, but currently conversion of power series in `R[This is the Trac macro *X* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#X-macro)` to pari is only implemented when R=QQ or R=ZZ (via strings).

We should improve the _pari_() function for power series rings to allow R to be any ring in which pari conversion is already defined.


---

Comment by fwclarke created at 2010-08-27 10:18:54

Currently pari conversion doesn't even work for series with integer coefficients.  This was pointed out in the docstring for `sage.modular.overconvergent.genus0.OverconvergentModularFormElement._pari_`.

The attached patch extends the range of possible base rings significantly, but is still limited by what `sage.rings.polynomial.polynomial_element.Polynomial._pari_` can do; see its extensive docstring.


---

Comment by fwclarke created at 2010-08-27 10:18:54

Changing status from new to needs_review.


---

Attachment


---

Comment by niles created at 2010-12-04 16:41:00

I wonder if making a new comment will get [Patch Buildbot](http://wiki.sagemath.org/buildbot) to look at this . . .


---

Comment by mstreng created at 2010-12-06 10:53:21

Changing status from needs_review to needs_info.


---

Comment by mstreng created at 2010-12-06 10:53:21

Applies and builds without any problems on top of 4.6.1.alpha2 on the machine that I tried it on. All tests pass, the code looks good, and the patch seems to do what it says.

I would have made it "positive review", but then there is the new "Buildbot" link at the top of this page, which says "TestsFailed ..."

What should I do with that?


---

Comment by lftabera created at 2010-12-06 11:13:45

The buildbot is a tool to help you. If you check the fail. You will see that the tests that fail are stratup.py and setup0.py. These two are failing in all tickets, the fail does not have to do with this ticket. So if you have checked that the code is ok and your tests pass, feel free to give a positive review.


---

Comment by lftabera created at 2010-12-06 11:13:45

Changing status from needs_info to needs_review.


---

Comment by mstreng created at 2010-12-06 11:42:07

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-12-06 13:22:02

As a possible follow-up, we should also implement/check conversion to GP.


---

Comment by jdemeyer created at 2010-12-06 13:22:02

Changing keywords from "power series pari" to "power series pari gp".


---

Comment by jdemeyer created at 2011-01-27 14:55:58

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-01-27 14:55:58

Test failures on sage-4.6.2.alpha1:

```
sage -t  "devel/sage/sage/rings/power_series_poly.pyx"
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/sage-4.7.alpha0/devel/sage/sage/rings/power_series_poly.pyx", line 766:
    sage: g = f.reversion(); g
Expected:
    1/(2*b)*t - 1/(8*b^2)*t^2 + ((-3*b + 1)/(16*b^3))*t^3 + O(t^4)
Got:
    O(t^4)
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/sage-4.7.alpha0/devel/sage/sage/rings/power_series_poly.pyx", line 770:
    sage: f(g)
Expected:
    t + O(t^4)
Got:
    O(t^4)
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/sage-4.7.alpha0/devel/sage/sage/rings/power_series_poly.pyx", line 772:
    sage: g(f)
Expected:
    t + O(t^4)
Got:
    0
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/sage-4.7.alpha0/devel/sage/sage/rings/power_series_poly.pyx", line 779:                                      sage: b = a.reversion(); b                                                                                                            Exception raised:                                                                                                                             Traceback (most recent call last):
      File "/mnt/usb1/scratch/jdemeyer/sage-4.7.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/jdemeyer/sage-4.7.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/jdemeyer/sage-4.7.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_32[31]>", line 1, in <module>
        b = a.reversion(); b###line 779:
    sage: b = a.reversion(); b
      File "power_series_poly.pyx", line 847, in sage.rings.power_series_poly.PowerSeries_poly.reversion (sage/rings/power_series_poly.c:6881)
      File "gen.pyx", line 9851, in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:46023)
    PariError:  (20)
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/sage-4.7.alpha0/devel/sage/sage/rings/power_series_poly.pyx", line 781:
    sage: a(b)
Expected:
    t + O(t^6)
Got:
    b^5 + 6*b^4 + b^2 + b
**********************************************************************
File "/mnt/usb1/scratch/jdemeyer/sage-4.7.alpha0/devel/sage/sage/rings/power_series_poly.pyx", line 783:
    sage: b(a)
Expected:
    t + O(t^6)
Got:
    t + t^2 + 6*t^4 + t^5 + O(t^6)
**********************************************************************
```



---

Comment by jdemeyer created at 2011-01-27 14:56:44

Apply on top of previous patch


---

Attachment

The attached patch removes the conversion PARI -> string -> PARI.  It does not address the doctest failures.


---

Comment by fwclarke created at 2011-01-31 18:58:57

Replying to [comment:9 jdemeyer]:

> Test failures on sage-4.6.2.alpha1: 
> ...

What's happened is that #7644 means that many more series can be converted to Pari and reversion performed using `sereverse`.  But when the degree-one coefficient is not a unit, converting the result back to Sage has exposed the following problem:

```
sage: P.<x> = Q[]
sage: Q = P.fraction_field()
sage: Q(1/x)
1/x
sage: Q(pari(1/x))
0
```

This is caused by 

```
sage: P(pari(1/x))
0
```

whereas `P(1/x)` raises `TypeError: denominator must be a unit`.

The other group of failures is caused when conversion to a Pari series is successful but reversion raises a Pari error.

I will shortly post a patch which sorts these difficulties out. I've added a doctest for `reversion` in order to provide another example where Pari fails and the Lagrange inversion code needs to be used.


---

Comment by fwclarke created at 2011-01-31 19:56:38

Changing status from needs_work to needs_review.


---

Comment by fwclarke created at 2011-01-31 19:56:38

The attached patch makes the changes made in the previous patchescompatible with those made in !#7644.


---

Comment by mstreng created at 2011-01-31 20:45:04

Changing status from needs_review to needs_work.


---

Comment by mstreng created at 2011-01-31 20:45:04

On lines 316 and 317 of sage/rings/polynomial/polynomial_ring.py, you write

```
except (NotImplementedError, ValueError): 
    raise TypeError, "denominator must be a unit" 
```

I don't think a `NotImplementedError` should lead to a `TypeError`: that would give a lot of confusion.

Otherwise, this all looks very good.

(this ticket now depends on #7644)


---

Comment by jdemeyer created at 2011-02-01 14:19:31

I'm wondering if we shouldn't simply do

```
if x.type() == 't_RFRAC':
    raise TypeError, "denominator must be a unit"
```


I doubt that a PARI RFRAC can ever have a denominator which *is* a unit.


---

Attachment

Apply after previous two patches


---

Comment by fwclarke created at 2011-02-02 09:17:12

Replying to [comment:14 jdemeyer]:
> ...
> I doubt that a PARI RFRAC can ever have a denominator which *is* a unit.

I agree. So I've replaced the patch with one which implements your suggestion.


---

Comment by fwclarke created at 2011-02-02 09:17:12

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2011-02-02 10:25:59

Francis: your patches look fine to me.  Can somebody review my patch and give this ticket positive review?


---

Comment by niles created at 2011-03-18 14:11:27

[attachment:4376_no_strings.patch] looks good: it accomplishes the same thing as the "with strings" version of the code, but skips the step of converting a pari polynomial to a string and then back to a pari polynomial.  The patch includes some good corner-case tests, and a comment referencing the ticket number and what's being fixed.

Therefore, positive review for this patch.  If I understand the above correctly, the other patches here have already been positively reviewed, so I'm switching the whole ticket to `positive review`.


---

Comment by niles created at 2011-03-18 14:11:27

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-03-24 20:39:02

Resolution: fixed
