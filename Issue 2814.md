# Issue 2814: sage-3.0-alpha1 on ppc -- new randstate code doesn't work right at all

archive/issues_002814.json:
```json
{
    "body": "Assignee: cwitty\n\nVarious examples to illustrate the problems:\n\nThe new randstate stuff is massively broken on ppc, evidently:\n\n```\nsage -t  devel/sage/sage/misc/randstate.pyx\n**********************************************\n************************\nFile \"/Users/was/build/sage-3.0.alpha1/tmp/randstate.py\", line 47:\n   : rtest()\nExpected:\n   (303, -0.187141682737491, 1/2*x^2 - 1/95*x - 1/2, (1,2),\n1698070399, 8045, 0.96619117347084138)\nGot:\n   (303, -0.187141682737491, 1/2*x^2 - 1/95*x - 1/2, (1,2)(4,5),\n1698070399, 8045, 0.96619117347084138)\n**********************************************************************\nFile \"/Users/was/build/sage-3.0.alpha1/tmp/randstate.py\", line 50:\n   : rtest()\nExpected:\n   (978, 0.184109262667515, -3*x^2 - 1/12, (2,3), 1046254370, 60359,\n0.83350776541997362)\nGot:\n   (978, 0.184109262667515, -3*x^2 - 1/12, (1,2,3), 1046254370,\n60359, 0.83350776541997362)\n**********************************************************************\nFile \"/Users/was/build/sage-3.0.alpha1/tmp/randstate.py\", line 53:\n   : rtest()\nExpected:\n   (207, 0.505364206568040, 4*x^2 + 1/2, (1,2)(4,5), 2137873234,\n27695, 0.19982565117278328)\nGot:\n   (207, 0.505364206568040, 4*x^2 + 1/2, (4,5), 2137873234, 27695,\n0.19982565117278328)\n**********************************************************************\nFile \"/Users/was/build/sage-3.0.alpha1/tmp/randstate.py\", line 56:\n   : rtest()\nExpected:\n   (303, -0.187141682737491, 1/2*x^2 - 1/95*x - 1/2, (1,2),\n1698070399, 8045, 0.96619117347084138)\nGot:\n   (303, -0.187141682737491, 1/2*x^2 - 1/95*x - 1/2, (1,2)(4,5),\n1698070399, 8045, 0.96619117347084138)\n**********************************************************************\nFile \"/Users/was/build/sage-3.0.alpha1/tmp/randstate.py\", line 59:\n   : rtest()\nExpected:\n   (978, 0.184109262667515, -3*x^2 - 1/12, (2,3), 1046254370, 60359,\n0.83350776541997362)\nGot:\n   (978, 0.184109262667515, -3*x^2 - 1/12, (1,2,3), 1046254370,\n60359, 0.83350776541997362)\n**********************************************************************\nFile \"/Users/was/build/sage-3.0.alpha1/tmp/randstate.py\", line 62:\n   : rtest()\nExpected:\n   (207, 0.505364206568040, 4*x^2 + 1/2, (1,2)(4,5), 2137873234,\n27695, 0.19982565117278328)\nGot:\n   (207, 0.505364206568040, 4*x^2 + 1/2, (4,5), 2137873234, 27695,\n0.19982565117278328)\n**********************************************************************\nFile \"/Users/was/build/sage-3.0.alpha1/tmp/randstate.py\", line 72:\n   : rtest()\nExpected:\n   (720, 0.0216737401150802, x^2 - x, (), 1506569166, 14005,\n0.92053315995181839)\nGot:\n   (720, 0.0216737401150802, x^2 - x, (1,3,2)(4,5), 1506569166,\n14005, 0.92053315995181839)\n**********************************************************************\nFile \"/Users/was/build/sage-3.0.alpha1/tmp/randstate.py\", line 206:\n   : r1 = rtest(); r1\nExpected:\n   (303, -0.187141682737491, 1/2*x^2 - 1/95*x - 1/2, (1,2),\n1698070399, 8045, 0.96619117347084138)\nGot:\n   (303, -0.187141682737491, 1/2*x^2 - 1/95*x - 1/2, (1,2)(4,5),\n1698070399, 8045, 0.96619117347084138)\n**********************************************************************\n**********************************************************************\nFile \"/Users/was/build/sage-3.0.alpha1/tmp/randstate.py\", line 208:\n   : r2 = rtest(); r2\nExpected:\n   (105, -0.581229341007821, -x^2 - x - 6, (1,3,2)(4,5), 697338742,\n1271, 0.001767155077382232)\nGot:\n   (105, -0.581229341007821, -x^2 - x - 6, (2,3), 697338742, 1271,\n0.001767155077382232)\n**********************************************************************\nFile \"/Users/was/build/sage-3.0.alpha1/tmp/randstate.py\", line 216:\n   : with seed(1): rtest()\nExpected:\n   (978, 0.184109262667515, -3*x^2 - 1/12, (2,3), 1046254370, 60359,\n0.83350776541997362)\nGot:\n   (978, 0.184109262667515, -3*x^2 - 1/12, (1,2,3), 1046254370,\n60359, 0.83350776541997362)\n**********************************************************************\nFile \"/Users/was/build/sage-3.0.alpha1/tmp/randstate.py\", line 218:\n   : r2m = rtest(); r2m\nExpected:\n   (105, -0.581229341007821, -x^2 - x - 6, (1,3,2)(4,5), 697338742,\n19769, 0.001767155077382232)\nGot:\n   (105, -0.581229341007821, -x^2 - x - 6, (2,3), 697338742, 19769,\n0.001767155077382232)\n**********************************************************************\nFile \"/Users/was/build/sage-3.0.alpha1/tmp/randstate.py\", line 233:\n   : with seed(1): (rtest(), rtest())\nExpected:\n   ((978, 0.184109262667515, -3*x^2 - 1/12, (2,3), 1046254370, 60359,\n0.83350776541997362), (138, -0.2475\n78366457583, 2*x - 24, (), 1077419109, 10234, 0.0033332230808060803))\nGot:\n   ((978, 0.184109262667515, -3*x^2 - 1/12, (1,2,3), 1046254370,\n60359, 0.83350776541997362), (138, -0.24\n7578366457583, 2*x - 24, (4,5), 1077419109, 10234, 0.0033332230808060803))\n**********************************************************************\nFile \"/Users/was/build/sage-3.0.alpha1/tmp/randstate.py\", line 248:\n   : try:\n         ctx.__enter__()\n         rtest()\n   finally:\n         ctx.__exit__(None, None, None)\nExpected:\n   <sage.misc.randstate.randstate object at 0x...>\n   (978, 0.184109262667515, -3*x^2 - 1/12, (2,3), 1046254370, 60359,\n0.83350776541997362)\n   False\nGot:\n   <sage.misc.randstate.randstate object at 0x6e258a0>\n   (978, 0.184109262667515, -3*x^2 - 1/12, (1,2,3), 1046254370,\n60359, 0.83350776541997362)\n   False\n**********************************************************************\nFile \"/Users/was/build/sage-3.0.alpha1/tmp/randstate.py\", line 629:\n   sage: gap.Random(1, 10^50)\nExpected:\n   24922966241004817547714978350347109473543873184564\nGot:\n   97144566318213989637952954803537490912828430192472\n**********************************************************************\n2 items had failures:\n 13 of  60 in __main__.example_0\n  1 of   4 in __main__.example_10\n***Test Failed*** 14 failures.\nFor whitespace errors, see the file\n/Users/was/build/sage-3.0.alpha1/tmp/.doctest_randstate.py\n        [19.4 s]\n```\n\n\n\nMore stuff probably related to random stuff.\n\n```\n        [16.6 s]sage -t  devel/sage/sage/groups/perm_gps/permgroup.py\n     **********************************************************************\nFile \"/Users/was/build/sage-3.0.alpha1/tmp/permgroup.py\", line 709:\n   sage: G.random_element()\nExpected:\n   (1,2)(4,5)\nGot:    (2,3)\n**********************************************************************\nFile \"/Users/was/build/sage-3.0.alpha1/tmp/permgroup.py\", line 1270:\n   sage: g = G.random_element(); g\nExpected:\n   (1,3)\nGot:\n   (1,2)(3,4)\n**********************************************************************\nFile \"/Users/was/build/sage-3.0.alpha1/tmp/permgroup.py\", line 1272:\n   sage: G.normalizer(g)\nExpected:\n   Group( [ (1,3), (2,4) ] )\nGot:\n   Group( [ (1,2)(3,4), (1,4)(2,3) ] )\n**********************************************************************\n2 items had failures:\n  1 of   3 in __main__.example_22\n  2 of   6 in __main__.example_39\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file\n/Users/was/build/sage-3.0.alpha1/tmp/.doctest_permgroup.py\n        [19.1 s]\n```\n\n\n\nNo clue:\n\n```\nsage -t  devel/sage/sage/groups/matrix_gps/unitary.py\n**********************************************\n************************\nFile \"/Users/was/build/sage-3.0.alpha1/tmp/unitary.py\", line 21:\n   sage: G.random()\nExpected:\n   [    3*a     2*a 4*a + 3]\n   [      3 2*a + 4     3*a]\n   [4*a + 1 4*a + 1 3*a + 2]\nGot:\n   [      4 2*a + 4     2*a]\n   [3*a + 3   a + 1   a + 3]\n   [2*a + 2   a + 1 3*a + 1]\n**********************************************************************\n1 items had failures:\n  1 of   8 in __main__.example_0\n***Test Failed*** 1 failures.\n```\n\n\n\n\n```\nsage -t  devel/sage/sage/groups/matrix_gps/symplectic.py\n**********************************************\n************************\nFile \"/Users/was/build/sage-3.0.alpha1/tmp/symplectic.py\", line 14:\n   sage: G.random()\nExpected:\n   [1 0 5 6]\n   [0 5 2 4]\n   [4 0 2 3]\n   [3 6 2 0]\nGot:\n   [4 6 2 0]\n   [2 5 4 0]\n   [3 3 5 1]\n   [2 0 5 5]\n**********************************************************************\n1 items had failures:\n  1 of   6 in __main__.example_0\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file\n/Users/was/build/sage-3.0.alpha1/tmp/.doctest_symplectic.py\n        [7.0 s]\n```\n\n\n\n\n```\nFile \"/Users/was/build/sage-3.0.alpha1/tmp/orthogonal.py\", line 212:\n sage: GO( 3, GF(7), 0).random()\nExpected:\n   [3 2 1]\n   [4 0 0]\n   [6 0 1]Got:\n   [1 5 3]\n   [0 1 0]\n   [0 6 6]\n**********************************************************************\nFile \"/Users/was/build/sage-3.0.alpha1/tmp/orthogonal.py\", line 120:\n   sage: G.random()\nExpected:\n   [2 5 1 1]\n   [3 0 0 0]\n   [0 0 3 5]\n   [2 0 4 4]\nGot:\n   [3 4 5 2]\n   [1 5 2 5]\n   [6 4 6 2]\n   [2 6 4 2]\n**********************************************************************\n2 items had failures:\n  1 of   4 in __main__.example_10\n  1 of   4 in __main__.example_4\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file\n/Users/was/build/sage-3.0.alpha1/tmp/.doctest_orthogonal.py\n        [7.9 s]\nsage -t  devel/sage/sage/groups/matrix_gps/special_linear.py\n```\n\n\n\n\n```\nsage -t  devel/sage/sage/groups/matrix_gps/matrix_group.py\n**********************************************\n************************ File\n\"/Users/was/build/sage-3.0.alpha1/tmp/matrix_group.py\", line 448:\nsage: G.random()Expected:    [2 1 1 1]    [1 0 2 1]\n   [0 1 1 0]\n   [1 0 0 1]\nGot:\n   [1 1 0 1]    [2 1 1 1]\n   [1 2 1 0]\n   [1 1 2 0]\n**********************************************************************\nFile \"/Users/was/build/sage-3.0.alpha1/tmp/matrix_group.py\", line 457:\n   sage: G.random()\nExpected:\n   [1 3]\n   [0 3]\nGot:\n   [2 3]\n   [0 1]\n**********************************************************************\nFile \"/Users/was/build/sage-3.0.alpha1/tmp/matrix_group.py\", line 460:\n   sage: G.random()\nExpected:\n   [2 2]\n   [1 0]\nGot:\n   [4 1]\n   [1 2]\n**********************************************************************\nFile \"/Users/was/build/sage-3.0.alpha1/tmp/matrix_group.py\", line 463:\n   sage: G.random()\nExpected:\n   [4 0]\n   [1 4]\nGot:\n   [4 4]\n   [2 0]\n**********************************************************************\n1 items had failures:\n  4 of   9 in __main__.example_17\n***Test Failed*** 4 failures.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2814\n\n",
    "created_at": "2008-04-05T20:01:31Z",
    "labels": [
        "component: misc",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "sage-3.0-alpha1 on ppc -- new randstate code doesn't work right at all",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2814",
    "user": "https://github.com/williamstein"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/2814





---

archive/issue_comments_019277.json:
```json
{
    "body": "Attachment [trac2814-gap-random-endianness.patch](tarball://root/attachments/some-uuid/ticket2814/trac2814-gap-random-endianness.patch) by cwitty created at 2008-04-10 02:58:39",
    "created_at": "2008-04-10T02:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2814#issuecomment-19277",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac2814-gap-random-endianness.patch](tarball://root/attachments/some-uuid/ticket2814/trac2814-gap-random-endianness.patch) by cwitty created at 2008-04-10 02:58:39



---

archive/issue_comments_019278.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-10T03:02:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2814#issuecomment-19278",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Changing status from new to assigned.



---

archive/issue_comments_019279.json:
```json
{
    "body": "I believe that the two patches fix all of the issues in this ticket.  With the patches, sage -testall passes on 32-bit x86, but they have NOT BEEN TESTED on PPC at all, so somebody needs to do that.",
    "created_at": "2008-04-10T03:02:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2814#issuecomment-19279",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

I believe that the two patches fix all of the issues in this ticket.  With the patches, sage -testall passes on 32-bit x86, but they have NOT BEEN TESTED on PPC at all, so somebody needs to do that.



---

archive/issue_comments_019280.json:
```json
{
    "body": "Applying both patches to my PPC test build does not fix the issue:\n\n```\nsage -t  devel/sage-main/sage/rings/complex_double.pyx\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.0.alpha3/tmp/complex_double.py\", line 179:\n    sage: CDF.random_element()\nExpected:\n    -0.436810529675 + 0.736945423566*I\nGot:\n    0.736945423566 - 0.436810529675*I\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.0.alpha3/tmp/complex_double.py\", line 181:\n    sage: CDF.random_element(-10,10,-10,10)\nExpected:\n    -7.08874026302 - 9.54135400334*I\nGot:\n    -9.54135400334 - 7.08874026302*I\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.0.alpha3/tmp/complex_double.py\", line 183:\n    sage: CDF.random_element(-10^20,10^20,-2,2)\nExpected:\n    -7.58765473764e+19 + 0.925549022839*I\nGot:\n    4.62774511419e+19 - 1.51753094753*I\n**********************************************************************\n1 items had failures:\n   3 of   4 in __main__.example_7\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file /Users/mabshoff/sage-3.0.alpha3/tmp/.doctest_complex_double.py\n```\n\nmisc/randstate.pyx:\n\n```\n----------------------------------------------------------------------\nsage -t  devel/sage-main/sage/misc/randstate.pyx\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.0.alpha3/tmp/randstate.py\", line 47:\n    : rtest()\nExpected:\n    (303, -0.187141682737491, 1/2*x^2 - 1/95*x - 1/2, (1,2), 1698070399, 8045, 0.96619117347084138)\nGot:\n    (303, -0.187141682737491, 1/2*x^2 - 1/95*x - 1/2, (1,2)(4,5), 1698070399, 8045, 0.96619117347084138)\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.0.alpha3/tmp/randstate.py\", line 50:\n    : rtest()\nExpected:\n    (978, 0.184109262667515, -3*x^2 - 1/12, (2,3), 1046254370, 60359, 0.83350776541997362)\nGot:\n    (978, 0.184109262667515, -3*x^2 - 1/12, (1,2,3), 1046254370, 60359, 0.83350776541997362)\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.0.alpha3/tmp/randstate.py\", line 53:\n    : rtest()\nExpected:\n    (207, 0.505364206568040, 4*x^2 + 1/2, (1,2)(4,5), 2137873234, 27695, 0.19982565117278328)\nGot:\n    (207, 0.505364206568040, 4*x^2 + 1/2, (4,5), 2137873234, 27695, 0.19982565117278328)\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.0.alpha3/tmp/randstate.py\", line 56:\n    : rtest()\nExpected:\n    (303, -0.187141682737491, 1/2*x^2 - 1/95*x - 1/2, (1,2), 1698070399, 8045, 0.96619117347084138)\nGot:\n    (303, -0.187141682737491, 1/2*x^2 - 1/95*x - 1/2, (1,2)(4,5), 1698070399, 8045, 0.96619117347084138)\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.0.alpha3/tmp/randstate.py\", line 59:\n    : rtest()\nExpected:\n    (978, 0.184109262667515, -3*x^2 - 1/12, (2,3), 1046254370, 60359, 0.83350776541997362)\nGot:\n    (978, 0.184109262667515, -3*x^2 - 1/12, (1,2,3), 1046254370, 60359, 0.83350776541997362)\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.0.alpha3/tmp/randstate.py\", line 62:\n    : rtest()\nExpected:\n    (207, 0.505364206568040, 4*x^2 + 1/2, (1,2)(4,5), 2137873234, 27695, 0.19982565117278328)\nGot:\n    (207, 0.505364206568040, 4*x^2 + 1/2, (4,5), 2137873234, 27695, 0.19982565117278328)\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.0.alpha3/tmp/randstate.py\", line 72:\n    : rtest()\nExpected:\n    (720, 0.0216737401150802, x^2 - x, (), 1506569166, 14005, 0.92053315995181839)\nGot:\n    (720, 0.0216737401150802, x^2 - x, (1,3,2)(4,5), 1506569166, 14005, 0.92053315995181839)\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.0.alpha3/tmp/randstate.py\", line 206:\n    : r1 = rtest(); r1\nExpected:\n    (303, -0.187141682737491, 1/2*x^2 - 1/95*x - 1/2, (1,2), 1698070399, 8045, 0.96619117347084138)\nGot:\n    (303, -0.187141682737491, 1/2*x^2 - 1/95*x - 1/2, (1,2)(4,5), 1698070399, 8045, 0.96619117347084138)\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.0.alpha3/tmp/randstate.py\", line 208:\n    : r2 = rtest(); r2\nExpected:\n    (105, -0.581229341007821, -x^2 - x - 6, (1,3,2)(4,5), 697338742, 1271, 0.001767155077382232)\nGot:\n    (105, -0.581229341007821, -x^2 - x - 6, (2,3), 697338742, 1271, 0.001767155077382232)\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.0.alpha3/tmp/randstate.py\", line 216:\n    : with seed(1): rtest()\nExpected:\n    (978, 0.184109262667515, -3*x^2 - 1/12, (2,3), 1046254370, 60359, 0.83350776541997362)\nGot:\n    (978, 0.184109262667515, -3*x^2 - 1/12, (1,2,3), 1046254370, 60359, 0.83350776541997362)\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.0.alpha3/tmp/randstate.py\", line 218:\n    : r2m = rtest(); r2m\nExpected:\n    (105, -0.581229341007821, -x^2 - x - 6, (1,3,2)(4,5), 697338742, 19769, 0.001767155077382232)\nGot:\n    (105, -0.581229341007821, -x^2 - x - 6, (2,3), 697338742, 19769, 0.001767155077382232)\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.0.alpha3/tmp/randstate.py\", line 233:\n    : with seed(1): (rtest(), rtest())\nExpected:\n    ((978, 0.184109262667515, -3*x^2 - 1/12, (2,3), 1046254370, 60359, 0.83350776541997362), (138, -0.247578366457583, 2*x - 24, (), 1077419109, 10234, 0.0033332230808060803))\nGot:\n    ((978, 0.184109262667515, -3*x^2 - 1/12, (1,2,3), 1046254370, 60359, 0.83350776541997362), (138, -0.247578366457583, 2*x - 24, (4,5), 1077419109, 10234, 0.0033332230808060803))\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.0.alpha3/tmp/randstate.py\", line 248:\n    : try:\n          ctx.__enter__()\n          rtest()\n    finally:\n          ctx.__exit__(None, None, None)\nExpected:\n    <sage.misc.randstate.randstate object at 0x...>\n    (978, 0.184109262667515, -3*x^2 - 1/12, (2,3), 1046254370, 60359, 0.83350776541997362)\n    False\nGot:\n    <sage.misc.randstate.randstate object at 0x7032e40>\n    (978, 0.184109262667515, -3*x^2 - 1/12, (1,2,3), 1046254370, 60359, 0.83350776541997362)\n    False\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.0.alpha3/tmp/randstate.py\", line 630:\n    sage: gap.Random(1, 10^50)\nExpected:\n    24922966241004817547714978350347109473543873184564\nGot:\n    97144566318213989637952954803537490912828430192472\n**********************************************************************\n2 items had failures:\n  13 of  60 in __main__.example_0\n   1 of   4 in __main__.example_10\n***Test Failed*** 14 failures.\nFor whitespace errors, see the file /Users/mabshoff/sage-3.0.alpha3/tmp/.doctest_randstate.py\n```\n\ngroups/perm_gps/permgroup.py:\n\n```\n----------------------------------------------------------------------\nsage -t  devel/sage-main/sage/groups/perm_gps/permgroup.py\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.0.alpha3/tmp/permgroup.py\", line 709:\n    sage: G.random_element()\nExpected:\n    (1,2)(4,5)\nGot:\n    (2,3)\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.0.alpha3/tmp/permgroup.py\", line 1270:\n    sage: g = G.random_element(); g\nExpected:\n    (1,3)\nGot:\n    (1,2)(3,4)\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.0.alpha3/tmp/permgroup.py\", line 1272:\n    sage: G.normalizer(g)\nExpected:\n    Group( [ (1,3), (2,4) ] )\nGot:\n    Group( [ (1,2)(3,4), (1,4)(2,3) ] )\n**********************************************************************\n```\n\ngroups/matrix_gps/unitary.py:\n\n```\n----------------------------------------------------------------------\nsage -t  devel/sage-main/sage/groups/matrix_gps/unitary.py\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.0.alpha3/tmp/unitary.py\", line 21:\n    sage: G.random()\nExpected:\n    [    3*a     2*a 4*a + 3]\n    [      3 2*a + 4     3*a]\n    [4*a + 1 4*a + 1 3*a + 2]\nGot:\n    [      4 2*a + 4     2*a]\n    [3*a + 3   a + 1   a + 3]\n    [2*a + 2   a + 1 3*a + 1]\n**********************************************************************\n```\n\ngroups/matrix_gps/symplectic.py:\n\n```\n----------------------------------------------------------------------\nsage -t  devel/sage-main/sage/groups/matrix_gps/symplectic.py\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.0.alpha3/tmp/symplectic.py\", line 14:\n    sage: G.random()\nExpected:\n    [1 0 5 6]\n    [0 5 2 4]\n    [4 0 2 3]\n    [3 6 2 0]\nGot:\n    [4 6 2 0]\n    [2 5 4 0]\n    [3 3 5 1]\n    [2 0 5 5]\n**********************************************************************\n```\n\ngroups/matrix_gps/orthogonal.py:\n\n```\n----------------------------------------------------------------------\nsage -t  devel/sage-main/sage/groups/matrix_gps/orthogonal.py\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.0.alpha3/tmp/orthogonal.py\", line 212:\n    sage: GO( 3, GF(7), 0).random()\nExpected:\n    [3 2 1]\n    [4 0 0]\n    [6 0 1]\nGot:\n    [1 5 3]\n    [0 1 0]\n    [0 6 6]\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.0.alpha3/tmp/orthogonal.py\", line 120:\n    sage: G.random()\nExpected:\n    [2 5 1 1]\n    [3 0 0 0]\n    [0 0 3 5]\n    [2 0 4 4]\nGot:\n    [3 4 5 2]\n    [1 5 2 5]\n    [6 4 6 2]\n    [2 6 4 2]\n**********************************************************************\n```\n\ngroups/matrix_gps/matrix_group.py:\n\n```\n----------------------------------------------------------------------\nsage -t  devel/sage-main/sage/groups/matrix_gps/matrix_group.py\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.0.alpha3/tmp/matrix_group.py\", line 448:\n    sage: G.random()\nExpected:\n    [2 1 1 1]\n    [1 0 2 1]\n    [0 1 1 0]\n    [1 0 0 1]\nGot:\n    [1 1 0 1]\n    [2 1 1 1]\n    [1 2 1 0]\n    [1 1 2 0]\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.0.alpha3/tmp/matrix_group.py\", line 457:\n    sage: G.random()\nExpected:\n    [1 3]\n    [0 3]\nGot:\n    [2 3]\n    [0 1]\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.0.alpha3/tmp/matrix_group.py\", line 460:\n    sage: G.random()\nExpected:\n    [2 2]\n    [1 0]\nGot:\n    [4 1]\n    [1 2]\n**********************************************************************\nFile \"/Users/mabshoff/sage-3.0.alpha3/tmp/matrix_group.py\", line 463:\n    sage: G.random()\nExpected:\n    [4 0]\n    [1 4]\nGot:\n    [4 4]\n    [2 0]\n**********************************************************************\n```\n",
    "created_at": "2008-04-10T13:15:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2814#issuecomment-19280",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

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

archive/issue_comments_019281.json:
```json
{
    "body": "With a clean build all tests pass now:\n\n```\nfermat:sage-3.0.alpha3 mabshoff$ uname -a\nDarwin fermat.math.harvard.edu 9.2.0 Darwin Kernel Version 9.2.0: Tue Feb  5 16:15:19 PST 2008; root:xnu-1228.3.13~1/RELEASE_PPC Power Macintosh\n\nfermat:sage-3.0.alpha3 mabshoff$ ./sage -t  devel/sage-main/sage/rings/complex_double.pyx\nGlobal iterations: 1\nFile iterations: 1\nTeX files: 0\n\n----------------------------------------------------------------------\nsage -t  devel/sage-main/sage/rings/complex_double.pyx\n         [7.6 s]\nAll tests passed!\nTotal time for all tests: 7.6 seconds\n\nfermat:sage-3.0.alpha3 mabshoff$ ./sage -t  devel/sage-main/sage/misc/randstate.pyx\nGlobal iterations: 1\nFile iterations: 1\nTeX files: 0\n\n----------------------------------------------------------------------\nsage -t  devel/sage-main/sage/misc/randstate.pyx\n         [20.8 s]\nAll tests passed!\nTotal time for all tests: 20.8 seconds\n\nfermat:sage-3.0.alpha3 mabshoff$ ./sage -t  devel/sage-main/sage/groups/perm_gps/permgroup.py\nGlobal iterations: 1\nFile iterations: 1\nTeX files: 0\n\n----------------------------------------------------------------------\n\nsage -t  devel/sage-main/sage/groups/perm_gps/permgroup.py\n         [19.0 s]\nAll tests passed!\nTotal time for all tests: 19.0 seconds\nfermat:sage-3.0.alpha3 mabshoff$\nfermat:sage-3.0.alpha3 mabshoff$ sage -t  devel/sage-main/sage/groups/matrix_gps/unitary.py\nGlobal iterations: 1\nFile iterations: 1\nTeX files: 0\n\n----------------------------------------------------------------------\n\nsage -t  devel/sage-main/sage/groups/matrix_gps/unitary.py\n         [8.8 s]\nAll tests passed!\nTotal time for all tests: 8.8 seconds\nfermat:sage-3.0.alpha3 mabshoff$\nfermat:sage-3.0.alpha3 mabshoff$ ./sage -t  devel/sage-main/sage/groups/matrix_gps/symplectic.py\nGlobal iterations: 1\nFile iterations: 1\nTeX files: 0\n\n----------------------------------------------------------------------\n\nsage -t  devel/sage-main/sage/groups/matrix_gps/symplectic.py\n         [7.2 s]\nAll tests passed!\nTotal time for all tests: 7.2 seconds\nfermat:sage-3.0.alpha3 mabshoff$\nfermat:sage-3.0.alpha3 mabshoff$ ./sage -t  devel/sage-main/sage/groups/matrix_gps/orthogonal.py\nGlobal iterations: 1\nFile iterations: 1\nTeX files: 0\n\n----------------------------------------------------------------------\n\nsage -t  devel/sage-main/sage/groups/matrix_gps/orthogonal.py\n         [8.2 s]\nAll tests passed!\nTotal time for all tests: 8.2 seconds\nfermat:sage-3.0.alpha3 mabshoff$\nfermat:sage-3.0.alpha3 mabshoff$ ./sage -t  devel/sage-main/sage/groups/matrix_gps/matrix_group.py\nGlobal iterations: 1\nFile iterations: 1\nTeX files: 0\n\n----------------------------------------------------------------------\n\nsage -t  devel/sage-main/sage/groups/matrix_gps/matrix_group.py\n         [69.5 s]\nAll tests passed!\nTotal time for all tests: 69.5 seconds \n```\n\n\nPositive review. I also tested on sage.math [x86-64] and it works there.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-10T19:14:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2814#issuecomment-19281",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

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

archive/issue_comments_019282.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-10T19:14:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2814#issuecomment-19282",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019283.json:
```json
{
    "body": "Merged in Sage 3.0.alpha4",
    "created_at": "2008-04-10T19:14:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2814#issuecomment-19283",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha4



---

archive/issue_events_006474.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-10T19:14:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2814",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2814#event-6474"
}
```
