# Issue 365: very serious infinite loop in coercion somewhere

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-05-17 15:47:05

Assignee: somebody


```
On 5/17/07, Prof. J. E. Cremona <john.cremona`@`nottingham.ac.uk> wrote:
> 
> Problem:  when executing the following, the last line takes forever and
> had to be killed:
> 
> R = PolynomialRing(QQ, ['a','b','c','d','e'], 5)
> K = R.fraction_field()
> a,b,c,d,e = K.gens()
> 
> ig = 12*a*e-3*b*d+c^2
> jg = 72*a*c*e+9*b*c*d-27*a*d^2-27*e*b^2-2*c^3
> hg = 8*a*c-3*b^2
> deltag = 4*ig^3-jg^2
> 
> Ky.<y> = PolynomialRing(K,'y')
> phipoly = y^3-3*ig*y+jg
> 
> What am I missing?

Nothing --  You have found a subtle bug in SAGE's coercion code.  
If you make the coercion that is going on in the last line very explicit,
then the above line works, e.g., this works (note that I've used some
more compact notation at the beginning, but it's equivalent to
what you wrote):

{{{
R.<a,b,c,d,e> = QQ[]
K = R.fraction_field()
a,b,c,d,e = K.gens()
ig = 12*a*e-3*b*d+c^2
jg = 72*a*c*e+9*b*c*d-27*a*d^2-27*e*b^2-2*c^3
hg = 8*a*c-3*b^2
deltag = 4*ig^3-jg^2
}}}

{{{
Ky.<y> = PolynomialRing(K,'y')
phipoly = y^3-3*ig*y+Ky([jg])
phipoly
///
y^3 + (-3*c^2 + 9*b*d - 36*a*e)*y + -2*c^3 + 9*b*c*d - 27*b^2*e - 27*a*d^2 + 72*a*c*e
}}}

The difference is that I put Ky([jg]) explicitly instead of jg.  

Whatever is causing this is a serious bug, and I hope somebody fixes
it soon (or that I do).  It's trac #

```



---

Comment by was created at 2007-05-18 15:46:04

Resolution: fixed


---

Comment by was created at 2007-05-18 15:46:04

This is fixed now.  It was a problem in the __call__ method of polynomial ring.


```
`@``@` -156,6 +163,8 `@``@` class PolynomialRing_general(sage.algebr
         C = self.__polynomial_class
         if isinstance(x, C) and x.parent() is self:
             return x
+        elif is_Element(x) and x.parent() == self.base_ring():
+            return self([x])
         elif is_SingularElement(x) and self._has_singular:
             self._singular_().set_ring()
             try:
```

