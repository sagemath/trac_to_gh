# Issue 6205: add __invert__ to number field morphism

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-06-04 03:42:36

Assignee: was

CC:  craigcitro fwclarke

Keywords: number field morphism invert

This tiny patch does the linear algebra to invert an endomorphism of a number field.


---

Attachment


---

Comment by craigcitro created at 2009-06-05 05:06:57

I like it. My only minor quibble is that I would add the one line "Return the inverse of self." to the docstring, even though it really adds no value whatsoever. 

So since there were no methods in that class before, and 1 now, does that mean this patch makes number field homomorphisms infniitely more useful? `:)`


---

Comment by ncalexan created at 2009-06-13 20:35:28

Resolution: fixed
