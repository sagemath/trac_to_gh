# Issue 8902: Subsets element construction is broken

Issue created by migration from https://trac.sagemath.org/ticket/8902

Original creator: hivert

Original creation time: 2010-05-06 02:30:52

Assignee: sage-combinat

CC:  sage-combinat

Keywords: Subsets constructor


```
sage: S2 = Subsets(2)
sage: S2([])
<type 'sage.structure.parent.Set_generic'>
sage: S2([1])
<type 'sage.structure.parent.Set_generic'>
```



---

Comment by hivert created at 2010-05-12 20:12:41

Note: This is a temporary fixes before the cleanup of combinat (categorification of the combinatorial classes is done).


---

Comment by hivert created at 2010-05-12 20:12:41

Changing status from new to needs_review.


---

Comment by hivert created at 2010-05-12 20:12:55

Changing assignee from sage-combinat to hivert.


---

Attachment


---

Comment by hivert created at 2010-05-31 10:31:06

Nicolas on sage-combinat series file:

```
trac_8902-subsets_call_fix-fh.patch               # Positive review, assuming tests pass (NT)
```

I got a all test passes on massena.

Note: the category related problem we discussed on the phone is postponed until #8910 in the patch `trac_8910-subsets_an_element-fh.patch`. 

If you are ok with that can you put a positive review ?


---

Comment by nthiery created at 2010-05-31 11:54:40

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-05 22:18:51

Resolution: fixed
