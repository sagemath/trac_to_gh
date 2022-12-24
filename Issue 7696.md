# Issue 7696: zlib -- source spkg contains precompiled binary crap (.obj files)

archive/issues_007696.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nzlib-1.2.3.p4/src/contrib/masmx86/inffas32.obj: 80386 COFF\nzlib-1.2.3.p4/src/contrib/masmx86/gvmat32.obj: 80386 COFF\nzlib-1.2.3.p4/src/contrib/masmx64/inffasx64.obj: ACB archive data\nzlib-1.2.3.p4/src/contrib/masmx64/gvmat64.obj: ACB archive data\n```\n\n\nDelete the above and it builds fine.  Similar directories don't have obj files.\n\nNote that the above is for Microsoft Windows anyways, so it's especially important we don't distribute their binary stuff!\n\nIssue created by migration from https://trac.sagemath.org/ticket/7696\n\n",
    "created_at": "2009-12-16T00:54:45Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "zlib -- source spkg contains precompiled binary crap (.obj files)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7696",
    "user": "was"
}
```
Assignee: tbd


```
zlib-1.2.3.p4/src/contrib/masmx86/inffas32.obj: 80386 COFF
zlib-1.2.3.p4/src/contrib/masmx86/gvmat32.obj: 80386 COFF
zlib-1.2.3.p4/src/contrib/masmx64/inffasx64.obj: ACB archive data
zlib-1.2.3.p4/src/contrib/masmx64/gvmat64.obj: ACB archive data
```


Delete the above and it builds fine.  Similar directories don't have obj files.

Note that the above is for Microsoft Windows anyways, so it's especially important we don't distribute their binary stuff!

Issue created by migration from https://trac.sagemath.org/ticket/7696





---

archive/issue_comments_066031.json:
```json
{
    "body": "The following new spkg deletes the binary crap *and* also greatly improves the SPKG.txt:\n\n    http://wstein.org/home/wstein/patches/zlib-1.2.3.p5.spkg",
    "created_at": "2009-12-18T06:17:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7696",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7696#issuecomment-66031",
    "user": "was"
}
```

The following new spkg deletes the binary crap *and* also greatly improves the SPKG.txt:

    http://wstein.org/home/wstein/patches/zlib-1.2.3.p5.spkg



---

archive/issue_comments_066032.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-18T06:17:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7696",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7696#issuecomment-66032",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066033.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-12-27T16:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7696",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7696#issuecomment-66033",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_066034.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-27T16:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7696",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7696#issuecomment-66034",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066035.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-03T22:23:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7696",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7696#issuecomment-66035",
    "user": "mhansen"
}
```

Resolution: fixed
