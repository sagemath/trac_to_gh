# Issue 3356: [with patch; not ready for review] finance -- add randomization code; optimize some models; improve plotting code

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-06-03 07:13:19

Assignee: was




---

Attachment

This depends on #3346.


---

Attachment


---

Attachment


---

Attachment

This will be ready to review once the doctest coverage is back at 100%.  As of patch 5 it is at about 90%.


---

Attachment

Added log-normal random distribution.


---

Comment by craigcitro created at 2008-06-20 04:58:55

Changing keywords from "" to "editor_wstein".


---

Attachment

Added doctests for TimeSeries.randomize


---

Comment by ghtdak created at 2008-06-21 04:23:43

patches are dead: Long Live Branches

All future development for sage-finance lives on the finpatch branch.  Instructions at:

http://wiki.sagemath.org/finance


---

Comment by was created at 2008-06-21 23:50:49

>patches are dead: Long Live Branches
> All future development for sage-finance lives on the finpatch branch. Instructions at: 

Umh, no.  All code that goes into Sage must appear as patches on this trac server first so
it can be refereed etc.  What you do to obtain those patches -- use queues, branches, etc.,
is up to you. 

 -- William


---

Comment by ghtdak created at 2008-06-22 00:25:38

In keeping with the Twisted rule, all work has a ticket.  This comment
was posted on a ticket "not ready for review". When its changed to
ready, an aggregate patch will be posted using the accepted process.

The branches, and published repos for the finance/dsageng development
activities provide a finer grained view of the development process for
contributors and casual observers.  Since we have this set up, it seems
easier to use branchy development between reviewable events.

-glenn


---

Attachment


---

Attachment

this patch gets doctest coverage to 100%


---

Comment by was created at 2008-07-03 02:17:14

REMARK: I just realized that the autocovariance function doesn't check that its input
is nonnegative but assumes it in the code.  It would thus segfault or give random garbage
for negative input.  This should be fixed.


---

Attachment

doctest addition and name change of linear_filter to autoregressive_fit


---

Comment by jkantor created at 2008-07-06 01:04:43

Positive review with comments

I've made some changes to the docstring on the linear filter/forecast methods. I think its more accurate to call it autoregressive_fit, and autoregressive_forecast, also added a doctest (patch attached). Also there was a problem with numerical noise on the hurst_exponent causing a doctest failure I added a ...


The doctest for the linear_filter function involving the multifractal random walk seems odd to me (the one outside the time series class, which I call autoregressive_fit). The reason I'm skeptical is that a complicated series is generated and then one does a fit and produces regression coefficients that are [ .998, stuff nearly 0] which means that the forcast says the best prediction of the next value is the previous one plus noise, which makes sense but somehow doesn't seem like as good of a test of the function to me as it could be given its complexity.



Suggestions for future improvement I'll do them in a separate patch unless someone does them first

easy: 

1.  I think it would be nice if autocovariance/correlation could have a second optional parameter so that t.autocovariance(i,j) would return all the autocovariance 
coefficients from i to i+j or between i and j as a timeseries (this is just a list comprehension).



2. partial autocorrelation function, its a function often denoted by \pi such that
\pi_p is last coefficient outputted by autoregressive_fit(p) (formerly known as linearly_filter).


---

Comment by mabshoff created at 2008-07-06 19:35:43

Resolution: fixed


---

Comment by mabshoff created at 2008-07-06 19:35:43

Merged finance.hg in Sage 3.0.4.alpha2 and after resolving two merge issues it seems to doctest fine.

The comments should move to three new tickets.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-06 19:48:07

There are some doctest issues:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2$ sage -t  devel/sage/sage/finance/time_series.pyx # 3 doctests failed
sage -t  devel/sage/sage/finance/time_series.pyx            
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/time_series.py", line 525:
    sage: v.linear_forecast(F)
Expected:
    86.017728504280015
Got:
    86.01772850427912
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/time_series.py", line 1428:
    sage: fbm.hurst_exponent()
Expected:
    0.66787027921443409
Got:
    0.66787027921463038
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/time_series.py", line 1433:
    sage: fbm.hurst_exponent()
Expected:
    0.30450273560706259
Got:
    0.30450273560706026
**********************************************************************
2 items had failures:
   1 of   7 in __main__.example_15
   2 of   9 in __main__.example_46
***Test Failed*** 3 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/.doctest_time_series.py
	 [13.1 s]
exit code: 1024
```

And

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2$ sage -t  devel/sage/sage/matrix/matrix_space.py # 1 doctests failed
sage -t  devel/sage/sage/matrix/matrix_space.py  
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.4.alpha2/tmp/matrix_space.py", line 653:
    sage: list( MatrixSpace(GF(2), 2, 0) )
Expected:
    [[]
    []]
Got:
    [[]]
**********************************************************************
```

and a segfault in devel/sage/sage/matrix/matrix2.pyx.

Checking the merge before taking valgrind for a spin.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-06 19:54:02

This patch fixes the numerical noise doctest issues and one mismerge by me
