# Issue 2317: possible job starvation of dsage server

Issue created by migration from Trac.

Original creator: yi

Original creation time: 2008-02-26 17:42:21

Assignee: yi

Currently if a worker gets a job and never submits it back (either maliciously or because of a bug), the server will never know the difference. Hence someone could just ask for a bunch of jobs and never do them, which starves the server of jobs.

Proposed fixes:
1) Server pings the worker which has the job and asks for its status periodically, if the worker does not reply for some number of attempts, reinject the job into the queue.


---

Comment by was created at 2010-01-19 07:36:40

Dsage has been deprecated.


---

Comment by was created at 2010-01-19 07:36:40

Resolution: wontfix
