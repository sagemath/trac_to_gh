# Issue 7870: dozens of failures in magma optional test suite on skynet (eno) with sage-4.3

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-01-07 20:51:18

Assignee: was

I ran the magma optional test suite on skynet (eno):

```
./sage -t --only_optional=magma devel/sage/sage > magma.out&
```


And the failures are:

```
        sage -t --only_optional=magma "devel/sage/sage/rings/polynomial/pbori.pyx"
        sage -t --only_optional=magma "devel/sage/sage/rings/polynomial/multi_polynomial_ring_generic.pyx"
        sage -t --only_optional=magma "devel/sage/sage/rings/polynomial/term_order.py"
        sage -t --only_optional=magma "devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py"
        sage -t --only_optional=magma "devel/sage/sage/crypto/mq/mpolynomialsystem.py"
        sage -t --only_optional=magma "devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_g2_generic.py"
        sage -t --only_optional=magma "devel/sage/sage/symbolic/expression.pyx"
Total time for all tests: 364.0 seconds
```



---

Comment by was created at 2010-01-07 20:51:42

this is the output of running the test suite, showing the actual failures.


---

Attachment

I tested again using the new magma V2.16-7 with sage-4.3.5. 

```
[wstein`@`eno sage-4.3.5]$ magma
Magma V2.16-7     Tue Apr  6 2010 11:14:18 on eno      [Seed = 3125460604]
Type ? for help.  Type <Ctrl>-D to quit.
```

There are now even more failures.  I've attached a new test log created using the following on eno:

```
./sage -tp 10 -only_optional=magma devel/sage/sage
```



---

Comment by was created at 2010-04-06 15:16:25

it got much worse!


---

Attachment

This fixes all the doctest issues on eno with magma V2.16-7


---

Comment by was created at 2010-04-06 16:21:30

Changing status from new to needs_review.


---

Comment by cremona created at 2010-04-06 16:33:58

Changing assignee from was to cremona.


---

Comment by cremona created at 2010-04-06 16:33:58

I am testing this now with magma V2.16-1 and will report back.  It will not be a clean result, since I already saw

```

**********************************************************************
File "/storage/jec/sage-4.3.5/devel/sage-tests/sage/symbolic/expression.pyx", line 499:
    sage: magma(f)                         # optional - magma
Expected:
    sin(cos(x^2) + log(x))
Got:
    sin(log(x) + cos(x^2))
```



---

Comment by cremona created at 2010-04-06 16:36:25

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2010-04-06 16:36:25

Full log is at http://www.warwick.ac.uk/staff/J.E.Cremona/magma_test.log .


---

Comment by cremona created at 2010-04-06 17:08:53

Replying to [comment:4 cremona]:
> Full log is at http://www.warwick.ac.uk/staff/J.E.Cremona/magma_test.log .

Apologies -- it looks as if I did not apply the patch since the differences look exactly like the ones you fixed!  I will try again.


---

Comment by cremona created at 2010-04-06 17:08:53

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-04-06 17:20:51

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2010-04-06 17:20:51

OK, so after actually applying the patch (I had forgotten to do hg qpush) I get exactly one failure.  This is on 64-bit ubuntu, Sage 4.3.5 and Magma V2.16-1:

```
sage -t --only_optional=magma "./sage/interfaces/magma.py"  
**********************************************************************
File "/storage/jec/sage-4.3.5/devel/sage-tests/sage/interfaces/magma.py", line 187:
    sage: y * 1.0                                                         # optional - magma
Exception raised:
    Traceback (most recent call last):
      File "/home/jec/sage-current/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jec/sage-current/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jec/sage-current/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[46]>", line 1, in <module>
        y * RealNumber('1.0')                                                         # optional - magma###line 187:
    sage: y * 1.0                                                         # optional - magma
      File "element.pyx", line 1398, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:11337)
        return coercion_model.bin_op(left, right, mul)
      File "coerce.pyx", line 717, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6212)
        raise
      File "coerce.pyx", line 713, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6151)
        return PyObject_CallObject(op, xy)
      File "element.pyx", line 1393, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:11265)
        return (<RingElement>left)._mul_(<RingElement>right)
      File "element.pyx", line 1400, in sage.structure.element.RingElement._mul_ (sage/structure/element.c:11385)
        cpdef RingElement _mul_(self, RingElement right):
      File "/home/jec/sage-current/local/lib/python/site-packages/sage/interfaces/expect.py", line 1909, in _mul_
        return self._operation('*', right)
      File "/home/jec/sage-current/local/lib/python/site-packages/sage/interfaces/expect.py", line 1866, in _operation
        raise TypeError, msg
    TypeError: Error evaluating Magma code.
    IN:
[27]:=_sage_[19] * _sage_[25];
    OUT:
    >> _sage_[27]:=_sage_[19] * _sage_[25];
                              ^
    Runtime error in '*': Bad argument types
    Argument types given: RngUPolElt[RngInt], FldReElt

```

