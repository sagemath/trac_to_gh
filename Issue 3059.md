# Issue 3059: notebook -- rewrite notebook(...) function to *not* use SSL by default

Issue created by migration from https://trac.sagemath.org/ticket/3059

Original creator: was

Original creation time: 2008-04-30 00:13:03

Assignee: boothby




---

Attachment


---

Attachment

The two patches turn ssl off by default, make logins required by default no matter what, print a big warning in a worrisome case, use a token to automate the first login, and fill in the admin username if it is the only possible username.


---

Comment by robertwb created at 2008-04-30 00:50:17

This is mostly to accommodate Firefox 3, right? If two users are running on the same system is it possible to sniff localhost traffic (short of being root, in which case the notebook could be compromised anyways...)? If not, then it looks good (though I have yet to try it out) and if so, is this a risk we're willing to take? (Probably so.)


---

Comment by boothby created at 2008-04-30 01:05:02

AFAIK, it is impossible to sniff localhost without being root.  This is not necessarily the case in Windows.  We should get a security expert to weigh in on this issue.

First patch appears to be completely orthogonal to the issue -- it seems to globally replace SAGE with Sage.  Specifically, if the second patch is not given a positive review soon, please split the first into a new ticket to avoid bitrot.

Second patch appears fine (modulo the security discussion) but I haven't tested it and won't until  Wednesday or later.


---

Attachment


---

Comment by was created at 2008-04-30 04:32:14

Comments:

1. In UNIX (linux and OS X) one definitely cannot sniff localhost unless one's system is purposely seriously misconfigured.

2. Windows is not relevant at this point, since there is no native notebook server under windows.  

3. Boothby's comment that "First patch appears to be completely orthogonal to the issue -- it seems to globally replace SAGE with Sage." isn't right.  That patch (1) makes the case change, and (2) adds a template parameter.  Both patches need to be applied.

4. Timothy Clemans did thoroughly test out the patch and found no bugs particularly caused by the patch, according to his remarks on irc.


---

Comment by was created at 2008-04-30 04:34:24

I give sage-3059-doc.patch (the patch added by Timothy) a possitive review.


---

Comment by TimothyClemans created at 2008-04-30 04:36:10

Positive review. Tested on sage.math. I doctested twist.py and no errors. I tried various combinations including "secure=True, require_login=False".


---

Comment by mabshoff created at 2008-04-30 04:53:30

Merged all three patches in Sage 3.0.1.alpha1


---

Comment by mabshoff created at 2008-04-30 04:53:30

Resolution: fixed
