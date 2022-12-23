# Issue 2161: [with patch] some speed improvements for mpolynomials over ZZ

Issue created by migration from https://trac.sagemath.org/ticket/2161

Original creator: jbmohler

Original creation time: 2008-02-14 19:18:02

Assignee: malb

Here's a patch improving some things associated with scalar multiplication over ZZ.

Prior to patch:

```
sage: R.<x,y,z>=ZZ[]
sage: f=x+y+z
sage: timeit f*3
1000 loops, best of 3: 322 Âµs per loop
```


After patch:

```
sage: R.<x,y,z>=ZZ[]
sage: f=x+y+z
sage: timeit f*3
10000 loops, best of 3: 68 Âµs per loop
```



---

Attachment

scalar mult optimizations


---

Comment by ncalexan created at 2008-02-14 23:06:44

I say apply, it looks good to me.  There are additional improvements, it seems: maybe caching one, and the TODO (typoed to TOOD) about addition and subtraction.


---

Comment by malb created at 2008-02-14 23:11:24

Replying to [comment:1 ncalexan]:
> I say apply, it looks good to me.  There are additional improvements, it seems: maybe caching one, and the TODO (typoed to TOOD) about addition and subtraction.

Every parent should have a one cache called `_one_element` where *should* means that a parent is already supposed to implement it.


---

Comment by mabshoff created at 2008-02-15 00:17:35

Resolution: fixed


---

Comment by mabshoff created at 2008-02-15 00:17:35

Merged in Sage 2.10.2.alpha0
