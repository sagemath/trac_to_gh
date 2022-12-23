# Issue 1239: Wrap Simon's new gp two descent code

Issue created by migration from https://trac.sagemath.org/ticket/1239

Original creator: robertwb

Original creation time: 2007-11-21 19:43:50

Assignee: was

Scripts were recently updated http://www.math.unicaen.fr/~simon/

It now handles two-torsion more uniformly, works on more curves, and actually returns points on the curve given. 


---

Attachment


---

Attachment

John Cremona and I worked on this during Sage Days 6. 

The attached patches have the new version of the code (to be applied to extcode) and a revised interface. 

This also includes an implementation of transformations between different Weierstrass models.


---

Comment by robertwb created at 2007-11-21 19:48:48

Changing assignee from was to robertwb.


---

Comment by was created at 2007-12-15 07:12:47

WARNING: This is full of bugs and issues.  

E.g.,             

```
sage: E = EllipticCurve([0, 0, 1/216, -7/1296, 1/7776])
sage: F = E.global_integral_model(); F
outputs a non-integral model!
```


DO NOT apply this until further patche(s) are posted.

I'm working on some now.

ALSO -- there are many new functions with no doctets.


---

Comment by was created at 2007-12-15 07:15:11

Some missing doctests or things that will cause latex problems:

```
a/sage/schemes/elliptic_curves/ell_generic.py
integral_model
change_weierstrass_model

a/sage/rings/complex_double.pyx
argument

* number_field_element.pyx -- nth_root has \ but no r"""
* same prob in WeierstrassIsomorphism
* no doctest in init method for WeierstrassIsomorphism
* no doctest in init method for WeierstrassIsomorphism _call_
```



---

Comment by was created at 2007-12-15 07:16:30


```
[11:14pm] wstein-rvw-1239: It might be easy for you to fix the problems.
[11:14pm] wstein-rvw-1239: E.g.,            sage: E = EllipticCurve([0, 0, 1/216, -7/1296, 1/7776])
[11:14pm] wstein-rvw-1239:             sage: F = E.global_integral_model(); F
[11:14pm] wstein-rvw-1239: doesn't return an integral model.
[11:14pm] wstein-rvw-1239: E = EllipticCurve([1/3, 5]); E
[11:14pm] wstein-rvw-1239: E.integral_model()
[11:14pm] wstein-rvw-1239: returns a non-integral model
```



---

Attachment

tentative_trac-1239.patch


---

Comment by was created at 2007-12-15 07:23:01

[good review -- on extcode] The extcode bundle is *OK* -- no problems.


---

Attachment


---

Comment by robertwb created at 2007-12-15 07:52:31

The global_integral_model / integral_model code in question is John Cremona's. I'll look into it more. 

WARNING: The extcode patch can't go in without this one (due to interface changes).


---

Comment by robertwb created at 2007-12-15 07:52:31

Changing status from new to assigned.


---

Attachment

Turned out to be an indentation issue. Also added another doctest. 

Should be ready to go in now.


---

Comment by mabshoff created at 2007-12-15 08:42:45

Merged in 2.9.rc0.


---

Comment by mabshoff created at 2007-12-15 08:49:18

Resolution: fixed
