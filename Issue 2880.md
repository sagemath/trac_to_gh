# Issue 2880: Special code for elliptic curve cardinality for j=0 and j=1728

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-04-11 20:07:20

Assignee: was

When the new code for point counting on elliptic curves over arbitrary finite fields was implemented, I left handling the special cases j=0 and j=1728 for a rainy day.  These cases were handled in not too bad a way, but as there are special formulas for these cases it was always going to be a good idea to implement them.

Not having any reference which does everything needed here (especially for the really exceptional cases where the characteristic is 2 or 3 and j=0=1728) I worked it all out from scratch, and here is the result.

There are copious comments and doctests.  I will write up the full justification in due course.  In the meantime I hope we can merge this patch (based on 3.0.alpha1) quite soon!


---

Attachment


---

Comment by cremona created at 2008-04-11 20:10:03

Changing keywords from "" to "elliptic curves".


---

Attachment

replaces previous patch; applies to 3.0.alpha3


---

Comment by cremona created at 2008-04-11 21:18:20

The original patch was based on 3.0.alpha1 and did not apply to alpha3.  The new one does apply ok to alpha3.


---

Attachment

Apply after preceding main patch


---

Comment by cremona created at 2008-04-12 19:12:55

Two small changes to be applied after the main patch:

   * In abelian_group() when j=0 or 1728 call cardinality() first, now that it is very fast, as that speeds up the group computation

   * In abelian_group(), a small adjustment to speed up the linear_relation() finding for the second generator.


---

Comment by AlexGhitza created at 2008-04-13 15:11:19

Patches look good.


---

Comment by mabshoff created at 2008-04-13 16:03:31

Resolution: fixed


---

Comment by mabshoff created at 2008-04-13 16:03:31

Merged 9467.patch and 9468.patch in Sage 3.0.alpha5


---

Comment by cremona created at 2008-04-14 13:25:42

Replying to [comment:5 AlexGhitza]:
> Patches look good.
Thanks!  and sorry for the factor_integer() problem which these caused.  John
