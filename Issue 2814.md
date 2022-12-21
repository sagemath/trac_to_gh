# Issue 2814: sage-3.0-alpha1 on ppc -- new randstate code doesn't work right at all

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-05 20:01:31

Assignee: cwitty

Various examples to illustrate the problems:

The new randstate stuff is massively broken on ppc, evidently:

```
sage -t  devel/sage/sage/misc/randstate.pyx
**********************************************
************************
File "/Users/was/build/sage-3.0.alpha1/tmp/randstate.py", line 47:
   : rtest()
Expected:
   (303, -0.187141682737491, 1/2*x^2 - 1/95*x - 1/2, (1,2),
1698070399, 8045, 0.96619117347084138)
Got:
   (303, -0.187141682737491, 1/2*x^2 - 1/95*x - 1/2, (1,2)(4,5),
1698070399, 8045, 0.96619117347084138)
**********************************************************************
File "/Users/was/build/sage-3.0.alpha1/tmp/randstate.py", line 50:
   : rtest()
Expected:
   (978, 0.184109262667515, -3*x^2 - 1/12, (2,3), 1046254370, 60359,
0.83350776541997362)
Got:
   (978, 0.184109262667515, -3*x^2 - 1/12, (1,2,3), 1046254370,
60359, 0.83350776541997362)
**********************************************************************
File "/Users/was/build/sage-3.0.alpha1/tmp/randstate.py", line 53:
   : rtest()
Expected:
   (207, 0.505364206568040, 4*x^2 + 1/2, (1,2)(4,5), 2137873234,
27695, 0.19982565117278328)
Got:
   (207, 0.505364206568040, 4*x^2 + 1/2, (4,5), 2137873234, 27695,
0.19982565117278328)
**********************************************************************
File "/Users/was/build/sage-3.0.alpha1/tmp/randstate.py", line 56:
   : rtest()
Expected:
   (303, -0.187141682737491, 1/2*x^2 - 1/95*x - 1/2, (1,2),
1698070399, 8045, 0.96619117347084138)
Got:
   (303, -0.187141682737491, 1/2*x^2 - 1/95*x - 1/2, (1,2)(4,5),
1698070399, 8045, 0.96619117347084138)
**********************************************************************
File "/Users/was/build/sage-3.0.alpha1/tmp/randstate.py", line 59:
   : rtest()
Expected:
   (978, 0.184109262667515, -3*x^2 - 1/12, (2,3), 1046254370, 60359,
0.83350776541997362)
Got:
   (978, 0.184109262667515, -3*x^2 - 1/12, (1,2,3), 1046254370,
60359, 0.83350776541997362)
**********************************************************************
File "/Users/was/build/sage-3.0.alpha1/tmp/randstate.py", line 62:
   : rtest()
Expected:
   (207, 0.505364206568040, 4*x^2 + 1/2, (1,2)(4,5), 2137873234,
27695, 0.19982565117278328)
Got:
   (207, 0.505364206568040, 4*x^2 + 1/2, (4,5), 2137873234, 27695,
0.19982565117278328)
**********************************************************************
File "/Users/was/build/sage-3.0.alpha1/tmp/randstate.py", line 72:
   : rtest()
Expected:
   (720, 0.0216737401150802, x^2 - x, (), 1506569166, 14005,
0.92053315995181839)
Got:
   (720, 0.0216737401150802, x^2 - x, (1,3,2)(4,5), 1506569166,
14005, 0.92053315995181839)
**********************************************************************
File "/Users/was/build/sage-3.0.alpha1/tmp/randstate.py", line 206:
   : r1 = rtest(); r1
Expected:
   (303, -0.187141682737491, 1/2*x^2 - 1/95*x - 1/2, (1,2),
1698070399, 8045, 0.96619117347084138)
Got:
   (303, -0.187141682737491, 1/2*x^2 - 1/95*x - 1/2, (1,2)(4,5),
1698070399, 8045, 0.96619117347084138)
**********************************************************************
**********************************************************************
File "/Users/was/build/sage-3.0.alpha1/tmp/randstate.py", line 208:
   : r2 = rtest(); r2
Expected:
   (105, -0.581229341007821, -x^2 - x - 6, (1,3,2)(4,5), 697338742,
1271, 0.001767155077382232)
Got:
   (105, -0.581229341007821, -x^2 - x - 6, (2,3), 697338742, 1271,
0.001767155077382232)
**********************************************************************
File "/Users/was/build/sage-3.0.alpha1/tmp/randstate.py", line 216:
   : with seed(1): rtest()
Expected:
   (978, 0.184109262667515, -3*x^2 - 1/12, (2,3), 1046254370, 60359,
0.83350776541997362)
Got:
   (978, 0.184109262667515, -3*x^2 - 1/12, (1,2,3), 1046254370,
60359, 0.83350776541997362)
**********************************************************************
File "/Users/was/build/sage-3.0.alpha1/tmp/randstate.py", line 218:
   : r2m = rtest(); r2m
Expected:
   (105, -0.581229341007821, -x^2 - x - 6, (1,3,2)(4,5), 697338742,
19769, 0.001767155077382232)
Got:
   (105, -0.581229341007821, -x^2 - x - 6, (2,3), 697338742, 19769,
0.001767155077382232)
**********************************************************************
File "/Users/was/build/sage-3.0.alpha1/tmp/randstate.py", line 233:
   : with seed(1): (rtest(), rtest())
Expected:
   ((978, 0.184109262667515, -3*x^2 - 1/12, (2,3), 1046254370, 60359,
0.83350776541997362), (138, -0.2475
78366457583, 2*x - 24, (), 1077419109, 10234, 0.0033332230808060803))
Got:
   ((978, 0.184109262667515, -3*x^2 - 1/12, (1,2,3), 1046254370,
60359, 0.83350776541997362), (138, -0.24
7578366457583, 2*x - 24, (4,5), 1077419109, 10234, 0.0033332230808060803))
**********************************************************************
File "/Users/was/build/sage-3.0.alpha1/tmp/randstate.py", line 248:
   : try:
         ctx.__enter__()
         rtest()
   finally:
         ctx.__exit__(None, None, None)
Expected:
   <sage.misc.randstate.randstate object at 0x...>
   (978, 0.184109262667515, -3*x^2 - 1/12, (2,3), 1046254370, 60359,
0.83350776541997362)
   False
Got:
   <sage.misc.randstate.randstate object at 0x6e258a0>
   (978, 0.184109262667515, -3*x^2 - 1/12, (1,2,3), 1046254370,
60359, 0.83350776541997362)
   False
**********************************************************************
File "/Users/was/build/sage-3.0.alpha1/tmp/randstate.py", line 629:
   sage: gap.Random(1, 10^50)
Expected:
   24922966241004817547714978350347109473543873184564
Got:
   97144566318213989637952954803537490912828430192472
**********************************************************************
2 items had failures:
 13 of  60 in __main__.example_0
  1 of   4 in __main__.example_10
***Test Failed*** 14 failures.
For whitespace errors, see the file
/Users/was/build/sage-3.0.alpha1/tmp/.doctest_randstate.py
        [19.4 s]
```



