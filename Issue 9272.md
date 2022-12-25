# Issue 9272: make -only-optional=... case-insensitive

archive/issues_009272.json:
```json
{
    "body": "Assignee: mvngu\n\nSome doctests in sage/homology/tests.py are marked `# optional - CHomP` (or they should be marked this way: see #9270 and #9271).  Running `sage -t -only-optional=chomp tests.py` runs those tests, but running `sage -t -only-optional=CHomP tests.py` does not.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9272\n\n",
    "created_at": "2010-06-19T02:54:35Z",
    "labels": [
        "component: doctest coverage",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "make -only-optional=... case-insensitive",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9272",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: mvngu

Some doctests in sage/homology/tests.py are marked `# optional - CHomP` (or they should be marked this way: see #9270 and #9271).  Running `sage -t -only-optional=chomp tests.py` runs those tests, but running `sage -t -only-optional=CHomP tests.py` does not.


Issue created by migration from https://trac.sagemath.org/ticket/9272





---

archive/issue_comments_087187.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-19T03:02:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9272#issuecomment-87187",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087188.json:
```json
{
    "body": "Here's a patch for the scripts repo.  During parsing, the line being doctested gets converted to lower-case (line 245 in sage-doctest), but the arguments for \"-only-optional\" were not being converted.  The patch fixes this.",
    "created_at": "2010-06-19T03:02:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9272#issuecomment-87188",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a patch for the scripts repo.  During parsing, the line being doctested gets converted to lower-case (line 245 in sage-doctest), but the arguments for "-only-optional" were not being converted.  The patch fixes this.



---

archive/issue_comments_087189.json:
```json
{
    "body": "scripts repo",
    "created_at": "2010-06-19T03:02:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9272#issuecomment-87189",
    "user": "https://github.com/jhpalmieri"
}
```

scripts repo



---

archive/issue_comments_087190.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-20T22:55:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9272#issuecomment-87190",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087191.json:
```json
{
    "body": "Attachment [trac_9272-only-optional-case-insensitive.patch](tarball://root/attachments/some-uuid/ticket9272/trac_9272-only-optional-case-insensitive.patch) by @rlmill created at 2010-06-20 22:55:27\n\nLooks good to me!",
    "created_at": "2010-06-20T22:55:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9272#issuecomment-87191",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_9272-only-optional-case-insensitive.patch](tarball://root/attachments/some-uuid/ticket9272/trac_9272-only-optional-case-insensitive.patch) by @rlmill created at 2010-06-20 22:55:27

Looks good to me!



---

archive/issue_comments_087192.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-25T15:43:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9272#issuecomment-87192",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
