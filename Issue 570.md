# Issue 570: rubik.solve doesn't work (sage -t --long groups/perm_gps/cubegroup.py  fails.)

archive/issues_000570.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage -t --long groups/perm_gps/cubegroup.py                 **********************************************************************\nFile \"cubegroup.py\", line 979:\n    sage: rubik.solve(state)  # long time; *computationally intensive* even for simple moves\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/s/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_15[2]>\", line 1, in <module>\n        rubik.solve(state)  # long time; *computationally intensive* even for simple moves###line 979:\n    sage: rubik.solve(state)  # long time; *computationally intensive* even for simple moves\n      File \"/home/was/s/local/lib/python2.5/site-packages/sage/groups/perm_gps/cubegroup.py\", line 999, in solve\n        soln = hom.PreImagesRepresentative(gap(str(g)))\n      File \"/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 674, in __call__\n        return cls(self, x)\n      File \"/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 904, in __init__\n        raise TypeError, x\n    TypeError: Gap produced error output\n    Syntax error: literal expected in /home/was/.sage//temp/ubuntu/13323//interfac\\\n    e//tmp line 1\n    $sage14:={'right': [[19, 29, 32], [18, 0, 31], [17, 28, 30]], 'up': [[3, 5, 38\\\n    ], [2, 0, 36], [1, 4, 25]], 'back': [[48, 26, 27], [45, 0, 37], [43, 39, 40]],\\\n     'down': [[41, 42, 11], [44, 0, 21], [46, 47, 24]], 'front': [[9, 10, 8], [20,\\\n     0, 7], [22, 23, 6]], 'left': [[33, 34, 35], [12, 0, 13], [14, 15, 16]]};;\n             ^\n\n       executing Read(\"/home/was/.sage//temp/ubuntu/13323//interface//tmp\");\n**********************************************************************\n1 items had failures:\n   1 of   3 in __main__.example_15\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctest_cubegroup.py\n         [13.5 s]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/570\n\n",
    "created_at": "2007-09-02T17:39:12Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "rubik.solve doesn't work (sage -t --long groups/perm_gps/cubegroup.py  fails.)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/570",
    "user": "was"
}
```
Assignee: somebody


```
sage -t --long groups/perm_gps/cubegroup.py                 **********************************************************************
File "cubegroup.py", line 979:
    sage: rubik.solve(state)  # long time; *computationally intensive* even for simple moves
Exception raised:
    Traceback (most recent call last):
      File "/home/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_15[2]>", line 1, in <module>
        rubik.solve(state)  # long time; *computationally intensive* even for simple moves###line 979:
    sage: rubik.solve(state)  # long time; *computationally intensive* even for simple moves
      File "/home/was/s/local/lib/python2.5/site-packages/sage/groups/perm_gps/cubegroup.py", line 999, in solve
        soln = hom.PreImagesRepresentative(gap(str(g)))
      File "/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 674, in __call__
        return cls(self, x)
      File "/home/was/s/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 904, in __init__
        raise TypeError, x
    TypeError: Gap produced error output
    Syntax error: literal expected in /home/was/.sage//temp/ubuntu/13323//interfac\
    e//tmp line 1
    $sage14:={'right': [[19, 29, 32], [18, 0, 31], [17, 28, 30]], 'up': [[3, 5, 38\
    ], [2, 0, 36], [1, 4, 25]], 'back': [[48, 26, 27], [45, 0, 37], [43, 39, 40]],\
     'down': [[41, 42, 11], [44, 0, 21], [46, 47, 24]], 'front': [[9, 10, 8], [20,\
     0, 7], [22, 23, 6]], 'left': [[33, 34, 35], [12, 0, 13], [14, 15, 16]]};;
             ^

       executing Read("/home/was/.sage//temp/ubuntu/13323//interface//tmp");
**********************************************************************
1 items had failures:
   1 of   3 in __main__.example_15
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_cubegroup.py
         [13.5 s]
```


Issue created by migration from https://trac.sagemath.org/ticket/570





---

archive/issue_comments_002953.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-09-06T01:52:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/570#issuecomment-2953",
    "user": "wdj"
}
```

Attachment



---

archive/issue_comments_002954.json:
```json
{
    "body": "Fixed the docstring and now all tests pass:\n\n\n```\nwdj@wooster:~/sagefiles/sage-2.8.3.rc3> ./sage -t --long \"/home/wdj/sagefiles/sage-2.8.3.rc3/devel/sage-cube/sage/groups/perm_gps/cubegroup.py\"\nsage -t --long devel/sage-cube/sage/groups/perm_gps/cubegroup.py\n         [31.1 s]\n\n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 31.2 seconds\n```\n",
    "created_at": "2007-09-06T01:53:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/570#issuecomment-2954",
    "user": "wdj"
}
```

Fixed the docstring and now all tests pass:


```
wdj@wooster:~/sagefiles/sage-2.8.3.rc3> ./sage -t --long "/home/wdj/sagefiles/sage-2.8.3.rc3/devel/sage-cube/sage/groups/perm_gps/cubegroup.py"
sage -t --long devel/sage-cube/sage/groups/perm_gps/cubegroup.py
         [31.1 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 31.2 seconds
```




---

archive/issue_comments_002955.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-09-06T19:19:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/570#issuecomment-2955",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_002956.json:
```json
{
    "body": "Added parse() method to take several kinds of inputs, re-enabled doctest for solve.",
    "created_at": "2007-09-06T19:20:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/570#issuecomment-2956",
    "user": "robertwb"
}
```

Added parse() method to take several kinds of inputs, re-enabled doctest for solve.



---

archive/issue_comments_002957.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-06T19:20:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/570#issuecomment-2957",
    "user": "robertwb"
}
```

Resolution: fixed



---

archive/issue_comments_002958.json:
```json
{
    "body": "Changing component from basic arithmetic to combinatorics.",
    "created_at": "2007-09-06T19:20:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/570#issuecomment-2958",
    "user": "robertwb"
}
```

Changing component from basic arithmetic to combinatorics.



---

archive/issue_comments_002959.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-09-06T20:21:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/570#issuecomment-2959",
    "user": "robertwb"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_002960.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-09-06T20:21:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/570#issuecomment-2960",
    "user": "robertwb"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_002961.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-07T04:34:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/570#issuecomment-2961",
    "user": "was"
}
```

Resolution: fixed
