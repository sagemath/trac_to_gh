# Issue 8666: Bug in cyclotomic linear algebra

Issue created by migration from https://trac.sagemath.org/ticket/8666

Original creator: craigcitro

Original creation time: 2010-04-09 22:11:38

Assignee: AlexGhitza

CC:  robertwb

David Loeffler ran into this bug:


```
sage: K.<zeta4> = CyclotomicField(4) 
sage: m = matrix(K, [186]) 
sage: n = matrix(K, [125]) 
sage: m * n 
[-23087] 
```


(See http://groups.google.com/group/sage-devel/browse_thread/thread/4f8633d6acf1c4ef# for the full thread.)

The issue is that the bound for what modulus the entries can be computed modulo is off by a factor of 2, because it doesn't take the sign into consideration. (Amusingly, this was basically the same fix as in #4823.) 


---

Comment by craigcitro created at 2010-04-09 22:14:23

Changing status from new to needs_review.


---

Attachment


---

Comment by robertwb created at 2010-04-09 22:18:01

Yep, that should do it.


---

Comment by robertwb created at 2010-04-09 22:18:01

Changing status from needs_review to positive_review.


---

Comment by burcin created at 2010-04-11 12:48:52

This is a duplicate of #8541. Since this already has a patch with positive review, we should close #8541.


---

Comment by jhpalmieri created at 2010-04-16 18:41:06

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-16 18:41:06

Merged trac_8666.patch in 4.4.alpha0.
