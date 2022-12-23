# Issue 9283: sage notebook error when opening default page

Issue created by migration from https://trac.sagemath.org/ticket/9283

Original creator: retry

Original creation time: 2010-06-20 13:06:39

Assignee: jason, was

CC:  chapoton

When I start sage notebook and it start the default page with link: http://localhost:8000/?startup_token=bc78dfa581c408ffb65ce4d556960690, i get error:

2010-06-20 !16:02:21+0300 [HTTPChannel,1,127.0.0.1] /opt/sagemath/local/lib/python2.6/site-packages/twisted/internet/!defer.py:262: exceptions.DeprecationWarning: Don't pass strings (like 'Bad token') to failure.Failure (replacing with a DefaultException).



2010-06-20 !16:00:21+0300 [HTTPChannel,1,127.0.0.1] Exception rendering:

2010-06-20 !16:00:21+0300 [HTTPChannel,1,127.0.0.1] Unhandled Error        Traceback (most recent call last):        Failure: twisted.python.failure.DefaultException: Bad tokenMy browser opens up with with text:

# Internal Server Error
An error occurred rendering the requested  page. More information is available in the server log.

If i delete the startup token part, everything works correctly.


---

Attachment

full notebook log.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Changing status from new to needs_review.


---

Comment by dimpase created at 2020-08-22 08:18:36

Changing status from needs_review to positive_review.


---

Comment by dimpase created at 2020-08-22 08:18:36

yep.


---

Comment by chapoton created at 2020-08-22 08:43:53

Resolution: invalid
