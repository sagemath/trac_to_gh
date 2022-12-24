# Issue 9764: matrix2.pyx: replace "x < 1e-15" by "abs(x) < 1e-15"

archive/issues_009764.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nIn matrix2.pyx, there is a doctest (line 6406):\n\n```\n            sage: all(imag(e) < 1.1e-15 for e in eigs)\n```\n\nWe should replace \"imag(e)\" by \"abs(imag(e))\".\n\nThe attached patch depends on #9760.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9765\n\n",
    "created_at": "2010-08-18T22:14:49Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "matrix2.pyx: replace \"x < 1e-15\" by \"abs(x) < 1e-15\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9764",
    "user": "jhpalmieri"
}
```
Assignee: AlexGhitza

In matrix2.pyx, there is a doctest (line 6406):

```
            sage: all(imag(e) < 1.1e-15 for e in eigs)
```

We should replace "imag(e)" by "abs(imag(e))".

The attached patch depends on #9760.


Issue created by migration from https://trac.sagemath.org/ticket/9765





---

archive/issue_comments_095662.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-18T22:16:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9764#issuecomment-95662",
    "user": "jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_095663.json:
```json
{
    "body": "Attachment [trac_9765-matrix2-abs.patch](tarball://root/attachments/some-uuid/ticket9765/trac_9765-matrix2-abs.patch) by jhpalmieri created at 2010-08-18 22:16:48",
    "created_at": "2010-08-18T22:16:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9764#issuecomment-95663",
    "user": "jhpalmieri"
}
```

Attachment [trac_9765-matrix2-abs.patch](tarball://root/attachments/some-uuid/ticket9765/trac_9765-matrix2-abs.patch) by jhpalmieri created at 2010-08-18 22:16:48



---

archive/issue_comments_095664.json:
```json
{
    "body": "The test still passes on bsd, redhawk, sage, and t2.math.",
    "created_at": "2010-08-23T01:16:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9764#issuecomment-95664",
    "user": "mpatel"
}
```

The test still passes on bsd, redhawk, sage, and t2.math.



---

archive/issue_comments_095665.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-23T01:16:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9764#issuecomment-95665",
    "user": "mpatel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095666.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-08-23T22:17:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9764#issuecomment-95666",
    "user": "mpatel"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_095667.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-24T02:48:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9764",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9764#issuecomment-95667",
    "user": "mpatel"
}
```

Resolution: fixed
