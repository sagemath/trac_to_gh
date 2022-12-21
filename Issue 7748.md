# Issue 7748: Make incomplete gamma function symbolic

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2009-12-22 17:18:07

Assignee: burcin

CC:  mvngu

We don't appear to have this, though perhaps it is in Pynac/Ginac already.  We also need to translate Maxima's gamma_incomplete to our gamma_inc or incomplete_gamma as part of this ticket.


---

Comment by burcin created at 2009-12-22 23:09:31

After a quick look at the GiNaC sources, I don't think there is an implementation of the incomplete gamma function in there.

Numerical evaluation of this can be done with the `gammainc()` function of mpmath.

The conversion should just work, if the conversions dictionary argument of `BuiltinFunction.__init__` contains `maxima='gamma_incomplete'`.


---

Comment by kcrisman created at 2009-12-23 04:42:36

Replying to [comment:1 burcin]:
> After a quick look at the GiNaC sources, I don't think there is an implementation of the incomplete gamma function in there.
> 
Okay.
> Numerical evaluation of this can be done with the `gammainc()` function of mpmath.
But will it give us symbolic evaluation ala gamma_inc(1,1)=1/e?  That would be best.

> The conversion should just work, if the conversions dictionary argument of `BuiltinFunction.__init__` contains `maxima='gamma_incomplete'`.
Yes, of course, but we still have to do it :)


---

Comment by was created at 2009-12-24 20:17:13

> Numerical evaluation of this can be done with the gammainc() function of mpmath.

Doesn't PARI also have an incomplete gamma implementation (it's used by RR and CC, I think)?


---

Comment by fstan created at 2010-02-07 11:37:27

Make Ei symbolic.


---

Attachment

Make incomplete gamma function symbolic.


---

Comment by fstan created at 2010-02-07 11:42:41

The 2 patches should make the incomplete gamma function symbolic. The exponential integral Ei was used in its symbolic evaluation, therefore it was also made symbolic.


---

Comment by fstan created at 2010-02-07 11:42:41

Changing status from new to needs_review.


---

Comment by zimmerma created at 2010-02-07 21:53:54

I tried the exponential integral patch and it works ok. However I don't understand the changes in
random_tests.py. Also the following could be evaluated:

```
sage: diff(Ei(x),x)
D[0](Ei)(x)
sage: integrate(Ei(x),x)
integrate(Ei(x), x)
```

Should this be in a separate ticket?


---

Comment by kcrisman created at 2010-02-08 02:19:09

Replying to [comment:5 zimmerma]:
> I tried the exponential integral patch and it works ok. However I don't understand the changes in
> random_tests.py. 

This makes a 'random' symbolic expression, and when we add new symbolic functions (and sometimes when we change them) this doctest needs to be changed, not because anything bad happened.


---

Comment by fstan created at 2010-02-08 11:03:15

Replying to [comment:5 zimmerma]:
> I tried the exponential integral patch and it works ok. However I don't understand the changes in
> random_tests.py. Also the following could be evaluated:

```
sage: diff(Ei(x),x)
D[0](Ei)(x)
sage: integrate(Ei(x),x)
integrate(Ei(x), x)
```

> Should this be in a separate ticket?

Thank you for the review. I'll include the derivative and submit again. Integration looks more complicated.

Greetings, 

Flavia


---

Comment by fstan created at 2010-02-08 11:03:15

Changing status from needs_review to needs_work.


---

Comment by zimmerma created at 2010-02-08 13:09:40

Changing assignee from burcin to zimmerma.


---

Comment by zimmerma created at 2010-02-08 13:09:40

I tried sage -t * with both patches, and I get one additional failure with respect to those I get
due to #7773:

```
tarte% sage -t "rings/complex_number.pyx"
sage -t  "rings/complex_number.pyx"                         
**********************************************************************
File "/usr/local/sage-4.3-core2/devel/sage-main/sage/rings/complex_number.pyx", line 1611:
    sage: gamma_inc(2, 5)
Expected:
    0.0404276819945128
Got:
    gamma(2, 5)
```

Consider also the following:

```
sage: gamma_inc(2, 5.)
0.0404276819945128
sage: gamma(2, 5) 
1
```



---

Comment by burcin created at 2010-02-08 16:36:18

Replying to [comment:8 zimmerma]:

> Consider also the following:

```
sage: gamma_inc(2, 5.)
0.0404276819945128
sage: gamma(2, 5) 
1
```


We should write a python function wrapping `gamma_inc` and `gamma`, similar to the provided for `psi()` in #6961.

