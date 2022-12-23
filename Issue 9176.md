# Issue 9176: cygwin: various heegner_index errors involving interval arithmetic on cygwin

Issue created by migration from https://trac.sagemath.org/ticket/9176

Original creator: was

Original creation time: 2010-06-07 05:33:45

Assignee: tbd

CC:  kcrisman dimpase


```

sage -t  "devel/sage/sage/schemes/elliptic_curves/heegner.py"
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/heegner.py", line 6380:
    sage: E.heegner_index(-7)
Expected:
    1.00000?
Got:
    1
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/heegner.py", line 6410:
    sage: I = E.heegner_index(-8); I
Expected:
    1.50000?
Got:
    1
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/heegner.py", line 6412:
    sage: 2*I
Expected:
    3.0000?
Got:
    2
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/heegner.py", line 6546:
    sage: E.heegner_index_bound()
Expected:
    ([2], -7)
Got:
    ([], -7)
**********************************************************************
2 items had failures:
   3 of  15 in __main__.example_229
   1 of   4 in __main__.example_231
***Test Failed*** 4 failures.
For whitespace errors, see the file /home/wstein/.sage//tmp/.doctest_heegner.py
```



---

Comment by kcrisman created at 2011-08-02 02:24:56

This file passed doctests in a build of mine on XP.


---

Comment by kcrisman created at 2011-08-19 14:33:31

But trying the first example by hand leads to a segfault (presumably related to the segfault currently bedeveling Cygwin startup, see #11551).

That is weird.  Is it possible that a _silent_ segfault makes a doctest think it passed?


---

Comment by jpflori created at 2013-01-15 18:13:07

Got lots of failures, apparently because of forking issues, I'll try a rebase.


---

Comment by jpflori created at 2013-01-15 18:14:00

Also lots of MemoryError for PARI trying to allocate memory.


---

Comment by kcrisman created at 2013-01-15 18:14:49

> Got lots of failures, apparently because of forking issues, I'll try a rebase.
Glad at least _one_ of the forking issues I had cropped up for you :-) Even if it does work on a rebase, don't forget to try by hand as well.


---

Comment by jpflori created at 2013-01-15 18:15:34

And indeed inside "./sage -gp" I cannot allocatemem(512000000), but only 256000000, not sure why though.


---

Comment by jpflori created at 2013-01-15 18:16:33

I think I only have one forking issue (among 202 failing tests) caused by ecl which I rebuilt in the end (and potentially did not rebase after that).


---

Comment by jpflori created at 2013-01-15 18:18:35

And I guess it is http://cygwin.com/cygwin-ug-net/setup-maxmem.html so was expected.

So I'm left with the one forking issue :)


---

Comment by jpflori created at 2013-01-15 21:04:52

Ok I still get the forking issue after rebasing :( the only solution might be to get a clean install at once (I rebuilt ECL p1 spkg and dependencies after having installed all Sage with the p0).

Not sure how to let Cygwin increase the mx mem used, using peflags on python tells me it could not open the file...


---

Comment by jpflori created at 2013-01-16 10:08:01

The max mem I can allocate is 502333407 and all the hacks I tried in the registry seem to have no (good or bad) effect.


---

Comment by jpflori created at 2013-01-16 10:37:54

Ok, I manage to use peflags to modify --cygwin-heap but if I set it to 1024MB then I get forking errors...


---

Comment by jpflori created at 2013-01-16 10:45:02

I can set it to 600MB without forking errors and that is enough to let the tests pass.
(And indeed the global variable heap_chunk_in_mb support has been removed in Cygwin 1.7.10, see http://cygwin.com/cygwin-ug-net/ov-new1.7.html.)


---

Comment by dimpase created at 2013-01-27 09:34:48

Changing status from new to needs_review.


---

Comment by dimpase created at 2013-01-27 09:34:48

I propose to close it (as won't fix/worksforme), as it works now.


---

Comment by jpflori created at 2013-01-30 10:41:03

Replying to [comment:13 dimpase]:
> I propose to close it (as won't fix/worksforme), as it works now.
Did you actually manage to run the test without hacking around with --cygwin-heap?
I think we should at least add some doc somewhere to state that the tests are expected to fail with default max heap memory and how to modify that (e.g. use peflags and the global var is not supported anymore).


---

Comment by jpflori created at 2013-01-30 17:47:26

Changing status from needs_review to needs_info.


---

Comment by jpflori created at 2013-03-01 10:31:44

Changing status from needs_info to needs_review.


---

Comment by jpflori created at 2013-03-01 10:31:44

Anyway, I don't think we should deal with the peflags usage in another ticket as this was not the point of this ticket originally.

So lets close this one.
Ill open a ticket for documenting usage of peflags shortly.


---

Comment by jpflori created at 2013-03-01 10:34:08

This is #14207.


---

Comment by kcrisman created at 2013-03-08 12:56:36

Okay, I finally got this to doctest without forking errors, and mostly am seeing the same problem you are.  I'm not going to bother messing around with Pari's memory because I don't know how to do that and you guys are on it.  I do get a lot of extra failures

```
Expected:
    0
Got:
    32
```

which seems to be exactly one per example.  Of course, there _is_ no such doctest listed in the file, so this must be something in the framework.


---

Comment by jpflori created at 2013-03-14 00:25:38

Replying to [comment:18 kcrisman]:
> Okay, I finally got this to doctest without forking errors, and mostly am seeing the same problem you are.  I'm not going to bother messing around with Pari's memory because I don't know how to do that and you guys are on it.  I do get a lot of extra failures
> {{{
> Expected:
>     0
> Got:
>     32
> }}}
I guess these extra failures are mostly due to the fact a previous doctest needing too much memory for PARI failed.
> which seems to be exactly one per example.  Of course, there _is_ no such doctest listed in the file, so this must be something in the framework.


---

Comment by kcrisman created at 2013-03-15 18:24:01

Sorry for not following up - so you agree with Dima that this is a pure memory issue, and so should be closed?  Should we at least put a mention in the doc for this file that "if you are on a system with not much memory allocated (such as default Cygwin, but perhaps others like tablets or something) then there is this trick, see the verbiage added by #14207"?


---

Comment by jpflori created at 2013-03-30 13:00:48

I do, lets close this one.


---

Comment by jpflori created at 2013-03-30 13:00:48

Changing status from needs_review to positive_review.


---

Comment by jpflori created at 2013-03-30 13:00:48

Changing keywords from "" to "cygwin".


---

Comment by jdemeyer created at 2013-04-01 13:01:04

Please fill in Author/Reviewer.


---

Comment by jdemeyer created at 2013-04-03 15:11:18

Resolution: invalid
