# Issue 1586: preparser.py doctest failures

archive/issues_001586.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nrlmill@sage:~/release/sage-2.9.1.alpha3$ ./sage -t  devel/sage-main/sage/misc/preparser.py\nsage -t  devel/sage-main/sage/misc/preparser.py             **********************************************************************\nFile \"preparser.py\", line 472:\n    sage: preparse(\"ZZ.<x> = ZZ['x']\")   \nExpected:\n    'ZZ = ZZ[\"x\"]; (x,) = ZZ._first_ngens(Integer(1))'\nGot:\n    \"ZZ = ZZ['x']; (x,) = ZZ._first_ngens(Integer(1))\"\n**********************************************************************\nFile \"preparser.py\", line 474:\n    sage: preparse(\"ZZ.<x> = ZZ['y']\")\nExpected:\n    'ZZ = ZZ[\"x\"]; (x,) = ZZ._first_ngens(Integer(1))'\nGot:\n    \"ZZ = ZZ['y']; (x,) = ZZ._first_ngens(Integer(1))\"\n**********************************************************************\nFile \"preparser.py\", line 476:\n    sage: preparse(\"ZZ.<x,y> = ZZ[]\")\nExpected:\n    'ZZ = ZZ[\"x, y\"]; (x, y,) = ZZ._first_ngens(Integer(2))'\nGot:\n    \"ZZ = ZZ['x, y']; (x, y,) = ZZ._first_ngens(Integer(2))\"\n**********************************************************************\nFile \"preparser.py\", line 478:\n    sage: preparse(\"ZZ.<x,y> = ZZ['u,v']\")\nExpected:\n    'ZZ = ZZ[\"x, y\"]; (x, y,) = ZZ._first_ngens(Integer(2))'\nGot:\n    \"ZZ = ZZ['u,v']; (x, y,) = ZZ._first_ngens(Integer(2))\"\n**********************************************************************\nFile \"preparser.py\", line 480:\n    sage: preparse(\"ZZ.<x> = QQ[2^(1/3)]\")\nExpected:\n    'ZZ = QQ[\"x\"]; (x,) = ZZ._first_ngens(Integer(1))'\nGot:\n    'ZZ = QQ[Integer(2)**(Integer(1)/Integer(3))]; (x,) = ZZ._first_ngens(Integer(1))'\n**********************************************************************\n1 items had failures:\n   5 of   6 in __main__.example_6\n***Test Failed*** 5 failures.\nFor whitespace errors, see the file .doctest_preparser.py\n         [2.7 s]\nexit code: 256\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  devel/sage-main/sage/misc/preparser.py\nTotal time for all tests: 2.7 seconds\nrlmill@sage:~/release/sage-2.9.1.alpha3$ \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1586\n\n",
    "created_at": "2007-12-22T05:19:00Z",
    "labels": [
        "algebraic geometry",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.1",
    "title": "preparser.py doctest failures",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1586",
    "user": "@rlmill"
}
```
Assignee: @williamstein


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


Issue created by migration from https://trac.sagemath.org/ticket/1586





---

archive/issue_comments_010093.json:
```json
{
    "body": "http://sage.math.washington.edu/home/rlmill/release/merged-sage-2.9.1.rc0/fix_preparser_doctests.patch",
    "created_at": "2007-12-22T10:10:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1586#issuecomment-10093",
    "user": "@rlmill"
}
```

http://sage.math.washington.edu/home/rlmill/release/merged-sage-2.9.1.rc0/fix_preparser_doctests.patch



---

archive/issue_comments_010094.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-22T10:11:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1586#issuecomment-10094",
    "user": "@rlmill"
}
```

Resolution: fixed
