# Issue 9394: latex representation of negative coefficients broken

Issue created by migration from https://trac.sagemath.org/ticket/9394

Original creator: burcin

Original creation time: 2010-06-30 12:05:02

Assignee: burcin

Keywords: pynac

Reported by Mike Witt on sage-support:


```
sage: latex(t)
\left(2 I\right) \, \pi n x + \left(-2 I\right) \, \pi n
```


`+ (-2 I )` looks really ugly.


---

Comment by fwclarke created at 2010-07-02 20:03:39

See recent comments in #8938, where similar phenomena have been noted.


---

Comment by burcin created at 2010-09-12 11:54:10

Changing status from new to needs_review.


---

Attachment

With the new pynac package at #9901, we have:


```
sage: var('n')
n
sage: t = 2*I*n*pi*x - 2*I*n*pi
sage: latex(t)
2 i \, \pi n x - 2 i \, \pi n
```


attachment:trac_9394-leading_minus.patch contains the doctest changes. The fixes in the printing of rational functions (for #9834) are also included in this patch.

The pynac package includes patches for #9834, #9878, #9879, #9881, #9900 as well as this ticket. See the ticket description of #9901 for the list (and order) of patches associated to the new version.


---

Comment by kcrisman created at 2010-09-22 17:59:58

With #9901, positive review.  Do not merge until #9901 has positive review and is merged.


---

Comment by kcrisman created at 2010-09-22 17:59:58

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-10-06 03:20:02

Resolution: fixed
