# Issue 5987: fix a few more bad comparison doctests

Issue created by migration from https://trac.sagemath.org/ticket/5987

Original creator: AlexGhitza

Original creation time: 2009-05-05 07:35:47

Assignee: AlexGhitza

CC:  embray

To make up for my past mistakes, here's a simple patch that modifies or removes a few bad comparison doctests (not all of which were introduced by me).



---

Attachment


---

Comment by mabshoff created at 2009-05-05 07:45:36

This patch is wrong. Instead of deleting the tests they should either be rewritten as 

```
sage: f !=g
True
```

or

```
sage: f<g in [-1,1]
True
```


Cheers,

Michael


---

Comment by mabshoff created at 2009-05-05 07:47:30

And I forgot to mention: In some cases these comparisons are deterministic, so it needs to be dealt with on a case by case basis. I am not sure what applies in this case.

Cheers,

Michael


---

Comment by chapoton created at 2018-12-17 19:43:39

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2018-12-17 19:43:39

let us close this old one as obsolete


---

Comment by tscrim created at 2018-12-18 03:47:53

Changing status from needs_review to positive_review.


---

Comment by embray created at 2019-02-26 13:58:00

Resolution: invalid


---

Comment by embray created at 2019-02-26 13:58:00

Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.
