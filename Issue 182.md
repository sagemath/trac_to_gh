# Issue 182: Integers(7).multiplicative_generator() no longer works

Issue created by migration from https://trac.sagemath.org/ticket/182

Original creator: dmharvey

Original creation time: 2006-12-13 19:15:33

Assignee: somebody


```
sage: Integers(7).multiplicative_generator()
Traceback (most recent call last):
  File "", line 1, in   File "/home/server2/sage_notebook/worksheets/david/code/23.py", line 4, in Integers(Integer(7)).multiplicative_generator()
  File "/sage-1.5/local/lib/python2.5/", line 1, in     
AttributeError: 'IntegerModRing_generic' object has no attribute 'multiplicative_generator'
```


I'm sure this used to work -- the default SAGE on sage.math still accepts it.



---

Comment by was created at 2007-01-09 18:36:37

fixed for sage-1.6

```
rank4:~/d/sage/sage/rings was$ hg export 2316     
# HG changeset patch
# User William Stein <wstein@gmail.com>
# Date 1168367697 28800
# Node ID 9ed3822169452626abd38e84da465d133b40ea2b
# Parent  5e2621f3400050664fc52f68097a68a679bc5033
Fixed trac bug #182 (added some useful functionality for Z/nZ)

diff -r 5e2621f34000 -r 9ed382216945 sage/rings/integer_mod_ring.py
--- a/sage/rings/integer_mod_ring.py    Tue Jan 09 10:12:19 2007 -0800
+++ b/sage/rings/integer_mod_ring.py    Tue Jan 09 10:34:57 2007 -0800
@@ -248,7 +248,113 @@ class IntegerModRing_generic(quotient_ri
             True
         """
         return self.order().is_prime()
-        
+
+    def field(self):
+        """
+        If this ring is a field, return the corresponding field as a
+        finite field, which may have extra functionality and
+        structure.  Otherwise, raise a ValueError. 
+
+        EXAMPLES:
+            sage: R = Integers(7); R
+            Ring of integers modulo 7
+            sage: R.field()
+            Finite Field of size 7
+            sage: R = Integers(9)
+            sage: R.field()
+            Traceback (most recent call last):
+            ...
+            ValueError: self must be a field        
+        """
+        try:
+            return self.__field
+        except AttributeError:
+            if not self.is_field():
+                raise ValueError, "self must be a field"
+            import finite_field
+            k = finite_field.FiniteField(self.order())
+            self.__field = k
+            return k
+
+    def multiplicative_group_is_cyclic(self):
+        """
+        Return True if the multiplicative group of this field is
+        cyclic.  This is the case exactly when the order is less than
+        8 or a power of an odd prime.
+
+        EXAMPLES:
+            sage: R = Integers(7); R
+            Ring of integers modulo 7
+            sage: R.multiplicative_group_is_cyclic()
+            True
+            sage: R = Integers(9)
+            sage: R.multiplicative_group_is_cyclic()
+            True
+            sage: Integers(8).multiplicative_group_is_cyclic()
+            False
+            sage: Integers(4).multiplicative_group_is_cyclic()
+            True
+            sage: Integers(25*3).multiplicative_group_is_cyclic()
+            False        
+        """
+        n = self.order()
+        if n < 8:
+            return True
+        if arith.is_prime(n):
+            return True
+        
+        # TODO -- the implementation below uses factoring, but it doesn't
+        # need to; really it just needs to know if n is a prime power or not,
+        # which is easier than factoring. 
+    
+        F = arith.factor(n)
+        if len(F) > 1:
+            return False
+        if F[0][0] == 2:
+            return False
+        return True
+
+    def multiplicative_generator(self):
+        """
+        Return a generator for the multiplicative group of this ring,
+        assuming the multiplicative group is cyclic.
+
+        Use the unit_gens function to obtain generators even in the
+        non-cyclic case. 
+
+        EXAMPLES:
+            sage: R = Integers(7); R
+            Ring of integers modulo 7
+            sage: R.multiplicative_generator()
+            3
+            sage: R = Integers(9)
+            sage: R.multiplicative_generator()
+            2
+            sage: Integers(8).multiplicative_generator()
+            Traceback (most recent call last):
+            ...
+            ValueError: multiplicative group of this ring is not cyclic
+            sage: Integers(4).multiplicative_generator()
+            3
+            sage: Integers(25*3).multiplicative_generator()
+            Traceback (most recent call last):
+            ...
+            ValueError: multiplicative group of this ring is not cyclic
+            sage: Integers(25*3).unit_gens()
+            [26, 52]        
+        """
+        try:
+            return self.__mult_gen
+        except AttributeError:
+            if self.is_field():
+                a = self(self.field().multiplicative_generator())
+            elif self.multiplicative_group_is_cyclic():
+                a = self.unit_gens()[0]
+            else:
+                raise ValueError, "multiplicative group of this ring is not cyclic"
+            self.__mult_gen = a
+            return a
+            
     def factored_order(self):
         """
         EXAMPLES:


```



---

Comment by was created at 2007-01-09 18:36:37

Resolution: fixed
