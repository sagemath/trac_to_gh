# Issue 7532: "return NotImplementedError" in ring.pyx

Issue created by migration from https://trac.sagemath.org/ticket/7532

Original creator: was

Original creation time: 2009-11-26 05:37:36

Assignee: AlexGhitza


```
On Wed, Nov 25, 2009 at 7:26 PM, John H Palmieri <jhpalmieri64@gmail.com> wrote:
> In ring.pyx, there is code like this:
>
>        if proof:
>            return NotImplementedError
>        else:
>            return False
>
> I would think that the second line should say "raise
> NotImplementedError".  (Changing it makes some doctests fail,
> though.)  Is there a good reason for doing "return
> NotImplementedError"?

That's *definitely* a bug.   No question about it. 
```



---

Comment by ylchapuy created at 2009-11-26 09:07:47

grep gives:

 * ./symbolic/expression.pyx:        return NotImplementedError
 * ./symbolic/expression_conversions.py:            return NotImplementedError("SymPy function '%s' doesn't exist" % f)
 * ./rings/ring.pyx:            return NotImplementedError
 * ./modular/arithgroup/congroup_gammaH.py:            return NotImplementedError
 * ./geometry/polyhedra.py:            return NotImplementedError


---

Comment by ylchapuy created at 2009-11-26 09:14:11

and allowing other error types we get:

  * ./interfaces/gap.py:            return RuntimeError, "Error evaluating %s in %s"%(line, self)
  * ./modular/abvar/finite_subgroup.py:            return ValueError, "self and other must be in the same ambient Jacobian"
  * ./groups/perm_gps/permgroup_named.py:            return ValueError, "Degree must be 2."
  * ./groups/perm_gps/permgroup_named.py:            return ValueError, "Degree must be 2."


---

Comment by ylchapuy created at 2009-11-26 09:29:49

and also (my grep has a strange behavior..?):

 *./structure/element.pyx:            return ArithmeticError, "Multiplicative order of 0 not defined."
 *./rings/finite_field_givaro.pyx:                return ArithmeticError, "Multiplicative order of 0 not defined."


---

Comment by jhpalmieri created at 2009-11-26 15:45:30

See also #7535.


---

Comment by jhpalmieri created at 2010-01-19 00:50:06

Given the patches at #7535, the one remaining case of this is the one in ring.pyx.  If I make the change from

```
return NotImplementedError
```

to

```
raise NotImplementedError
```

there, I get doctest failures in the files

```
	sage -t -long "devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py"
	sage -t -long "devel/sage/sage/schemes/elliptic_curves/padics.py"
	sage -t -long "devel/sage/sage/schemes/elliptic_curves/sha_tate.py"
```

and maybe some others in this directory.


---

Comment by jhpalmieri created at 2010-01-19 00:50:06

Changing assignee from AlexGhitza to cremona.


---

Comment by jhpalmieri created at 2010-01-19 00:50:06

Changing component from algebra to elliptic curves.


---

Comment by cremona created at 2010-01-19 09:55:48

On my 64-bit ubuntu build of 4.3.1.rc0 with #7535 patches applied, I only get failures in ell_rational_field.py  I'll fix that and try again on a 32-bit machine.


---

Comment by cremona created at 2010-01-19 12:43:49

Apply after the patches at #7535 on 4.3.1.rc0


---

Comment by cremona created at 2010-01-19 12:45:46

Changing status from new to needs_review.


---

Attachment

The attached patch fixes an error in ell_rational_field.py which is the only one I see in that directory after applying the patches at #7535,

John (jhpalmieri), can you post the details of the errors you had on the other 3 files in that directory?


---

Comment by jhpalmieri created at 2010-01-19 18:23:40

Hi John,

I think your patch really belongs on #7535, not here, since it fixes a doctest which was broken by the patches there.  My comment was, if I make another change, this time to ring.pyx (see the new patch), then I get the following doctest failures:

