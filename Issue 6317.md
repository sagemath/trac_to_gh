# Issue 6317: optional doctest failure -- maple interface

archive/issues_006317.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @mkoeppe\n\nEvidently the maple interface is even completely broken on sage.math right now!\n\n```\nsage -t -long --optional devel/sage/sage/calculus/calculus.py\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/calculus/calculus.py\", line 479:\n    sage: g = maple(f); g                             # optional -- requires maple\nExpected:\n    sin(x^2)+y^z\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/calculus/calculus.py\", line 481:\n    sage: g.integrate(x)                              # optional -- requires maple\nExpected:\n    1/2*2^(1/2)*Pi^(1/2)*FresnelS(2^(1/2)/Pi^(1/2)*x)+y^z*x\nGot:\n    read \"/scratch/wstein/sage//temp/sage.math.washington.edu/2399//interface//tmp2399\";\n    read \"/scratch/wstein/sage//temp/sage.math.washington.edu/2399//interface//tmp2399\";\n    read \"/scratch/wstein/sage//temp/sage.math.washington.edu/2399//interface//tmp2399\";\n    sage2\n**********************************************************************\n1 items had failures:\n   2 of  56 in __main__.example_1\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_calculus.py\n\t [13.3 s]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6317\n\n",
    "created_at": "2009-06-16T14:46:05Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "optional doctest failure -- maple interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6317",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

CC:  @mkoeppe

Evidently the maple interface is even completely broken on sage.math right now!

```
sage -t -long --optional devel/sage/sage/calculus/calculus.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/calculus/calculus.py", line 479:
    sage: g = maple(f); g                             # optional -- requires maple
Expected:
    sin(x^2)+y^z
Got:
    <BLANKLINE>
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/calculus/calculus.py", line 481:
    sage: g.integrate(x)                              # optional -- requires maple
Expected:
    1/2*2^(1/2)*Pi^(1/2)*FresnelS(2^(1/2)/Pi^(1/2)*x)+y^z*x
Got:
    read "/scratch/wstein/sage//temp/sage.math.washington.edu/2399//interface//tmp2399";
    read "/scratch/wstein/sage//temp/sage.math.washington.edu/2399//interface//tmp2399";
    read "/scratch/wstein/sage//temp/sage.math.washington.edu/2399//interface//tmp2399";
    sage2
**********************************************************************
1 items had failures:
   2 of  56 in __main__.example_1
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_calculus.py
	 [13.3 s]
```


Issue created by migration from https://trac.sagemath.org/ticket/6317





---

archive/issue_comments_050319.json:
```json
{
    "body": "More doctest failures caused by the Maple interface being broken:\n\n```\nsage -t -long --optional devel/sage/sage/modules/free_module_element.pyx\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/modules/free_module_element.pyx\", line 839:\n    sage: maple(v)                                  #optional\nExpected:\n    Vector[row](4, [0,1,2,3])\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/modules/free_module_element.pyx\", line 845:\n    sage: maple(v)                                  #optional\nExpected:\n    Vector[row](3, [2/3,0,5/4])\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/modules/free_module_element.pyx\", line 852:\n    sage: maple(v)                                           #optional\nExpected:\n    Vector[row](3, [x^2+2,2*x+1,-2*x^2+4*x])\nGot:\n    <BLANKLINE>\n**********************************************************************\n1 items had failures:\n   3 of   9 in __main__.example_22\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_free_module_element.py\n\t [8.7 s]\n```\n",
    "created_at": "2009-06-16T14:57:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6317#issuecomment-50319",
    "user": "https://github.com/williamstein"
}
```

More doctest failures caused by the Maple interface being broken:

```
sage -t -long --optional devel/sage/sage/modules/free_module_element.pyx
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/modules/free_module_element.pyx", line 839:
    sage: maple(v)                                  #optional
Expected:
    Vector[row](4, [0,1,2,3])
Got:
    <BLANKLINE>
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/modules/free_module_element.pyx", line 845:
    sage: maple(v)                                  #optional
Expected:
    Vector[row](3, [2/3,0,5/4])
Got:
    <BLANKLINE>
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/modules/free_module_element.pyx", line 852:
    sage: maple(v)                                           #optional
Expected:
    Vector[row](3, [x^2+2,2*x+1,-2*x^2+4*x])
Got:
    <BLANKLINE>
**********************************************************************
1 items had failures:
   3 of   9 in __main__.example_22
***Test Failed*** 3 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_free_module_element.py
	 [8.7 s]
