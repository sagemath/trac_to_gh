# Issue 5214: coercion to orders in relative number fields is not implemented

Issue created by migration from https://trac.sagemath.org/ticket/5214

Original creator: ncalexan

Original creation time: 2009-02-09 05:34:51

Assignee: was

CC:  robertwb

Keywords: relative order number field coercion


```
sage: t = OK.basis()[0]
sage: x = ZZ['x'].0
sage: K.<a,b> = NumberField([x^2 + 1, x^2 - 3])
sage: OK = K.maximal_order(); OK.basis()                                                                                          
[1, 1/2*a - 1/2*b, -1/2*b*a + 1/2, a]
sage: OK(a)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (363, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1152, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/ncalexan/.sage/temp/sage.math.washington.edu/21534/_home_ncalexan__sage_init_sage_0.py in <module>()

/scratch/ncalexan/sage-3.3.alpha5-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/rings/number_field/order.pyc\
 in __call__(self, x)
   1192         if x.parent() is not self._K:
   1193             x = self._K(x)
-> 1194         x = self._absolute_order(x) # will test membership
   1195         return OrderElement_relative(self, x)
   1196

/scratch/ncalexan/sage-3.3.alpha5-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/rings/number_field/order.pyc\
 in __call__(self, x)
    900             return x
    901         if not is_Element(x) or x.parent() is not self._K:
--> 902             x = self._K(x)
    903         V, _, embedding = self._K.vector_space()
    904         if not embedding(x) in self._module_rep:

/scratch/ncalexan/sage-3.3.alpha5-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.\
structure.parent.Parent.__call__ (sage/structure/parent.c:3653)()

/scratch/ncalexan/sage-3.3.alpha5-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in \
sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:2793)()

/scratch/ncalexan/sage-3.3.alpha5-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in \
sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2700)()

/scratch/ncalexan/sage-3.3.alpha5-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/rings/number_field/number_fi\
eld.pyc in _element_constructor_(self, x)
    829                     return self._element_class(self, x)
    830                 x = L(x)
--> 831             return self._coerce_from_other_number_field(x)
    832         elif isinstance(x,str):
    833             return self._coerce_from_str(x)

/scratch/ncalexan/sage-3.3.alpha5-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/rings/number_field/number_fi\
eld.pyc in _coerce_from_other_number_field(self, x)
   3560             return self._element_class(self, f[0])
   3561         # todo: more general coercion if embedding have been asserted
-> 3562         raise TypeError, "Cannot coerce element into this number field"
   3563
   3564     def _coerce_non_number_field_element_in(self, x):

TypeError: Cannot coerce element into this number field
OK(b)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (363, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1152, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/ncalexan/.sage/temp/sage.math.washington.edu/21534/_home_ncalexan__sage_init_sage_0.py in <module>()

/scratch/ncalexan/sage-3.3.alpha5-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/rings/number_field/order.pyc\
 in __call__(self, x)
   1192         if x.parent() is not self._K:
   1193             x = self._K(x)
-> 1194         x = self._absolute_order(x) # will test membership
   1195         return OrderElement_relative(self, x)
   1196

/scratch/ncalexan/sage-3.3.alpha5-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/rings/number_field/order.pyc\
 in __call__(self, x)
    900             return x
    901         if not is_Element(x) or x.parent() is not self._K:
--> 902             x = self._K(x)
    903         V, _, embedding = self._K.vector_space()
    904         if not embedding(x) in self._module_rep:

/scratch/ncalexan/sage-3.3.alpha5-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.\
structure.parent.Parent.__call__ (sage/structure/parent.c:3653)()

/scratch/ncalexan/sage-3.3.alpha5-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in \
sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:2793)()

/scratch/ncalexan/sage-3.3.alpha5-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in \
sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2700)()

/scratch/ncalexan/sage-3.3.alpha5-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/rings/number_field/number_fi\
eld.pyc in _element_constructor_(self, x)
    829                     return self._element_class(self, x)
    830                 x = L(x)
--> 831             return self._coerce_from_other_number_field(x)
    832         elif isinstance(x,str):
    833             return self._coerce_from_str(x)

/scratch/ncalexan/sage-3.3.alpha5-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/rings/number_field/number_fi\
eld.pyc in _coerce_from_other_number_field(self, x)
/scratch/ncalexan/sage-3.3.alpha5-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/rings/number_field/number_fi\
eld.pyc in _coerce_from_other_number_field(self, x)
   3560             return self._element_class(self, f[0])
   3561         # todo: more general coercion if embedding have been asserted
-> 3562         raise TypeError, "Cannot coerce element into this number field"
   3563
   3564     def _coerce_non_number_field_element_in(self, x):

TypeError: Cannot coerce element into this number field
sage: OK.basis()[3].list()
[0, 1]
sage: OK(OK.basis()[3].list())
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/ncalexan/.sage/temp/sage.math.washington.edu/21534/_home_ncalexan__sage_init_sage_0.py in <module>()

/scratch/ncalexan/sage-3.3.alpha5-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/rings/number_field/order.pyc\
 in __call__(self, x)
   1190         Coerce an element into this relative order.
   1191         """                                                                                                               
-> 1192         if x.parent() is not self._K:                                                                                     
   1193             x = self._K(x)                                                                                                
   1194         x = self._absolute_order(x) # will test membership                                                                
                                                                                                                                  
AttributeError: 'list' object has no attribute 'parent'                                      
}}}                                    


---

Comment by mabshoff created at 2009-02-09 06:02:07

3.4 is mostly about the ReST patches. Once those are in we will likely cut 3.4 as a release and then quickly open 3.4.1 to merge fixes on top of the ReST code.

Cheers,

Michael


---

Comment by fwclarke created at 2009-03-13 19:03:22

The problem is solved by changes to `__call__` for the class `RelativeOrder` in `sage/rings/number_theory/order.py` to be found in #5508.


---

Comment by mabshoff created at 2009-03-25 08:55:39

To close this we would need a doctest.

Cheers,

Michael


---

Comment by fwclarke created at 2009-03-26 08:51:15

Replying to [comment:3 mabshoff]:
> To close this we would need a doctest.

See lines 1194 to 1199 of sage/rings/number_field/order.py as patched by 
#5508:

```
            sage: K.<a, b> = NumberField([x^2 + 2, x^2 + 1000*x + 1]) 
            sage: OK = K.ring_of_integers()
            sage: OK(a)
            sage: a
            sage: OK([3, 4])
            4*a + 3
```



---

Comment by mabshoff created at 2009-03-26 20:35:55

Resolution: fixed


---

Comment by mabshoff created at 2009-03-26 20:35:55

Fixed in Sage 3.4.1.alpha0 via #5508. Thanks Francis :)

Cheers,

Michael
