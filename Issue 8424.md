# Issue 8424: bounding box calculation doesn't handle NaN or infinity

Issue created by migration from https://trac.sagemath.org/ticket/8424

Original creator: jason

Original creation time: 2010-03-02 19:14:58

Assignee: was

CC:  robertwb robert.marik drkirkby

Robert Marik pointed out that there is a bug in the bounding box calculation of the following plot:


```
var('y')
plot3d(sqrt(sin(x)*sin(y)), (x,0,2*pi),(y,0,2*pi))
```


The problem is that there are lots of NaNs generated in the evaluation of the plot, and these are not handled well by the bounding box calculation.

The attached patch fixes the issues in two of the three places the bounding box is calculated.  A third place is not touched in plot3d/transform.pyx, where I don't have time to make sure the fix is the right one and supply the necessary doctests.


---

Comment by jason created at 2010-03-02 19:21:30

Changing assignee from was to jason.


---

Comment by jason created at 2010-03-02 19:26:21

Changing status from new to needs_review.


---

Attachment

New patch fixes one doctest.  Robert (either one! :), feel free to review this.

drkirkby: I use the INFINITY constant and the isfinite macro from math.h.  Does this pose a problem on Solaris?


---

Comment by robert.marik created at 2010-03-04 08:18:19

Works for me, installs fine, solves the problem, tests passed. 

When tested, I observed another (related, but probably independent) problem - #8433 

Documentation builds fine. Thanks for the patch, positive review!


---

Comment by robert.marik created at 2010-03-04 08:18:19

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-03-04 15:03:38

Hi Jason, 

The macros isfinite() and isinf() are both defined in math.h, so the use of either of those would not present a problem. 

INFINITY is defined for C99 code, so I believe that as long as you specify -std=c99 as an option to gcc, then it will be ok. 

Dave


---

Comment by jhpalmieri created at 2010-04-15 23:50:54

Merged "trac-8424-bounding-boxes.patch" into 4.4.alpha0.


---

Comment by jhpalmieri created at 2010-04-15 23:50:54

Resolution: fixed
