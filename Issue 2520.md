# Issue 2520: 2.10.4.a0: doctest failures in combinatorics after merging #2489

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-03-14 21:10:40

Assignee: mhansen

CC:  sage-combinat


```
sage -t -long devel/sage-main/sage/libs/symmetrica/kostka.pxi
**********************************************************************
File "kostka.py", line 67:
    sage: symmetrica.kostka_tab([2,1],[1,1,1])
Expected:
    [[[1, 2], [3]], [[1, 3], [2]]]
Got:
    [[[1, 2], [3, None]], [[1, 3], [2, None]]]
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_1
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_kostka.pxi
         [2.2 s]
exit code: 256
```

and

```
sage -t -long devel/sage-main/sage/combinat/tableau.py
**********************************************************************
File "tableau.py", line 1457:
    sage: SST.list()
Expected:
    [[[1, 1], [2]],
     [[1, 1], [3]],
     [[1, 2], [2]],
     [[1, 2], [3]],
     [[1, 3], [2]],
     [[1, 3], [3]],
     [[2, 2], [3]],
     [[2, 3], [3]]]
Got:
    [[[1, 1], [2, None]], [[1, 1], [3, None]], [[1, 2], [2, None]], [[1, 2], [3, None]], [[1, 3], [2, None]], [[1, 3], [3, None]], [[2, 2], [3, None]], [[2, 3], [3, None]]]
**********************************************************************
File "tableau.py", line 1470:
    sage: SST.list()
Expected:
    [This is the Trac macro *[1, 1, 1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[1, 1, 1-macro),
     [This is the Trac macro *1, 1, 2* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1, 1, 2-macro),
     [This is the Trac macro *1, 1, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1, 1, 3-macro),
     [This is the Trac macro *1, 2, 2* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1, 2, 2-macro),
     [This is the Trac macro *1, 2, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1, 2, 3-macro),
     [This is the Trac macro *1, 3, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1, 3, 3-macro),
     [This is the Trac macro *2, 2, 2* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#2, 2, 2-macro),
     [This is the Trac macro *2, 2, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#2, 2, 3-macro),
     [This is the Trac macro *2, 3, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#2, 3, 3-macro),
     [This is the Trac macro *3, 3, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#3, 3, 3-macro),
     [[1, 1], [2]],
     [[1, 1], [3]],
     [[1, 2], [2]],
     [[1, 2], [3]],
     [[1, 3], [2]],
     [[1, 3], [3]],
     [[2, 2], [3]],
     [[2, 3], [3]],
     [[1], [2], [3]]]
Got:
    [This is the Trac macro *[1, 1, 1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[1, 1, 1-macro), [This is the Trac macro *1, 1, 2* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1, 1, 2-macro), [This is the Trac macro *1, 1, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1, 1, 3-macro), [This is the Trac macro *1, 2, 2* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1, 2, 2-macro), [This is the Trac macro *1, 2, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1, 2, 3-macro), [This is the Trac macro *1, 3, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1, 3, 3-macro), [This is the Trac macro *2, 2, 2* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#2, 2, 2-macro), [This is the Trac macro *2, 2, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#2, 2, 3-macro), [This is the Trac macro *2, 3, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#2, 3, 3-macro), [This is the Trac macro *3, 3, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#3, 3, 3-macro), [[1, 1], [2, None]], [[1, 1], [3, None]], [[1, 2], [2, None]], [[1, 2], [3, None]], [[1, 3], [2, None]], [[1, 3], [3, None]], [[2, 2], [3, None]], [[2, 3], [3, None]], [[1], [2], [3]]]
**********************************************************************
File "tableau.py", line 1597:
    sage: all([sst in SST for sst in SST])
Expected:
    True
Got:
    False
**********************************************************************
File "tableau.py", line 1626:
    sage: SemistandardTableaux(3).list()
Expected:
    [This is the Trac macro *[1, 1, 1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[1, 1, 1-macro),
     [This is the Trac macro *1, 1, 2* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1, 1, 2-macro),
     [This is the Trac macro *1, 1, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1, 1, 3-macro),
     [This is the Trac macro *1, 2, 2* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1, 2, 2-macro),
     [This is the Trac macro *1, 2, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1, 2, 3-macro),
     [This is the Trac macro *1, 3, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1, 3, 3-macro),
     [This is the Trac macro *2, 2, 2* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#2, 2, 2-macro),
     [This is the Trac macro *2, 2, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#2, 2, 3-macro),
     [This is the Trac macro *2, 3, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#2, 3, 3-macro),
     [This is the Trac macro *3, 3, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#3, 3, 3-macro),
     [[1, 1], [2]],
     [[1, 1], [3]],
     [[1, 2], [2]],
     [[1, 2], [3]],
     [[1, 3], [2]],
     [[1, 3], [3]],
     [[2, 2], [3]],
     [[2, 3], [3]],
     [[1], [2], [3]]]
Got:
    [This is the Trac macro *[1, 1, 1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[1, 1, 1-macro), [This is the Trac macro *1, 1, 2* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1, 1, 2-macro), [This is the Trac macro *1, 1, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1, 1, 3-macro), [This is the Trac macro *1, 2, 2* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1, 2, 2-macro), [This is the Trac macro *1, 2, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1, 2, 3-macro), [This is the Trac macro *1, 3, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1, 3, 3-macro), [This is the Trac macro *2, 2, 2* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#2, 2, 2-macro), [This is the Trac macro *2, 2, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#2, 2, 3-macro), [This is the Trac macro *2, 3, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#2, 3, 3-macro), [This is the Trac macro *3, 3, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#3, 3, 3-macro), [[1, 1], [2, None]], [[1, 1], [3, None]], [[1, 2], [2, None]], [[1, 2], [3, None]], [[1, 3], [2, None]], [[1, 3], [3, None]], [[2, 2], [3, None]], [[2, 3], [3, None]], [[1], [2], [3]]]
**********************************************************************
File "tableau.py", line 1677:
    sage: all([sst in SST for sst in SST])
Expected:
    True
Got:
    False
**********************************************************************
File "tableau.py", line 1679:
    sage: len(filter(lambda x: x in SST, SemistandardTableaux(3)))
Expected:
    1
Got:
    0
**********************************************************************
File "tableau.py", line 1730:
    sage: SemistandardTableaux([3,2,1], [2, 2, 2]).list()
Expected:
    [[[1, 1, 2], [2, 3], [3]], [[1, 1, 3], [2, 2], [3]]]
Got:
    [[[1, 1, 2], [2, 3, None], [3, None, None]], [[1, 1, 3], [2, 2, None], [3, None, None]]]
**********************************************************************
File "tableau.py", line 1752:
    sage: all([sst in SST for sst in SST])
Expected:
    True
Got:
    False
**********************************************************************
File "tableau.py", line 1754:
    sage: len(filter(lambda x: x in SST, SemistandardTableaux(3)))
Expected:
    8
Got:
    0
**********************************************************************
File "tableau.py", line 1805:
    sage: SemistandardTableaux([2,1]).list()
Expected:
    [[[1, 1], [2]],
     [[1, 1], [3]],
     [[1, 2], [2]],
     [[1, 2], [3]],
     [[1, 3], [2]],
     [[1, 3], [3]],
     [[2, 2], [3]],
     [[2, 3], [3]]]
Got:
    [[[1, 1], [2, None]], [[1, 1], [3, None]], [[1, 2], [2, None]], [[1, 2], [3, None]], [[1, 3], [2, None]], [[1, 3], [3, None]], [[2, 2], [3, None]], [[2, 3], [3, None]]]
**********************************************************************
File "tableau.py", line 1843:
    sage: SemistandardTableaux(3, [2,1]).list()
Expected:
    [This is the Trac macro *[1, 1, 2* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[1, 1, 2-macro), [[1, 1], [2]]]
Got:
    [This is the Trac macro *[1, 1, 2* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[1, 1, 2-macro), [[1, 1], [2, None]]]
**********************************************************************
File "tableau.py", line 1845:
    sage: SemistandardTableaux(4, [2,2]).list()
Expected:
    [This is the Trac macro *[1, 1, 2, 2* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[1, 1, 2, 2-macro), [[1, 1, 2], [2]], [[1, 1], [2, 2]]]
Got:
    [This is the Trac macro *[1, 1, 2, 2* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#[1, 1, 2, 2-macro), [[1, 1, 2], [2, None, None]], [[1, 1], [2, 2]]]
**********************************************************************
File "tableau.py", line 1869:
    sage: all([sst in SST for sst in SST])
Expected:
    True
Got:
    False
**********************************************************************
File "tableau.py", line 1871:
    sage: all([sst in SST for sst in SemistandardTableaux([3,2,1],[2,2,2])])
Expected:
    True
Got:
    False
**********************************************************************
9 items had failures:
   2 of   4 in __main__.example_69
   1 of   4 in __main__.example_75
   1 of   2 in __main__.example_77
   2 of   4 in __main__.example_80
   1 of   4 in __main__.example_82
   2 of   4 in __main__.example_84
   1 of   3 in __main__.example_87
   2 of   2 in __main__.example_90
   2 of   3 in __main__.example_92
***Test Failed*** 14 failures.
For whitespace errors, see the file .doctest_tableau.py
         [3.5 s]
exit code: 256

----------------------------------------------------------------------
The following tests failed:


        sage -t -long devel/sage-main/sage/combinat/tableau.py
Total time for all tests: 3.5 seconds
```



---

Attachment


---

Comment by mabshoff created at 2008-03-14 21:45:03

Patch looks good to me. mhansen explained me the finer details of what the patch does. Doctests pass again.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-14 21:45:48

Merged in Sage 2.10.4.alpha0


---

Comment by mabshoff created at 2008-03-14 21:45:48

Resolution: fixed