```




---

archive/issue_comments_050320.json:
```json
{
    "body": "And more:\n\n```\nsage -t -long --optional devel/sage/sage/symbolic/constants.py\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/symbolic/constants.py\", line 51:\n    sage: maple(pi)                   # optional\nExpected:\n    Pi\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/symbolic/constants.py\", line 1210:\n    sage: m.N(200)                                 # optional\nExpected:\n    2.6854520010653064453097148354817956938203822939944629530511523455572188595371520028011411749318476979951534659052880900828976777164109630517925334832596683818523154213321194996260393285220448194096181                \nGot:\n    2.68545200106530644530971483548179569382038229399446295305115234555721885953715200280114117493184769799515346590528809008289767771641096305179253348325966838185231542133211949962603932852204481940961807\n**********************************************************************\n2 items had failures:\n   1 of  58 in __main__.example_0\n   1 of   5 in __main__.example_62\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_constants.py\n\t [6.4 s]\n```\n",
    "created_at": "2009-06-16T14:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6317#issuecomment-50320",
    "user": "https://github.com/williamstein"
}
```

And more:

```
sage -t -long --optional devel/sage/sage/symbolic/constants.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/symbolic/constants.py", line 51:
    sage: maple(pi)                   # optional
Expected:
    Pi
Got:
    <BLANKLINE>
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/symbolic/constants.py", line 1210:
    sage: m.N(200)                                 # optional
Expected:
    2.6854520010653064453097148354817956938203822939944629530511523455572188595371520028011411749318476979951534659052880900828976777164109630517925334832596683818523154213321194996260393285220448194096181                
Got:
    2.68545200106530644530971483548179569382038229399446295305115234555721885953715200280114117493184769799515346590528809008289767771641096305179253348325966838185231542133211949962603932852204481940961807
**********************************************************************
2 items had failures:
   1 of  58 in __main__.example_0
   1 of   5 in __main__.example_62
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_constants.py
	 [6.4 s]
```




---

archive/issue_comments_050321.json:
```json
{
    "body": "And of course there are many more failures, including a total hang:\n\n```\nsage -t -long --optional devel/sage/sage/interfaces/maple.py\n*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n*** *** Error: TIMED OUT! *** ***\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/maple.py\", line 27:\n    sage: maple('3 * 5')                                 # optional - maple\nExpected:\n    15\nGot:\n    <BLANKLINE>\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/maple.py\", line 29:\n    sage: maple.eval('ifactor(2005)')                    # optional - maple\nExpected:\n    '\"(5)*\"(401)'\nGot:\n    ''\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/maple.py\", line 31:\n    sage: maple.ifactor(2005)                            # optional - maple\nExpected:\n    \"(5)*\"(401)\nGot:\n    <BLANKLINE>\n... hundreds more...\n\n```\n",
    "created_at": "2009-06-16T15:21:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6317#issuecomment-50321",
    "user": "https://github.com/williamstein"
}
```

And of course there are many more failures, including a total hang:

```
sage -t -long --optional devel/sage/sage/interfaces/maple.py
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/maple.py", line 27:
    sage: maple('3 * 5')                                 # optional - maple
Expected:
    15
Got:
    <BLANKLINE>
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/maple.py", line 29:
    sage: maple.eval('ifactor(2005)')                    # optional - maple
Expected:
    '"(5)*"(401)'
Got:
    ''
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/interfaces/maple.py", line 31:
    sage: maple.ifactor(2005)                            # optional - maple
Expected:
    "(5)*"(401)
Got:
    <BLANKLINE>
... hundreds more...

```




---

archive/issue_comments_050322.json:
```json
{
    "body": "Changing keywords from \"\" to \"maple\".",
    "created_at": "2015-09-16T12:38:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6317#issuecomment-50322",
    "user": "https://github.com/fchapoton"
}
```

Changing keywords from "" to "maple".



---

archive/issue_comments_050323.json:
```json
{
    "body": "obsolete ?",
    "created_at": "2020-10-02T14:05:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6317#issuecomment-50323",
    "user": "https://github.com/fchapoton"
}
```

obsolete ?



---

archive/issue_events_006564.json:
```json
{
    "actor": "@fchapoton",
    "created_at": "2022-10-08T07:33:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6317",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6317#event-6564"
}
```



---

archive/issue_comments_050324.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2022-10-08T07:33:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6317#issuecomment-50324",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid



---

archive/issue_comments_050325.json:
```json
{
    "body": "closing as very old and working now",
    "created_at": "2022-10-08T07:33:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6317",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6317#issuecomment-50325",
    "user": "https://github.com/fchapoton"
}
```

closing as very old and working now
