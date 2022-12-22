# Issue 9707: Add a "signless" option to laplacian

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-08-08 00:40:24

Assignee: jason, ncohen, rlm

CC:  ncohen rlm dcoudert

We should have an option to g.laplacian() to return the signless Laplacian, which is attracting attention these days, and which is calculated by `D+A` instead of `D-A` (see p. 12 of http://www.doiserbia.nb.rs/ft.aspx?id=0350-13020795011C, for example).

Thanks to Steve Butler for the feature request.


---

Comment by @rajat1433 created at 2019-03-12 18:45:35

Signless laplacian is indeed gaining popularity as evident in the papers below.
So can I add the option to the current Laplacian Matrix method to return signless laplacian matrix?

https://arxiv.org/pdf/1803.06135.pdf

http://elib.mi.sanu.ac.rs/files/journals/publ/101/n095p011.pdf

https://ac.els-cdn.com/S0024379507000316/1-s2.0-S0024379507000316-main.pdf?_tid=59a3915e-dd7a-4dea-87a7-1892bc82cdca&acdnat=1552416165_1a56db5226e8357d8b7c9879a5dc3973


---

Comment by dcoudert created at 2019-03-13 10:19:03

A quick search effectively returns a significant number of recent publications.


---

Comment by @rajat1433 created at 2019-03-13 14:25:00

Changing assignee from jason, ncohen, rlm to @rajat1433.


---

Comment by git created at 2019-03-13 15:06:16

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by @rajat1433 created at 2019-03-13 15:07:27

Changing status from new to needs_review.


---

Comment by @rajat1433 created at 2019-03-13 15:07:57

Do i need to include this ticket number somewhere in the code?


---

Comment by dcoudert created at 2019-03-13 17:13:24

Changing status from needs_review to positive_review.


---

Comment by dcoudert created at 2019-03-13 17:13:24

We usually add ticket number when we fix a bug. So it's not needed here.

LGTM.


---

Comment by vbraun created at 2019-03-14 18:14:03

Resolution: fixed
