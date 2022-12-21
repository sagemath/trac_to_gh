# Issue 4244: [with patch, needs review] pynac interface enhancements, symbolic functions

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2008-10-04 20:36:40

Assignee: burcin

CC:  was mhansen

Keywords: pynac, symbolics

The patches attached contain various enhancements to the pynac interface:
 * variables.patch - adds a .variables() method to sage.symbolic.expression.Expression
 * custom_eval_func.patch - allows the user to set custom python functions to perform evaluation, numeric evaluation, derivation, series expansion etc. on the given function (sage.symbolic.function.SFunction).

Changes in custom_eval_func.patch depend on the package at #4243, which in turn depends on #3872.


---

Attachment

add .variables() function to sage.symbolic.expression.Expression


---

Attachment

allow sage.symbolic.function.SFunction to use custom python function for evalution, series expansion, derivation, etc.


---

Comment by burcin created at 2008-10-15 09:10:53

fix some problems with modular coefficients


---

Attachment

Note that you need the package at #4243 to try these patches.


---

Comment by mhansen created at 2008-10-18 09:36:27

I went over this with Burcin at SD10.  Positive review.


---

Comment by mabshoff created at 2008-10-18 13:05:28

Resolution: fixed


---

Comment by mabshoff created at 2008-10-18 13:05:28

Merged all three patches in Sage 3.2.alpha0
