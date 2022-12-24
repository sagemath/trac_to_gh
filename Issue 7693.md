# Issue 7693: the lrs SPKG.txt is not very useful.

archive/issues_007693.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  wstein\n\nThe lrs SPKG.txt is just:\n\n```\nwstein@boxen:/tmp/wstein/lrs-4.2b.p0$ more SPKG.txt\n* 2008-05-15 (Marshall Hampton)\n*initial build\n1. Deleted McGill-specific build stuff from makefile\n2. Added SAGE_LOCAL gmp build locations\n```\n\nFix this.  I was trying to figure out what the heck lrs is, and this wasn't helfpul. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7693\n\n",
    "created_at": "2009-12-15T23:07:40Z",
    "labels": [
        "packages: optional",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "the lrs SPKG.txt is not very useful.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7693",
    "user": "was"
}
```
Assignee: tbd

CC:  wstein

The lrs SPKG.txt is just:

```
wstein@boxen:/tmp/wstein/lrs-4.2b.p0$ more SPKG.txt
* 2008-05-15 (Marshall Hampton)
*initial build
1. Deleted McGill-specific build stuff from makefile
2. Added SAGE_LOCAL gmp build locations
```

Fix this.  I was trying to figure out what the heck lrs is, and this wasn't helfpul. 

Issue created by migration from https://trac.sagemath.org/ticket/7693





---

archive/issue_comments_066008.json:
```json
{
    "body": "Well, that's strange, I had a much better package that was supposedly included about a year ago:\n\nhttp://trac.sagemath.org/sage_trac/ticket/5018\n\nI hadn't noticed since the actual program hadn't changed from p0 to p1.  I did all the work on that to prepare this for being a standard package, which I think it should be.",
    "created_at": "2009-12-16T03:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7693#issuecomment-66008",
    "user": "mhampton"
}
```

Well, that's strange, I had a much better package that was supposedly included about a year ago:

http://trac.sagemath.org/sage_trac/ticket/5018

I hadn't noticed since the actual program hadn't changed from p0 to p1.  I did all the work on that to prepare this for being a standard package, which I think it should be.



---

archive/issue_comments_066009.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-16T03:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7693#issuecomment-66009",
    "user": "mhampton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066010.json:
```json
{
    "body": "IU fixed that #5018 was never actually uploaded.",
    "created_at": "2009-12-16T08:19:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7693#issuecomment-66010",
    "user": "was"
}
```

IU fixed that #5018 was never actually uploaded.



---

archive/issue_comments_066011.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-16T08:19:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7693#issuecomment-66011",
    "user": "was"
}
```

Resolution: fixed
