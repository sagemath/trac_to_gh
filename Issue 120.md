# Issue 120: abs for elements of CyclotomicField

Issue created by migration from https://trac.sagemath.org/ticket/120

Original creator: wdj

Original creation time: 2006-10-08 02:34:43

Assignee: was

Keywords: abs, cyclotomic field

It seems to me that this behaviour is wrong:

```
sage: z = CyclotomicField(7).gen()

sage: abs(z)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/wdj/sagefiles/sage-1.4/<ipython console> in <module>()

<type 'exceptions.TypeError'>: bad operand type for abs(): 'NumberFieldElement'

```



---

Comment by was created at 2007-01-07 19:41:32

Resolution: fixed


---

Comment by was created at 2007-01-07 19:41:32

Fixed

```
rank4:~/d/sage/sage/rings/number_field was$ hg export 2286
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1168195848 28800
# Node ID e6383f221f932db108f7507c91c1d79c6978671f
# Parent  01a95c126cbc373b9538f51dc19f32d42419dac6
Fix trac 120 -- abs for number field elements wasn't defined.

diff -r 01a95c126cbc -r e6383f221f93 sage/rings/number_field/number_field_element.py
--- a/sage/rings/number_field/number_field_element.py   Sun Jan 07 10:17:49 2007 -0800
+++ b/sage/rings/number_field/number_field_element.py   Sun Jan 07 10:50:48 2007 -0800
@@ -151,6 +151,38 @@ class NumberFieldElement(field_element.F
 
     def __cmp__(self, other):
         return cmp(self.__element, other.__element)
+
+    def __abs__(self, i=0, prec=53):
+        """
+        Return the absolute value of this element with respect to the
+        ith complex embedding of parent, to the given precision.
+
+        EXAMPLES:
+            sage: z = CyclotomicField(7).gen()
+            sage: abs(z)
+            0.999999999999999
+            sage: abs(z^2 + 17*z - 3)
+            16.0604426799930
+            sage: K.<a> = NumberField(x^3+17)
+            sage: abs(a)
+            2.57128159065823
+            sage: a.__abs__(prec=100)
+            2.5712815906582353554531872087
+            sage: a.__abs__(1,100)
+            2.5712815906582353554531872087
+            sage: a.__abs__(2,100)
+            2.5712815906582353554531872087
+
+        Here's one where the absolute value depends on the embedding.
+            sage: K.<b> = NumberField(x^2-2)
+            sage: a = 1 + b
+            sage: a.__abs__(i=0)
+            0.414213562373094
+            sage: a.__abs__(i=1)
+            2.41421356237309            
+        """
+        P = self.parent().complex_embeddings(prec)[i]
+        return abs(P(self))
 
     def __pow__(self, right):
         right = int(right)
```

