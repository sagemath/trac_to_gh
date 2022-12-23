# Issue 9752: sorting of number field elements is broken

Issue created by migration from https://trac.sagemath.org/ticket/9752

Original creator: was

Original creation time: 2010-08-15 17:46:07

Assignee: davidloeffler

The design of number field elements (and other aspects of sage) assumes that cmp defines a total ordering, which of course doesn't respect the algebraic field structure.   Unfortunately, the actual implementation (in number_field_element.pyx) is buggy and doesn't define a total ordering.   Look at the code and you'll see.  Or just look at this example:


```
sage: L.<b> = NumberField(x^3-10001)
sage: b+1 < L(1667)
False
sage: L(1667) < b+1
False
```




I think the best correct implementation of cmp should be one that is efficient and *also* agrees with the lexicographic ordering of elements based on their representation as a polynomial in the generator of the number field.   I did implement this as part of the patch bomb #9541.  The point of the present ticket is to "backport" something like this out of #9541, or implement a new fix from scratch.  This is motivated by #9400. 


---

Comment by jdemeyer created at 2010-09-20 19:26:05

See also #6132, there is some code to compare number field elements.


---

Comment by was created at 2011-03-21 01:17:13

Resolution: duplicate


---

Comment by was created at 2011-03-21 01:17:13

I'm closing this as a dup of #6132.
