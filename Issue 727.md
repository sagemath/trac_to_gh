# Issue 727: find rational points on ternary quadratic forms -- volunteer needed

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-21 08:45:15

Assignee: somebody

CC:  ncalexan justin mstreng rlm pbruin


```
John Cremona <john.cremona`@`gmail.com> 		 hide details	 1:37 am (2 minutes ago) 
	reply-to		sage-support`@`googlegroups.com	 
	to		sage-support`@`googlegroups.com	 
	date		Sep 21, 2007 1:37 AM	 
	subject		[sage-support] Re: rational solutions to a bivariate polynomial	 
	mailed-by		googlegroups.com	 

It *is* a ternary quadratic form once you homogenize with a 3rd variable z.

Finding rational points on plane conics (which is what this is) has
advanced substantially in the last few years.  My paper with Rusin
(Mathematics of Computation, 72 (2003), no. 243, pages 1417-1441.)
works well for diaginal ones and is behind Magma's first
implementations for RationalPoint(Conic());  a different method by
Denis Simon is better for non-diagonal ones and is (I believe) what
Magma uses.

My method is implemented in the C++ code which is already in Sage in
the mwrank package, so all tat would be needed would be to write the
appropriate wrappers!

```



---

Comment by AlexGhitza created at 2008-01-27 05:02:02

Changing component from basic arithmetic to algebraic geometry.


---

Comment by AlexGhitza created at 2008-01-27 05:02:02

Changing assignee from somebody to was.


---

Comment by ncalexan created at 2008-02-29 08:26:55

This is so random -- I have written code to do this.  We already distribute Denis Simon's code to solve such systems, and I have have integrated a little of it.  Patch coming up.  Please talk to me before implementing this.


---

Comment by ncalexan created at 2008-02-29 08:26:55

Changing keywords from "" to "rational point points conic quadratic form".


---

Comment by mabshoff created at 2008-11-08 21:31:34

Changing assignee from was to justin.


---

Comment by mabshoff created at 2008-11-08 21:31:34

Changing component from algebraic geometry to quadratic forms.


---

Comment by mstreng created at 2009-06-18 18:06:03

Define a Conic class with an interface to Denis Simon's qfsolve


---

Comment by mstreng created at 2009-06-18 18:15:53

Changing assignee from justin to mhampton.


---

Attachment

The patches I just uploaded were part of ncalexan's patch for ticket 6341, implementing Mestre's algorithm. They implement a Conic class and allow one to find points over the rationals. This Conic class needs to be expanded to provide much more functionality, such as finding points and/or rational parametrizations over other fields. If the original question is only for the rationals, then that at least is answered.


---

Comment by mstreng created at 2009-06-18 18:15:53

Changing component from quadratic forms to geometry.


---

Comment by mstreng created at 2009-06-23 12:23:42

Changing status from new to assigned.


---

Comment by mstreng created at 2009-06-23 12:23:42

Changing assignee from mhampton to mstreng.


---

Comment by mstreng created at 2009-06-23 12:23:42

I'll work on the Conic class.


---

Attachment


---

Comment by mstreng created at 2010-07-06 14:27:55

* this is being revived at Sage Days 23

* trac_727-conic-extcode.patch should be removed: it updates Denis Simon's code from 2005 to 2007, while 2009 is already shipped with the latest Sage

* trac_727_more_conic_files.patch implements a Conic class that uses Denis Simon's code and can find points on conics over number fields and finite fields. It includes most of trac_727-conic.patch and works by itself on 4.4.4. Some doctests fail. It includes an incomplete and incorrect implementation of Hilbert symbols that should be replaced by the Hilbert symbols of #9334


---

Comment by mstreng created at 2010-07-06 16:13:06

* see http://wiki.sagemath.org/days23/conics

 * I missed the file sage/schemes/plane_conics/__init__.py (which is empty), so the patch in its current form doesn't work


---

Attachment

apply this patch and the one without "2" to get something that almost works


---

Attachment

needs two previous tickets trac_727_more... and trac_9334-hilbert.patch


---

Comment by mstreng created at 2010-07-12 12:31:07

apply after trac_727_more_conic_files1,2,3; requires trac_9334-hilbert.patch to work


---

Attachment

apply on sage 4.4.4 after trac_727_more_conic_files1,2,3,4, shouldn't require trac_9334-hilbert.patch


---

Attachment

apply on sage 4.4.4 after trac_727_more_conic_files1,2,3,4,5


---

Attachment

apply only this latest file


---

Attachment

apply the 1-6 patch on sage 4.5.1, then apply this one


---

Attachment

apply after 7 (there is no 8)


---

Comment by mstreng created at 2010-07-20 12:45:56

I'm running a doctest right now. I'll fold them when I get the time. Who wants to review it?


---

Comment by mstreng created at 2010-07-20 20:40:19

apply only this latest file (works on sage 4.4.4 and on 4.5.1)


---

Attachment

"All tests passed!", and I combined the patches into one file


---

Comment by mstreng created at 2010-07-20 20:42:15

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-07-20 21:22:28

Those `[with patch, needs review]` bits in the description are no longer necessary, thanks to the workflow.


---

Comment by cremona created at 2010-09-11 17:55:07

The patch applies fine to 4.6.alpha0, but not all the tests in the new directory pass:

```
	sage -t -long "devel/sage-main/sage/schemes/plane_conics/con_field.py"
	sage -t -long "devel/sage-main/sage/schemes/plane_conics/con_number_field.py"
	sage -t -long "devel/sage-main/sage/schemes/plane_conics/con_rational_field.py"
	sage -t -long "devel/sage-main/sage/schemes/plane_conics/rnfisnorm.py"
```

I feared that it would be worse after the new Pari upgrade (which is in 4.6.alpha0).  But it does need looking into.


---

Comment by cremona created at 2010-09-11 17:55:07

Changing status from needs_review to needs_work.


---

Comment by mstreng created at 2010-11-03 09:58:46

It worked just fine on my 4.5.something. I guess the problems are all in "devel/sage-main/sage/schemes/plane_conics/rnfisnorm.py", which we can get rid of after #2329 is finished. So let's do #2329 first.


---

Attachment

Apply trac_727_conics.patch to sage 4.6 after #2329 and #9334


---

Comment by mstreng created at 2010-12-08 17:34:03

Here's a version that uses hilbert symbols and rnfisnorm from resp. #9334 and #2329. This patch provides motivation and testcases for those two other tickets.


---

Attachment

Apply only this latest file (works on sage 4.6.1.rc0 without any other patches)


---

Comment by mstreng created at 2011-01-13 14:37:04

I moved all number field functionality to #10621. Because of this, no patches from other tickets are needed, you only need to apply trac_727_conics_without_number_fields.patch


---

Comment by mstreng created at 2011-01-13 14:37:04

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2011-01-22 15:36:28

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2011-01-22 15:36:28

This looks really good. It's embarrassing that we've been shipping Denis Simon's scripts with Sage for years but nobody's sat down and written the interface code necessary to make it accessible.

Patch applied fine to 4.6.2.alpha1, all doctests in sage/schemes passed, the ref manual built OK, and all the examples I tried worked.

I have one minor gripe: there are one or two cases where the new Conic classes inherit methods from the generic plane curve classes that perhaps ought to be replaced with more appropriate conic-specific implementations (e.g the method "rational_points"). But that can come in future tickets if people feel it's needed.


---

Comment by jdemeyer created at 2011-01-25 08:13:28

Resolution: fixed
