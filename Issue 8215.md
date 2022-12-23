# Issue 8215: The empty word is a factor of a word

Issue created by migration from https://trac.sagemath.org/ticket/8215

Original creator: slabbe

Original creation time: 2010-02-08 14:16:09

Assignee: slabbe

CC:  sage-combinat abmasse

Keywords: empty word

The following three results should be True.


```
sage: Word().is_factor(Word())
False
sage: Word().is_factor(Word('abad'))
False
sage: Word().is_factor(Word([0,1,2]))
False
sage: Word('').is_factor(Word('abad'))
False
sage: Word([]).is_factor(Word([0,1,2]))
False
```



---

Attachment


---

Comment by slabbe created at 2010-02-08 14:20:30

Changing status from new to needs_review.


---

Comment by abmasse created at 2010-02-10 10:56:02

Changing status from needs_review to positive_review.


---

Comment by abmasse created at 2010-02-10 10:56:02

Tested on sage 4.3.1. Doc builds fine, all tests passed and it fixes the bug. Not much more to say... Positive review !


---

Comment by mpatel created at 2010-02-11 14:48:35

Changing assignee from slabbe to mpatel.


---

Comment by mpatel created at 2010-02-11 14:49:06

Changing assignee from mpatel to slabbe.


---

Comment by mpatel created at 2010-02-11 14:49:06

Oops!


---

Comment by mpatel created at 2010-02-11 14:49:13

Resolution: fixed
