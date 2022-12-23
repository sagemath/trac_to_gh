# Issue 7014: Add a chat service to the notebook

Issue created by migration from https://trac.sagemath.org/ticket/7014

Original creator: mpatel

Original creation time: 2009-09-25 13:49:12

Assignee: boothby

Features:

 * Visit [#sage-devel](http://webchat.freenode.net/?channels=sage-devel), say, from a worksheet.
 * Create, join, and send invites to ad hoc [private] chatrooms managed by a notebook server.

A prime candidate is [qwebirc](http://qwebirc.org/).  Apparently, this is the backend for [Freenode's](http://freenode.net/) own [webchat client](http://webchat.freenode.net/).


---

Comment by mpatel created at 2009-09-28 18:25:04

There's a jsMath-enabled [qwebirc](http://qwebirc.org/) at

 * http://sage.math.washington.edu/home/mpatel/projects/sagenet

To test the server, unpack the archive, run `run.py`, visit

 * http://sage.math.washington.edu:9090/?channels=sage-devel

join the channel, and enter `$\alpha$`, say.


---

Comment by kedlaya created at 2016-08-16 19:34:33

Triaging moribund tickets here...

Now that SageMathCloud provides a chat service, is this request still desirable? If not, this ticket should be closed.


---

Comment by boothby created at 2020-03-29 02:12:30

Resolution: invalid


---

Comment by boothby created at 2020-03-29 02:12:30

Closing deprecated notebook tickets
