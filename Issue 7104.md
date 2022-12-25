# Issue 7104: [with patch, needs review] Add config.py back to the reference manual.

archive/issues_007104.json:
```json
{
    "body": "Assignee: tba\n\nTicket #6556 adds a much-needed, module-level docstring to `sage/server/notebook/config.py`.  It should be in the Sage reference manual.\n\nSee [sage-devel](http://groups.google.com/group/sage-devel/msg/b07018c5c407edc4).\n\nIssue created by migration from https://trac.sagemath.org/ticket/7104\n\n",
    "created_at": "2009-10-04T02:13:53Z",
    "labels": [
        "component: documentation",
        "trivial"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "[with patch, needs review] Add config.py back to the reference manual.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7104",
    "user": "https://github.com/qed777"
}
```
Assignee: tba

Ticket #6556 adds a much-needed, module-level docstring to `sage/server/notebook/config.py`.  It should be in the Sage reference manual.

See [sage-devel](http://groups.google.com/group/sage-devel/msg/b07018c5c407edc4).

Issue created by migration from https://trac.sagemath.org/ticket/7104





---

archive/issue_comments_058688.json:
```json
{
    "body": "Add the notebook key-bindings module to the reference manual.  Apply to sage repository.",
    "created_at": "2009-10-04T02:19:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7104#issuecomment-58688",
    "user": "https://github.com/qed777"
}
```

Add the notebook key-bindings module to the reference manual.  Apply to sage repository.



---

archive/issue_comments_058689.json:
```json
{
    "body": "Attachment [trac_7104-add_keys_to_ref_manual.patch](tarball://root/attachments/some-uuid/ticket7104/trac_7104-add_keys_to_ref_manual.patch) by @qed777 created at 2009-10-04 02:21:00",
    "created_at": "2009-10-04T02:21:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7104#issuecomment-58689",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7104-add_keys_to_ref_manual.patch](tarball://root/attachments/some-uuid/ticket7104/trac_7104-add_keys_to_ref_manual.patch) by @qed777 created at 2009-10-04 02:21:00



---

archive/issue_comments_058690.json:
```json
{
    "body": "Oops.  I think we need to account for all modules affected by the notebook separation (cf. #6983).",
    "created_at": "2009-10-04T07:01:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7104#issuecomment-58690",
    "user": "https://github.com/qed777"
}
```

Oops.  I think we need to account for all modules affected by the notebook separation (cf. #6983).



---

archive/issue_comments_058691.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-07T19:17:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7104#issuecomment-58691",
    "user": "https://github.com/maxthemouse"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058692.json:
```json
{
    "body": "Works with sage -docbuild reference html. ~! Adam",
    "created_at": "2009-10-07T19:17:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7104#issuecomment-58692",
    "user": "https://github.com/maxthemouse"
}
```

Works with sage -docbuild reference html. ~! Adam



---

archive/issue_comments_058693.json:
```json
{
    "body": "I'm confused.  This is just adding to the reference manual pages about the old notebook code, which isn't even used anymore.  I don't understand what the point is.",
    "created_at": "2009-10-19T06:25:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7104#issuecomment-58693",
    "user": "https://github.com/williamstein"
}
```

I'm confused.  This is just adding to the reference manual pages about the old notebook code, which isn't even used anymore.  I don't understand what the point is.



---

archive/issue_comments_058694.json:
```json
{
    "body": "(Of course, it can't really hurt for now, I guess, except to mislead people...)",
    "created_at": "2009-10-19T06:26:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7104#issuecomment-58694",
    "user": "https://github.com/williamstein"
}
```

(Of course, it can't really hurt for now, I guess, except to mislead people...)



---

archive/issue_comments_058695.json:
```json
{
    "body": "Changing component from documentation to notebook.",
    "created_at": "2009-10-19T06:28:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7104#issuecomment-58695",
    "user": "https://github.com/williamstein"
}
```

Changing component from documentation to notebook.



---

archive/issue_comments_058696.json:
```json
{
    "body": "I didn't realize this is old.  It'll need to be rebased against http://nb.sagemath.org/.",
    "created_at": "2009-10-19T06:28:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7104#issuecomment-58696",
    "user": "https://github.com/williamstein"
}
```

I didn't realize this is old.  It'll need to be rebased against http://nb.sagemath.org/.



---

archive/issue_comments_058697.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-11-11T19:46:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7104#issuecomment-58697",
    "user": "https://github.com/williamstein"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_058698.json:
```json
{
    "body": "changing to needs work, since it needs to be rebased/redone.",
    "created_at": "2009-11-11T19:46:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7104#issuecomment-58698",
    "user": "https://github.com/williamstein"
}
```

changing to needs work, since it needs to be rebased/redone.



---

archive/issue_comments_058699.json:
```json
{
    "body": "Replying to [comment:7 was]:\n> changing to needs work, since it needs to be rebased/redone. \nPlease see #7367.",
    "created_at": "2009-11-12T01:28:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7104#issuecomment-58699",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:7 was]:
> changing to needs work, since it needs to be rebased/redone. 
Please see #7367.



---

archive/issue_comments_058700.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-12T04:55:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7104#issuecomment-58700",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_058701.json:
```json
{
    "body": "This is fixed by #7367, so I'm closing this.",
    "created_at": "2009-11-12T04:55:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7104#issuecomment-58701",
    "user": "https://github.com/williamstein"
}
```

This is fixed by #7367, so I'm closing this.