and this looks like some error in parsing the expected output (are you allowed two different "..."?) since it looks fine to me.  The only other things I can think of is that there may be different numbers of spaces in the expected and actual magma output!


---

Comment by cremona created at 2010-04-06 17:20:51

Changing keywords from "" to "Magma".


---

Comment by was created at 2010-04-27 02:59:39

John,

I think you should give my patch a positive review anyways.  The problem above is that in Magma V2.16-7, this works fine:

```
[wstein`@`eno ~]$ magma
Magma V2.16-7     Mon Apr 26 2010 22:51:34 on eno      [Seed = 294390646]
Type ? for help.  Type <Ctrl>-D to quit.
> R<x> := PolynomialRing(Integers());
> x*1.0;
$.1
> 
```

However, in older versions of Magma, it doesn't:

```
flat:~ wstein$ magma
Magma V2.15-11    Mon Apr 26 2010 19:53:21 on flat     [Seed = 4201111680]
Type ? for help.  Type <Ctrl>-D to quit.
> R<x> := PolynomialRing(Integers());
> x*1.0;

>> x*1.0;
    ^
Runtime error in '*': Bad argument types
Argument types given: RngUPolElt[RngInt], FldReElt
```


Since Magma's capabilities, etc., change a *lot* -- even from minor version to version -- I think the Sage optional doctests should be targeted at the latest released version of Magma.   

Note that the computation is multiplying a polynomial over ZZ[x] by a floating point numbers.  In Sage, there is a beautiful coercion model that makes most such things "just work".  In Magma, one implements the '*' function for every conceivable choice of pairs of types... and I guess somebody got around to eventually implementing this one. 

Just to emphasize how totally arbitrary (and sad) Magma's system still is after all these years, notice that even in Magma V2.16-7, the same computation with polynomials over ZZ and rational numbers doesn't work!

```
> x + 1/2;        

>> x + 1/2;
     ^
Runtime error in '+': Bad argument types
Argument types given: RngUPolElt[RngInt], FldRatElt

> x*(1/2);

>> x*(1/2);
    ^
Runtime error in '*': Bad argument types
Argument types given: RngUPolElt[RngInt], FldRatElt

> 
```


Sage had the same sort of silly anomalies until people like David Harvey, Craig Citro, David Roe, and *Robert Bradshaw* and others stepped in and greatly improved the situation. 


```
sage: R.<x> = ZZ[]
sage: x * 1.0
x
sage: parent(x * 1.0)
Univariate Polynomial Ring in x over Real Field with 53 bits of precision
sage: x + 1/2
x + 1/2
sage: (1/2)*x
1/2*x
```


Sage coercion is still of course far from perfect.  But it's also far from sucking. 

 -- William


---

Comment by was created at 2010-04-27 02:59:46

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-04-27 12:46:40

I just lost my posting here (cookie problem) and don't feel like rewriting it all....

I only have C2.16-1 and the patch requires V2.16-7 or higher to pass, it seems, so I cannot verify it at present.

Is it anywhere documented which version of Magma Sage relies on for positive tests?


---

Comment by cremona created at 2010-04-28 09:51:19

With Sage 4.4 and a newly installed magma V1.16-7 I still get falures in these files:

```
	sage -t --only_optional=magma "devel/sage/sage/rings/finite_rings/element_givaro.pyx"
	sage -t --only_optional=magma "devel/sage/sage/rings/polynomial/multi_polynomial.pyx"
	sage -t --only_optional=magma "devel/sage/sage/rings/polynomial/polynomial_element.pyx"
	sage -t --only_optional=magma "devel/sage/sage/rings/polynomial/polynomial_ring.py"
	sage -t --only_optional=magma "devel/sage/sage/schemes/elliptic_curves/ell_generic.py"
	sage -t --only_optional=magma "devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_generic.py"
```

