# Issue 6353: change cookies structure to support multiple notebook logins at different ports

Issue created by migration from https://trac.sagemath.org/ticket/6353

Original creator: boothby

Original creation time: 2009-06-18 00:07:45

Assignee: boothby

CC:  boothby

At present, a user cannot log into two different notebooks at the same address with different ports.  For example, if I run two notebooks at

http://sage.math.washington.edu:8001

and

http://sage.math.washington.edu:8002

then I can only use one at a time unless I use two separate browsers.  A simple change to the cookies should fix this.


---

Attachment

Appends port number to the cookie names.


---

Comment by timdumol created at 2010-01-19 11:07:18

Changing status from new to needs_review.


---

Comment by timdumol created at 2010-01-19 11:07:18

This should do the trick.


---

Comment by mpatel created at 2010-01-20 03:33:43

Nice excuse to try out [Firecookie](https://addons.mozilla.org/en-US/firefox/addon/6683).


---

Comment by mpatel created at 2010-01-20 03:33:43

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-01-25 00:52:38

Resolution: fixed
