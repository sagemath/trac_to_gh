# Issue 8505: random points on elliptic curve misses half the group

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-03-12 00:34:32

Assignee: cremona

This is because it chooses only the first of the (usually) two possible lifts of a random x. Computing both is not more expensive, and this avoids the (expensive) exception creation and throwing as well. 

May have a bit of fuzz with #8311.


---

Attachment


---

Comment by robertwb created at 2010-03-12 00:36:06

Changing status from new to needs_review.


---

Comment by cremona created at 2010-03-12 14:57:55

Looks ok, will test and report back shortly.  (Have to go prove the Mordell-Weil Theorem first....)


---

Comment by cremona created at 2010-03-12 16:27:04

I tested all sage/schemes/elliptic_curves with -long and had one failure:

```
jec`@`selmer%sage -t -long "sage/schemes/elliptic_curves/ell_finite_field.py"
**********************************************************************
File "/storage/jec/sage-4.3.4.alpha1/devel/sage-tests/sage/schemes/elliptic_curves/ell_finite_field.py", line 1269:
    sage: E.gens()
Expected:
    ((0 : 7 : 1),)
Got:
    ((0 : 4 : 1),)
**********************************************************************
File "/storage/jec/sage-4.3.4.alpha1/devel/sage-tests/sage/schemes/elliptic_curves/ell_finite_field.py", line 1423:
    sage: for p in prime_range(10000):           #long time (~20s)
          if p != Integer(389):
              G=E.change_ring(GF(p)).abelian_group()
Exception raised:
    Traceback (most recent call last):
      File "/home/jec/sage-current/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/jec/sage-current/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/jec/sage-current/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_24[17]>", line 3, in <module>
        G=E.change_ring(GF(p)).abelian_group()
      File "/home/jec/sage-current/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_finite_field.py", line 1512, in abelian_group
        Q = self.random_point()
      File "/home/jec/sage-current/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_finite_field.py", line 380, in random_element
        v = self.lift_x(k.random_element(), all=True)
      File "/home/jec/sage-current/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_generic.py", line 836, in lift_x
        return [self.point([x, (-b+d)/2, one], check=False) for d in D.sqrt(all=True)]
    TypeError: 'sage.rings.integer_mod.IntegerMod_int' object is not iterable
**********************************************************************
File "/storage/jec/sage-4.3.4.alpha1/devel/sage-tests/sage/schemes/elliptic_curves/ell_finite_field.py", line 336:
    sage: P = E.random_element(); P
Expected:
    (751 : 10581 : 1)
Got:
    (16740 : 12486 : 1)
**********************************************************************
File "/storage/jec/sage-4.3.4.alpha1/devel/sage-tests/sage/schemes/elliptic_curves/ell_finite_field.py", line 347:
    sage: P = E.random_element(); P
Expected:
    (a^3 + a + 5 : 5*a^4 + 6*a^3 + 5*a^2 + 3*a + 6 : 1)
Got:
    (2*a^4 + 3*a^3 + 5*a^2 + 6*a + 4 : 6*a^4 + 4*a^3 + a + 6 : 1)
**********************************************************************
File "/storage/jec/sage-4.3.4.alpha1/devel/sage-tests/sage/schemes/elliptic_curves/ell_finite_field.py", line 358:
    sage: P = E.random_element(); P
Expected:
    (a^4 + a^3 + a : 1 : 1)
Got:
    (a^4 + a^2 + 1 : a^3 + a : 1)
**********************************************************************
3 items had failures:
   1 of  10 in __main__.example_21
   1 of  25 in __main__.example_24
   3 of  20 in __main__.example_9
***Test Failed*** 5 failures.
For whitespace errors, see the file /home/jec/.sage//tmp/.doctest_ell_finit
```

These are all but one trivial and I'll fix them with a reviewer patch.  But the other one looks stranger.  So some more investigation is required...watch this space!


---

Comment by cremona created at 2010-03-12 17:08:38

replaces previous


---

Attachment

My patch (after reviewing and testing the whole sage library) has to be applied *instead* of Robert's, though it still has his tag on it (sorry).  It does two things relative to his:
    1. I changed a few doctest outputs for the random point tests.  I am worried though, since these changes were not only replacing a point by its negative!  Why?
    2. testing with -long revealed a bug in sqrt() for integer-mods: when 0 then the return was 0 and not [0] which broke the new code since it uses the all=true option.  This was *only* revealed in the -long test!  Take note!!

I left this as "needs review" since it needs someone else (e.g. robertwb) to check my change, especially the one at 2. above, and also I would like to hear views on my other remark under 1.


---

Comment by cremona created at 2010-03-12 17:15:38

PS Robert: why do you care about missing half the group?  the only places I know where this function is used do not care (finding random points in order to find generators for the group of points).  Are you just being pedantic?  We could always add a paramter to the random_point() function which switches on or off this new behaviour?


---

Comment by robertwb created at 2010-03-12 17:32:33

Thanks. I thought I had fixed all the doctest changes. The reason that some tests were changed by more then negation is because there is a second call to random() that updates the state of the random number generator. Regarding remark 2, see #8507. My motivation was actually that when using the all=False flag, half the time an (expensive, especially over non-prime fields) error is raised, but I think the current behavior is better as well. It would be like ZZ.random_element() always returning a positive value.


---

Comment by cremona created at 2010-03-14 14:39:58

Robert, if you are happy with my patch then you could give this a positive review.  Or tell me, and I will.


---

Comment by robertwb created at 2010-03-15 19:18:21

Changing status from needs_review to positive_review.


---

Attachment

Yes, I'm happy with it. I re-posted the patch removing the conflict with #8507, just in case that gets into an alpha before this. 

Release manager: exactly one of `trac_8505-review.patch` or `trac_8505-review-post-8507.patch` should be applied.


---

Comment by jhpalmieri created at 2010-04-17 04:12:39

Changing status from positive_review to needs_work.


---

Comment by jhpalmieri created at 2010-04-17 04:12:39

This (" trac_8505-review-post-8507.patch") doesn't apply cleanly to 4.3.5 or to Sage 4.4.alpha0.  Please rebase it against 4.4.alpha0, and we'll try hard to get this into 4.4.alpha1.


---

Attachment

Rebased on 4.4.alpha0


---

Comment by robertwb created at 2010-04-17 19:27:23

Changing status from needs_work to needs_review.


---

Comment by robertwb created at 2010-04-17 19:28:27

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2010-04-17 19:28:27

Yep, #8311 touched the same code, but it was trivial to merge. I'm remarking this as positive review because it was just a rebase.


---

Comment by jhpalmieri created at 2010-04-19 05:15:48

Merged "8505-ell-finite-random-rebased.patch" into 4.4.alpha1.


---

Comment by jhpalmieri created at 2010-04-19 05:15:48

Resolution: fixed
