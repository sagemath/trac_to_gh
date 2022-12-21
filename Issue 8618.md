# Issue 8618: Non standard alphabet

Issue created by migration from Trac.

Original creator: vdelecroix

Original creation time: 2010-03-28 09:12:23

Assignee: sage-combinat

CC:  sage-combinat

Keywords: word, substitution

It seems that some functions that use morphisms of words do not work for not standard alphabet. This ticket follows the bug found in the fixed_point method (#8595).

*pseudo palindrome*


```
sage: t = WordMorphism({'a1':['a2'], 'a2':['a1']})
sage: W = Words(['a1','a2'])
sage: W(['a1','a2']).is_palindrome(t)
AttributeError Traceback (most recent call last)
...
KeyError: 'a'
```




---

Comment by slabbe created at 2010-03-31 10:53:28

Changing status from new to needs_review.


---

Attachment

Depends on #8595


---

Comment by vdelecroix created at 2010-04-08 07:22:49

Changing status from needs_review to positive_review.


---

Comment by vdelecroix created at 2010-04-08 07:22:49

Thank you for this correction.


---

Comment by jhpalmieri created at 2010-04-16 18:50:38

Merged "trac_8618_is_identity-sl.patch" in 4.4.alpha0


---

Comment by jhpalmieri created at 2010-04-16 18:50:38

Resolution: fixed
