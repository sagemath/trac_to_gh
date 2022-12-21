# Issue 3362: lmul is broken for modules.

Issue created by migration from Trac.

Original creator: gfurnish

Original creation time: 2008-06-04 16:19:22

Assignee: robertwb


```
Integer(5)._lmul_(Integer(3))
```

 should produce 15, but instead throws

```
NotImplementedError: parents Integer Ring Integer Ring True
```

This makes it hard to write general code that works with noncomutative multiplication.  


---

Comment by robertwb created at 2008-06-05 10:01:08

If a._lmul_(b) is desired, why can't one simply write a*b? 

The raising of a NotImplementedError in _lmul_ signifies that _lmul_ is not implemented, and the two elements should be coerced into a common parent where the normal _mul_ should be used instead.


---

Comment by mabshoff created at 2008-10-28 16:57:37

Robert, any idea what is going on here? 

This is still broken with "new" coercion:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.2.alpha1, Release Date: 2008-10-26                  |
| Type notebook() for the GUI, and license() for information.        |
sage: Integer(5)._lmul_(Integer(3))
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/scratch/mabshoff/release-cycle/sage-3.2.alpha2/<ipython console> in <module>()

/scratch/mabshoff/release-cycle/sage-3.2.alpha2/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.RingElement._lmul_ (sage/structure/element.c:8032)()

/scratch/mabshoff/release-cycle/sage-3.2.alpha2/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.RingElement._lmul_ (sage/structure/element.c:8002)()

NotImplementedError: parents Integer Ring Integer Ring True
sage: 
```


Cheers,

Michael


---

Comment by robertwb created at 2008-10-28 17:19:38

This should be marked as invalid. _lmul_ and _rmul_ are used for multiplication by an element of the basering, not for multiplication of elements themselves. Throwing an error here is the right thing to do, as it signals that the coercion model an action is not the appropriate thing to do here, but rather that both a and b should be coerced to the same parent and a._mul_(b) should be called. 

Writing a*b or b*a preserves the order of operands are fed into _mul_, so non-commutative operations can be supported just fine. 

_lmul_, _rmul_, etc. are not made to be called directly anyways in most cases.


---

Comment by mabshoff created at 2008-10-28 17:22:26

RobertWB's wish is my command -> Invalid. :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-28 17:22:26

Resolution: invalid
