# Issue 9512: Sage Source Editor

archive/issues_009512.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  boothby acleone cwitty @fchapoton\n\nAdd an \"Edit this page\" link at the bottom of source files (/src/...) where one can edit the file.\n\nOnly `user_type(username) == 'admin'` can edit the files.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9512\n\n",
    "closed_at": "2020-09-11T10:41:57Z",
    "created_at": "2010-07-15T20:07:12Z",
    "labels": [
        "component: notebook",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Sage Source Editor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9512",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```
Assignee: jason, was

CC:  boothby acleone cwitty @fchapoton

Add an "Edit this page" link at the bottom of source files (/src/...) where one can edit the file.

Only `user_type(username) == 'admin'` can edit the files.

Issue created by migration from https://trac.sagemath.org/ticket/9512





---

archive/issue_comments_091303.json:
```json
{
    "body": "Attachment [9512_source_editor.patch](tarball://root/attachments/some-uuid/ticket9512/9512_source_editor.patch) by boothby created at 2010-07-15 20:08:21",
    "created_at": "2010-07-15T20:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9512#issuecomment-91303",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [9512_source_editor.patch](tarball://root/attachments/some-uuid/ticket9512/9512_source_editor.patch) by boothby created at 2010-07-15 20:08:21



---

archive/issue_comments_091304.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-15T20:08:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9512#issuecomment-91304",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091305.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-15T20:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9512#issuecomment-91305",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091306.json:
```json
{
    "body": "I'm added the commit string\n\n```\n#9512: Sage source editor.  Tom Boothby\n```\nfor the patch I'm merging into SageNB 0.8.2 (#9572).",
    "created_at": "2010-07-23T06:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9512#issuecomment-91306",
    "user": "https://github.com/qed777"
}
```

I'm added the commit string

```
#9512: Sage source editor.  Tom Boothby
```
for the patch I'm merging into SageNB 0.8.2 (#9572).



---

archive/issue_comments_091307.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-23T07:18:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9512#issuecomment-91307",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_023617.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-23T07:18:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9512#event-23617"
}
```



---

archive/issue_comments_091308.json:
```json
{
    "body": "[comment:ticket:9572:6 C. Witty's comment] at #9572:\n> Actually, I found a bug: the \"source editor\" feature (#9512) converts line endings from Unix to DOS (so once you've edited the file, mercurial thinks every line has changed).\n\n\n> Given the total non-discoverability of #9512, I'm not sure this bug is worth holding up the new spkg; I'll let somebody else decide that.\n\n\nI also see this behavior.  I'm reopening this ticket, changing its status to \"needs work,\" and removing it, for now, from #9572's SageNB 0.8.2.",
    "created_at": "2010-07-25T07:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9512#issuecomment-91308",
    "user": "https://github.com/qed777"
}
```

[comment:ticket:9572:6 C. Witty's comment] at #9572:
> Actually, I found a bug: the "source editor" feature (#9512) converts line endings from Unix to DOS (so once you've edited the file, mercurial thinks every line has changed).


> Given the total non-discoverability of #9512, I'm not sure this bug is worth holding up the new spkg; I'll let somebody else decide that.


I also see this behavior.  I'm reopening this ticket, changing its status to "needs work," and removing it, for now, from #9572's SageNB 0.8.2.



---

archive/issue_comments_091309.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-07-25T07:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9512#issuecomment-91309",
    "user": "https://github.com/qed777"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_091310.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-07-25T07:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9512#issuecomment-91310",
    "user": "https://github.com/qed777"
}
```

Changing status from closed to new.



---

archive/issue_events_023618.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-07-25T07:28:25Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9512#event-23618"
}
```



---

archive/issue_comments_091311.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-07-25T07:28:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9512#issuecomment-91311",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_091312.json:
```json
{
    "body": "Changing priority from trivial to minor.",
    "created_at": "2010-07-25T07:28:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9512#issuecomment-91312",
    "user": "https://github.com/qed777"
}
```

Changing priority from trivial to minor.



---

archive/issue_events_023619.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9512#event-23619"
}
```



---

archive/issue_events_023620.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9512#event-23620"
}
```



---

archive/issue_events_023621.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9512#event-23621"
}
```



---

archive/issue_events_023622.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9512#event-23622"
}
```



---

archive/issue_events_023623.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9512#event-23623"
}
```



---

archive/issue_events_023624.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9512#event-23624"
}
```



---

archive/issue_events_023625.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9512#event-23625"
}
```



---

archive/issue_comments_091313.json:
```json
{
    "body": "Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9512#issuecomment-91313",
    "user": "https://github.com/mkoeppe"
}
```

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.



---

archive/issue_comments_091314.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9512#issuecomment-91314",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_events_023626.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-08-18T00:36:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9512#event-23626"
}
```



---

archive/issue_events_023627.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-08-18T00:36:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9512#event-23627"
}
```



---

archive/issue_events_023628.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-09-11T10:41:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9512#event-23628"
}
```



---

archive/issue_comments_091315.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-09-11T10:41:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9512#issuecomment-91315",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid
