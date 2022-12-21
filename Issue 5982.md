# Issue 5982: Can't construct fraction field

Issue created by migration from Trac.

Original creator: jmbr

Original creation time: 2009-05-04 23:19:45

Assignee: tbd

CC:  malb

----------------------------------------------------------------------
the GUI, and license() for information.  |
----------------------------------------------------------------------
| Sage Version 3.4, Release Date: 2009-03-11 | | Type notebook() for
sage: R.<x, y> = PolynomialRing(QQ, 2) sage: I = (x^2 + y^2 - 1)*R
sage: Q = R.quotient(I) sage: Q Quotient of Multivariate Polynomial
Ring in x, y over Rational Field by the ideal (x^2 + y^2 - 1) sage:
Q.fraction_field()
---------------------------------------------------------------------------
NotImplementedError Traceback (most recent call last)

...


---

Attachment

Fix/workaround using Macaulay 2


---

Comment by jmbr created at 2009-05-04 23:23:26

[with patch, needs review]


```
----------------------------------------------------------------------
the GUI, and license() for information.  |
----------------------------------------------------------------------
| Sage Version 3.4, Release Date: 2009-03-11 | | Type notebook() for
sage: R.<x, y> = PolynomialRing(QQ, 2) sage: I = (x^2 + y^2 - 1)*R
sage: Q = R.quotient(I) sage: Q Quotient of Multivariate Polynomial
Ring in x, y over Rational Field by the ideal (x^2 + y^2 - 1) sage:
Q.fraction_field()
---------------------------------------------------------------------------
NotImplementedError Traceback (most recent call last)

...
```



---

Comment by mabshoff created at 2009-05-05 01:28:51

Hi,

M2 isn't a default part of Sage, so the doctest must be made optional. I also don't see a reason why this cannot be implemented via libSingular for example, but maybe I am overlooking things.

You also posted a diff, so please check in the code and post an hg patch to properly preserve credit. 

And since you are not listed at http://trac.sagemath.org/sage_trac/wiki please add yourself there.

Cheers,

Michael


---

Comment by jmbr created at 2009-05-06 16:59:07

Hi Michael,

Attached is a Mercurial bundle with the same patch plus the docstring modifications you requested.  I'd like to write a native Sage implementation of this in the future but for now this works well enough for me.

Regards,


---

Comment by mabshoff created at 2009-05-06 21:47:17

Hi Juan,

a patch would have been better, but someone can extra the changeset from the bundle and post the patch.

One more thing: When you post an updated patch you need to change the summary to read "needs review" again.

Cheers,

Michael


---

Attachment


---

Comment by ncalexan created at 2009-06-19 22:25:03

`trac_5982-ncalexan.patch` replaces all others.  This version doesn't use Macaulay2, but it could be really slow.


---

Comment by craigcitro created at 2009-06-20 21:43:00

Would it be reasonable to have both versions of `is_prime` added, with a flag for which to use (defaulting to `native`, but with `M2` an option)? This way, if there were cases that one cared about but were slow, one could call off to M2 and (hopefully) get an answer back faster ...


---

Comment by ncalexan created at 2009-06-21 08:17:45

I thought about doing exactly that, but if you're clever enough to know one is better than the other, aren't you clever enough to call `_macaulay2_().isPrime()`?  Also, as far as I can tell, the Macaulay2 algorithm is the same as the Singular.


---

Comment by jmbr created at 2009-06-21 10:20:29

Hi Nick,

Could you point me to the location of Singular's ideal primality testing algorithm?  Thanks


---

Comment by ncalexan created at 2009-06-21 18:39:51

Replying to [comment:11 jmbr]:
> Hi Nick,
> 
> Could you point me to the location of Singular's ideal primality testing algorithm?  Thanks

AFAICT, Singular does not have a toplevel isprime() (or ismaximal()) function.  Reading some mailing list posts regarding Singular and Macaulay2, I believe both implement the same two algorithms for calculating the complete primary decomposition of an ideal.  I don't understand enough to say definitively and I may be misusing the complete primary decomposition for testing primality.  I was hoping that Martin Albrecht would review and clarify the situation.


