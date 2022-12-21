# Issue 6504: Add doctests to toy_buchberger to get it to 100%

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2009-07-09 22:52:51

Assignee: tbd

Keywords: groebner basis, buchberger

Some functions were missing doctests, I think I have corrected that.


---

Attachment

Patches are the same, I just forgot to put the ticket number on the first one.


---

Comment by malb created at 2009-07-13 20:12:23

fixes a few whitespace issues in the original patch


---

Attachment

I read the patch and it looks fine, it applies cleanly and passes doctest. There were a few whitespace issues w.r.t. the reference manual, which are fixed in the attached patch (only apply this one). The update needs signing off by mhampton.


---

Attachment

supersedes previous versions; better ref manual formatting


---

Comment by mhampton created at 2009-07-14 03:56:16

I switched spol from a lambda definition to a documented function, since it seems important enough in this module.  I also cleaned up a few things for the reference manual formatting (OUTPUT sections were in bold, for example, unintentionally).

Martin Albrect (malb) should get both contributor and reviewer credit for this, I think.  But now that I have made a new version, I think it is appropriate that he reviews again (hopefully for a final time).


---

Comment by malb created at 2009-07-14 09:26:39

Apply only trac_6504_toy_buch.3.patch.


---

Comment by mvngu created at 2009-07-19 00:19:40

With the patch `trac_6504_toy_buch.3.patch`, I'm seeing some doctest failures:

```
sage -t -long devel/sage-exp/sage/rings/polynomial/multi_polynomial_ideal.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-exp/sage/rings/polynomial/multi_polynomial_ideal.py", line 944:
    sage: I.dimension()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_19[9]>", line 1, in <module>
        I.dimension()###line 944:
    sage: I.dimension()
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 402, in __call__
        return self.f(self._instance, *args, **kwds)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 978, in dimension
        gb = toy_buchberger.buchberger_improved(self)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/toy_buchberger.py", line 279, in buchberger_improved
        h = spol(g1,g2).reduce(G)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/toy_buchberger.py", line 175, in spol
        return p(fg_lcm/LT(f)*f - fg_lcm/LT(g)*g)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ring.py", line 422, in __call__
        raise TypeError, "unable to coerce since the denominator is not 1"
    TypeError: unable to coerce since the denominator is not 1
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1.alpha0/devel/sage-exp/sage/rings/polynomial/multi_polynomial_ideal.py", line 948:
    sage: I.dimension()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_19[11]>", line 1, in <module>
        I.dimension()###line 948:
    sage: I.dimension()
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 402, in __call__
        return self.f(self._instance, *args, **kwds)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 978, in dimension
        gb = toy_buchberger.buchberger_improved(self)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/toy_buchberger.py", line 279, in buchberger_improved
        h = spol(g1,g2).reduce(G)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/toy_buchberger.py", line 175, in spol
        return p(fg_lcm/LT(f)*f - fg_lcm/LT(g)*g)
      File "/scratch/mvngu/release/sage-4.1.1.alpha0/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ring.py", line 422, in __call__
        raise TypeError, "unable to coerce since the denominator is not 1"
    TypeError: unable to coerce since the denominator is not 1
**********************************************************************
1 items had failures:
   2 of  15 in __main__.example_19
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1.alpha0/tmp/.doctest_multi_polynomial_ideal.py
	 [13.4 s]

```



---

Comment by mhampton created at 2009-07-19 14:23:39

Fixed an issue with spol function


---

Attachment

OK, I fixed the spol function so that multi_polynomial_ideal.py passes tests as well.  I had thought what I had done was equivalent but I guess not over finite fields - actually I wonder if this is a failure in coercion but that's beyond the scope of this ticket.


---

Comment by mhampton created at 2009-07-19 14:25:38

New patch is cumulative, its the only one that needs to be applied.


---

Comment by mvngu created at 2009-07-24 08:41:57

Resolution: fixed
