# Issue 6206: move algebraic_closure method from RLF to LazyField

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-06-04 03:45:24

Assignee: was

CC:  craigcitro fwclarke robertwb

Keywords: number field lazy field algebraic_closure

Tiny patch moves algebraic_closure method up the tree; I claim this is "obviously" the correct place for it to be, but you only hit this bug (missing method) when you are using strange embeddings of number fields and I don't have a good example at hand.


---

Attachment


---

Comment by robertwb created at 2009-06-04 06:47:17

Yes, that makes sense.


---

Comment by robertwb created at 2009-06-04 06:49:07

Just a sec, while we're at it, I just noticed the docstring is wrong. It speaks of the "Complex Double Field" rather than "Complex Lazy Field." This was probably originally my fault, but might as well fix it now.


---

Comment by mhansen created at 2009-06-04 18:25:44

Merged in 4.0.1.rc1 (and took care of the double -> lazy change.


---

Comment by mhansen created at 2009-06-04 18:25:44

Resolution: fixed
