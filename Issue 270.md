# Issue 270: bug in permutation group arithmetic code

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-02-20 18:13:20

Assignee: somebody

This was found by Mike Hansen


```
sage: g1 = PermutationGroupElement([(1,2),(3,4,5)])
sage: g1.parent()   # => Symmetric group of order 5! as a permutation group
Symmetric group of order 5! as a permutation group
sage: g2 = PermutationGroupElement([(1,2)])
sage: g2.parent()   # => Symmetric group of order 2! as a permutation group
Symmetric group of order 2! as a permutation group
sage: g1*g2  # => (3,4,5)
(3,4,5)
sage: g2*g2
()
sage: g2*g1
---------------------------------------------------------------------------
<type 'exceptions.RuntimeError'>          Traceback (most recent call last)

/home/was/<ipython console> in <module>()

/home/was/element.pyx in element.MonoidElement.__mul__()

/home/was/element.pyx in element.bin_op_c()

/home/was/element.pyx in element.canonical_coercion_c()

/home/was/element.pyx in element._verify_canonical_coercion_c()

<type 'exceptions.RuntimeError'>: There is a bug in the coercion code in SAGE.
Both x (=(1,2)) and y (=None) are supposed to have identical parents but they don't.
In fact, x has parent 'SymmetricGroup(2)'
whereas y has parent '<type 'NoneType'>'
```



---

Comment by was created at 2007-02-27 13:49:50

Resolution: fixed
