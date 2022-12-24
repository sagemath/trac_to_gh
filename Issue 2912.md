# Issue 2912: M4RI should be built with -O3

archive/issues_002912.json:
```json
{
    "body": "Assignee: was\n\nKeywords: speed, build system\n\n* it is fairly straight forward C so it shouldn't break under `-O3`\n* it makes a noticeable speed difference. To echelonise a random 10<sup>4</sup> x 10<sup>4</sup> matrix takes ~ 8 seconds with `-O2` and ~ 6 seconds with `-O3`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2912\n\n",
    "created_at": "2008-04-13T21:05:11Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "M4RI should be built with -O3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2912",
    "user": "malb"
}
```
Assignee: was

Keywords: speed, build system

* it is fairly straight forward C so it shouldn't break under `-O3`
* it makes a noticeable speed difference. To echelonise a random 10<sup>4</sup> x 10<sup>4</sup> matrix takes ~ 8 seconds with `-O2` and ~ 6 seconds with `-O3`.

Issue created by migration from https://trac.sagemath.org/ticket/2912





---

archive/issue_comments_020060.json:
```json
{
    "body": "New SPKG up at:\n\n   http://sage.math.washington.edu/home/malb/libm4ri-20071224.p2.spkg",
    "created_at": "2008-04-13T21:55:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2912#issuecomment-20060",
    "user": "malb"
}
```

New SPKG up at:

   http://sage.math.washington.edu/home/malb/libm4ri-20071224.p2.spkg



---

archive/issue_comments_020061.json:
```json
{
    "body": "Spkg looks good to me. Changes are minimal. We still need an SPKG.txt, but that can be done down the road. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-13T23:41:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2912#issuecomment-20061",
    "user": "mabshoff"
}
```

Spkg looks good to me. Changes are minimal. We still need an SPKG.txt, but that can be done down the road. Positive review.

Cheers,

Michael



---

archive/issue_comments_020062.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-13T23:42:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2912#issuecomment-20062",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020063.json:
```json
{
    "body": "Merged in Sage 3.0.alpha5",
    "created_at": "2008-04-13T23:42:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2912",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2912#issuecomment-20063",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha5
