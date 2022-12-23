# Issue 7804: Move mipCoin and mipGlpk to Sage

Issue created by migration from https://trac.sagemath.org/ticket/7804

Original creator: ncohen

Original creation time: 2010-01-01 13:36:52

Assignee: AlexGhitza

CC:  mvngu

Hello !!

This patches moves the files mipCoin and mipGlpk to Sage. They are currently included in the packages CBC and GLPK and are a lot harder to work on because of this.

This patch copies them in sage/numerical/ and adds several lines to modules_list so that they will only be compiled if the corresponding packages are installed.

For the moment, the copies of these files included in the packages will not be removed, in order to preserve backward-compatibility : the users of earlier versions of Sage will then be able to keep using the same packages. 

*Only the changes to file modules_list need to be reviewed -- mipCoin and mipGLPK are copies of what is included in the spkg and have already been checked ! This should be a short review :-) *


---

Comment by ncohen created at 2010-01-01 13:41:29

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-01-01 13:44:00

Changing component from algebra to numerical.


---

Comment by was created at 2010-01-04 17:36:07

I was curious and skimmed this patch for ~ 3 minutes and it "looks good" (not a positive review -- I didn't test it yet).


---

Attachment

I just modified it so that it is now independent from the huge changes going on in graph.py. Would it be possible to have this merged to the next release ? It would let me write another speed-up patch now that solve_glpk and solve_cbc are available ;-)

Nathann


---

Comment by rlm created at 2010-01-13 11:37:45

Resolution: fixed


---

Comment by rlm created at 2010-01-13 11:37:45

positive review


---

Comment by ncohen created at 2010-01-13 11:40:19

Yessssssssssss !! :-) Thanks !!!!

Nathann


---

Comment by jhpalmieri created at 2010-01-13 22:56:54

How did this get a positive review when the new pyx files have no doctests?


---

Comment by rlm created at 2010-01-13 23:15:17

That's a good point-- I suppose my review was a bit rushed.

Nathann,

Do you want to make a separate ticket for making some doctests here, or would you prefer it if I just pull the patch back out?


---

Comment by ncohen created at 2010-01-14 06:13:59

see #7925 :-)

But they will be way harder to write with the spkg GLPK and cbc broken :-/

Nathann
