# Issue 5283: problem with posets: iterating the subposet construction

Issue created by migration from https://trac.sagemath.org/ticket/5283

Original creator: jhpalmieri

Original creation time: 2009-02-16 07:01:52

Assignee: somebody

CC:  sage-combinat

If I try to create a subposet of a subposet of something, I have problems:

```
sage: P = BooleanLattice(2)
sage: above = P.principal_order_filter(0)
sage: Q = P.subposet(above)
sage: above_new = Q.principal_order_filter(Q.list()[0])
sage: Q.subposet(above_new)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/Users/palmieri/.sage/temp/Macintosh.local/16679/_Users_palmieri__sage_init_sage_0.py in <module>()

/Applications/sage/local/lib/python2.5/site-packages/sage/combinat/posets/posets.pyc in subposet(self, elements)
   1036             raise ValueError, "not a list."
   1037         for element in elements:
-> 1038             if element not in self:
   1039                 raise ValueError, "element not in self"
   1040         relations = []

/Applications/sage/local/lib/python2.5/site-packages/sage/combinat/posets/posets.pyc in __contains__(self, x)
    272         else:
    273             y = x
--> 274         return y in self._elements
    275 
    276     def __call__(self,element):

/Applications/sage/local/lib/python2.5/site-packages/sage/combinat/posets/elements.pyc in __eq__(self, other)
     50             False
     51         """
---> 52         return self.parent() == other.parent() \
     53                 and self.element == other.element \
     54                 and self.vertex == other.vertex

AttributeError: 'int' object has no attribute 'parent'
```

I think that the problem is in the `__contains__` method for posets, where the argument x is converted to x.element, which might be an int.  I'm not sure why I have to iterate the subposet construction twice to get this to happen...




---

Attachment

The poset elements are just wrapping elements, so I modified the subposet constructor to unwrap before constructing the subposet (it was wrapping a wrapped element).

Note that you can still create a poset of poset elements, this is just for the subposet constructor.


---

Comment by jhpalmieri created at 2009-05-03 04:36:50

This fixes the problem, and all tests pass.  Simple change to the code, good addition to the doctests.


---

Comment by mabshoff created at 2009-05-11 10:00:45

Merged in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-11 10:00:45

Resolution: fixed
