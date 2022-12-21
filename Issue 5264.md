# Issue 5264: [with patch, needs review] optimize small permgroup elements

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-02-14 06:49:24

Assignee: joyner

Avoid allocation for very small permutation group elements (which can be a significant cost of element creation). 


---

Attachment


---

Comment by robertwb created at 2009-02-14 06:58:02

Before: 


```
sage: G = SymmetricGroup(3)
sage: L = [G.random_element() for _ in range(100)] * 17
sage: timeit("prod(L)")
625 loops, best of 3: 651 µs per loop

sage: G = SymmetricGroup(10)
sage: L = [G.random_element() for _ in range(100)] * 17
sage: timeit("prod(L)")
625 loops, best of 3: 766 µs per loop

sage: G = SymmetricGroup(20)
sage: L = [G.random_element() for _ in range(100)] * 17
sage: timeit("prod(L)")
625 loops, best of 3: 854 µs per loop
```


After: 

```
sage: sage: G = SymmetricGroup(3)
sage: sage: L = [G.random_element() for _ in range(100)] * 17
sage: sage: timeit("prod(L)")
625 loops, best of 3: 485 µs per loop

sage: sage: G = SymmetricGroup(10)
sage: sage: L = [G.random_element() for _ in range(100)] * 17
sage: sage: timeit("prod(L)")
625 loops, best of 3: 564 µs per loop

sage: sage: G = SymmetricGroup(20)
sage: sage: L = [G.random_element() for _ in range(100)] * 17
sage: sage: timeit("prod(L)")
625 loops, best of 3: 876 µs per loop
```



---

Comment by mabshoff created at 2009-04-16 11:35:23

Resolution: fixed


---

Comment by mabshoff created at 2009-04-16 11:35:23

Merged in Sage 3.4.1.rc3.

Cheers,

Michael
