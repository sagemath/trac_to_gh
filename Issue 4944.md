# Issue 4944: speed regression in finding roots over number fields when an embedding is specified

archive/issues_004944.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  robertwb was\n\nKeywords: roots number field embedding\n\n\n```\nsage: x = ZZ['x'].0; (x^2 + 1).roots(NumberField(x^2 - 106*x + 2789, 'a', embedding=CC.0))\n```\n\n\nDoesn't terminate in reasonable time on sage.math or my Mac OS X box.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4944\n\n",
    "created_at": "2009-01-06T00:48:32Z",
    "labels": [
        "number theory",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "speed regression in finding roots over number fields when an embedding is specified",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4944",
    "user": "@ncalexan"
}
```
Assignee: @williamstein

CC:  robertwb was

Keywords: roots number field embedding


```
sage: x = ZZ['x'].0; (x^2 + 1).roots(NumberField(x^2 - 106*x + 2789, 'a', embedding=CC.0))
```


Doesn't terminate in reasonable time on sage.math or my Mac OS X box.

Issue created by migration from https://trac.sagemath.org/ticket/4944





---

archive/issue_comments_037530.json:
```json
{
    "body": "Nick,\n\nthis looks similar to #4723 and there is a patch from Carl. The patch over there (which isn't merged yet) fixes the problem for me. Before I killed it after 10 seconds CPU time, with the patch applied:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: time x = ZZ['x'].0; (x^2 + 1).roots(NumberField(x^2 - 106*x + 2789, 'a', embedding=CC.0))\nCPU times: user 0.02 s, sys: 0.01 s, total: 0.03 s\nWall time: 0.03 s\nsage: x = ZZ['x'].0; (x^2 + 1).roots(NumberField(x^2 - 106*x + 2789, 'a', embedding=CC.0))\n[]\n```\n\nIronically the other issue was also reported by you :)\n| Sage Version 3.2.3.final, Release Date: 2009-01-02                 |\n| Type notebook() for the GUI, and license() for information.        |\nCheers,\n\nMichael",
    "created_at": "2009-01-06T01:07:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4944#issuecomment-37530",
    "user": "mabshoff"
}
```

Nick,

this looks similar to #4723 and there is a patch from Carl. The patch over there (which isn't merged yet) fixes the problem for me. Before I killed it after 10 seconds CPU time, with the patch applied:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: time x = ZZ['x'].0; (x^2 + 1).roots(NumberField(x^2 - 106*x + 2789, 'a', embedding=CC.0))
CPU times: user 0.02 s, sys: 0.01 s, total: 0.03 s
Wall time: 0.03 s
sage: x = ZZ['x'].0; (x^2 + 1).roots(NumberField(x^2 - 106*x + 2789, 'a', embedding=CC.0))
[]
```

Ironically the other issue was also reported by you :)
| Sage Version 3.2.3.final, Release Date: 2009-01-02                 |
| Type notebook() for the GUI, and license() for information.        |
Cheers,

Michael



---

archive/issue_comments_037531.json:
```json
{
    "body": "This won't make it into 3.2.3, better luck in 3.3. I also assume this is a dupe since Carl's patch fixes the problem (unless the new patch doesn't find some roots, etc).\n\nCheers,\n\nMichael",
    "created_at": "2009-01-06T02:37:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4944#issuecomment-37531",
    "user": "mabshoff"
}
```

This won't make it into 3.2.3, better luck in 3.3. I also assume this is a dupe since Carl's patch fixes the problem (unless the new patch doesn't find some roots, etc).

Cheers,

Michael



---

archive/issue_comments_037532.json:
```json
{
    "body": "The patch for #4723 fixes this.",
    "created_at": "2009-01-17T06:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4944#issuecomment-37532",
    "user": "@ncalexan"
}
```

The patch for #4723 fixes this.



---

archive/issue_comments_037533.json:
```json
{
    "body": "Fixed by merging #4723.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-18T15:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4944#issuecomment-37533",
    "user": "mabshoff"
}
```

Fixed by merging #4723.

Cheers,

Michael



---

archive/issue_comments_037534.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-18T15:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4944#issuecomment-37534",
    "user": "mabshoff"
}
```

Resolution: fixed
