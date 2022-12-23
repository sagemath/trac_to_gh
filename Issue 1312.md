# Issue 1312: [graphs] find hamiltonian cycles and paths

Issue created by migration from https://trac.sagemath.org/ticket/1312

Original creator: jason

Original creation time: 2007-11-28 20:01:49

Assignee: mhansen

Keywords: graphs




---

Comment by rlm created at 2007-12-17 15:15:00

Changing assignee from mhansen to rlm.


---

Comment by rlm created at 2007-12-17 15:15:00

Changing component from combinatorics to graph theory.


---

Comment by rlm created at 2007-12-17 15:15:00

Changing keywords from "graphs" to "".


---

Comment by jason created at 2008-08-22 18:08:41

We should merge the code written at http://wiki.wstein.org/2008/480a/theprojects by  	
Michael Rutherford


---

Comment by mvngu created at 2009-05-21 10:05:05

Replying to [comment:3 jason]:
> We should merge the code written at http://wiki.wstein.org/2008/480a/theprojects by  	
> Michael Rutherford 
With Sage 3.4.2, I can't seem to (up)load Michael Rutherford's worksheet. Some investigation with the Linux command `file` shows that it's compressed using the RAR format. Can someone confirm this? If so, then can someone upload a Sage-friendly worksheet?


---

Comment by myurko created at 2009-07-11 21:45:23

Useable version of file


---

Attachment

Replying to [comment:4 mvngu]:
> Replying to [comment:3 jason]:
> > We should merge the code written at http://wiki.wstein.org/2008/480a/theprojects by  	
> > Michael Rutherford 
> With Sage 3.4.2, I can't seem to (up)load Michael Rutherford's worksheet. Some investigation with the Linux command `file` shows that it's compressed using the RAR format. Can someone confirm this? If so, then can someone upload a Sage-friendly worksheet?


---

Comment by myurko created at 2009-07-11 21:51:49

Replying to [comment:4 mvngu]:
> Replying to [comment:3 jason]:
> > We should merge the code written at http://wiki.wstein.org/2008/480a/theprojects by  	
> > Michael Rutherford 
> With Sage 3.4.2, I can't seem to (up)load Michael Rutherford's worksheet. Some investigation with the Linux command `file` shows that it's compressed using the RAR format. Can someone confirm this? If so, then can someone upload a Sage-friendly worksheet?

I've uploaded a usable version. It was in a rar archive.


---

Comment by chapoton created at 2018-04-27 19:45:37

Changing status from new to needs_review.


---

Comment by chapoton created at 2018-04-27 19:45:37

We do have methods

```
g.is_hamiltonian
g.hamiltonian_cycle
g.hamiltonian_path
```

So this ticket can now be closed.


---

Comment by vdelecroix created at 2018-05-01 12:32:36

Changing status from needs_review to positive_review.


---

Comment by vdelecroix created at 2018-05-18 17:16:26

closing positively reviewed duplicates


---

Comment by vdelecroix created at 2018-05-18 17:16:26

Resolution: wontfix
