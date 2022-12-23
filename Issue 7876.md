# Issue 7876: symbolic expression displayed wrong

Issue created by migration from https://trac.sagemath.org/ticket/7876

Original creator: iandrus

Original creation time: 2010-01-09 13:57:28

Assignee: burcin

It appears that the internal representation is correct since further calculations give correct answers, but the answer is displayed incorrectly.


```
sage: f=(1/2-1/2*I )*sqrt(2)
sage: f
-(1/2*I + 1/2)*sqrt(2)
sage: f+1/2*sqrt(2)
-(1/2*I + 1)*sqrt(2)
sage: f-1/2*sqrt(2)
-1/2*I*sqrt(2)
sage: latex(f)
-\left(\frac{1}{2} I + \frac{1}{2}\right) \, \sqrt{2}
sage: 
```



---

Comment by burcin created at 2010-01-17 06:00:27

Changing status from new to needs_work.


---

Comment by burcin created at 2010-01-17 06:00:27

I fixed this in pynac. attachment:trac_7876-pynac_print.patch contains doctest fixes.

I will post a pynac package with the fix in the next few days.

Thanks a lot for the report.


---

Comment by burcin created at 2010-01-17 06:00:27

Changing keywords from "" to "pynac".


---

Comment by burcin created at 2010-01-17 06:03:15

add doctests


---

Attachment

add one more doctest fix - apply only this patch


---

Attachment

New pynac package available here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.11.spkg

The package contains fixes for #7822, #6961, #7876, #7363, #6465 and #6559. Apart from this ticket, #7363 contains printing changes. Doctests should be run with the patch from that ticket applied as well.


---

Comment by burcin created at 2010-01-19 14:09:15

Changing priority from major to blocker.


---

Comment by burcin created at 2010-01-19 14:09:15

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-01-21 00:12:11

I get a single reject from the patch, in symbolic/random_tests.py on sage.math.  Here is what I have in random_tests.py:


```
        sage: random_expr(50, nvars=3, coeff_generator=CDF.random_element)
        sinh(sinh(-coth(v2)/erf(-(0.615863165633 + 0.879368031485*I)*v1^2*v3) - gamma(pi) + csch(-(0.708874026302 - 0.954135400334*I)*v3)))^coth(-cosh(-polylog((v2 + 0.913564344312 + 0.0898040160336*I)^(-(0.723896589334 - 0.799038508886*I)*v2), -v1 - v3))/arcsin(-(0.0263902659909 + 0.153261789843*I)*arctan2(pi, arccot(pi))))

```


whereas the patch has:


```
         sage: from sage.symbolic.random_tests import *
         sage: random_expr(50, nvars=3, coeff_generator=CDF.random_element)
-        arctanh(sinh(-coth(v2)/erf(-(0.615863165633 + 0.879368031485*I)*v1^2*v3) - gamma(pi) + erf(-(0.708874026302 - 0.954135400334*I)*v3)))^arcsech(-cosh(-polylog((v2 + 0.913564344312 + 0.0898040160336*I)^(-(0.723896589334 - 0.799038508886*I)*v2), -v1 - v3))/arcsin(-(0.0263902659909 + 0.153261789843*I)*arctan2(pi, arccot(pi))))
+        arctanh(sinh(-coth(v2)/erf((-0.615863165633 + 0.879368031485*I)*v1^2*v3) - gamma(pi) + erf((-0.708874026302 - 0.954135400334*I)*v3)))^arcsech(-cosh(-polylog((v2 + 0.913564344312 + 0.0898040160336*I)^((-0.723896589334 - 0.799038508886*I)*v2), -v1 - v3))/arcsin((-0.0263902659909 + 0.153261789843*I)*arctan2(pi, arccot(pi))))
```



---

Comment by jason created at 2010-01-21 01:46:06

See #6559 for the correct order of patches to avoid the reject.


---

Comment by rossk created at 2010-01-25 08:23:02

The following now displays correctly using Sage Version 4.3.1 (Release Date: 2010-01-20)
with pynac 0.1.11 (and also without any patches mentioned in this ticket)


```
sage: f=(1/2-1/2*I )*sqrt(2)

sage: f
(-1/2*I + 1/2)*sqrt(2)

sage: f-1/2*sqrt(2)
-1/2*I*sqrt(2)

sage: f+1/2*sqrt(2)
(-1/2*I + 1)*sqrt(2)

sage: f-I*1/2*sqrt(2)
(-I + 1/2)*sqrt(2)

sage: f-I/2*sqrt(2)
(-I + 1/2)*sqrt(2)

sage: f+I/2*sqrt(2)
1/2*sqrt(2)

sage: latex(f)
\left(-\frac{1}{2} I + \frac{1}{2}\right) \, \sqrt{2}

sage: latex(f+I/2*sqrt(2))
\frac{1}{2} \, \sqrt{2}

sage: (1-I)^2
-2*I

sage: (1+I)^2
2*I

sage: (1+I*sqrt(2))^2
(I*sqrt(2) + 1)^2

sage: expand((1+I*sqrt(2))^2)
2*I*sqrt(2) - 1
```



---

Comment by rossk created at 2010-01-25 08:23:02

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-18 21:40:47

Resolution: fixed


---

Comment by mvngu created at 2010-02-18 21:40:47

Merged [trac_7876-pynac_print.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7876/trac_7876-pynac_print.take2.patch).
