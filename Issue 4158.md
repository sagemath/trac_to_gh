# Issue 4158: system dependent doctest failures

Issue created by migration from https://trac.sagemath.org/ticket/4158

Original creator: was

Original creation time: 2008-09-20 15:36:43

Assignee: mabshoff

On cicero:

```
sage -t  devel/sage/sage/combinat/root_system/type_dual.py  **********************************************************************
File "/home/wstein/cicero/build/sage-3.1.2/tmp/type_dual.py", line 43:
    sage: [[x.__cmp__(y) for x in ct] for y in ct]
Expected:
    [[0, 1, -1], [-1, 0, -1], [1, 1, 0]]
Got:
    [[0, 1, 1], [-1, 0, 1], [1, 1, 0]]
**********************************************************************
File "/home/wstein/cicero/build/sage-3.1.2/tmp/type_dual.py", line 45:
    sage: sorted(ct)
Expected:
    [['A', 4], A1xB2, B2xA1]
Got:
    [A1xB2, B2xA1, ['A', 4]]
**********************************************************************
1 items had failures:
   2 of   8 in __main__.example_3
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/wstein/cicero/build/sage-3.1.2/tmp/.doctest_type_dual.py
         [3.3 s]
sage -t  devel/sage/sage/combinat/root_system/type_reducible.py**********************************************************************
File "/home/wstein/cicero/build/sage-3.1.2/tmp/type_reducible.py", line 53:
    sage: [[x.__cmp__(y) for x in ct] for y in ct]
Expected:
    [[0, 1, -1], [-1, 0, -1], [1, 1, 0]]
Got:
    [[0, 1, 1], [-1, 0, 1], [1, 1, 0]]
**********************************************************************
File "/home/wstein/cicero/build/sage-3.1.2/tmp/type_reducible.py", line 55:
    sage: sorted(ct)
Expected:
    [['A', 4], A1xB2, B2xA1]
Got:
    [A1xB2, B2xA1, ['A', 4]]
**********************************************************************
1 items had failures:
   2 of   8 in __main__.example_3
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/wstein/cicero/build/sage-3.1.2/tmp/.doctest_type_reducible.py
         [3.4 s]
```


Cicero is:

```
[wstein@cicero sage-3.1.2]$ cat /etc/issue
Fedora release 8 (Werewolf)
Kernel \r on an \m

[wstein@cicero sage-3.1.2]$ uname -a
Linux cicero 2.6.25.9-40.fc8 #1 SMP Fri Jun 27 16:25:53 EDT 2008 i686 i686 i386 GNU/Linux
[wstein@cicero sage-3.1.2]$ 
```



---

Comment by mabshoff created at 2008-10-26 03:34:23

Resolution: fixed


---

Comment by mabshoff created at 2008-10-26 03:34:23

The problem is gone with Sage 3.1.4 with the system compiler as well as gcc 4.3.2.

Cheers,

Michael
