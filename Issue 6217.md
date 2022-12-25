# Issue 6217: [with patch, needs review] fix issues with sorting in formal_sum

archive/issues_006217.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nOk, note that this is rc1 on Fedora 10, 32 bit:\n\nThe followin tests failed:\n\n\nsage -t  \"devel/sage/sage/structure/formal_sum.py\"\n**********************************************************************\nFile \"/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/structure/formal_sum.py\", line 293:\n    sage: for z in FormalSum([(1,2), (5, 'a'), (-3, 7)]): print z\nExpected:\n    (5, 'a')\n    (1, 2)\n    (-3, 7)\nGot:\n    (1, 2)\n    (-3, 7)\n    (5, 'a')\n**********************************************************************\nFile \"/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/structure/formal_sum.py\", line 304:\n    sage: v = FormalSum([(1,2), (5, 'a'), (-3, 7)]); v\nExpected:\n    5*a + 2 - 3*7\nGot:\n    2 - 3*7 + 5*a\n**********************************************************************\nFile \"/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/structure/formal_sum.py\", line 306:\n    sage: v[0]         # indirect doctest\nExpected:\n    (5, 'a')\nGot:\n    (1, 2)\n**********************************************************************\nFile \"/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/structure/formal_sum.py\", line 308:\n    sage: v[1]\nExpected:\n    (1, 2)\nGot:\n    (-3, 7)\n**********************************************************************\nFile \"/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/structure/formal_sum.py\", line 310:\n    sage: v[2]\nExpected:\n    (-3, 7)\nGot:\n    (5, 'a')\n**********************************************************************\nFile \"/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/structure/formal_sum.py\", line 312:\n    sage: list(v)\nExpected:\n    [(5, 'a'), (1, 2), (-3, 7)]\nGot:\n    [(1, 2), (-3, 7), (5, 'a')]\n**********************************************************************\nFile \"/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/structure/formal_sum.py\", line 321:\n    sage: v = FormalSum([(1,2), (5, 'a'), (-3, 7)]); v\nExpected:\n    5*a + 2 - 3*7\nGot:\n    2 - 3*7 + 5*a\n**********************************************************************\n3 items had failures:\n   1 of   3 in __main__.example_12\n   5 of   7 in __main__.example_13\n   1 of   4 in __main__.example_14\n***Test Failed*** 7 failures.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6217\n\n",
    "created_at": "2009-06-05T00:22:10Z",
    "labels": [
        "component: basic arithmetic",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "[with patch, needs review] fix issues with sorting in formal_sum",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6217",
    "user": "https://github.com/mwhansen"
}
```
Assignee: somebody


```
Ok, note that this is rc1 on Fedora 10, 32 bit:

The followin tests failed:


sage -t  "devel/sage/sage/structure/formal_sum.py"
**********************************************************************
File "/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/structure/formal_sum.py", line 293:
    sage: for z in FormalSum([(1,2), (5, 'a'), (-3, 7)]): print z
Expected:
    (5, 'a')
    (1, 2)
    (-3, 7)
Got:
    (1, 2)
    (-3, 7)
    (5, 'a')
**********************************************************************
File "/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/structure/formal_sum.py", line 304:
    sage: v = FormalSum([(1,2), (5, 'a'), (-3, 7)]); v
Expected:
    5*a + 2 - 3*7
Got:
    2 - 3*7 + 5*a
**********************************************************************
File "/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/structure/formal_sum.py", line 306:
    sage: v[0]         # indirect doctest
Expected:
    (5, 'a')
Got:
    (1, 2)
**********************************************************************
File "/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/structure/formal_sum.py", line 308:
    sage: v[1]
Expected:
    (1, 2)
Got:
    (-3, 7)
**********************************************************************
File "/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/structure/formal_sum.py", line 310:
    sage: v[2]
Expected:
    (-3, 7)
Got:
    (5, 'a')
**********************************************************************
File "/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/structure/formal_sum.py", line 312:
    sage: list(v)
Expected:
    [(5, 'a'), (1, 2), (-3, 7)]
Got:
    [(1, 2), (-3, 7), (5, 'a')]
**********************************************************************
File "/home/jaap/Download/sage-4.0.alpha0/devel/sage/sage/structure/formal_sum.py", line 321:
    sage: v = FormalSum([(1,2), (5, 'a'), (-3, 7)]); v
Expected:
    5*a + 2 - 3*7
Got:
    2 - 3*7 + 5*a
**********************************************************************
3 items had failures:
   1 of   3 in __main__.example_12
   5 of   7 in __main__.example_13
   1 of   4 in __main__.example_14
***Test Failed*** 7 failures.
```


Issue created by migration from https://trac.sagemath.org/ticket/6217





---

archive/issue_comments_049568.json:
```json
{
    "body": "Attachment [trac_6217.patch](tarball://root/attachments/some-uuid/ticket6217/trac_6217.patch) by @mwhansen created at 2009-06-05 00:53:15\n\nI've made it so that the examples don't use the string 'a' as a bases since that was causing problems for the sorting.",
    "created_at": "2009-06-05T00:53:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6217#issuecomment-49568",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_6217.patch](tarball://root/attachments/some-uuid/ticket6217/trac_6217.patch) by @mwhansen created at 2009-06-05 00:53:15

I've made it so that the examples don't use the string 'a' as a bases since that was causing problems for the sorting.



---

archive/issue_comments_049569.json:
```json
{
    "body": "merged in 4.0.1.rc3",
    "created_at": "2009-06-06T16:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6217#issuecomment-49569",
    "user": "https://github.com/williamstein"
}
```

merged in 4.0.1.rc3



---

archive/issue_comments_049570.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-06T16:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6217",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6217#issuecomment-49570",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
