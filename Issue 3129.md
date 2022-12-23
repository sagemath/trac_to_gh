# Issue 3129: [with patch, needs review] The singular interface should not claim to support polynomial rings with no variables

Issue created by migration from https://trac.sagemath.org/ticket/3129

Original creator: broune

Original creation time: 2008-05-07 23:01:58

Assignee: broune

The function can_convert_to_singular in polynomial_singular_interface claims (by returning True) that Singular can support multivariate polynomial rings with no variables. This claim seems to be unintended, since the wrapper for Singular polynomial ideals claims the opposite.

The attached trivial patch makes can_convert_to_singular return False if the passed-in ring has zero generators.



---

Comment by broune created at 2008-05-07 23:03:06

Changing status from new to assigned.


---

Attachment


---

Comment by cwitty created at 2008-05-10 20:51:40

Looks good; doctests pass in sage/rings/polynomial.  Positive review.


---

Comment by mabshoff created at 2008-05-11 08:08:18

Merged in Sage 3.0.2.alpha0


---

Comment by mabshoff created at 2008-05-11 08:08:18

Resolution: fixed
