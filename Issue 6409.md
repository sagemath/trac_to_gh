# Issue 6409: srange inconsistent when including endpoints

Issue created by migration from https://trac.sagemath.org/ticket/6409

Original creator: malb

Original creation time: 2009-06-25 16:12:42

Assignee: somebody

CC:  robertwb craigcitro


```
sage: srange(1,0,include_endpoint=True)
[]
sage: srange(1,QQ(0),include_endpoint=True)
[0]
```


These two should agree on something.


---

Comment by mjordan7 created at 2010-05-24 23:59:47

Fixed srange problem. I used xsrange for some cases, which also had the same bug, so I modified xsrange as well. I added some doctests, and tested the speed. It is as fast as the old code for common calls.


---

Comment by mjordan7 created at 2010-05-24 23:59:47

Changing keywords from "" to "srange".


---

Comment by mjordan7 created at 2010-05-24 23:59:47

Changing status from new to needs_review.


---

Comment by lftabera created at 2010-06-22 15:49:45

Looks good, but I have made a superficial review with a rebase to 4.4.3, doctest passes, I will check better before giving positive review.


---

Comment by lftabera created at 2010-06-24 10:52:08

Changed last line of srange, positive review

new patch the previous one did not apply to a clean sage installation


---

Attachment


---

Comment by robertwb created at 2010-06-24 19:03:07

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-06-28 21:30:25

Changing status from positive_review to needs_work.


---

Comment by rlm created at 2010-06-28 21:30:25

Please tell the release manager which patches to apply. It is not clear here.

-- RLM + SD MSRI tutorial audience :)


---

Comment by rlm created at 2010-06-28 23:28:34

Changing status from needs_work to needs_info.


---

Comment by rlm created at 2010-06-28 23:42:47

Changing status from needs_info to needs_review.


---

Comment by rlm created at 2010-06-28 23:42:47

I was just being overly pedantic to demonstrate how to work with the trac server. I'll delete the older patches.


---

Comment by rlm created at 2010-06-28 23:43:30

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2010-06-29 16:09:50

It's conventional to put full names, not trac usernames, in the Author and Reviewer fields (as these are used to assemble the release notes). I'm assuming mjordan7 is Mark Jordan.


---

Comment by mpatel created at 2010-07-20 09:17:54

Resolution: fixed
