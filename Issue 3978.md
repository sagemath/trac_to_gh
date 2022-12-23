# Issue 3978: Sage 3.1.2.alpha1: ghmm and hmm numerical noise doctest failures

Issue created by migration from https://trac.sagemath.org/ticket/3978

Original creator: mabshoff

Original creation time: 2008-08-28 19:55:32

Assignee: mabshoff

John Cremona reported:

```
sage -t  devel/sage/sage/stats/hmm/hmm.pyx 
********************************************************************** 
File "/home/john/sage-3.1.2.alpha1/tmp/hmm.py", line 678: 
    sage: a.viterbi([1,0,0,1,0,0,1,1]) 
Expected: 
    ([1, 0, 0, 1, 1, 0, 1, 1], -11.062453224772216) 
Got: 
    ([1, 0, 0, 1, 0, 0, 1, 1], -11.062453224772215) 
********************************************************************** 
File "/home/john/sage-3.1.2.alpha1/tmp/hmm.py", line 686: 
    sage: a.viterbi([3/4, 'abc', 'abc'] + [3/4]*10) 
Expected: 
    ([0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], -25.299405845367794) 
Got: 
    ([0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], -25.299405845367794) 
********************************************************************** 
1 items had failures: 
   2 of   6 in __main__.example_19 
***Test Failed*** 2 failures. 
For whitespace errors, see the file 
/home/john/sage-3.1.2.alpha1/tmp/.doctest_hmm.py 
         [1.8 s] 
exit code: 1024 
```

William then suggested:

```
I think the above is just numerical noise.  The Viterbi algorithm
is an approximate numerical algorithm using double precision numbers,
and can give slightly different answers on different hardware.
Can you change the doctest to:

     sage: a.viterbi([1,0,0,1,0,0,1,1])  # numerical instability on
some platforms
    ([1, 0, 0, 1, ..., 0, 1, 1], -11.06245322477221...)
```


Cheers,

Michael


---

Comment by jsp created at 2008-08-28 20:29:59

On Fedora 9, 32 bits I get:



