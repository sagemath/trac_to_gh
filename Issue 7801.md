# Issue 7801: save_notebook is called twice on notebook shutdown

archive/issues_007801.json:
```json
{
    "body": "Assignee: was\n\nSee `run_notebook.py`'s `run_twisted`, which generates `DOT_SAGE/sagen_notebook.sagenb/twistedconf.tac`.\n\nMentioned [comment:ticket:7514:16 here].\n\nIssue created by migration from https://trac.sagemath.org/ticket/7801\n\n",
    "created_at": "2010-01-01T05:03:22Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "save_notebook is called twice on notebook shutdown",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7801",
    "user": "mpatel"
}
```
Assignee: was

See `run_notebook.py`'s `run_twisted`, which generates `DOT_SAGE/sagen_notebook.sagenb/twistedconf.tac`.

Mentioned [comment:ticket:7514:16 here].

Issue created by migration from https://trac.sagemath.org/ticket/7801





---

archive/issue_comments_067496.json:
```json
{
    "body": "Attachment [trac_7801-save_notebook_twice.patch](tarball://root/attachments/some-uuid/ticket7801/trac_7801-save_notebook_twice.patch) by acleone created at 2010-01-19 01:36:26\n\nFixed interrupt handler to stop the twisted server instead of in save_notebook",
    "created_at": "2010-01-19T01:36:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7801#issuecomment-67496",
    "user": "acleone"
}
```

Attachment [trac_7801-save_notebook_twice.patch](tarball://root/attachments/some-uuid/ticket7801/trac_7801-save_notebook_twice.patch) by acleone created at 2010-01-19 01:36:26

Fixed interrupt handler to stop the twisted server instead of in save_notebook



---

archive/issue_comments_067497.json:
```json
{
    "body": "What the problem was:\nThe signal handler would call save_notebook(), which would stop the twisted server.  There was a handler on the server shutdown, \"reactor.addSystemEventTrigger('before', 'shutdown', save_notebook)\", that would call save_notebook() again.\n\nChanges:\nMoved the code that stops the server into the signal handler, and removed the save_notebook call.",
    "created_at": "2010-01-19T01:42:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7801#issuecomment-67497",
    "user": "acleone"
}
```

What the problem was:
The signal handler would call save_notebook(), which would stop the twisted server.  There was a handler on the server shutdown, "reactor.addSystemEventTrigger('before', 'shutdown', save_notebook)", that would call save_notebook() again.

Changes:
Moved the code that stops the server into the signal handler, and removed the save_notebook call.



---

archive/issue_comments_067498.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T01:42:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7801#issuecomment-67498",
    "user": "acleone"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067499.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T01:51:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7801#issuecomment-67499",
    "user": "timdumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067500.json:
```json
{
    "body": "LGTM. Nice job.",
    "created_at": "2010-01-19T01:51:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7801#issuecomment-67500",
    "user": "timdumol"
}
```

LGTM. Nice job.



---

archive/issue_comments_067501.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T03:33:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7801#issuecomment-67501",
    "user": "timdumol"
}
```

Resolution: fixed
