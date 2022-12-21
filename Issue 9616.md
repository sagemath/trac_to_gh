# Issue 9616: segfault / NFS problems with parallel/decorate.py

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2010-07-28 02:51:53

Assignee: mvngu

CC:  leif jhpalmieri kcrisman malb mvngu simonking was

Keywords: fork nfs segfault

In 4.5.2.alpha1, we have for many people:

```
sage -t -long "devel/sage/sage/parallel/decorate.py"        


------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occurred in Sage.
This probably occurred because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
------------------------------------------------------------

**********************************************************************
File "/mnt/usb1/scratch/drake/release/tmp/sage-4.5.2.alpha1/devel/sage/sage/parallel/decorate.py", line 300:
    sage: g()
Expected:
    '10'
Got:
    [Errno 16] Device or resource busy: '/home/drake/.sage/temp/sage.math.washington.edu/30336/dir_0/.nfs0000000000591f8700069d5c'
    '10'
**********************************************************************
File "/mnt/usb1/scratch/drake/release/tmp/sage-4.5.2.alpha1/devel/sage/sage/parallel/decorate.py", line 311:
    sage: g()
Expected:
    'a'
Got:
    [Errno 16] Device or resource busy: '/home/drake/.sage/temp/sage.math.washington.edu/30336/dir_1/.nfs0000000000591f8d00069d5d'
    'a'
**********************************************************************
```

and so on. See https://groups.google.com/group/sage-release/msg/88b030aa31926459 and that thread.

This seems related to #9501.


---

Comment by mpatel created at 2010-07-28 05:35:49

For what they're worth, tests on sage.math with variations on

```sh
#!/bin/bash                                                                     

# This does not keep overall statistics:                                        
# env SAGE_TEST_GLOBAL_ITER=100 ./sage -tp 1 -long /path/to/file.py                     

SAGE_TEST="./sage -t -long"
#SAGE_TEST="env DOT_SAGE=/dev/shm/$USER/.sage $SAGE_TEST"                       
#SAGE_TEST="env DOT_SAGE=/scratch/$USER/.sage $SAGE_TEST"                       
RUNS=100
for I in `seq 1 $RUNS`;
do
    $SAGE_TEST devel/sage/sage/parallel/decorate.py
    CODE[$I]=$?

    echo "Results after $I of $RUNS runs:"
    echo "${CODE[*]}" | tr ' ' '\n' | sort -n | uniq -c
done
```

end with

```
Results after 100 of 100 runs:                                          
     1 0                                                                      
    99 128                                                                    
Results after 100 of 100 runs:                                       
   100 0                                                                      
Results after 100 of 100 runs:                                       
   100 0                                                                      
```

for the default DOT_SAGE, `/scratch/$USER/.sage`, and `/dev/shm/$USER/.sage`, respectively.


---

Comment by mpatel created at 2010-07-28 05:48:52

