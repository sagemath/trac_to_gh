# Issue 87: multivariable FractionField vs MPolynomial

Issue created by migration from https://trac.sagemath.org/ticket/87

Original creator: jdc

Original creation time: 2006-09-26 21:22:36

Assignee: was

CC:  jdc@uwo.ca

This bug is a bit more subtle than I expected:

--------------------------------------------------------
--------------------------------------------------------
| SAGE Version 1.3.7.3.3, Build Date: 2006-09-21       |
| Distributed under the GNU General Public License V2. |
sage: Qx=QQ['x']; x,=Qx.gens()

sage: (1/x)*x                                                                  
 1

sage: Qyz=QQ['y,z']; y,z=Qyz.gens()                                            

sage: (1/y)*y                                                                  
 1

sage: (y^2/y)*y                                                                
---------------------------------------------------------------------------
exceptions.TypeError                                 Traceback (most recent call last)

/home/scratchy/math/me/CayleyDickson/python/symbolic/<ipython console> 

/home/scratchy/math/me/CayleyDickson/python/symbolic/element.pyx in element.RingElement.__mul__()

/home/scratchy/math/me/CayleyDickson/python/symbolic/coerce.pyx in coerce.bin_op()

TypeError: unable to find an unambiguous parent

sage: type(1/y)                                                                
 <class 'sage.rings.fraction_field_element.FractionFieldElement'>

sage: type(y^2/y)                                                              
 <class 'sage.rings.fraction_field_element.FractionFieldElement'>

sage: type(y)                                                                  
 <class 'sage.rings.multi_polynomial_element.MPolynomial_polydict'>

Dan


---

Comment by was created at 2007-01-13 02:16:46

It works fine now:


```

sage: Qyz=QQ['y,z']; y,z=Qyz.gens()
sage: (1/y)*y
1
sage: (y^2/y)*y
y^2
```



---

Comment by was created at 2007-01-13 02:16:46

Resolution: fixed