See http://www.warwick.ac.uk/staff/J.E.Cremona/magma.out for the full log.


---

Comment by cremona created at 2010-04-28 10:20:38

A shorter log file with only the failing files is at http://www.warwick.ac.uk/staff/J.E.Cremona/magma.out.short


---

Comment by was created at 2010-05-01 07:11:09

Oh boy, it looks like sage-4.4 changed (from when I made the patch) and introduced a *bunch* of new issues :-(.   Sigh, I'll have to rewrite a bunch of the interface, evidently. Well at least I know now.


---

Comment by drkirkby created at 2010-06-02 20:29:15

Is there any explanation of why these doc tests need to be revised? I can see 

sage/symbolic/expression.pyx

has a pretty trivial change, since Magma has decided to reverse the order of the outputs. 

But others seem really odd. 

magma(HyperellipticCurve(f)).IgusaClebschInvariants() # optional - magma 
remove: [ 0, -2048/375, -4096/25, -4881645568/84375 ] 
add: [ -640, -20480, 1310720, 52160364544 ] 

Were the first set of Magma results wrong? If so, why was they used as a doctest? 

This is probably my lack of mathematical knowledge showing here, but it appears to me Magma has output something completely different in many cases. Is the new output correct? Was the old output incorrect? 

Dave


---

Comment by rlm created at 2010-06-22 17:49:38

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2010-06-22 17:49:38

Replying to [comment:12 was]:
> Oh boy, it looks like sage-4.4 changed (from when I made the patch) and introduced a *bunch* of new issues :-(.   Sigh, I'll have to rewrite a bunch of the interface, evidently. Well at least I know now.

Based on this, I'm changing this to needs_work. Not volunteering to review, just trying to clean up trac a bit!


---

Attachment

Replaces all previous patches;  applies to 4.6.1 and Magma 2.17-4


---

Comment by cremona created at 2011-02-18 23:06:06

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2011-02-18 23:06:06

New patch passes all optional doctests on skynet (eno) with 4.6.1 and Magma 2.17-4.


---

Comment by mraum created at 2011-03-02 09:57:45

I had to change one doctest, such that it also fits my output. This is definitely no issue, as I just added ... for the time. Apart from this: Perfect!

For the record, the patchbot and the release manager:

Apply trac_7870-magma-doctest.patch
Apply trac-7870-magma-doctest-review.patch


---

Comment by mraum created at 2011-03-02 09:57:45

Changing status from needs_review to positive_review.


---

Attachment


---

Comment by cremona created at 2011-03-02 16:48:14

I'm happy with the reviewer's patch, and note that this ticket is still marked "positive review".


---

Comment by mariah created at 2011-03-04 16:26:46


```
trac_7870-magma-doctest.patch and trac-7870-magma-doctest-review.patch
when applied to 4.6.2 pass all optional doctests
(-only-optional=magma) on skynet/eno with Magma-2.17-5.
```



---

Comment by jdemeyer created at 2011-03-08 09:02:25

Replying to [comment:16 mraum]:
> For the record, the patchbot and the release manager:
> 
> Apply trac_7870-magma-doctest.patch
> Apply trac-7870-magma-doctest-review.patch

*Please* in the future write this in the ticket *description*.  Thanks!


---

Comment by drkirkby created at 2011-03-08 09:37:03

Replying to [comment:19 jdemeyer]:
> Replying to [comment:16 mraum]:
> > For the record, the patchbot and the release manager:
> > 
> > Apply trac_7870-magma-doctest.patch
> > Apply trac-7870-magma-doctest-review.patch
> 
> *Please* in the future write this in the ticket *description*.  Thanks!

That makes a lot of sence and should probably be put in some sort of guide to using trac. Is there one specifically for Sage? 

I know I came unstuck recently when I put a link to an spkg in the description, but that spkg needed tekinfo (or whatever it was), so Francois posted one which did not need it. But mine was in the description, his one was less prominently placed in the notes, so you used mine and found it did not work. 

At the very least, specifying the locations of .spkgs and what patches needed to be applied, should be mentioned on sage-devel, but ideally we need it documented on the trac server. 

Dave


---

Comment by jdemeyer created at 2011-03-08 12:49:58

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-03-08 12:49:58

All doctests involving magma should be marked `# optional - magma`.  I get various failures in `sage/rings/number_field/number_field.py`.


---

Comment by cremona created at 2011-03-08 17:09:58

Replying to [comment:21 jdemeyer]:
> All doctests involving magma should be marked `# optional - magma`.  I get various failures in `sage/rings/number_field/number_field.py`.

Apologies, this refers to the new function I put in (_magma_polynomial_) where I did not tag the doctests as optional.  It's my fault (though William was sitting next to me at the time, so I blame him too!)


---

Attachment

And it's my fault as well. I'm terribly sorry!
John, do you have a maschine without magma to run tests for the above fix on? It was only one function that was missed.

Martin


---

Comment by cremona created at 2011-03-08 19:02:10

I don't think it is necessary to have a machine without magma.  Just run a complete test both with and with out the --optional-magma.  It is faster to run with that flag since only doctests with the optional magma flag are run.


---

Comment by jdemeyer created at 2011-03-08 21:04:16

Changing status from needs_work to needs_review.


---

Comment by mraum created at 2011-03-09 01:40:47

This seems right. So, if everything is ok for you, also, give it a positive review.


---

Comment by drkirkby created at 2011-03-09 06:26:48

According to the `sage -h`, the option should be `-only-optional=magma` and *not* `--only-optional=magma`


I don't have Magma, but do have Mathematica, so I thought I'd try


```
drkirkby`@`hawk:~/sage-4.6.2.rc1$ ./sage -t -only_optional=mathematica devel/sage/sage
sage -t -only_optional=mathematica "devel/sage/sage/probability/all.py"
	 [0.1 s]
sage -t -only_optional=mathematica "devel/sage/sage/probability/__init__.py"
	 [0.1 s]
sage -t -only_optional=mathematica "devel/sage/sage/probability/random_variable.py"
```


but it seems to run every doctest, not just the Mathematica ones, which fail anyway, as noted at #8495. 


Dave


---

Comment by jdemeyer created at 2011-03-11 22:07:19

This needs to be rebased to sage-4.7.alpha1.


---

Comment by jdemeyer created at 2011-03-11 22:07:19

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by mraum created at 2011-03-12 20:57:47

I rebased the patch to 4.7alpha1. Please only apply the last one: review3.

Could anyone (John?) check this soon, so that we won't need to rebase it again?


---

Comment by mraum created at 2011-03-12 20:57:47

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2011-03-14 01:26:25

Replying to [comment:29 mraum]:
> I rebased the patch to 4.7alpha1. Please only apply the last one: review3.

Thanks.

> 
> Could anyone (John?) check this soon, so that we won't need to rebase it again?

OK, I'll try that soon.  (I have just been away for the weekend or I would have done it already.)


---

Comment by cremona created at 2011-03-15 04:33:05

With magma-V2.17-5 (which I downloaded and installed specially) and sage-4.7.alpha1 I tested everything both with and without -only-optional=magma and in both cases all tests passed.

So I am giving this a positive review (again).


---

Comment by cremona created at 2011-03-15 04:33:05

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-03-17 14:39:55

It seems that your 'review3' patch is based on an *older* version of the patches, I get the number_field doctest failures again.


---

Comment by jdemeyer created at 2011-03-17 14:39:55

Changing status from positive_review to needs_work.


---

Comment by mraum created at 2011-03-17 16:29:53

Well, yes. We really need to run the test on a setup without Magma then. I add the fix for this problem (which is review2 patch rebased to current Sage).


---

Comment by mraum created at 2011-03-17 16:29:53

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by cremona created at 2011-03-17 16:43:43

With the earlier patch (patch3) and the latest magma I tested everything and got no errors, so it seems like a waste of (my) time to do it all again.

I do not understand mraum's comments about doing tests on a machine with no magma.  I ran complete tests with and without  -only-optional=magma.


---

Comment by jdemeyer created at 2011-03-18 13:42:36

Resolution: fixed


---

Comment by jdemeyer created at 2011-03-18 13:42:36

Works now without magma.
