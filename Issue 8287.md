# Issue 8287: The _check used for creation of words makes it slower

Issue created by migration from Trac.

Original creator: slabbe

Original creation time: 2010-02-16 22:12:09

Assignee: slabbe

CC:  vdelecroix

The `_check` function of the Combinatorial class of all words (checking that the 40 first letters of the word are in the parent) is called for each word created by the user ....and by any other function. It would be good to add a check parameter (True or False) whether to do the checking. For example, for internal function, it could be turned off. Here is a example of what can be gained from this modification when generating all words of a given length :

BEFORE:

```
sage: W = Words([0,1])
sage: time l = list(W.iterate_by_length(15))
CPU times: user 2.60 s, sys: 0.09 s, total: 2.69 s
Wall time: 2.71 s
```


AFTER:


```
sage: W = Words([0,1])
sage: time l = list(W.iterate_by_length(15))
CPU times: user 1.99 s, sys: 0.06 s, total: 2.05 s
Wall time: 2.08 s
```





---

Comment by slabbe created at 2010-02-17 00:03:44

Changing status from new to needs_work.


---

Attachment


---

Comment by slabbe created at 2015-12-02 10:22:29

It was done last year in #17021. I suggest to close this ticket as duplicate.


---

Comment by slabbe created at 2015-12-02 10:22:29

Changing status from needs_work to needs_review.


---

Comment by vdelecroix created at 2015-12-02 19:48:02

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-12-04 22:12:43

Resolution: fixed
