# Issue 58: wanted -- subsets of a set

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-09-14 10:45:59

Assignee: somebody

I would like to be able to type

```
sage: X = Set(range(5))
sage: X.subsets()  # or X.powerset()
```

and get iterator over the power set.  

I wold also like to do 

```
sage: X.subsets(2)
```

and get all 2-element subsets.

It seems that even Python's built-in set type doesn't do these basic operations...



---

Comment by jason created at 2007-10-25 21:22:18

The patch below uses Mike's combinatorial stuff.


```
diff -r 58095d7eaad0 sage/sets/set.py
--- a/sage/sets/set.py  Thu Oct 25 00:59:26 2007 -0700
+++ b/sage/sets/set.py  Thu Oct 25 16:21:12 2007 -0500
`@``@` -472,6 +472,23 `@``@` class Set_object(Set_generic):
         """
         return self.__object

+
+    def subsets(self,size=None):
+        """
+        Return the Subset object representing the subsets of a set.  If size
+        is specified, return the subsets of that size.
+
+        EXAMPLES:
+            sage: X = Set([1,2,3])
+            sage: list(X.subsets())
+            [{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]
+            sage: list(X.subsets(2))
+            [{1, 2}, {1, 3}, {2, 3}]
+
+        """
+        from sage.combinat.subset import Subsets
+        return Subsets(self,size)
+
 class Set_object_enumerated(Set_object):
     """
     A finite enumerated set.
```



---

Comment by jason created at 2007-10-25 21:32:30

whew, this has been open a long time.  Good thing Mike implemented the combinatorics stuff recently ;).


---

Comment by cwitty created at 2007-10-27 02:47:26

Resolution: fixed
