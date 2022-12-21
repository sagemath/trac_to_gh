# Issue 911: hash() on Graph objects changes as the object is mutated

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-10-17 06:20:15

Assignee: somebody

This is bad:

```
sage: foo = Graph()
sage: hash(foo)
1033452963
sage: foo.add_vertex(1)
sage: hash(foo)
1537218837
```


__hash__ on Graph objects should be overridden to raise a TypeError.


---

Comment by jason created at 2007-10-17 15:26:23

From the python docs for __hash__ at http://docs.python.org/ref/customization.html :

"If a class defines mutable objects and implements a __cmp__() or __eq__() method, it should not implement __hash__(), since the dictionary implementation requires that a key's hash value is immutable (if the object's hash value changes, it will be in the wrong hash bucket)."

Currently, a Graph object defines a __cmp__ method, but not a __hash__ method.  This seems to be in accordance with the python docs.  However, I guess we are inheriting the __hash__ method from SageObject, so we should redefine the __hash__ method?

Here's a patch:


```
diff -r 36489d2c9a2e sage/graphs/graph.py
--- a/sage/graphs/graph.py      Tue Oct 16 09:50:59 2007 -0500
+++ b/sage/graphs/graph.py      Wed Oct 17 10:19:53 2007 -0500
`@``@` -359,6 +359,20 `@``@` class GenericGraph(SageObject):
             return self._nxg.name
         else:
             return repr(self)
+
+    def __hash__(self):
+        """
+       Since graphs are mutable, they should not be hashable, so we return a type error.
+
+       EXAMPLE:
+           sage: hash(Graph())
+            Traceback (most recent call last):
+            ...
+            TypeError: graphs are mutable, and so therefore are unhashable
+    
+       """
+       raise TypeError, "graphs are mutable, and so therefore are unhashable"
+
 
     def _latex_(self):
         """
```



---

Comment by jason created at 2007-10-17 15:26:23

Changing assignee from somebody to was.


---

Comment by jason created at 2007-10-17 15:26:23

Changing keywords from "" to "graphs".


---

Comment by jason created at 2007-10-17 15:26:23

Changing component from basic arithmetic to combinatorics.


---

Attachment


---

Comment by ekirkman created at 2007-10-18 02:41:39

Defect resolved by attached patch.  Ready to include in 2.8.8!


---

Comment by mabshoff created at 2007-10-18 10:09:50

Please see http://groups.google.com/group/sage-devel/t/72ca87d027fb3e63 regarding the

```
[tested by ...]
```

byline.

Cheers,

Michael


---

Comment by was created at 2007-10-21 00:48:45

Resolution: fixed
