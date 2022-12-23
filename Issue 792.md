# Issue 792: Problem creating element in module over QQ[x]

Issue created by migration from https://trac.sagemath.org/ticket/792

Original creator: justin

Original creation time: 2007-10-02 18:56:44

Assignee: was

We generate a module over QQ[x], and try to get a random element.  Somehow, we wander into code that wants a numerator of a polyomial:


```
sage: R1.<x>=PolynomialRing(QQ)
sage: M=FreeModule(R1,3)
sage: B=M.basis()
sage: f2=R1.random_element()
sage: n2 = f2*B[1]
sage: V2=M.span([n2])
sage: m3=V2.random_element()
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/SandBox/Justin/sb/sage-2.8.5.1/<ipython console> in <module>()

/SandBox/Justin/sb/sage-2.8.5.1/local/lib/python2.5/site-packages/sage/modules/free_module.py in random_element(self, prob, **kwds)
   1240         for i in range(self.rank()):
   1241             if random.random() <= prob:
-> 1242                 v += self.gen(i) * R.random_element(**kwds)
   1243         return v
   1244 

/SandBox/Justin/sb/sage-2.8.5.1/element.pyx in element.Vector.__mul__()

/SandBox/Justin/sb/sage-2.8.5.1/element.pyx in element.ModuleElement._multiply_by_scalar()

/SandBox/Justin/sb/sage-2.8.5.1/element.pyx in element.ModuleElement._lmul_c()

/SandBox/Justin/sb/sage-2.8.5.1/free_module_element.pyx in free_module_element.FreeModuleElement_generic_dense._lmul_c_impl()

/SandBox/Justin/sb/sage-2.8.5.1/element.pyx in element.RingElement._mul_c()

/SandBox/Justin/sb/sage-2.8.5.1/local/lib/python2.5/site-packages/sage/rings/fraction_field_element.py in _mul_(self, right)
    245     def _mul_(self, right):
    246         return FractionFieldElement(self.parent(),
--> 247            self.__numerator*right.__numerator,
    248            self.__denominator*right.__denominator, coerce=False, reduce=True)
    249 

<type 'exceptions.AttributeError'>: 'Polynomial_rational_dense' object has no attribute '_FractionFieldElement__numerator'
```




---

Comment by justin created at 2007-10-03 03:15:23

I'm going to close this.  I can now create elements such as 'm3', above.  The problem went away with the fix to Trac#789,


---

Comment by justin created at 2007-10-03 03:15:23

Resolution: fixed
