# Issue 6401: Typesettings of real() and imag() are broken

Issue created by migration from https://trac.sagemath.org/ticket/6401

Original creator: gmhossain

Original creation time: 2009-06-25 11:09:12

Typesetting of real() and imag() methods are broken due to missing parenthesis.


```
sage: latex(x.real())
\Rex
```

"\Rex" is not a valid latex expression. It should be something
like "\Re\left(x\right)".

Similar issues are present also for Symbolic functions

```
sage: f(x) = function('f',x)
sage: latex( f(x).imag())
\Imf\left(x\right)
```

Again it should be similar to "\Im\left(f\left(x\right)\right)".



---

Attachment

doctest fixes for typesetting changes in pynac


---

Comment by burcin created at 2009-07-28 12:45:57

Changing status from new to assigned.


---

Comment by burcin created at 2009-07-28 12:45:57

Set assignee to burcin.


---

Comment by burcin created at 2009-07-28 12:45:57

I have a fix for this in my local pynac tree. I will make a new package with a few more bugfixes available soon.


---

Comment by burcin created at 2009-08-01 02:29:48

This now depends on the package linked from #6404.

Please follow the instructions on that ticket to apply & test.


---

Comment by gmhossain created at 2009-08-02 15:13:01

Hi Burcin,

I am testing out the new pynac spkg. Seems alright to me so far. Out of curiosity: is there
any reason to print the extra spaces around the the argument of real() and imag()?

```
sage: latex(real(x))
\Re \left( x \right)
```

Given it differs a bit from your earlier convention for default typesetting of 
symbolic function

```
sage: psi(x) = function('psi',x)
sage: latex(psi(x))
\psi\left(x\right)
```


Otherwise, I am ready to give positive review as the output is valid latex expression in
both cases.


---

Comment by burcin created at 2009-08-02 15:47:03

There is no specific reason I chose that format. We can change it in the future if we decide on a convention.


---

Comment by gmhossain created at 2009-08-02 19:22:25

Note: I am giving partial positive review because I tested this patch against my stable sage-4.1. So if it applies cleanly on Sage-4.1.1.rc1 then that would be full positive from me.


---

Comment by mvngu created at 2009-08-03 00:30:19

Resolution: fixed


---

Comment by mvngu created at 2009-08-03 00:30:19

I applied patches in the following order:
 1. the spkg `pynac-0.1.8.p2.spkg` at #6404
 1. `trac_6404-conjugate_typesetting.patch`
 1. `trac_6401-real_imag_typesetting.patch`
 1. `trac_6377-exp_infinity.patch`
 1. `trac_6243-fderivative_hash.patch`
All doctests pass in my merge tree. So I'm changing #6404, #6401, #6377 and #6243 to positive review as per Golam's request.
