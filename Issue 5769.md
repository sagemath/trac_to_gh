# Issue 5769: power series are accidentally *mutable* (really dangerous)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-04-12 05:19:59

Assignee: somebody


```
wstein`@`sage:~/build/sage-3.4.1.rc2$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: ref2
sage: R.<t> = ZZ[[]]
sage: f = 1 + 17*t - 4*t^3 + O(t^5)
sage: f[1] = 10
...
IndexError: power series are immutable
```

Except they are mutable:

```
sage: f *= 2
sage: f
2 + 34*t - 8*t^3 + O(t^5)
```

But they shouldn't be!  The _imul_ method needs to be deleted.
| Sage Version 3.4.1.rc2, Release Date: 2009-04-10                   |
| Type notebook() for the GUI, and license() for information.        |


---

Comment by lftabera created at 2010-06-16 08:24:40

The code has nothing to do with mutability. 

sage: a= (1,2,3)

a is a tuple, an immutable object

sage: a += a
sage: a
(1, 2, 3, 1, 2, 3)

sage: R.<t> = ZZ[[]]
sage: f = 1 + 17*t - 4*t^3 + O(t^5)
sage: g=f
sage: g is f
True
sage: f+=f
sage: f
2 + 34*t - 8*t^3 + O(t^5)
sage: g
1 + 17*t - 4*t^3 + O(t^5)
sage: f is g
False


---

Comment by lftabera created at 2010-06-16 08:24:40

Resolution: invalid
