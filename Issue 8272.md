# Issue 8272: R's spkg-install tries to disable iconv, but it is *essential* for R.

archive/issues_008272.json:
```json
{
    "body": "Assignee: amhou\n\nR has long since wanted iconv support, although there was an option to disable it. That option has now been removed, and R **must** have iconv. However, there is junk left over in R's spkg-install which tries to disable iconv, and reports it is doing so. \n\n\n```\nDisabling libiconv support on Solaris\n```\n\n\nIt likewise tries to do that same on OS X. \n\nIssue created by migration from https://trac.sagemath.org/ticket/8272\n\n",
    "created_at": "2010-02-15T11:17:11Z",
    "labels": [
        "statistics",
        "major",
        "bug"
    ],
    "title": "R's spkg-install tries to disable iconv, but it is *essential* for R.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8272",
    "user": "drkirkby"
}
```
Assignee: amhou

R has long since wanted iconv support, although there was an option to disable it. That option has now been removed, and R **must** have iconv. However, there is junk left over in R's spkg-install which tries to disable iconv, and reports it is doing so. 


```
Disabling libiconv support on Solaris
```


It likewise tries to do that same on OS X. 

Issue created by migration from https://trac.sagemath.org/ticket/8272





---

archive/issue_comments_073220.json:
```json
{
    "body": "#8285 addresses this issue, along with several other issues.",
    "created_at": "2010-02-17T01:02:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8272#issuecomment-73220",
    "user": "drkirkby"
}
```

#8285 addresses this issue, along with several other issues.



---

archive/issue_comments_073221.json:
```json
{
    "body": "This has long been resolved, so can be closed.",
    "created_at": "2010-07-19T07:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8272#issuecomment-73221",
    "user": "drkirkby"
}
```

This has long been resolved, so can be closed.



---

archive/issue_comments_073222.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-19T07:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8272#issuecomment-73222",
    "user": "drkirkby"
}
```

Resolution: fixed
