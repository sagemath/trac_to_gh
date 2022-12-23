# Issue 7372: Fix iterator for finite fields

Issue created by migration from https://trac.sagemath.org/ticket/7372

Original creator: rbeezer

Original creation time: 2009-11-01 23:57:36

Assignee: AlexGhitza

CC:  malb ylchapuy

Keywords: finite field iterator


```
sage: K.<a>=GF(2^16)
sage: K.list()
...
TypeError: 'sage.rings.ring.FiniteFieldIterator' object is not iterable
```


See #7366 for smaller fields (givaro implementation), this is for fields as large as 2^16.

Discussion: http://groups.google.com/group/sage-devel/browse_thread/thread/f141bdaaebf4bcbf



---

Attachment


---

Comment by malb created at 2009-11-02 00:01:53

This is a dupe of #7370 although your doctest is better :)


---

Comment by rbeezer created at 2009-11-02 00:05:47

OK, malb caught me in the act, and this is fixed.  See #7370.

Release manager - mark this obsolete.


---

Comment by mhansen created at 2009-11-02 04:20:40

Resolution: duplicate