More stuff probably related to random stuff.

```
        [16.6 s]sage -t  devel/sage/sage/groups/perm_gps/permgroup.py
     **********************************************************************
File "/Users/was/build/sage-3.0.alpha1/tmp/permgroup.py", line 709:
   sage: G.random_element()
Expected:
   (1,2)(4,5)
Got:    (2,3)
**********************************************************************
File "/Users/was/build/sage-3.0.alpha1/tmp/permgroup.py", line 1270:
   sage: g = G.random_element(); g
Expected:
   (1,3)
Got:
   (1,2)(3,4)
**********************************************************************
File "/Users/was/build/sage-3.0.alpha1/tmp/permgroup.py", line 1272:
   sage: G.normalizer(g)
Expected:
   Group( [ (1,3), (2,4) ] )
Got:
   Group( [ (1,2)(3,4), (1,4)(2,3) ] )
**********************************************************************
2 items had failures:
  1 of   3 in __main__.example_22
  2 of   6 in __main__.example_39
***Test Failed*** 3 failures.
For whitespace errors, see the file
/Users/was/build/sage-3.0.alpha1/tmp/.doctest_permgroup.py
        [19.1 s]
```



No clue:

```
sage -t  devel/sage/sage/groups/matrix_gps/unitary.py
**********************************************
************************
File "/Users/was/build/sage-3.0.alpha1/tmp/unitary.py", line 21:
   sage: G.random()
Expected:
   [    3*a     2*a 4*a + 3]
   [      3 2*a + 4     3*a]
   [4*a + 1 4*a + 1 3*a + 2]
Got:
   [      4 2*a + 4     2*a]
   [3*a + 3   a + 1   a + 3]
   [2*a + 2   a + 1 3*a + 1]
**********************************************************************
1 items had failures:
  1 of   8 in __main__.example_0
***Test Failed*** 1 failures.
```




