# Issue 2606: command line option to kill a background notebook

Issue created by migration from Trac.

Original creator: nbruin

Original creation time: 2008-03-19 22:06:09

Assignee: boothby

Since running sage -notebook now checks if another instance is already running, it would be fairly straightforward to create an option that kills that notebook process as well.

The rationale is that it is probably much easier for a user to recreate the circumstances under which the notebook was started, and hence enable sage to find the relevant PID file, than to figure out where that PID file is stored.

Given the code in sage.server.notebook.run_notebook it can be rather involved to track down where twistd.pid gets stored (and it might change in the future too), being able to get a hold of the pidfile in a general way would make startup scripts much more robust (the location of twistd.pid has already changed once)

As an example, daemon-like services such as vncserver and dhclient have "-kill" and "-r" options to kill previously started instances in a way that takes the burden from the user to figure out which PID to kill.

One should probably first address

http://trac.sagemath.org/sage_trac/ticket/2359


---

Comment by was created at 2008-03-19 22:49:37

Can you suggest a very specific design?  E.g.,

```
sage: notebook.killall()
... kills all running notebook servers
sage: notebook.pids()
... shows pids' of all running notebook servers
sage: notebook.urls()
... shows urls...
```


What do you think?


---

Comment by boothby created at 2020-03-29 02:12:30

Resolution: invalid


---

Comment by boothby created at 2020-03-29 02:12:30

Closing deprecated notebook tickets
