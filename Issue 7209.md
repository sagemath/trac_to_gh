# Issue 7209: Make `sage -coverage` aware of TestSuite

archive/issues_007209.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat\n\nWith the attached patch, sage -coverage looks for either a loads/dumps test or TestSuite, and suggests using the later.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7209\n\n",
    "created_at": "2009-10-14T13:50:22Z",
    "labels": [
        "component: doctest coverage"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "Make `sage -coverage` aware of TestSuite",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7209",
    "user": "https://github.com/nthiery"
}
```
Assignee: @nthiery

CC:  sage-combinat

With the attached patch, sage -coverage looks for either a loads/dumps test or TestSuite, and suggests using the later.

Issue created by migration from https://trac.sagemath.org/ticket/7209





---

archive/issue_comments_059716.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-14T13:55:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7209#issuecomment-59716",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059717.json:
```json
{
    "body": "Attachment [trac_7209-coverage-TestSuite-nt.patch](tarball://root/attachments/some-uuid/ticket7209/trac_7209-coverage-TestSuite-nt.patch) by @nthiery created at 2009-10-14 14:09:30",
    "created_at": "2009-10-14T14:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7209#issuecomment-59717",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_7209-coverage-TestSuite-nt.patch](tarball://root/attachments/some-uuid/ticket7209/trac_7209-coverage-TestSuite-nt.patch) by @nthiery created at 2009-10-14 14:09:30



---

archive/issue_comments_059718.json:
```json
{
    "body": "With the new category framework there will be a lot of parent which will be tested by the testsuite machinery. It is very useful that sage-coverage stop complaining about missing `s == loads(dumps(s))` because it is done during\n`TestSuite(s).run()`. The patch looks good and works. Positive review. \n\nCheers,\n\nFlorent",
    "created_at": "2009-10-19T19:50:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7209#issuecomment-59718",
    "user": "https://github.com/hivert"
}
```

With the new category framework there will be a lot of parent which will be tested by the testsuite machinery. It is very useful that sage-coverage stop complaining about missing `s == loads(dumps(s))` because it is done during
`TestSuite(s).run()`. The patch looks good and works. Positive review. 

Cheers,

Florent



---

archive/issue_comments_059719.json:
```json
{
    "body": "Changing keywords from \"\" to \"TestSuite, coverage\".",
    "created_at": "2009-10-19T19:50:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7209#issuecomment-59719",
    "user": "https://github.com/hivert"
}
```

Changing keywords from "" to "TestSuite, coverage".



---

archive/issue_comments_059720.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-19T19:50:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7209#issuecomment-59720",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059721.json:
```json
{
    "body": "Notice that #5819 is somewhat related to this. It would be nice to fix that issue eventually...",
    "created_at": "2009-10-19T20:20:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7209#issuecomment-59721",
    "user": "https://github.com/jhpalmieri"
}
```

Notice that #5819 is somewhat related to this. It would be nice to fix that issue eventually...



---

archive/issue_comments_059722.json:
```json
{
    "body": "Replying to [comment:5 jhpalmieri]:\n> Notice that #5819 is somewhat related to this. It would be nice to fix that issue eventually...\n\nSure. But right now our primary goal is to finish the category stuff ASAP...\nI'm sorry for this but we really have to take the straight line :-)\n\nCheers,\n\nFlorent",
    "created_at": "2009-10-19T20:57:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7209#issuecomment-59722",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:5 jhpalmieri]:
> Notice that #5819 is somewhat related to this. It would be nice to fix that issue eventually...

Sure. But right now our primary goal is to finish the category stuff ASAP...
I'm sorry for this but we really have to take the straight line :-)

Cheers,

Florent



---

archive/issue_events_017075.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-21T04:01:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7209",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7209#event-17075"
}
```



---

archive/issue_comments_059723.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-21T04:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7209#issuecomment-59723",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
