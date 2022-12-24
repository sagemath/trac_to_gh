# Issue 7689: cd spkg/; ./install scripts --- this results in an annoying (but harmless error message); get rid of it

archive/issues_007689.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nAn \"official\" way to setup the basic bootstrap for building Sage is to execute the following in an extracted Sage source tarball from SAGE_ROOT:\n\n```\ncd spkg/; ./install scripts\n```\n\n\nDoing so works, but unfortunately also results in:\n\n```\n...\npython: can't open file '/scratch/wstein/build/x/sage-4.3.rc0/devel/sage/doc/common/builder.py': [Errno 2] No such file or directory\n```\n\n\nFix this.  Get rid of this error message. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7689\n\n",
    "created_at": "2009-12-15T19:39:08Z",
    "labels": [
        "build",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "cd spkg/; ./install scripts --- this results in an annoying (but harmless error message); get rid of it",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7689",
    "user": "@williamstein"
}
```
Assignee: GeorgSWeber

An "official" way to setup the basic bootstrap for building Sage is to execute the following in an extracted Sage source tarball from SAGE_ROOT:

```
cd spkg/; ./install scripts
```


Doing so works, but unfortunately also results in:

```
...
python: can't open file '/scratch/wstein/build/x/sage-4.3.rc0/devel/sage/doc/common/builder.py': [Errno 2] No such file or directory
```


Fix this.  Get rid of this error message. 

Issue created by migration from https://trac.sagemath.org/ticket/7689





---

archive/issue_comments_065977.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-12-29T23:21:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7689#issuecomment-65977",
    "user": "@jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065978.json:
```json
{
    "body": "Currently, `cd build; ./install scripts` doesn't work and it certainly isn't an \"official\" way to bootstrap anything.",
    "created_at": "2013-12-29T23:21:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7689#issuecomment-65978",
    "user": "@jdemeyer"
}
```

Currently, `cd build; ./install scripts` doesn't work and it certainly isn't an "official" way to bootstrap anything.



---

archive/issue_comments_065979.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-01-04T00:04:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7689#issuecomment-65979",
    "user": "@jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065980.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2014-01-04T02:38:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7689",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7689#issuecomment-65980",
    "user": "@vbraun"
}
```

Resolution: invalid
