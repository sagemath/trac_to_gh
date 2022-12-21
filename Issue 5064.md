# Issue 5064: Steenrod algebras are non-unique

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2009-01-23 02:16:15

Assignee: tbd

CC:  jhpalmieri


```
sage: A = SteenrodAlgebra(17)
sage: A(0).parent() is A
False
```



---

Comment by boothby created at 2009-01-23 02:16:45

Changing priority from major to minor.


---

Comment by boothby created at 2009-01-23 02:16:45

Changing component from algebra to commutative algebra.


---

Comment by boothby created at 2009-01-23 02:16:45

Changing assignee from tbd to malb.


---

Comment by boothby created at 2009-01-23 02:17:32

Changing component from commutative algebra to algebra.


---

Comment by boothby created at 2009-01-23 02:17:32

Changing assignee from malb to tbd.


---

Attachment


---

Comment by shumow created at 2009-01-24 11:42:45

tried the patch, it doesn't work for me.


---

Comment by shumow created at 2009-01-24 11:49:58

My bad.  I screwed up the test.  It works for me now.
I ran the tests and looked the code over, but I don't know enough about Steenrod Algebras to feel comfortable refereeing this.


---

Comment by shumow created at 2009-01-24 12:02:17

On closer explanation from boothby, I feel I can give this a positive review.


---

Comment by mabshoff created at 2009-01-24 16:28:55

Merged in Sage 3.3.alpha2


---

Comment by mabshoff created at 2009-01-24 16:28:55

Resolution: fixed
