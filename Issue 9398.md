# Issue 9398: Sage meddles with soft rlimits

archive/issues_009398.json:
```json
{
    "body": "Assignee: jason\n\nSage currently removes any soft resource limits set. If those limits are set, it's probably with good reason, so it would be better if it kept limits in place\n\n```\nsh-3.2$ ulimit -S -v 1000000\nsh-3.2$ ulimit -v\n1000000\nsh-3.2$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: import os\nsage: os.system(\"ulimit -v\")\nunlimited\n0\n```\n\n| Sage Version 4.4.4, Release Date: 2010-06-23                       |\n| Type notebook() for the GUI, and license() for information.        |\n\nIssue created by migration from https://trac.sagemath.org/ticket/9398\n\n",
    "created_at": "2010-06-30T22:11:44Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "Sage meddles with soft rlimits",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9398",
    "user": "nbruin"
}
```
Assignee: jason

Sage currently removes any soft resource limits set. If those limits are set, it's probably with good reason, so it would be better if it kept limits in place

```
sh-3.2$ ulimit -S -v 1000000
sh-3.2$ ulimit -v
1000000
sh-3.2$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: import os
sage: os.system("ulimit -v")
unlimited
0
```

| Sage Version 4.4.4, Release Date: 2010-06-23                       |
| Type notebook() for the GUI, and license() for information.        |

Issue created by migration from https://trac.sagemath.org/ticket/9398





---

archive/issue_comments_089517.json:
```json
{
    "body": "change all.py to not touch rlimits",
    "created_at": "2010-06-30T22:13:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9398#issuecomment-89517",
    "user": "nbruin"
}
```

change all.py to not touch rlimits



---

archive/issue_comments_089518.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-30T22:14:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9398#issuecomment-89518",
    "user": "nbruin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089519.json:
```json
{
    "body": "Attachment [preserve_rlimits.patch](tarball://root/attachments/some-uuid/ticket9398/preserve_rlimits.patch) by nbruin created at 2010-06-30 22:14:07",
    "created_at": "2010-06-30T22:14:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9398#issuecomment-89519",
    "user": "nbruin"
}
```

Attachment [preserve_rlimits.patch](tarball://root/attachments/some-uuid/ticket9398/preserve_rlimits.patch) by nbruin created at 2010-06-30 22:14:07



---

archive/issue_comments_089520.json:
```json
{
    "body": "I can't remember why this was added to Sage in 2005, so... positive review.",
    "created_at": "2010-06-30T22:18:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9398#issuecomment-89520",
    "user": "was"
}
```

I can't remember why this was added to Sage in 2005, so... positive review.



---

archive/issue_comments_089521.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-30T22:18:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9398#issuecomment-89521",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089522.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-22T08:26:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9398#issuecomment-89522",
    "user": "ddrake"
}
```

Resolution: fixed
