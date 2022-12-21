# Issue 8943: RuntimeError with series

Issue created by migration from Trac.

Original creator: casamayou

Original creation time: 2010-05-10 09:42:29

Assignee: burcin

Keywords: series, taylor

The function *series* can not give the power series expansion of f(x)=(1+arctan(x))**(1/x) , while *taylor* succeeds. Note that the function f can be continuously extended at 0.


```
sage: taylor((1+arctan(x))**(1/x), x, 0, 3)
1/16*x^3*e + 1/8*x^2*e - 1/2*x*e + e
sage: ((1+arctan(x))**(1/x)).series(x==0, 3)
RuntimeError: power::eval(): division by zero
```



---

Comment by kcrisman created at 2011-03-16 16:18:30

Changing priority from trivial to minor.


---

Comment by kcrisman created at 2011-03-16 16:18:30

Looks like this is in Ginac/Pynac.  But maybe it makes sense _not_ to have an answer here?  After all, the technical definition would imply that f doesn't have a Taylor series there, if it doesn't even exist.  Probably Maxima is more lenient about such things.


---

Attachment

This was fixed upstream in ginac. The changes will be in the next pynac release. Patch with doctest is attached.


---

Comment by burcin created at 2011-05-09 15:10:24

New pynac package with the fix is at #11317.


---

Comment by burcin created at 2011-05-09 15:10:24

Changing status from new to needs_review.


---

Comment by kcrisman created at 2011-05-09 19:04:04

This is nice, and the other examples given by the author also did not work before but now do:

```
sage: (cos(x)^(sin(x)/x)).series(x==0,9)
1 + (-1/2)*x^2 + 1/8*x^4 + (-1/30)*x^6 + 631/120960*x^8 + Order(x^9)
sage: ((1+x)^(1/x)).series(x==0,9)
(e) + (-1/2*e)*x + (11/24*e)*x^2 + (-7/16*e)*x^3 + (2447/5760*e)*x^4 + (-959/2304*e)*x^5 + (238043/580608*e)*x^6 + (-67223/165888*e)*x^7 + (559440199/1393459200*e)*x^8 + Order(x^9)
```


Also, the new series does correctly approximate the original function near x=0 :)


---

Comment by kcrisman created at 2011-05-09 19:04:04

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-05-27 12:01:14

Resolution: fixed
