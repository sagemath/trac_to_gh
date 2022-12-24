# Issue 6598: Change the sage build system to use "set -e" so that if any error occurs in spkg-install then the build immediately terminates with an error

archive/issues_006598.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @dimpase @jhpalmieri\n\n\n```\n> Nonetheless, we should be checking the error code after every line\n> executes, one way or another.  Is there a way to automatically do this\n> in bash?\n\n\"set -e\" should do it.\n\nGoogle brings up this page, besides lots of others:\n\nhttp://www.davidpashley.com/articles/writing-robust-shell-scripts.html\n\n\nCheers,\nBurcin\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6598\n\n",
    "created_at": "2009-07-23T09:46:34Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Change the sage build system to use \"set -e\" so that if any error occurs in spkg-install then the build immediately terminates with an error",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6598",
    "user": "@williamstein"
}
```
Assignee: tbd

CC:  @dimpase @jhpalmieri


```
> Nonetheless, we should be checking the error code after every line
> executes, one way or another.  Is there a way to automatically do this
> in bash?

"set -e" should do it.

Google brings up this page, besides lots of others:

http://www.davidpashley.com/articles/writing-robust-shell-scripts.html


Cheers,
Burcin
```


Issue created by migration from https://trac.sagemath.org/ticket/6598





---

archive/issue_comments_054015.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-08-30T19:06:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6598#issuecomment-54015",
    "user": "@mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_054016.json:
```json
{
    "body": "outdated, can be closed",
    "created_at": "2020-08-30T19:06:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6598#issuecomment-54016",
    "user": "@mkoeppe"
}
```

outdated, can be closed



---

archive/issue_comments_054017.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-08-31T02:15:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6598#issuecomment-54017",
    "user": "@jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_054018.json:
```json
{
    "body": "Okay",
    "created_at": "2020-08-31T02:15:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6598#issuecomment-54018",
    "user": "@jhpalmieri"
}
```

Okay



---

archive/issue_comments_054019.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-10-04T07:53:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6598#issuecomment-54019",
    "user": "@fchapoton"
}
```

Resolution: invalid
