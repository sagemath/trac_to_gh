# Issue 6197: conversion of binomial fails

Issue created by migration from https://trac.sagemath.org/ticket/6197

Original creator: whuss

Original creation time: 2009-06-03 17:55:57

Converting symbolic expressions containing binomial coefficients
to maxima elements does not work.


```
sage: maxima(binomial(2*x, x))
sage1
```


Also the conversions to mathematica and maple fail:


```
sage: mathematica(binomial(2*x, x))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/huss/.sage/temp/bernoulli/6709/_home_huss__sage_init_sage_0.py in <module>()

/local/data/huss/software/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)                                                                                                    
   1024             return cls(self, x, name=name)                                                               
   1025         try:                                                                                             
-> 1026             return self._coerce_from_special_method(x)                                                   
   1027         except TypeError:                                                                                
   1028             raise                                                                                        

/local/data/huss/software/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in _coerce_from_special_method(self, x)                                                                                       
   1048             s = '_gp_'                                                                                   
   1049         try:                                                                                             
-> 1050             return (x.__getattribute__(s))(self)                                                         
   1051         except AttributeError:                                                                           
   1052             return self(x._interface_init_())                                                            

/local/data/huss/software/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.SageObject._mathematica_ (sage/structure/sage_object.c:5033)()                               

/local/data/huss/software/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression._interface_ (sage/symbolic/expression.cpp:3293)()                                     

/local/data/huss/software/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:2828)()                                 

/local/data/huss/software/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)                                                                                                    
   1022                                                                                                          
   1023         if isinstance(x, basestring):                                                                    
-> 1024             return cls(self, x, name=name)                                                               
   1025         try:                                                                                             
   1026             return self._coerce_from_special_method(x)                                                   

/local/data/huss/software/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in __init__(self, parent, value, is_name, name)
   1426             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
   1427                 self._session_number = -1
-> 1428                 raise TypeError, x
   1429         self._session_number = parent._session_number
   1430

TypeError: Error executing code in Mathematica
CODE:
        sage1=<function binomial at 0x917ddbc>[(x)*(2),x];
Mathematica ERROR:
        Syntax::sntxf: "sage1=" cannot be followed by
    "<function binomial at 0x917ddbc>[(x)*(2),x];".
```



```
sage: maple(binomial(2*x, x))                       
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/huss/.sage/temp/bernoulli/6709/_home_huss__sage_init_sage_0.py in <module>()

/local/data/huss/software/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)                                                                                                    
   1024             return cls(self, x, name=name)                                                               
   1025         try:                                                                                             
-> 1026             return self._coerce_from_special_method(x)                                                   
   1027         except TypeError:                                                                                
   1028             raise                                                                                        

/local/data/huss/software/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in _coerce_from_special_method(self, x)                                                                                       
   1048             s = '_gp_'                                                                                   
   1049         try:                                                                                             
-> 1050             return (x.__getattribute__(s))(self)                                                         
   1051         except AttributeError:                                                                           
   1052             return self(x._interface_init_())                                                            

/local/data/huss/software/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.SageObject._maple_ (sage/structure/sage_object.c:4795)()                                     

/local/data/huss/software/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression._interface_ (sage/symbolic/expression.cpp:3293)()                                     

/local/data/huss/software/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/structure/sage_object.so in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:2828)()                                 

/local/data/huss/software/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)                                                                                                    
   1022                                                                                                          
   1023         if isinstance(x, basestring):                                                                    
-> 1024             return cls(self, x, name=name)                                                               
   1025         try:                                                                                             
   1026             return self._coerce_from_special_method(x)                                                   

/local/data/huss/software/sage-4.0.rc0/local/lib/python2.5/site-packages/sage/interfaces/expect.pyc in __init__(self, parent, value, is_name, name)                                                                               
   1426             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:                          
   1427                 self._session_number = -1
-> 1428                 raise TypeError, x
   1429         self._session_number = parent._session_number
   1430

TypeError: An error occured running a Maple command:
INPUT:
read "/home/huss/.sage//temp/bernoulli/6709//interface//tmp6709";
OUTPUT:
on line 1, syntax error, missing operator or `;`:
sage1:=<function binomial at 0x917ddbc>((x)*(2),x):;
                        ^
Error, while reading
`/home/huss/.sage//temp/bernoulli/6709//interface//tmp6709`
```



---

Comment by kcrisman created at 2009-08-28 20:43:10

The error for the original bug is now 

```
sage: maxima(binomial(2*x,x))
Traceback
...
RuntimeError: cannot find SFunction in table
```

so the fix for this is to create a symbolic binomial and provide for this in the init method, the way factorial is done in functions/other.py (this works for Maxima; I don't have access to the others - but the fix would presumably be identical).  

However, I can't get this to import properly so that the symbolic binomial is what you get from binomial? like you do for factorial?, even after adding it to the import list in functions/all.py, so I am reluctant to post anything at this point.


---

Comment by kcrisman created at 2009-09-02 15:58:43

This should fix the problem reported in the bug, also hopefully for Mathematica (and for factorial).  It doesn't really help that much since Maxima doesn't automatically simplify binomials :) but that wasn't the ticket.  Adding Maple to the list, or other functions one desires, would be very similar.  The symbolic binomial wouldn't import properly, so this patch does not import it at all, but the bug is still fixed and the tests for these and a few related files pass.


---

Comment by mhansen created at 2009-09-08 06:20:51

Looks good to me.


---

Comment by mvngu created at 2009-09-08 10:46:21

I received a doctest failure with the patch `trac_6197-binomial-maxima.patch`:

```
sage -t -long devel/sage-main/sage/symbolic/random_tests.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/sage/symbolic/random_tests.py", line 204:
    sage: random_expr(50, nvars=3, coeff_generator=CDF.random_element)
Expected:
    arctanh(sinh(-arcsech(v2)/floor(-(0.615863165633 + 0.879368031485*I)*v1^2*v3) - gamma(pi) + floor(-(0.708874026302 - 0.954135400334*I)*v3)))^arcsech(-cosh(-polylog((v2 + 0.913564344312 + 0.0898040160336*I)^(-(0.723896589334 - 0.799038508886*I)*v2),-v1 - v3))/sin(-(0.0263902659909 + 0.153261789843*I)*arctan2(pi, e^pi)))
Got:
    arctanh(sinh(-arcsech(v2)/csch(-(0.615863165633 + 0.879368031485*I)*v1^2*v3) - gamma(pi) + floor(-(0.708874026302 - 0.954135400334*I)*v3)))^arcsech(-cosh(-polylog((v2 + 0.913564344312 + 0.0898040160336*I)^(-(0.723896589334 - 0.799038508886*I)*v2),-v1 - v3))/arcsin(-(0.0263902659909 + 0.153261789843*I)*arctan2(pi, arccot(pi))))
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_4
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.2.alpha1/tmp/.doctest_random_tests.py
	 [2.5 s]
```



---

Comment by kcrisman created at 2009-09-08 13:36:51

Adding a new function changes the list random_expr uses.  This is actually fixed in #6636, though I guess it must have already been a problem in this one.  I will try to separate that out from that patch and post updates to both.


---

Attachment

Okay, this should do it.  Literally the only change is that doctest, so hopefully just testing that should restore positive review.


---

Comment by mhansen created at 2009-09-08 19:43:59

Looks good.


---

Comment by mvngu created at 2009-09-09 02:53:42

Resolution: fixed
