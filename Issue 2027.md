# Issue 2027: PolyBoRi.spkg: add one line patch to fix memleak

archive/issues_002027.json:
```json
{
    "body": "Assignee: mabshoff\n\nRPW applied Michael Brickenstein's patch to\n\nhttp://coderpunks.org/tmp/polybori-0.1-r7.spkg\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2027\n\n",
    "created_at": "2008-02-02T03:36:26Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "PolyBoRi.spkg: add one line patch to fix memleak",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2027",
    "user": "mabshoff"
}
```
Assignee: mabshoff

RPW applied Michael Brickenstein's patch to

http://coderpunks.org/tmp/polybori-0.1-r7.spkg

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/2027





---

archive/issue_comments_013113.json:
```json
{
    "body": "To be more precise about the changelog:\n\n* pulled in changes from PolyBoRi's SF CVS repo for a memleak fix in nf.cc\n* fixes to the comments. claims about potential patents were removed by PolyBoRi authors.\n\nUnfortunately this increased the spkg size by 2 mb. Once we update to PolyBoRi 2.0 we should consider resetting the hg changelog. I also checked in some outstanding small changes in `spkg-install`.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-02T03:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2027#issuecomment-13113",
    "user": "mabshoff"
}
```

To be more precise about the changelog:

* pulled in changes from PolyBoRi's SF CVS repo for a memleak fix in nf.cc
* fixes to the comments. claims about potential patents were removed by PolyBoRi authors.

Unfortunately this increased the spkg size by 2 mb. Once we update to PolyBoRi 2.0 we should consider resetting the hg changelog. I also checked in some outstanding small changes in `spkg-install`.

Cheers,

Michael



---

archive/issue_comments_013114.json:
```json
{
    "body": "Spkg compiles and passes `-testall` on OSX and Linux.",
    "created_at": "2008-02-02T05:20:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2027#issuecomment-13114",
    "user": "mabshoff"
}
```

Spkg compiles and passes `-testall` on OSX and Linux.



---

archive/issue_comments_013115.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc5",
    "created_at": "2008-02-02T05:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2027#issuecomment-13115",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.rc5



---

archive/issue_comments_013116.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-02T05:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2027",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2027#issuecomment-13116",
    "user": "mabshoff"
}
```

Resolution: fixed