```
jaap@paix sage-3.1.2.alpha1]$ ./sage -t  devel/sage/sage/stats/hmm/chmm.pyx
sage -t  devel/sage/sage/stats/hmm/chmm.pyx                 **********************************************************************
File "/home/jaap/downloads/sage-3.1.2.alpha1/tmp/chmm.py", line 392:
    sage: m
Expected:
    Gaussian Hidden Markov Model with 2 States
    Transition matrix:
    [0.000368587006957    0.999631412993]
    [              0.1               0.9]
    Emission parameters:
    [(0.0, 1.0), (1.0, 1.0)]
    Initial probabilities: [1.0, 0.0]
Got:
    Gaussian Hidden Markov Model with 2 States
    Transition matrix:
    [0.000368587006957    0.999631412993]
    [              0.1               0.9]
    Emission parameters:
    [(0.0, 1.0), (1.0, 1.0)]
    Initial probabilities: [0.99999999999999989, 0.0]
**********************************************************************
File "/home/jaap/downloads/sage-3.1.2.alpha1/tmp/chmm.py", line 579:
    sage: m.log_likelihood([ ([1,0,1,1], 10),  ([1,0,1,20], 0.1)  ])
Expected:
    -72.225116741468781
Got:
    -72.225116741468767
**********************************************************************
File "/home/jaap/downloads/sage-3.1.2.alpha1/tmp/chmm.py", line 599:
    sage: m.log_likelihood(finance.TimeSeries(100).randomize('normal',0,1))
Expected:
    -5275.3082940787635
Got:
    -5275.3082940787644
**********************************************************************
File "/home/jaap/downloads/sage-3.1.2.alpha1/tmp/chmm.py", line 701:
    sage: m
Expected:
    Gaussian Hidden Markov Model with 2 States
    Transition matrix:
    [1.0 0.0]
    [0.0 1.0]
    Emission parameters:
    [(1.946539535984342, 0.70508296299241024), (2.0208156913293394, 0.70680033099099593)]
    Initial probabilities: [0.28024729110782109, 0.71975270889217891]
Got:
    Gaussian Hidden Markov Model with 2 States
    Transition matrix:
    [1.0 0.0]
    [0.0 1.0]
    Emission parameters:
    [(1.9465395359843407, 0.70508296299241002), (2.0208156913293394, 0.70680033099099593)]
    Initial probabilities: [0.28024729110782109, 0.71975270889217891]
**********************************************************************
File "/home/jaap/downloads/sage-3.1.2.alpha1/tmp/chmm.py", line 713:
    sage: m
Expected:
    Gaussian Hidden Markov Model with 2 States
    Transition matrix:
    [1.0 0.0]
    [0.0 1.0]
    Emission parameters:
    [(1.5851786151779879, 0.57264580740105153), (1.5945035666064733, 0.57928632238916189)]
    Initial probabilities: [0.38546857052811945, 0.61453142947188055]
Got:
    Gaussian Hidden Markov Model with 2 States
    Transition matrix:
    [1.0 0.0]
    [0.0 1.0]
    Emission parameters:
    [(1.5851786151779879, 0.5726458074010512), (1.5945035666064735, 0.579286322389162)]
    Initial probabilities: [0.38546857052811911, 0.614531429471881]
**********************************************************************
File "/home/jaap/downloads/sage-3.1.2.alpha1/tmp/chmm.py", line 1012:
    sage: m
Expected:
    Gaussian Hidden Markov Model with 2 States
    Transition matrix:
    [0.000368587006957    0.999631412993]
    [              0.1               0.9]
    Emission parameters:
    [(0.0, 1.0), (1.0, 1.0)]
    Initial probabilities: [1.0, 0.0]
Got:
    Gaussian Hidden Markov Model with 2 States
    Transition matrix:
    [0.000368587006957    0.999631412993]
    [              0.1               0.9]
    Emission parameters:
    [(0.0, 1.0), (1.0, 1.0)]
    Initial probabilities: [0.99999999999999989, 0.0]
**********************************************************************
4 items had failures:
   1 of   9 in __main__.example_11
   2 of  13 in __main__.example_18
   2 of  13 in __main__.example_20
   1 of   9 in __main__.example_27
***Test Failed*** 6 failures.
For whitespace errors, see the file /home/jaap/downloads/sage-3.1.2.alpha1/tmp/.doctest_chmm.py
	 [8.9 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  devel/sage/sage/stats/hmm/chmm.pyx
Total time for all tests: 8.9 seconds

```




```
sage -t  devel/sage/sage/stats/hmm/hmm.pyx                  **********************************************************************
File "/home/jaap/downloads/sage-3.1.2.alpha1/tmp/hmm.py", line 678:
    sage: a.viterbi([1,0,0,1,0,0,1,1])
Expected:
    ([1, 0, 0, 1, 1, 0, 1, 1], -11.062453224772216)
Got:
    ([1, 0, 0, 1, 0, 0, 1, 1], -11.062453224772215)
**********************************************************************
File "/home/jaap/downloads/sage-3.1.2.alpha1/tmp/hmm.py", line 686:
    sage: a.viterbi([3/4, 'abc', 'abc'] + [3/4]*10)
Expected:
    ([0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], -25.299405845367794)
Got:
    ([0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], -25.299405845367794)
**********************************************************************
1 items had failures:
   2 of   6 in __main__.example_19
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/jaap/downloads/sage-3.1.2.alpha1/tmp/.doctest_hmm.py
	 [3.2 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  devel/sage/sage/stats/hmm/hmm.pyx
Total time for all tests: 3.2 seconds

```



---

Attachment


---

Comment by rlm created at 2008-09-12 23:22:04

Looks good to me.


---

Comment by mabshoff created at 2008-09-12 23:24:55

Merged in Sage 3.1.2.rc2


---

Comment by mabshoff created at 2008-09-12 23:24:55

Resolution: fixed
