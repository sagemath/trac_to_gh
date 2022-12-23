# Issue 1214: error in polynomial ideal membership testing

Issue created by migration from https://trac.sagemath.org/ticket/1214

Original creator: mhansen

Original creation time: 2007-11-20 05:33:53

Assignee: malb


```
sage: x^2 in I
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/opt/maple11/lib/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/ideal.py in __contains__(self, x)
    315         if self.gen().is_zero():
    316             return x.is_zero()
--> 317         return self.gen().divides(x)
    318     
    319     def __cmp__(self, other):

<type 'exceptions.AttributeError'>: 'Polynomial_rational_dense' object has no attribute 'divides'
```



---

Comment by mhansen created at 2007-11-20 05:43:43


```
sage: P.<x> = PolynomialRing(QQ)
sage: I = P.ideal(x^2-2)
sage: x^2 in I
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/opt/maple11/lib/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/ideal.py in __contains__(self, x)
    315         if self.gen().is_zero():
    316             return x.is_zero()
--> 317         return self.gen().divides(x)
    318     
    319     def __cmp__(self, other):

<type 'exceptions.AttributeError'>: 'Polynomial_rational_dense' object has no attribute 'divides'
sage: P.<x> = PolynomialRing(ZZ)
sage: I = P.ideal(x^2-2)
sage: x^2 in I
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/opt/maple11/lib/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/rings/ideal.py in __contains__(self, x)
    315         if self.gen().is_zero():
    316             return x.is_zero()
--> 317         return self.gen().divides(x)
    318     
    319     def __cmp__(self, other):

<type 'exceptions.AttributeError'>: 'sage.rings.polynomial.polynomial_integer_dense_ntl' object has no attribute 'divides'
```



---

Attachment


---

Comment by mhansen created at 2007-11-20 05:51:05

Changing assignee from malb to mhansen.


---

Comment by mhansen created at 2007-11-20 05:51:05

Changing status from new to assigned.


---

Comment by ncalexan created at 2007-11-23 20:06:28

This patch should be applied -- doctests are excellent and I think the divides() function is good.

There is a typo:

```
 	1624	    def divides(self, x): 
 	1625	        """ 
 	1626	        Return True if self divides n. 
```


$n$ should be $x$.


---

Comment by mabshoff created at 2007-12-01 18:47:33

Merged in 2.8.15.alpha1 - I corrected the documentation as Nick suggested.


---

Comment by mabshoff created at 2007-12-01 18:47:33

Resolution: fixed
