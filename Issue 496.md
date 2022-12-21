# Issue 496: In several places the generic powering and n*x code is stupid.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-08-27 21:26:34

Assignee: boothby

* In rings/arith.py the code for generic powering does an extra multiply the last time through the loop.
This can take a huge amount of extra time on big powering.

* In structure/element.pyx the code for generic n*x (the function cdef ModuleElement _lmul_c_impl(self, RingElement right), around line 1125) does possibly an extra add.


To fix this either rewrite or refactor the above code to be more like the __pow__ that is around
line 1057 of element.pyx.  Also, write *lots of doctests* to make sure you're really computing
the right thing. 



---

Attachment

Attached patch fixes the problem.


---

Comment by boothby created at 2007-08-28 06:43:29

Resolution: fixed


---

Comment by mabshoff created at 2007-08-28 07:27:10

Hello,

I think that bugs should only be closed as fixed once the patch has made it into the Repo. While this might be the case at least to the outside world this changeset is not visible yet. So I would suggest adding in Action an option "fix attached" to the resolve option.

Cheers,

Michael


---

Comment by boothby created at 2007-08-29 23:16:35

Resolution changed from fixed to 


---

Comment by boothby created at 2007-08-29 23:16:35

Changing status from closed to reopened.


---

Comment by boothby created at 2007-08-29 23:16:35

Attached file introduces bugs.  Better fix is located at:

[http://sage.math.washington.edu/home/boothby/my_patches/arith_2.8.3.hg](http://sage.math.washington.edu/home/boothby/my_patches/arith_2.8.3.hg)

(patch re-opened due to Michael's suggestion)


---

Comment by was created at 2007-08-31 22:06:13

Resolution: fixed


---

Comment by was created at 2007-08-31 22:07:00

Resolution changed from fixed to 


---

Comment by was created at 2007-08-31 22:07:00

Changing status from closed to reopened.


---

Comment by boothby created at 2007-08-31 22:45:13

Resolution: fixed


---

Comment by boothby created at 2007-08-31 22:45:13

Everything seems to check out.  Almost all element classes are now using the generic code, and all tests pass.  The classes which do not use generic code are listed in #503, or have good reason not to use it (for example, integers call mpz library code).
