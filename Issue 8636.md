# Issue 8636: iconv -- put the "do not build check" in the right place

archive/issues_008636.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nNew spkg here\n\n   http://boxen.math.washington.edu/home/wstein/patches/iconv-1.13.1.p1.spkg\n\nI've already posted this to the sagemath.org website, so people get it when they upgrade.   However, it's critical that it go into sage-4.4, or the problem will just reappear. \n\nIssue created by migration from https://trac.sagemath.org/ticket/8636\n\n",
    "created_at": "2010-03-31T15:22:15Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "title": "iconv -- put the \"do not build check\" in the right place",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8636",
    "user": "was"
}
```
Assignee: GeorgSWeber

New spkg here

   http://boxen.math.washington.edu/home/wstein/patches/iconv-1.13.1.p1.spkg

I've already posted this to the sagemath.org website, so people get it when they upgrade.   However, it's critical that it go into sage-4.4, or the problem will just reappear. 

Issue created by migration from https://trac.sagemath.org/ticket/8636





---

archive/issue_comments_078317.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-31T15:51:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8636#issuecomment-78317",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078318.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-31T16:24:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8636#issuecomment-78318",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078319.json:
```json
{
    "body": "First, the code is obviously right.  Second, it works: starting with Sage 4.3.4, force-installing the previous version of the iconv spkg breaks Sage 4.3.4 on platforms other than Solaris or Cygwin.  Force-installing this one doesn't.",
    "created_at": "2010-03-31T16:32:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8636#issuecomment-78319",
    "user": "jhpalmieri"
}
```

First, the code is obviously right.  Second, it works: starting with Sage 4.3.4, force-installing the previous version of the iconv spkg breaks Sage 4.3.4 on platforms other than Solaris or Cygwin.  Force-installing this one doesn't.



---

archive/issue_comments_078320.json:
```json
{
    "body": "Merged spkg from #8638 in 4.4.alpha0.",
    "created_at": "2010-04-16T17:22:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8636#issuecomment-78320",
    "user": "jhpalmieri"
}
```

Merged spkg from #8638 in 4.4.alpha0.



---

archive/issue_comments_078321.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-16T17:22:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8636",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8636#issuecomment-78321",
    "user": "jhpalmieri"
}
```

Resolution: fixed
