# Issue 8107: Fewer unnecessary imports from `sage.server.*`

Issue created by migration from https://trac.sagemath.org/ticket/8107

Original creator: mpatel

Original creation time: 2010-01-28 05:33:30

Assignee: was

CC:  robertwb timdumol

This should reduce startup time, according to `sage -startuptime`.




---

Attachment

_sage_ repo.


---

Comment by mpatel created at 2010-01-28 05:55:54

The _sage_-repository patch and #8102 together reduce the overall time for me from ~1.9 s to ~1.7 s.


---

Comment by mpatel created at 2010-01-28 05:55:54

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-01-28 05:57:07

I'm sure we can do better with #7502...


---

Comment by was created at 2010-01-28 06:00:45

Awesome -- I was just being annoyed by precisely these imports last night.


---

Comment by was created at 2010-01-28 06:00:45

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2010-01-28 09:43:21

A big +1 from me too. I'm curious about the comment 


```
# We import the following two only for doctesting purposes
```


though.


---

Comment by mpatel created at 2010-01-30 05:18:33

Replying to [comment:4 robertwb]:
> A big +1 from me too. I'm curious about the comment 

```
# We import the following two only for doctesting purposes
```

I'm not sure, but post-#7650, these imports should be unnecessary.  The patch above does not affect the results of `make ptestlong` on sage.math.


---

Comment by mvngu created at 2010-01-30 23:52:17

Resolution: fixed
