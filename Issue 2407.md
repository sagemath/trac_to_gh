# Issue 2407: Notebook fails without explanation when cookies are disabled

Issue created by migration from https://trac.sagemath.org/ticket/2407

Original creator: rhinton

Original creation time: 2008-03-06 17:19:30

Assignee: boothby

This may be more of enhancement, but it would be nice to throw up an error message in the notebook if cookies are disabled in the browser.  

For example, I jumped on sagenb.org to try things out.  After logging in I started with nothing.  I clicked on "New Worksheet" to get started, and I get a "404 Not Found" error for the page /new_worksheet.  This seems an easy and natural place to tell the user they need to enable cookies in their browser.  Even better would be to check for the expected cookie in the "just logged in" page generation logic.

For completeness, most of the other links on the "just logged in" page just ask me to log in again.  (This is when I figured out the problem.  Originally I assumed the notebook must be broken.)  The "Upload" link gives me a corresponding 404 page, and "Log" and "Help" just open new, empty pages.  (Not particularly helpful when I tried it.)  I am using Firefox 2.0.0.12 on FreeBSD 6.3.


---

Attachment


---

Attachment


---

Attachment

Ticket has been rebased. Apply all 3 patches.


---

Comment by TimothyClemans created at 2008-09-29 20:50:51


```
13:43 < jason-> okay, after getting the error, I reenabled cookies, but I still
                get the error.
13:44 < tclemans> refresh the homepage?
13:44 < tclemans> *login page
13:44 < jason-> ah, works now.
13:45 < jason-> huh, so I disable cookies after logging in
13:45 < jason-> and get a "You are not logged in or do not have access to the
                worksheet '104'."
13:45 < jason-> not a cookie message
13:46 < tclemans> ok well I never meant to fix that issue basically on the
                  login page we set a test cookie and while login is being
                  processed we look for that cookie
13:46 < jason-> okay
13:46 < tclemans> and then that cookie is deleted after succesful login
```



---

Comment by jason created at 2008-09-29 20:53:54

I applied all three patches to 3.1.3alpha1 and verified that the intended error message pops up trying to log in without cookies enabled.  I looked at the code and it looks like it might be reasonable, but I am not familiar with this specific section of the code base, so I might have missed something.

Tentative positive review, in that I verified from the user's standpoint the bug is fixed.


---

Comment by mabshoff created at 2008-09-29 22:28:52

Jason, 

please stick with the agreed upon labels.

Cheers,

Michael


---

Comment by ddrake created at 2008-09-30 01:17:36

I'm with jason: I applied the three patches 3.1.3alpha1 and now get an error message when trying to log in with no cookies, but I don't know the Twisted code much and can't really comment on that. So consider this another positive user-experience review.


---

Comment by mhansen created at 2008-09-30 11:54:45

I think we can merge this.


---

Comment by mabshoff created at 2008-09-30 11:59:04

Resolution: fixed


---

Comment by mabshoff created at 2008-09-30 11:59:04

Merged all three patches in Sage 3.1.3.alpha2
