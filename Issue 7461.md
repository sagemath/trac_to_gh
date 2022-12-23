# Issue 7461: partition_refinement.pyx

Issue created by migration from https://trac.sagemath.org/ticket/7461

Original creator: was

Original creation time: 2009-11-14 18:38:48

Assignee: mhansen

I have witnessed this on many 32-bit linux machines:

```
[wstein@flavius sage-4.2.1.rc0]$ ./sage -t --long "devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx"
sage -t --long "devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx"

[[times out after 1800 seconds]]

^CKeyboardInterrupt -- interrupted after 1386.7687881 seconds!
         [1387.2 s]
 
```


Doing the same with --verbose dosn't necessarily time out. 


---

Comment by was created at 2009-11-14 18:39:03

Changing assignee from mhansen to rlm.


---

Comment by rlm created at 2009-11-14 19:20:40

Changing status from new to needs_info.


---

Comment by rlm created at 2009-11-14 19:20:40

Is this consistently reproducible, or something you hit randomly?


---

Comment by was created at 2009-11-17 06:39:05

> Is this consistently reproducible, or something you hit randomly? 

It *always* happens on I think every single 32-bit Linux platform with non-verbose doctests.


---

Comment by rlm created at 2009-11-18 18:45:21

On my virtual machine, 32-bit Ubuntu with non-verbose doctests:

```
rlmill@rlm32ubu:~/sage-4.2.1-linux-Ubuntu_9.10-i686-Linux$ ./sage -t -long devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx
init.sage does not exist ... creating
sage -t -long "devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx"
	 [228.4 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 228.4 seconds
```

They passed three times in a row.

Any ideas where to try next?


---

Comment by rlm created at 2009-11-19 09:12:41

I think I am seeing this on centos32 on boxen. On this machine, the trouble is that the walltime is somehow severely messed up.


```
sage: walltime()
1256774719.748621
```


*Exactly* ten seconds later:


```
sage: walltime()
1256774720.2823999
```


The difference is only 0.533. At that rate, what is supposed to be a 180 second doctest would take 3,374 seconds.

I'm noticing other strange behavior here too. To debug, I had the code writing to a file. When I kill the doctest, I get my terminal back. But, in the other terminal which I am using to "tail" the file, I watch things continue to be written. Also, running the doctest for one minute, and sending a keyboard interrupt, gives the following:


```
wstein@centos53-32:/tmp/wstein/farm/sage-4.2.1$ ./sage -t -long devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx
sage -t -long "devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx"
KeyboardInterrupt -- interrupted after 3.99422097206 seconds!
	 [4.5 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long "devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx"
Total time for all tests: 4.5 seconds
```


Huh!?!


---

Comment by rlm created at 2009-11-28 06:42:28

Changing status from needs_info to needs_review.


---

Comment by rlm created at 2009-11-28 06:42:28

The agreed fix was to have the tests run for a certain number of cases, not for a certain time. This will also improve the valgrind testing when it is done, since it won't just time out after one test.

However, these are new estimates for the number of tests that should be run (in particular, in the `-long` case). The release manager should give an opinion on whether the long doctests are too long for any of the systems we regularly test on.

Also, I have fixed the doctests to ensure that they are truly random, so that all this testing might actually find something.


---

Attachment


---

Comment by mhansen created at 2009-12-01 04:51:27

Looks good to me.


---

Comment by mhansen created at 2009-12-01 04:51:27

Resolution: fixed
