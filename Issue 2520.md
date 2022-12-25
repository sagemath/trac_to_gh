# Issue 2520: 2.10.4.a0: doctest failures in combinatorics after merging #2489

archive/issues_002520.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\n\n```\nsage -t -long devel/sage-main/sage/libs/symmetrica/kostka.pxi\n**********************************************************************\nFile \"kostka.py\", line 67:\n    sage: symmetrica.kostka_tab([2,1],[1,1,1])\nExpected:\n    [[[1, 2], [3]], [[1, 3], [2]]]\nGot:\n    [[[1, 2], [3, None]], [[1, 3], [2, None]]]\n**********************************************************************\n1 items had failures:\n   1 of   5 in __main__.example_1\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file .doctest_kostka.pxi\n         [2.2 s]\nexit code: 256\n```\n\nand\n\n```\nsage -t -long devel/sage-main/sage/combinat/tableau.py\n**********************************************************************\nFile \"tableau.py\", line 1457:\n    sage: SST.list()\nExpected:\n    [[[1, 1], [2]],\n     [[1, 1], [3]],\n     [[1, 2], [2]],\n     [[1, 2], [3]],\n     [[1, 3], [2]],\n     [[1, 3], [3]],\n     [[2, 2], [3]],\n     [[2, 3], [3]]]\nGot:\n    [[[1, 1], [2, None]], [[1, 1], [3, None]], [[1, 2], [2, None]], [[1, 2], [3, None]], [[1, 3], [2, None]], [[1, 3], [3, None]], [[2, 2], [3, None]], [[2, 3], [3, None]]]\n**********************************************************************\nFile \"tableau.py\", line 1470:\n    sage: SST.list()\nExpected:\n    [[[1, 1, 1]],\n     [[1, 1, 2]],\n     [[1, 1, 3]],\n     [[1, 2, 2]],\n     [[1, 2, 3]],\n     [[1, 3, 3]],\n     [[2, 2, 2]],\n     [[2, 2, 3]],\n     [[2, 3, 3]],\n     [[3, 3, 3]],\n     [[1, 1], [2]],\n     [[1, 1], [3]],\n     [[1, 2], [2]],\n     [[1, 2], [3]],\n     [[1, 3], [2]],\n     [[1, 3], [3]],\n     [[2, 2], [3]],\n     [[2, 3], [3]],\n     [[1], [2], [3]]]\nGot:\n    [[[1, 1, 1]], [[1, 1, 2]], [[1, 1, 3]], [[1, 2, 2]], [[1, 2, 3]], [[1, 3, 3]], [[2, 2, 2]], [[2, 2, 3]], [[2, 3, 3]], [[3, 3, 3]], [[1, 1], [2, None]], [[1, 1], [3, None]], [[1, 2], [2, None]], [[1, 2], [3, None]], [[1, 3], [2, None]], [[1, 3], [3, None]], [[2, 2], [3, None]], [[2, 3], [3, None]], [[1], [2], [3]]]\n**********************************************************************\nFile \"tableau.py\", line 1597:\n    sage: all([sst in SST for sst in SST])\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"tableau.py\", line 1626:\n    sage: SemistandardTableaux(3).list()\nExpected:\n    [[[1, 1, 1]],\n     [[1, 1, 2]],\n     [[1, 1, 3]],\n     [[1, 2, 2]],\n     [[1, 2, 3]],\n     [[1, 3, 3]],\n     [[2, 2, 2]],\n     [[2, 2, 3]],\n     [[2, 3, 3]],\n     [[3, 3, 3]],\n     [[1, 1], [2]],\n     [[1, 1], [3]],\n     [[1, 2], [2]],\n     [[1, 2], [3]],\n     [[1, 3], [2]],\n     [[1, 3], [3]],\n     [[2, 2], [3]],\n     [[2, 3], [3]],\n     [[1], [2], [3]]]\nGot:\n    [[[1, 1, 1]], [[1, 1, 2]], [[1, 1, 3]], [[1, 2, 2]], [[1, 2, 3]], [[1, 3, 3]], [[2, 2, 2]], [[2, 2, 3]], [[2, 3, 3]], [[3, 3, 3]], [[1, 1], [2, None]], [[1, 1], [3, None]], [[1, 2], [2, None]], [[1, 2], [3, None]], [[1, 3], [2, None]], [[1, 3], [3, None]], [[2, 2], [3, None]], [[2, 3], [3, None]], [[1], [2], [3]]]\n**********************************************************************\nFile \"tableau.py\", line 1677:\n    sage: all([sst in SST for sst in SST])\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"tableau.py\", line 1679:\n    sage: len(filter(lambda x: x in SST, SemistandardTableaux(3)))\nExpected:\n    1\nGot:\n    0\n**********************************************************************\nFile \"tableau.py\", line 1730:\n    sage: SemistandardTableaux([3,2,1], [2, 2, 2]).list()\nExpected:\n    [[[1, 1, 2], [2, 3], [3]], [[1, 1, 3], [2, 2], [3]]]\nGot:\n    [[[1, 1, 2], [2, 3, None], [3, None, None]], [[1, 1, 3], [2, 2, None], [3, None, None]]]\n**********************************************************************\nFile \"tableau.py\", line 1752:\n    sage: all([sst in SST for sst in SST])\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"tableau.py\", line 1754:\n    sage: len(filter(lambda x: x in SST, SemistandardTableaux(3)))\nExpected:\n    8\nGot:\n    0\n**********************************************************************\nFile \"tableau.py\", line 1805:\n    sage: SemistandardTableaux([2,1]).list()\nExpected:\n    [[[1, 1], [2]],\n     [[1, 1], [3]],\n     [[1, 2], [2]],\n     [[1, 2], [3]],\n     [[1, 3], [2]],\n     [[1, 3], [3]],\n     [[2, 2], [3]],\n     [[2, 3], [3]]]\nGot:\n    [[[1, 1], [2, None]], [[1, 1], [3, None]], [[1, 2], [2, None]], [[1, 2], [3, None]], [[1, 3], [2, None]], [[1, 3], [3, None]], [[2, 2], [3, None]], [[2, 3], [3, None]]]\n**********************************************************************\nFile \"tableau.py\", line 1843:\n    sage: SemistandardTableaux(3, [2,1]).list()\nExpected:\n    [[[1, 1, 2]], [[1, 1], [2]]]\nGot:\n    [[[1, 1, 2]], [[1, 1], [2, None]]]\n**********************************************************************\nFile \"tableau.py\", line 1845:\n    sage: SemistandardTableaux(4, [2,2]).list()\nExpected:\n    [[[1, 1, 2, 2]], [[1, 1, 2], [2]], [[1, 1], [2, 2]]]\nGot:\n    [[[1, 1, 2, 2]], [[1, 1, 2], [2, None, None]], [[1, 1], [2, 2]]]\n**********************************************************************\nFile \"tableau.py\", line 1869:\n    sage: all([sst in SST for sst in SST])\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"tableau.py\", line 1871:\n    sage: all([sst in SST for sst in SemistandardTableaux([3,2,1],[2,2,2])])\nExpected:\n    True\nGot:\n    False\n**********************************************************************\n9 items had failures:\n   2 of   4 in __main__.example_69\n   1 of   4 in __main__.example_75\n   1 of   2 in __main__.example_77\n   2 of   4 in __main__.example_80\n   1 of   4 in __main__.example_82\n   2 of   4 in __main__.example_84\n   1 of   3 in __main__.example_87\n   2 of   2 in __main__.example_90\n   2 of   3 in __main__.example_92\n***Test Failed*** 14 failures.\nFor whitespace errors, see the file .doctest_tableau.py\n         [3.5 s]\nexit code: 256\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t -long devel/sage-main/sage/combinat/tableau.py\nTotal time for all tests: 3.5 seconds\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2520\n\n",
    "created_at": "2008-03-14T21:10:40Z",
    "labels": [
        "component: combinatorics",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "2.10.4.a0: doctest failures in combinatorics after merging #2489",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2520",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @mwhansen

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
    [[[1, 1, 1]],
     [[1, 1, 2]],
     [[1, 1, 3]],
     [[1, 2, 2]],
     [[1, 2, 3]],
     [[1, 3, 3]],
     [[2, 2, 2]],
     [[2, 2, 3]],
     [[2, 3, 3]],
     [[3, 3, 3]],
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
    [[[1, 1, 1]], [[1, 1, 2]], [[1, 1, 3]], [[1, 2, 2]], [[1, 2, 3]], [[1, 3, 3]], [[2, 2, 2]], [[2, 2, 3]], [[2, 3, 3]], [[3, 3, 3]], [[1, 1], [2, None]], [[1, 1], [3, None]], [[1, 2], [2, None]], [[1, 2], [3, None]], [[1, 3], [2, None]], [[1, 3], [3, None]], [[2, 2], [3, None]], [[2, 3], [3, None]], [[1], [2], [3]]]
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
    [[[1, 1, 1]],
     [[1, 1, 2]],
     [[1, 1, 3]],
     [[1, 2, 2]],
     [[1, 2, 3]],
     [[1, 3, 3]],
     [[2, 2, 2]],
     [[2, 2, 3]],
     [[2, 3, 3]],
     [[3, 3, 3]],
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
    [[[1, 1, 1]], [[1, 1, 2]], [[1, 1, 3]], [[1, 2, 2]], [[1, 2, 3]], [[1, 3, 3]], [[2, 2, 2]], [[2, 2, 3]], [[2, 3, 3]], [[3, 3, 3]], [[1, 1], [2, None]], [[1, 1], [3, None]], [[1, 2], [2, None]], [[1, 2], [3, None]], [[1, 3], [2, None]], [[1, 3], [3, None]], [[2, 2], [3, None]], [[2, 3], [3, None]], [[1], [2], [3]]]
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
    [[[1, 1, 2]], [[1, 1], [2]]]
Got:
    [[[1, 1, 2]], [[1, 1], [2, None]]]
**********************************************************************
File "tableau.py", line 1845:
    sage: SemistandardTableaux(4, [2,2]).list()
Expected:
    [[[1, 1, 2, 2]], [[1, 1, 2], [2]], [[1, 1], [2, 2]]]
Got:
    [[[1, 1, 2, 2]], [[1, 1, 2], [2, None, None]], [[1, 1], [2, 2]]]
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


Issue created by migration from https://trac.sagemath.org/ticket/2520





---

archive/issue_comments_017158.json:
```json
{
    "body": "Attachment [2520.patch](tarball://root/attachments/some-uuid/ticket2520/2520.patch) by @mwhansen created at 2008-03-14 21:25:12",
    "created_at": "2008-03-14T21:25:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2520#issuecomment-17158",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2520.patch](tarball://root/attachments/some-uuid/ticket2520/2520.patch) by @mwhansen created at 2008-03-14 21:25:12



---

archive/issue_comments_017159.json:
```json
{
    "body": "Patch looks good to me. mhansen explained me the finer details of what the patch does. Doctests pass again.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-14T21:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2520#issuecomment-17159",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me. mhansen explained me the finer details of what the patch does. Doctests pass again.

Cheers,

Michael



---

archive/issue_comments_017160.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-14T21:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2520#issuecomment-17160",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.4.alpha0



---

archive/issue_comments_017161.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-14T21:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2520#issuecomment-17161",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002701.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-14T21:45:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2520",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2520#event-2701"
}
```
