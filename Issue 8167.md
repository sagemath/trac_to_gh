# Issue 8167: Use LaTeX-friendly Unicode characters in SageNB docstrings

archive/issues_008167.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  mvngu @robert-marik @jhpalmieri\n\nIn order to build the PDF reference manual --- with the current settings in `doc/common/conf.py` --- we need replace several Unicode characters introduced at #7249.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8167\n\n",
    "created_at": "2010-02-03T09:23:05Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "Use LaTeX-friendly Unicode characters in SageNB docstrings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8167",
    "user": "@qed777"
}
```
Assignee: @williamstein

CC:  mvngu @robert-marik @jhpalmieri

In order to build the PDF reference manual --- with the current settings in `doc/common/conf.py` --- we need replace several Unicode characters introduced at #7249.

Issue created by migration from https://trac.sagemath.org/ticket/8167





---

archive/issue_comments_071859.json:
```json
{
    "body": "Replace some Unicode characters.  sagenb repo.",
    "created_at": "2010-02-03T09:27:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8167#issuecomment-71859",
    "user": "@qed777"
}
```

Replace some Unicode characters.  sagenb repo.



---

archive/issue_comments_071860.json:
```json
{
    "body": "Attachment [trac_8167-simpler_unicode.patch](tarball://root/attachments/some-uuid/ticket8167/trac_8167-simpler_unicode.patch) by @qed777 created at 2010-02-03 09:29:34",
    "created_at": "2010-02-03T09:29:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8167#issuecomment-71860",
    "user": "@qed777"
}
```

Attachment [trac_8167-simpler_unicode.patch](tarball://root/attachments/some-uuid/ticket8167/trac_8167-simpler_unicode.patch) by @qed777 created at 2010-02-03 09:29:34



---

archive/issue_comments_071861.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-02-03T09:30:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8167#issuecomment-71861",
    "user": "@qed777"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_071862.json:
```json
{
    "body": "Small-scale tests with the patch show promise.  I'm attempting to build the full PDF manual now.",
    "created_at": "2010-02-03T09:30:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8167#issuecomment-71862",
    "user": "@qed777"
}
```

Small-scale tests with the patch show promise.  I'm attempting to build the full PDF manual now.



---

archive/issue_comments_071863.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-03T09:30:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8167#issuecomment-71863",
    "user": "@qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071864.json:
```json
{
    "body": "It builds!",
    "created_at": "2010-02-03T09:41:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8167#issuecomment-71864",
    "user": "@qed777"
}
```

It builds!



---

archive/issue_comments_071865.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-04T16:00:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8167#issuecomment-71865",
    "user": "@jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071866.json:
```json
{
    "body": "Builds for me, too -- if I install sagenb-0.7.3, building the PDF documentation fails before the patch, succeeds afterward.",
    "created_at": "2010-02-04T16:00:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8167#issuecomment-71866",
    "user": "@jhpalmieri"
}
```

Builds for me, too -- if I install sagenb-0.7.3, building the PDF documentation fails before the patch, succeeds afterward.



---

archive/issue_comments_071867.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-05T00:36:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8167",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8167#issuecomment-71867",
    "user": "@qed777"
}
```

Resolution: fixed
