# Issue 6369: the sage cleaner should kill all notebook servers if sage that spawned them is killed

Issue created by migration from https://trac.sagemath.org/ticket/6369

Original creator: was

Original creation time: 2009-06-20 15:34:43

Assignee: boothby

Try this:

1. `sage -notebook foo`
2. Find the pid of the sage -notebook process with `ps ax |grep "sage -notebook"`
3. Kill that process with `kill -9 [pid]`
4. The notebook server is still going.  And now the only way to kill it is with `ps ax |grep tracd` and start killing things until you hit the right one.

Since people, especially new sage users, often kill the notebook server by, e.g., clicking kill in a terminal or some other silly means, it would be much better if the sage-cleaner could at least step in and kill the notebook server, so it gets shut down cleanly (saving its state), and doesn't stop the notebook from running in the future (if it is always running, it can't run again), hence confusing users.

To do all this is probably as simple as calling one little register function in sage.misc.cleaner.


---

Comment by timdumol created at 2010-01-19 07:06:41

This seems to be fixed now. `kill [pid]` kills the notebook as well. SIG_KILL doesn't seem like it will allow sage-cleaner to kill the notebook since it will be killed immediately. Confirm and close?


---

Comment by kcrisman created at 2014-12-10 19:21:25

This definitely kills the process but also definitely keeps the server going!  (And a number of other processes as well.)


---

Comment by boothby created at 2020-03-29 02:13:09

Resolution: invalid


---

Comment by boothby created at 2020-03-29 02:13:09

Closing deprecated notebook tickets
