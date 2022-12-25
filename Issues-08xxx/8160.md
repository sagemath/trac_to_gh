# Issue 8160: add 'text' option to sphinxify

archive/issues_008160.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @qed777\n\nThis patch adds a 'text' option to sphinxify: use `sphinxify(s, format='text')` or `sphinxify(s, format='html')`, where format is optional with default value 'html'.  The intended use is in sage.misc.sagedoc for producing docstrings from the command line.  I'll create another ticket (#8161) for that.\n\nDepends on #8102.\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8160\n\n",
    "closed_at": "2010-02-05T00:37:35Z",
    "created_at": "2010-02-03T02:20:23Z",
    "labels": [
        "component: notebook",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "add 'text' option to sphinxify",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8160",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @williamstein

CC:  @qed777

This patch adds a 'text' option to sphinxify: use `sphinxify(s, format='text')` or `sphinxify(s, format='html')`, where format is optional with default value 'html'.  The intended use is in sage.misc.sagedoc for producing docstrings from the command line.  I'll create another ticket (#8161) for that.

Depends on #8102.




Issue created by migration from https://trac.sagemath.org/ticket/8160





---

archive/issue_comments_071652.json:
```json
{
    "body": "Attachment [trac_8160-sphinxify.patch](tarball://root/attachments/some-uuid/ticket8160/trac_8160-sphinxify.patch) by @jhpalmieri created at 2010-02-03 02:30:58\n\napply to sagenb repo",
    "created_at": "2010-02-03T02:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8160#issuecomment-71652",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8160-sphinxify.patch](tarball://root/attachments/some-uuid/ticket8160/trac_8160-sphinxify.patch) by @jhpalmieri created at 2010-02-03 02:30:58

apply to sagenb repo



---

archive/issue_comments_071653.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-03T02:33:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8160#issuecomment-71653",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071654.json:
```json
{
    "body": "Attachment [trac_8160-sphinxify_text.patch](tarball://root/attachments/some-uuid/ticket8160/trac_8160-sphinxify_text.patch) by @qed777 created at 2010-02-03 04:47:41\n\nRebased vs. #8102.  Apply only this patch.  sagenb repo.",
    "created_at": "2010-02-03T04:47:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8160#issuecomment-71654",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8160-sphinxify_text.patch](tarball://root/attachments/some-uuid/ticket8160/trac_8160-sphinxify_text.patch) by @qed777 created at 2010-02-03 04:47:41

Rebased vs. #8102.  Apply only this patch.  sagenb repo.



---

archive/issue_comments_071655.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-03T04:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8160#issuecomment-71655",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071656.json:
```json
{
    "body": "I've attached a version rebased against #8102 --- it seemed a bit easier than the opposite.  Positive review for the first patch, at least.",
    "created_at": "2010-02-03T04:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8160#issuecomment-71656",
    "user": "https://github.com/qed777"
}
```

I've attached a version rebased against #8102 --- it seemed a bit easier than the opposite.  Positive review for the first patch, at least.



---

archive/issue_comments_071657.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-05T00:37:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8160#issuecomment-71657",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_019547.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-02-05T00:37:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8160",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8160#event-19547"
}
```
