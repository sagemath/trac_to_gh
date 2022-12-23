# Issue 7011: fiddle with the number of threads automatically used for parallel testing

Issue created by migration from https://trac.sagemath.org/ticket/7011

Original creator: ddrake

Original creation time: 2009-09-25 07:39:05

Assignee: tbd

CC:  mvngu drkirkby jhpalmieri

At #6283, we changed the parallel testing framework so that it automatically uses all the cores/threads available, but perhaps this is not the best solution.

Dave says ([comment:9:ticket:6283]) "I would have personally not allowed the default to exceed 8", so maybe we can incorporate his limit in a way that still lets ordinary multicore computers be well-used:

  * NUM_THREADS defaults to 0, which is now interpreted in the sage-ptest script as min(cpu_count(), 8) -- so the default doesn't exceed 8, as Dave suggested.
  * if NUM_THREADS is -1, it just uses cpu_count().

On sage-devel, I suggested that a solution that works really well for 99+% of people is a good one -- and since most "regular" machines on which Sage is doctested have 8 or fewer cores, this still works fine for them, and with the above suggestion, people won't bring sage.math or t2.math to their knees.

Thoughts?


---

Comment by ddrake created at 2009-09-25 08:18:45

On second thought, scratch the -1 idea. We can just make one change to sage-ptest: line 267 could be

```
numthreads = min(8, multiprocessing.cpu_count())
```

Anyone who is desperate to saturate a machine with more than 8 cores can just specify it on the command line.


---

Comment by ddrake created at 2009-09-29 08:22:13

add in default maximum of 8 threads


---

Attachment

patch for $SAGE_ROOT/makefile


---

Comment by ddrake created at 2009-09-29 08:36:53

Changing status from new to assigned.


---

Comment by ddrake created at 2009-09-29 08:36:53

Changing assignee from tbd to ddrake.


---

Attachment

I've uploaded patches for the sage_scripts repo, and for the root makefile. The second attachment is an ordinary unified diff.


---

Comment by jhpalmieri created at 2009-09-30 20:12:01

Looks good to me. Very helpful comments, too.


---

Comment by was created at 2009-10-14 01:27:29

Resolution: fixed


---

Comment by was created at 2009-10-14 01:27:29

merged into sage-4.1.2
