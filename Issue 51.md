# Issue 51: (5 + O(5)) / 1 causes exception

Issue created by migration from https://trac.sagemath.org/ticket/51

Original creator: dmharvey

Original creation time: 2006-09-13 18:48:33

Assignee: somebody


```
sage: (5 + O(5)) / 1
---------------------------------------------------------------------------
exceptions.ZeroDivisionError                         Traceback (most recent call last)

/home/dmharvey/sage-1.3.7/<ipython console> 

/home/dmharvey/sage-1.3.7/element.pyx in element.RingElement.__div__()

/home/dmharvey/sage-1.3.7/coerce.pyx in coerce.bin_op()

/home/dmharvey/sage-1.3.7/element.pyx in element.RingElement.__div__()

/home/dmharvey/sage-1.3.7/local/lib/python2.4/site-packages/sage/rings/padic.py in _div_(self, right)
    471             7 + 6*19 + 6*19^2 + 6*19^3 + 6*19^4 + O(19^5)
    472         """
--> 473         return self * right.__invert__(self.prec())
    474 
    475     def __mod__(self, right):

/home/dmharvey/sage-1.3.7/local/lib/python2.4/site-packages/sage/rings/padic.py in __invert__(self, prec)
    556             prec = self.parent().prec()
    557         if prec <= 0:
--> 558             raise ZeroDivisionError, "Can not invert self"
    559         unit = arith.inverse_mod(self.__unit, self.__p**prec)
    560         big_oh = prec - self.__ordp

ZeroDivisionError: Can not invert self
```




---

Comment by was created at 2007-01-07 18:07:05

Fixed.  Though of course working on the "slated for death"
p-adic code is disturbing. ..


```
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1168193133 28800
# Node ID 8536e22f8ff3fb30da752d4f4c21dfc2cc5e9b27
# Parent  08bcbca5d56554a829a59a508997d2c64d238a6c
Fixed trac #51

(5 + O(5)) / 1 causes exception

diff -r 08bcbca5d565 -r 8536e22f8ff3 sage/rings/padic.py
--- a/sage/rings/padic.py       Sat Jan 06 20:49:13 2007 -0800
+++ b/sage/rings/padic.py       Sun Jan 07 10:05:33 2007 -0800
@@ -354,8 +354,11 @@ class pAdic(field_element.FieldElement):
                                                   self.__unit, self.__p, self.__prec)
         # series printing
         if self.__ordp == infinity:
-            return "0"
-            #return "0 + O(%o^Infinity)"%(self.__p)
+            o = self.big_oh()
+            if o == infinity:
+                return "0"
+            else:
+                return "O(%s^%s)"%(self.__p, o)
         if self.__ordp == 0 and self.__prec == infinity and self.__unit == 1:
             return "1"
         s     = ""
@@ -411,7 +414,7 @@ class pAdic(field_element.FieldElement):
             sage: b = K(1); b
             1
             sage: a+b
-            0
+            O(11^10)
         """
         if self.__ordp <= right.__ordp:
             x = self; y = right
@@ -429,9 +432,9 @@ class pAdic(field_element.FieldElement):
         prec = big_oh - n - x.__ordp
         if prec != infinity:
             a %= p**prec
-        if a==0:
+        if a == 0:
             return pAdic(self.__parent, 0, big_oh)
-        return pAdic(self.__parent, a, big_oh ,x.__ordp + n)
+        return pAdic(self.__parent, a, big_oh, x.__ordp + n)
 
     def _sub_(self, right):
         """
@@ -472,8 +475,10 @@ class pAdic(field_element.FieldElement):
             3*19^-1 + O(19^Infinity)
             sage: a/b
             7 + 6*19 + 6*19^2 + 6*19^3 + 6*19^4 + O(19^5)
-        """
-        return self * right.__invert__(self.prec())
+            sage: (5 + O(5)) / 1
+            O(5^1)
+        """
+        return self * right.__invert__(self.__prec + self.__ordp)
 
     def __mod__(self, right):
         if self.__ordp < 0:
```



---

Comment by was created at 2007-01-07 18:07:05

Resolution: fixed
