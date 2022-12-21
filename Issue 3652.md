# Issue 3652: [with patch, needs review] FreeModule(ZZ, 2000).random_element() is far slower than it should be

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-07-13 22:19:27

Assignee: was

Currently, random_element on a `FreeModule` constructs a basis, even if we know the basis is trivial.  The attached patch fixes this for `FreeModule_ambient` and subclasses.

Before:

```
sage: K = FreeModule(ZZ, 2000)
sage: get_memory_usage()
118.60546875
sage: %time _ = K.random_element()
CPU times: user 1.45 s, sys: 0.12 s, total: 1.57 s
Wall time: 1.57 s
sage: get_memory_usage()
225.56640625
```


After:

```
sage: K = FreeModule(ZZ, 2000)
sage: get_memory_usage()
118.60546875
sage: %time _ = K.random_element()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
sage: get_memory_usage()
118.60546875
sage: timeit('K.random_element()')
125 loops, best of 3: 2.32 ms per loop
```


A 600-fold speedup.


---

Attachment

Applies nicely and does speed up the operation on my system.


---

Comment by mabshoff created at 2008-08-10 22:52:51

Resolution: fixed


---

Comment by mabshoff created at 2008-08-10 22:52:51

Merged in Sage 3.1.alpha1
