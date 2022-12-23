# Issue 2821: get rid of anything "about this document" sections of any sage docs that say "send email to stein"

Issue created by migration from https://trac.sagemath.org/ticket/2821

Original creator: was

Original creation time: 2008-04-06 04:04:03

Assignee: tba

I'm tired of getting personal emails that are much better put on list.


---

Attachment

doc patch


---

Comment by AlexGhitza created at 2008-04-25 00:36:50

See the attached patch.


---

Comment by wdj created at 2008-04-25 03:41:55

Applies cleanly using hg_doc.apply and all the latex docs pass sage -t. Also, every change in the diff file looks reasonable. Looks like a good doc patch to me.


---

Comment by mabshoff created at 2008-04-25 04:14:23

Merged in Sage 3.0.1.alpha0


---

Comment by mabshoff created at 2008-04-25 04:14:23

Resolution: fixed
