# Issue 4178: dist_functions.py doctest timeout is too small

archive/issues_004178.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nOn my PPC Power Book 550 MHz, 768 MB RAM, Mac OS X 10.4.11, Xcode 2.5, the \"long\" doctest fails because the timeout is too small.\n\nAs soon as I have checked how big it should be (on that box) to make it run through, I'll add the info here. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4178\n\n",
    "created_at": "2008-09-23T21:58:17Z",
    "labels": [
        "doctest coverage",
        "minor",
        "bug"
    ],
    "title": "dist_functions.py doctest timeout is too small",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4178",
    "user": "GeorgSWeber"
}
```
Assignee: GeorgSWeber

On my PPC Power Book 550 MHz, 768 MB RAM, Mac OS X 10.4.11, Xcode 2.5, the "long" doctest fails because the timeout is too small.

As soon as I have checked how big it should be (on that box) to make it run through, I'll add the info here. 

Issue created by migration from https://trac.sagemath.org/ticket/4178





---

archive/issue_comments_030318.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-23T21:58:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4178#issuecomment-30318",
    "user": "GeorgSWeber"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030319.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-09-23T22:04:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4178#issuecomment-30319",
    "user": "mabshoff"
}
```

Resolution: wontfix



---

archive/issue_comments_030320.json:
```json
{
    "body": "Nope, this is a won't fix. The long timeout is *huge*, i.e. 30 minutes. The problem is another one, i.e. ecm not returning and hence the doctest never finishes. This issue is already covered by another DSage ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-23T22:04:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4178",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4178#issuecomment-30320",
    "user": "mabshoff"
}
```

Nope, this is a won't fix. The long timeout is *huge*, i.e. 30 minutes. The problem is another one, i.e. ecm not returning and hence the doctest never finishes. This issue is already covered by another DSage ticket.

Cheers,

Michael
