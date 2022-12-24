# Issue 2982: Itanium (RHEL 5) -- weird problem in code_construction.py

archive/issues_002982.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nsage -t  devel/sage/sage/coding/code_constructions.py       **********************************************************************\nFile \"/home/wstein/sage-3.0.rc0/tmp/code_constructions.py\", line 1121:\n    sage: C.minimum_distance()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wstein/sage-3.0.rc0/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_22[4]>\", line 1, in <module>\n        C.minimum_distance()###line 1121:\n    sage: C.minimum_distance()\n      File \"/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py\", line 1269, in minimum_distance\n        return hamming_weight(min_wt_vec(Gstr,F))\n      File \"/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py\", line 243, in min_wt_vec\n        c = [gfq_gap_to_sage(cg[j],F) for j in range(1,n+1)]\n      File \"/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/interfaces/gap.py\", line 778, in gfq_gap_to_sage\n        K = FiniteField(q, F.variable_name())\n      File \"/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/rings/finite_field.py\", line 240, in FiniteField\n        raise ValueError, \"order of finite field must be a prime power\"\n    ValueError: order of finite field must be a prime power\n**********************************************************************\n1 items had failures:\n   1 of  10 in __main__.example_22\n***Test Failed*** 1 failures.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2982\n\n",
    "created_at": "2008-04-21T03:23:24Z",
    "labels": [
        "porting",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Itanium (RHEL 5) -- weird problem in code_construction.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2982",
    "user": "@williamstein"
}
```
Assignee: mabshoff


```
sage -t  devel/sage/sage/coding/code_constructions.py       **********************************************************************
File "/home/wstein/sage-3.0.rc0/tmp/code_constructions.py", line 1121:
    sage: C.minimum_distance()
Exception raised:
    Traceback (most recent call last):
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_22[4]>", line 1, in <module>
        C.minimum_distance()###line 1121:
    sage: C.minimum_distance()
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 1269, in minimum_distance
        return hamming_weight(min_wt_vec(Gstr,F))
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/coding/linear_code.py", line 243, in min_wt_vec
        c = [gfq_gap_to_sage(cg[j],F) for j in range(1,n+1)]
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/interfaces/gap.py", line 778, in gfq_gap_to_sage
        K = FiniteField(q, F.variable_name())
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/rings/finite_field.py", line 240, in FiniteField
        raise ValueError, "order of finite field must be a prime power"
    ValueError: order of finite field must be a prime power
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_22
***Test Failed*** 1 failures.
```


Issue created by migration from https://trac.sagemath.org/ticket/2982





---

archive/issue_comments_020532.json:
```json
{
    "body": "This will be fixed by #2984.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-21T04:34:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2982#issuecomment-20532",
    "user": "mabshoff"
}
```

This will be fixed by #2984.

Cheers,

Michael



---

archive/issue_comments_020533.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-21T06:54:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2982#issuecomment-20533",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020534.json:
```json
{
    "body": "Fixed by merging #2984.",
    "created_at": "2008-04-21T06:54:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2982#issuecomment-20534",
    "user": "mabshoff"
}
```

Fixed by merging #2984.
