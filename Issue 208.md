# Issue 208: Implied Magma conversion causes seg fault

Issue created by migration from Trac.

Original creator: kedlaya

Original creation time: 2007-01-23 18:25:41

Assignee: was

Keywords: Magma, polynomial, coercion

The following code segment causes a segmentation fault (unhandled SIGSEGV):

```
P.<x> = PolynomialRing(Rationals())
y = magma(x) * 1.0
```

The expected behavior is to return a Magma polynomial over the real field.


---

Comment by was created at 2007-01-23 19:48:25

Kiran,

The implied behavior you want from MAGMA won't ever work, because
MAGMA does not do that implicit coercion (like SAGE would):


```
was`@`sage:~$ magma
Magma V2.13-5     Tue Jan 23 2007 11:46:41 on sage     [Seed = 3876897989]
Type ? for help.  Type <Ctrl>-D to quit.
> R<x> := PolynomialRing(RationalField());
> x * 1.0;

>> x * 1.0;
     ^
Runtime error in '*': Bad argument types
Argument types given: RngUPolElt[FldRat], FldReElt
```


That said, the infinite loop / seg fault you report is definitely
a SAGE bug -- SAGE should terminate with a proper error report.


---

Comment by was created at 2007-01-23 20:05:36

OK, fixed.

```
sage: R.<x> = ZZ[]
sage: x * 5
5*x
sage: x * 1.0
1.00000000000000*x
sage: x * (2/3)
2/3*x
sage: y = magma(x)
sage: y * 5
5*x
sage: y * 1.0
Traceback (most recent call last):
...
TypeError: unsupported operand parent(s) for '*': 'Magma' and 'Magma'
sage: y * (2/3)
Traceback (most recent call last):
...
TypeError: unsupported operand parent(s) for '*': 'Magma' and 'Magma'    

```



```
# HG changeset patch
# User William Stein <wstein`@`gmail.com>
# Date 1169582527 28800
# Node ID decd1e49efc3cef353d0dcc8121eb681b4e38764
# Parent  b99914e8d818b8ad1381e92dd8a4be2e6010654c
Fix trac #208 -- seg fault multiplying magma and non-magma elements

diff -r b99914e8d818 -r decd1e49efc3 sage/interfaces/expect.py
--- a/sage/interfaces/expect.py Tue Jan 23 11:40:08 2007 -0800
+++ b/sage/interfaces/expect.py Tue Jan 23 12:02:07 2007 -0800
`@``@` -896,27 +896,41 `@``@` class ExpectElement(RingElement):
         return P.new('%s.%s'%(self._name, int(n)))
 
     def _add_(self, right):
-        P = self._check_valid()        
-        return P.new('%s + %s'%(self._name, right._name))
+        P = self._check_valid()
+        try:
+            return P.new('%s + %s'%(self._name, right._name))
+        except Exception, msg:
+            raise TypeError, msg
         
     def _sub_(self, right):
         P = self._check_valid()        
-        return P.new('%s - %s'%(self._name, right._name))
+        try:
+            return P.new('%s - %s'%(self._name, right._name))
+        except Exception, msg:
+            raise TypeError, msg
+        
 
     def _mul_(self, right):
-        P = self._check_valid()        
-        return P.new('%s * %s'%(self._name, right._name))
+        P = self._check_valid()
+        try:
+            return P.new('%s * %s'%(self._name, right._name))
+        except Exception, msg:
+            raise TypeError,msg
 
     def _div_(self, right):
         P = self._check_valid()        
-        return P.new('%s / %s'%(self._name, right._name))
+        try:
+            return P.new('%s / %s'%(self._name, right._name))
+        except Exception, msg:
+            raise TypeError, msg
+        
 
     def __pow__(self, n):
         P = self._check_valid()
         if isinstance(n, ExpectElement):
             return P.new('%s ^ %s'%(self._name,n._name))
         else:
-           return P.new('%s ^ %s'%(self._name,n))
+            return P.new('%s ^ %s'%(self._name,n))
 
 
 def reduce_load(parent, x):
diff -r b99914e8d818 -r decd1e49efc3 sage/interfaces/magma.py
--- a/sage/interfaces/magma.py  Tue Jan 23 11:40:08 2007 -0800
+++ b/sage/interfaces/magma.py  Tue Jan 23 12:02:07 2007 -0800
`@``@` -117,6 +117,27 `@``@` We coerce some polynomial rings into MAG
     Univariate Polynomial Ring in y over Rational Field
     sage: S.1
     y
+
+This example illustrates that SAGE doesn't magically extend how MAGMA
+implicit coercion (what there is, at least) works:
+    sage: R.<x> = ZZ[]
+    sage: x * 5
+    5*x
+    sage: x * 1.0
+    1.00000000000000*x
+    sage: x * (2/3)
+    2/3*x
+    sage: y = magma(x)
+    sage: y * 5
+    5*x
+    sage: y * 1.0
+    Traceback (most recent call last):
+    ...
+    TypeError: unsupported operand parent(s) for '*': 'Magma' and 'Magma'
+    sage: y * (2/3)
+    Traceback (most recent call last):
+    ...
+    TypeError: unsupported operand parent(s) for '*': 'Magma' and 'Magma'    
 
 
 AUTHOR:

```



---

Comment by was created at 2007-01-23 20:05:36

Resolution: fixed
