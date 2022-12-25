# Issue 7801: save_notebook is called twice on notebook shutdown

archive/issues_007801.json:
```json
{
    "body": "Assignee: @williamstein\n\nSee `run_notebook.py`'s `run_twisted`, which generates `DOT_SAGE/sagen_notebook.sagenb/twistedconf.tac`.\n\nMentioned [comment:ticket:7514:16 here].\n\nIssue created by migration from https://trac.sagemath.org/ticket/7801\n\n",
    "created_at": "2010-01-01T05:03:22Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "save_notebook is called twice on notebook shutdown",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7801",
    "user": "https://github.com/qed777"
}
```
Assignee: @williamstein

See `run_notebook.py`'s `run_twisted`, which generates `DOT_SAGE/sagen_notebook.sagenb/twistedconf.tac`.

Mentioned [comment:ticket:7514:16 here].

Issue created by migration from https://trac.sagemath.org/ticket/7801





---

archive/issue_comments_067379.json:
```json
{
    "body": "Attachment [trac_7801-save_notebook_twice.patch](tarball://root/attachments/some-uuid/ticket7801/trac_7801-save_notebook_twice.patch) by acleone created at 2010-01-19 01:36:26\n\nFixed interrupt handler to stop the twisted server instead of in save_notebook",
    "created_at": "2010-01-19T01:36:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7801#issuecomment-67379",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

Attachment [trac_7801-save_notebook_twice.patch](tarball://root/attachments/some-uuid/ticket7801/trac_7801-save_notebook_twice.patch) by acleone created at 2010-01-19 01:36:26

Fixed interrupt handler to stop the twisted server instead of in save_notebook



---

archive/issue_comments_067380.json:
```json
{
    "body": "What the problem was:\nThe signal handler would call save_notebook(), which would stop the twisted server.  There was a handler on the server shutdown, \"reactor.addSystemEventTrigger('before', 'shutdown', save_notebook)\", that would call save_notebook() again.\n\nChanges:\nMoved the code that stops the server into the signal handler, and removed the save_notebook call.",
    "created_at": "2010-01-19T01:42:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7801#issuecomment-67380",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

What the problem was:
The signal handler would call save_notebook(), which would stop the twisted server.  There was a handler on the server shutdown, "reactor.addSystemEventTrigger('before', 'shutdown', save_notebook)", that would call save_notebook() again.

Changes:
Moved the code that stops the server into the signal handler, and removed the save_notebook call.



---

archive/issue_comments_067381.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T01:42:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7801#issuecomment-67381",
    "user": "https://trac.sagemath.org/admin/accounts/users/acleone"
}
```

Changing status from new to needs_review.



---

archive/issue_events_018680.json:
```json
{
    "actor": "https://github.com/TimDumol",
    "created_at": "2010-01-19T01:51:06Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7801",
    "milestone": "sage-4.3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7801#event-18680"
}
```



---

archive/issue_comments_067382.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T01:51:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7801#issuecomment-67382",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067383.json:
```json
{
    "body": "LGTM. Nice job.",
    "created_at": "2010-01-19T01:51:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7801#issuecomment-67383",
    "user": "https://github.com/TimDumol"
}
```

LGTM. Nice job.



---

archive/issue_events_018681.json:
```json
{
    "actor": "https://github.com/TimDumol",
    "created_at": "2010-01-19T03:33:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7801",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7801#event-18681"
}
```



---

archive/issue_comments_067384.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T03:33:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7801",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7801#issuecomment-67384",
    "user": "https://github.com/TimDumol"
}
```

Resolution: fixed



---

archive/issue_events_018682.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-01-19T05:21:40Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7801",
    "milestone": "sage-4.3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7801#event-18682"
}
```



---

archive/issue_events_018683.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-01-19T05:21:40Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7801",
    "milestone": "sage-4.3.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7801#event-18683"
}
```
