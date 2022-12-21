# Issue 7561: Replaces InfinitePolynomialRing in MixedIntegerLinearProgram by 'var'

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-11-30 17:40:24

Assignee: jkantor

InfinitePolynomialRing was responsible for some bugs and extreme slowness in the utilisation of MixedINtegerLinearProgram for LP containing more than 1000 variables.

By replacing this polynomial ring by 'var', this is settled and waaaaayyyy mroe efficient !!

This patch depends on #7270


---

Comment by ncohen created at 2009-12-01 08:34:52

Changing status from new to needs_review.


---

Comment by malb created at 2009-12-02 14:20:42

Patch looks good and indeed speeds up everything considerably for me. Some small issues:
 * id should not be used as a variable name
 * The documentation says `# Returns the optimal value of x[3]` but you are asking for y[2][9]
 * min/max should not be used as variable names


---

Comment by ncohen created at 2009-12-02 18:14:39

Hello !!! It seems there are no "id" anymore in the file, and I corrected the x[3]..

The min/max variables are only defined in some (short) functions where they appear natural enough... Do you think we should change the arguments of the add_constraint() function ? I understand why you do not like to see this and I was not aware of it before you mentionned it, but they seem mostly harmless and I have no idea of which keyword we could pick to replace them... If you have any idea, though.... :-)

Nathann


---

Comment by ncohen created at 2009-12-05 14:30:17

Still around ??? :-)

It would be good if this patch was merged into next release ! :-)


---

Comment by malb created at 2009-12-05 14:46:28

Replying to [comment:3 ncohen]:
> Hello !!! It seems there are no "id" anymore in the file, and I corrected the x[3]..

Hi, it seems you didn't upload your new patch.
 
> The min/max variables are only defined in some (short) functions where they appear natural enough... Do you think we should change the arguments of the add_constraint() function ? I understand why you do not like to see this and I was not aware of it before you mentionned it, but they seem mostly harmless and I have no idea of which keyword we could pick to replace them... If you have any idea, though.... :-)

How about `minimum` & `maximum`? I'll leave it to you to change it or to keep min/max.


---

Comment by ncohen created at 2009-12-05 14:51:04

I forgot to uploaded it and erased it since... I'll upload a new one in a few seconds ! :-)


---

Comment by ncohen created at 2009-12-05 14:57:47

Here it is ! I only corrected the x[3] and let the min/max be... The function in which they appear is very short, and longer version would mean updating manymany patches (currently under review) and having longer aliases when it does not hurt that much. ( though I understand how you felt about them, I did not realized it when I first used them ).

We will be able to change them later if needed anyway :-)

Nathann


---

Attachment

This should go into 4.3, it opens a whole new world for MIP problems.


---

Comment by malb created at 2009-12-05 14:59:46

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2009-12-05 15:02:46

Thankssssssssssssss :-)


---

Attachment


---

Comment by mhansen created at 2009-12-06 08:51:22

Resolution: fixed