```
sage -t  devel/sage/sage/groups/matrix_gps/symplectic.py
**********************************************
************************
File "/Users/was/build/sage-3.0.alpha1/tmp/symplectic.py", line 14:
   sage: G.random()
Expected:
   [1 0 5 6]
   [0 5 2 4]
   [4 0 2 3]
   [3 6 2 0]
Got:
   [4 6 2 0]
   [2 5 4 0]
   [3 3 5 1]
   [2 0 5 5]
**********************************************************************
1 items had failures:
  1 of   6 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file
/Users/was/build/sage-3.0.alpha1/tmp/.doctest_symplectic.py
        [7.0 s]
```




```
File "/Users/was/build/sage-3.0.alpha1/tmp/orthogonal.py", line 212:
 sage: GO( 3, GF(7), 0).random()
Expected:
   [3 2 1]
   [4 0 0]
   [6 0 1]Got:
   [1 5 3]
   [0 1 0]
   [0 6 6]
**********************************************************************
File "/Users/was/build/sage-3.0.alpha1/tmp/orthogonal.py", line 120:
   sage: G.random()
Expected:
   [2 5 1 1]
   [3 0 0 0]
   [0 0 3 5]
   [2 0 4 4]
Got:
   [3 4 5 2]
   [1 5 2 5]
   [6 4 6 2]
   [2 6 4 2]
**********************************************************************
2 items had failures:
  1 of   4 in __main__.example_10
  1 of   4 in __main__.example_4
***Test Failed*** 2 failures.
For whitespace errors, see the file
/Users/was/build/sage-3.0.alpha1/tmp/.doctest_orthogonal.py
        [7.9 s]
sage -t  devel/sage/sage/groups/matrix_gps/special_linear.py
```




```
sage -t  devel/sage/sage/groups/matrix_gps/matrix_group.py
**********************************************
************************ File
"/Users/was/build/sage-3.0.alpha1/tmp/matrix_group.py", line 448:
sage: G.random()Expected:    [2 1 1 1]    [1 0 2 1]
   [0 1 1 0]
   [1 0 0 1]
Got:
   [1 1 0 1]    [2 1 1 1]
   [1 2 1 0]
   [1 1 2 0]
**********************************************************************
File "/Users/was/build/sage-3.0.alpha1/tmp/matrix_group.py", line 457:
   sage: G.random()
Expected:
   [1 3]
   [0 3]
Got:
   [2 3]
   [0 1]
**********************************************************************
File "/Users/was/build/sage-3.0.alpha1/tmp/matrix_group.py", line 460:
   sage: G.random()
Expected:
   [2 2]
   [1 0]
Got:
   [4 1]
   [1 2]
**********************************************************************
File "/Users/was/build/sage-3.0.alpha1/tmp/matrix_group.py", line 463:
   sage: G.random()
Expected:
   [4 0]
   [1 4]
Got:
   [4 4]
   [2 0]
**********************************************************************
1 items had failures:
  4 of   9 in __main__.example_17
***Test Failed*** 4 failures.
```



---

Attachment


---

Comment by cwitty created at 2008-04-10 03:02:12

Changing status from new to assigned.


---

Comment by cwitty created at 2008-04-10 03:02:12

