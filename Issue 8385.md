# Issue 8385: Add hostname, date and time to test.log

archive/issues_008385.json:
```json
{
    "body": "Assignee: tbd\n\nCurrently, if one runs \n\n\n```\n$ make test\n```\n\n\na file\n\n\n```\n$HOME/.sage/tmp/test.log\n```\n\n\nis created with the results of the tests. However, this stops testing two versions of Sage at the same time - even if the tests take place on different machines. \n\nHence it would be useful if the log file had the hostname, date and time in it. \n\nI would suggest a name like\n\n\n```\ntest.log-redstart-23:22:57-02:26:2010\n```\n\n\nwould be useful to indicate\n\n* The hostname was \"redstart\"\n* The time the tests started was \"23:22:57\"\n* The date the tests started was \"02:26:2010\"\n\nThis would allow multiple versions of Sage to be tested on multiple computers at the same time. \n\nAdding the Sage version would be nice too, as below for Sage 4.3.3\n\n\n```\ntest.log-4.3.3-redstart-23:22:57-02:26:2010\n```\n\n\n\nDave \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8385\n\n",
    "created_at": "2010-02-26T23:35:43Z",
    "labels": [
        "component: doctest"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Add hostname, date and time to test.log",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8385",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

Currently, if one runs 


```
$ make test
```


a file


```
$HOME/.sage/tmp/test.log
```


is created with the results of the tests. However, this stops testing two versions of Sage at the same time - even if the tests take place on different machines. 

Hence it would be useful if the log file had the hostname, date and time in it. 

I would suggest a name like


```
test.log-redstart-23:22:57-02:26:2010
```


would be useful to indicate

* The hostname was "redstart"
* The time the tests started was "23:22:57"
* The date the tests started was "02:26:2010"

This would allow multiple versions of Sage to be tested on multiple computers at the same time. 

Adding the Sage version would be nice too, as below for Sage 4.3.3


```
test.log-4.3.3-redstart-23:22:57-02:26:2010
```



Dave 


Issue created by migration from https://trac.sagemath.org/ticket/8385





---

archive/issue_comments_074879.json:
```json
{
    "body": "Changing component from doctest to doctest framework.",
    "created_at": "2013-03-28T23:00:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8385#issuecomment-74879",
    "user": "https://github.com/roed314"
}
```

Changing component from doctest to doctest framework.



---

archive/issue_comments_074880.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-05-17T14:02:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8385#issuecomment-74880",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_074881.json:
```json
{
    "body": "Given that the original problem (writing to `$HOME`) doesn't occur anymore, given that running `make (p)test(long)` twice in the same installation is unlikely and given that it's nice to have easy, predictable filenames for the logfiles, I propose to close this as invalid.",
    "created_at": "2013-05-17T14:02:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8385#issuecomment-74881",
    "user": "https://github.com/jdemeyer"
}
```

Given that the original problem (writing to `$HOME`) doesn't occur anymore, given that running `make (p)test(long)` twice in the same installation is unlikely and given that it's nice to have easy, predictable filenames for the logfiles, I propose to close this as invalid.



---

archive/issue_comments_074882.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-05-19T13:14:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8385#issuecomment-74882",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008570.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2013-05-21T07:24:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8385",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8385#event-8570"
}
```



---

archive/issue_comments_074883.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-05-21T07:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8385",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8385#issuecomment-74883",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: invalid
