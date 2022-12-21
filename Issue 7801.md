# Issue 7801: save_notebook is called twice on notebook shutdown

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-01-01 05:03:22

Assignee: was

See `run_notebook.py`'s `run_twisted`, which generates `DOT_SAGE/sagen_notebook.sagenb/twistedconf.tac`.

Mentioned [comment:ticket:7514:16 here].


---

Attachment

Fixed interrupt handler to stop the twisted server instead of in save_notebook


---

Comment by acleone created at 2010-01-19 01:42:14

What the problem was:
The signal handler would call save_notebook(), which would stop the twisted server.  There was a handler on the server shutdown, "reactor.addSystemEventTrigger('before', 'shutdown', save_notebook)", that would call save_notebook() again.

Changes:
Moved the code that stops the server into the signal handler, and removed the save_notebook call.


---

Comment by acleone created at 2010-01-19 01:42:14

Changing status from new to needs_review.


---

Comment by timdumol created at 2010-01-19 01:51:06

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-01-19 01:51:06

LGTM. Nice job.


---

Comment by timdumol created at 2010-01-19 03:33:52

Resolution: fixed
