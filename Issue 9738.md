# Issue 9738: Stealth core dump from testing sage/interfaces/genus2reduction.py

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-08-12 22:58:35

Assignee: mvngu

CC:  robertwb was jdemeyer

With Sage 4.5.3.alpha0 on sage.math:

```sh
$ cd SAGE_ROOT
$ find -name core -type f
$ ulimit -c unlimited
$ ./sage -t -long devel/sage/sage/interfaces/genus2reduction.py 
sage -t -long "devel/sage/sage/interfaces/genus2reduction.py"
         [3.1 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 3.1 seconds
$ find -name core -type f
./data/extcode/genus2reduction/core
$
```

For background see [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/239f712a39fce4a).


---

Comment by mpatel created at 2010-08-12 23:15:27

I interleaved `find -name core -type f` with executing the examples in `genus2reduction.py` in an interactive Sage session.  I see the core file only _after_ I exit Sage, which ends with

```
Exiting Sage (CPU time 0m0.17s, Wall time 2m6.89s).
Exiting spawned Genus2reduction process.
```

Also, [here is the log](http://sage.math.washington.edu/home/mpatel/trac/9738/genus2reduction-21918-22537264-2.log) I  find in `DOT_SAGE/pexpect_logs/` after

```sh
env SAGE_PEXPECT_LOG="yes" ./sage -t devel/sage/sage/interfaces/genus2reduction.py
```



---

Attachment

Quit on `quit`.  Diff of `genus2reduction.c` from g2r 0.3.p6.


---

Comment by mpatel created at 2010-08-13 00:45:23

I've attached a possible solution.  If it looks good, I can make a new spkg.  We may need to coordinate with #9591.


---

Comment by jdemeyer created at 2010-08-13 22:45:57

Replying to [comment:2 mpatel]:
> We may need to coordinate with #9591.

I don't think there is a problem, this issue is independent of #9343 and #9591 (we just have to rename the spkg at #9591 if this gets merged first).


---

Attachment

Alternative patch to fix the issue


---

Comment by jdemeyer created at 2010-08-13 22:53:20

I think mpatel's patch fixes the problem but does not address the real issue here, namely that PARI by default catches various signals and "handles" them.  But this is not what we want here.  Not making PARI install signal handlers solves the issue.

My patch also makes genus2reduction exit when EOF is encountered in the standard input.


---

Comment by mpatel created at 2010-08-13 23:50:41

Jeroen's patch is definitely better than mine.  Thanks!

Whether I run the doctest above or run `genus2reduction` directly from the shell and press ctrl-c/d, the program quits with no core dump.  Evaluating `genus2reduction.console()` in the Sage console and pressing ctrl-c/d returns me to the `sage:` prompt.  Also, running the long doctest suite passes without reproducible failures and leaves no relevant cores.

`Genus2reduction_expect` in `genus2reduction.py` still uses its base class' `Expect._quit_string`, which returns "quit", but I think we can leave that alone(?).

Are there any objections to making a new spkg here with Jeroen's patch?  If we do, we should put `genus2reduction.c` under version control.  Although I'm averse to putting too many logically different spkg changes in one ticket, I'll understand if we roll the changes here into #9591 and make this ticket a virtual blocker for an otherwise PARI-focused Sage 4.6.


---

Comment by mpatel created at 2010-08-14 05:15:25

Changing priority from blocker to major.


---

Comment by jdemeyer created at 2010-08-14 09:51:14

Replying to [comment:6 mpatel]:
> Are there any objections to making a new spkg here with Jeroen's patch?
No objections.  If you think this patch can make it into sage-4.5.3, go ahead and do it.  If we merge it in sage-4.6, it would be better suited in #9591.


---

Comment by jdemeyer created at 2010-08-14 19:39:06

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2010-08-14 19:39:06

Since there seems to be a push towards merging #9343 (and hence #9591) soon, I will merge my patch into #9591.


---

Comment by mpatel created at 2010-08-31 00:41:03

# Release manager

Please close this ticket when #9591 is merged.


---

Comment by mpatel created at 2010-09-04 07:07:07

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-10 10:54:31

Resolution: duplicate
