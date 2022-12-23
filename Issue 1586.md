# Issue 1586: preparser.py doctest failures

Issue created by migration from https://trac.sagemath.org/ticket/1586

Original creator: rlm

Original creation time: 2007-12-22 05:19:00

Assignee: was


```
rlmill@sage:~/release/sage-2.9.1.alpha3$ ./sage -t  devel/sage-main/sage/misc/preparser.py
sage -t  devel/sage-main/sage/misc/preparser.py             **********************************************************************
File "preparser.py", line 472:
    sage: preparse("ZZ.<x> = ZZ['x']")   
Expected:
    'ZZ = ZZ["x"]; (x,) = ZZ._first_ngens(Integer(1))'
Got:
    "ZZ = ZZ['x']; (x,) = ZZ._first_ngens(Integer(1))"
**********************************************************************
File "preparser.py", line 474:
    sage: preparse("ZZ.<x> = ZZ['y']")
Expected:
    'ZZ = ZZ["x"]; (x,) = ZZ._first_ngens(Integer(1))'
Got:
    "ZZ = ZZ['y']; (x,) = ZZ._first_ngens(Integer(1))"
**********************************************************************
File "preparser.py", line 476:
    sage: preparse("ZZ.<x,y> = ZZ[]")
Expected:
    'ZZ = ZZ["x, y"]; (x, y,) = ZZ._first_ngens(Integer(2))'
Got:
    "ZZ = ZZ['x, y']; (x, y,) = ZZ._first_ngens(Integer(2))"
**********************************************************************
File "preparser.py", line 478:
    sage: preparse("ZZ.<x,y> = ZZ['u,v']")
Expected:
    'ZZ = ZZ["x, y"]; (x, y,) = ZZ._first_ngens(Integer(2))'
Got:
    "ZZ = ZZ['u,v']; (x, y,) = ZZ._first_ngens(Integer(2))"
**********************************************************************
File "preparser.py", line 480:
    sage: preparse("ZZ.<x> = QQ[2^(1/3)]")
Expected:
    'ZZ = QQ["x"]; (x,) = ZZ._first_ngens(Integer(1))'
Got:
    'ZZ = QQ[Integer(2)**(Integer(1)/Integer(3))]; (x,) = ZZ._first_ngens(Integer(1))'
**********************************************************************
1 items had failures:
   5 of   6 in __main__.example_6
***Test Failed*** 5 failures.
For whitespace errors, see the file .doctest_preparser.py
         [2.7 s]
exit code: 256

----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage-main/sage/misc/preparser.py
Total time for all tests: 2.7 seconds
rlmill@sage:~/release/sage-2.9.1.alpha3$ 
```



---

Comment by rlm created at 2007-12-22 10:10:55

http://sage.math.washington.edu/home/rlmill/release/merged-sage-2.9.1.rc0/fix_preparser_doctests.patch


---

Comment by rlm created at 2007-12-22 10:11:05

Resolution: fixed
