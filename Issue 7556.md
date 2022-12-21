# Issue 7556: change default rounding behavior for QQ to

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-11-29 23:34:16

Assignee: AlexGhitza

This is inconsistent:

```
sage: (9/2).round()
4
sage: RDF('4.5').round()
5
sage: import __builtin__
sage: __builtin__.round(float('4.5'))
5.0
sage: RR('4.5').round()
5
```


It's also inconsistent for negatives.  The simple fix is to make the default rounding direction 'away' in rational.pyx. 


---

Comment by was created at 2009-11-29 23:40:47

Changing status from new to needs_review.


---

Attachment


---

Comment by mhansen created at 2009-11-30 04:01:39

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-30 04:01:39

Looks good to me.


---

Comment by mhansen created at 2009-12-01 05:09:52

Resolution: fixed
