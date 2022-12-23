# Issue 8687: Weak SSL certificates in notebooks

Issue created by migration from https://trac.sagemath.org/ticket/8687

Original creator: sneves

Original creation time: 2010-04-14 13:32:34

Assignee: jason, was

To generate the certificate required for secure (https) notebooks, openssl is called (in Linux, at least). By default, openssl generates 512bit RSA keys, which are far too weak to be used with any degree of confidence.

The offending code is in the sagenb module, in the run_notebook.py file, line 100. A simple fix is to change the line to:

  cmd = ['openssl genrsa 2048 > %s' % private_pem]


---

Comment by kcrisman created at 2014-12-10 21:07:14

Fixed (for some value of fixed, probably needs to be updated again) in [this long-ago commit](https://github.com/sagemath/sagenb/commit/3cbaaec1fc0362bb0acc40dcf7fe8d8172fad357).   See also https://github.com/sagemath/sagenb/pull/253


---

Comment by kcrisman created at 2014-12-10 21:07:14

Changing status from new to needs_review.


---

Comment by kcrisman created at 2014-12-10 21:07:19

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-12-11 18:35:43

Resolution: fixed
