# Issue 8367: element_class of Subsets is broken

Issue created by migration from Trac.

Original creator: giraudo

Original creation time: 2010-02-25 17:39:41

Assignee: giraudo

Keywords: Subsets element_class

element_class of Subsets is broken

```
sage: s = Subsets(Set([1]))
sage: e = s.first()
sage: isinstance(e, s.element_class)
False
```


Note: this should be caught by setting good categories 

```
sage: s.category()
Category of objects
```



---

Attachment


---

Comment by giraudo created at 2010-02-25 18:22:52

Changing status from new to needs_review.


---

Comment by hivert created at 2010-03-01 16:39:18

Replying to [comment:1 giraudo]:

Hi Samuele,

I think you made a mistake in opening new ticket #8396 for this problem. This ticket should be closed as duplicate.


---

Comment by hivert created at 2010-03-01 16:39:18

Resolution: duplicate
