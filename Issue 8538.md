# Issue 8538: Update mpi4py (MPI for Python) to the latest version (1.2.1)

Issue created by migration from https://trac.sagemath.org/ticket/8538

Original creator: drkirkby

Original creation time: 2010-03-15 00:12:38

Assignee: tbd

As reported before (#8522) Open MPI fails to build on Solaris. The version is old, so I opened a ticket for an update to Open MPI (#8537). William indicated that mpi4py depends on Open MPI, so I might as well update mpi4py too. 




---

Comment by maldun created at 2011-01-07 00:28:07

After updating openmpi (see #8537) mpi4py has to be updated.
The the spkg for the latest stable releas (v. 1.2.2) can be found under: http://code.google.com/p/spkg-upload/downloads/detail?name=mpi4py-1.2.2.spkg
There were no troubles with installation on linux ubuntu 10.04

Have Fun!


---

Comment by maldun created at 2011-01-07 00:28:07

Changing status from new to needs_review.


---

Comment by mhansen created at 2011-12-18 09:50:10

Looks good to me.  I've updated the website to include this.


---

Comment by mhansen created at 2011-12-18 09:50:10

Resolution: fixed