The fact that `gamma()` accepts two arguments at the moment is a bug that I introduced in #7490. Looking at the code, it also doesn't handle the `prec` parameter correctly. I'll upload a patch with a wrapper `gamma()` function and a fix for the `prec` issue.

Replying to [comment:7 fstan]:

> Integration looks more complicated. 

Integration cannot be handled with a custom method in symbolic functions. The patches attached to #6465 should make this easier.


---

Comment by zimmerma created at 2010-02-10 12:39:43

Flavia, please can you fix the rings/complex_number.pyx issue?


---

Attachment

Added derivative method.


---

Comment by fstan created at 2010-02-15 23:28:10

Fixed tests from complex_number.pyx


---

Attachment

I've uploaded new patches which should fix the docs and the derivative.

Greetings,

Flavia


---

Attachment

rebased to 4.3.3.alpha1


---

Comment by burcin created at 2010-02-20 17:51:53

rebased to 4.3.3.alpha1


---

Attachment

wrapper for gamma and incomplete gamma


---

Attachment

wrapper for gamma and incomplete gamma


---

Comment by burcin created at 2010-02-20 18:03:28

attachment:trac_7748-gamma_wrapper.2.patch adds a new wrapper function to call gamma or incomplete gamma depending on the number of arguments. It also corrects the way `prec` parameter to `gamma` was handled.

Flavia's patches needed to be rebased to 4.3.3.alpha1 since the changes to `random_tests.py` didn't apply anymore.

The patches to be applied are (in this order):
 * attachment:trac_7748-exp_integral_ver2.4.3.3.alpha1.patch
 * attachment:trac_7748-incomplete_gamma_ver2.4.3.3.alpha1.patch
 * attachment:trac_7748-gamma_wrapper.2.patch

I'm changing this to needs review. :)


---

Comment by burcin created at 2010-02-20 18:03:28

Changing status from needs_work to needs_review.


---

Comment by zimmerma created at 2010-02-24 07:27:18

a partial review against 4.3.3:

```
sage -t  "devel/sage-main/sage/schemes/elliptic_curves/ell_rational_field.py"
...
    sage: E.Lambda(1.4+0.5*I, 50)
      File "/usr/local/sage-4.3.3/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 3088, in Lambda
        Gamma_inc = transcendental.gamma_inc
    AttributeError: 'module' object has no attribute 'gamma_inc'
```

This test was ok with vanilla 4.3.3.


---

Comment by zimmerma created at 2010-02-24 07:27:18

Changing status from needs_review to needs_work.


---

Comment by zimmerma created at 2010-02-24 08:40:32

apart from the above failure, all tests pass with sage 4.3.3 (apart from the Fedora 12 Segfaults).


---

Attachment

fix new doctest failure


---

Comment by burcin created at 2010-03-02 11:37:17

I added a fix for the doctest failure in comment:13 to my patch, attachment:trac_7748-gamma_wrapper.3.patch.

The patches to be applied are (in this order): 

    * attachment:trac_7748-exp_integral_ver2.4.3.3.alpha1.patch
    * attachment:trac_7748-incomplete_gamma_ver2.4.3.3.alpha1.patch
    * attachment:trac_7748-gamma_wrapper.3.patch

I am OK with Flavia's changes. If someone can review my patch this can still get in 4.3.4. :)


---

Comment by burcin created at 2010-03-02 11:37:17

Changing status from needs_work to needs_review.


---

Comment by zimmerma created at 2010-03-03 12:24:49

Everything works now. Great work!

Paul


---

Comment by zimmerma created at 2010-03-03 12:24:49

Changing status from needs_review to positive_review.


---

Comment by burcin created at 2010-03-17 08:09:33

Hi Minh,

What is holding up this ticket? Note that it has a positive review and the patches to be applied are listed in comment:15.

Cheers,

Burcin


---

Comment by mvngu created at 2010-03-17 08:13:14

Replying to [comment:17 burcin]:
> What is holding up this ticket?
I can't merge this ticket. We are now in feature freeze.


---

Comment by jhpalmieri created at 2010-04-15 20:15:07

Merged in 4.4.alpha0:

 - trac_7748-exp_integral_ver2.4.3.3.alpha1.patch
 - trac_7748-incomplete_gamma_ver2.4.3.3.alpha1.patch
 - trac_7748-gamma_wrapper.3.patch


---

Comment by jhpalmieri created at 2010-04-15 20:15:07

Resolution: fixed
