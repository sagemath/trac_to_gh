# Issue 2803: notebook -- the confirmation email after creating a new account is marked as spam

Issue created by migration from https://trac.sagemath.org/ticket/2803

Original creator: was

Original creation time: 2008-04-05 02:23:27

Assignee: boothby


```
----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA1

Professor Stein:
After registering for the sage notebook, I noticed that my confirmation
email was tagged as spam. looking at the headers I saw
math.sage.washington.edu (more accurately its IP 128.208.160.191) was
blacklisted by XBL:
http://www.spamhaus.org/xbl/
Checking XBL, I found that the IP was included since it was included in
another blacklist, CBL:
http://cbl.abuseat.org/lookup.cgi?ip=128.208.160.191

CBL lists the server for non-RFC2821 compliant HELO host names. Checking
the header of the notebook registration confirmed this.

Received: from localhost.localdomain (sage.math.washington.edu
[128.208.160.191])
by mail.erkert.com with SMTP id 97F2E2CB077
for <>; Fri,  4 Apr 2008 04:37:23 -0700 (PDT)

To remove the server from the blacklists CBL&XBL, it should be a pretty
easy fix and is discussed for numerous MTAs on:
http://cbl.abuseat.org/namingproblems.html

- --Nick Erkert

```



---

Comment by timdumol created at 2009-11-15 17:21:42

Changing type from defect to task.


---

Comment by kcrisman created at 2013-06-14 20:31:07

Given that this IP is still relevant to Sage, but according to the link above:

```
IP Address 128.208.160.191 is not listed in the CBL.
```

I think we can close this.


---

Comment by kcrisman created at 2013-06-14 20:31:07

Changing status from new to needs_review.


---

Comment by kcrisman created at 2013-06-14 20:34:05

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2013-06-14 20:34:05

Neither is 128.208.160.198, sagenb.org, so I think we're set.


---

Comment by jdemeyer created at 2013-06-19 12:19:52

Changing component from notebook to website/wiki.


---

Comment by jdemeyer created at 2013-06-19 12:19:52

In any case, this is not a Sage ticket.


---

Comment by jdemeyer created at 2013-06-19 12:19:52

Resolution: invalid
