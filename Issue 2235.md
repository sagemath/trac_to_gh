# Issue 2235: doctest issue -- combining # long and # 32-bit / # 64-bit

archive/issues_002235.json:
```json
{
    "body": "Assignee: failure\n\nCC:  ncalexander@gmail.com\n\nSo I ran into some weird issue earlier with a doctest, and the problem seems to be this: combining # long with # 32-bit / # 64-bit seems to completely ignore the # long directive. Nick can probably tell me more about why it fails, or if his new stuff should fix it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2235\n\n",
    "created_at": "2008-02-20T20:29:27Z",
    "labels": [
        "doctest",
        "minor",
        "bug"
    ],
    "title": "doctest issue -- combining # long and # 32-bit / # 64-bit",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2235",
    "user": "craigcitro"
}
```
Assignee: failure

CC:  ncalexander@gmail.com

So I ran into some weird issue earlier with a doctest, and the problem seems to be this: combining # long with # 32-bit / # 64-bit seems to completely ignore the # long directive. Nick can probably tell me more about why it fails, or if his new stuff should fix it.

Issue created by migration from https://trac.sagemath.org/ticket/2235





---

archive/issue_comments_014800.json:
```json
{
    "body": "Note: there's a long doctest in sage/rings/number_field/totallyreal_rel.py that is what caused me to notice this; I've made that a # no doctest for now, because it was causing timeouts on some machines. When this bug is fixed, that needs to be changed into a # long.",
    "created_at": "2008-02-21T18:11:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2235#issuecomment-14800",
    "user": "craigcitro"
}
```

Note: there's a long doctest in sage/rings/number_field/totallyreal_rel.py that is what caused me to notice this; I've made that a # no doctest for now, because it was causing timeouts on some machines. When this bug is fixed, that needs to be changed into a # long.



---

archive/issue_comments_014801.json:
```json
{
    "body": "Just need to add a doctest that this works now.",
    "created_at": "2013-03-07T09:45:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2235#issuecomment-14801",
    "user": "jdemeyer"
}
```

Just need to add a doctest that this works now.



---

archive/issue_comments_014802.json:
```json
{
    "body": "Attachment [2235_long_time.patch](tarball://root/attachments/some-uuid/ticket2235/2235_long_time.patch) by jdemeyer created at 2013-03-13 10:37:56",
    "created_at": "2013-03-13T10:37:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2235#issuecomment-14802",
    "user": "jdemeyer"
}
```

Attachment [2235_long_time.patch](tarball://root/attachments/some-uuid/ticket2235/2235_long_time.patch) by jdemeyer created at 2013-03-13 10:37:56



---

archive/issue_comments_014803.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-03-13T10:38:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2235#issuecomment-14803",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_014804.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-03-14T20:24:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2235#issuecomment-14804",
    "user": "roed"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_014805.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2013-03-14T20:24:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2235#issuecomment-14805",
    "user": "roed"
}
```

Looks good to me.



---

archive/issue_comments_014806.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-03-17T15:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2235#issuecomment-14806",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_014807.json:
```json
{
    "body": "Changing component from doctest to doctest framework.",
    "created_at": "2013-03-28T22:41:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2235",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2235#issuecomment-14807",
    "user": "roed"
}
```

Changing component from doctest to doctest framework.