I believe that the two patches fix all of the issues in this ticket.  With the patches, sage -testall passes on 32-bit x86, but they have NOT BEEN TESTED on PPC at all, so somebody needs to do that.


---

Comment by mabshoff created at 2008-04-10 13:15:27

Applying both patches to my PPC test build does not fix the issue:

```
sage -t  devel/sage-main/sage/rings/complex_double.pyx
**********************************************************************
File "/Users/mabshoff/sage-3.0.alpha3/tmp/complex_double.py", line 179:
    sage: CDF.random_element()
Expected:
    -0.436810529675 + 0.736945423566*I
Got:
    0.736945423566 - 0.436810529675*I
**********************************************************************
File "/Users/mabshoff/sage-3.0.alpha3/tmp/complex_double.py", line 181:
    sage: CDF.random_element(-10,10,-10,10)
Expected:
    -7.08874026302 - 9.54135400334*I
Got:
    -9.54135400334 - 7.08874026302*I
**********************************************************************
File "/Users/mabshoff/sage-3.0.alpha3/tmp/complex_double.py", line 183:
    sage: CDF.random_element(-10^20,10^20,-2,2)
Expected:
    -7.58765473764e+19 + 0.925549022839*I
Got:
    4.62774511419e+19 - 1.51753094753*I
**********************************************************************
1 items had failures:
   3 of   4 in __main__.example_7
***Test Failed*** 3 failures.
For whitespace errors, see the file /Users/mabshoff/sage-3.0.alpha3/tmp/.doctest_complex_double.py
```

misc/randstate.pyx:

