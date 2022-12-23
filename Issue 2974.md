# Issue 2974: interfaces/r.py doctest failures on many linux machines

Issue created by migration from https://trac.sagemath.org/ticket/2974

Original creator: was

Original creation time: 2008-04-20 21:04:35

Assignee: failure


```
sage -t  devel/sage/sage/interfaces/r.py                    **********************************************************************
File "/home/was/build/sage-3.0.rc0/tmp/r.py", line 329:
    sage: r.png(file='"%s"'%filename)
Expected:
    NULL
Got:
    [1] 10.4
**********************************************************************
File "/home/was/build/sage-3.0.rc0/tmp/r.py", line 333:
    sage: r.plot(x,y)
Expected:
    NULL
Got:
    [1] 3
**********************************************************************
File "/home/was/build/sage-3.0.rc0/tmp/r.py", line 335:
    sage: r.dev_off()
Expected:
        null device
                  1
Got:
    [1] 2
**********************************************************************
File "/home/was/build/sage-3.0.rc0/tmp/r.py", line 338:
    sage: import os; os.unlink(filename)
Exception raised:
    Traceback (most recent call last):
      File "/home/was/build/sage-3.0.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[7]>", line 1, in <module>
        import os; os.unlink(filename)###line 338:
    sage: import os; os.unlink(filename)
    OSError: [Errno 2] No such file or directory: '/home/was/.sage//temp/arch/17729//tmp_1.png'
**********************************************************************
File "/home/was/build/sage-3.0.rc0/tmp/r.py", line 1064:
    sage: r.png(file='"%s"'%filename)
Expected:
    NULL
Got:
    [1] 1
**********************************************************************
File "/home/was/build/sage-3.0.rc0/tmp/r.py", line 1068:
    sage: r.plot(x,y)
Expected:
    NULL
Got:
    [1] 1 2 3
**********************************************************************
File "/home/was/build/sage-3.0.rc0/tmp/r.py", line 1070:
    sage: r.dev_off()
Expected:
        null device
                  1
Got:
    [1] 3
**********************************************************************
File "/home/was/build/sage-3.0.rc0/tmp/r.py", line 1073:
    sage: import os; os.unlink(filename)
Exception raised:
    Traceback (most recent call last):
      File "/home/was/build/sage-3.0.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_40[7]>", line 1, in <module>
        import os; os.unlink(filename)###line 1073:
    sage: import os; os.unlink(filename)
    OSError: [Errno 2] No such file or directory: '/home/was/.sage//temp/arch/17729//tmp_2.png'
**********************************************************************
2 items had failures:
   4 of   8 in __main__.example_3
   4 of   8 in __main__.example_40
***Test Failed*** 8 failures.
For whitespace errors, see the file /home/was/build/sage-3.0.rc0/tmp/.doctest_r.py
         [10.0 s]
```



---

Comment by mhansen created at 2008-04-21 00:40:03

Changing status from new to assigned.


---

Attachment


---

Comment by mhansen created at 2008-04-21 00:40:03

Changing assignee from failure to mhansen.


---

Comment by mabshoff created at 2008-04-21 02:46:18

Merged in Sage 3.0.rc1


---

Comment by mabshoff created at 2008-04-21 02:46:18

Resolution: fixed


---

Comment by jason created at 2009-09-16 16:38:57

This will likely be reverted once #2178 is fixed.


---

Comment by jason created at 2009-09-16 16:39:17

Oops, I mean once #2978 is fixed.
