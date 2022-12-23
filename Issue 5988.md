# Issue 5988: notebook feature request -- make it so non-logged in users are redirected to login page

Issue created by migration from https://trac.sagemath.org/ticket/5988

Original creator: was

Original creation time: 2009-05-05 14:22:58

Assignee: boothby

CC:  timdumol

I strongly agree with the following feature request.  I have wanted the same feature myself.


```
If the sage notebook server is restarted while a logged in user is
viewing a notebook page, a user attempt to refresh the page results in
a completely blank page titled "Error | Sage Notebook".  The user must
manually edit the URL to go back to the main server page and login
again, presumably because the login credentials have been lost with
the server reboot.

But, it may not be obvious to all users what they need to do to
recover from this situation.  Is there some twisted option I can set
to either redirect the browser back to the login page, or to add
explanatory text to the blank page with a link to the login page?  If
neither of these options is currently possible, I'd like to make a
feature request to enhance the server response to an attempt to access
a page when a user is apparently not logged in, to provide the user
with a useful page, rather than a completely blank page.

I'm running sage 3.4.2.

Thanks,
--
Kevin Horton
Ottawa, Canada

```



---

Comment by mabshoff created at 2009-05-18 13:19:23

See also #6069.

Cheers,

Michael


---

Comment by mpatel created at 2010-01-25 15:06:36

I think this is no longer a problem, at least with SageNB 0.7 (#8051) and maybe even with SageNB 0.6.  If I try to reload the home page or an opened worksheet, I get redirected to the login page or to a page with a message, e.g.,

  You are not logged in or do not have access to the worksheet 'XXX'. Continue

Clicking "Continue" takes me to the login page.  But clicking on "Log," "Settings," or "Help" returns `404 Not Found`, instead of redirecting to the login page.


---

Comment by mpatel created at 2010-01-25 16:38:28

Actually, this may still be a problem in WebKit browsers.


---

Comment by kcrisman created at 2014-12-10 18:57:25

I cannot replicate this in Safari, Chrome, or FF on Mac.  The "searching for Sage server" takes care of most instances, and I don't see the page mentioned above.  Presumably the flask transition?


---

Comment by kcrisman created at 2014-12-10 18:57:25

Changing status from new to needs_review.


---

Comment by kcrisman created at 2014-12-10 18:57:31

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-12-11 18:37:04

Resolution: worksforme
