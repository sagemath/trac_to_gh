# Issue 380: bug when defining a relative extension

Issue created by migration from https://trac.sagemath.org/ticket/380

Original creator: was

Original creation time: 2007-05-26 02:29:56

Assignee: was

Dimitar Jetchev found the following bug:


```
sage: k.<a> = NumberField(x^2+1); k
Number Field in a with defining polynomial x^2 + 1
sage: m.<b> = k.extension(y^2+1); m
```


and it fails .... it says: variable name should be alphanumeric.




---

Comment by was created at 2007-05-26 02:45:13


```
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1180147432 25200
# Node ID d5baafd9ca025979d8ac8558d9bc54cedd77904e
# Parent  430c6cb23845fe12c69fed0cb063646c1a87c3d0
Fix trac #380: bug when defining a relative extension

diff -r 430c6cb23845 -r d5baafd9ca02 sage/rings/number_field/number_field.py
--- a/sage/rings/number_field/number_field.py   Fri May 25 17:36:34 2007 -0700
+++ b/sage/rings/number_field/number_field.py   Fri May 25 19:43:52 2007 -0700
@@ -531,7 +531,7 @@ class NumberField_generic(field.Field):
             name = name[0]
         if name is None:
             raise TypeError, "the variable name must be specified."
-        return NumberField_extension(self, poly, repr(name))
+        return NumberField_extension(self, poly, str(name))

     def factor_integer(self, n):
         r"""
```



---

Comment by was created at 2007-05-26 02:45:13

Resolution: fixed
