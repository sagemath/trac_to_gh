# Issue 5353: add xgcd for polynomial over GF(2)

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-02-23 23:51:42

Assignee: malb

Currently, this fails:


```
sage: R.<x> = GF(2)[]
sage: fr = ((x+1)/(x^3+x+1) + (x+1)/(x^3+x^2+1));
sage: fr.partial_fraction_decomposition() 
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/home/mhansen/.sage/temp/sage.math.washington.edu/19940/_home_mhansen__sage_init_sage_0.py in <module>()

/home/mhansen/sage-3.3.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/rings/fraction_field_element.so in sage.rings.fraction_field_element.FractionFieldElement.partial_fraction_decomposition (sage/rings/fraction_field_element.c:3052)()

/home/mhansen/sage-3.3.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial.inverse_mod (sage/rings/polynomial/polynomial_element.c:8191)()

/home/mhansen/sage-3.3.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_gf2x.so in sage.rings.polynomial.polynomial_gf2x.Polynomial_template.xgcd (sage/rings/polynomial/polynomial_gf2x.cpp:5685)()

/home/mhansen/sage-3.3.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_gf2x.so in sage.rings.polynomial.polynomial_gf2x.celement_xgcd (sage/rings/polynomial/polynomial_gf2x.cpp:3517)()

NotImplementedError: 
```



---

Comment by mhansen created at 2009-02-23 23:56:29

Currently, in sage.libs.ntl.ntl_GF2X_linkage.pyx celement_xgcd just raises a NotImplementedError, but NTL does provide a xgcd for GF2X elements.


---

Attachment


---

Comment by mhansen created at 2009-02-24 01:59:31

Changing assignee from malb to mhansen.


---

Comment by mhansen created at 2009-02-24 01:59:31

Changing status from new to assigned.


---

Comment by ylchapuy created at 2009-02-25 11:12:55

The patch seems good but why does

```
f.xgcd?
```

show another docstring?


---

Comment by mhansen created at 2009-02-25 11:15:57

This is due to the polynomial templating which allows many of the polynomial types to share lots of boilerplate code.  The generic code for xgcd calls the celement_xgcd defined here.


---

Comment by ylchapuy created at 2009-03-16 17:35:37

ok with sage 3.4


---

Comment by mabshoff created at 2009-03-25 06:01:22

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-25 06:01:22

Resolution: fixed
