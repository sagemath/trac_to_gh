# Issue 2353: MPolynomialRing should be deprecated

Issue created by migration from https://trac.sagemath.org/ticket/2353

Original creator: burcin

Original creation time: 2008-02-29 10:02:59

Assignee: was

CC:  malb

It seems that the constructors `PolynomialRing` and `MPolynomialRing` are actually the same function.

sage.rings.polynomial.multi_polynomial_ring imports `PolynomialRing` as `MPolynomialRing`, and this gets imported into global scope.

Keeping to the python mantra "there is only one way to do it", the alias `MPolynomialRing` should be removed.

See ticket:2000 about this issue as well, though I don't see creating multivariate polynomial rings with only 1 variable as a valid use case to keep `MPolynomialRing`.


---

Comment by was created at 2008-02-29 21:36:28

> See ticket:2000 about this issue as well, though I don't see creating multivariate
> polynomial rings with only 1 variable as a valid use case to keep MPolynomialRing.

Yep, since this works I agree with you:

```
sage: type(PolynomialRing(QQ,'x',1))
<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular'>
sage: type(PolynomialRing(QQ,'x'))
<class 'sage.rings.polynomial.polynomial_ring.PolynomialRing_field'>
```


William


---

Comment by burcin created at 2008-05-11 02:03:12

add deprecation notice to MPolynomialRing, change doctests


---

Attachment

documentation changes


---

Comment by burcin created at 2008-05-11 02:17:44

Changing assignee from was to burcin.


---

Comment by burcin created at 2008-05-11 02:17:44

Changing status from new to assigned.


---

Attachment

attachment:2353_deprecate_MPolynomialRing.patch adds a deprecation notice to `MPolynomialRing` using Python's `warnings` module. It also prepends the docstring for `PolynomialRing` with the text:

```
    This function is deprecated and will be removed in a future version of
    Sage. Please use PolynomialRing instead.

    If you have questions regarding this function and it's replacement,
    please send your comments to sage-support@googlegroups.com.
```


attachment:2353_deprecate_MPolynomialRing-doc_changes.patch replaces occurences of `MPolynomialRing` in the documentation with `PolynomialRing`. I don't know why the file `commontex/patchlevel.tex` appears in this patch.


---

Comment by malb created at 2008-06-03 14:30:11

Positive review, patches look good. The date/version string change for the doc patch might be an issue, I don't know.


---

Comment by mabshoff created at 2008-06-04 18:22:17

The were some small problems with the doc patch:

```
--- a/tut/tut.tex       Sun May 04 11:23:15 2008 -0700
+++ b/tut/tut.tex       Sun May 11 04:01:36 2008 +0200
@@ -947,12 +947,10 @@ in one of two ways.
 \index{polynomial!ring of multivariate}

 \begin{verbatim}
-sage: R = MPolynomialRing(GF(5),3,"z")
+sage: R = PolynomialRing(GF(5),3,"z")
 sage: R
 Multivariate Polynomial Ring in z0, z1, z2 over Finite Field of size 5
 \end{verbatim}
-(The object \code{MPolynomialRing(GF(5),3,"z")} is the same as
-the object \code{MPolynomialRing(GF(5),3,"z")}.)
 Just as for univariate polynomials, there is an alternative more
 compact notation:
 \begin{verbatim}
```


This conflicts with some work done by John Palmieri, so I resolved that manually.

Cheers,

Michael


---

Comment by mabshoff created at 2008-06-04 18:22:39

Merged both patches in Sage 3.0.3.alpha1


---

Comment by mabshoff created at 2008-06-04 18:22:39

Resolution: fixed