```
$ sage -t -long /Applications/sage/devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py 
sage -t -long "devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py"
**********************************************************************
File "/Applications/sage/devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 1549:
    sage: A = monsky_washnitzer.matrix_of_frobenius(Q, p, M)    # long time
Exception raised:
    Traceback (most recent call last):
      File "/Applications/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Applications/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Applications/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_32[66]>", line 1, in <module>
        A = monsky_washnitzer.matrix_of_frobenius(Q, p, M)    # long time###line 1549:
    sage: A = monsky_washnitzer.matrix_of_frobenius(Q, p, M)    # long time
      File "/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 1606, in matrix_of_frobenius
        F0_reduced = reduce_all(Q, p, F0_coeffs, offset)
      File "/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 1023, in reduce_all
        exact_form = reduce_negative(Q, p, coeffs, offset, exact_form)
      File "/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 757, in reduce_negative
        m = helper_matrix(Q).list()
      File "/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 689, in helper_matrix
        return (1/D) * matrix(Q.base_ring(), 3, 3,
      File "element.pyx", line 1326, in sage.structure.element.RingElement.__div__ (sage/structure/element.c:10897)
      File "coerce.pyx", line 707, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6073)
      File "coerce.pyx", line 1178, in sage.structure.coerce.CoercionModel_cache_maps.get_action (sage/structure/coerce.c:10911)
      File "coerce.pyx", line 1309, in sage.structure.coerce.CoercionModel_cache_maps.discover_action (sage/structure/coerce.c:12070)
      File "coerce.pyx", line 1346, in sage.structure.coerce.CoercionModel_cache_maps.discover_action (sage/structure/coerce.c:12620)
      File "ring.pyx", line 933, in sage.rings.ring.CommutativeRing._pseudo_fraction_field (sage/rings/ring.c:6321)
      File "ring.pyx", line 900, in sage.rings.ring.CommutativeRing.fraction_field (sage/rings/ring.c:6164)
      File "ring.pyx", line 695, in sage.rings.ring.Ring.is_integral_domain (sage/rings/ring.c:5074)
    NotImplementedError
**********************************************************************
File "/Applications/sage/devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 1551:
    sage: B                                                     # long time
Expected:
    [1144 + 264*t + 841*t^2 + 1025*t^3 + O(t^4)  176 + 1052*t + 216*t^2 + 523*t^3 + O(t^4)]
    [   847 + 668*t + 81*t^2 + 424*t^3 + O(t^4)   185 + 341*t + 171*t^2 + 642*t^3 + O(t^4)]
Got:
    [ 514  927]
    [ 702 1036]
**********************************************************************
File "/Applications/sage/devel/sage/sage/schemes/elliptic_curves/monsky_washnitzer.py", line 1562:
    sage: B.det()                                               # long time
Expected:
    11 + 484*t^2 + 451*t^3 + O(t^4)
Got:
    209
**********************************************************************
1 items had failures:
   3 of  70 in __main__.example_32
***Test Failed*** 3 failures.
For whitespace errors, see the file /Users/palmieri/.sage//tmp/.doctest_monsky_washnitzer.py
	 [20.6 s]
exit code: 1024
```

and

```
sage -t -long "devel/sage/sage/schemes/elliptic_curves/padics.py"
**********************************************************************
File "/Applications/sage/devel/sage/sage/schemes/elliptic_curves/padics.py", line 197:
    sage: E.padic_regulator(5, 10)
Exception raised:
    Traceback (most recent call last):
      File "/Applications/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Applications/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Applications/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[3]>", line 1, in <module>
        E.padic_regulator(Integer(5), Integer(10))###line 197:
    sage: E.padic_regulator(5, 10)
      File "/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/padics.py", line 253, in padic_regulator
        height = self.padic_height(p, prec, check_hypotheses=False)
      File "/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/padics.py", line 659, in padic_height
        sigma = self.padic_sigma(p, adjusted_prec, check_hypotheses=False)
      File "/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/padics.py", line 1009, in padic_sigma
        f = X.formal_group().differential(N+2)   # f = 1 + ... + O(t^{N+2})
      File "/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/formal_group.py", line 360, in differential
        x = self.x(prec+1)
      File "/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/formal_group.py", line 253, in x
        y = self.y(prec)
      File "/Applications/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/formal_group.py", line 303, in y
        y = -1/w + O(t**prec)
      File "element.pyx", line 1326, in sage.structure.element.RingElement.__div__ (sage/structure/element.c:10897)
      File "coerce.pyx", line 707, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6073)
      File "coerce.pyx", line 1178, in sage.structure.coerce.CoercionModel_cache_maps.get_action (sage/structure/coerce.c:10911)
      File "coerce.pyx", line 1309, in sage.structure.coerce.CoercionModel_cache_maps.discover_action (sage/structure/coerce.c:12070)
      File "coerce.pyx", line 1346, in sage.structure.coerce.CoercionModel_cache_maps.discover_action (sage/structure/coerce.c:12620)
      File "ring.pyx", line 933, in sage.rings.ring.CommutativeRing._pseudo_fraction_field (sage/rings/ring.c:6321)
      File "ring.pyx", line 900, in sage.rings.ring.CommutativeRing.fraction_field (sage/rings/ring.c:6164)
      File "ring.pyx", line 695, in sage.rings.ring.Ring.is_integral_domain (sage/rings/ring.c:5074)
    NotImplementedError
**********************************************************************
```