```
----------------------------------------------------------------------
sage -t  devel/sage-main/sage/misc/randstate.pyx
**********************************************************************
File "/Users/mabshoff/sage-3.0.alpha3/tmp/randstate.py", line 47:
    : rtest()
Expected:
    (303, -0.187141682737491, 1/2*x^2 - 1/95*x - 1/2, (1,2), 1698070399, 8045, 0.96619117347084138)
Got:
    (303, -0.187141682737491, 1/2*x^2 - 1/95*x - 1/2, (1,2)(4,5), 1698070399, 8045, 0.96619117347084138)
**********************************************************************
File "/Users/mabshoff/sage-3.0.alpha3/tmp/randstate.py", line 50:
    : rtest()
Expected:
    (978, 0.184109262667515, -3*x^2 - 1/12, (2,3), 1046254370, 60359, 0.83350776541997362)
Got:
    (978, 0.184109262667515, -3*x^2 - 1/12, (1,2,3), 1046254370, 60359, 0.83350776541997362)
**********************************************************************
File "/Users/mabshoff/sage-3.0.alpha3/tmp/randstate.py", line 53:
    : rtest()
Expected:
    (207, 0.505364206568040, 4*x^2 + 1/2, (1,2)(4,5), 2137873234, 27695, 0.19982565117278328)
Got:
    (207, 0.505364206568040, 4*x^2 + 1/2, (4,5), 2137873234, 27695, 0.19982565117278328)
**********************************************************************
File "/Users/mabshoff/sage-3.0.alpha3/tmp/randstate.py", line 56:
    : rtest()
Expected:
    (303, -0.187141682737491, 1/2*x^2 - 1/95*x - 1/2, (1,2), 1698070399, 8045, 0.96619117347084138)
Got:
    (303, -0.187141682737491, 1/2*x^2 - 1/95*x - 1/2, (1,2)(4,5), 1698070399, 8045, 0.96619117347084138)
**********************************************************************
File "/Users/mabshoff/sage-3.0.alpha3/tmp/randstate.py", line 59:
    : rtest()
Expected:
    (978, 0.184109262667515, -3*x^2 - 1/12, (2,3), 1046254370, 60359, 0.83350776541997362)
Got:
    (978, 0.184109262667515, -3*x^2 - 1/12, (1,2,3), 1046254370, 60359, 0.83350776541997362)
**********************************************************************
File "/Users/mabshoff/sage-3.0.alpha3/tmp/randstate.py", line 62:
    : rtest()
Expected:
    (207, 0.505364206568040, 4*x^2 + 1/2, (1,2)(4,5), 2137873234, 27695, 0.19982565117278328)
Got:
    (207, 0.505364206568040, 4*x^2 + 1/2, (4,5), 2137873234, 27695, 0.19982565117278328)
**********************************************************************
File "/Users/mabshoff/sage-3.0.alpha3/tmp/randstate.py", line 72:
    : rtest()
Expected:
    (720, 0.0216737401150802, x^2 - x, (), 1506569166, 14005, 0.92053315995181839)
Got:
    (720, 0.0216737401150802, x^2 - x, (1,3,2)(4,5), 1506569166, 14005, 0.92053315995181839)
**********************************************************************
File "/Users/mabshoff/sage-3.0.alpha3/tmp/randstate.py", line 206:
    : r1 = rtest(); r1
Expected:
    (303, -0.187141682737491, 1/2*x^2 - 1/95*x - 1/2, (1,2), 1698070399, 8045, 0.96619117347084138)
Got:
    (303, -0.187141682737491, 1/2*x^2 - 1/95*x - 1/2, (1,2)(4,5), 1698070399, 8045, 0.96619117347084138)
**********************************************************************
File "/Users/mabshoff/sage-3.0.alpha3/tmp/randstate.py", line 208:
    : r2 = rtest(); r2
Expected:
    (105, -0.581229341007821, -x^2 - x - 6, (1,3,2)(4,5), 697338742, 1271, 0.001767155077382232)
Got:
    (105, -0.581229341007821, -x^2 - x - 6, (2,3), 697338742, 1271, 0.001767155077382232)
**********************************************************************
File "/Users/mabshoff/sage-3.0.alpha3/tmp/randstate.py", line 216:
    : with seed(1): rtest()
Expected:
    (978, 0.184109262667515, -3*x^2 - 1/12, (2,3), 1046254370, 60359, 0.83350776541997362)
Got:
    (978, 0.184109262667515, -3*x^2 - 1/12, (1,2,3), 1046254370, 60359, 0.83350776541997362)
**********************************************************************
File "/Users/mabshoff/sage-3.0.alpha3/tmp/randstate.py", line 218:
    : r2m = rtest(); r2m
Expected:
    (105, -0.581229341007821, -x^2 - x - 6, (1,3,2)(4,5), 697338742, 19769, 0.001767155077382232)
Got:
    (105, -0.581229341007821, -x^2 - x - 6, (2,3), 697338742, 19769, 0.001767155077382232)
**********************************************************************
File "/Users/mabshoff/sage-3.0.alpha3/tmp/randstate.py", line 233:
    : with seed(1): (rtest(), rtest())
Expected:
    ((978, 0.184109262667515, -3*x^2 - 1/12, (2,3), 1046254370, 60359, 0.83350776541997362), (138, -0.247578366457583, 2*x - 24, (), 1077419109, 10234, 0.0033332230808060803))
Got:
    ((978, 0.184109262667515, -3*x^2 - 1/12, (1,2,3), 1046254370, 60359, 0.83350776541997362), (138, -0.247578366457583, 2*x - 24, (4,5), 1077419109, 10234, 0.0033332230808060803))
**********************************************************************
File "/Users/mabshoff/sage-3.0.alpha3/tmp/randstate.py", line 248:
    : try:
          ctx.__enter__()
          rtest()
    finally:
          ctx.__exit__(None, None, None)
Expected:
    <sage.misc.randstate.randstate object at 0x...>
    (978, 0.184109262667515, -3*x^2 - 1/12, (2,3), 1046254370, 60359, 0.83350776541997362)
    False
Got:
    <sage.misc.randstate.randstate object at 0x7032e40>
    (978, 0.184109262667515, -3*x^2 - 1/12, (1,2,3), 1046254370, 60359, 0.83350776541997362)
    False
**********************************************************************
File "/Users/mabshoff/sage-3.0.alpha3/tmp/randstate.py", line 630:
    sage: gap.Random(1, 10^50)
Expected:
    24922966241004817547714978350347109473543873184564
Got:
    97144566318213989637952954803537490912828430192472
**********************************************************************
2 items had failures:
  13 of  60 in __main__.example_0
   1 of   4 in __main__.example_10
***Test Failed*** 14 failures.
For whitespace errors, see the file /Users/mabshoff/sage-3.0.alpha3/tmp/.doctest_randstate.py
```

