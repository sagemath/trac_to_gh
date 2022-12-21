# Issue 5061: Steenrod algebras report additive order of 0 is p

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2009-01-23 00:28:53

Assignee: tbd

This is wrong:


```
sage: S2 = SteenrodAlgebra(2)
sage: z = S2(0)
sage: z.additive_order()
2
```


looking at the code, it's easy to see why this happens...


```
    def additive_order(self):
        """
        The additive order of any element of the mod p Steenrod algebra is p.

        OUTPUT:
            order -- positive prime number

        EXAMPLES:
            sage: z = Sq(4) + Sq(6) + Sq(0)
            sage: z.additive_order()
            2
        """
        return self._prime
```




---

Comment by boothby created at 2009-01-23 01:43:35

Changing assignee from tbd to boothby.


---

Comment by boothby created at 2009-01-23 01:43:35

Changing priority from major to trivial.


---

Comment by boothby created at 2009-01-23 01:43:35

Changing status from new to assigned.


---

Comment by boothby created at 2009-01-23 01:43:35

Changing component from algebra to commutative algebra.


---

Comment by boothby created at 2009-01-23 02:18:10

Changing component from commutative algebra to algebra.


---

Attachment


---

Comment by robertwb created at 2009-01-23 22:16:58

Looks good. The documentation should probably be fixed as well though, and you need a doctest.


---

Attachment

apply on top of other patch


---

Comment by jhpalmieri created at 2009-02-26 18:50:20

Here's a documentation/doctest patch to go on top of the other one.


---

Comment by robertwb created at 2009-02-26 20:42:15

I'm happy with it.


---

Comment by mabshoff created at 2009-02-28 17:08:32

Resolution: fixed


---

Comment by mabshoff created at 2009-02-28 17:08:32

Merged both patches in Sage 3.4.rc0.

Cheers,

Michael
