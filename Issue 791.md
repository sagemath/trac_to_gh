# Issue 791: ugly absprec parameter in Polynomial constructor

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2007-10-02 18:38:47

Assignee: was

I'm not happy with the profusion of code to deal with the absprec parameter in Polynomial-related code (for example, search for the string "absprec" in sage/rings/polynomial/polynomial_element.pyx). Something feels wrong with this design; the code keeps splitting into branches to deal with "absprec" or "no absprec" cases. I believe the "absprec" parameter has something to do with polynomials over p-adics. There has to be a cleaner way to deal with this issue. Please add comments below.



---

Comment by mabshoff created at 2007-10-04 19:49:53

Changing assignee from was to somebody.


---

Comment by mabshoff created at 2007-10-04 19:49:53

Changing component from algebraic geometry to basic arithmetic.


---

Attachment


---

Comment by AlexGhitza created at 2009-01-27 06:04:19

rebase of previous patch against 3.3.alpha2


---

Attachment

Looks good.  I have rebased the patch against 3.3.alpha2, since it got entangled in the whole Sage Days 12 flurry of activity.


---

Comment by mabshoff created at 2009-01-28 12:59:11

Resolution: fixed


---

Comment by mabshoff created at 2009-01-28 12:59:11

Merged in Sage 3.3.alpha3
