# Issue 2641: replace guava 3.1 by guava 3.3

archive/issues_002641.json:
```json
{
    "body": "Assignee: rlm\n\nThere is a significantly improved version of GUAVA (a GAP package) available.\nThe new tarball is at\nhttp://sage.math.washington.edu/home/wdj/guava/guava3.3.tar.gz\nThis new version has a new C code function for (quickly) computing the\nminimum distance of binary and ternary codes (accessed via the new GUAVA function MinimumWeight), and also includes Brouwer's patch which (I'm told) fixes some or all the memory problems which Leon's code suffered. The GUAVA part also has many new functions, especially new code constructions.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2641\n\n",
    "created_at": "2008-03-22T01:29:55Z",
    "labels": [
        "coding theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "replace guava 3.1 by guava 3.3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2641",
    "user": "wdj"
}
```
Assignee: rlm

There is a significantly improved version of GUAVA (a GAP package) available.
The new tarball is at
http://sage.math.washington.edu/home/wdj/guava/guava3.3.tar.gz
This new version has a new C code function for (quickly) computing the
minimum distance of binary and ternary codes (accessed via the new GUAVA function MinimumWeight), and also includes Brouwer's patch which (I'm told) fixes some or all the memory problems which Leon's code suffered. The GUAVA part also has many new functions, especially new code constructions.


Issue created by migration from https://trac.sagemath.org/ticket/2641





---

archive/issue_comments_018148.json:
```json
{
    "body": "This new gap version has been posted to\nhttp://sage.math.washington.edu/home/wdj/patches/gap-4.4.10.p3.spkg\nIt loads fine on sage 2.10.4 (using sage -f) and passes sage -testall",
    "created_at": "2008-03-30T16:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2641#issuecomment-18148",
    "user": "wdj"
}
```

This new gap version has been posted to
http://sage.math.washington.edu/home/wdj/patches/gap-4.4.10.p3.spkg
It loads fine on sage 2.10.4 (using sage -f) and passes sage -testall



---

archive/issue_comments_018149.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-03-30T17:38:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2641#issuecomment-18149",
    "user": "rlm"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_018150.json:
```json
{
    "body": "David: the spkg looks good. The only thing you didn't do was checking in the changed spkg-install and SPKG.txt into the repo. I did that and that spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/alpha0/gap-4.4.10.p3.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-03-31T14:04:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2641#issuecomment-18150",
    "user": "mabshoff"
}
```

David: the spkg looks good. The only thing you didn't do was checking in the changed spkg-install and SPKG.txt into the repo. I did that and that spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/alpha0/gap-4.4.10.p3.spkg

Cheers,

Michael



---

archive/issue_comments_018151.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-31T14:06:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2641#issuecomment-18151",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018152.json:
```json
{
    "body": "Merged in Sage 3.0.alpha0",
    "created_at": "2008-03-31T14:06:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2641",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2641#issuecomment-18152",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha0