---

Comment by malb created at 2009-06-21 20:36:14

The patch looks good to me, I didn't run doctests though. I can't really clarify the situation any more than what Nick wrote above.


---

Comment by jmbr created at 2009-06-21 20:53:42

As far as I can recall, Macaulay2 implements the Gianni-Trager-Zacharias algorithm for primality testing instead of relying on primary decomposition.

Best regards


---

Comment by was created at 2009-07-21 04:51:47

Positive review modulo fixing this one trivial change to a doctest:

```
wstein`@`sage:~/build/sage-4.1$ ./sage -t  devel/sage/sage/rings/quotient_ring.py
sage -t  "devel/sage/sage/rings/quotient_ring.py"           
**********************************************************************
File "/scratch/wstein/build/sage-4.1/devel/sage/sage/rings/quotient_ring.py", line 442:
    sage: Q.is_integral_domain()
Expected:
    Traceback (most recent call last):
    ...
    NotImplementedError
Got:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_13[7]>", line 1, in <module>
        Q.is_integral_domain()###line 442:
    sage: Q.is_integral_domain()
      File "/scratch/wstein/build/sage-4.1/local/lib/python/site-packages/sage/rings/quotient_ring.py", line 447, in is_integral_domain
        return self.defining_ideal().is_prime()
      File "/scratch/wstein/build/sage-4.1/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 854, in is_prime
        CPD = self.complete_primary_decomposition(**kwds)
      File "/scratch/wstein/build/sage-4.1/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 401, in __call__
        raise ValueError("Coefficient ring must be a field for function '%s'."%(self.f.__name__))
    ValueError: Coefficient ring must be a field for function 'complete_primary_decomposition'.
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_13
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/wstein/build/sage-4.1/tmp/.doctest_quotient_ring.py
         [1.8 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/rings/quotient_ring.py"
Total time for all tests: 1.8 seconds
wstein`@`sage:~/build/sage-4.1$ 
```



---

Attachment

Minh (or whoever merges this),

Apply *only* trac_5982-ncalexan-with-check.patch.  Note that you'll have to check it in as Nick Alexander and "Juan M. Bello Rivas <jmbr`@`superadditive.com>" when applying the patch, since Juan didn't use HG evidently.


---

Attachment

reviewer patch: fix ReST typos


---

Comment by mvngu created at 2009-08-23 11:12:05

The reviewer patch `trac_5982-reviewer.patch` fixes some ReST typos in `trac_5982-ncalexan-with-check.patch` so that the reference manual builds without warnings. After applying patches in this order:

 1. `trac_5982-ncalexan-with-check.patch`
 1. `trac_5982-reviewer.patch`
 
I get the following doctest failure:

```
sage -t -long devel/sage-main/sage/schemes/hyperelliptic_curves/jacobian_morphism.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/schemes/hyperelliptic_curves/jacobian_morphism.py", line 297:
    sage: J = H.jacobian()(F); J
Expected:
    verbose 0 (919: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.
    Set of points of Jacobian of Hyperelliptic Curve over Finite Field of size 1000000000000000000000000000057 defined by y^2 + 2*x*y = x^7 + x^2 + 1 defined over Finite Field of size 1000000000000000000000000000057
Got:
    verbose 0 (964: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.
    Set of points of Jacobian of Hyperelliptic Curve over Finite Field of size 1000000000000000000000000000057 defined by y^2 + 2*x*y = x^7 + x^2 + 1 defined over Finite Field of size 1000000000000000000000000000057
**********************************************************************
1 items had failures:
   1 of  20 in __main__.example_4
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_jacobian_morphism.py
	 [3.1 s]
```



---

Comment by jason created at 2009-09-29 07:42:17

It looks like the difference is just the line number of the doctest...


---

