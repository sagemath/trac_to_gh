# Issue 6715: spell-check all modules under sage/logic

archive/issues_006715.json:
```json
{
    "body": "Assignee: tba\n\nAs the subject says.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6715\n\n",
    "created_at": "2009-08-09T16:09:50Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "spell-check all modules under sage/logic",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6715",
    "user": "mvngu"
}
```
Assignee: tba

As the subject says.

Issue created by migration from https://trac.sagemath.org/ticket/6715





---

archive/issue_comments_055114.json:
```json
{
    "body": "Attachment [trac_6715-unix-endlines.patch](tarball://root/attachments/some-uuid/ticket6715/trac_6715-unix-endlines.patch) by mvngu created at 2009-08-09 16:28:19\n\nbased on Sage 4.1.1.rc2",
    "created_at": "2009-08-09T16:28:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6715#issuecomment-55114",
    "user": "mvngu"
}
```

Attachment [trac_6715-unix-endlines.patch](tarball://root/attachments/some-uuid/ticket6715/trac_6715-unix-endlines.patch) by mvngu created at 2009-08-09 16:28:19

based on Sage 4.1.1.rc2



---

archive/issue_comments_055115.json:
```json
{
    "body": "Patches should be applied in this order:\n1. `trac_6715-unix-endlines.patch` --- Most files under the directory `sage/logic` are in the DOS text file format. This patch converts all such files to the Unix text file format.\n2. `trac_6715-spell-check-logic.patch` --- This patch spell-checks all modules under `sage/logic`.",
    "created_at": "2009-08-09T16:42:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6715#issuecomment-55115",
    "user": "mvngu"
}
```

Patches should be applied in this order:
1. `trac_6715-unix-endlines.patch` --- Most files under the directory `sage/logic` are in the DOS text file format. This patch converts all such files to the Unix text file format.
2. `trac_6715-spell-check-logic.patch` --- This patch spell-checks all modules under `sage/logic`.



---

archive/issue_comments_055116.json:
```json
{
    "body": "based on Sage 4.1.1.rc2",
    "created_at": "2009-08-11T12:23:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6715#issuecomment-55116",
    "user": "mvngu"
}
```

based on Sage 4.1.1.rc2



---

archive/issue_comments_055117.json:
```json
{
    "body": "Attachment [trac_6715-spell-check-logic.patch](tarball://root/attachments/some-uuid/ticket6715/trac_6715-spell-check-logic.patch) by schilly created at 2009-08-14 10:18:39\n\nlooks good, only comments and doc-lines touched, no code or doctests.\n\nthere is just a \"newline missing\" note from mercurial at the bottom of the first part of the first patch. i think it is still ok, though (line 123 in sage/logic/booleval.py, first patch).",
    "created_at": "2009-08-14T10:18:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6715#issuecomment-55117",
    "user": "schilly"
}
```

Attachment [trac_6715-spell-check-logic.patch](tarball://root/attachments/some-uuid/ticket6715/trac_6715-spell-check-logic.patch) by schilly created at 2009-08-14 10:18:39

looks good, only comments and doc-lines touched, no code or doctests.

there is just a "newline missing" note from mercurial at the bottom of the first part of the first patch. i think it is still ok, though (line 123 in sage/logic/booleval.py, first patch).



---

archive/issue_comments_055118.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-14T10:42:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6715#issuecomment-55118",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_055119.json:
```json
{
    "body": "Merged both patches.",
    "created_at": "2009-08-14T10:42:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6715#issuecomment-55119",
    "user": "mvngu"
}
```

Merged both patches.
