# Issue 3971: [with patch; needs review] hidden markov models -- implement nsteps and log_likelihood_cutoff

Issue created by migration from https://trac.sagemath.org/ticket/3971

Original creator: was

Original creation time: 2008-08-27 23:37:19

Assignee: cwitty

I forgot to implement the nsteps and log_likelihood_cuttoff parameters for discrete hidden markov models, despite documenting them as implemented. The attached short patch fixes this oversight. 


---

Attachment


---

Comment by jkantor created at 2008-08-28 06:11:09

This looks good to me. No real comments but positive review


---

Comment by mabshoff created at 2008-08-28 12:00:19

Merged in Sage 3.1.2.alpha2


---

Comment by mabshoff created at 2008-08-28 12:00:19

Resolution: fixed
