# Issue 182: Integers(7).multiplicative_generator() no longer works

archive/issues_000182.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: Integers(7).multiplicative_generator()\nTraceback (most recent call last):\n  File \"\", line 1, in   File \"/home/server2/sage_notebook/worksheets/david/code/23.py\", line 4, in Integers(Integer(7)).multiplicative_generator()\n  File \"/sage-1.5/local/lib/python2.5/\", line 1, in     \nAttributeError: 'IntegerModRing_generic' object has no attribute 'multiplicative_generator'\n```\n\n\nI'm sure this used to work -- the default SAGE on sage.math still accepts it.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/182\n\n",
    "created_at": "2006-12-13T19:15:33Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "title": "Integers(7).multiplicative_generator() no longer works",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/182",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: somebody


```
sage: Integers(7).multiplicative_generator()
Traceback (most recent call last):
  File "", line 1, in   File "/home/server2/sage_notebook/worksheets/david/code/23.py", line 4, in Integers(Integer(7)).multiplicative_generator()
  File "/sage-1.5/local/lib/python2.5/", line 1, in     
AttributeError: 'IntegerModRing_generic' object has no attribute 'multiplicative_generator'
```


I'm sure this used to work -- the default SAGE on sage.math still accepts it.


Issue created by migration from https://trac.sagemath.org/ticket/182





---

archive/issue_comments_000831.json:
```json
{
    "body": "fixed for sage-1.6\n\n```\nrank4:~/d/sage/sage/rings was$ hg export 2316     \n# HG changeset patch\n# User William Stein <wstein@gmail.com>\n# Date 1168367697 28800\n# Node ID 9ed3822169452626abd38e84da465d133b40ea2b\n# Parent  5e2621f3400050664fc52f68097a68a679bc5033\nFixed trac bug #182 (added some useful functionality for Z/nZ)\n\ndiff -r 5e2621f34000 -r 9ed382216945 sage/rings/integer_mod_ring.py\n--- a/sage/rings/integer_mod_ring.py    Tue Jan 09 10:12:19 2007 -0800\n+++ b/sage/rings/integer_mod_ring.py    Tue Jan 09 10:34:57 2007 -0800\n@@ -248,7 +248,113 @@ class IntegerModRing_generic(quotient_ri\n             True\n         \"\"\"\n         return self.order().is_prime()\n-        \n+\n+    def field(self):\n+        \"\"\"\n+        If this ring is a field, return the corresponding field as a\n+        finite field, which may have extra functionality and\n+        structure.  Otherwise, raise a ValueError. \n+\n+        EXAMPLES:\n+            sage: R = Integers(7); R\n+            Ring of integers modulo 7\n+            sage: R.field()\n+            Finite Field of size 7\n+            sage: R = Integers(9)\n+            sage: R.field()\n+            Traceback (most recent call last):\n+            ...\n+            ValueError: self must be a field        \n+        \"\"\"\n+        try:\n+            return self.__field\n+        except AttributeError:\n+            if not self.is_field():\n+                raise ValueError, \"self must be a field\"\n+            import finite_field\n+            k = finite_field.FiniteField(self.order())\n+            self.__field = k\n+            return k\n+\n+    def multiplicative_group_is_cyclic(self):\n+        \"\"\"\n+        Return True if the multiplicative group of this field is\n+        cyclic.  This is the case exactly when the order is less than\n+        8 or a power of an odd prime.\n+\n+        EXAMPLES:\n+            sage: R = Integers(7); R\n+            Ring of integers modulo 7\n+            sage: R.multiplicative_group_is_cyclic()\n+            True\n+            sage: R = Integers(9)\n+            sage: R.multiplicative_group_is_cyclic()\n+            True\n+            sage: Integers(8).multiplicative_group_is_cyclic()\n+            False\n+            sage: Integers(4).multiplicative_group_is_cyclic()\n+            True\n+            sage: Integers(25*3).multiplicative_group_is_cyclic()\n+            False        \n+        \"\"\"\n+        n = self.order()\n+        if n < 8:\n+            return True\n+        if arith.is_prime(n):\n+            return True\n+        \n+        # TODO -- the implementation below uses factoring, but it doesn't\n+        # need to; really it just needs to know if n is a prime power or not,\n+        # which is easier than factoring. \n+    \n+        F = arith.factor(n)\n+        if len(F) > 1:\n+            return False\n+        if F[0][0] == 2:\n+            return False\n+        return True\n+\n+    def multiplicative_generator(self):\n+        \"\"\"\n+        Return a generator for the multiplicative group of this ring,\n+        assuming the multiplicative group is cyclic.\n+\n+        Use the unit_gens function to obtain generators even in the\n+        non-cyclic case. \n+\n+        EXAMPLES:\n+            sage: R = Integers(7); R\n+            Ring of integers modulo 7\n+            sage: R.multiplicative_generator()\n+            3\n+            sage: R = Integers(9)\n+            sage: R.multiplicative_generator()\n+            2\n+            sage: Integers(8).multiplicative_generator()\n+            Traceback (most recent call last):\n+            ...\n+            ValueError: multiplicative group of this ring is not cyclic\n+            sage: Integers(4).multiplicative_generator()\n+            3\n+            sage: Integers(25*3).multiplicative_generator()\n+            Traceback (most recent call last):\n+            ...\n+            ValueError: multiplicative group of this ring is not cyclic\n+            sage: Integers(25*3).unit_gens()\n+            [26, 52]        \n+        \"\"\"\n+        try:\n+            return self.__mult_gen\n+        except AttributeError:\n+            if self.is_field():\n+                a = self(self.field().multiplicative_generator())\n+            elif self.multiplicative_group_is_cyclic():\n+                a = self.unit_gens()[0]\n+            else:\n+                raise ValueError, \"multiplicative group of this ring is not cyclic\"\n+            self.__mult_gen = a\n+            return a\n+            \n     def factored_order(self):\n         \"\"\"\n         EXAMPLES:\n\n\n```\n",
    "created_at": "2007-01-09T18:36:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/182#issuecomment-831",
    "user": "https://github.com/williamstein"
}
```

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

archive/issue_comments_000832.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-09T18:36:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/182#issuecomment-832",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000189.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-01-09T18:36:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/182",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/182#event-189"
}
```
