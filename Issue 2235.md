# Issue 2235: doctest issue -- combining # long and # 32-bit / # 64-bit

archive/issues_002235.json:
```json
{
    "body": "Assignee: failure\n\nCC:  ncalexander@gmail.com\n\nSo I ran into some weird issue earlier with a doctest, and the problem seems to be this: combining # long with # 32-bit / # 64-bit seems to completely ignore the # long directive. Nick can probably tell me more about why it fails, or if his new stuff should fix it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2235\n\n",
    "created_at": "2008-02-20T20:29:27Z",
    "labels": [
        "component: doctest",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.9",
    "title": "doctest issue -- combining # long and # 32-bit / # 64-bit",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2235",
    "user": "https://github.com/craigcitro"
}
```
Assignee: failure

CC:  ncalexander@gmail.com

So I ran into some weird issue earlier with a doctest, and the problem seems to be this: combining # long with # 32-bit / # 64-bit seems to completely ignore the # long directive. Nick can probably tell me more about why it fails, or if his new stuff should fix it.

Issue created by migration from https://trac.sagemath.org/ticket/2235





---

archive/issue_comments_014769.json:
```json
{
    "body": "Note: there's a long doctest in sage/rings/number_field/totallyreal_rel.py that is what caused me to notice this; I've made that a # no doctest for now, because it was causing timeouts on some machines. When this bug is fixed, that needs to be changed into a # long.",
    "created_at": "2008-02-21T18:11:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2235#issuecomment-14769",
    "user": "https://github.com/craigcitro"
}
```

Note: there's a long doctest in sage/rings/number_field/totallyreal_rel.py that is what caused me to notice this; I've made that a # no doctest for now, because it was causing timeouts on some machines. When this bug is fixed, that needs to be changed into a # long.



---

archive/issue_comments_014770.json:
```json
{
    "body": "Just need to add a doctest that this works now.",
    "created_at": "2013-03-07T09:45:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2235#issuecomment-14770",
    "user": "https://github.com/jdemeyer"
}
```

Just need to add a doctest that this works now.



---

archive/issue_comments_014771.json:
```json
{
    "body": "Attachment [2235_long_time.patch](tarball://root/attachments/some-uuid/ticket2235/2235_long_time.patch) by @jdemeyer created at 2013-03-13 10:37:56",
    "created_at": "2013-03-13T10:37:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2235#issuecomment-14771",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [2235_long_time.patch](tarball://root/attachments/some-uuid/ticket2235/2235_long_time.patch) by @jdemeyer created at 2013-03-13 10:37:56



---

archive/issue_comments_014772.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-03-13T10:38:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2235#issuecomment-14772",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_014773.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-03-14T20:24:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2235#issuecomment-14773",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_014774.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2013-03-14T20:24:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2235#issuecomment-14774",
    "user": "https://github.com/roed314"
}
```

Looks good to me.



---

archive/issue_events_002405.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-03-17T15:31:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2235",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2235#event-2405"
}
```



---

archive/issue_comments_014775.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-03-17T15:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2235#issuecomment-14775",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_014776.json:
```json
{
    "body": "Changing component from doctest to doctest framework.",
    "created_at": "2013-03-28T22:41:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2235#issuecomment-14776",
    "user": "https://github.com/roed314"
}
```

Changing component from doctest to doctest framework.
