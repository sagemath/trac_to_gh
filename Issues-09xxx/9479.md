# Issue 9479: wrong license in readline SPKG.txt

archive/issues_009479.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @williamstein drkirkby\n\nKeywords: license\n\nIn sage 4.4.4, the file SPKG.txt says:\n\n```\n## License\n\n * GPL V2+\n```\nwhereas src/COPYING says:\n\n```\n                    GNU GENERAL PUBLIC LICENSE\n                       Version 3, 29 June 2007\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9479\n\n",
    "closed_at": "2013-08-30T08:44:10Z",
    "created_at": "2010-07-12T12:30:20Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "wrong license in readline SPKG.txt",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9479",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: tbd

CC:  @williamstein drkirkby

Keywords: license

In sage 4.4.4, the file SPKG.txt says:

```
## License

 * GPL V2+
```
whereas src/COPYING says:

```
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007
```

Issue created by migration from https://trac.sagemath.org/ticket/9479





---

archive/issue_comments_090850.json:
```json
{
    "body": "Attachment [readline-6.2.p4.spkg](tarball://root/attachments/some-uuid/ticket9479/readline-6.2.p4.spkg) by @zimmermann6 created at 2013-08-23 14:39:23\n\nthe attached spkg should fix that issue.\n\nPaul",
    "created_at": "2013-08-23T14:39:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9479#issuecomment-90850",
    "user": "https://github.com/zimmermann6"
}
```

Attachment [readline-6.2.p4.spkg](tarball://root/attachments/some-uuid/ticket9479/readline-6.2.p4.spkg) by @zimmermann6 created at 2013-08-23 14:39:23

the attached spkg should fix that issue.

Paul



---

archive/issue_comments_090851.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-08-23T14:39:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9479#issuecomment-90851",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from new to needs_review.



---

archive/issue_events_023499.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-26T19:08:57Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9479",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9479#event-23499"
}
```



---

archive/issue_comments_090852.json:
```json
{
    "body": "Fixed by #14405 instead.",
    "created_at": "2013-08-26T19:08:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9479#issuecomment-90852",
    "user": "https://github.com/jdemeyer"
}
```

Fixed by #14405 instead.



---

archive/issue_comments_090853.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-08-26T19:08:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9479#issuecomment-90853",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_023500.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-30T08:44:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9479",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9479#event-23500"
}
```



---

archive/issue_comments_090854.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-08-30T08:44:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9479#issuecomment-90854",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
