# Issue 8812: notebook doctest failure in sage-4.4.1.alpha0

Issue created by migration from https://trac.sagemath.org/ticket/8812

Original creator: was

Original creation time: 2010-04-29 00:30:55

Assignee: jason, was

CC:  acleone


```
wstein@sage:~/build/release/4.4.1/sage-4.4.1.alpha1$ ./sage -t  -long "local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/notebook/twist.py"
sage -t -long "local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/notebook/twist.py"
 **********************************************************************
File "/mnt/usb1/scratch/wstein/build/release/4.4.1/sage-4.4.1.alpha1/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/notebook/twist.py", line 1696:
    sage: E.render(ctx)
Expected:
    <RedirectResponse 301 Document moved to over there.>
Got:
    <sagenb.notebook.twist.RedirectResponse code=303, streamlen=None>
**********************************************************************
1 items had failures:
   1 of  15 in __main__.example_30
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/wstein/sage//tmp/.doctest_twist.py
         [4.0 s]

----------------------------------------------------------------------
The following tests failed:


        sage -t -long "local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/notebook/twist.py"
Total time for all tests: 4.0 seconds
```


This is a result of #8725.


---

Comment by acleone created at 2010-04-29 01:16:32

Resolution: duplicate


---

Comment by acleone created at 2010-04-29 01:16:32

Already a patch up at #8724