plus 45 more failures in padics.py (too many to include here), and I expect failures in sha-tate.py -- currently in the middle of testing and I have to go teach, so I can't wait for it to finish.


---

Attachment

for purposes of illustration only -- causes doctest failures in schemes/elliptic_curves


---

Comment by cremona created at 2010-01-19 20:18:58

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2010-01-19 20:18:58

OK, I'll move my patch from here to #7535.  I'll also take a look at those other files to see if I can work out what is going on.


---

Comment by timdumol created at 2010-01-20 09:41:11

Positive review: see comment:7:ticket:7535


---

Comment by timdumol created at 2010-01-20 09:41:11

Resolution: fixed


---

Comment by timdumol created at 2010-01-20 09:41:46

Changing status from closed to needs_work.


---

Comment by timdumol created at 2010-01-20 09:41:46

That should have been positive review. Sorry about that.


---

Comment by timdumol created at 2010-01-20 09:41:56

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2010-01-20 09:42:00

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-01-20 10:26:01

I have got to the bottom of (at least) the problem with monsky_washnitser.py.  A quantity D is computed which is in `(Z/NZ)[This is the Trac macro *t* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#t-macro)` and non-zero, where N is a prime power not a prime.  At some point in the code we need 1/D.  This crashes (while `D^(-1)` is OK).  IN the inversion, soemone asks if the parent of D is an integral domain which cannot be determined, which raises a run-time error.  Before the patch it *returned* the error, and as it was returning something nonzero that was interpreted by python as "True".

I think I can fix this, but I am still working on it.  It will need a new patch -- sorry to have muddled matters by putting onto this ticket a patch which belonged to #7535.


---

Comment by cremona created at 2010-01-20 13:08:53

Apply instead of previous one to 4.3.1.rc0 (rings.pyx fix)


---

Attachment

The patch trac_7532-rings.patch  fixes the problem in rings.pyx and all the fallout -- I checked the entire library and it is fine.  The diagnosis was exactly as above, and only a few lines needed to be changed!

I am switchingg this to "needs work" and then "needs review", hoping that it can get in on the back of #7535 (just this once!)


---

Comment by cremona created at 2010-01-20 13:10:48

Changing status from positive_review to needs_work.


---

Comment by cremona created at 2010-01-20 13:10:58

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-01-20 16:38:44

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-01-20 16:38:44

Looks good, all tests pass.  Thanks for the fix, John.


---

Comment by cremona created at 2010-01-20 17:01:34

Replying to [comment:18 jhpalmieri]:
> Looks good, all tests pass.  Thanks for the fix, John.

My pleasure.  I hope the release manager can see that trac_7532.patch only needs to be applied once, not both here and at #7535!

I only just discovered the joys of "sage -pt n" which makes testing the whole library a breeze: my research machine has 16 processors of which only a few are usually in use, so I put n=10 and a full test only takes 6 minutes and the -long test I did here took only 701s!


---

Comment by mvngu created at 2010-01-23 17:45:58

First I applied patches at #7535 to Sage 4.3.1, then I applied [trac_7532-rings.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7532/trac_7532-rings.patch). Running doctest on the full Sage library results in the following failure:

```
[mvngu@sage sage-4.3.1]$ ./sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py
sage -t -long "devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py"
**********************************************************************
File "/mnt/usb1/scratch/mvngu/release/sage-4.3.1/devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py", line 4027:
    sage: E.isogenies_prime_degree(4)
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/mvngu/release/sage-4.3.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/mvngu/release/sage-4.3.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/mvngu/release/sage-4.3.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_86[14]>", line 1, in <module>
        E.isogenies_prime_degree(Integer(4))###line 4027:
    sage: E.isogenies_prime_degree(4)
      File "/mnt/usb1/scratch/mvngu/release/sage-4.3.1/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 4036, in isogenies_prime_degree
        return isogenies_sporadic_Q(self, l)
      File "/mnt/usb1/scratch/mvngu/release/sage-4.3.1/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_curve_isogeny.py", line 4004, in isogenies_sporadic_Q
        raise ValueError("%s is not prime."%l)
    ValueError: 4 is not prime.
```

Did I correctly apply the necessary patches? Does this ticket depend on #7535?


---

Comment by jhpalmieri created at 2010-01-23 18:30:48

Please apply trac_7532.patch as well.  Does that help?  (See the "addendum" in the ticket description.)


---

Comment by mvngu created at 2010-01-23 20:03:36

Thank you for pointing out the addendum, jhpalmieri.  Merged in this order:

 1. patches at #7535
 1. [trac_7532.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7532/trac_7532.patch)
 1. [trac_7532-rings.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7532/trac_7532-rings.patch)
