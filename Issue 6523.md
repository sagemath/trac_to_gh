# Issue 6523: .is_zero() method raises error for symbolic expression involving derivative

Issue created by migration from Trac.

Original creator: gmhossain

Original creation time: 2009-07-13 11:39:09

CC:  mhansen

If a symbolic expression contains  symbolic derivative then
checking whether it is zero, raises error:

```
sage: x.diff(x,2).is_zero()
True

sage: f(x) = function('f',x)
sage: f(x).diff(x).is_zero()
....
NotImplementedError: derivative
```


This fails because new symbolics tries to convert it to maxima
expression for checking the relation.

It works fine for any other expression not involving symbolic
derivative and without invoking maxima.

It seems to me, pynac relational test needs to be fixed.


---

Attachment


---

Comment by burcin created at 2009-08-01 11:16:11

Unfortunately, the fact that an expression contains a symbolic derivative doesn't guarantee that it is nonzero:


```
sage: t = f(x).derivative(x)
sage: (x*t +(1-x)*t - t)
-(x - 1)*D[1](f)(x) + x*D[1](f)(x) - D[1](f)(x)
sage: (x*t +(1-x)*t - t).collect(x)
0
```


The right fix for this is to either implement the `.derivative()` method in `sage/symbolic/expression_conversions.py` or to change pynac to allow different parents in `evalf()`, so that conversion to `CIF` can be done without the code in `expression_conversions.pyx`. 

I was planning to do this for #6243, but ended up using a different/better fix there.


---

Attachment

add doctests


---

Comment by burcin created at 2009-11-21 11:24:36

Changing status from new to needs_review.


---

Comment by burcin created at 2009-11-21 11:24:36

This is fixed by #7490, since we don't use the `expression_conversions` module to convert to `RIF` any more.

attachment:trac_6523-derivative_is_zero.patch adds a doctest with the example in the description.


---

Comment by mhansen created at 2009-12-06 08:33:39

Resolution: fixed


---

Comment by mhansen created at 2009-12-06 08:33:39

Looks good to me.

Merged trac_6523-derivative_is_zero.patch.
