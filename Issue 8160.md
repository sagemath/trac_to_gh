# Issue 8160: add 'text' option to sphinxify

archive/issues_008160.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @qed777\n\nThis patch adds a 'text' option to sphinxify: use `sphinxify(s, format='text')` or `sphinxify(s, format='html')`, where format is optional with default value 'html'.  The intended use is in sage.misc.sagedoc for producing docstrings from the command line.  I'll create another ticket for that.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8160\n\n",
    "created_at": "2010-02-03T02:20:23Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "add 'text' option to sphinxify",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8160",
    "user": "@jhpalmieri"
}
```
Assignee: @williamstein

CC:  @qed777

This patch adds a 'text' option to sphinxify: use `sphinxify(s, format='text')` or `sphinxify(s, format='html')`, where format is optional with default value 'html'.  The intended use is in sage.misc.sagedoc for producing docstrings from the command line.  I'll create another ticket for that.

Issue created by migration from https://trac.sagemath.org/ticket/8160





---

archive/issue_comments_071773.json:
```json
{
    "body": "Attachment [trac_8160-sphinxify.patch](tarball://root/attachments/some-uuid/ticket8160/trac_8160-sphinxify.patch) by @jhpalmieri created at 2010-02-03 02:30:58\n\napply to sagenb repo",
    "created_at": "2010-02-03T02:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8160#issuecomment-71773",
    "user": "@jhpalmieri"
}
```

Attachment [trac_8160-sphinxify.patch](tarball://root/attachments/some-uuid/ticket8160/trac_8160-sphinxify.patch) by @jhpalmieri created at 2010-02-03 02:30:58

apply to sagenb repo



---

archive/issue_comments_071774.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-03T02:33:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8160#issuecomment-71774",
    "user": "@jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071775.json:
```json
{
    "body": "Attachment [trac_8160-sphinxify_text.patch](tarball://root/attachments/some-uuid/ticket8160/trac_8160-sphinxify_text.patch) by @qed777 created at 2010-02-03 04:47:41\n\nRebased vs. #8102.  Apply only this patch.  sagenb repo.",
    "created_at": "2010-02-03T04:47:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8160#issuecomment-71775",
    "user": "@qed777"
}
```

Attachment [trac_8160-sphinxify_text.patch](tarball://root/attachments/some-uuid/ticket8160/trac_8160-sphinxify_text.patch) by @qed777 created at 2010-02-03 04:47:41

Rebased vs. #8102.  Apply only this patch.  sagenb repo.



---

archive/issue_comments_071776.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-03T04:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8160#issuecomment-71776",
    "user": "@qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071777.json:
```json
{
    "body": "I've attached a version rebased against #8102 --- it seemed a bit easier than the opposite.  Positive review for the first patch, at least.",
    "created_at": "2010-02-03T04:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8160#issuecomment-71777",
    "user": "@qed777"
}
```

I've attached a version rebased against #8102 --- it seemed a bit easier than the opposite.  Positive review for the first patch, at least.



---

archive/issue_comments_071778.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-05T00:37:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8160",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8160#issuecomment-71778",
    "user": "@qed777"
}
```

Resolution: fixed
