# Issue 6310: optional doctest failure

archive/issues_006310.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nsage -t -long --optional devel/sage/sage/schemes/elliptic_curves/ell_egros.py\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/elliptic_curves/ell_egros.py\", line 63:\n    sage: [e.label() for e in EllipticCurves_with_good_reduction_outside_S([11])]\nExpected:\n    Failed to find S-integral points on  [0, 0, 0, 0, -25299648]\n    Failed to find S-integral points on  [0, 0, 0, 0, -278296128]\n    ['11a1',\n    '11a2',\n    '11a3',\n    '121a1',\n    '121a2',\n    '121b1',\n    '121b2',\n    '121c1',\n    '121c2',\n    '121d1',\n    '121d2',\n    '121d3']\nGot:\n    ['11a1', '11a2', '11a3', '121a1', '121a2', '121b1', '121b2', '121c1', '121c2', '121d1', '121d2', '121d3']\n**********************************************************************\n1 items had failures:\n   1 of   4 in __main__.example_0\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_ell_egros.py\n\t [29.5 s]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6310\n\n",
    "created_at": "2009-06-16T14:39:31Z",
    "labels": [
        "packages: optional",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "optional doctest failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6310",
    "user": "was"
}
```
Assignee: tbd


```
sage -t -long --optional devel/sage/sage/schemes/elliptic_curves/ell_egros.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/schemes/elliptic_curves/ell_egros.py", line 63:
    sage: [e.label() for e in EllipticCurves_with_good_reduction_outside_S([11])]
Expected:
    Failed to find S-integral points on  [0, 0, 0, 0, -25299648]
    Failed to find S-integral points on  [0, 0, 0, 0, -278296128]
    ['11a1',
    '11a2',
    '11a3',
    '121a1',
    '121a2',
    '121b1',
    '121b2',
    '121c1',
    '121c2',
    '121d1',
    '121d2',
    '121d3']
Got:
    ['11a1', '11a2', '11a3', '121a1', '121a2', '121b1', '121b2', '121c1', '121c2', '121d1', '121d2', '121d3']
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_ell_egros.py
	 [29.5 s]
```


Issue created by migration from https://trac.sagemath.org/ticket/6310





---

archive/issue_comments_050365.json:
```json
{
    "body": "Was that with the large database installed?  that would make sense -- it needs the MW basis of the two curves whose conductors are 13068 and 52272, which it cannot find unless the optional package is installed.\n\nI don't think I know how to tag that test to expect two warnings lines iff that package is not installed.  Would it work to put an initial \"...\" in front of the output?",
    "created_at": "2009-06-16T14:45:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6310#issuecomment-50365",
    "user": "cremona"
}
```

Was that with the large database installed?  that would make sense -- it needs the MW basis of the two curves whose conductors are 13068 and 52272, which it cannot find unless the optional package is installed.

I don't think I know how to tag that test to expect two warnings lines iff that package is not installed.  Would it work to put an initial "..." in front of the output?



---

archive/issue_comments_050366.json:
```json
{
    "body": "applies to 4.0.2.rc2",
    "created_at": "2009-06-16T16:43:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6310#issuecomment-50366",
    "user": "cremona"
}
```

applies to 4.0.2.rc2



---

archive/issue_comments_050367.json:
```json
{
    "body": "Attachment [trac_6310.patch](tarball://root/attachments/some-uuid/ticket6310/trac_6310.patch) by cremona created at 2009-06-16 16:44:00\n\nI have fixed it by running that example with \"proof=False\" and explaining in the accompanying text that this is only needed to avoid warnings when the optional database is not installed.\n\nTested both with and without the database installed!",
    "created_at": "2009-06-16T16:44:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6310#issuecomment-50367",
    "user": "cremona"
}
```

Attachment [trac_6310.patch](tarball://root/attachments/some-uuid/ticket6310/trac_6310.patch) by cremona created at 2009-06-16 16:44:00

I have fixed it by running that example with "proof=False" and explaining in the accompanying text that this is only needed to avoid warnings when the optional database is not installed.

Tested both with and without the database installed!



---

archive/issue_comments_050368.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-23T03:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6310",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6310#issuecomment-50368",
    "user": "mvngu"
}
```

Resolution: fixed
