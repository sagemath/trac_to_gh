# Issue 7630: Require email confirmation before account activation

Issue created by migration from https://trac.sagemath.org/ticket/7630

Original creator: jason

Original creation time: 2009-12-08 20:04:21

Assignee: was

Right now it says in the Settings page "Require e-mail for account registration".  This implies to me that an account will not be activated until a valid email address is added.  Furthermore, when this is checked, a new account screen says: "Your email address is required for account confirmation and recovery. You will be emailed a confirmation link right after you successfully sign up."  This definitely implies that an account will not be activated until the user clicks on a link.

However, the account is activated, whether or not the user clicks on the link in the email.

If we're going through the trouble of making a link and confirming email addresses, it makes sense to follow the well-established practice of not letting the user log in until they confirm their email address.

It seems that this could be a very easy check in the login stage, too.  Just check to see if "require email address" is set, and if so, check to make sure the user's email address is confirmed.




---

Comment by ddrake created at 2010-02-08 12:05:32

Patch up, please review. Sorry for the whitespace noise in the patch, I have nuke-trailing-whitespace on in emacs.

Several issues I noticed while working on this:

  * The confirmation tokens are not saved across sessions, so if a user signs up, then you quit the notebook and restart, then the user clicks on the confirmation URL, the server says it doesn't know about that confirmation token. This may or may not be something we want to fix.
  * We should have a way of letting the admin user bypass the email confirmation, since email can get lost, etc. Perhaps another column in the suspend/reset user account page, so that the admin can just click to consider the email confirmed, or to bypass email confirmation for that user. Or, we might have a "resend confirmation email" feature. Perhaps we should have both.


---

Comment by ddrake created at 2010-02-08 12:05:32

Changing status from new to needs_review.


---

Comment by wdj created at 2010-02-08 12:26:07

Replying to [comment:1 ddrake]:
> Patch up, please review. Sorry for the whitespace noise in the patch, I have nuke-trailing-whitespace on in emacs.
> 

...

>   * We should have a way of letting the admin user bypass the email confirmation, since email can get lost, etc. 


I totally agree. IMHO this is not a good feature unless it can be turned off. I also am unclear how the email is to be sent out. 
Install a mail server too? (a) This is not allowed where I work, except on certain machines. (b) If I am using Sage on a local lan set up for a specific computer lab then I am not interested in wasting class time with confirmation emails. In my opinion, there should be something like accounts_with_confirmation=True to implement this and accounts = True does not. If the only option to setting up accounts once this patch is applied is to require email confirmation then I think this patch "needs work".

Hopefully I am just completely misunderstanding the entire purpose of this ticket.


---

Comment by ddrake created at 2010-02-08 13:16:59

Replying to [comment:2 wdj]:

> >   * We should have a way of letting the admin user bypass the email confirmation, since email can get lost, etc.  
> 
> I totally agree. IMHO this is not a good feature unless it can be turned off. I also am unclear how the email is to be sent out.

Twisted includes an SMTP server.

 (b) If I am using Sage on a local lan set up for a specific computer lab then I am not interested in wasting class time with confirmation emails. In my opinion, there should be something like accounts_with_confirmation=True to implement this and accounts = True does not.

As the admin user, go to Settings -> Notebook Settings -> Require email for account registration. You can tick the box to require it, or leave it unticked.

> Hopefully I am just completely misunderstanding the entire purpose of this ticket.

Right now, the notebook server has the option to require email confirmation before logging in -- but you can log in anyway, even before the email has been confirmed. That's the purpose of this ticket. No one will be forced to do anything with email registration / confirmation.


---

Comment by ddrake created at 2010-02-08 13:30:42

BTW, with this patch, if the admin user adds a user on the "Manage Users" page when "require email" is checked, that user cannot log in until his email is confirmed...and since there's no email associated to the user, it's spectacularly unlikely that the user will ever be able to login.

Also, I don't know how this will work with existing users who have never had their email addresses confirmed. For backwards compatibility, it would be nice if there was some kind of "has_logged_in_at_least_once" boolean that we could test; if the user has already logged in somehow, email confirmation gets bypassed.


