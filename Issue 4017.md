# Issue 4017: Sage 3.1.2.alpha1 - PPC OSX: numerical noise in sage/stats/hmm/chmm.pyx

Issue created by migration from https://trac.sagemath.org/ticket/4017

Original creator: mabshoff

Original creation time: 2008-08-31 08:22:58

Assignee: mabshoff


```
sage -t  devel/sage/sage/stats/hmm/chmm.pyx                
**********************************************************************
File "/Users/sagedevel/Desktop/sage-3.1.2.alpha1/tmp/chmm.py", line 579:
    sage: m.log_likelihood([ ([1,0,1,1], 10),  ([1,0,1,20], 0.1)  ])
Expected:
    -72.225116741468781
Got:
    -72.225116741468767
**********************************************************************
File "/Users/sagedevel/Desktop/sage-3.1.2.alpha1/tmp/chmm.py", line 701:
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
    [(1.9465395359843427, 0.70508296299241024), (2.0208156913293389, 0.70680033099099593)]
    Initial probabilities: [0.28024729110782093, 0.71975270889217924]
**********************************************************************
File "/Users/sagedevel/Desktop/sage-3.1.2.alpha1/tmp/chmm.py", line 713:
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
    [(1.5851786151779883, 0.57264580740105153), (1.5945035666064731, 0.57928632238916189)]
    Initial probabilities: [0.38546857052811928, 0.61453142947188077]
**********************************************************************
```



---

Comment by mabshoff created at 2008-08-31 08:23:46

Changing status from new to assigned.


---

Attachment


---

Comment by mhansen created at 2008-08-31 22:16:48

Looks good to me.


---

Comment by mabshoff created at 2008-09-01 02:19:02

Resolution: fixed


---

Comment by mabshoff created at 2008-09-01 02:19:02

Merged in Sage 3.1.2.alpha4
