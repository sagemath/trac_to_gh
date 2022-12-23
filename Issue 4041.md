# Issue 4041: Implementing non-monic number fields

Issue created by migration from https://trac.sagemath.org/ticket/4041

Original creator: mabshoff

Original creation time: 2008-09-02 20:40:36

Assignee: was

Implementing non-monic number fields would be hard, but not if the   
leading coefficient is a unit :)

```
sage: NumberField(x^2 - 2, 'a') 
Number Field in a with defining polynomial x^2 - 2 
sage: NumberField(-x^2 - 2, 'a') 
--------------------------------------------------------------------------- 
NotImplementedError                       Traceback (most recent call   
last) 
/Users/ncalexan/Devel/Squeak-3.10-1/platforms/unix/bld/<ipython   
console> in <module>() 
/Users/ncalexan/sage-3.0.6/local/lib/python2.5/site-packages/sage/ 
rings/number_field/number_field.py in NumberField(polynomial, name,   
check, names, cache) 
     288 
     289     if polynomial.degree() == 2: 
--> 290         K = NumberField_quadratic(polynomial, name, check) 
     291     else: 
     292         K = NumberField_absolute(polynomial, name, None, check) 
/Users/ncalexan/sage-3.0.6/local/lib/python2.5/site-packages/sage/ 
rings/number_field/number_field.py in __init__(self, polynomial, name,   
check) 
    6001             Number Field in a with defining polynomial x^2 - 4 
    6002         """ 
-> 6003         NumberField_absolute.__init__(self, polynomial,   
name=name, check=check) 
    6004         self._element_class =   
number_field_element_quadratic.NumberFieldElement_quadratic 
    6005         c, b, a = [rational.Rational(t) for t in   
self.defining_polynomial().list()] 
/Users/ncalexan/sage-3.0.6/local/lib/python2.5/site-packages/sage/ 
rings/number_field/number_field.py in __init__(self, polynomial, name,   
latex_name, check) 
    3272 
    3273     def __init__(self, polynomial, name, latex_name=None,   
check=True): 
-> 3274         NumberField_generic.__init__(self, polynomial, name,   
latex_name, check) 
    3275         self._element_class =   
number_field_element.NumberFieldElement_absolute 
    3276 
/Users/ncalexan/sage-3.0.6/local/lib/python2.5/site-packages/sage/ 
rings/number_field/number_field.py in __init__(self, polynomial, name,   
latex_name, check) 
     668                 raise TypeError, "polynomial must be defined   
over rational field" 
     669             if not polynomial.is_monic(): 
--> 670                 raise NotImplementedError, "number fields for   
non-monic polynomials not yet implemented." 
     671             if not polynomial.is_irreducible(): 
     672                 raise ValueError, "defining polynomial (%s)   
must be irreducible"%polynomial 
NotImplementedError: number fields for non-monic polynomials not yet   
implemented. 
}}} 



---

Comment by cremona created at 2008-09-02 21:14:34

It's not clear to me exactly what Nick means: defining polys in Z[x] with leading coefficient -1, or something more general over Q, or also relative number fields.


---

Comment by cremona created at 2008-09-04 15:18:36

This ticket seems to be a duplicate of #252.  So I think this one can be deleted.


---

Comment by mabshoff created at 2008-09-04 17:32:25

As John pointed out this is a dupe of #252, so close this ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-04 17:32:25

Resolution: fixed


---

Comment by mabshoff created at 2008-09-04 17:33:02

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-09-04 17:33:02

Resolution changed from fixed to 


---

Comment by mabshoff created at 2008-09-04 17:33:13

Resolution: duplicate