---

Comment by ddrake created at 2010-02-24 03:51:39

attachment:trac_7630-with-debugging.patch is, I think, a working patch. It is still full of print statements that I used while working on this, and doesn't have any updated docstrings yet. But I think it works. It's against 4.3.2 (sagenb 0.7.4). 

In this setup, if the admin user adds a user, no email confirmation is ever required. Each regular user has a email_confirmation variable, which replaces the old email_confirmed boolean, and can be one of three states: not_required, pending, and confirmed. All users get not_required, except those that register themselves while email confirmation is turned on; they get 'pending'.

This patch is not ready for a "real" review yet, but please test and look over the code.


---

Comment by ddrake created at 2010-02-24 07:54:29

version 2 of patch, with lots of print statements


---

Attachment

Current version should pass doctests if you comment out the print statement in `add_user` in notebook.py (line 509).


---

Comment by ddrake created at 2010-03-06 08:08:16

In #8454, we are updating the docstring for `notebook()`, which uses an outdated call for `add_user`. Since this patch alters that function's parameters, we should also make sure to update the generic instructions for `notebook()` if necessary.


---

Comment by jason created at 2010-04-15 03:56:23

Is this really "needs review"?  The last few comments seem to indicate that it is still "needs work".


---

Comment by ddrake created at 2010-04-15 11:47:26

Replying to [comment:8 jason]:
> Is this really "needs review"?  The last few comments seem to indicate that it is still "needs work".

Well, there's lots of print statements throughout the code, and I decided to leave those in for reviewing purposes. When I was working on this, I found it very hard to follow the execution path, so I put in lots of "prints" -- it seems like a reviewer would also appreciate the help in seeing what's happening.

After the patch gets a good review, I can add a small remove-all-the-prints patch.

(Although I would like to see the notebook print more information; some kind of verbose logging option would be really useful.)


---

Comment by was created at 2010-04-24 23:53:02

Replying to [comment:9 ddrake]:
> Replying to [comment:8 jason]:
> > Is this really "needs review"?  The last few comments seem to indicate that it is still "needs work".
> 
> Well, there's lots of print statements throughout the code, and I decided to leave those in for reviewing purposes. When I was working on this, I found it very hard to follow the execution path, so I put in lots of "prints" -- it seems like a reviewer would also appreciate the help in seeing what's happening.
> 
> After the patch gets a good review, I can add a small remove-all-the-prints patch.

Please make all the print statements conditional, e.g., write a function

```
   def log_devel(s):
        if VERBOSE: print s
```

and call that function everywhere.    Then make a file-scope variable VERBOSE which is False in your patch.
Explain here (and in a comment) that by setting it to True, the reviewer can enable devel logging.  This'll get
used elsewhere too. 

 -- William


---

Comment by was created at 2010-04-24 23:53:02

Changing status from needs_review to needs_work.


---

Attachment

version 3 of patch. Apply only this.


---

Comment by ddrake created at 2010-04-26 07:42:51

Changing status from needs_work to needs_review.


---

Comment by ddrake created at 2010-04-26 07:42:51

Replying to [comment:10 was]:
> Please make all the print statements conditional, e.g., write a function
> {{{
>    def log_devel(s):
>         if VERBOSE: print s
> }}}
> and call that function everywhere.    Then make a file-scope variable VERBOSE which is False in your patch.
> Explain here (and in a comment) that by setting it to True, the reviewer can enable devel logging.  This'll get
> used elsewhere too. 

Okay, done. I've rebased the patch so it applies to sagenb 0.8.1 (see #8727).


---

Comment by jdemeyer created at 2012-07-27 20:42:54

Please fill in your real name as Author.


---

Comment by jdemeyer created at 2013-02-05 19:33:13

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-02-05 19:33:13

I think this should be closed since the notebook is now a separate project and in any case, there is work on a completely new frontend.


---

Comment by jdemeyer created at 2013-02-08 13:23:54

Resolution: invalid
