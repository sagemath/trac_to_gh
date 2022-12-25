# Issue 7970: Make `hg` interfaces use `subprocess.Popen` and return exit code

archive/issues_007970.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @mwhansen\n\nAs mentioned on #7760, it would be nice if the `hg_sage`, etc. returned the exit code from the `__call__` method. We'd have to switch `os.popen3` to `subprocess.Popen` to do this, which isn't so bad, and is worth it in the long run (since `os.popen3` is deprecated). \n\nIssue created by migration from https://trac.sagemath.org/ticket/7970\n\n",
    "created_at": "2010-01-17T23:48:44Z",
    "labels": [
        "component: build"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Make `hg` interfaces use `subprocess.Popen` and return exit code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7970",
    "user": "https://github.com/craigcitro"
}
```
Assignee: GeorgSWeber

CC:  @mwhansen

As mentioned on #7760, it would be nice if the `hg_sage`, etc. returned the exit code from the `__call__` method. We'd have to switch `os.popen3` to `subprocess.Popen` to do this, which isn't so bad, and is worth it in the long run (since `os.popen3` is deprecated). 

Issue created by migration from https://trac.sagemath.org/ticket/7970





---

archive/issue_comments_069408.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-12-19T12:08:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7970",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7970#issuecomment-69408",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069409.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-12-19T12:08:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7970",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7970#issuecomment-69409",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069410.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2013-12-19T22:37:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7970",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7970#issuecomment-69410",
    "user": "https://github.com/vbraun"
}
```

Resolution: wontfix



---

archive/issue_events_008185.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2013-12-19T22:37:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7970",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7970#event-8185"
}
```
