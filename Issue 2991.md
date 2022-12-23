# Issue 2991: dsage testdoc problem

Issue created by migration from https://trac.sagemath.org/ticket/2991

Original creator: was

Original creation time: 2008-04-21 16:49:02

Assignee: yi

The following happens some of the time (though not always).  I'm guessing the fix is to
allow for more possibilities in the output?


```
sage@modular:~/build/sage-3.0.rc1$ ./sage -t devel/sage/sage/dsage/tests/testdoc.py
sage -t  devel/sage/sage/dsage/tests/testdoc.py             **********************************************************************
File "/home2/sage/build/sage-3.0.rc1/tmp/testdoc.py", line 46:
    sage: reactor.callFromThread(reactor.stop)
Expected nothing
Got:
    [DSage] Closed connection to localhost
**********************************************************************
File "/home2/sage/build/sage-3.0.rc1/tmp/testdoc.py", line 47:
    sage: d._dsage_thread.join()
Expected:
    [DSage] Closed connection to localhost
Got nothing
**********************************************************************
1 items had failures:
   2 of  23 in __main__.example_0
***Test Failed*** 2 failures.
For whitespace errors, see the file /home2/sage/build/sage-3.0.rc1/tmp/.doctest_testdoc.py
         [20.0 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage/sage/dsage/tests/testdoc.py
Total time for all tests: 20.0 seconds
sage@modular:~/build/sage-3.0.rc1$ 
```



---

Comment by was created at 2008-04-22 04:52:05

Resolution: fixed


---

Attachment
