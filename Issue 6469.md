# Issue 6469: sage-4.1.rc0: numerical noise in graph.py

archive/issues_006469.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nsage -t  \"devel/sage/sage/graphs/graph.py\"\n**********************************************************************\nFile \"/home/jaap/downloads/sage-4.1.alpha2/devel/sage/sage/graphs/graph.py\", line 7144:\n     sage: T.spectrum()\nExpected:\n     [1, -0.500000000000000? + 0.866025403784439?*I, -0.500000000000000? - 0.866025403784439?*I]\nGot:\n     [1, -0.50000000000000000? + 0.866025403784439?*I, -0.500000000000000? - 0.866025403784439?*I]\n**********************************************************************\nFile \"/home/jaap/downloads/sage-4.1.alpha2/devel/sage/sage/graphs/graph.py\", line 7272:\n     sage: T.eigenvectors()\nExpected:\n     [(1, [\n     (1, 1, 1)\n     ], 1), (-0.500000000000000? - 0.866025403784439?*I, [(1, -0.500000000000000? - 0.866025403784439?*I, -0.500000000000000? + 0.866025403784439?*I)], 1),\n(-0.500000000000000? + 0.866025403784439?*I, [(1, -0.500000000000000? + 0.866025403784439?*I, -0.500000000000000? - 0.866025403784439?*I)], 1)]\nGot:\n     [(1, [\n     (1, 1, 1)\n     ], 1), (-0.500000000000000? - 0.866025403784439?*I, [(1, -0.500000000000000? - 0.866025403784439?*I, -0.500000000000000? + 0.866025403784439?*I)], 1),\n(-0.50000000000000000? + 0.866025403784439?*I, [(1, -0.50000000000000000? + 0.866025403784439?*I, -0.50000000000000000? - 0.866025403784439?*I)], 1)]\n********************************************************************** \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6469\n\n",
    "created_at": "2009-07-06T17:33:15Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "sage-4.1.rc0: numerical noise in graph.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6469",
    "user": "rlm"
}
```
Assignee: tbd


```
sage -t  "devel/sage/sage/graphs/graph.py"
**********************************************************************
File "/home/jaap/downloads/sage-4.1.alpha2/devel/sage/sage/graphs/graph.py", line 7144:
     sage: T.spectrum()
Expected:
     [1, -0.500000000000000? + 0.866025403784439?*I, -0.500000000000000? - 0.866025403784439?*I]
Got:
     [1, -0.50000000000000000? + 0.866025403784439?*I, -0.500000000000000? - 0.866025403784439?*I]
**********************************************************************
File "/home/jaap/downloads/sage-4.1.alpha2/devel/sage/sage/graphs/graph.py", line 7272:
     sage: T.eigenvectors()
Expected:
     [(1, [
     (1, 1, 1)
     ], 1), (-0.500000000000000? - 0.866025403784439?*I, [(1, -0.500000000000000? - 0.866025403784439?*I, -0.500000000000000? + 0.866025403784439?*I)], 1),
(-0.500000000000000? + 0.866025403784439?*I, [(1, -0.500000000000000? + 0.866025403784439?*I, -0.500000000000000? - 0.866025403784439?*I)], 1)]
Got:
     [(1, [
     (1, 1, 1)
     ], 1), (-0.500000000000000? - 0.866025403784439?*I, [(1, -0.500000000000000? - 0.866025403784439?*I, -0.500000000000000? + 0.866025403784439?*I)], 1),
(-0.50000000000000000? + 0.866025403784439?*I, [(1, -0.50000000000000000? + 0.866025403784439?*I, -0.50000000000000000? - 0.866025403784439?*I)], 1)]
********************************************************************** 
```


Issue created by migration from https://trac.sagemath.org/ticket/6469





---

archive/issue_comments_052299.json:
```json
{
    "body": "Attachment [trac_6469_eigenvalue_noise.patch](tarball://root/attachments/some-uuid/ticket6469/trac_6469_eigenvalue_noise.patch) by rbeezer created at 2009-07-07 00:21:40\n\nDoctests added in #6258 are failing on some systems due to slightly different degrees of accuracy.  This patch truncates each non-integer value to 10 digits in these doctests.  Documentation builds fine, and sage/graphs/graph.py passes all tests on 64-bit Ubuntu 9.04 on Intel.",
    "created_at": "2009-07-07T00:21:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6469#issuecomment-52299",
    "user": "rbeezer"
}
```

Attachment [trac_6469_eigenvalue_noise.patch](tarball://root/attachments/some-uuid/ticket6469/trac_6469_eigenvalue_noise.patch) by rbeezer created at 2009-07-07 00:21:40

Doctests added in #6258 are failing on some systems due to slightly different degrees of accuracy.  This patch truncates each non-integer value to 10 digits in these doctests.  Documentation builds fine, and sage/graphs/graph.py passes all tests on 64-bit Ubuntu 9.04 on Intel.



---

archive/issue_comments_052300.json:
```json
{
    "body": "with patch graph testing passes on 32 bit Arch, so probably also on other platforms where it was failing",
    "created_at": "2009-07-07T09:05:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6469#issuecomment-52300",
    "user": "aginiewicz"
}
```

with patch graph testing passes on 32 bit Arch, so probably also on other platforms where it was failing



---

archive/issue_comments_052301.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-07T19:57:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6469#issuecomment-52301",
    "user": "rlm"
}
```

Resolution: fixed
