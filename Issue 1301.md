# Issue 1301: nauty interface

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-11-28 17:36:17

Assignee: mhansen

Keywords: graphs

It would be handy to have an interface to nauty like the ones to other software not included with Sage.  We have much of the functionality built-in, but an interface to nauty would let us double-check answers and also may provide speed benefits to those who have nauty installed already.

Nauty: http://cs.anu.edu.au/~bdm/nauty/



---

Comment by jason created at 2007-11-28 19:39:32

From Robert Miller:


```
>>> We need some hooks to nauty.
> Not done: we have reimplemented instead. If I don't do it before Sage
> Days 7, I will do it there: create a (necessarily optional) spkg to
> include nauty, and give all the relevant functions the option to call
> nauty instead. I believe geng is part of nauty, so this would come
> along for the ride. This should definitely be a wishlist trac ticket.
```



---

Comment by rlm created at 2007-12-02 04:48:11

Changing assignee from mhansen to rlm.


---

Comment by rlm created at 2007-12-02 04:48:11

Changing status from new to assigned.


---

Comment by rlm created at 2007-12-17 15:11:50

Changing keywords from "graphs" to "".


---

Comment by rlm created at 2007-12-17 15:11:50

Changing component from combinatorics to graph theory.


---

Comment by mabshoff created at 2008-05-23 01:45:49

Resolution: fixed


---

Comment by mabshoff created at 2008-05-23 01:45:49

Jason Grout did provide a nauty optional spkg and interface a couple weeks ago.

Cheers,

Michael


---

Comment by jason created at 2008-05-23 02:03:41

For reference, see #2242
