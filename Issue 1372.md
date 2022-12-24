# Issue 1372: 2.8.15.alpha2: dokchitser.py doctest failure (numerical noise)

archive/issues_001372.json:
```json
{
    "body": "Assignee: mabshoff\n\nJaap reports on Linux FC7, 32 bit:\n\n```\nFile \"dokchitser.py\", line 384:\n     sage: L.taylor_series(1,3)\nExpected:\n     6.2239725530250970363983975962696997888173850098274602272589e-73 + (-3.5271062035449946049211903242820246129524508593200000161038e-73)*z + \n0.75931650028842677023019260789472201907809751649492435158581*z^2 + O(z^3)\nGot:\n     6.2239725530250970363983975962696997888173850098274602272589e-73 + (-3.5271062035449946049211903242820246129524508593201400619235e-73)*z + \n0.75931650028842677023019260789472201907809751649492435158581*z^2 + O(z^3)\n**********************************************************************\n1 items had failures:\n    1 of   8 in __main__.example_7\n***Test Failed*** 1 failures.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1372\n\n",
    "created_at": "2007-12-02T16:34:43Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "2.8.15.alpha2: dokchitser.py doctest failure (numerical noise)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1372",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Jaap reports on Linux FC7, 32 bit:

```
File "dokchitser.py", line 384:
     sage: L.taylor_series(1,3)
Expected:
     6.2239725530250970363983975962696997888173850098274602272589e-73 + (-3.5271062035449946049211903242820246129524508593200000161038e-73)*z + 
0.75931650028842677023019260789472201907809751649492435158581*z^2 + O(z^3)
Got:
     6.2239725530250970363983975962696997888173850098274602272589e-73 + (-3.5271062035449946049211903242820246129524508593201400619235e-73)*z + 
0.75931650028842677023019260789472201907809751649492435158581*z^2 + O(z^3)
**********************************************************************
1 items had failures:
    1 of   8 in __main__.example_7
***Test Failed*** 1 failures.
```


Issue created by migration from https://trac.sagemath.org/ticket/1372





---

archive/issue_comments_008805.json:
```json
{
    "body": "Attachment [Sage-2.8.15.alpha2-fix-dokchitser-doctest-FC7-32bit.patch](tarball://root/attachments/some-uuid/ticket1372/Sage-2.8.15.alpha2-fix-dokchitser-doctest-FC7-32bit.patch) by mabshoff created at 2007-12-02 16:38:46",
    "created_at": "2007-12-02T16:38:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1372#issuecomment-8805",
    "user": "mabshoff"
}
```

Attachment [Sage-2.8.15.alpha2-fix-dokchitser-doctest-FC7-32bit.patch](tarball://root/attachments/some-uuid/ticket1372/Sage-2.8.15.alpha2-fix-dokchitser-doctest-FC7-32bit.patch) by mabshoff created at 2007-12-02 16:38:46



---

archive/issue_comments_008806.json:
```json
{
    "body": "Merged in 2.8.15.rc0.",
    "created_at": "2007-12-02T22:10:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1372#issuecomment-8806",
    "user": "mabshoff"
}
```

Merged in 2.8.15.rc0.



---

archive/issue_comments_008807.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-02T22:10:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1372#issuecomment-8807",
    "user": "mabshoff"
}
```

Resolution: fixed
