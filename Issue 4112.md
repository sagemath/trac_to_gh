# Issue 4112: 3.1.2.rc2 doctest failure: sage/interfaces/sage0.py

Issue created by migration from https://trac.sagemath.org/ticket/4112

Original creator: craigcitro

Original creation time: 2008-09-14 06:20:47

Assignee: was

I saw the following doctest failure on my Intel OSX 10.5 MacBook Pro:


```
sage -t  devel/sage-main/sage/interfaces/sage0.py           *******************
**************************************************
File "/Users/craigcitro/three-oh-two/tmp/sage0.py", line 276:
    sage: sage0.eval('2+2')
Expected:
    '4'
Got:
    '4\n'
**********************************************************************
File "/Users/craigcitro/three-oh-two/tmp/sage0.py", line 289:
    sage: sage0.get('x')
Expected:
    '2'
Got:
    '2\n'
**********************************************************************
File "/Users/craigcitro/three-oh-two/tmp/sage0.py", line 303:
    sage: sage0.get('x')
Expected:
    '2'
Got:
    '2\n'
**********************************************************************
File "/Users/craigcitro/three-oh-two/tmp/sage0.py", line 314:
    sage: sage0.get('x')
Expected:
    '2'
Got:
    '2\n'
**********************************************************************
File "/Users/craigcitro/three-oh-two/tmp/sage0.py", line 317:
    sage: sage0.get('x')
Expected:
    "...NameError: name 'x' is not defined"
Got:
    "--------------------------------------------------------------------------
\nNameError                                 Traceback (most recent call last)\n
n/Users/craigcitro/three-oh-two/data/extcode/sage/<ipython console> in <module>
)\n\nNameError: name 'x' is not defined\n"
**********************************************************************
File "/Users/craigcitro/three-oh-two/tmp/sage0.py", line 326:
    sage: sage0._contains('2', 'QQ')
Expected:
    True
Got:
    False
**********************************************************************
File "/Users/craigcitro/three-oh-two/tmp/sage0.py", line 350:
    sage: sage0.version() == version()
Expected:
    True
Got:
    False
**********************************************************************
File "/Users/craigcitro/three-oh-two/tmp/sage0.py", line 487:
    sage: sage0_version() == version()
Expected:
    True
Got:
    False
**********************************************************************
File "/Users/craigcitro/three-oh-two/tmp/sage0.py", line 177:
    sage: s.eval('2+2')
Expected:
    '4'
Got:
    '4\n'
**********************************************************************
8 items had failures:
   1 of   3 in __main__.example_10
   1 of   4 in __main__.example_11
   1 of   4 in __main__.example_12
   2 of   6 in __main__.example_13
   1 of   3 in __main__.example_14
   1 of   4 in __main__.example_16
   1 of   4 in __main__.example_26
   1 of   5 in __main__.example_5
***Test Failed*** 9 failures.
For whitespace errors, see the file /Users/craigcitro/three-oh-two/tmp/.doctest
sage0.py
         [9.7 s]
exit code: 1024
```



---

Attachment


---

Attachment

Positive review for trac-4112.patch. There is also some orthogonal issue, but that is followed up at #4116.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-14 09:36:29

Resolution: fixed


---

Comment by mabshoff created at 2008-09-14 09:36:29

Merged in Sage 3.1.2.rc3
