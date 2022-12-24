# Issue 9512: Sage Source Editor

archive/issues_009512.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  boothby acleone cwitty chapoton\n\nAdd an \"Edit this page\" link at the bottom of source files (/src/...) where one can edit the file.\n\nOnly `user_type(username) == 'admin'` can edit the files.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9512\n\n",
    "created_at": "2010-07-15T20:07:12Z",
    "labels": [
        "notebook",
        "trivial",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Sage Source Editor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9512",
    "user": "acleone"
}
```
Assignee: jason, was

CC:  boothby acleone cwitty chapoton

Add an "Edit this page" link at the bottom of source files (/src/...) where one can edit the file.

Only `user_type(username) == 'admin'` can edit the files.

Issue created by migration from https://trac.sagemath.org/ticket/9512





---

archive/issue_comments_091456.json:
```json
{
    "body": "Attachment [9512_source_editor.patch](tarball://root/attachments/some-uuid/ticket9512/9512_source_editor.patch) by boothby created at 2010-07-15 20:08:21",
    "created_at": "2010-07-15T20:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9512#issuecomment-91456",
    "user": "boothby"
}
```

Attachment [9512_source_editor.patch](tarball://root/attachments/some-uuid/ticket9512/9512_source_editor.patch) by boothby created at 2010-07-15 20:08:21



---

archive/issue_comments_091457.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-15T20:08:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9512#issuecomment-91457",
    "user": "boothby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091458.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-15T20:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9512#issuecomment-91458",
    "user": "acleone"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091459.json:
```json
{
    "body": "I'm added the commit string\n\n```\n#9512: Sage source editor.  Tom Boothby\n```\n\nfor the patch I'm merging into SageNB 0.8.2 (#9572).",
    "created_at": "2010-07-23T06:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9512#issuecomment-91459",
    "user": "mpatel"
}
```

I'm added the commit string

```
#9512: Sage source editor.  Tom Boothby
```

for the patch I'm merging into SageNB 0.8.2 (#9572).



---

archive/issue_comments_091460.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-23T07:18:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9512#issuecomment-91460",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_091461.json:
```json
{
    "body": "[comment:ticket:9572:6 C. Witty's comment] at #9572:\n> Actually, I found a bug: the \"source editor\" feature (#9512) converts line endings from Unix to DOS (so once you've edited the file, mercurial thinks every line has changed).\n\n> Given the total non-discoverability of #9512, I'm not sure this bug is worth holding up the new spkg; I'll let somebody else decide that.\n\nI also see this behavior.  I'm reopening this ticket, changing its status to \"needs work,\" and removing it, for now, from #9572's SageNB 0.8.2.",
    "created_at": "2010-07-25T07:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9512#issuecomment-91461",
    "user": "mpatel"
}
```

[comment:ticket:9572:6 C. Witty's comment] at #9572:
> Actually, I found a bug: the "source editor" feature (#9512) converts line endings from Unix to DOS (so once you've edited the file, mercurial thinks every line has changed).

> Given the total non-discoverability of #9512, I'm not sure this bug is worth holding up the new spkg; I'll let somebody else decide that.

I also see this behavior.  I'm reopening this ticket, changing its status to "needs work," and removing it, for now, from #9572's SageNB 0.8.2.



---

archive/issue_comments_091462.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2010-07-25T07:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9512#issuecomment-91462",
    "user": "mpatel"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_091463.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-07-25T07:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9512#issuecomment-91463",
    "user": "mpatel"
}
```

Changing status from closed to new.



---

archive/issue_comments_091464.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-07-25T07:28:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9512#issuecomment-91464",
    "user": "mpatel"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_091465.json:
```json
{
    "body": "Changing priority from trivial to minor.",
    "created_at": "2010-07-25T07:28:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9512#issuecomment-91465",
    "user": "mpatel"
}
```

Changing priority from trivial to minor.



---

archive/issue_comments_091466.json:
```json
{
    "body": "Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9512#issuecomment-91466",
    "user": "mkoeppe"
}
```

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.



---

archive/issue_comments_091467.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9512#issuecomment-91467",
    "user": "mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_091468.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-09-11T10:41:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9512#issuecomment-91468",
    "user": "chapoton"
}
```

Resolution: invalid
