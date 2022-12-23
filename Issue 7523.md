# Issue 7523: Lightweight Wrapper for Rpy2

Issue created by migration from https://trac.sagemath.org/ticket/7523

Original creator: amhou

Original creation time: 2009-11-24 06:22:36

Assignee: amhou

Keywords: rpy, rpy2

Creates an easier to use interface for Rpy2


---

Attachment

MAJORERROR: imports numpy and rpy2 into the global namespace. Not sure how to get past this.


---

Comment by amhou created at 2009-11-24 06:25:20

Changing status from new to needs_review.


---

Comment by was created at 2009-11-24 06:30:49


```
nice
[10:29pm] amhou:
not sure how to get past the importing into global namespace
[10:29pm] amhou:
because we definitely don't want that
[10:30pm] amhou:
but if I define within the functions, then the stuff called outside of the functions doesn't work
[10:30pm] amhou:
:-/
[10:30pm] williamstein:
Robert Bradshaw came up with some new clever, clever code to uniformly deal with this problem.
[10:30pm] williamstein:
I'll ping him.
```



---

Comment by robertwb created at 2009-11-24 07:07:29

In this case, I think what you want is http://www.python.org/dev/peps/pep-0369/

I'm not sure about using IntVector, as it will silently truncate all non-integer lists...


```
sage: list(rpy2.robjects.IntVector([1,1/2,pi]))
[1, 0, 3]
```



---

Comment by robertwb created at 2009-11-24 07:07:29

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by drkirkby created at 2010-03-19 22:44:17

R  has been updated (I've no idea what ticket, but it happened). I suspect these patches might need rebasing at the very least. 

dave
