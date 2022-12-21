# Issue 4071: Fix issues in the lisp interface

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-09-07 18:09:06

Assignee: was


```
File "/Users/mhansen/sage-3.1.2.rc0/tmp/lisp.py", line 5:
    sage: lisp.eval('(* 4 5)')
Expected:
    '20'
Got:
    '(* 4 5)\r\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\n20'
**********************************************************************
File "/Users/mhansen/sage-3.1.2.rc0/tmp/lisp.py", line 22:
    sage: lisp.eval('(+ %s %s)'%(a.name(), b.name()))
Expected:
    '8'
Got:
    '(+ sage0 sage1)\r\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\n8'
**********************************************************************
File "/Users/mhansen/sage-3.1.2.rc0/tmp/lisp.py", line 27:
    sage: lisp.eval('(defun factorial (n) (if (= n 1) 1 (* n (factorial (- n 1)))))')
Expected:
    'FACTORIAL'
Got:
    '(defun factorial (n)\x08\x08\x08\x1b[C\x1b[C\x1b[C (if (= n 1)\x08\x08\x08\x08\x08\x08\x08\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C 1 (* n (factorial (- n 1)\x08\x08\x08\x08\x08\x08\x08\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C)\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C)\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x08\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C)\r\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C)\r\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\nFACTORIAL'
**********************************************************************
File "/Users/mhansen/sage-3.1.2.rc0/tmp/lisp.py", line 112:
    sage: lisp.eval('(+ 2 2)')
Expected:
    '4'
Got:
    '(+ 2 2)\r\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\x1b[C\n4'
**********************************************************************
File "/Users/mhansen/sage-3.1.2.rc0/tmp/lisp.py", line 390:
    sage: one == one
Expected:
    True
Got:
    False
**********************************************************************
File "/Users/mhansen/sage-3.1.2.rc0/tmp/lisp.py", line 394:
    sage: one < two
Expected:
    True
Got:
    False
**********************************************************************
File "/Users/mhansen/sage-3.1.2.rc0/tmp/lisp.py", line 400:
    sage: two == 2
Expected:
    True
Got:
    False
**********************************************************************
File "/Users/mhansen/sage-3.1.2.rc0/tmp/lisp.py", line 420:
    sage: lisp(0).bool()
Expected:
    False
Got:
    True
**********************************************************************
4 items had failures:
   3 of  17 in __main__.example_0
   1 of   3 in __main__.example_2
   3 of   9 in __main__.example_23
   1 of   5 in __main__.example_24
***Test Failed*** 8 failures.
For whitespace errors, see the file /Users/mhansen/sage-3.1.2.rc0/tmp/.doctest_lisp.py
         [7.4 s]
exit code: 1024
```



---

Attachment


---

Comment by mhansen created at 2008-09-07 18:22:09

Changing status from new to assigned.


---

Comment by mhansen created at 2008-09-07 18:22:09

Changing assignee from was to mhansen.


---

Comment by mabshoff created at 2008-09-07 18:25:07

Patch looks good to me and fixes the issue.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-07 23:06:15

Resolution: fixed


---

Comment by mabshoff created at 2008-09-07 23:06:15

Merged in Sage 3.1.2.rc1
