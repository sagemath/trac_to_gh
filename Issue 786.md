# Issue 786: standard smith normal form

archive/issues_000786.json:
```json
{
    "body": "Assignee: syazdani\n\nKeywords: smith_form\n\nThe smith_form function for integer dense matrices are printed backward from the usual notation. This is because pari prints them backward.\n\nThe enclosed patch fixes this problem, by permuting the entries appropriately.\n\nIssue created by migration from https://trac.sagemath.org/ticket/786\n\n",
    "created_at": "2007-10-02T13:38:17Z",
    "labels": [
        "linear algebra",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.6",
    "title": "standard smith normal form",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/786",
    "user": "syazdani"
}
```
Assignee: syazdani

Keywords: smith_form

The smith_form function for integer dense matrices are printed backward from the usual notation. This is because pari prints them backward.

The enclosed patch fixes this problem, by permuting the entries appropriately.

Issue created by migration from https://trac.sagemath.org/ticket/786





---

archive/issue_comments_004711.json:
```json
{
    "body": "Attachment [matrix_integer_dense.pyx.hg](tarball://root/attachments/some-uuid/ticket786/matrix_integer_dense.pyx.hg) by syazdani created at 2007-10-02 18:13:52\n\nThe previous attachement was filled with all sorts of other changes. This should only be one function added to integer_dense function.",
    "created_at": "2007-10-02T18:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/786#issuecomment-4711",
    "user": "syazdani"
}
```

Attachment [matrix_integer_dense.pyx.hg](tarball://root/attachments/some-uuid/ticket786/matrix_integer_dense.pyx.hg) by syazdani created at 2007-10-02 18:13:52

The previous attachement was filled with all sorts of other changes. This should only be one function added to integer_dense function.



---

archive/issue_comments_004712.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-04T18:57:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/786",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/786#issuecomment-4712",
    "user": "was"
}
```

Resolution: fixed
