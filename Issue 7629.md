# Issue 7629: Make it possible to restrict the domains of email addresses

Issue created by migration from https://trac.sagemath.org/ticket/7629

Original creator: jason

Original creation time: 2009-12-08 19:58:17

Assignee: was

CC:  ddrake chapoton

I'm setting up a campus server, and it would extremely useful if I could require valid email addresses and restrict email addresses to campus addresses.  This would allow anyone with a valid campus email address to create an account.

Note that for this to work, we also need to make it required to confirm email addresses before accounts are activated.


---

Comment by jason created at 2009-12-08 20:04:39

See #7630


---

Comment by timdumol created at 2010-01-19 09:07:24

Changing type from defect to enhancement.


---

Comment by mpatel created at 2010-01-28 06:27:28

Validate with extra regexp from notebook settings.  Depends on #8038.  sagenb repo.


---

Comment by mpatel created at 2010-01-28 06:28:57

Changing status from new to needs_review.


---

Attachment

The patch is from #8038's V3.


---

Comment by ddrake created at 2010-02-08 13:10:24

Changing status from needs_review to needs_work.


---

Comment by ddrake created at 2010-02-08 13:10:24

This needs a bit of work. 

First, is it possible to doctest this? Ultimately, the function is just doing a regex match, so we should be able to doctest it...but I don't exactly know how.

Second, I think `re.search` would be better than `re.match`; search finds the regex anywhere in the string, but match by default only looks at the beginning of the string (http://docs.python.org/library/re.html). We can use `re.search` and anyone who needs the regex to match at the beginning of the string can use `^`. I thought the patch was broken until I looked this up in the Python documentation, so others will definitely run into this.

Finally, it would be nice to distinguish between invalid email addresses and disallowed addresses. Invalid is something like "two..dots`@`foo.com"; disallowed is something that the server admin doesn't allow. I say this because I'm anticipating emails from people outside of campus saying "the server says my email isn't valid, but it is, really!" and then I'd have to explain. Ideally, I'd like something like "The server administrator has restricted the email addresses that can be used here, and yours is not allowed."

With doctests and `re.search`, I'll give this a positive review.


---

Comment by kcrisman created at 2014-12-10 20:47:18

https://github.com/sagemath/sagenb/issues/298


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Changing status from needs_work to needs_review.


---

Comment by dimpase created at 2020-08-25 09:26:12

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-08-31 08:12:43

Resolution: invalid
