# Issue 7158: SageNB -- Set up challenge-response, such as a CAPTCHA, for account registration

Issue created by migration from https://trac.sagemath.org/ticket/7158

Original creator: mpatel

Original creation time: 2009-10-08 17:07:10

Assignee: boothby

CC:  timdumol was

Keywords: sagenb captcha

See

 * [CAPTCHA](http://en.wikipedia.org/wiki/CAPTCHA)
 * [reCAPTCHA](http://recaptcha.net/)

for descriptions and examples.


---

Attachment

Add challenge-response to notebook registration page. Depends on #7110.


---

Comment by mpatel created at 2009-10-08 17:38:18

Changing status from new to needs_review.


---

Comment by mpatel created at 2009-10-08 17:38:18

The attached patch, which depends "somewhat" (`twist.py`) on #7110, adds two challenge-response methods for new user registration:

 * Simple question and answer, e.g., "How many bits are in one byte?"
 * [reCAPTCHA](http://recaptcha.net/).

The code for both is in the new file `sagenb.notebook.challenge.py`.  I've also

 * Rewritten `twist.RegistrationPage` for linearity.
 * Modified `registration.html` and added the template `recaptcha.html`.
 * Added several options to `sagenb.notebook.server_conf.defaults`:

```python
defaults = {
             [...]
             'email': True,
             'challenge': True,
             'challenge_type': 'simple',
#             'challenge_type': 'recaptcha',
             'recaptcha_public_key': '',
             'recaptcha_private_key': '',
            }
```


One way to test the "simple" challenge, after applying the patch:

 * Backup `~/.sage`
 * Delete `~/.sage`
 * `sage`
 * `sage: import sagenb.notebook.notebook_object as n; n.notebook(accounts=True)`
 * Enter admin's password twice.
 * Browse to `http://localhost:8000`
 * Log out, if necessary, and click on "Sign up for a new Sage Notebook account".
 * Try to sign up for new accounts.

To test the "recaptcha" challenge, [sign up](http://recaptcha.net/whyrecaptcha.html) for a [reCAPTCHA](http://recaptcha.net/) key, update `server_conf.py`, and follow the steps above.


---

Comment by mpatel created at 2009-10-08 17:47:29

To do

 * Add the new `challenge` module to the reference manual.


---

Comment by mpatel created at 2009-10-12 18:40:04

Reminder: Rebase against the outcome of #7196.


---

Comment by mpatel created at 2009-10-14 08:45:41

Rebased for #7196.  Added regexp test for simple challenge.  Apply only this patch.


---

Attachment

Patch v2:

 * Uses regular expressions to verify "simple" challenge responses.
 * Rebased against #7196.

As before, please edit `sagenb.notebook.server_conf.py` to set up and enable the new feature.


---

Comment by mpatel created at 2009-10-14 11:52:38

Reminder: Fix doctests, e.g.,

```
sage: tmp = tmp_dir() 
sage: import sagenb.notebook.notebook as n 
sage: nb = n.Notebook(tmp) 
```

broken by the new `.sagenb` directory name requirement(?).


---

Attachment

apply this *after* applying trac_7158-captcha_v2.patch; it just makes a few minor changes I made during refereeing


---

Comment by was created at 2009-10-17 06:01:18

I refereed this.  All of it completely works precisely as advertised.  I fixed all the doctests as mentioned above in the "broken by the new .sagenb directory name" remark.  I also made the default dumb questions dumber, so as not to discourage new users by default.   In my experience any measure at all is enough to prevent spammers, but one will definitely use real reCaptcha (which is easy to setup and works well) in any serious setting.   Very nice!  I love how this patch really provides a solid mature feature to the notebook.  

It's critically important that usage of this is documented and that we make a notebook server settings page that can configure all this stuff.  I had no clue how to configure these things, except for the very helpful directions on this trac ticket (which were excellent). 

This is merged into sagenb-0.3.2 as part of sage-4.2


---

Comment by was created at 2009-10-17 06:01:18

Resolution: fixed
