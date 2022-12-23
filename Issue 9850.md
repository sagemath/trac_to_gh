# Issue 9850: sage -pkg may hang if there are many uncommitted changes in the package

archive/issues_009850.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  mpatel\n\nKeywords: sage-pkg, stderr hangs\n\nAt [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/c008a74ae2b3af95), I reported the following problem.\n\n- Take a folder with many uncommitted changes in a Mercurial repository. [Example](http://www.google.com/url?sa=D&q=http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-2.1.alpha0.tar.gz&usg=AFQjCNE362g2kL77GzI-7T5RaOBx92X0KQ).\n- Run `sage -pkg` on it.\n- It will hang forever while it is attempted to read from `stderr` of a subprocess.\n\nMitesh Patel pointed to the solution: One should use `communicate` rather than stdout/stdin/stderr!\n\nI don't know how to doctest the issue; but I have a patch that solves the problem.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9851\n\n",
    "created_at": "2010-09-03T09:51:51Z",
    "labels": [
        "packages: standard",
        "minor",
        "bug"
    ],
    "title": "sage -pkg may hang if there are many uncommitted changes in the package",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9850",
    "user": "SimonKing"
}
```
Assignee: tbd

CC:  mpatel

Keywords: sage-pkg, stderr hangs

At [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/c008a74ae2b3af95), I reported the following problem.

- Take a folder with many uncommitted changes in a Mercurial repository. [Example](http://www.google.com/url?sa=D&q=http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-2.1.alpha0.tar.gz&usg=AFQjCNE362g2kL77GzI-7T5RaOBx92X0KQ).
- Run `sage -pkg` on it.
- It will hang forever while it is attempted to read from `stderr` of a subprocess.

Mitesh Patel pointed to the solution: One should use `communicate` rather than stdout/stdin/stderr!

I don't know how to doctest the issue; but I have a patch that solves the problem.

Issue created by migration from https://trac.sagemath.org/ticket/9851





---

archive/issue_comments_097228.json:
```json
{
    "body": "Replace p.stderr.read()/p.stdout.read() by p.communicate() in the sage-pkg script",
    "created_at": "2010-09-03T09:55:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9850#issuecomment-97228",
    "user": "SimonKing"
}
```

Replace p.stderr.read()/p.stdout.read() by p.communicate() in the sage-pkg script



---

archive/issue_comments_097229.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-03T09:57:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9850#issuecomment-97229",
    "user": "SimonKing"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097230.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-09-03T09:57:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9850#issuecomment-97230",
    "user": "SimonKing"
}
```

Attachment



---

archive/issue_comments_097231.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-03T23:07:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9850#issuecomment-97231",
    "user": "mpatel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097232.json:
```json
{
    "body": "Thanks for tracking this down and fixing it!",
    "created_at": "2010-09-03T23:07:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9850#issuecomment-97232",
    "user": "mpatel"
}
```

Thanks for tracking this down and fixing it!



---

archive/issue_comments_097233.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T11:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9850#issuecomment-97233",
    "user": "mpatel"
}
```

Resolution: fixed
