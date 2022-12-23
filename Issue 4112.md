# Issue 4112: 3.1.2.rc2 doctest failure: sage/interfaces/sage0.py

archive/issues_004112.json:
```json
{
    "body": "Assignee: was\n\nI saw the following doctest failure on my Intel OSX 10.5 MacBook Pro:\n\n\n```\nsage -t  devel/sage-main/sage/interfaces/sage0.py           *******************\n**************************************************\nFile \"/Users/craigcitro/three-oh-two/tmp/sage0.py\", line 276:\n    sage: sage0.eval('2+2')\nExpected:\n    '4'\nGot:\n    '4\\n'\n**********************************************************************\nFile \"/Users/craigcitro/three-oh-two/tmp/sage0.py\", line 289:\n    sage: sage0.get('x')\nExpected:\n    '2'\nGot:\n    '2\\n'\n**********************************************************************\nFile \"/Users/craigcitro/three-oh-two/tmp/sage0.py\", line 303:\n    sage: sage0.get('x')\nExpected:\n    '2'\nGot:\n    '2\\n'\n**********************************************************************\nFile \"/Users/craigcitro/three-oh-two/tmp/sage0.py\", line 314:\n    sage: sage0.get('x')\nExpected:\n    '2'\nGot:\n    '2\\n'\n**********************************************************************\nFile \"/Users/craigcitro/three-oh-two/tmp/sage0.py\", line 317:\n    sage: sage0.get('x')\nExpected:\n    \"...NameError: name 'x' is not defined\"\nGot:\n    \"--------------------------------------------------------------------------\n\\nNameError                                 Traceback (most recent call last)\\n\nn/Users/craigcitro/three-oh-two/data/extcode/sage/<ipython console> in <module>\n)\\n\\nNameError: name 'x' is not defined\\n\"\n**********************************************************************\nFile \"/Users/craigcitro/three-oh-two/tmp/sage0.py\", line 326:\n    sage: sage0._contains('2', 'QQ')\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/Users/craigcitro/three-oh-two/tmp/sage0.py\", line 350:\n    sage: sage0.version() == version()\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/Users/craigcitro/three-oh-two/tmp/sage0.py\", line 487:\n    sage: sage0_version() == version()\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"/Users/craigcitro/three-oh-two/tmp/sage0.py\", line 177:\n    sage: s.eval('2+2')\nExpected:\n    '4'\nGot:\n    '4\\n'\n**********************************************************************\n8 items had failures:\n   1 of   3 in __main__.example_10\n   1 of   4 in __main__.example_11\n   1 of   4 in __main__.example_12\n   2 of   6 in __main__.example_13\n   1 of   3 in __main__.example_14\n   1 of   4 in __main__.example_16\n   1 of   4 in __main__.example_26\n   1 of   5 in __main__.example_5\n***Test Failed*** 9 failures.\nFor whitespace errors, see the file /Users/craigcitro/three-oh-two/tmp/.doctest\nsage0.py\n         [9.7 s]\nexit code: 1024\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4112\n\n",
    "created_at": "2008-09-14T06:20:47Z",
    "labels": [
        "interfaces",
        "blocker",
        "bug"
    ],
    "title": "3.1.2.rc2 doctest failure: sage/interfaces/sage0.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4112",
    "user": "craigcitro"
}
```
Assignee: was

I saw the following doctest failure on my Intel OSX 10.5 MacBook Pro:


```
sage -t  devel/sage-main/sage/interfaces/sage0.py           *******************
**************************************************
File "/Users/craigcitro/three-oh-two/tmp/sage0.py", line 276:
    sage: sage0.eval('2+2')
Expected:
    '4'
Got:
    '4\n'
**********************************************************************
File "/Users/craigcitro/three-oh-two/tmp/sage0.py", line 289:
    sage: sage0.get('x')
Expected:
    '2'
Got:
    '2\n'
**********************************************************************
File "/Users/craigcitro/three-oh-two/tmp/sage0.py", line 303:
    sage: sage0.get('x')
Expected:
    '2'
Got:
    '2\n'
**********************************************************************
File "/Users/craigcitro/three-oh-two/tmp/sage0.py", line 314:
    sage: sage0.get('x')
Expected:
    '2'
Got:
    '2\n'
**********************************************************************
File "/Users/craigcitro/three-oh-two/tmp/sage0.py", line 317:
    sage: sage0.get('x')
Expected:
    "...NameError: name 'x' is not defined"
Got:
    "--------------------------------------------------------------------------
\nNameError                                 Traceback (most recent call last)\n
n/Users/craigcitro/three-oh-two/data/extcode/sage/<ipython console> in <module>
)\n\nNameError: name 'x' is not defined\n"
**********************************************************************
File "/Users/craigcitro/three-oh-two/tmp/sage0.py", line 326:
    sage: sage0._contains('2', 'QQ')
Expected:
    True
Got:
    False
**********************************************************************
File "/Users/craigcitro/three-oh-two/tmp/sage0.py", line 350:
    sage: sage0.version() == version()
Expected:
    True
Got:
    False
**********************************************************************
File "/Users/craigcitro/three-oh-two/tmp/sage0.py", line 487:
    sage: sage0_version() == version()
Expected:
    True
Got:
    False
**********************************************************************
File "/Users/craigcitro/three-oh-two/tmp/sage0.py", line 177:
    sage: s.eval('2+2')
Expected:
    '4'
Got:
    '4\n'
**********************************************************************
8 items had failures:
   1 of   3 in __main__.example_10
   1 of   4 in __main__.example_11
   1 of   4 in __main__.example_12
   2 of   6 in __main__.example_13
   1 of   3 in __main__.example_14
   1 of   4 in __main__.example_16
   1 of   4 in __main__.example_26
   1 of   5 in __main__.example_5
***Test Failed*** 9 failures.
For whitespace errors, see the file /Users/craigcitro/three-oh-two/tmp/.doctest
sage0.py
         [9.7 s]
exit code: 1024
```


Issue created by migration from https://trac.sagemath.org/ticket/4112





---

archive/issue_comments_029781.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-09-14T09:01:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4112#issuecomment-29781",
    "user": "craigcitro"
}
```

Attachment



---

archive/issue_comments_029782.json:
```json
{
    "body": "Attachment\n\nPositive review for trac-4112.patch. There is also some orthogonal issue, but that is followed up at #4116.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-14T09:34:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4112#issuecomment-29782",
    "user": "mabshoff"
}
```

Attachment

Positive review for trac-4112.patch. There is also some orthogonal issue, but that is followed up at #4116.

Cheers,

Michael



---

archive/issue_comments_029783.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-14T09:36:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4112#issuecomment-29783",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029784.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc3",
    "created_at": "2008-09-14T09:36:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4112",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4112#issuecomment-29784",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc3
