# Issue 4386: Sage 3.1.4: optional doctest failure in sage/rings/number_field/totallyreal_phc.py

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-10-30 04:19:15

Assignee: mhampton

CC:  craigcitro jvoight


```
sage -t -long -optional devel/sage/sage/rings/number_field/totallyreal_phc.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/totallyreal_phc.py", line 86:
    sage: __lagrange_bounds_phc(3,5,[8,1,2,0,1],tmpfile='phc') # optional
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[2]>", line 1, in <module>
        __lagrange_bounds_phc(Integer(3),Integer(5),[Integer(8),Integer(1),Integer(2),Integer(0),Integer(1)],tmpfile='phc') # optional###line 86:
    sage: __lagrange_bounds_phc(3,5,[8,1,2,0,1],tmpfile='phc') # optional
    NameError: name '__lagrange_bounds_phc' is not defined
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/totallyreal_phc.py", line 89:
    sage: __lagrange_bounds_phc(3,2,[8,1,2,0,1],tmpfile='phc') # optional
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[3]>", line 1, in <module>
        __lagrange_bounds_phc(Integer(3),Integer(2),[Integer(8),Integer(1),Integer(2),Integer(0),Integer(1)],tmpfile='phc') # optional###line 89:
    sage: __lagrange_bounds_phc(3,2,[8,1,2,0,1],tmpfile='phc') # optional
    NameError: name '__lagrange_bounds_phc' is not defined
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/totallyreal_phc.py", line 92:
    sage: __lagrange_bounds_phc(3,1,[8,1,2,0,1],tmpfile='phc') # optional
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[4]>", line 1, in <module>
        __lagrange_bounds_phc(Integer(3),Integer(1),[Integer(8),Integer(1),Integer(2),Integer(0),Integer(1)],tmpfile='phc') # optional###line 92:
    sage: __lagrange_bounds_phc(3,1,[8,1,2,0,1],tmpfile='phc') # optional
    NameError: name '__lagrange_bounds_phc' is not defined
**********************************************************************
1 items had failures:
   3 of   5 in __main__.example_2
***Test Failed*** 3 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/.doctest_totallyreal_phc.py
	 [2.0 s]
exit code: 1024
```



---

Comment by mabshoff created at 2008-10-30 05:24:25

Craig's patch exposes the next problem:

```
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/totallyreal_phc.py", line 87:
    sage: __lagrange_bounds_phc(3,5,[8,1,2,0,1],tmpfile='phc') # optional
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[3]>", line 1, in <module>
        __lagrange_bounds_phc(Integer(3),Integer(5),[Integer(8),Integer(1),Integer(2),Integer(0),Integer(1)],tmpfile='phc') # optional###line 87:
    sage: __lagrange_bounds_phc(3,5,[8,1,2,0,1],tmpfile='phc') # optional
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/site-packages/sage/rings/number_field/totallyreal_phc.py", line 118, in __lagrange_bounds_phc
        for P in sage.combinat.combinat.partitions_list(n-1,m-1):
    AttributeError: 'module' object has no attribute 'partitions_list'
**********************************************************************
```

mhansen pointed out in IRC:

```
[9:13pm] mhansen: partitions_list should be deprecated.  Partitions(n).list() 
should be used if you want a list otherwise Partitions(n) provides an __iter__
```


Cheers,

Michael


---

Attachment


---

Comment by craigcitro created at 2008-10-30 07:25:08

Much better patch attached.


---

Comment by craigcitro created at 2008-10-30 07:25:08

Changing assignee from mhampton to craigcitro.


---

Comment by craigcitro created at 2008-10-30 07:25:08

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-10-30 07:34:02

Better patch, but still some trouble:

```
sage -t -long -optional devel/sage/sage/rings/number_field/totallyreal_phc.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/totallyreal_phc.py", line 91:
    sage: x, y = __lagrange_bounds_phc(3,2,[8,1,2,0,1]) # optional
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[4]>", line 1, in <module>
        x, y = __lagrange_bounds_phc(Integer(3),Integer(2),[Integer(8),Integer(1),Integer(2),Integer(0),Integer(1)]) # optional###line 91:
    sage: x, y = __lagrange_bounds_phc(3,2,[8,1,2,0,1]) # optional
    ValueError: need more than 0 values to unpack
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/totallyreal_phc.py", line 92:
    e: x # optional
Expected:
    -1.3333333333333299
Got:
    x
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/totallyreal_phc.py", line 94:
    e: y < 0.00000001 # optional
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.1.3.final/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[6]>", line 1, in <module>
        y < RealNumber('0.00000001') # optional###line 94:
    e: y < 0.00000001 # optional
    NameError: name 'y' is not defined
**********************************************************************
1 items had failures:
   3 of   8 in __main__.example_2
***Test Failed*** 3 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/.doctest_totallyreal_phc.py
	 [2.4 s]
exit code: 1024
```


Cheers,

Michael


---

Attachment


---

Comment by craigcitro created at 2008-10-31 04:50:50

Second patch added, which *should* fix the issue.


---

Comment by mabshoff created at 2008-10-31 05:26:02

Positive review. With both patches applied the issue is resolved:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.1.3.final$ ./sage -t -optional -long devel/sage/sage/rings/number_field/totallyreal_phc.py
sage -t -optional -long devel/sage/sage/rings/number_field/totallyreal_phc.py
	 [2.4 s]
 
----------------------------------------------------------------------
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-10-31 05:27:19

Merged both patches in Sage 3.2.alpha2


---

Comment by mabshoff created at 2008-10-31 05:27:19

Resolution: fixed
