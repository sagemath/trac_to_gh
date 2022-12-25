# Issue 9352: givaro spkg: trivial typo in spkg-check

archive/issues_009352.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  drkirkby\n\nThe file spkg-check in the givaro spkg prints the following if testing fails: \"Error while running the R testsuite ... exiting\".  The new spkg changes \"R\" to \"Givaro\".\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9352\n\n",
    "created_at": "2010-06-27T17:18:32Z",
    "labels": [
        "component: spkg-check",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.3",
    "title": "givaro spkg: trivial typo in spkg-check",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9352",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: tbd

CC:  drkirkby

The file spkg-check in the givaro spkg prints the following if testing fails: "Error while running the R testsuite ... exiting".  The new spkg changes "R" to "Givaro".


Issue created by migration from https://trac.sagemath.org/ticket/9352





---

archive/issue_comments_088640.json:
```json
{
    "body": "Attachment [givaro.patch](tarball://root/attachments/some-uuid/ticket9352/givaro.patch) by @jhpalmieri created at 2010-06-27 17:20:11",
    "created_at": "2010-06-27T17:20:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9352#issuecomment-88640",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [givaro.patch](tarball://root/attachments/some-uuid/ticket9352/givaro.patch) by @jhpalmieri created at 2010-06-27 17:20:11



---

archive/issue_comments_088641.json:
```json
{
    "body": "I've attaching the output from \"hg diff\".  The new spkg is here: [http://sage.math.washington.edu/home/palmieri/SPKG/givaro-3.2.13rc2.p2.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/givaro-3.2.13rc2.p2.spkg).",
    "created_at": "2010-06-27T17:22:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9352#issuecomment-88641",
    "user": "https://github.com/jhpalmieri"
}
```

I've attaching the output from "hg diff".  The new spkg is here: [http://sage.math.washington.edu/home/palmieri/SPKG/givaro-3.2.13rc2.p2.spkg](http://sage.math.washington.edu/home/palmieri/SPKG/givaro-3.2.13rc2.p2.spkg).



---

archive/issue_comments_088642.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-27T17:22:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9352#issuecomment-88642",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_088643.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-27T17:43:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9352#issuecomment-88643",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_088644.json:
```json
{
    "body": "Positive review of course. \n\nDave",
    "created_at": "2010-06-27T17:43:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9352#issuecomment-88644",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Positive review of course. 

Dave



---

archive/issue_comments_088645.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-09T09:35:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9352#issuecomment-88645",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_023079.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-09T09:35:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9352",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9352#event-23079"
}
```



---

archive/issue_events_023080.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-09T09:35:55Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9352",
    "milestone": "sage-4.5.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9352#event-23080"
}
```



---

archive/issue_comments_088646.json:
```json
{
    "body": "Could it be that the version number really should have been\n\n```\ngivaro-3.2.13rc1.p2.spkg\n```\n\ninstead of\n\n```\ngivaro-3.2.13rc2.p2.spkg\n}}}?",
    "created_at": "2011-12-12T09:16:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9352#issuecomment-88646",
    "user": "https://github.com/jdemeyer"
}
```

Could it be that the version number really should have been

```
givaro-3.2.13rc1.p2.spkg
```

instead of

```
givaro-3.2.13rc2.p2.spkg
}}}?
