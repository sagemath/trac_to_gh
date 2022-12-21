# Issue 6377: exp(x) is broken at x=Infinity and x=-Infinity

Issue created by migration from Trac.

Original creator: gmhossain

Original creation time: 2009-06-21 17:56:25

Keywords: symbolic exp

exponetial function exp(x) is broken at both x=-Infinity
and x=Infinity


```
sage: exp(-Infinity)
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
....
RuntimeError: x*Infinity with non real x encountered.
```




```
sage: exp(Infinity)
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
....
RuntimeError: x*Infinity with non real x encountered.
```



---

Comment by burcin created at 2009-06-22 13:02:26

Set assignee to burcin.


---

Comment by burcin created at 2009-06-22 13:02:26

Changing status from new to assigned.


---

Comment by burcin created at 2009-06-22 13:02:26

Good catch! After adding support for infinity in pynac, I forgot to add cases to handle infinity in the eval functions of special functions. 

The fix for `exp()` needs to go into pynac. I don't know what other functions are effected by this. It would be good to try other special functions defined by Sage to see if they handle infinity, or other constants defined by Sage properly.


---

Attachment

doctests for the fix


---

Comment by burcin created at 2009-07-31 23:56:37

I have a fix for this in my local pynac tree. I will make a new pynac package available soon.

I checked all the functions defined in inifcns_trans.cpp in pynac. The remaining functions still need to be fixed.


---

Comment by burcin created at 2009-08-01 02:32:05

This now depends on the package linked from #6404.

Please follow the instructions on that ticket to apply & test.


---

Comment by gmhossain created at 2009-08-02 18:51:06

Hi Burcin,

I tested this out. It looks fine to me. 

I guess, it would be good if we could follow some standard convention for 
values of these functions at their poles, brunch cuts. For example, following 
looks odd to me

```
sage: arctan(-Infinity)
-1/2*pi
sage: tan(-pi/2)
Infinity
```


May be we should discuss this in sage-devel for adopting a convention for
these special values.

There are some other issues that would need future work. For example, you have
fixed values of log at 0

```
sage: SR(0).log()
-Infinity
```


However, following still raises error

```
sage: log(0)
ValueError ...
```


In any case, this patch fixes lot of issues and should be included.
The remaining issues should be fixed later. I am going to give a positive
review shortly.


---

Comment by gmhossain created at 2009-08-02 19:24:09

Note: I am giving partial positive review because I tested this patch against my stable sage-4.1. So if it applies cleanly on Sage-4.1.1.rc1 then that would be full positive from me.


---

Comment by mvngu created at 2009-08-03 00:31:27

Resolution: fixed


---

Comment by mvngu created at 2009-08-03 00:31:27

I applied patches in the following order:
 1. the spkg `pynac-0.1.8.p2.spkg` at #6404
 1. `trac_6404-conjugate_typesetting.patch`
 1. `trac_6401-real_imag_typesetting.patch`
 1. `trac_6377-exp_infinity.patch`
 1. `trac_6243-fderivative_hash.patch`
All doctests pass in my merge tree. So I'm changing #6404, #6401, #6377 and #6243 to positive review as per Golam's request.
