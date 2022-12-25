# Issue 7756: Extra, unwanted text inserted in cells by shift-enter

archive/issues_007756.json:
```json
{
    "body": "Assignee: @williamstein\n\nSee [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/95aa96ca848ef135) and [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/47f6756f00df1f72/6f3dd9ce745832e4?#6f3dd9ce745832e4).\n\nIssue created by migration from https://trac.sagemath.org/ticket/7756\n\n",
    "created_at": "2009-12-24T06:18:37Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Extra, unwanted text inserted in cells by shift-enter",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7756",
    "user": "https://github.com/qed777"
}
```
Assignee: @williamstein

See [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/95aa96ca848ef135) and [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/47f6756f00df1f72/6f3dd9ce745832e4?#6f3dd9ce745832e4).

Issue created by migration from https://trac.sagemath.org/ticket/7756





---

archive/issue_comments_066678.json:
```json
{
    "body": "Minimal version ripped from #7666. sagenb repo.",
    "created_at": "2009-12-24T06:22:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7756#issuecomment-66678",
    "user": "https://github.com/qed777"
}
```

Minimal version ripped from #7666. sagenb repo.



---

archive/issue_comments_066679.json:
```json
{
    "body": "Attachment [trac_7756-extra_text_shift_enter.patch](tarball://root/attachments/some-uuid/ticket7756/trac_7756-extra_text_shift_enter.patch) by @qed777 created at 2009-12-24 06:32:00\n\nThe problem seems to be that the auto-indent code \"fires\" too often, e.g., when the shift key comes up before the enter key.  The [attachment:trac_7756-extra_text_shift_enter.patch patch] should fix this in Cr, FF, S, and O.  If it does not, please let me know!\n\nNote: I've extracted the patch here from the patch at #7666.",
    "created_at": "2009-12-24T06:32:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7756#issuecomment-66679",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7756-extra_text_shift_enter.patch](tarball://root/attachments/some-uuid/ticket7756/trac_7756-extra_text_shift_enter.patch) by @qed777 created at 2009-12-24 06:32:00

The problem seems to be that the auto-indent code "fires" too often, e.g., when the shift key comes up before the enter key.  The [attachment:trac_7756-extra_text_shift_enter.patch patch] should fix this in Cr, FF, S, and O.  If it does not, please let me know!

Note: I've extracted the patch here from the patch at #7666.



---

archive/issue_comments_066680.json:
```json
{
    "body": "This does indeed seem to fix the problem for me.  Subtle.\n\nMerged into sagenb-0.4.8.",
    "created_at": "2009-12-24T06:56:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7756#issuecomment-66680",
    "user": "https://github.com/williamstein"
}
```

This does indeed seem to fix the problem for me.  Subtle.

Merged into sagenb-0.4.8.



---

archive/issue_events_007968.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-12-24T06:56:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7756",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7756#event-7968"
}
```



---

archive/issue_comments_066681.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-24T06:56:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7756",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7756#issuecomment-66681",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