For now, should we tag the relevant tests with `# not tested` or [backout the whole patch](https://groups.google.com/group/sage-release/browse_thread/thread/9455213e89f94692/5aba6862d5c35b8c#5aba6862d5c35b8c)?  Other options?


---

Comment by mpatel created at 2010-07-28 05:53:01

By the way, here are the latest doctesting exist codes (cf. #9243), from the top of `sage-doctest`:

```
# Return value in process exit code:
# 0: all tests passed
# 1: file not found
# 2: KeyboardInterrupt
# 4: doctest process was terminated by a signal
# 8: the doctesting framework raised an exception
# 16: script called with bad options
# 32: (used internally in sage-ptest)
# 64: time out
# 128: failed doctests
```



---

Comment by leif created at 2010-07-28 13:23:19

According to William on sage-release, the segfault is an intentional part of a doctest, so I've changed the ticket's title.


---

Comment by leif created at 2010-07-28 13:23:19

Changing keywords from "fork nfs segfault" to "fork nfs device resource busy".


---

Comment by jhpalmieri created at 2010-07-28 14:42:08

Replying to [comment:2 mpatel]:
> For now, should we tag the relevant tests with `# not tested` or [backout the whole patch](https://groups.google.com/group/sage-release/browse_thread/thread/9455213e89f94692/5aba6862d5c35b8c#5aba6862d5c35b8c)?  Other options?

If we backout the whole patch, I have more confidence that the doctests will get fixed quickly.


---

Attachment

Backout #9501


---

Comment by mpatel created at 2010-07-28 22:41:44

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-07-28 22:41:44

Replying to [comment:5 jhpalmieri]:
> Replying to [comment:2 mpatel]:
> > For now, should we tag the relevant tests with `# not tested` or [backout the whole patch](https://groups.google.com/group/sage-release/browse_thread/thread/9455213e89f94692/5aba6862d5c35b8c#5aba6862d5c35b8c)?  Other options?
> 
> If we backout the whole patch, I have more confidence that the doctests will get fixed quickly.

Adapting the procedure in [comment:ticket:9583:47 this comment] at #9583, I've attached a patch that undoes (or should undo) all of #9501.  If the patch gets a positive review, we can open a new ticket for re-merging #9501.


---

Comment by leif created at 2010-07-28 23:09:58

Hmmm, of course a simple procedure, but we'd back out too much in my opinion...

But I can live with that. (And I'm currently too (laz|bus)y to sort out the desirable parts of the original patch.)


---

Attachment

Backouts only ticket-relevant parts of #9501 (subset of Mitesh's patch)


---

Comment by leif created at 2010-07-28 23:50:14

Replying to [comment:7 leif]:
> (And I'm currently too (laz|bus)y to sort out the desirable parts of the original patch.)

Couldn't resist though (simpler as expected).

Not very tested, only successfully ran `./sage -t -long devel/sage/sage/parallel/` and rebuilt the documentation without errors or warnings.
(Ubuntu 9.04 x86_64, Core2, gcc 4.3.3)

So now two concurrent patches to review... ;-)


---

Comment by jhpalmieri created at 2010-07-29 00:03:17

I've tested mpatel's patch on 5 machines: 4 on which the problem originally occurred (sage.math and skynet machines eno, iras, and taurus) and one machine (running OS X) which didn't have the original problem.  After applying the patch, all tests pass for the directory "parallel" on all 5 machines.  Long doctests for the whole Sage library pass on sage.math and taurus except for previously known, unrelated, failures.

I don't know if I'll get to leif's patch.

Since this is a rollback to a previous situation, I think this is good enough for a positive review for mpatel's patch, though.  Opinions?


---

Comment by leif created at 2010-07-29 00:09:13

Let the release managers decide... ;-)


---

Comment by ddrake created at 2010-07-29 00:26:57

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-07-29 00:26:57

Replying to [comment:9 jhpalmieri]:
> Since this is a rollback to a previous situation, I think this is good enough for a positive review for mpatel's patch, though.  Opinions?

You've done some good testing, and since the original patch was an enhancement, and didn't fix any bugs or failing doctests (right?), I think a positive review is warranted here.


---

Comment by leif created at 2010-07-29 00:31:54

Replying to [comment:11 ddrake]:
> ... since the original patch was an enhancement, and didn't fix any bugs or failing doctests (right?)

Well, I pushed back in mostly fixes (and improvements) to the documentation (one might consider bugfixes, too).


---

Comment by leif created at 2010-07-29 00:36:40

Besides the above mentioned, this would completely miss, too:

```
       - ``reset_interface`` -- if True (the default), all the 
         pexpect interfaces are reset in the forked off 
         subprocesses.  You definitely want this, since not doing 
         this can lead to weird issues.
```



---

Comment by leif created at 2010-07-29 00:41:31

Ooops, forget my last comment: The reset is performed just unconditionally in Mitesh's version.


---

Comment by mpatel created at 2010-07-29 05:31:02

A partial backout, since it retains only some of the changes from #9501, needs a new review, which currently, at least, we don't have.  Given the need to press forward with the 4.5.2 release cycle, I'm merging [attachment:trac_9616-backout_9501_fork_deco.patch] into 4.5.2.rc0.

This may not be an ideal resolution, but it seems reasonable given the circumstances.  Absolutely no offense is intended.

I've opened #9631 for re-merging #9501 after we fix the NFS/doctest problem.


---

Comment by mpatel created at 2010-07-29 05:31:02

Resolution: fixed
