# Issue 5280: problem with a subposet coming from an order_filter

Issue created by migration from https://trac.sagemath.org/ticket/5280

Original creator: jhpalmieri

Original creation time: 2009-02-15 23:44:24

Assignee: somebody

CC:  sage-combinat

With sage-3.3.rc0:

```
sage: B = BooleanLattice(3)
sage: 4 in B
True
sage: B.principal_order_filter(4)  # all elements >= 4
[4, 5, 6, 7]
sage: B.subposet(B.principal_order_filter(4))
Finite poset containing 4 elements
sage: show(B.subposet(B.principal_order_filter(4)))
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
...
NotImplementedError: BUG: sort algorithm for elements of 'Finite lattice containing 8 elements' not implemented
```


I get the same problem with 'order_filter' instead of 'principal_order_filter', and also for 'order_ideal' (e.g., `show(B.subposet(B.order_ideal([2, 4])))` produces a similar message).  Note, though, that `show(B.subposet(B.principal_order_ideal(4)))` works just fine.




---

Attachment

I implemented `__cmp__` for poset elements, which deals with these problems.

The patch depends on #5918.


---

Comment by jhpalmieri created at 2009-05-03 04:36:15

This fixes the problem, and all tests pass.  I'd like to give this a positive review since I reported the original problem, but I'm not familiar enough with the posets code to evaluate all of the changes here.  Can anyone else help out?


---

Comment by rlm created at 2009-06-19 22:44:00

I'd also give this a positive review, but I have to ask: why is `__cmp__` returning 1 (`cmp(a,b)==1` indicates `a < b`) when elements are incomparable? Shouldn't it be raising an error instead?


---

Attachment

I've added a patch which fixes some doc formatting.


---

Comment by rlm created at 2009-06-20 01:24:09

mhansen, care to at least comment why this doesn't concern you?:

Replying to [comment:5 rlm]:
> Why is `__cmp__` returning 1 when elements are incomparable? Shouldn't it be raising an error instead?


---

Comment by saliola created at 2009-06-21 12:39:10

Replying to rlm:

> Why is `__cmp__` returning 1 when elements are incomparable? Shouldn't it be raising an error instead?

Here are a couple of reasons why it shouldn't.

(1) `__cmp__` should never raise an error, otherwise you won't be able to
sort a list of elements:


```
sage: class C(object):
...       def __cmp__(self, other):
...           raise ValueError, 'elements are incomparable'

sage: sorted([C(), C()])
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "<ipython console>", line 3, in __cmp__
ValueError: elements are incomparable
```


(2) All the rich comparisons have been implemented for `PosetElement`, so
`x<y` is handled by `x.__lt__(y)`. That is, the answer will be correct.


So you might wonder why `__cmp__` even needs to be implemented. Shouldn't
`cmp` just use the rich comparison methods to determine its value? 

