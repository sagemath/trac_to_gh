# Issue 6404: Typeseting for conjugate() of symbolic function is inadequate

Issue created by migration from https://trac.sagemath.org/ticket/6404

Original creator: gmhossain

Original creation time: 2009-06-25 14:22:31

In current Sage (4.0.2), while typesetting conjugate() of
an symbolic expression, latex symbol "\bar" is used

```
sage: latex(x.conjugate())
\bar{x}
```


The problem with "\bar" is that it is of fixed width and not scalable. For example, this is inadequate for symbolic functions


```
sage: x,y=var('x,y')
sage: f = function('psi',x,y)
sage: latex(f.conjugate())
\bar{\psi\left(x, y\right)
```


A better solution is to use "\overline" instead of "\bar".



---

Attachment

doctest fixes for conjugate typesetting change


---

Comment by burcin created at 2009-07-28 12:14:14

Changing status from new to assigned.


---

Comment by burcin created at 2009-07-28 12:14:14

I have a fix for this in my local pynac tree. I'll make a new pynac package available soon, with some other bug fixes.


---

Comment by burcin created at 2009-07-28 12:14:14

Set assignee to burcin.


---

Comment by burcin created at 2009-08-01 02:27:52

New pynac package is available here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.8.p2.spkg

Besides this issue, it includes fixes for #6401, #6243 and #6377. Please apply the patches from those issues too before doctesting.


---

Comment by gmhossain created at 2009-08-02 19:18:42

Looks OK to me.

Note: I am giving partial positive review because I tested this patch against my stable sage-4.1. So if it applies cleanly on Sage-4.1.1.rc1 then that would be full positive from me.


---

Comment by mvngu created at 2009-08-03 00:28:00

Resolution: fixed


---

Comment by mvngu created at 2009-08-03 00:28:00

I applied patches in the following order:
 1. the spkg `pynac-0.1.8.p2.spkg`
 1. `trac_6404-conjugate_typesetting.patch`
 1. `trac_6401-real_imag_typesetting.patch`
 1. `trac_6377-exp_infinity.patch`
 1. `trac_6243-fderivative_hash.patch`
All doctests pass in my merge tree. So I'm changing #6404, #6401, #6377 and #6243 to positive review as per Golam's request.