groups/perm_gps/permgroup.py:

```
----------------------------------------------------------------------
sage -t  devel/sage-main/sage/groups/perm_gps/permgroup.py
**********************************************************************
File "/Users/mabshoff/sage-3.0.alpha3/tmp/permgroup.py", line 709:
    sage: G.random_element()
Expected:
    (1,2)(4,5)
Got:
    (2,3)
**********************************************************************
File "/Users/mabshoff/sage-3.0.alpha3/tmp/permgroup.py", line 1270:
    sage: g = G.random_element(); g
Expected:
    (1,3)
Got:
    (1,2)(3,4)
**********************************************************************
File "/Users/mabshoff/sage-3.0.alpha3/tmp/permgroup.py", line 1272:
    sage: G.normalizer(g)
Expected:
    Group( [ (1,3), (2,4) ] )
Got:
    Group( [ (1,2)(3,4), (1,4)(2,3) ] )
**********************************************************************
```

groups/matrix_gps/unitary.py:

```
----------------------------------------------------------------------
sage -t  devel/sage-main/sage/groups/matrix_gps/unitary.py
**********************************************************************
File "/Users/mabshoff/sage-3.0.alpha3/tmp/unitary.py", line 21:
    sage: G.random()
Expected:
    [    3*a     2*a 4*a + 3]
    [      3 2*a + 4     3*a]
    [4*a + 1 4*a + 1 3*a + 2]
Got:
    [      4 2*a + 4     2*a]
    [3*a + 3   a + 1   a + 3]
    [2*a + 2   a + 1 3*a + 1]
**********************************************************************
```

groups/matrix_gps/symplectic.py:

```
----------------------------------------------------------------------
sage -t  devel/sage-main/sage/groups/matrix_gps/symplectic.py
**********************************************************************
File "/Users/mabshoff/sage-3.0.alpha3/tmp/symplectic.py", line 14:
    sage: G.random()
Expected:
    [1 0 5 6]
    [0 5 2 4]
    [4 0 2 3]
    [3 6 2 0]
Got:
    [4 6 2 0]
    [2 5 4 0]
    [3 3 5 1]
    [2 0 5 5]
**********************************************************************
```

groups/matrix_gps/orthogonal.py:

```
----------------------------------------------------------------------
sage -t  devel/sage-main/sage/groups/matrix_gps/orthogonal.py
**********************************************************************
File "/Users/mabshoff/sage-3.0.alpha3/tmp/orthogonal.py", line 212:
    sage: GO( 3, GF(7), 0).random()
Expected:
    [3 2 1]
    [4 0 0]
    [6 0 1]
Got:
    [1 5 3]
    [0 1 0]
    [0 6 6]
**********************************************************************
File "/Users/mabshoff/sage-3.0.alpha3/tmp/orthogonal.py", line 120:
    sage: G.random()
Expected:
    [2 5 1 1]
    [3 0 0 0]
    [0 0 3 5]
    [2 0 4 4]
Got:
    [3 4 5 2]
    [1 5 2 5]
    [6 4 6 2]
    [2 6 4 2]
**********************************************************************
```

groups/matrix_gps/matrix_group.py:

```
----------------------------------------------------------------------
sage -t  devel/sage-main/sage/groups/matrix_gps/matrix_group.py
**********************************************************************
File "/Users/mabshoff/sage-3.0.alpha3/tmp/matrix_group.py", line 448:
    sage: G.random()
Expected:
    [2 1 1 1]
    [1 0 2 1]
    [0 1 1 0]
    [1 0 0 1]
Got:
    [1 1 0 1]
    [2 1 1 1]
    [1 2 1 0]
    [1 1 2 0]
**********************************************************************
File "/Users/mabshoff/sage-3.0.alpha3/tmp/matrix_group.py", line 457:
    sage: G.random()
Expected:
    [1 3]
    [0 3]
Got:
    [2 3]
    [0 1]
**********************************************************************
File "/Users/mabshoff/sage-3.0.alpha3/tmp/matrix_group.py", line 460:
    sage: G.random()
Expected:
    [2 2]
    [1 0]
Got:
    [4 1]
    [1 2]
**********************************************************************
File "/Users/mabshoff/sage-3.0.alpha3/tmp/matrix_group.py", line 463:
    sage: G.random()
Expected:
    [4 0]
    [1 4]
Got:
    [4 4]
    [2 0]
**********************************************************************
```



