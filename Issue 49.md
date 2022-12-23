# Issue 49: possible bug with p-adic number constructor

Issue created by migration from https://trac.sagemath.org/ticket/49

Original creator: dmharvey

Original creation time: 2006-09-13 14:36:50

Assignee: somebody

I'm not sure if this is a bug, but it sure is confusing to me.


```
sage: K = pAdicField(5, 10)
sage: K(1/2, prec=20)
 3 + 2*5 + 2*5^2 + 2*5^3 + 2*5^4 + 2*5^5 + 2*5^6 + 2*5^7 + 2*5^8 + 2*5^9 + O(5^10)
```


The field's default precision seems to override the precision explicitly requested in the constructor. I can vaguely see how this might make sense, but it gets extremely confusing when you don't even supply the default precision:


```
sage: K = pAdicField(5)
sage: K(1/2, prec=30)
 3 + 2*5 + 2*5^2 + 2*5^3 + 2*5^4 + 2*5^5 + 2*5^6 + 2*5^7 + 2*5^8 + 2*5^9 + 2*5^10 + 2*5^11 + 2*5^12 + 2*5^13 + 2*5^14 + 2*5^15 + 2*5^16 + 2*5^17 + 2*5^18 + 2*5^19 + O(5^20)
```


I think it would be better if the precision requested in the constructor was always honoured, assuming that the input data had enough precision in the first place to support it (which in this case it does, being a Rational number).



---

Comment by dmharvey created at 2006-09-13 14:45:09

Another way of putting this is that the *only* time the default precision should be relevant is when coercing other objects into the field, and this should be overridable in the element constructor. At all other times, e.g. performing arithmetic on two elements, the precision of the *elements* should be the only relevant thing.


---

Comment by dmharvey created at 2006-09-16 05:06:40

Fixed.

Wed Sep 13 08:17:07 PDT 2006  dmharvey`@`math.harvard.edu
  * changed padic constructor precision behaviour:
   * now pAdicField(5)(1/2, 40) actually returns a p-adic number with 40 digits instead of 20
   * added some doctests for rational -> padic coercion


---

Comment by dmharvey created at 2006-09-16 05:06:40

Resolution: fixed
