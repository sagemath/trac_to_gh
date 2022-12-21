# Issue 8249: sagenb: notebook cookies

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-02-12 12:12:00

Assignee: was

CC:  acleone mpatel mhampton

This is a followup to #6353.   That ticket improved cookie naming a bit.  However, it appears to be not enough.  


```
On Thu, Feb 11, 2010 at 7:21 PM, Marshall Hampton <> wrote:
> Just for the record, this has happened to me quite a bit recently.
>
> I use a lot of different sage servers, often running different
> versions, so I don't usually report this kind of stuff since I think I
> am something of an extreme case.  But most of the servers I use are
> now running 4.3.2 and I am pretty sure I have seen the cookie message
> more than before.
>

Here's the relevant ticket I was remembering:

     http://trac.sagemath.org/sage_trac/ticket/6353

It is definitely in sage-4.3.2 (since it is merged into sagenb-0.7.4).   

Looking at that patch show that:

  (1) it addresses a related issue,

  (2) it might not solve the issue we're discussing, since it merely includes the *port* in the cookie name -- some unique id for the notebook (e.g., the URL or something else) is maybe also needed to fix the problem we're discussing.

So somebody should look at ticket 6353, see if a small modification of it would give a real fix, and make said modification.      Alex Leone: this would be a good project for you, if you're looking for something to do on the notebook. 

 -- William
```



---

Comment by acleone created at 2010-02-12 21:00:43

I couldn't reproduce his by signing in/out of sagenb.org and demo.sagenb.org.  Cookies are stored by domain (sagenb.org and demo.sagenb.org are two seperate sites), so differentiating by port should be all that's necessary.

I made sure all instances of 'cookie' in twist.py were updated from #6353 (they were), so I really have no idea what is causing this.  It could be a subtle bug in the 'cookie_test' cookie.


---

Comment by mpatel created at 2010-02-14 03:56:48

Has anyone been able to reproduce the problem reliably?  It would help greatly to have specific instructions.


---

Comment by mpatel created at 2010-02-14 04:38:25

Expire cookies on logout.  sagenb repo.


---

Attachment

I've attached a patch that should delete both the test and notebook session cookies, when a user logs out.


---

Comment by mpatel created at 2010-02-14 04:44:46

The patch may depend weakly on #6069.


---

Comment by mpatel created at 2010-02-14 04:51:22

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-02-14 04:51:22

Changing priority from minor to major.


---

Comment by acleone created at 2010-02-14 06:05:44

LGTM: I can't produce any cookie errors through normal use.

However, selenium errors when logging out - I'm working on a new patch to fix the tests.  (See attached for log)


---

Comment by acleone created at 2010-02-14 06:05:44

Changing status from needs_review to needs_work.


---

Comment by acleone created at 2010-02-14 06:07:08

Selenium errors with patch.  Same errors when the patch for #6069 -missing_pub_ws.3 is applied.


---

Attachment

Thanks for catching the Se test errors.  I should have checked.

The patch fixes for me the one cookie-related problem I could reproduce reliably:  Logging out in Chrom* displays a browser error page:


```
This webpage has a redirect loop.

The webpage at http://localhost:8000/home/admin/ has resulted in too many redirects. Clearing your cookies for this site or allowing third-party cookies may fix the problem. If not, it is possibly a server configuration issue and not a problem with your computer.
```

But with the patch, clicking on "Sign Out" just returns me to the login page.  I'm not sure if it helps with the reported problems, but making the cookies expire on logout seems logical.


---

Comment by acleone created at 2010-02-15 04:57:55

For some reason Selenium doesn't like HTTP redirect responses.  I keep getting this 'Problem loading page' error (in firefox):

```
The page isn't redirecting properly
      
Firefox has detected that the server is redirecting the request for this address in a way that will never complete.

    *   This problem can sometimes be caused by disabling or refusing to accept
          cookies.
```


This always happens when the selenium gets the redirect HTTP response.  Perhaps we should change it back to a dedicated logout page, but add a `<meta http-equiv="Refresh"` tag so the page redirects after a second.


---

Comment by mpatel created at 2010-02-15 07:36:09

Adjust `close_callback` to make Se tests pass.  Apply only this patch.


---

Attachment

V2 replaces `'/'` with `'/home/' + user_name` in `notebook_lib.js`'s `close_callback`.  Strangely, this seems to work.


---

Comment by mpatel created at 2010-02-16 02:01:56

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2010-03-19 08:21:12

I'm signing this off since it's a good idea, and may help. I'm unable to replicate the cookie issue though, with or without this patch, but it may be related to the performance issues of the sagenb server.


---

Comment by timdumol created at 2010-03-19 08:21:24

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-03-19 08:21:44

Woops. Forgot to add Alex.


---

Comment by timdumol created at 2010-05-04 04:44:35

Resolution: fixed
