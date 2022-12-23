# Issue 4428: [with patch, needs review] Forgot to close open files in sage/rings/number_field/totallyreal_phc.py

Issue created by migration from https://trac.sagemath.org/ticket/4428

Original creator: craigcitro

Original creation time: 2008-11-02 22:35:53

Assignee: craigcitro

I forgot to close the file handles opened by `popen2` in my fix for #4386. The attached patch cleans this up.


---

Attachment

Looks good to me. Nice catch, sorry I did not catch it during the review of the previous ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-04 21:33:49

Merged in Sage 3.2.alpha3


---

Comment by mabshoff created at 2008-11-04 21:33:49

Resolution: fixed