In theory, yes. But `PosetElement` inherits from `Element`, which
defines `__cmp__`. It seems to be that since `__cmp__` is not the
default implementation (`object.__cmp__`), the `cmp` function ignores
all the rich comparison operations and calls `__cmp__` directly. See the
following example, which was adapted from
[http://docs.sympy.org/_sources/python-comparisons.txt](http://docs.sympy.org/_sources/python-comparisons.txt).


```
sage: class C_without_cmp(SageObject):
...       def __init__(self, a):
...           self.a = a
...       def __repr__(self):
...           return str(self.a)
...       def __eq__(self, o):
...           print "%s.__eq__(%s)" % (self.a, o.a)
...           return NotImplemented
...       def __ne__(self, o):
...           print "%s.__ne__(%s)" % (self.a, o.a)
...           return NotImplemented
...       def __lt__(self, o):
...           print "%s.__lt__(%s)" % (self.a, o.a)
...           return NotImplemented
...       def __le__(self, o):
...           print "%s.__le__(%s)" % (self.a, o.a)
...           return NotImplemented
...       def __gt__(self, o):
...           print "%s.__gt__(%s)" % (self.a, o.a)
...           return NotImplemented
...       def __ge__(self, o):
...           print "%s.__ge__(%s)" % (self.a, o.a)
...           return NotImplemented

# cmp uses the rich comparison methods if no __cmp__ is found
sage: a = C_without_cmp("a"); b = C_without_cmp("b")
sage: cmp(a,b)
a.__eq__(b)
b.__eq__(a)
b.__eq__(a)
a.__eq__(b)
a.__lt__(b)
b.__gt__(a)
b.__gt__(a)
a.__lt__(b)
a.__gt__(b)
b.__lt__(a)
b.__lt__(a)
a.__gt__(b)
1

sage: class C_with_cmp(C_without_cmp):
...       def __cmp__(self, o):
...           print "%s.__cmp__(%s)" % (self.a, o.a)
...           return NotImplemented

# cmp uses __cmp__, ignoring the rich comparison methods if it is defined
sage: a = C_with_cmp("a"); b = C_with_cmp("b")
sage: cmp(a,b)
a.__cmp__(b)
b.__cmp__(a)
-1
```


This leads to the following error for posets, which is what this ticket is about.


```
sage: P = Poset([[1,2],[3],[3],[]])
sage: sorted(P)
[0, 1, 2, 3]
sage: sorted(P, cmp)
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "element.pyx", line 648, in sage.structure.element.Element.__cmp__ (sage/structure/element.c:6062)
  File "element.pyx", line 561, in sage.structure.element.Element._cmp (sage/structure/element.c:5133)
  File "element.pyx", line 663, in sage.structure.element.Element._cmp_c_impl (sage/structure/element.c:6237)
NotImplementedError: BUG: sort algorithm for elements of 'Finite poset containing 4 elements' not implemented

> /home/saliola/Applications/sage-4.0.2-busted/local/bin/element.pyx(663)sage.structure.element.Element._cmp_c_impl (sage/structure/element.c:6237)()
```


So I implemented `__cmp__` for `PosetElement`.

Are these satisfactory reasons?


---

Comment by rlm created at 2009-06-21 12:47:42

Franco,

Thanks for the incredibly detailed explanation! The main reason I was asking is that there is no indication why this is okay in the code itself. Could you put a sentence or two, maybe just in a comment, explaining why this is done? Maybe something like "When the user asks for `a<b`, rich comparison is used, and this is implemented only to enable sorting." Also, if the result of sorting isn't consistent (e.g. cmp(a,b) == cmp(b,a)), this should be mentioned too, I think.


---

Comment by saliola created at 2009-06-21 18:43:18

Replying to [comment:10 rlm]:
> Franco,
> 
> Thanks for the incredibly detailed explanation! The main reason I was asking is that there is no indication why this is okay in the code itself. Could you put a sentence or two, maybe just in a comment, explaining why this is done? Maybe something like "When the user asks for `a<b`, rich comparison is used, and this is implemented only to enable sorting." Also, if the result of sorting isn't consistent (e.g. cmp(a,b) == cmp(b,a)), this should be mentioned too, I think.

I'm attaching a patch with the docfixes, and that also implements the
`__ne__` method, which I must have forgot to define. (Unfortunately, in
Python `__ne__` does not default to `!__eq__`.)


---

Attachment

Apply on top of the previous two.


---

Comment by rlm created at 2009-06-21 22:01:39

Looks good, applies and passes tests.


---

Comment by nthiery created at 2009-06-22 06:26:00

Replying to [comment:10 rlm]:
> Franco,
> 
> Thanks for the incredibly detailed explanation! The main reason I was asking is that there is no indication why this is okay in the code itself. Could you put a sentence or two, maybe just in a comment, explaining why this is done? Maybe something like "When the user asks for `a<b`, rich comparison is used, and this is implemented only to enable sorting." Also, if the result of sorting isn't consistent (e.g. cmp(a,b) == cmp(b,a)), this should be mentioned too, I think.

Thanks also! I am having similar problems in several other places. This really should be though of once for all, and a systematic policy should be set up for
all occurences of this issue. Actually, it would be best if this could be solved once for all at a higher level (in Element)?

One fine point (which certainly does not jeopardize this patch): I would feel better returning 0 for incomparable elements rather than +1.

Would you mind starting a discussion about this on sage-devel?


---

Comment by saliola created at 2009-06-22 10:21:27

Replying to [comment:14 nthiery]:

> One fine point (which certainly does not jeopardize this patch): I would feel better returning 0 for incomparable elements rather than +1.

That's fine with me. I just picked one randomly, but 0 is better. I will make the change.

> Would you mind starting a discussion about this on sage-devel?

http://groups.google.com/group/sage-devel/browse_thread/thread/44dbe252426c3831


---

Attachment

Apply on top of the previous three


---

Comment by saliola created at 2009-06-22 10:39:07

The last change that switches to returning 0 instead of 1 for incomparable elements needs reviewing.


---

Comment by rlm created at 2009-06-22 10:44:26

Looks good.


---

Comment by rlm created at 2009-06-24 10:14:11

Resolution: fixed
