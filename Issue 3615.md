# Issue 3615: update constructions document for solving linear equations.

archive/issues_003615.json:
```json
{
    "body": "Assignee: tba\n\nhttp://modular.math.washington.edu/sage/doc/html/const/node35.html\n\nSage can do far better than what's there:\n\n\n```\n<mhansen> sage: matrix(ZZ, [[1,2],[3,5]]) \\ vector([5,6])\n<mhansen> (-13, 9)\n<mhansen> sage: matrix(RR, [[1,2],[3,5]]) \\ vector([5,6])\n<mhansen> (-13.0000000000000, 9.00000000000000)\n<mhansen> sage: matrix(RIF, [[1,2],[3,5]]) \\ vector([5,6])\n<mhansen> ([-13.000000000000000 .. -13.000000000000000], [9.0000000000000000 .. 9.0000000000000000])\n<mhansen> sage: matrix(CDF, [[1,2],[3,5]]) \\ vector([5,6])\n<mhansen> (-13.0, 9.0)\n<mhansen> sage: a,b = var('a,b')\n<mhansen> sage: matrix(SR, [[1,2],[3,5]]) \\ vector([a,b])\n<mhansen> (a - 2*(3*a - b), 3*a - b)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3615\n\n",
    "created_at": "2008-07-08T18:55:06Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "update constructions document for solving linear equations.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3615",
    "user": "mhansen"
}
```
Assignee: tba

http://modular.math.washington.edu/sage/doc/html/const/node35.html

Sage can do far better than what's there:


```
<mhansen> sage: matrix(ZZ, [[1,2],[3,5]]) \ vector([5,6])
<mhansen> (-13, 9)
<mhansen> sage: matrix(RR, [[1,2],[3,5]]) \ vector([5,6])
<mhansen> (-13.0000000000000, 9.00000000000000)
<mhansen> sage: matrix(RIF, [[1,2],[3,5]]) \ vector([5,6])
<mhansen> ([-13.000000000000000 .. -13.000000000000000], [9.0000000000000000 .. 9.0000000000000000])
<mhansen> sage: matrix(CDF, [[1,2],[3,5]]) \ vector([5,6])
<mhansen> (-13.0, 9.0)
<mhansen> sage: a,b = var('a,b')
<mhansen> sage: matrix(SR, [[1,2],[3,5]]) \ vector([a,b])
<mhansen> (a - 2*(3*a - b), 3*a - b)
```


Issue created by migration from https://trac.sagemath.org/ticket/3615





---

archive/issue_comments_025519.json:
```json
{
    "body": "If you are suggesting to add these I'd be happy to create a patch for it. Or are you suggesting to make a replacement?",
    "created_at": "2008-07-08T22:36:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3615#issuecomment-25519",
    "user": "wdj"
}
```

If you are suggesting to add these I'd be happy to create a patch for it. Or are you suggesting to make a replacement?



---

archive/issue_comments_025520.json:
```json
{
    "body": "Replying to [ticket:3615 mhansen]:\n> http://modular.math.washington.edu/sage/doc/html/const/node35.html\n[...]\n\nThis URL gave me an \"Object not found!\" message. But here's a link to the official online version\n[http://www.sagemath.org/doc/const/node35.html](http://www.sagemath.org/doc/const/node35.html)",
    "created_at": "2008-09-19T20:52:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3615",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3615#issuecomment-25520",
    "user": "mvngu"
}
```

Replying to [ticket:3615 mhansen]:
> http://modular.math.washington.edu/sage/doc/html/const/node35.html
[...]

This URL gave me an "Object not found!" message. But here's a link to the official online version
[http://www.sagemath.org/doc/const/node35.html](http://www.sagemath.org/doc/const/node35.html)