---

Comment by mabshoff created at 2008-04-10 19:14:04

With a clean build all tests pass now:

```
fermat:sage-3.0.alpha3 mabshoff$ uname -a
Darwin fermat.math.harvard.edu 9.2.0 Darwin Kernel Version 9.2.0: Tue Feb  5 16:15:19 PST 2008; root:xnu-1228.3.13~1/RELEASE_PPC Power Macintosh

fermat:sage-3.0.alpha3 mabshoff$ ./sage -t  devel/sage-main/sage/rings/complex_double.pyx
Global iterations: 1
File iterations: 1
TeX files: 0

----------------------------------------------------------------------
sage -t  devel/sage-main/sage/rings/complex_double.pyx
         [7.6 s]
All tests passed!
Total time for all tests: 7.6 seconds

fermat:sage-3.0.alpha3 mabshoff$ ./sage -t  devel/sage-main/sage/misc/randstate.pyx
Global iterations: 1
File iterations: 1
TeX files: 0

----------------------------------------------------------------------
sage -t  devel/sage-main/sage/misc/randstate.pyx
         [20.8 s]
All tests passed!
Total time for all tests: 20.8 seconds

fermat:sage-3.0.alpha3 mabshoff$ ./sage -t  devel/sage-main/sage/groups/perm_gps/permgroup.py
Global iterations: 1
File iterations: 1
TeX files: 0

----------------------------------------------------------------------

sage -t  devel/sage-main/sage/groups/perm_gps/permgroup.py
         [19.0 s]
All tests passed!
Total time for all tests: 19.0 seconds
fermat:sage-3.0.alpha3 mabshoff$
fermat:sage-3.0.alpha3 mabshoff$ sage -t  devel/sage-main/sage/groups/matrix_gps/unitary.py
Global iterations: 1
File iterations: 1
TeX files: 0

----------------------------------------------------------------------

sage -t  devel/sage-main/sage/groups/matrix_gps/unitary.py
         [8.8 s]
All tests passed!
Total time for all tests: 8.8 seconds
fermat:sage-3.0.alpha3 mabshoff$
fermat:sage-3.0.alpha3 mabshoff$ ./sage -t  devel/sage-main/sage/groups/matrix_gps/symplectic.py
Global iterations: 1
File iterations: 1
TeX files: 0

----------------------------------------------------------------------

sage -t  devel/sage-main/sage/groups/matrix_gps/symplectic.py
         [7.2 s]
All tests passed!
Total time for all tests: 7.2 seconds
fermat:sage-3.0.alpha3 mabshoff$
fermat:sage-3.0.alpha3 mabshoff$ ./sage -t  devel/sage-main/sage/groups/matrix_gps/orthogonal.py
Global iterations: 1
File iterations: 1
TeX files: 0

----------------------------------------------------------------------

sage -t  devel/sage-main/sage/groups/matrix_gps/orthogonal.py
         [8.2 s]
All tests passed!
Total time for all tests: 8.2 seconds
fermat:sage-3.0.alpha3 mabshoff$
fermat:sage-3.0.alpha3 mabshoff$ ./sage -t  devel/sage-main/sage/groups/matrix_gps/matrix_group.py
Global iterations: 1
File iterations: 1
TeX files: 0

----------------------------------------------------------------------

sage -t  devel/sage-main/sage/groups/matrix_gps/matrix_group.py
         [69.5 s]
All tests passed!
Total time for all tests: 69.5 seconds 
```


Positive review. I also tested on sage.math [x86-64] and it works there.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-10 19:14:49

Resolution: fixed


---

Comment by mabshoff created at 2008-04-10 19:14:49

Merged in Sage 3.0.alpha4
