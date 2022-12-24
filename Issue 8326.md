# Issue 8326: Sphinx warnings about posets and poset_example

archive/issues_008326.json:
```json
{
    "body": "Assignee: sage-combinat\n\nSphinx warnings from building the HTML reference manual include: \n\n```\ncombinat/posets/poset_examples.rst:6: (WARNING/2) error while formatting signature for sage.combinat.posets.poset_examples.random: arg is not a module, class, method, function, traceback, frame, or code object\ncombinat/posets/posets.rst:6: (WARNING/2) error while formatting signature for sage.combinat.posets.posets.random: arg is not a module, class, method, function, traceback, frame, or code object\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8326\n\n",
    "created_at": "2010-02-22T06:06:02Z",
    "labels": [
        "combinatorics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Sphinx warnings about posets and poset_example",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8326",
    "user": "mpatel"
}
```
Assignee: sage-combinat

Sphinx warnings from building the HTML reference manual include: 

```
combinat/posets/poset_examples.rst:6: (WARNING/2) error while formatting signature for sage.combinat.posets.poset_examples.random: arg is not a module, class, method, function, traceback, frame, or code object
combinat/posets/posets.rst:6: (WARNING/2) error while formatting signature for sage.combinat.posets.posets.random: arg is not a module, class, method, function, traceback, frame, or code object
```


Issue created by migration from https://trac.sagemath.org/ticket/8326





---

archive/issue_comments_073920.json:
```json
{
    "body": "Work around Sphinx poset warnings.  sage repo.",
    "created_at": "2010-02-22T06:07:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8326#issuecomment-73920",
    "user": "mpatel"
}
```

Work around Sphinx poset warnings.  sage repo.



---

archive/issue_comments_073921.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-22T06:12:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8326#issuecomment-73921",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073922.json:
```json
{
    "body": "Changing priority from minor to trivial.",
    "created_at": "2010-02-22T06:12:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8326#issuecomment-73922",
    "user": "mpatel"
}
```

Changing priority from minor to trivial.



---

archive/issue_comments_073923.json:
```json
{
    "body": "Attachment [trac_8326-sphinx_posets.patch](tarball://root/attachments/some-uuid/ticket8326/trac_8326-sphinx_posets.patch) by mpatel created at 2010-02-22 06:12:19\n\nThe patch appears to work, but feel free to reject it.",
    "created_at": "2010-02-22T06:12:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8326#issuecomment-73923",
    "user": "mpatel"
}
```

Attachment [trac_8326-sphinx_posets.patch](tarball://root/attachments/some-uuid/ticket8326/trac_8326-sphinx_posets.patch) by mpatel created at 2010-02-22 06:12:19

The patch appears to work, but feel free to reject it.



---

archive/issue_comments_073924.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-24T23:25:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8326#issuecomment-73924",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073925.json:
```json
{
    "body": "Looks okay to me: the patch is pretty innocuous, and it fixes the docbuild problem.",
    "created_at": "2010-02-24T23:25:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8326#issuecomment-73925",
    "user": "jhpalmieri"
}
```

Looks okay to me: the patch is pretty innocuous, and it fixes the docbuild problem.



---

archive/issue_comments_073926.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-02T21:47:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8326#issuecomment-73926",
    "user": "mvngu"
}
```

Resolution: fixed
