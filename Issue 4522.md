# Issue 4522: [with patch, needs review] polynomial interface improvements

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2008-11-14 09:17:02

Assignee: burcin

Attached patch makes the following changes to improve the user interface of the polynomial classes:

 * Remove .name() method, since .variable_name() already provides same functionality.
 * make the .degree() function of univariate polynomials accept one argument,
  the generator, to be consistent with the .degree() of multivariate
  polynomials.
 * Add an .is_monomial() method to univariate polynomials.



---

Comment by burcin created at 2008-11-14 09:24:13

One more change I forgot to specify above:
 * make the .polynomial() function of univariate polynomials behave the same way as that of multivariate polynomials. (I.e., return a univariate polynomial with a coefficient ring in the rest of the generators of the same parent, which simply means returning self in this case.)


---

Comment by was created at 2008-11-28 03:57:08

REFEREE REPORT:

This looks very good. Positive review *subject* to you posting an additional patch that puts the name method back in and has a deprecation warning with a doctest of this.  We'll delete that in a few months.


---

Comment by was created at 2008-11-28 03:59:19

Oh yes, by the way, I doctested all of the rings directory after this patch and it works 100%.


---

Attachment

make the interface of polynomials more consistent


---

Comment by burcin created at 2008-11-28 12:45:54

New version of the patch with the deprecation warning, and doctests for it.

I'm marking this positivie review, since William didn't state that he wanted to see the patch again. :)


---

Comment by mabshoff created at 2008-11-28 20:51:15

Merged in Sage 3.2.1.rc0


---

Comment by mabshoff created at 2008-11-28 20:51:15

Resolution: fixed
