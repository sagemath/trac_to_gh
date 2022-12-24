# Issue 3369: bool(x<0) should raise an error rather than return False

archive/issues_003369.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nCC:  cwitty @jasongrout\n\nSee, e.g. discussion at http://groups.google.com/group/sage-devel/browse_thread/thread/bcdc671d2791056e/e086a9d59ff4b9ba\n\nIssue created by migration from https://trac.sagemath.org/ticket/3369\n\n",
    "created_at": "2008-06-05T00:08:53Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "bool(x<0) should raise an error rather than return False",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3369",
    "user": "@robertwb"
}
```
Assignee: @garyfurnish

CC:  cwitty @jasongrout

See, e.g. discussion at http://groups.google.com/group/sage-devel/browse_thread/thread/bcdc671d2791056e/e086a9d59ff4b9ba

Issue created by migration from https://trac.sagemath.org/ticket/3369





---

archive/issue_comments_023573.json:
```json
{
    "body": "This is absolutely not a bug and will break all kinds of things horribley, kill performance, require lots of try statements around trivial code, etc.  Recommend closing as \"not a bug.\"",
    "created_at": "2008-06-05T00:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3369#issuecomment-23573",
    "user": "@garyfurnish"
}
```

This is absolutely not a bug and will break all kinds of things horribley, kill performance, require lots of try statements around trivial code, etc.  Recommend closing as "not a bug."



---

archive/issue_comments_023574.json:
```json
{
    "body": "This was also discussed on IRC with wstein (IIRC) some time ago I believe and the concensus was that raising errors was bad.",
    "created_at": "2008-06-05T00:12:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3369#issuecomment-23574",
    "user": "@garyfurnish"
}
```

This was also discussed on IRC with wstein (IIRC) some time ago I believe and the concensus was that raising errors was bad.



---

archive/issue_comments_023575.json:
```json
{
    "body": "Hmmm... so concensus on IRC != concensus on sage-devel. Can you give an example of something that would be really bad?",
    "created_at": "2008-06-05T00:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3369#issuecomment-23575",
    "user": "@robertwb"
}
```

Hmmm... so concensus on IRC != concensus on sage-devel. Can you give an example of something that would be really bad?



---

archive/issue_comments_023576.json:
```json
{
    "body": "When I said \"nobody ever opened a trac ticket\", I was wrong; see #2781 (which has a prototype patch to implement this).",
    "created_at": "2008-06-05T00:23:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3369#issuecomment-23576",
    "user": "cwitty"
}
```

When I said "nobody ever opened a trac ticket", I was wrong; see #2781 (which has a prototype patch to implement this).



---

archive/issue_comments_023577.json:
```json
{
    "body": "Ah, OK. Then I guess we should close this.",
    "created_at": "2008-06-05T00:34:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3369#issuecomment-23577",
    "user": "@robertwb"
}
```

Ah, OK. Then I guess we should close this.



---

archive/issue_comments_023578.json:
```json
{
    "body": "Closed as invalid upon request by Robert.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-09T06:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3369#issuecomment-23578",
    "user": "mabshoff"
}
```

Closed as invalid upon request by Robert.

Cheers,

Michael



---

archive/issue_comments_023579.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-06-09T06:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3369#issuecomment-23579",
    "user": "mabshoff"
}
```

Resolution: invalid
