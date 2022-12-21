# Issue 8912: documentation error in pseudo_order for finite monoid element

Issue created by migration from Trac.

Original creator: saliola

Original creation time: 2010-05-07 14:56:05

Assignee: saliola

Keywords: documentation

the word self is latexed in the first line of the documentation string, but it shouldn't be.


```
m = FiniteMonoids().example()
x = m.an_element()
x.pseudo_order??
```


a patch is coming soon


---

Attachment


---

Comment by saliola created at 2010-05-07 15:30:03

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-05-08 23:53:27

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-05-08 23:53:27

Looks good to me.


---

Comment by mvngu created at 2010-05-09 04:16:42

Resolution: fixed
