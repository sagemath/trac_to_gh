# Issue 3050: notebook -- add "remember me" checkbox

Issue created by migration from https://trac.sagemath.org/ticket/3050

Original creator: TimothyClemans

Original creation time: 2008-04-28 16:48:26

Assignee: TimothyClemans

Port the attached SVN patch from Knoboo to the Sage Notebook.


---

Comment by was created at 2008-04-29 16:20:36

The Knoboo people have this feature.  Timothy attached a patch that is relevant to their implementation, which might be of some use to whoever implements this for sage.


---

Comment by TimothyClemans created at 2008-04-29 20:06:36

I want to make it clear that this functionality is not in Knoboo currently. From Alex Clemesha, "We will get this into knoboo as soon as the "settings" functionality
starts to settle into knoboo, because, (as you would probably agree), this only thing missing with the patch would be a way for the Admin user to set the "expires time" (instead of hard-coded)."


---

Attachment


---

Comment by TimothyClemans created at 2008-05-17 15:42:55

Fixes #3155 also.


---

Comment by TimothyClemans created at 2008-05-17 15:46:24

Warning: Depends on #3213


---

Comment by was created at 2008-05-17 16:14:02

REVIEW:

 1. It would be nice if you added a comment about what is going on in the modifications to twist.py.

 2. I don't actually understand how to test that this patch is actually doing something!  Could you give me simple step-by-step instructions to test out a situation where the behavior of something is different whether or not remember me is checked?   Does this feature only do anything when there are multiple accounts?  I tried what I thought was the obvious test, and it seems like Remember Me just doesn't work.  We can figure this out at the cafe today.


---

Comment by mabshoff created at 2008-05-17 20:29:56

Resolution: fixed


---

Comment by mabshoff created at 2008-05-17 20:29:56

Merged all three patches in Sage 3.0.2.alpha1


---

Comment by was created at 2008-05-18 16:32:31

Hi,

I was just using Sage on my computer with this patch applied and having a lot of problems if I open and close my browser.  I get into a state where I absolutely can't login, etc.

I.e., this patch is definitely not ready for prime time.  It will break the notebook for a lot of people in confusing ways. 

We'll get it fixed though.


---

Comment by was created at 2008-05-18 16:32:31

Changing status from closed to reopened.


---

Comment by was created at 2008-05-18 16:32:31

Resolution changed from fixed to 


---

Comment by TimothyClemans created at 2008-05-19 03:35:48

new and includes sage-3050.patch and sage-3050_2.patch


---

Attachment

I changed the cookie name to the static name "nb_session" in both the render for UserToplevel and in the function get_our_cookie in guard.py. I don't know if doing this fixes the problem.


---

Comment by was created at 2008-05-19 03:45:28

The new patch works.


---

Comment by was created at 2008-05-19 05:35:55

The new patch still causes problems, where notebooks just "don't work".  This is very serious and would cause mass problems by users.


---

Comment by was created at 2008-05-19 05:41:14

Wait, I spoke too soon.  I was confused by another separate problem.


---

Comment by mabshoff created at 2008-05-19 06:07:52

Merged extcode-3050.patch and trac_3050-revised-sage-3050.patch in Sage 3.0.2.alpha1


---

Comment by mabshoff created at 2008-05-19 06:07:52

Resolution: fixed
