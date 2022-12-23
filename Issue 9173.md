# Issue 9173: cygwin: BSD.py tests behave differently on cygwin, so need to be written to reflect that

Issue created by migration from https://trac.sagemath.org/ticket/9173

Original creator: was

Original creation time: 2010-06-07 04:55:50

Assignee: tbd

CC:  jpflori dimpase kcrisman


```

sage -t  "devel/sage/sage/schemes/elliptic_curves/BSD.py"   
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/BSD.py", line 174:
    sage: native_two_isogeny_descent_work(E, E.two_torsion_rank())
Expected:
    (1, 1, 0, 0, None)
Got:
    (0, 1, 0, 1, None)
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/BSD.py", line 391:
    sage: E.prove_BSD(verbosity=1, secs_hi=1)
Expected:
    p = 2: True by 2-descent
    Timeout stopped Heegner index computation...
    Proceeding to use heegner_index_bound instead.
    True for p not in {2, 3} by Kolyvagin.
    [3]
Got:
    p = 2: True by 2-descent
    Timeout stopped Heegner index computation...
    Proceeding to use heegner_index_bound instead.
    True for p not in {2, 3, 5} by Kolyvagin.
    True for p=5 by Stein-Wuthrich.
    [3]
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/schemes/elliptic_curves/BSD.py", line 426:
    sage: E.prove_BSD(verbosity=1)
Expected:
    p = 2: True by 2-descent
    Timeout stopped Heegner index computation...
    Proceeding to use heegner_index_bound instead.
    True for p not in {2} by Kolyvagin.
    []
Got:
    p = 2: True by 2-descent
    Timeout stopped Heegner index computation...
    Proceeding to use heegner_index_bound instead.
    True for p not in {2, 3, 5} by Kolyvagin.
    True for p=5 by Stein-Wuthrich.
    p = 3 may divide the Heegner index, for which only a bound was computed.
    ALERT: p = 3 left in Kolyvagin bound
        0 <= ord_p(#Sha) <= 2
        ord_p(#Sha_an) = 0
    [3]
**********************************************************************
2 items had failures:
   1 of   7 in __main__.example_4
   2 of  34 in __main__.example_6
***Test Failed*** 3 failures.
```



---

Comment by drkirkby created at 2010-06-08 00:40:42

The same is happening on Solaris 10 on all the SPARC boxes I have access to - see #9127  It appears to be a function of the speed of the computer, with timeouts occuring on slower hardware. I assume the overhead of Cygwin is causing this problem. 

As such, I think this can probably be closed as a duplicate of #9127, which has positive review. You can try the patch there

http://trac.sagemath.org/sage_trac/raw-attachment/ticket/9127/trac_9127.patch

Dave


---

Comment by drkirkby created at 2010-06-08 00:45:28

On closer inspection, it looks like the issues you are getting on Cygwin are larger than those on Solaris, as I have not seen the 


```
Expected:
    (1, 1, 0, 0, None)
Got:
    (0, 1, 0, 1, None)
```


error - only the ones due to timeouts. 

Dave


---

Comment by kcrisman created at 2011-08-02 02:26:28

This doctest passed on a build of mine on XP.  In fact, the only files in schemes/ that failed were two in the plane conics section, probably because of "I" not working.


---

Comment by kcrisman created at 2013-01-15 15:49:28

I get lots of forking errors now, because it "can't start pari".


---

Comment by jpflori created at 2013-01-15 18:10:26

And the test passes for me (64bits W7 + 5.6.rc0).


---

Comment by kcrisman created at 2013-01-15 18:11:58

> And the test passes for me (64bits W7 + 5.6.rc0).
Don't forget to try these by hand as well.  In the past I've had failures only in the terminal.


---

Comment by jpflori created at 2013-01-15 21:09:38

Replying to [comment:6 kcrisman]:
> > And the test passes for me (64bits W7 + 5.6.rc0).
> Don't forget to try these by hand as well.  In the past I've had failures only in the terminal.
You mean copy/paste the doctests in an interactive Sage session?
That's kind of boring isn't it? :)


---

Comment by jpflori created at 2013-01-15 21:15:05

I tested some random examples and some from te failing ones quoting in the ticket description and had no problems.


---

Comment by kcrisman created at 2013-01-16 01:49:40

> > > And the test passes for me (64bits W7 + 5.6.rc0).
> > Don't forget to try these by hand as well.  In the past I've had failures only in the terminal.
> You mean copy/paste the doctests in an interactive Sage session?
> That's kind of boring isn't it? :)
Yes, you are right.  But unfortunately I had some bad experiences with these Cygwin tests in the past so I figure I should ask - sorry :(


---

Comment by jpflori created at 2013-01-30 10:48:00

Changing status from new to needs_review.


---

Comment by jpflori created at 2013-02-08 12:45:20

Changing status from needs_review to positive_review.


---

Comment by jpflori created at 2013-02-08 12:45:20

No problems on another install, so let's close this one.


---

Comment by jdemeyer created at 2013-02-08 13:19:52

Resolution: worksforme