Comment by mhansen created at 2009-10-05 19:06:39

All tests pass for me when I tried the two patches.  I'm giving this a positive review again.  The doctest in question has "..." where the 919/964 are.


---

Comment by mhansen created at 2009-10-16 08:40:17

Changing status from positive_review to needs_work.


---

Comment by mhansen created at 2009-10-16 08:40:17

In 4.1.2, I get a number of failures arising from NotImplementedErrors in is_integral_domain.


---

Comment by davidloeffler created at 2011-01-23 18:36:18

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2011-01-23 18:36:18

Curiously, all tests in sage/rings and sage/schemes pass for me under sage 4.6.2.alpha1. I'm going to reinstate the "needs review", since I can't replicate mhansen's problem. We'll see if patchbot agrees :-)

Apply trac_5982-ncalexan-with-check.patch, trac_5982-reviewer.patch


---

Comment by davidloeffler created at 2011-01-23 19:30:00

Patchbot seems to be happy with it, but a full ptestlong run on my 4.6.2.alpha1 build revealed a couple of failures: `sage/algebras/quatalg/quaternion_algebra.py` and `sage/matrix/tests.py`. Both of these are to do with the symbolic ring, which (rather oddly) knows it's a field but isn't sure if it's an integral domain. These can be squashed by simply moving the field check to before the integral domain check.


---

Attachment

Why is this

```
        The following is Trac #5982.  Note that the quotient ring 
        is not recognized as being a field at this time, so the 
        fraction field is not the quotient ring itself:: 
 
            sage: Q = R.quotient(I); Q 
            Quotient of Multivariate Polynomial Ring in x, y over Rational Field by the ideal (x^2 - y^2 - 1) 
            sage: Q.fraction_field() 
            Fraction Field of Quotient of Multivariate Polynomial Ring in x, y over Rational Field by the ideal (x^2 - y^2 - 1) 
```

part of the documentation of `is_prime` and not of `fraction_field`?

All tests pass with these patches on sage-4.6.2.alpha4. Patches fix the problem in the ticket description, and all changes look good.


---

Comment by cremona created at 2011-04-22 15:20:28

Marco, did you forget to mark this as "positive review"?


---

Comment by mstreng created at 2011-04-22 15:45:44

Replying to [comment:27 cremona]:
> Marco, did you forget to mark this as "positive review"?

Actually, I was waiting for an answer to my question first, and then forgot all about the ticket.

If I recall correctly, the question was not that important.


---

Comment by mstreng created at 2011-04-22 15:45:44

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-04-25 13:18:41

[attachment:trac_5982-ncalexan-with-check.patch] is not a proper `hg` changeset.  Patches should be made using `hg export tip` and not `hg diff`.


---

Comment by jdemeyer created at 2011-04-25 13:18:41

Changing status from positive_review to needs_work.


---

Comment by mstreng created at 2011-04-28 10:38:14

proper hg changeset version of trac_5982-ncalexan-with-check.patch


---

Comment by mstreng created at 2011-04-28 10:41:08

Changing status from needs_work to positive_review.


---

Attachment

I made that patch into a proper hg changeset. All tests still pass, and as the new patch does exactly the same as the old one, I put it back to positive_review.

(apply [attachment:trac_5982-ncalexan-with-check2.patch], [attachment:trac_5982-reviewer.patch], [attachment:trac_5982_review2.patch])


---

Attachment

the difference between trac_5982-ncalexan-with-check.patch and trac_5982-ncalexan-with-check2.patch


---

Comment by mstreng created at 2011-04-28 10:47:39

(apply trac_5982-ncalexan-with-check2.patch, trac_5982-reviewer.patch, trac_5982_review2.patch)


---

Comment by mstreng created at 2011-04-28 10:50:02

(apply trac_5982-ncalexan-with-check2.patch, trac_5982-reviewer.patch, trac_5982_review2.patch )


---

Comment by jdemeyer created at 2011-05-03 12:28:22

Resolution: fixed
