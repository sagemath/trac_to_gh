# Issue 7093: fast_eval -- numerical noise on OS X 10.6

Issue created by migration from https://trac.sagemath.org/ticket/7093

Original creator: was

Original creation time: 2009-10-01 19:43:40

Assignee: tbd


```
sage -t -long "devel/sage/sage/ext/fast_eval.pyx"
**********************************************************************
File "/Users/was/build/sage-4.1.2.rc0/devel/sage/sage/ext/fast_eval.pyx", line 1080:
    sage: f(0.5)
Expected:
    0.5235987755982989...
Got:
    0.52359877559829882
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_32
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/was/.sage//tmp/.doctest_fast_eval.py
```



---

Attachment


---

Comment by timdumol created at 2009-10-01 19:51:20

Doesn't seem it can do any harm. Applies and passes on *Linux*. Release manager may want to see if this works on OS X as advertised.


---

Comment by was created at 2009-10-01 20:01:51

Resolution: fixed


---

Comment by chapoton created at 2017-07-19 09:02:48

for uniqueness of author names
