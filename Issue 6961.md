# Issue 6961: provide wrapper for psi function of GiNaC

Issue created by migration from https://trac.sagemath.org/ticket/6961

Original creator: burcin

Original creation time: 2009-09-19 15:32:32

From sage-support:


```
On Fri, 18 Sep 2009 15:47:45 -0700 (PDT)
The_Fool <masterfulet@yahoo.com> wrote:

> While working with the derivative of the Gamma function, the digamma
> function is obviously involved.  The sage "diff" function does show Γ
> '(x) == Γ(x)ψ(x) like it should, however, the digamma function (called
> psi in sage) is not defined whenever I try to do anything with it.  It
> seems as if only the output of "diff" can use this function.
```


`psi()` is defined in GiNaC, but we don't provide wrappers for it.

Defining a function `psi`, similar to the way `arctan2` is defined in line 422 of `sage/functions/trig.py` should fix this.


The sage-support thread is here:

http://groups.google.com/group/sage-support/browse_thread/thread/1ad313c921b7dbc0


---

Comment by zimmerma created at 2009-09-21 06:45:20

More precisely:

```
sage: diff(gamma(x), x)
gamma(x)*psi(x)
```

but "psi" is unknown to Sage...


---

Attachment

wrappers for psi function from pynac


---

Comment by burcin created at 2010-01-17 05:05:49

Changing status from new to needs_work.


---

Comment by burcin created at 2010-01-17 05:05:49

It turns out defining this function wasn't as straightforward as I thought. Pynac defines 2 functions with the same name `psi`. :)

attachment:trac_6961-psi.patch wraps these 2 functions, and provides a global `psi()` to call the appropriate one. Unpickling these correctly requires changes in pynac. I'll make a new pynac package available later this week.


---

Comment by burcin created at 2010-01-19 14:05:17

Changing status from needs_work to needs_review.


---

Comment by burcin created at 2010-01-19 14:05:17

New pynac package available here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.11.spkg

The package contains fixes for #7822, #6961, #7876, #7363, #6465 and #6559. From these #7876 and #7363 contain printing fixes. Doctests should be run at least with patches from these two tickets.


---

Comment by mvngu created at 2010-01-25 19:30:14

The patch on this ticket conflicts with #6207. If I first apply the patches on #6207 to Sage 4.3.1, and then [trac_6961-psi.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6961/trac_6961-psi.patch), I would get a hunk failure:

```
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6207/trac_6207.patch && hg qpush
adding trac_6207.patch to series file
applying trac_6207.patch
now at: trac_6207.patch
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6207/trac_6207-part2.patch && hg qpush
adding trac_6207-part2.patch to series file
applying trac_6207-part2.patch
now at: trac_6207-part2.patch
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6207/trac_6207-review.patch && hg qpush
adding trac_6207-review.patch to series file
applying trac_6207-review.patch
now at: trac_6207-review.patch
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6961/trac_6961-psi.patch && hg qpush
adding trac_6961-psi.patch to series file
applying trac_6961-psi.patch
patching file sage/symbolic/pynac.pyx
Hunk #2 FAILED at 1566
1 out of 3 hunks FAILED -- saving rejects to file sage/symbolic/pynac.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_6961-psi.patch
```

Perhaps you want to rebase [trac_6961-psi.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6961/trac_6961-psi.patch) on top of #6207?


---

Comment by mvngu created at 2010-01-25 19:30:14

Changing status from needs_review to needs_work.


---

Attachment

rebased


---

Comment by burcin created at 2010-01-25 20:23:35

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-01-28 21:07:45

The unrebased patch is fine; I can't get the other patches in the symbolics queue to work off of the rebase, not yet anyway.

If there is time, would it be possible to make an alias polygamma = psi2?  Not just because Mma uses it, but because a lot of references call it that (such as the ones a students of mine is using for some research) in written form.  This is great functionality to add, though.


---

Comment by kcrisman created at 2010-02-04 03:23:10

Replying to [comment:3 burcin]:
> New pynac package available here:
> 
> http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.11.spkg
> 

Now apparently at boxen.math instead.


---

Comment by rossk created at 2010-02-15 08:03:25

Changing status from needs_review to positive_review.


---

Comment by rossk created at 2010-02-15 08:03:25

Changing keywords from "" to "psi, gamma, digamma, polygamma".


---

Comment by rossk created at 2010-02-15 08:03:25


