# Issue 5668: notebook optimization -- when saving state sometimes the sage public notebook server (after running for a long time) takes a *huge* amount of RAM

archive/issues_005668.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @kcrisman @jhpalmieri\n\nThe attached screenshot shows the public Sage notebook server (which has about 7000 user accounts) saving state after I pressed control-C.  It uses a huge amount of RAM, but does finish after several minutes.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5668\n\n",
    "created_at": "2009-04-02T20:06:46Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "notebook optimization -- when saving state sometimes the sage public notebook server (after running for a long time) takes a *huge* amount of RAM",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5668",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

CC:  @kcrisman @jhpalmieri

The attached screenshot shows the public Sage notebook server (which has about 7000 user accounts) saving state after I pressed control-C.  It uses a huge amount of RAM, but does finish after several minutes.



Issue created by migration from https://trac.sagemath.org/ticket/5668





---

archive/issue_comments_044254.json:
```json
{
    "body": "picture of top and fact that we're saving state.",
    "created_at": "2009-04-02T20:07:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5668#issuecomment-44254",
    "user": "https://github.com/williamstein"
}
```

picture of top and fact that we're saving state.



---

archive/issue_comments_044255.json:
```json
{
    "body": "Attachment [Picture 2.png](tarball://root/attachments/some-uuid/ticket5668/Picture 2.png) by @williamstein created at 2009-04-02 20:10:45\n\npicture of too many open files.",
    "created_at": "2009-04-02T20:10:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5668#issuecomment-44255",
    "user": "https://github.com/williamstein"
}
```

Attachment [Picture 2.png](tarball://root/attachments/some-uuid/ticket5668/Picture 2.png) by @williamstein created at 2009-04-02 20:10:45

picture of too many open files.



---

archive/issue_comments_044256.json:
```json
{
    "body": "ancient ticket about deprecated sagenb, can we close ?",
    "created_at": "2020-03-28T20:36:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5668#issuecomment-44256",
    "user": "https://github.com/fchapoton"
}
```

ancient ticket about deprecated sagenb, can we close ?



---

archive/issue_events_013330.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-03-28T20:36:23Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5668",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5668#event-13330"
}
```



---

archive/issue_comments_044257.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-03-28T20:36:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5668#issuecomment-44257",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_044258.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-03-28T20:41:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5668#issuecomment-44258",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_044259.json:
```json
{
    "body": "This was only really ever applicable to absolutely immense notebook instantiations anyway :)",
    "created_at": "2020-03-28T20:41:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5668#issuecomment-44259",
    "user": "https://github.com/kcrisman"
}
```

This was only really ever applicable to absolutely immense notebook instantiations anyway :)



---

archive/issue_events_013331.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-03-28T20:41:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5668",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5668#event-13331"
}
```



---

archive/issue_comments_044260.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-03-28T20:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5668#issuecomment-44260",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid



---

archive/issue_comments_044261.json:
```json
{
    "body": "thx",
    "created_at": "2020-03-28T20:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5668",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5668#issuecomment-44261",
    "user": "https://github.com/fchapoton"
}
```

thx
