# Issue 9344: matrix constructor does not honor nrows if given a method to generate the entries

Issue created by migration from https://trac.sagemath.org/ticket/9344

Original creator: lftabera

Original creation time: 2010-06-26 10:13:59

Assignee: AlexGhitza

The is a bug in the matrix constructor. If the entries are given by a method, the output matrix is always square of dimension ncols


```
sage: matrix(QQ, 1, 3, lambda x,y: x)
[0 0 0]
[1 1 1]
[2 2 2]
sage: sage: matrix(QQ, 3, 1, lambda x,y: x)
[0]
```



---

Attachment


---

Comment by lftabera created at 2010-06-26 10:15:00

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2010-06-29 14:36:17

Looks fine and all doctests pass. Positive review.


---

Comment by davidloeffler created at 2010-06-29 14:36:17

Changing status from needs_review to positive_review.


---

Attachment

apply this patch -- identical code but with more informative hg header information


---

Comment by davidloeffler created at 2010-06-30 08:58:33

Just an afterthought: I noticed while cleaning up my hg queue that this patch doesn't have a very informative name and also there is essentially no information in the hg header. This makes the release maintainer's job harder (they have to keep track of hundreds of patches and remember what to attribute to whom in the release notes). I've uploaded a patch functionally identical to yours, but with your full username and a more informative filename and commit message.


---

Comment by mpatel created at 2010-07-20 09:30:38

Resolution: fixed
