# Issue 6545: sorting of ideal bases

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-07-16 19:23:45

Assignee: malb

`MPolynomialIdeal.interreduced_basis()` should return the same sorted list as `MPolynomialIdeal.interreduced_basis()`, also the input to `MPolynomialIdeal.triangular_decomposition()` must be sorted to avoid confusing Singular.


---

Attachment


---

Comment by john_perry created at 2009-08-18 20:27:11

I don't understand the description of the comment: "MPolynomialIdeal.interreduced_basis() should return the same sorted list as MPolynomialIdeal.interreduced_basis()" Can someone elaborate?


---

Comment by malb created at 2009-08-18 20:51:48

Sorry, my bad. It should read


`MPolynomialIdeal.interreduced_basis()` should return the same sorted list as `MPolynomialIdeal.groebner_basis()` when called on an ideal which has a  (not reduced) Groebner basis as set of generators.


---

Comment by malb created at 2009-08-26 12:06:10

Still applies against 4.1.1. One hunk might fail if #6596 and #6628 are applied (they fix the same annoying doctest output).


---

Comment by john_perry created at 2009-08-26 17:49:06

I'm working on an unmodified sage 4.1.1 and I can't get the patch to work. Nearly all the hunks fail.


---

Comment by malb created at 2009-08-26 17:56:00

Strange, here is what I do:
 * hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6545/trac_6545_mpolynomial_ideal_sorted_outputs.patch
 * hg qpush (no hunk fails)
 * sage -b

Did you mix up raw-attachment and attachment?


---

Comment by john_perry created at 2009-08-26 18:18:36

I tried your suggestion and it failed with the same errors. This will sound weird, but I'm looking at the diff and at the file, and it looks as if the patch applied anyway. I don't get it; maybe this thing isn't unmodified, or something is mucked up in the hg. I'm trying to work it out...


---

Comment by john_perry created at 2009-08-26 18:46:36

This seems to be working, with one exception. When I run it, I get one error:

    TypeError: factor() got an unexpected keyword argument 'proof'

This is ticket #5958, isn't it?


---

Comment by malb created at 2009-08-26 19:10:02

Yep, that should be it.


---

Comment by john_perry created at 2009-08-26 20:50:27

Should I mark this as a positive review? Once the patch to ticket 5958 is applied, this should work.


---

Comment by malb created at 2009-08-26 21:22:56

I just did a {{{make test}} with the following patches applied on sage.math


```
variety_CC.patch
variety_CC2.patch
trac_6545_mpolynomial_ideal_sorted_outputs.patch
```


and all tests passed. So I guess it is a *positive review* then? I leave it up to you.


---

Comment by john_perry created at 2009-08-26 22:53:05

I say positive review. If anyone says otherwise I'll leave academia and become a hermit.

Well, maybe not. But I'll want to. ;-)


---

Comment by mvngu created at 2009-09-03 06:13:47

First I merged patches at #6596 and #6628. Merging `trac_6545_mpolynomial_ideal_sorted_outputs.patch` results in a hunk failure:

```
[mvngu`@`mod sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6545/trac_6545_mpolynomial_ideal_sorted_outputs.patch && hg qpush
adding trac_6545_mpolynomial_ideal_sorted_outputs.patch to series file
applying trac_6545_mpolynomial_ideal_sorted_outputs.patch
patching file sage/schemes/hyperelliptic_curves/jacobian_morphism.py
Hunk #1 FAILED at 294
1 out of 1 hunks FAILED -- saving rejects to file sage/schemes/hyperelliptic_curves/jacobian_morphism.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
Errors during apply, please fix and refresh trac_6545_mpolynomial_ideal_sorted_outputs.patch
```



---

Comment by malb created at 2009-09-03 08:49:40

You can ignore this hunk failure it was also fixed in either #6596 or #6628. It was just this really annoying doctest failure which would crop up everytime one changes anything related to multivariate polynomial ideals.


---

Comment by mvngu created at 2009-09-09 06:02:54

rebased against Sage 4.1.2.alpha1


---

Attachment

The patch `trac_6545-rebased.patch` is a rebase of `trac_6545_mpolynomial_ideal_sorted_outputs.patch` against Sage 4.1.2.alpha1. The rebased patch is the same as the previous patch, but without this hunk:

```
--- jacobian_morphism.py                                                                                                                                                                                             
+++ jacobian_morphism.py                                                                                                                                                                                             
`@``@` -295,7 +295,7 `@``@`
         sage: H = HyperellipticCurve(f, 2*x); H                                                                                                                                                                     
         Hyperelliptic Curve over Finite Field of size 1000000000000000000000000000057 defined by y^2 + 2*x*y = x^7 + x^2 + 1                                                                                        
         sage: J = H.jacobian()(F); J                                                                                                                                                                                
-        verbose 0 (919: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.                                                                                                
+        verbose 0 (...: multi_polynomial_ideal.py, dimension) Warning: falling back to very slow toy implementation.                                                                                                
         Set of points of Jacobian of Hyperelliptic Curve over Finite Field of size 1000000000000000000000000000057 defined by y^2 + 2*x*y = x^7 + x^2 + 1 defined over Finite Field of size 10000000000000000000000\
00000057                                                                                                                                                                                                             
         sage: Q = J(H.lift_x(F(1))); Q                                                                                                                                                                              
         (x + 1000000000000000000000000000056, y + 1000000000000000000000000000056)
```



---

Comment by mvngu created at 2009-09-09 06:37:38

Merged `trac_6545-rebased.patch`.


---

Comment by mvngu created at 2009-09-09 06:37:38

Resolution: fixed
