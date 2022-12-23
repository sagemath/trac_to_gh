# Issue 405: add setting of rows or columns to a matrix

Issue created by migration from https://trac.sagemath.org/ticket/405

Original creator: was

Original creation time: 2007-07-26 15:23:45

Assignee: was


```
On 7/26/07, David Joyner <wdjoyner@gmail.com> wrote:
> On 7/26/07, mak <mak@math.uvic.ca> wrote:
> > 1.  How do I change the entire row or column of a matrix at once?  In
> > pari, I could do e.g. a=[1,2,3;4,5,6], and then put a[1,]=[0,0,0],
> > which would give a=[0,0,0;4,5,6].  What's the sage equivalent?

There is no SAGE equivalent yet.  David's example might be helpful
below though.  The best you could in SAGE is set each entry
one at a time right now.  I should add something.  

def set_row(A, r, v):
    for i in range(A.ncols()):
         A[r, i] = v[i]

I'm not sure how we forgot to ever do this. 
```



---

Comment by was created at 2007-07-26 15:23:55

Changing priority from major to minor.


---

Comment by was created at 2007-07-26 15:23:55

Changing component from algebraic geometry to linear algebra.


---

Attachment


---

Comment by mhansen created at 2007-12-22 17:10:22

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2007-12-22 17:10:22

Changing status from new to assigned.


---

Comment by rlm created at 2007-12-22 18:00:46

merged in 2.9.1 rc0


---

Comment by rlm created at 2007-12-22 18:00:46

Resolution: fixed
