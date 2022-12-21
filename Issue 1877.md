# Issue 1877: same range variables -- bug in 3d plotting (probably very very very easy to fix)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-21 06:40:06

Assignee: was


```
sage: var('x,y')
sage: plot3d(sin(x*y), (x,-1,1), (x,-1,1))
boom!
```


The problem is that both ranges use the variable x.  The fix is to make
sure that the two variables are different and if not raise an exception (do this also in parametric_plot3d). 



---

Attachment

plot3d and parametric_plot3d should fail a tiny bit more gracefully if they're given two ranges using the same variable:

```
sage: var('x,y')
sage: plot3d(sin(x*y), (x,-1,1), (x,-1,1))
ValueError: If the ranges in the argument of plot3d are 3-tuples, then the first components of those 3-tuples must be different.
sage: var('u,v')
sage: parametric_plot3d((cos(u), sin(u) + cos(v), sin(v)), (u, 0, 2*pi), (u, -pi, pi))
ValueError: If the ranges in the argument of parametric_plot3d are both 3-tuples, then the first components of those 3-tuples must be different.
```



---

Comment by thomag created at 2008-08-26 15:52:31

Changing status from new to assigned.


---

Comment by thomag created at 2008-08-26 15:52:31

Changing assignee from was to thomag.


---

Comment by mabshoff created at 2008-08-29 00:32:07

Changing keywords from "" to "editor_mhansen".


---

Comment by robertwb created at 2008-09-02 08:39:02

Please give a message with the raised value error. Pending that, I'd give a positive review.


---

Attachment

thomag, your patch is along the right lines, but the implementation wasn't quite right.  You don't need to catch an error after raising it and then print something to the screen.  Just supply a message with the error, and it will show up unless it's caught somewhere else.  Also, when you fix a bug, you should add a doctest demonstrating the new, correct behavior.

I've posted a new patch that raises an error in the usual way, and provides a briefer but still clear error message.  If this is accepted, only trac_1877.patch should be applied.


---

Attachment

trac_1877_review.patch does some minor cosmetic adjustements on top of trac_1877.patch (like not starting the error messages with a capital).  Otherwise this gets a positive review from me.

It might still my part still needs to be reviewed so I'll leave it as needs review.


---

Comment by jwmerrill created at 2008-09-06 15:59:25

Your review patch looks good to me, positive review.  Both trac_1877.patch and trac_1877_review.patch should be applied


---

Comment by jwmerrill created at 2008-09-06 16:02:45

Oops, this won't pass it's doctests as written, since the review patch alters the error message thrown, but not the doctest.


---

Comment by anakha created at 2008-09-06 16:14:28

Shame on me.  But with the new patch the doctests are changed and they pass.


---

Attachment


---

Comment by mabshoff created at 2008-09-06 23:12:27

Merged trac_1877.patch, trac_1877_review.patch and trac_1877_doctests.patch in Sage 3.1.2.rc0.


---

Comment by mabshoff created at 2008-09-06 23:12:27

Resolution: fixed
