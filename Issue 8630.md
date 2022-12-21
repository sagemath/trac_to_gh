# Issue 8630: Cusp forms constructor ignores the character and returns enormous space

Issue created by migration from Trac.

Original creator: davidloeffler

Original creation time: 2010-03-30 11:37:41

Assignee: craigcitro


```
sage: chi = DirichletGroup(109, CyclotomicField(3)).0
sage: CuspForms(chi, 2, base_ring = CyclotomicField(9))
Cuspidal subspace of dimension 442 of Modular Forms space of dimension 10, character [zeta3 + 1] and weight 2 over Cyclotomic Field of order 9 and degree6
```


*facepalm*


---

Comment by davidloeffler created at 2010-03-30 15:32:54

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2010-03-30 16:23:55

Changing status from needs_review to needs_work.


---

Comment by davidloeffler created at 2010-03-30 16:23:55

*** wait, it's still wrong in certain nastly cases ***


---

Attachment


---

Comment by davidloeffler created at 2010-03-30 17:40:08

Changing status from needs_work to needs_review.


---

Comment by was created at 2010-03-30 18:06:16

Changing priority from major to blocker.


---

Comment by was created at 2010-03-31 01:48:38

All doctests pass when this is applied against sage-4.3.5.


---

Comment by was created at 2010-03-31 05:02:32

1. Below "ring" should be "modular symbols space":

```
 	117	    def change_ring(self, R): 
 	118	        r""" 
 	119	        Return this ring with the base ring changed to the ring R. 
```


2. Here I think the sentence should end with ::


```
 	419	    A more complicated example involving both a nontrivial character, and a 
 	420	    base field that is not minimal for that character: 
```



It's really awesome that you sphinxified a bunch of docs, in addition to fixing the bug in this ticket.


---

Comment by was created at 2010-03-31 05:02:32

Changing status from needs_review to positive_review.


---

Attachment

apply over previous patch


---

Comment by davidloeffler created at 2010-03-31 11:08:07

Here's a tiny patch that corrects the two things you pointed out in the docstrings.


---

Comment by jhpalmieri created at 2010-04-16 18:54:00

Merged in 4.4.alpha0:
 - trac_8630.patch
 - trac_8630_docfixes.patch


---

Comment by jhpalmieri created at 2010-04-16 18:54:00

Resolution: fixed