```
sage: diff(gamma(x),x)/gamma(x) # definition of digamma (or "psi")
psi(x)

sage: diff(gamma(x),x).subs(x=1)
-euler_gamma

sage: psi(1)
-euler_gamma

# analytical result
sage: psi(1/2)
-euler_gamma - 2*log(2)

# numerical examples
sage: psi(.5)
-1.96351002602142

sage: psi(.5r)
-1.9635100260214233

sage: psi(complex(.5))
(-1.9635100260214233+0j)

# 1st argument means 0'th derivative (so psi(0, x) = psi(x))
sage: psi(0, .5)
psi(0.500000000000000)

sage: N(psi(0, .5))
-1.96351002602142
```



---

Attachment

fix doctest failure


---

Comment by mvngu created at 2010-02-18 04:08:17

Changing status from positive_review to needs_work.


---

Comment by mvngu created at 2010-02-18 04:08:46

Changing status from needs_work to needs_review.


---

Comment by mvngu created at 2010-02-18 04:08:46

I applied patches in the following order against Sage 4.3.3.alpha0, together with the updated package [pynac-0.1.11.spkg](http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.11.spkg):

 1. #6961: [trac_6961-psi.rebased.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6961/trac_6961-psi.rebased.patch)
 1. #7822: [trac_7822-py_log.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7822/trac_7822-py_log.take2.patch)
 1. #7876: [trac_7876-pynac_print.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7876/trac_7876-pynac_print.take2.patch)
 1. #7363
 1. #7957
 1. #7916: [trac_7916-same_name_method.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7916/trac_7916-same_name_method.take2.patch)
 1. #6465: 
  1. [trac_6465-chain_rule.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6465/trac_6465-chain_rule.take2.patch) 
  1. [trac_6465-moves-integration-into-sfunction-subclass.take3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6465/trac_6465-moves-integration-into-sfunction-subclass.take3.patch)
  1. [trac_6465-integral.take4.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6465/trac_6465-integral.take4.patch)
 1. #6559: 
  1. [trac_6559-domain-and-latex_name-for-variable.take2.3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6559/trac_6559-domain-and-latex_name-for-variable.take2.3.patch) 
  1. [trac_6559-referee.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6559/trac_6559-referee.take2.patch)

All doctests passed except for this trivial failure:

```
[mvngu@sage sage-4.3.3.alpha0.1]$ ./sage -t -long devel/sage/sage/rings/arith.py
sage -t -long "devel/sage/sage/rings/arith.py"              
**********************************************************************
File "/dev/shm/mvngu/sandbox/sage-4.3.3.alpha0.1/devel/sage/sage/rings/arith.py", line 287:
    sage: factorial(-32)
Expected:
    Traceback (most recent call last):
    ...
    ValueError: factorial -- self = (-32) must be nonnegative
Got:
    Traceback (most recent call last):
      File "/dev/shm/mvngu/sandbox/sage-4.3.3.alpha0.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.3.3.alpha0.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.3.3.alpha0.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[10]>", line 1, in <module>
        factorial(-Integer(32))###line 287:
    sage: factorial(-32)
      File "/dev/shm/mvngu/sandbox/sage-4.3.3.alpha0.1/local/lib/python/site-packages/sage/rings/arith.py", line 315, in factorial
        raise ValueError, "factorial -- must be nonnegative"
    ValueError: factorial -- must be nonnegative
**********************************************************************
1 items had failures:
   1 of  11 in __main__.example_3
***Test Failed*** 1 failures.
For whitespace errors, see the file /dev/shm/mvngu/dot_sage/tmp/.doctest_arith.py
	 [50.3 s]
```


The failure is fixed via [trac_6961-doctest.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6961/trac_6961-doctest.patch), so only this latter patch needs some reviewing love. I'm happy with both #6465 and #6559. If my patch is OK, then these 8 tickets can be closed: #6961, #7822, #7876, #7363, #7957, #7916, #6465, #6559.


---

Comment by burcin created at 2010-02-18 09:26:54

Hi Minh,

Your patch looks ok to me. I'm switching this to positive review.

It's be truly awesome if all those tickets can get merged in this release. :)

Cheers,

Burcin


---

Comment by burcin created at 2010-02-18 09:26:54

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-18 21:57:09

Resolution: fixed


---

Comment by mvngu created at 2010-02-18 21:57:09

Merged in this order:

 1. #6961: [trac_6961-psi.rebased.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6961/trac_6961-psi.rebased.patch)
 1. #7822
 1. #7876
 1. #7363
 1. #7957
 1. #7916
 1. #6465
 1. #6559
 1. #6961: [trac_6961-doctest.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6961/trac_6961-doctest.patch)
