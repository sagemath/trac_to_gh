# Issue 3809: reorder checks for creating a number field; prevents some silly errors

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2008-08-12 04:48:24

Assignee: was

Keywords: number field check

Reordering the checks for creating a number field prevents such strange things as:


```
sage: x = GF(7)['x'].0
sage: x.parent()
Univariate Polynomial Ring in x over Finite Field of size 7
sage: x^4 + 23
x^4 + 2
sage: K.<a> = NumberField(x^4 + 23)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/Users/ncalexan/sage-3.0.6/devel/sage-nca/<ipython console> in <module>()

/Users/ncalexan/sage-3.0.6/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py in NumberField(polynomial, name, check, names, cache)
    278         K = NumberField_quadratic(polynomial, name, check)
    279     else:
--> 280         K = NumberField_absolute(polynomial, name, None, check)
    281 
    282     if cache:

/Users/ncalexan/sage-3.0.6/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py in __init__(self, polynomial, name, latex_name, check)
   3219 
   3220     def __init__(self, polynomial, name, latex_name=None, check=True):
-> 3221         NumberField_generic.__init__(self, polynomial, name, latex_name, check)
   3222         self._element_class = number_field_element.NumberFieldElement_absolute
   3223 

/Users/ncalexan/sage-3.0.6/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py in __init__(self, polynomial, name, latex_name, check)
    644         if check:
    645             if not polynomial.is_irreducible():
--> 646                 raise ValueError, "defining polynomial (%s) must be irreducible"%polynomial
    647             if not polynomial.parent().base_ring() == QQ:
    648                 raise TypeError, "polynomial must be defined over rational field"

ValueError: defining polynomial (x^4 + 2) must be irreducible
```



---

Attachment


---

Attachment


---

Comment by mabshoff created at 2008-08-13 08:36:57

The referee patch looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-13 08:57:12

Merged both patches in Sage 3.1.alpha2


---

Comment by mabshoff created at 2008-08-13 08:57:12

Resolution: fixed
