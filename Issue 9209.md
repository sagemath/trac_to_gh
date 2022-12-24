# Issue 9209: Sage build can go wrong if there is a python install in /usr/local.

archive/issues_009209.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @jasongrout\n\nThere are at least two failed reports of Sage failing to build properly if there is an installation of python in /usr/local\n\n* http://groups.google.com/group/sage-solaris/browse_thread/thread/5dcc7ed68d279f67?hl=en\n* http://groups.google.com/group/sage-devel/browse_thread/thread/37a67ce63e68d55b?hl=en-GB\n\nwhere an installation in /usr/local of python screw up Sage. \n\nIn my own case, the only way I could find to stop the install in /usr/local preventing Sage building, was to execute as root\n\n\n```\nchmod 000 /usr/local/lib/libpython2.6.a /usr/local/lib/python2.6\n```\n\n\nDave\n\nIssue created by migration from https://trac.sagemath.org/ticket/9209\n\n",
    "created_at": "2010-06-10T23:45:54Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Sage build can go wrong if there is a python install in /usr/local.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9209",
    "user": "drkirkby"
}
```
Assignee: GeorgSWeber

CC:  @jasongrout

There are at least two failed reports of Sage failing to build properly if there is an installation of python in /usr/local

* http://groups.google.com/group/sage-solaris/browse_thread/thread/5dcc7ed68d279f67?hl=en
* http://groups.google.com/group/sage-devel/browse_thread/thread/37a67ce63e68d55b?hl=en-GB

where an installation in /usr/local of python screw up Sage. 

In my own case, the only way I could find to stop the install in /usr/local preventing Sage building, was to execute as root


```
chmod 000 /usr/local/lib/libpython2.6.a /usr/local/lib/python2.6
```


Dave

Issue created by migration from https://trac.sagemath.org/ticket/9209





---

archive/issue_comments_086196.json:
```json
{
    "body": "Changing assignee from GeorgSWeber to drkirkby.",
    "created_at": "2010-06-11T00:48:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9209#issuecomment-86196",
    "user": "drkirkby"
}
```

Changing assignee from GeorgSWeber to drkirkby.



---

archive/issue_comments_086197.json:
```json
{
    "body": "Remove assignee drkirkby.",
    "created_at": "2010-06-11T00:49:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9209#issuecomment-86197",
    "user": "drkirkby"
}
```

Remove assignee drkirkby.



---

archive/issue_comments_086198.json:
```json
{
    "body": "Set assignee to GeorgSWeber.",
    "created_at": "2010-06-11T00:49:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9209#issuecomment-86198",
    "user": "drkirkby"
}
```

Set assignee to GeorgSWeber.



---

archive/issue_comments_086199.json:
```json
{
    "body": "Does this still happen?",
    "created_at": "2015-01-09T14:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9209#issuecomment-86199",
    "user": "@a-andre"
}
```

Does this still happen?



---

archive/issue_comments_086200.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2017-04-19T13:14:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9209#issuecomment-86200",
    "user": "@jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_086201.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-04-19T13:14:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9209#issuecomment-86201",
    "user": "@jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086202.json:
```json
{
    "body": "Closing tickets in the sage-duplicate/invalid/wontfix module with positive_review (i.e. someone has confirmed they should be closed).",
    "created_at": "2017-07-13T07:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9209#issuecomment-86202",
    "user": "@embray"
}
```

Closing tickets in the sage-duplicate/invalid/wontfix module with positive_review (i.e. someone has confirmed they should be closed).



---

archive/issue_comments_086203.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2017-07-13T07:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9209#issuecomment-86203",
    "user": "@embray"
}
```

Resolution: wontfix
