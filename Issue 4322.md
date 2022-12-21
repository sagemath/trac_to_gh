# Issue 4322: modular polynomials database is broken

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2008-10-18 21:43:44

Assignee: mabshoff

CC:  robertwb

Keywords: modular polynomial database

In 3.1.4, install this optional spkg with


```
sage -i database_kohel-20060803
```


then 


```
sage: DBMP = ClassicalModularPolynomialDatabase()
sage: DBMP[29]
<string>:1: Warning: 'with' will become a reserved keyword in Python 2.6
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1683, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/opt/sage-3.1.4/devel/sage-main/sage/structure/<ipython console> in <module>()

/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/databases/db_modular_polynomials.pyc in __getitem__(self, level)
     93             for cff in coeff_list:
     94                 poly[(cff[0],cff[1])] = Integer(cff[2])
---> 95         return P(polydict.PolyDict(poly))
     96 
     97 class ModularCorrespondenceDatabase(ModularPolynomialDatabase):

/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_libsingular.so in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular.__call__ (sage/rings/polynomial/multi_polynomial_libsingular.cpp:6996)()

/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:3732)()
    303                         del self._convert_from_list[i]
    304                         break
--> 305                 raise
    306             
    307         raise TypeError, "No conversion defined from %s to %s"%(R, self)

/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.__call__ (sage/structure/parent.c:3619)()
    294             try:
    295                 if no_extra_args:
--> 296                     return mor._call_(x)
    297                 else:
    298                     return mor._call_with_args(x, args, kwds)

/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:2622)()
     74                 print type(self._codomain), self._codomain
     75                 print type(self._codomain._element_constructor), self._codomain._element_constructor
---> 76             raise
     77 
     78     cpdef Element _call_with_args(self, x, args=(), kwds={}):

/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps._call_ (sage/structure/coerce_maps.c:2537)()
     69     cpdef Element _call_(self, x):
     70         try:
---> 71             return self._codomain._element_constructor(x)
     72         except:
     73             if print_warnings:

/opt/sage-3.1.4/local/lib/python2.5/site-packages/sage/rings/integer.so in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:5688)()

TypeError: unable to coerce <type 'sage.rings.polynomial.polydict.PolyDict'> to an integer
```



---

Comment by kohel created at 2008-10-20 22:25:21

Somewhere between sage-3.0.2 and sage-3.1.4 this broke:

sage: P.<X,Y> = PolynomialRing(ZZ,2)
sage: P(sage.rings.polynomial.polydict.PolyDict({(1,0):1,(0,1):-1}))
X - Y

This looks like a problem with a change to the new coercion model; 
I will temporarily reassign to mabshoff.  Perhaps I am using access 
to the internal datastructure which has changed and/or not meant 
to be accessible. In that case he can send it back to me.


---

Comment by mabshoff created at 2008-10-20 22:27:50

Changing assignee from mabshoff to robertwb.


---

Comment by mabshoff created at 2008-10-20 22:27:50

Changing component from optional packages to coercion.


---

Comment by mabshoff created at 2008-10-20 22:27:50

RobertWB is the man here :)

Cheers,

Michael


---

Comment by robertwb created at 2008-10-21 19:06:46

Changing component from coercion to optional packages.


---

Comment by robertwb created at 2008-10-21 19:06:46

Changing assignee from robertwb to mabshoff.


---

Comment by robertwb created at 2008-10-21 19:06:46

Actually, it looks like it's due to #4021, MPolynomial_libsingular over ZZ. It still works in the generic case: 


```
sage: P.<x,y> = ZZ['t']['x,y']
sage: a = sage.rings.polynomial.polydict.PolyDict({(1,0):1,(0,1):-1})
sage: P(a)
x - y
```


Despite the fact that polydicts are no longer used, I can't think of any reason why one would need this construction. More efficient (and less prone to breakage in the future is) direct construction from a dict. 


```
sage: P.<x,y> = ZZ[]
sage: P({(1,0):1,(0,1):-1})
x - y
```



---

Attachment

The attached patch removes the uses of polydict.


---

Comment by mabshoff created at 2009-01-25 02:20:52

Merged in Sage 3.3.alpha2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-25 02:20:52

Resolution: fixed
